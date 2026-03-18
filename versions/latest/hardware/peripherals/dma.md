---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/dma.html
original_path: hardware/peripherals/dma.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Direct Memory Access (DMA)

## Overview

Direct Memory Access (Controller) is a commonly provided type of co-processor that can typically
offload transferring data to and from peripherals and memory.

The DMA API is not a portable API and really cannot be as each DMA has unique memory requirements,
peripheral interactions, and features. The API in effect provides a union of all useful DMA
functionality drivers have needed in the tree. It can still be a good abstraction, with care, for
peripheral devices for vendors where the DMA IP might be very similar but have slight variances.

## Driver Implementation Expectations

### Synchronization and Ownership

From an API point of view, a DMA channel is a single-owner object, meaning the drivers should not
attempt to wrap a channel with kernel synchronization primitives such as mutexes or semaphores. If
DMA channels require mutating shared registers, those register updates should be wrapped in a spin
lock.

This enables the entire API to be low-cost and callable from any call context, including ISRs where
it may be very useful to start/stop/suspend/resume/reload a channel transfer.

### Transfer Descriptor Memory Management

Drivers should not attempt to use heap allocations of any kind. If object pools are needed for
transfer descriptors then those should be setup in a way that does not break the promise of
ISR-allowable calls. Many drivers choose to create a simple static descriptor array per channel with
the size of the descriptor array adjustable using Kconfig.

### Channel State Machine Expectations

DMA channels should be viewed as state machines that the DMA API provides transition events for in
the form of API calls. Every driver is expected to maintain its own channel state tracking. The busy
state of the channel should be inspectable at any time with [`dma_get_status()`](#c.dma_get_status).

A diagram showing those expectated possible state transitions and their API calls is provided here
for reference.

digraph {
node [style=rounded];
edge [fontname=Courier];
init [shape=point];
CONFIGURED [label=Configured,shape=box];
RUNNING [label=Running,shape=box];
SUSPENDED [label=Suspended,shape=box];
init -> CONFIGURED [label=dma\_config];
CONFIGURED -> RUNNING [label=dma\_start];
CONFIGURED -> CONFIGURED [label=dma\_stop];
RUNNING -> CONFIGURED [label=dma\_stop];
RUNNING -> RUNNING [label=dma\_start];
RUNNING -> RUNNING [label=dma\_resume, headport=w];
RUNNING -> SUSPENDED [label=dma\_suspend];
SUSPENDED -> SUSPENDED [label=dma\_suspend];
SUSPENDED -> RUNNING [label=dma\_resume];
SUSPENDED -> CONFIGURED [label=dma\_stop];
}

DMA state finite state machine

## API Reference

*group* dma\_interface
:   DMA Interface.

    Defines

    DMA\_STATUS\_COMPLETE
    :   The DMA callback event has occurred at the completion of a transfer list.

    DMA\_STATUS\_BLOCK
    :   The DMA callback has occurred at the completion of a single transfer block in a transfer list.

    DMA\_MAGIC
    :   Magic code to identify context content.

    DMA\_BUF\_ADDR\_ALIGNMENT(node)
    :   Get the device tree property describing the buffer address alignment.

        Useful when statically defining or allocating buffers for DMA usage where memory alignment often matters.

        Parameters:
        :   - **node** – Node identifier, e.g. [DT\_NODELABEL(dma\_0)](../../build/dts/api/api.md#group__devicetree-generic-id_1gab7d23294a6bf7fd44a98b48ec47d8a79)

        Returns:
        :   alignment Memory byte alignment required for DMA buffers

    DMA\_BUF\_SIZE\_ALIGNMENT(node)
    :   Get the device tree property describing the buffer size alignment.

        Useful when statically defining or allocating buffers for DMA usage where memory alignment often matters.

        Parameters:
        :   - **node** – Node identifier, e.g. [DT\_NODELABEL(dma\_0)](../../build/dts/api/api.md#group__devicetree-generic-id_1gab7d23294a6bf7fd44a98b48ec47d8a79)

        Returns:
        :   alignment Memory byte alignment required for DMA buffers

    DMA\_COPY\_ALIGNMENT(node)
    :   Get the device tree property describing the minimal chunk of data possible to be copied.

        Parameters:
        :   - **node** – Node identifier, e.g. [DT\_NODELABEL(dma\_0)](../../build/dts/api/api.md#group__devicetree-generic-id_1gab7d23294a6bf7fd44a98b48ec47d8a79)

        Returns:
        :   minimal Minimal chunk of data possible to be copied

    Typedefs

    typedef void (\*dma\_callback\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, void \*user\_data, uint32\_t channel, int status)
    :   Callback function for DMA transfer completion.

        If enabled, callback function will be invoked at transfer or block completion, or when an error happens. In circular mode, `status` indicates that the DMA device has reached either the end of the buffer (DMA\_STATUS\_COMPLETE) or a water mark (DMA\_STATUS\_BLOCK).

        Param dev:
        :   Pointer to the DMA device calling the callback.

        Param user\_data:
        :   A pointer to some user data or NULL

        Param channel:
        :   The channel number

        Param status:
        :   Status of the transfer

            - DMA\_STATUS\_COMPLETE buffer fully consumed
            - DMA\_STATUS\_BLOCK buffer consumption reached a configured block or water mark
            - A negative errno otherwise

    Enums

    enum dma\_channel\_direction
    :   DMA channel direction.

        *Values:*

        enumerator MEMORY\_TO\_MEMORY = 0x0
        :   Memory to memory.

        enumerator MEMORY\_TO\_PERIPHERAL
        :   Memory to peripheral.

        enumerator PERIPHERAL\_TO\_MEMORY
        :   Peripheral to memory.

        enumerator PERIPHERAL\_TO\_PERIPHERAL
        :   Peripheral to peripheral.

        enumerator HOST\_TO\_MEMORY
        :   Host to memory.

        enumerator MEMORY\_TO\_HOST
        :   Memory to host.

        enumerator DMA\_CHANNEL\_DIRECTION\_COMMON\_COUNT
        :   Number of all common channel directions.

        enumerator DMA\_CHANNEL\_DIRECTION\_PRIV\_START = [DMA\_CHANNEL\_DIRECTION\_COMMON\_COUNT](#c.dma_channel_direction.DMA_CHANNEL_DIRECTION_COMMON_COUNT)
        :   This and higher values are dma controller or soc specific.

            Refer to the specified dma driver header file.

        enumerator DMA\_CHANNEL\_DIRECTION\_MAX = 0x7
        :   Maximum allowed value (3 bit field!).

    enum dma\_addr\_adj
    :   DMA address adjustment.

        Valid values for *source\_addr\_adj* and *dest\_addr\_adj*

        *Values:*

        enumerator DMA\_ADDR\_ADJ\_INCREMENT
        :   Increment the address.

        enumerator DMA\_ADDR\_ADJ\_DECREMENT
        :   Decrement the address.

        enumerator DMA\_ADDR\_ADJ\_NO\_CHANGE
        :   No change the address.

    enum dma\_channel\_filter
    :   DMA channel attributes.

        *Values:*

        enumerator DMA\_CHANNEL\_NORMAL

        enumerator DMA\_CHANNEL\_PERIODIC

    enum dma\_attribute\_type
    :   DMA attributes.

        *Values:*

        enumerator DMA\_ATTR\_BUFFER\_ADDRESS\_ALIGNMENT

        enumerator DMA\_ATTR\_BUFFER\_SIZE\_ALIGNMENT

        enumerator DMA\_ATTR\_COPY\_ALIGNMENT

        enumerator DMA\_ATTR\_MAX\_BLOCK\_COUNT

    Functions

    static inline int dma\_config(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel, struct [dma\_config](#c.dma_config) \*config)
    :   Configure individual channel for DMA transfer.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **channel** – Numeric identification of the channel to configure
            - **config** – Data structure containing the intended configuration for the selected channel

        Return values:
        :   - **0** – if successful.
            - **Negative** – errno code if failure.

    static inline int dma\_reload(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel, uint32\_t src, uint32\_t dst, size\_t size)
    :   Reload buffer(s) for a DMA channel.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **channel** – Numeric identification of the channel to configure selected channel
            - **src** – source address for the DMA transfer
            - **dst** – destination address for the DMA transfer
            - **size** – size of DMA transfer

        Return values:
        :   - **0** – if successful.
            - **Negative** – errno code if failure.

    int dma\_start(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel)
    :   Enables DMA channel and starts the transfer, the channel must be configured beforehand.

        Implementations must check the validity of the channel ID passed in and return -EINVAL if it is invalid.

        Start is allowed on channels that have already been started and must report success.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **channel** – Numeric identification of the channel where the transfer will be processed

        Return values:
        :   - **0** – if successful.
            - **Negative** – errno code if failure.

    int dma\_stop(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel)
    :   Stops the DMA transfer and disables the channel.

        Implementations must check the validity of the channel ID passed in and return -EINVAL if it is invalid.

        Stop is allowed on channels that have already been stopped and must report success.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **channel** – Numeric identification of the channel where the transfer was being processed

        Return values:
        :   - **0** – if successful.
            - **Negative** – errno code if failure.

    int dma\_suspend(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel)
    :   Suspend a DMA channel transfer.

        Implementations must check the validity of the channel state and ID passed in and return -EINVAL if either are invalid.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **channel** – Numeric identification of the channel to suspend

        Return values:
        :   - **0** – If successful.
            - **-ENOSYS** – If not implemented.
            - **-EINVAL** – If invalid channel id or state.
            - **-errno** – Other negative errno code failure.

    int dma\_resume(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel)
    :   Resume a DMA channel transfer.

        Implementations must check the validity of the channel state and ID passed in and return -EINVAL if either are invalid.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **channel** – Numeric identification of the channel to resume

        Return values:
        :   - **0** – If successful.
            - **-ENOSYS** – If not implemented
            - **-EINVAL** – If invalid channel id or state.
            - **-errno** – Other negative errno code failure.

    int dma\_request\_channel(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, void \*filter\_param)
    :   request DMA channel.

        request DMA channel resources return -EINVAL if there is no valid channel available.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **filter\_param** – filter function parameter

        Return values:
        :   - **dma** – channel if successful.
            - **Negative** – errno code if failure.

    void dma\_release\_channel(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel)
    :   release DMA channel.

        release DMA channel resources

        **Function properties (list may not be complete)**
        :   [isr-ok](../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **channel** – channel number

    int dma\_chan\_filter(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, int channel, void \*filter\_param)
    :   DMA channel filter.

        filter channel by attribute

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **channel** – channel number
            - **filter\_param** – filter attribute

        Return values:
        :   **Negative** – errno code if not support

    static inline int dma\_get\_status(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel, struct [dma\_status](#c.dma_status) \*stat)
    :   get current runtime status of DMA transfer

        Implementations must check the validity of the channel ID passed in and return -EINVAL if it is invalid or -ENOSYS if not supported.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **channel** – Numeric identification of the channel where the transfer was being processed
            - **stat** – a non-NULL [dma\_status](#structdma__status) object for storing DMA status

        Return values:
        :   - **non-negative** – if successful.
            - **Negative** – errno code if failure.

    static inline int dma\_get\_attribute(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t type, uint32\_t \*value)
    :   get attribute of a dma controller

        This function allows to get a device specific static or runtime attribute like required address and size alignment of a buffer. Implementations must check the validity of the type passed in and return -EINVAL if it is invalid or -ENOSYS if not supported.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **type** – Numeric identification of the attribute
            - **value** – A non-NULL pointer to the variable where the read value is to be placed

        Return values:
        :   - **non-negative** – if successful.
            - **Negative** – errno code if failure.

    static inline uint32\_t dma\_width\_index(uint32\_t size)
    :   Look-up generic width index to be used in registers.

        Warning

        This look-up works for most controllers, but *may* not work for yours. Ensure your controller expects the most common register bit values before using this convenience function. If your controller does not support these values, you will have to write your own look-up inside the controller driver.

        Parameters:
        :   - **size** – width of bus (in bytes)

        Return values:
        :   **common** – DMA index to be placed into registers.

    static inline uint32\_t dma\_burst\_index(uint32\_t burst)
    :   Look-up generic burst index to be used in registers.

        Warning

        This look-up works for most controllers, but *may* not work for yours. Ensure your controller expects the most common register bit values before using this convenience function. If your controller does not support these values, you will have to write your own look-up inside the controller driver.

        Parameters:
        :   - **burst** – number of bytes to be sent in a single burst

        Return values:
        :   **common** – DMA index to be placed into registers.

    struct dma\_block\_config
    :   *#include <dma.h>*

        DMA block configuration structure.

        Aside from source address, destination address, and block size many of these options are hardware and driver dependent.

        Public Members

        uint32\_t source\_address
        :   block starting address at source

        uint32\_t dest\_address
        :   block starting address at destination

        uint32\_t source\_gather\_interval
        :   Address adjustment at gather boundary.

        uint32\_t dest\_scatter\_interval
        :   Address adjustment at scatter boundary.

        uint16\_t dest\_scatter\_count
        :   Continuous transfer count between scatter boundaries.

        uint16\_t source\_gather\_count
        :   Continuous transfer count between gather boundaries.

        uint32\_t block\_size
        :   Number of bytes to be transferred for this block.

        struct [dma\_block\_config](#c.dma_block_config) \*next\_block
        :   Pointer to next block in a transfer list.

        uint16\_t source\_gather\_en
        :   Enable source gathering when set to 1.

        uint16\_t dest\_scatter\_en
        :   Enable destination scattering when set to 1.

        uint16\_t source\_addr\_adj
        :   Source address adjustment option.

            - 0b00 increment
            - 0b01 decrement
            - 0b10 no change

        uint16\_t dest\_addr\_adj
        :   Destination address adjustment.

            - 0b00 increment
            - 0b01 decrement
            - 0b10 no change

        uint16\_t source\_reload\_en
        :   Reload source address at the end of block transfer.

        uint16\_t dest\_reload\_en
        :   Reload destination address at the end of block transfer.

        uint16\_t fifo\_mode\_control
        :   FIFO fill before starting transfer, HW specific meaning.

        uint16\_t flow\_control\_mode
        :   Transfer flow control mode.

            - 0b0 source request service upon data availability
            - 0b1 source request postponed until destination request happens

    struct dma\_config
    :   *#include <dma.h>*

        DMA configuration structure.

        Public Members

        uint32\_t dma\_slot
        :   Which peripheral and direction, HW specific.

        uint32\_t channel\_direction
        :   Direction the transfers are occurring.

            - 0b000 memory to memory,
            - 0b001 memory to peripheral,
            - 0b010 peripheral to memory,
            - 0b011 peripheral to peripheral,
            - 0b100 host to memory
            - 0b101 memory to host
            - others hardware specific

        uint32\_t complete\_callback\_en
        :   Completion callback enable.

            - 0b0 callback invoked at transfer list completion only
            - 0b1 callback invoked at completion of each block

        uint32\_t error\_callback\_en
        :   Error callback enable.

            - 0b0 error callback enabled
            - 0b1 error callback disabled

        uint32\_t source\_handshake
        :   Source handshake, HW specific.

            - 0b0 HW
            - 0b1 SW

        uint32\_t dest\_handshake
        :   Destination handshake, HW specific.

            - 0b0 HW
            - 0b1 SW

        uint32\_t channel\_priority
        :   Channel priority for arbitration, HW specific.

        uint32\_t source\_chaining\_en
        :   Source chaining enable, HW specific.

        uint32\_t dest\_chaining\_en
        :   Destination chaining enable, HW specific.

        uint32\_t linked\_channel
        :   Linked channel, HW specific.

        uint32\_t cyclic
        :   Cyclic transfer list, HW specific.

        uint32\_t source\_data\_size
        :   Width of source data (in bytes).

        uint32\_t dest\_data\_size
        :   Width of destination data (in bytes).

        uint32\_t source\_burst\_length
        :   Source burst length in bytes.

        uint32\_t dest\_burst\_length
        :   Destination burst length in bytes.

        uint32\_t block\_count
        :   Number of blocks in transfer list.

        struct [dma\_block\_config](#c.dma_block_config) \*head\_block
        :   Pointer to the first block in the transfer list.

        void \*user\_data
        :   Optional attached user data for callbacks.

        [dma\_callback\_t](#c.dma_callback_t) dma\_callback
        :   Optional callback for completion and error events.

    struct dma\_status
    :   *#include <dma.h>*

        DMA runtime status structure.

        Public Members

        bool busy
        :   Is the current DMA transfer busy or idle.

        enum [dma\_channel\_direction](#c.dma_channel_direction) dir
        :   Direction fo the transfer.

        uint32\_t pending\_length
        :   Pending length to be transferred in bytes, HW specific.

        uint32\_t free
        :   Available buffers space, HW specific.

        uint32\_t write\_position
        :   Write position in circular DMA buffer, HW specific.

        uint32\_t read\_position
        :   Read position in circular DMA buffer, HW specific.

        uint64\_t total\_copied
        :   Total copied, HW specific.

    struct dma\_context
    :   *#include <dma.h>*

        DMA context structure Note: the [dma\_context](#structdma__context) shall be the first member of DMA client driver Data, got by dev->data.

        Public Members

        int32\_t magic
        :   magic code to identify the context

        int dma\_channels
        :   number of dma channels

        atomic\_t \*atomic
        :   atomic holding bit flags for each channel to mark as used/unused
