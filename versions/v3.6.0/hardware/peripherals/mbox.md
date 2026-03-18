---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/mbox.html
original_path: hardware/peripherals/mbox.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Multi-Channel Inter-Processor Mailbox (MBOX)

## Overview

An MBOX device is a peripheral capable of passing signals (and data depending
on the peripheral) between CPUs and clusters in the system. Each MBOX instance
is providing one or more channels, each one targeting one other CPU cluster
(multiple channels can target the same cluster).

## API Reference

Related code samples

[MBOX](../../samples/drivers/mbox/README.md#mbox "Perform inter-processor mailbox communication using the MBOX API.")
:   Perform inter-processor mailbox communication using the MBOX API.

[MBOX Data](../../samples/drivers/mbox_data/README.md#mbox_data "Perform inter-processor mailbox communication using the MBOX API with data.")
:   Perform inter-processor mailbox communication using the MBOX API with data.

*group* mbox\_interface
:   MBOX Interface.

    ```text
                         CPU #1        |
    +----------+                       |        +----------+
    |          +---TX9----+   +--------+--RX8---+          |
    |  dev A   |          |   |        |        |  CPU #2  |
    |          <---RX8--+ |   | +------+--TX9--->          |
    +----------+        | |   | |      |        +----------+
                     +--+-v---v-+--+   |
                     |             |   |
                     |   MBOX dev  |   |
                     |             |   |
                     +--+-^---^--+-+   |
    +----------+        | |   |  |     |        +----------+
    |          <---RX2--+ |   |  +-----+--TX3--->          |
    |  dev B   |          |   |        |        |  CPU #3  |
    |          +---TX3----+   +--------+--RX2---+          |
    +----------+                       |        +----------+
                                       |
    ```

    An MBOX device is a peripheral capable of passing signals (and data depending on the peripheral) between CPUs and clusters in the system. Each MBOX instance is providing one or more channels, each one targeting one other CPU cluster (multiple channels can target the same cluster).

    For example in the plot the device ‘dev A’ is using the TX channel 9 to signal (or send data to) the CPU #2 and it’s expecting data or signals on the RX channel 8. Thus it can send the message through the channel 9, and it can register a callback on the channel 8 of the MBOX device.

    This API supports two modes: signalling mode and data transfer mode.

    In signalling mode:

    - [mbox\_mtu\_get()](#group__mbox__interface_1ga82d9def1b5c31c574d2114abcce2eb1f) must return 0
    - [mbox\_send()](#group__mbox__interface_1ga18828e5c28201ad838ed9ba7c0afabfe) must have (msg == NULL)
    - the callback must be called with (data == NULL)

    In data transfer mode:

    - [mbox\_mtu\_get()](#group__mbox__interface_1ga82d9def1b5c31c574d2114abcce2eb1f) must return a (value != 0)
    - [mbox\_send()](#group__mbox__interface_1ga18828e5c28201ad838ed9ba7c0afabfe) must have (msg != NULL)
    - the callback must be called with (data != NULL)
    - The msg content must be the same between sender and receiver

    Defines

    MBOX\_DT\_CHANNEL\_GET(node\_id, name)
    :   Structure initializer for [mbox\_channel](#structmbox__channel) from devicetree.

        This helper macro expands to a static initializer for a `[mbox_channel](#structmbox__channel)` by reading the relevant device controller and channel number from the devicetree.

        Example devicetree fragment:

        ```text
        mbox1: mbox-controller@... { ... };

        n: node {
                mboxes = <&mbox1 8>,
                         <&mbox1 9>;
                mbox-names = "tx", "rx";
        };
        ```

        Example usage:

        ```text
        const struct mbox_channel channel = MBOX_DT_CHANNEL_GET(DT_NODELABEL(n), tx);
        ```

        Parameters:
        :   - **node\_id** – Devicetree node identifier for the MBOX device
            - **name** – lowercase-and-underscores name of the mboxes element

    Typedefs

    typedef void (\*mbox\_callback\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel, void \*user\_data, struct [mbox\_msg](#c.mbox_msg) \*data)
    :   Callback API for incoming MBOX messages.

        These callbacks execute in interrupt context. Therefore, use only interrupt-safe APIS. Registration of callbacks is done via *[mbox\_register\_callback()](#group__mbox__interface_1gad48e48c984e70348336a896bb2835c77)*

        The data parameter must be NULL in signalling mode.

        Param dev:
        :   Driver instance

        Param channel:
        :   Channel ID

        Param user\_data:
        :   Pointer to some private data provided at registration time

        Param data:
        :   Message struct

    typedef int (\*mbox\_send\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel, const struct [mbox\_msg](#c.mbox_msg) \*msg)
    :   Callback API to send MBOX messages.

        See *[mbox\_send()](#group__mbox__interface_1ga18828e5c28201ad838ed9ba7c0afabfe)* for function description

        Param dev:
        :   Driver instance

        Param channel:
        :   Channel ID

        Param msg:
        :   Message struct

        Return:
        :   See return values for *[mbox\_send()](#group__mbox__interface_1ga18828e5c28201ad838ed9ba7c0afabfe)*

    typedef int (\*mbox\_mtu\_get\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Callback API to get maximum data size.

        See *[mbox\_mtu\_get()](#group__mbox__interface_1ga82d9def1b5c31c574d2114abcce2eb1f)* for argument definitions.

    typedef int (\*mbox\_register\_callback\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel, [mbox\_callback\_t](#c.mbox_callback_t) cb, void \*user\_data)
    :   Callback API upon registration.

        See *[mbox\_register\_callback()](#group__mbox__interface_1gad48e48c984e70348336a896bb2835c77)* for function description

        Param dev:
        :   Driver instance

        Param channel:
        :   Channel ID

        Param cb:
        :   Callback function to execute on incoming message interrupts.

        Param user\_data:
        :   Application-specific data pointer which will be passed to the callback function when executed.

        Return:
        :   See return values for *[mbox\_register\_callback()](#group__mbox__interface_1gad48e48c984e70348336a896bb2835c77)*

    typedef int (\*mbox\_set\_enabled\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel, bool enable)
    :   Callback API upon enablement of interrupts.

        See *[mbox\_set\_enabled()](#group__mbox__interface_1ga563c6c0e2199b0608b2cd0606c46fc81)* for function description

        Param dev:
        :   Driver instance

        Param channel:
        :   Channel ID

        Param enable:
        :   Set to 0 to disable and to nonzero to enable.

        Return:
        :   See return values for *[mbox\_set\_enabled()](#group__mbox__interface_1ga563c6c0e2199b0608b2cd0606c46fc81)*

    typedef uint32\_t (\*mbox\_max\_channels\_get\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Callback API to get maximum number of channels.

        See *[mbox\_max\_channels\_get()](#group__mbox__interface_1gaf2f8adbd5e4f7f5972b2d34cfce68bdb)* for argument definitions.

    Functions

    static inline void mbox\_init\_channel(struct [mbox\_channel](#c.mbox_channel) \*channel, const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t ch\_id)
    :   Initialize a channel struct.

        Initialize an `[mbox_channel](#structmbox__channel)` passed by the user with a provided MBOX device and channel ID. This function is needed when the information about the device and the channel ID is not in the DT. In the DT case [MBOX\_DT\_CHANNEL\_GET()](#group__mbox__interface_1ga9e02e3a523a63ff564ce2bb42c03aa1f) must be used instead.

        Parameters:
        :   - **channel** – Pointer to the channel struct
            - **dev** – Driver instance
            - **ch\_id** – Channel ID

    int mbox\_send(const struct [mbox\_channel](#c.mbox_channel) \*channel, const struct [mbox\_msg](#c.mbox_msg) \*msg)
    :   Try to send a message over the MBOX device.

        Send a message over an `[mbox_channel](#structmbox__channel)`. The msg parameter must be NULL when the driver is used for signalling.

        If the msg parameter is not NULL, this data is expected to be delivered on the receiving side using the data parameter of the receiving callback.

        Parameters:
        :   - **channel** – Channel instance pointer
            - **msg** – Pointer to the message struct

        Return values:
        :   - **-EBUSY** – If the remote hasn’t yet read the last data sent.
            - **-EMSGSIZE** – If the supplied data size is unsupported by the driver.
            - **-EINVAL** – If there was a bad parameter, such as: too-large channel descriptor or the device isn’t an outbound MBOX channel.
            - **0** – On success, negative value on error.

    static inline int mbox\_register\_callback(const struct [mbox\_channel](#c.mbox_channel) \*channel, [mbox\_callback\_t](#c.mbox_callback_t) cb, void \*user\_data)
    :   Register a callback function on a channel for incoming messages.

        This function doesn’t assume anything concerning the status of the interrupts. Use *[mbox\_set\_enabled()](#group__mbox__interface_1ga563c6c0e2199b0608b2cd0606c46fc81)* to enable or to disable the interrupts if needed.

        Parameters:
        :   - **channel** – Channel instance pointer.
            - **cb** – Callback function to execute on incoming message interrupts.
            - **user\_data** – Application-specific data pointer which will be passed to the callback function when executed.

        Return values:
        :   **0** – On success, negative value on error.

    int mbox\_mtu\_get(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Return the maximum number of bytes possible in an outbound message.

        Returns the actual number of bytes that it is possible to send through an outgoing channel.

        This number can be 0 when the driver only supports signalling or when on the receiving side the content and size of the message must be retrieved in an indirect way (i.e. probing some other peripheral, reading memory regions, etc…).

        If this function returns 0, the msg parameter in *[mbox\_send()](#group__mbox__interface_1ga18828e5c28201ad838ed9ba7c0afabfe)* is expected to be NULL.

        Parameters:
        :   - **dev** – Driver instance pointer.

        Returns:
        :   Maximum possible size of a message in bytes, 0 for signalling, negative value on error.

    int mbox\_set\_enabled(const struct [mbox\_channel](#c.mbox_channel) \*channel, bool enable)
    :   Enable (disable) interrupts and callbacks for inbound channels.

        Enable interrupt for the channel when the parameter ‘enable’ is set to true. Disable it otherwise.

        Immediately after calling this function with ‘enable’ set to true, the channel is considered enabled and ready to receive signal and messages (even already pending), so the user must take care of installing a proper callback (if needed) using *[mbox\_register\_callback()](#group__mbox__interface_1gad48e48c984e70348336a896bb2835c77)* on the channel before enabling it. For this reason it is recommended that all the channels are disabled at probe time.

        Enabling a channel for which there is no installed callback is considered undefined behavior (in general the driver must take care of gracefully handling spurious interrupts with no installed callback).

        Parameters:
        :   - **channel** – Channel instance pointer.
            - **enable** – Set to 0 to disable and to nonzero to enable.

        Return values:
        :   - **0** – On success.
            - **-EINVAL** – If it isn’t an inbound channel.

    uint32\_t mbox\_max\_channels\_get(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Return the maximum number of channels.

        Return the maximum number of channels supported by the hardware.

        Parameters:
        :   - **dev** – Driver instance pointer.

        Returns:
        :   Maximum possible number of supported channels on success, negative value on error.

    struct mbox\_msg
    :   *#include <mbox.h>*

        Message struct (to hold data and its size).

        Public Members

        const void \*data
        :   Pointer to the data sent in the message.

        size\_t size
        :   Size of the data.

    struct mbox\_channel
    :   *#include <mbox.h>*

        Provides a type to hold an MBOX channel.

        Struct type to hold an MBOX device pointer and the channel ID.

        Public Members

        const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev
        :   MBOX device pointer.

        uint32\_t id
        :   Channel ID.

    struct mbox\_driver\_api
    :   *#include <mbox.h>*
