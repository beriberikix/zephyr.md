---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/audio/i2s.html
original_path: hardware/peripherals/audio/i2s.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Inter-IC Sound (I2S) Bus

## Overview

The I2S (Inter-IC Sound) API provides support for the standard I2S interface
as well as common non-standard extensions such as PCM Short/Long Frame Sync
and Left/Right Justified Data Formats.

## Configuration Options

Related configuration options:

- [`CONFIG_I2S`](../../../kconfig.md#CONFIG_I2S "CONFIG_I2S")

## API Reference

Related code samples

[I2S echo](../../../samples/drivers/i2s/echo/README.md#i2s-echo "Process an audio stream to add an echo effect.")
:   Process an audio stream to add an echo effect.

[I2S output](../../../samples/drivers/i2s/output/README.md#i2s-output "Send I2S output stream")
:   Send I2S output stream

[USB Audio asynchronous explicit feedback sample](../../../samples/subsys/usb/uac2_explicit_feedback/README.md#uac2-explicit-feedback "USB Audio 2 explicit feedback sample playing audio on I2S.")
:   USB Audio 2 explicit feedback sample playing audio on I2S.

*group* I2S Interface
:   I2S (Inter-IC Sound) Interface.

    **Since**
    :   1.9

    **Version**
    :   1.0.0

    The I2S API provides support for the standard I2S interface standard as well as common non-standard extensions such as PCM Short/Long Frame Sync, Left/Right Justified Data Format.

    Defines

    I2S\_FMT\_DATA\_FORMAT\_SHIFT
    :   Data Format bit field position.

    I2S\_FMT\_DATA\_FORMAT\_MASK
    :   Data Format bit field mask.

    I2S\_FMT\_DATA\_FORMAT\_I2S
    :   Standard I2S Data Format.

        Serial data is transmitted in two’s complement with the MSB first. Both Word Select (WS) and Serial Data (SD) signals are sampled on the rising edge of the clock signal (SCK). The MSB is always sent one clock period after the WS changes. Left channel data are sent first indicated by WS = 0, followed by right channel data indicated by WS = 1.

        ```text
           -. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-.
        SCK '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '
           -.                               .-------------------------------.
        WS  '-------------------------------'                               '----
           -.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.
        SD  |   |MSB|   |...|   |LSB| x |...| x |MSB|   |...|   |LSB| x |...| x |
           -'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'
                | Left channel                  | Right channel                 |
        ```

    I2S\_FMT\_DATA\_FORMAT\_PCM\_SHORT
    :   PCM Short Frame Sync Data Format.

        Serial data is transmitted in two’s complement with the MSB first. Both Word Select (WS) and Serial Data (SD) signals are sampled on the falling edge of the clock signal (SCK). The falling edge of the frame sync signal (WS) indicates the start of the PCM word. The frame sync is one clock cycle long. An arbitrary number of data words can be sent in one frame.

        ```text
             .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-.
        SCK -' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-
             .---.                                                       .---.
        WS  -'   '-                                                     -'   '-
            -.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---
        SD   |   |MSB|   |...|   |LSB|MSB|   |...|   |LSB|MSB|   |...|   |LSB|
            -'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---
                 | Word 1            | Word 2            | Word 3  |  Word n |
        ```

    I2S\_FMT\_DATA\_FORMAT\_PCM\_LONG
    :   PCM Long Frame Sync Data Format.

        Serial data is transmitted in two’s complement with the MSB first. Both Word Select (WS) and Serial Data (SD) signals are sampled on the falling edge of the clock signal (SCK). The rising edge of the frame sync signal (WS) indicates the start of the PCM word. The frame sync has an arbitrary length, however it has to fall before the start of the next frame. An arbitrary number of data words can be sent in one frame.

        ```text
             .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-.
        SCK -' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-
                 .--- ---.    ---.        ---.                               .---
        WS      -'       '-      '-          '-                             -'
            -.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---
        SD   |   |MSB|   |...|   |LSB|MSB|   |...|   |LSB|MSB|   |...|   |LSB|
            -'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---
                 | Word 1            | Word 2            | Word 3  |  Word n |
        ```

    I2S\_FMT\_DATA\_FORMAT\_LEFT\_JUSTIFIED
    :   Left Justified Data Format.

        Serial data is transmitted in two’s complement with the MSB first. Both Word Select (WS) and Serial Data (SD) signals are sampled on the rising edge of the clock signal (SCK). The bits within the data word are left justified such that the MSB is always sent in the clock period following the WS transition. Left channel data are sent first indicated by WS = 1, followed by right channel data indicated by WS = 0.

        ```text
             .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-.
        SCK -' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-
               .-------------------------------.                               .-
        WS  ---'                               '-------------------------------'
            ---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.-
        SD     |MSB|   |...|   |LSB| x |...| x |MSB|   |...|   |LSB| x |...| x |
            ---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'-
               | Left channel                  | Right channel                 |
        ```

    I2S\_FMT\_DATA\_FORMAT\_RIGHT\_JUSTIFIED
    :   Right Justified Data Format.

        Serial data is transmitted in two’s complement with the MSB first. Both Word Select (WS) and Serial Data (SD) signals are sampled on the rising edge of the clock signal (SCK). The bits within the data word are right justified such that the LSB is always sent in the clock period preceding the WS transition. Left channel data are sent first indicated by WS = 1, followed by right channel data indicated by WS = 0.

        ```text
             .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-.
        SCK -' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-
               .-------------------------------.                               .-
        WS  ---'                               '-------------------------------'
            ---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.-
        SD     | x |...| x |MSB|   |...|   |LSB| x |...| x |MSB|   |...|   |LSB|
            ---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'-
               | Left channel                  | Right channel                 |
        ```

    I2S\_FMT\_DATA\_ORDER\_MSB
    :   Send MSB first.

    I2S\_FMT\_DATA\_ORDER\_LSB
    :   Send LSB first.

    I2S\_FMT\_DATA\_ORDER\_INV
    :   Invert bit ordering, send LSB first.

    I2S\_FMT\_CLK\_FORMAT\_SHIFT
    :   Data Format bit field position.

    I2S\_FMT\_CLK\_FORMAT\_MASK
    :   Data Format bit field mask.

    I2S\_FMT\_BIT\_CLK\_INV
    :   Invert bit clock.

    I2S\_FMT\_FRAME\_CLK\_INV
    :   Invert frame clock.

    I2S\_FMT\_CLK\_NF\_NB
    :   Normal Frame, Normal Bit Clk.

    I2S\_FMT\_CLK\_NF\_IB
    :   Normal Frame, Inverted Bit Clk.

    I2S\_FMT\_CLK\_IF\_NB
    :   Inverted Frame, Normal Bit Clk.

    I2S\_FMT\_CLK\_IF\_IB
    :   Inverted Frame, Inverted Bit Clk.

    I2S\_OPT\_BIT\_CLK\_CONT
    :   Run bit clock continuously.

    I2S\_OPT\_BIT\_CLK\_GATED
    :   Run bit clock when sending data only.

    I2S\_OPT\_BIT\_CLK\_MASTER
    :   I2S driver is bit clock master.

    I2S\_OPT\_BIT\_CLK\_SLAVE
    :   I2S driver is bit clock slave.

    I2S\_OPT\_FRAME\_CLK\_MASTER
    :   I2S driver is frame clock master.

    I2S\_OPT\_FRAME\_CLK\_SLAVE
    :   I2S driver is frame clock slave.

    I2S\_OPT\_LOOPBACK
    :   Loop back mode.

        In loop back mode RX input will be connected internally to TX output. This is used primarily for testing.

    I2S\_OPT\_PINGPONG
    :   Ping pong mode.

        In ping pong mode TX output will keep alternating between a ping buffer and a pong buffer. This is normally used in audio streams when one buffer is being populated while the other is being played (DMAed) and vice versa. So, in this mode, 2 sets of buffers fixed in size are used. Static Arrays are used to achieve this and hence they are never freed.

    Typedefs

    typedef uint8\_t i2s\_fmt\_t
    :   I2S data stream format options.

    typedef uint8\_t i2s\_opt\_t
    :   I2S configuration options.

    Enums

    enum i2s\_dir
    :   I2C Direction.

        *Values:*

        enumerator I2S\_DIR\_RX
        :   Receive data.

        enumerator I2S\_DIR\_TX
        :   Transmit data.

        enumerator I2S\_DIR\_BOTH
        :   Both receive and transmit data.

    enum i2s\_state
    :   Interface state.

        *Values:*

        enumerator I2S\_STATE\_NOT\_READY
        :   The interface is not ready.

            The interface was initialized but is not yet ready to receive / transmit data. Call [i2s\_configure()](#group__i2s__interface_1ga299003d72146c127f88d7c12c08889cc) to configure interface and change its state to READY.

        enumerator I2S\_STATE\_READY
        :   The interface is ready to receive / transmit data.

        enumerator I2S\_STATE\_RUNNING
        :   The interface is receiving / transmitting data.

        enumerator I2S\_STATE\_STOPPING
        :   The interface is draining its transmit queue.

        enumerator I2S\_STATE\_ERROR
        :   TX buffer underrun or RX buffer overrun has occurred.

    enum i2s\_trigger\_cmd
    :   Trigger command.

        *Values:*

        enumerator I2S\_TRIGGER\_START
        :   Start the transmission / reception of data.

            If I2S\_DIR\_TX is set some data has to be queued for transmission by the [i2s\_write()](#group__i2s__interface_1ga01edf23acc6c16bbaf718dab8061a7a0) function. This trigger can be used in READY state only and changes the interface state to RUNNING.

        enumerator I2S\_TRIGGER\_STOP
        :   Stop the transmission / reception of data.

            Stop the transmission / reception of data at the end of the current memory block. This trigger can be used in RUNNING state only and at first changes the interface state to STOPPING. When the current TX / RX block is transmitted / received the state is changed to READY. Subsequent START trigger will resume transmission / reception where it stopped.

        enumerator I2S\_TRIGGER\_DRAIN
        :   Empty the transmit queue.

            Send all data in the transmit queue and stop the transmission. If the trigger is applied to the RX queue it has the same effect as I2S\_TRIGGER\_STOP. This trigger can be used in RUNNING state only and at first changes the interface state to STOPPING. When all TX blocks are transmitted the state is changed to READY.

        enumerator I2S\_TRIGGER\_DROP
        :   Discard the transmit / receive queue.

            Stop the transmission / reception immediately and discard the contents of the respective queue. This trigger can be used in any state other than NOT\_READY and changes the interface state to READY.

        enumerator I2S\_TRIGGER\_PREPARE
        :   Prepare the queues after underrun/overrun error has occurred.

            This trigger can be used in ERROR state only and changes the interface state to READY.

    Functions

    int i2s\_configure(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, enum [i2s\_dir](#c.i2s_dir) dir, const struct [i2s\_config](#c.i2s_config) \*cfg)
    :   Configure operation of a host I2S controller.

        The dir parameter specifies if Transmit (TX) or Receive (RX) direction will be configured by data provided via cfg parameter.

        The function can be called in NOT\_READY or READY state only. If executed successfully the function will change the interface state to READY.

        If the function is called with the parameter cfg->frame\_clk\_freq set to 0 the interface state will be changed to NOT\_READY.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **dir** – Stream direction: RX, TX, or both, as defined by I2S\_DIR\_\*. The I2S\_DIR\_BOTH value may not be supported by some drivers. For those, the RX and TX streams need to be configured separately.
            - **cfg** – Pointer to the structure containing configuration parameters.

        Return values:
        :   - **0** – If successful.
            - **-EINVAL** – Invalid argument.
            - **-ENOSYS** – I2S\_DIR\_BOTH value is not supported.

    static inline const struct [i2s\_config](#c.i2s_config) \*i2s\_config\_get(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, enum [i2s\_dir](#c.i2s_dir) dir)
    :   Fetch configuration information of a host I2S controller.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance
            - **dir** – Stream direction: RX or TX as defined by I2S\_DIR\_\*

        Return values:
        :   **Pointer** – to the structure containing configuration parameters, or NULL if un-configured

    static inline int i2s\_read(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, void \*\*mem\_block, size\_t \*size)
    :   Read data from the RX queue.

        Data received by the I2S interface is stored in the RX queue consisting of memory blocks preallocated by this function from rx\_mem\_slab (as defined by i2s\_configure). Ownership of the RX memory block is passed on to the user application which has to release it.

        The data is read in chunks equal to the size of the memory block. If the interface is in READY state the number of bytes read can be smaller.

        If there is no data in the RX queue the function will block waiting for the next RX memory block to fill in. This operation can timeout as defined by i2s\_configure. If the timeout value is set to K\_NO\_WAIT the function is non-blocking.

        Reading from the RX queue is possible in any state other than NOT\_READY. If the interface is in the ERROR state it is still possible to read all the valid data stored in RX queue. Afterwards the function will return -EIO error.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **mem\_block** – Pointer to the RX memory block containing received data.
            - **size** – Pointer to the variable storing the number of bytes read.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – The interface is in NOT\_READY or ERROR state and there are no more data blocks in the RX queue.
            - **-EBUSY** – Returned without waiting.
            - **-EAGAIN** – Waiting period timed out.

    int i2s\_buf\_read(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, void \*buf, size\_t \*size)
    :   Read data from the RX queue into a provided buffer.

        Data received by the I2S interface is stored in the RX queue consisting of memory blocks preallocated by this function from rx\_mem\_slab (as defined by i2s\_configure). Calling this function removes one block from the queue which is copied into the provided buffer and then freed.

        The provided buffer must be large enough to contain a full memory block of data, which is parameterized for the channel via [i2s\_configure()](#group__i2s__interface_1ga299003d72146c127f88d7c12c08889cc).

        This function is otherwise equivalent to [i2s\_read()](#group__i2s__interface_1ga7f23b7959280e1c4075a4305c3edd655).

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **buf** – Destination buffer for read data, which must be at least the as large as the configured memory block size for the RX channel.
            - **size** – Pointer to the variable storing the number of bytes read.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – The interface is in NOT\_READY or ERROR state and there are no more data blocks in the RX queue.
            - **-EBUSY** – Returned without waiting.
            - **-EAGAIN** – Waiting period timed out.

    static inline int i2s\_write(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, void \*mem\_block, size\_t size)
    :   Write data to the TX queue.

        Data to be sent by the I2S interface is stored first in the TX queue. TX queue consists of memory blocks preallocated by the user from tx\_mem\_slab (as defined by i2s\_configure). This function takes ownership of the memory block and will release it when all data are transmitted.

        If there are no free slots in the TX queue the function will block waiting for the next TX memory block to be send and removed from the queue. This operation can timeout as defined by i2s\_configure. If the timeout value is set to K\_NO\_WAIT the function is non-blocking.

        Writing to the TX queue is only possible if the interface is in READY or RUNNING state.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **mem\_block** – Pointer to the TX memory block containing data to be sent.
            - **size** – Number of bytes to write. This value has to be equal or smaller than the size of the memory block.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – The interface is not in READY or RUNNING state.
            - **-EBUSY** – Returned without waiting.
            - **-EAGAIN** – Waiting period timed out.

    int i2s\_buf\_write(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, void \*buf, size\_t size)
    :   Write data to the TX queue from a provided buffer.

        This function acquires a memory block from the I2S channel TX queue and copies the provided data buffer into it. It is otherwise equivalent to [i2s\_write()](#group__i2s__interface_1ga01edf23acc6c16bbaf718dab8061a7a0).

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **buf** – Pointer to a buffer containing the data to transmit.
            - **size** – Number of bytes to write. This value has to be equal or smaller than the size of the channel’s TX memory block configuration.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – The interface is not in READY or RUNNING state.
            - **-EBUSY** – Returned without waiting.
            - **-EAGAIN** – Waiting period timed out.
            - **-ENOMEM** – No memory in TX slab queue.
            - **-EINVAL** – Size parameter larger than TX queue memory block.

    int i2s\_trigger(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, enum [i2s\_dir](#c.i2s_dir) dir, enum [i2s\_trigger\_cmd](#c.i2s_trigger_cmd) cmd)
    :   Send a trigger command.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **dir** – Stream direction: RX, TX, or both, as defined by I2S\_DIR\_\*. The I2S\_DIR\_BOTH value may not be supported by some drivers. For those, triggering need to be done separately for the RX and TX streams.
            - **cmd** – Trigger command.

        Return values:
        :   - **0** – If successful.
            - **-EINVAL** – Invalid argument.
            - **-EIO** – The trigger cannot be executed in the current state or a DMA channel cannot be allocated.
            - **-ENOMEM** – RX/TX memory block not available.
            - **-ENOSYS** – I2S\_DIR\_BOTH value is not supported.

    struct i2s\_config
    :   *#include <i2s.h>*

        Interface configuration options.

        Memory slab pointed to by the mem\_slab field has to be defined and initialized by the user. For I2S driver to function correctly number of memory blocks in a slab has to be at least 2 per queue. Size of the memory block should be multiple of frame\_size where frame\_size = (channels \* word\_size\_bytes). As an example 16 bit word will occupy 2 bytes, 24 or 32 bit word will occupy 4 bytes.

        Please check Zephyr Kernel Primer for more information on memory slabs.

        Remark

        When I2S data format is selected parameter channels is ignored, number of words in a frame is always 2.

        Public Members

        uint8\_t word\_size
        :   Number of bits representing one data word.

        uint8\_t channels
        :   Number of words per frame.

        [i2s\_fmt\_t](#c.i2s_fmt_t) format
        :   Data stream format as defined by I2S\_FMT\_\* constants.

        [i2s\_opt\_t](#c.i2s_opt_t) options
        :   Configuration options as defined by I2S\_OPT\_\* constants.

        uint32\_t frame\_clk\_freq
        :   Frame clock (WS) frequency, this is sampling rate.

        struct k\_mem\_slab \*mem\_slab
        :   Memory slab to store RX/TX data.

        size\_t block\_size
        :   Size of one RX/TX memory block (buffer) in bytes.

        int32\_t timeout
        :   Read/Write timeout.

            Number of milliseconds to wait in case TX queue is full or RX queue is empty, or 0, or SYS\_FOREVER\_MS.
