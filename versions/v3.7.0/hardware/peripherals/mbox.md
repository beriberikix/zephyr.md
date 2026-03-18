---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/mbox.html
original_path: hardware/peripherals/mbox.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

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

*group* MBOX Interface
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

    **Since**
    :   1.0

    **Version**
    :   0.1.0

    An MBOX device is a peripheral capable of passing signals (and data depending on the peripheral) between CPUs and clusters in the system. Each MBOX instance is providing one or more channels, each one targeting one other CPU cluster (multiple channels can target the same cluster).

    For example in the plot the device ‘dev A’ is using the TX channel 9 to signal (or send data to) the CPU #2 and it’s expecting data or signals on the RX channel 8. Thus it can send the message through the channel 9, and it can register a callback on the channel 8 of the MBOX device.

    This API supports two modes: signalling mode and data transfer mode.

    In signalling mode:

    - [mbox\_mtu\_get()](#group__mbox__interface_1ga82d9def1b5c31c574d2114abcce2eb1f) must return 0
    - [mbox\_send()](#group__mbox__interface_1gaf4d02fb3a3ed788ba28a58783209d359) must have (msg == NULL)
    - the callback must be called with (data == NULL)

    In data transfer mode:

    - [mbox\_mtu\_get()](#group__mbox__interface_1ga82d9def1b5c31c574d2114abcce2eb1f) must return a (value != 0)
    - [mbox\_send()](#group__mbox__interface_1gaf4d02fb3a3ed788ba28a58783209d359) must have (msg != NULL)
    - the callback must be called with (data != NULL)
    - The msg content must be the same between sender and receiver

    Defines

    MBOX\_DT\_SPEC\_GET(node\_id, name)
    :   Structure initializer for struct [mbox\_dt\_spec](#structmbox__dt__spec) from devicetree.

        This helper macro expands to a static initializer for a struct [mbox\_dt\_spec](#structmbox__dt__spec) by reading the relevant device controller and channel number from the devicetree.

        Example devicetree fragment:

        ```devicetree
        n: node {
                mboxes = <&mbox1 8>,
                         <&mbox1 9>;
                mbox-names = "tx", "rx";
        };
        ```

        Example usage:

        ```c
        const struct mbox_dt_spec spec = MBOX_DT_SPEC_GET(DT_NODELABEL(n), tx);
        ```

        Parameters:
        :   - **node\_id** – Devicetree node identifier for the MBOX device
            - **name** – lowercase-and-underscores name of the mboxes element

        Returns:
        :   static initializer for a struct [mbox\_dt\_spec](#structmbox__dt__spec)

    MBOX\_DT\_SPEC\_INST\_GET(inst, name)
    :   Instance version of MBOX\_DT\_CHANNEL\_GET().

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **name** – lowercase-and-underscores name of the mboxes element

        Returns:
        :   static initializer for a struct [mbox\_dt\_spec](#structmbox__dt__spec)

    Typedefs

    typedef uint32\_t mbox\_channel\_id\_t
    :   Type for MBOX channel identifiers.

    Functions

    static inline bool mbox\_is\_ready\_dt(const struct [mbox\_dt\_spec](#c.mbox_dt_spec) \*spec)
    :   Validate if MBOX device instance from a struct [mbox\_dt\_spec](#structmbox__dt__spec) is ready.

        Parameters:
        :   - **spec** – MBOX specification from devicetree

        Returns:
        :   See return values for [mbox\_send()](#group__mbox__interface_1gaf4d02fb3a3ed788ba28a58783209d359)

    int mbox\_send(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [mbox\_channel\_id\_t](#c.mbox_channel_id_t) channel\_id, const struct [mbox\_msg](#c.mbox_msg) \*msg)
    :   Try to send a message over the MBOX device.

        Send a message over an struct mbox\_channel. The msg parameter must be NULL when the driver is used for signalling.

        If the msg parameter is not NULL, this data is expected to be delivered on the receiving side using the data parameter of the receiving callback.

        Parameters:
        :   - **dev** – MBOX device instance
            - **channel\_id** – MBOX channel identifier
            - **msg** – Message

        Return values:
        :   - **0** – On success.
            - **-EBUSY** – If the remote hasn’t yet read the last data sent.
            - **-EMSGSIZE** – If the supplied data size is unsupported by the driver.
            - **-EINVAL** – If there was a bad parameter, such as: too-large channel descriptor or the device isn’t an outbound MBOX channel.

    static inline int mbox\_send\_dt(const struct [mbox\_dt\_spec](#c.mbox_dt_spec) \*spec, const struct [mbox\_msg](#c.mbox_msg) \*msg)
    :   Try to send a message over the MBOX device from a struct [mbox\_dt\_spec](#structmbox__dt__spec).

        Parameters:
        :   - **spec** – MBOX specification from devicetree
            - **msg** – Message

        Returns:
        :   See return values for [mbox\_send()](#group__mbox__interface_1gaf4d02fb3a3ed788ba28a58783209d359)

    static inline int mbox\_register\_callback(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [mbox\_channel\_id\_t](#c.mbox_channel_id_t) channel\_id, mbox\_callback\_t cb, void \*user\_data)
    :   Register a callback function on a channel for incoming messages.

        This function doesn’t assume anything concerning the status of the interrupts. Use [mbox\_set\_enabled()](#group__mbox__interface_1ga9eea4b9501751919125cd6124f9e9868) to enable or to disable the interrupts if needed.

        Parameters:
        :   - **dev** – MBOX device instance
            - **channel\_id** – MBOX channel identifier
            - **cb** – Callback function to execute on incoming message interrupts.
            - **user\_data** – Application-specific data pointer which will be passed to the callback function when executed.

        Return values:
        :   - **0** – On success.
            - **-errno** – Negative errno on error.

    static inline int mbox\_register\_callback\_dt(const struct [mbox\_dt\_spec](#c.mbox_dt_spec) \*spec, mbox\_callback\_t cb, void \*user\_data)
    :   Register a callback function on a channel for incoming messages from a struct [mbox\_dt\_spec](#structmbox__dt__spec).

        Parameters:
        :   - **spec** – MBOX specification from devicetree
            - **cb** – Callback function to execute on incoming message interrupts.
            - **user\_data** – Application-specific data pointer which will be passed to the callback function when executed.

        Returns:
        :   See return values for [mbox\_register\_callback()](#group__mbox__interface_1gac1cc65cc54b9c7e6cf2639152a4d6a7a)

    int mbox\_mtu\_get(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Return the maximum number of bytes possible in an outbound message.

        Returns the actual number of bytes that it is possible to send through an outgoing channel.

        This number can be 0 when the driver only supports signalling or when on the receiving side the content and size of the message must be retrieved in an indirect way (i.e. probing some other peripheral, reading memory regions, etc…).

        If this function returns 0, the msg parameter in [mbox\_send()](#group__mbox__interface_1gaf4d02fb3a3ed788ba28a58783209d359) is expected to be NULL.

        Parameters:
        :   - **dev** – MBOX device instance.

        Return values:
        :   - **>0** – Maximum possible size of a message in bytes
            - **0** – Indicates signalling
            - **-errno** – Negative errno on error.

    static inline int mbox\_mtu\_get\_dt(const struct [mbox\_dt\_spec](#c.mbox_dt_spec) \*spec)
    :   Return the maximum number of bytes possible in an outbound message from struct [mbox\_dt\_spec](#structmbox__dt__spec).

        Parameters:
        :   - **spec** – MBOX specification from devicetree

        Returns:
        :   See return values for [mbox\_register\_callback()](#group__mbox__interface_1gac1cc65cc54b9c7e6cf2639152a4d6a7a)

    int mbox\_set\_enabled(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [mbox\_channel\_id\_t](#c.mbox_channel_id_t) channel\_id, bool enabled)
    :   Enable (disable) interrupts and callbacks for inbound channels.

        Enable interrupt for the channel when the parameter ‘enable’ is set to true. Disable it otherwise.

        Immediately after calling this function with ‘enable’ set to true, the channel is considered enabled and ready to receive signal and messages (even already pending), so the user must take care of installing a proper callback (if needed) using [mbox\_register\_callback()](#group__mbox__interface_1gac1cc65cc54b9c7e6cf2639152a4d6a7a) on the channel before enabling it. For this reason it is recommended that all the channels are disabled at probe time.

        Enabling a channel for which there is no installed callback is considered undefined behavior (in general the driver must take care of gracefully handling spurious interrupts with no installed callback).

        Parameters:
        :   - **dev** – MBOX device instance
            - **channel\_id** – MBOX channel identifier
            - **enabled** – Enable (true) or disable (false) the channel.

        Return values:
        :   - **0** – On success.
            - **-EINVAL** – If it isn’t an inbound channel.
            - **-EALREADY** – If channel is already `enabled`.

    static inline int mbox\_set\_enabled\_dt(const struct [mbox\_dt\_spec](#c.mbox_dt_spec) \*spec, bool enabled)
    :   Enable (disable) interrupts and callbacks for inbound channels from a struct [mbox\_dt\_spec](#structmbox__dt__spec).

        Parameters:
        :   - **spec** – MBOX specification from devicetree
            - **enabled** – Enable (true) or disable (false) the channel.

        Returns:
        :   See return values for [mbox\_set\_enabled()](#group__mbox__interface_1ga9eea4b9501751919125cd6124f9e9868)

    uint32\_t mbox\_max\_channels\_get(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Return the maximum number of channels.

        Return the maximum number of channels supported by the hardware.

        Parameters:
        :   - **dev** – MBOX device instance.

        Returns:
        :   >0 Maximum possible number of supported channels on success

        Returns:
        :   -errno Negative errno on error.

    static inline int mbox\_max\_channels\_get\_dt(const struct [mbox\_dt\_spec](#c.mbox_dt_spec) \*spec)
    :   Return the maximum number of channels from a struct [mbox\_dt\_spec](#structmbox__dt__spec).

        Parameters:
        :   - **spec** – MBOX specification from devicetree

        Returns:
        :   See return values for [mbox\_max\_channels\_get()](#group__mbox__interface_1gaf2f8adbd5e4f7f5972b2d34cfce68bdb)

    struct mbox\_msg
    :   *#include <mbox.h>*

        Message struct (to hold data and its size).

        Public Members

        const void \*data
        :   Pointer to the data sent in the message.

        size\_t size
        :   Size of the data.

    struct mbox\_dt\_spec
    :   *#include <mbox.h>*

        MBOX specification from DT.

        Public Members

        const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev
        :   MBOX device pointer.

        [mbox\_channel\_id\_t](#c.mbox_channel_id_t) channel\_id
        :   Channel ID.
