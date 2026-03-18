---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/audio/dmic.html
original_path: hardware/peripherals/audio/dmic.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Digital Microphone (DMIC)

## Overview

The audio DMIC interface provides access to digital microphones.

## Configuration Options

Related configuration options:

- [`CONFIG_AUDIO_DMIC`](../../../kconfig.md#CONFIG_AUDIO_DMIC "CONFIG_AUDIO_DMIC")

## API Reference

Related code samples

[Digital Microphone (DMIC)](../../../samples/drivers/audio/dmic/README.md#dmic "Perform PDM transfers using different configurations.")
:   Perform PDM transfers using different configurations.

[X-NUCLEO-IKS02A1 shield - MEMS microphone](../../../samples/shields/x_nucleo_iks02a1/microphone/README.md#x-nucleo-iks02a1-mic "Acquire audio using the digital MEMS microphone on X-NUCLEO-IKS02A1 shield.")
:   Acquire audio using the digital MEMS microphone on X-NUCLEO-IKS02A1 shield.

*group* Digital Microphone Interface
:   Abstraction for digital microphones.

    **Since**
    :   1.13

    **Version**
    :   0.1.0

    Enums

    enum dmic\_state
    :   DMIC driver states.

        *Values:*

        enumerator DMIC\_STATE\_UNINIT
        :   Uninitialized.

        enumerator DMIC\_STATE\_INITIALIZED
        :   Initialized.

        enumerator DMIC\_STATE\_CONFIGURED
        :   Configured.

        enumerator DMIC\_STATE\_ACTIVE
        :   Active.

        enumerator DMIC\_STATE\_PAUSED
        :   Paused.

        enumerator DMIC\_STATE\_ERROR
        :   Error.

    enum dmic\_trigger
    :   DMIC driver trigger commands.

        *Values:*

        enumerator DMIC\_TRIGGER\_STOP
        :   Stop stream.

        enumerator DMIC\_TRIGGER\_START
        :   Start stream.

        enumerator DMIC\_TRIGGER\_PAUSE
        :   Pause stream.

        enumerator DMIC\_TRIGGER\_RELEASE
        :   Release paused stream.

        enumerator DMIC\_TRIGGER\_RESET
        :   Reset stream.

    enum pdm\_lr
    :   PDM Channels LEFT / RIGHT.

        *Values:*

        enumerator PDM\_CHAN\_LEFT
        :   Left channel.

        enumerator PDM\_CHAN\_RIGHT
        :   Right channel.

    Functions

    static inline uint32\_t dmic\_build\_channel\_map(uint8\_t channel, uint8\_t pdm, enum [pdm\_lr](#c.pdm_lr) lr)
    :   Build the channel map to populate struct [pdm\_chan\_cfg](#structpdm__chan__cfg).

        Returns the map of PDM controller and LEFT/RIGHT channel shifted to the bit position corresponding to the input logical channel value

        Parameters:
        :   - **channel** – The logical channel number
            - **pdm** – The PDM hardware controller number
            - **lr** – LEFT/RIGHT channel within the chosen PDM hardware controller

        Returns:
        :   Bit-map containing the PDM and L/R channel information

    static inline void dmic\_parse\_channel\_map(uint32\_t channel\_map\_lo, uint32\_t channel\_map\_hi, uint8\_t channel, uint8\_t \*pdm, enum [pdm\_lr](#c.pdm_lr) \*lr)
    :   Helper function to parse the channel map in [pdm\_chan\_cfg](#structpdm__chan__cfg).

        Returns the PDM controller and LEFT/RIGHT channel corresponding to the channel map and the logical channel provided as input

        Parameters:
        :   - **channel\_map\_lo** – Lower order/significant bits of the channel map
            - **channel\_map\_hi** – Higher order/significant bits of the channel map
            - **channel** – The logical channel number
            - **pdm** – Pointer to the PDM hardware controller number
            - **lr** – Pointer to the LEFT/RIGHT channel within the PDM controller

    static inline uint32\_t dmic\_build\_clk\_skew\_map(uint8\_t pdm, uint8\_t skew)
    :   Build a bit map of clock skew values for each PDM channel.

        Returns the bit-map of clock skew value shifted to the bit position corresponding to the input PDM controller value

        Parameters:
        :   - **pdm** – The PDM hardware controller number
            - **skew** – The skew to apply for the clock output from the PDM controller

        Returns:
        :   Bit-map containing the clock skew information

    static inline int dmic\_configure(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [dmic\_cfg](#c.dmic_cfg) \*cfg)
    :   Configure the DMIC driver and controller(s).

        Configures the DMIC driver device according to the number of channels, channel mapping, PDM I/O configuration, PCM stream configuration, etc.

        Parameters:
        :   - **dev** – Pointer to the device structure for DMIC driver instance
            - **cfg** – Pointer to the structure containing the DMIC configuration

        Returns:
        :   0 on success, a negative error code on failure

    static inline int dmic\_trigger(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, enum [dmic\_trigger](#c.dmic_trigger) cmd)
    :   Send a command to the DMIC driver.

        Sends a command to the driver to perform a specific action

        Parameters:
        :   - **dev** – Pointer to the device structure for DMIC driver instance
            - **cmd** – The command to be sent to the driver instance

        Returns:
        :   0 on success, a negative error code on failure

    static inline int dmic\_read(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t stream, void \*\*buffer, size\_t \*size, int32\_t timeout)
    :   Read received decimated PCM data stream.

        Optionally waits for audio to be received and provides the received audio buffer from the requested stream

        Parameters:
        :   - **dev** – Pointer to the device structure for DMIC driver instance
            - **stream** – Stream identifier
            - **buffer** – Pointer to the received buffer address
            - **size** – Pointer to the received buffer size
            - **timeout** – Timeout in milliseconds to wait in case audio is not yet received, or SYS\_FOREVER\_MS

        Returns:
        :   0 on success, a negative error code on failure

    struct pdm\_io\_cfg
    :   *#include <dmic.h>*

        PDM Input/Output signal configuration.

        Parameters common to all PDM controllers

        uint32\_t min\_pdm\_clk\_freq
        :   Minimum clock frequency supported by the mic.

        uint32\_t max\_pdm\_clk\_freq
        :   Maximum clock frequency supported by the mic.

        uint8\_t min\_pdm\_clk\_dc
        :   Minimum duty cycle in % supported by the mic.

        uint8\_t max\_pdm\_clk\_dc
        :   Maximum duty cycle in % supported by the mic.

        Parameters unique to each PDM controller

        uint8\_t pdm\_clk\_pol
        :   Bit mask to optionally invert PDM clock.

        uint8\_t pdm\_data\_pol
        :   Bit mask to optionally invert mic data.

        uint32\_t pdm\_clk\_skew
        :   Collection of clock skew values for each PDM port.

    struct pcm\_stream\_cfg
    :   *#include <dmic.h>*

        Configuration of the PCM streams to be output by the PDM hardware.

        Note

        if either [pcm\_rate](#structpcm__stream__cfg_1ae6e3790576f910943b0383f4731a5545) or [pcm\_width](#structpcm__stream__cfg_1a7d9fd0039bc25de292f35f60c99c6615) is set to 0 for a stream, the stream would be disabled

        Public Members

        uint32\_t pcm\_rate
        :   PCM sample rate of stream.

        uint8\_t pcm\_width
        :   PCM sample width of stream.

        uint16\_t block\_size
        :   PCM sample block size per transfer.

        struct k\_mem\_slab \*mem\_slab
        :   SLAB for DMIC driver to allocate buffers for stream.

    struct pdm\_chan\_cfg
    :   *#include <dmic.h>*

        Mapping/ordering of the PDM channels to logical PCM output channel.

        Since each controller can have 2 audio channels (stereo), there can be a total of 8x2=16 channels. The actual number of channels shall be described in [act\_num\_chan](#structpdm__chan__cfg_1a3268169aaee14827cb15778fbc44ceb1).

        If 2 streams are enabled, the channel order will be the same for both streams.

        Each channel is described as a 4-bit number, the least significant bit indicates LEFT/RIGHT selection of the PDM controller.

        The most significant 3 bits indicate the PDM controller number:

        - bits 0-3 are for channel 0, bit 0 indicates LEFT or RIGHT
        - bits 4-7 are for channel 1, bit 4 indicates LEFT or RIGHT and so on.

        CONSTRAINT: The LEFT and RIGHT channels of EACH PDM controller needs to be adjacent to each other.

        Requested channel map

        uint32\_t req\_chan\_map\_lo
        :   Channels 0 to 7.

        uint32\_t req\_chan\_map\_hi
        :   Channels 8 to 15.

        Actual channel map that the driver could configure

        uint32\_t act\_chan\_map\_lo
        :   Channels 0 to 7.

        uint32\_t act\_chan\_map\_hi
        :   Channels 8 to 15.

        Public Members

        uint8\_t req\_num\_chan
        :   Requested number of channels.

        uint8\_t act\_num\_chan
        :   Actual number of channels that the driver could configure.

        uint8\_t req\_num\_streams
        :   Requested number of streams for each channel.

        uint8\_t act\_num\_streams
        :   Actual number of streams that the driver could configure.

    struct dmic\_cfg
    :   *#include <dmic.h>*

        Input configuration structure for the DMIC configuration API.

        Public Members

        struct [pcm\_stream\_cfg](#c.pcm_stream_cfg) \*streams
        :   Array of [pcm\_stream\_cfg](#structpcm__stream__cfg) for application to provide configuration for each stream.
