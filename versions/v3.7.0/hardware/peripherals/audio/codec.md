---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/audio/codec.html
original_path: hardware/peripherals/audio/codec.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Audio Codec

## Overview

The Audio Codec API provides access to digital audio codecs.

## Configuration Options

Related configuration options:

- [`CONFIG_AUDIO_CODEC`](../../../kconfig.md#CONFIG_AUDIO_CODEC "CONFIG_AUDIO_CODEC")

## API Reference

*group* Audio Codec Interface
:   Abstraction for audio codecs.

    **Since**
    :   1.13

    **Version**
    :   0.1.0

    Typedefs

    typedef void (\*audio\_codec\_error\_callback\_t)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t errors)
    :   Callback for error interrupt.

        Param dev:
        :   Pointer to the codec device

        Param errors:
        :   Device errors (bitmask of [audio\_codec\_error\_type](#group__audio__codec__interface_1ga2923c9aca9b8656ba3e3741d5860279a) values)

    Enums

    enum audio\_pcm\_rate\_t
    :   PCM audio sample rates.

        *Values:*

        enumerator AUDIO\_PCM\_RATE\_8K = 8000
        :   8 kHz sample rate

        enumerator AUDIO\_PCM\_RATE\_16K = 16000
        :   16 kHz sample rate

        enumerator AUDIO\_PCM\_RATE\_24K = 24000
        :   24 kHz sample rate

        enumerator AUDIO\_PCM\_RATE\_32K = 32000
        :   32 kHz sample rate

        enumerator AUDIO\_PCM\_RATE\_44P1K = 44100
        :   44.1 kHz sample rate

        enumerator AUDIO\_PCM\_RATE\_48K = 48000
        :   48 kHz sample rate

        enumerator AUDIO\_PCM\_RATE\_96K = 96000
        :   96 kHz sample rate

        enumerator AUDIO\_PCM\_RATE\_192K = 192000
        :   192 kHz sample rate

    enum audio\_pcm\_width\_t
    :   PCM audio sample bit widths.

        *Values:*

        enumerator AUDIO\_PCM\_WIDTH\_16\_BITS = 16
        :   16-bit sample width

        enumerator AUDIO\_PCM\_WIDTH\_20\_BITS = 20
        :   20-bit sample width

        enumerator AUDIO\_PCM\_WIDTH\_24\_BITS = 24
        :   24-bit sample width

        enumerator AUDIO\_PCM\_WIDTH\_32\_BITS = 32
        :   32-bit sample width

    enum audio\_dai\_type\_t
    :   Digital Audio Interface (DAI) type.

        *Values:*

        enumerator AUDIO\_DAI\_TYPE\_I2S
        :   I2S Interface.

        enumerator AUDIO\_DAI\_TYPE\_INVALID
        :   Other interfaces can be added here.

    enum audio\_property\_t
    :   Codec properties that can be set by [audio\_codec\_set\_property()](#group__audio__codec__interface_1ga6d28af0279eb8e4b693ea35f5235f189).

        *Values:*

        enumerator AUDIO\_PROPERTY\_OUTPUT\_VOLUME
        :   Output volume.

        enumerator AUDIO\_PROPERTY\_OUTPUT\_MUTE
        :   Output mute/unmute.

    enum audio\_channel\_t
    :   Audio channel identifiers to use in [audio\_codec\_set\_property()](#group__audio__codec__interface_1ga6d28af0279eb8e4b693ea35f5235f189).

        *Values:*

        enumerator AUDIO\_CHANNEL\_FRONT\_LEFT
        :   Front left channel.

        enumerator AUDIO\_CHANNEL\_FRONT\_RIGHT
        :   Front right channel.

        enumerator AUDIO\_CHANNEL\_LFE
        :   Low frequency effect channel.

        enumerator AUDIO\_CHANNEL\_FRONT\_CENTER
        :   Front center channel.

        enumerator AUDIO\_CHANNEL\_REAR\_LEFT
        :   Rear left channel.

        enumerator AUDIO\_CHANNEL\_REAR\_RIGHT
        :   Rear right channel.

        enumerator AUDIO\_CHANNEL\_REAR\_CENTER
        :   Rear center channel.

        enumerator AUDIO\_CHANNEL\_SIDE\_LEFT
        :   Side left channel.

        enumerator AUDIO\_CHANNEL\_SIDE\_RIGHT
        :   Side right channel.

        enumerator AUDIO\_CHANNEL\_ALL
        :   All channels.

    enum audio\_codec\_error\_type
    :   Codec error type.

        *Values:*

        enumerator AUDIO\_CODEC\_ERROR\_OVERCURRENT = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   Output over-current.

        enumerator AUDIO\_CODEC\_ERROR\_OVERTEMPERATURE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   Codec over-temperature.

        enumerator AUDIO\_CODEC\_ERROR\_UNDERVOLTAGE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)
        :   Power low voltage.

        enumerator AUDIO\_CODEC\_ERROR\_OVERVOLTAGE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(3)
        :   Power high voltage.

        enumerator AUDIO\_CODEC\_ERROR\_DC = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(4)
        :   Output direct-current.

    Functions

    static inline int audio\_codec\_configure(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [audio\_codec\_cfg](#c.audio_codec_cfg) \*cfg)
    :   Configure the audio codec.

        Configure the audio codec device according to the configuration parameters provided as input

        Parameters:
        :   - **dev** – Pointer to the device structure for codec driver instance.
            - **cfg** – Pointer to the structure containing the codec configuration.

        Returns:
        :   0 on success, negative error code on failure

    static inline void audio\_codec\_start\_output(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Set codec to start output audio playback.

        Setup the audio codec device to start the audio playback

        Parameters:
        :   - **dev** – Pointer to the device structure for codec driver instance.

    static inline void audio\_codec\_stop\_output(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Set codec to stop output audio playback.

        Setup the audio codec device to stop the audio playback

        Parameters:
        :   - **dev** – Pointer to the device structure for codec driver instance.

    static inline int audio\_codec\_set\_property(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, [audio\_property\_t](#c.audio_property_t) property, [audio\_channel\_t](#c.audio_channel_t) channel, [audio\_property\_value\_t](#c.audio_property_value_t) val)
    :   Set a codec property defined by [audio\_property\_t](#group__audio__codec__interface_1ga5411b79fa217b0f9c63dc6890323804c).

        Set a property such as volume level, clock configuration etc.

        Parameters:
        :   - **dev** – Pointer to the device structure for codec driver instance.
            - **property** – The codec property to set
            - **channel** – The audio channel for which the property has to be set
            - **val** – pointer to a property value of type audio\_codec\_property\_value\_t

        Returns:
        :   0 on success, negative error code on failure

    static inline int audio\_codec\_apply\_properties(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Atomically apply any cached properties.

        Following one or more invocations of audio\_codec\_set\_property, that may have been cached by the driver, audio\_codec\_apply\_properties can be invoked to apply all the properties as atomic as possible

        Parameters:
        :   - **dev** – Pointer to the device structure for codec driver instance.

        Returns:
        :   0 on success, negative error code on failure

    static inline int audio\_codec\_clear\_errors(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Clear any codec errors.

        Clear all codec errors. If an error interrupt exists, it will be de-asserted.

        Parameters:
        :   - **dev** – Pointer to the device structure for codec driver instance.

        Returns:
        :   0 on success, negative error code on failure

    static inline int audio\_codec\_register\_error\_callback(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, [audio\_codec\_error\_callback\_t](#c.audio_codec_error_callback_t) cb)
    :   Register a callback function for codec error.

        The callback will be called from a thread, so I2C or SPI operations are safe. However, the thread’s stack is limited and defined by the driver. It is currently up to the caller to ensure that the callback does not overflow the stack.

        Parameters:
        :   - **dev** – Pointer to the audio codec device
            - **cb** – The function that should be called when an error is detected fires

        Returns:
        :   0 if successful, negative errno code if failure.

    union audio\_dai\_cfg\_t
    :   *#include <codec.h>*

        Digital Audio Interface Configuration.

        Configuration is dependent on DAI type

        Public Members

        struct [i2s\_config](i2s.md#c.i2s_config "i2s_config") i2s
        :   I2S configuration.

    struct audio\_codec\_cfg
    :   *#include <codec.h>*

        Codec configuration parameters.

        Public Members

        uint32\_t mclk\_freq
        :   MCLK input frequency in Hz.

        [audio\_dai\_type\_t](#c.audio_dai_type_t) dai\_type
        :   Digital interface type.

        [audio\_dai\_cfg\_t](#c.audio_dai_cfg_t) dai\_cfg
        :   DAI configuration info.

    union audio\_property\_value\_t
    :   *#include <codec.h>*

        Codec property values.

        Public Members

        int vol
        :   Volume level in 0.5dB resolution.

        bool mute
        :   Mute if *true*, unmute if *false*.
