---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/audio.html
original_path: connectivity/bluetooth/api/audio.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth Audio

## API Reference

*group* bt\_audio
:   Bluetooth Audio.

    Defines

    BT\_AUDIO\_BROADCAST\_ID\_SIZE

    BT\_AUDIO\_BROADCAST\_ID\_MAX
    :   Maximum broadcast ID value.

    BT\_AUDIO\_PD\_PREF\_NONE
    :   Indicates that the server have no preference for the presentation delay.

    BT\_AUDIO\_PD\_MAX
    :   Maximum presentation delay in microseconds.

    BT\_AUDIO\_BROADCAST\_CODE\_SIZE

    BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_MIN
    :   Minimum supported channel counts.

    BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_MAX
    :   Maximum supported channel counts.

    BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_SUPPORT(...)
    :   Channel count support capability.

        Macro accepts variable number of channel counts. The allowed channel counts are defined by specification and have to be in range from [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_MIN](#group__bt__audio_1gac1251f8a35b5e343eeeff87f22f8ab10) to [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_MAX](#group__bt__audio_1gad91341739d394f92ffc4988b614f47b6) inclusive.

        Example to support 1 and 3 channels: [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_SUPPORT(1, 3)](#group__bt__audio_1ga8f835266fabd6461216fe13e1b3b3a0f)

    BT\_AUDIO\_CONTEXT\_TYPE\_ANY
    :   Any known context.

    BT\_AUDIO\_METADATA\_TYPE\_IS\_KNOWN(\_type)
    :   Helper to check whether metadata type is known by the stack.

        Note

        `_type` is evaluated thrice.

    BT\_AUDIO\_UNICAST\_ANNOUNCEMENT\_GENERAL

    BT\_AUDIO\_UNICAST\_ANNOUNCEMENT\_TARGETED

    BT\_AUDIO\_CODEC\_DATA(\_type, \_bytes...)
    :   Helper to declare elements of [bt\_audio\_codec\_cap](#structbt__audio__codec__cap) arrays.

        This macro is mainly for creating an array of struct [bt\_audio\_codec\_cap](#structbt__audio__codec__cap) data arrays.

        Parameters:
        :   - **\_type** – Type of advertising data field
            - **\_bytes** – Variable number of single-byte parameters

    BT\_AUDIO\_CODEC\_CFG(\_id, \_cid, \_vid, \_data, \_meta)
    :   Helper to declare [Codec config parsing APIs](#group__bt__audio__codec__cfg).

        Parameters:
        :   - **\_id** – Codec ID
            - **\_cid** – Company ID
            - **\_vid** – Vendor ID
            - **\_data** – Codec Specific Data in LVT format
            - **\_meta** – Codec Specific Metadata in LVT format

    BT\_AUDIO\_CODEC\_CAP(\_id, \_cid, \_vid, \_data, \_meta)
    :   Helper to declare Codec capability parsing APIs structure.

        Parameters:
        :   - **\_id** – Codec ID
            - **\_cid** – Company ID
            - **\_vid** – Vendor ID
            - **\_data** – Codec Specific Data in LVT format
            - **\_meta** – Codec Specific Metadata in LVT format

    BT\_AUDIO\_LOCATION\_ANY
    :   Any known location.

    BT\_AUDIO\_CODEC\_QOS(\_interval, \_framing, \_phy, \_sdu, \_rtn, \_latency, \_pd)
    :   Helper to declare elements of [bt\_audio\_codec\_qos](#structbt__audio__codec__qos).

        Parameters:
        :   - **\_interval** – SDU interval (usec)
            - **\_framing** – Framing
            - **\_phy** – Target PHY
            - **\_sdu** – Maximum SDU Size
            - **\_rtn** – Retransmission number
            - **\_latency** – Maximum Transport Latency (msec)
            - **\_pd** – Presentation Delay (usec)

    BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(\_interval, \_sdu, \_rtn, \_latency, \_pd)
    :   Helper to declare Input Unframed [bt\_audio\_codec\_qos](#structbt__audio__codec__qos).

        Parameters:
        :   - **\_interval** – SDU interval (usec)
            - **\_sdu** – Maximum SDU Size
            - **\_rtn** – Retransmission number
            - **\_latency** – Maximum Transport Latency (msec)
            - **\_pd** – Presentation Delay (usec)

    BT\_AUDIO\_CODEC\_QOS\_FRAMED(\_interval, \_sdu, \_rtn, \_latency, \_pd)
    :   Helper to declare Input Framed [bt\_audio\_codec\_qos](#structbt__audio__codec__qos).

        Parameters:
        :   - **\_interval** – SDU interval (usec)
            - **\_sdu** – Maximum SDU Size
            - **\_rtn** – Retransmission number
            - **\_latency** – Maximum Transport Latency (msec)
            - **\_pd** – Presentation Delay (usec)

    BT\_AUDIO\_CODEC\_QOS\_PREF(\_unframed\_supported, \_phy, \_rtn, \_latency, \_pd\_min, \_pd\_max, \_pref\_pd\_min, \_pref\_pd\_max)
    :   Helper to declare elements of [bt\_audio\_codec\_qos\_pref](#structbt__audio__codec__qos__pref).

        Parameters:
        :   - **\_unframed\_supported** – Unframed PDUs supported
            - **\_phy** – Preferred Target PHY
            - **\_rtn** – Preferred Retransmission number
            - **\_latency** – Preferred Maximum Transport Latency (msec)
            - **\_pd\_min** – Minimum Presentation Delay (usec)
            - **\_pd\_max** – Maximum Presentation Delay (usec)
            - **\_pref\_pd\_min** – Preferred Minimum Presentation Delay (usec)
            - **\_pref\_pd\_max** – Preferred Maximum Presentation Delay (usec)

    Enums

    enum bt\_audio\_codec\_cap\_type
    :   Codec capability types.

        Used to build and parse codec capabilities as specified in the PAC specification. Source is assigned numbers for Generic Audio, bluetooth.com.

        *Values:*

        enumerator BT\_AUDIO\_CODEC\_CAP\_TYPE\_FREQ = 0x01
        :   Supported sampling frequencies.

        enumerator BT\_AUDIO\_CODEC\_CAP\_TYPE\_DURATION = 0x02
        :   Supported frame durations.

        enumerator BT\_AUDIO\_CODEC\_CAP\_TYPE\_CHAN\_COUNT = 0x03
        :   Supported audio channel counts.

        enumerator BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_LEN = 0x04
        :   Supported octets per codec frame.

        enumerator BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_COUNT = 0x05
        :   Supported maximum codec frames per SDU.

    enum bt\_audio\_codec\_cap\_freq
    :   Supported frequencies bitfield.

        *Values:*

        enumerator BT\_AUDIO\_CODEC\_CAP\_FREQ\_8KHZ = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   8 Khz sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CAP\_FREQ\_11KHZ = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   11.025 Khz sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CAP\_FREQ\_16KHZ = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)
        :   16 Khz sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CAP\_FREQ\_22KHZ = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(3)
        :   22.05 Khz sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CAP\_FREQ\_24KHZ = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(4)
        :   24 Khz sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CAP\_FREQ\_32KHZ = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(5)
        :   32 Khz sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CAP\_FREQ\_44KHZ = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(6)
        :   44.1 Khz sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CAP\_FREQ\_48KHZ = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(7)
        :   48 Khz sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CAP\_FREQ\_88KHZ = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(8)
        :   88.2 Khz sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CAP\_FREQ\_96KHZ = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(9)
        :   96 Khz sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CAP\_FREQ\_176KHZ = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(10)
        :   176.4 Khz sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CAP\_FREQ\_192KHZ = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(11)
        :   192 Khz sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CAP\_FREQ\_384KHZ = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(12)
        :   384 Khz sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CAP\_FREQ\_ANY = ([BT\_AUDIO\_CODEC\_CAP\_FREQ\_8KHZ](#c.bt_audio_codec_cap_freq.BT_AUDIO_CODEC_CAP_FREQ_8KHZ) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_11KHZ](#c.bt_audio_codec_cap_freq.BT_AUDIO_CODEC_CAP_FREQ_11KHZ) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_16KHZ](#c.bt_audio_codec_cap_freq.BT_AUDIO_CODEC_CAP_FREQ_16KHZ) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_22KHZ](#c.bt_audio_codec_cap_freq.BT_AUDIO_CODEC_CAP_FREQ_22KHZ) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_24KHZ](#c.bt_audio_codec_cap_freq.BT_AUDIO_CODEC_CAP_FREQ_24KHZ) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_32KHZ](#c.bt_audio_codec_cap_freq.BT_AUDIO_CODEC_CAP_FREQ_32KHZ) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_44KHZ](#c.bt_audio_codec_cap_freq.BT_AUDIO_CODEC_CAP_FREQ_44KHZ) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_48KHZ](#c.bt_audio_codec_cap_freq.BT_AUDIO_CODEC_CAP_FREQ_48KHZ) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_88KHZ](#c.bt_audio_codec_cap_freq.BT_AUDIO_CODEC_CAP_FREQ_88KHZ) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_96KHZ](#c.bt_audio_codec_cap_freq.BT_AUDIO_CODEC_CAP_FREQ_96KHZ) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_176KHZ](#c.bt_audio_codec_cap_freq.BT_AUDIO_CODEC_CAP_FREQ_176KHZ) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_192KHZ](#c.bt_audio_codec_cap_freq.BT_AUDIO_CODEC_CAP_FREQ_192KHZ) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_384KHZ](#c.bt_audio_codec_cap_freq.BT_AUDIO_CODEC_CAP_FREQ_384KHZ))
        :   Any frequency capability.

    enum bt\_audio\_codec\_cap\_frame\_dur
    :   Supported frame durations bitfield.

        *Values:*

        enumerator BT\_AUDIO\_CODEC\_CAP\_DURATION\_7\_5 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   7.5 msec frame duration capability

        enumerator BT\_AUDIO\_CODEC\_CAP\_DURATION\_10 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   10 msec frame duration capability

        enumerator BT\_AUDIO\_CODEC\_CAP\_DURATION\_ANY = ([BT\_AUDIO\_CODEC\_CAP\_DURATION\_7\_5](#c.bt_audio_codec_cap_frame_dur.BT_AUDIO_CODEC_CAP_DURATION_7_5) | [BT\_AUDIO\_CODEC\_CAP\_DURATION\_10](#c.bt_audio_codec_cap_frame_dur.BT_AUDIO_CODEC_CAP_DURATION_10))
        :   Any frame duration capability.

        enumerator BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_7\_5 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(4)
        :   7.5 msec preferred frame duration capability.

            This shall only be set if [BT\_AUDIO\_CODEC\_CAP\_DURATION\_7\_5](#group__bt__audio_1ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441) is also set, and if [BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_10](#group__bt__audio_1ggaf37e8e19f956afb3c3a413cbaa1a21f5a9744473b3a29074c24cf0bbff35a5d8e) is not set.

        enumerator BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_10 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(5)
        :   10 msec preferred frame duration capability

            This shall only be set if [BT\_AUDIO\_CODEC\_CAP\_DURATION\_10](#group__bt__audio_1ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b) is also set, and if [BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_7\_5](#group__bt__audio_1ggaf37e8e19f956afb3c3a413cbaa1a21f5a7ab1c63639cf93fdf2c2dfdf43424e91) is not set.

    enum bt\_audio\_codec\_cap\_chan\_count
    :   *Values:*

        enumerator BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_1 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   Supporting 1 channel.

        enumerator BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_2 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   Supporting 2 channel.

        enumerator BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_3 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)
        :   Supporting 3 channel.

        enumerator BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_4 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(3)
        :   Supporting 4 channel.

        enumerator BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_5 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(4)
        :   Supporting 5 channel.

        enumerator BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_6 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(5)
        :   Supporting 6 channel.

        enumerator BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_7 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(6)
        :   Supporting 7 channel.

        enumerator BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_8 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(7)
        :   Supporting 8 channel.

        enumerator BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_ANY = ([BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_1](#c.bt_audio_codec_cap_chan_count.BT_AUDIO_CODEC_CAP_CHAN_COUNT_1) | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_2](#c.bt_audio_codec_cap_chan_count.BT_AUDIO_CODEC_CAP_CHAN_COUNT_2) | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_3](#c.bt_audio_codec_cap_chan_count.BT_AUDIO_CODEC_CAP_CHAN_COUNT_3) | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_4](#c.bt_audio_codec_cap_chan_count.BT_AUDIO_CODEC_CAP_CHAN_COUNT_4) | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_5](#c.bt_audio_codec_cap_chan_count.BT_AUDIO_CODEC_CAP_CHAN_COUNT_5) | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_6](#c.bt_audio_codec_cap_chan_count.BT_AUDIO_CODEC_CAP_CHAN_COUNT_6) | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_7](#c.bt_audio_codec_cap_chan_count.BT_AUDIO_CODEC_CAP_CHAN_COUNT_7) | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_8](#c.bt_audio_codec_cap_chan_count.BT_AUDIO_CODEC_CAP_CHAN_COUNT_8))
        :   Supporting all channels.

    enum bt\_audio\_codec\_cfg\_type
    :   Codec configuration types.

        Used to build and parse codec configurations as specified in the ASCS and BAP specifications. Source is assigned numbers for Generic Audio, bluetooth.com.

        *Values:*

        enumerator BT\_AUDIO\_CODEC\_CFG\_FREQ = 0x01
        :   Sampling frequency.

        enumerator BT\_AUDIO\_CODEC\_CFG\_DURATION = 0x02
        :   Frame duration.

        enumerator BT\_AUDIO\_CODEC\_CFG\_CHAN\_ALLOC = 0x03
        :   Audio channel allocation.

        enumerator BT\_AUDIO\_CODEC\_CFG\_FRAME\_LEN = 0x04
        :   Octets per codec frame.

        enumerator BT\_AUDIO\_CODEC\_CFG\_FRAME\_BLKS\_PER\_SDU = 0x05
        :   Codec frame blocks per SDU.

    enum bt\_audio\_codec\_cfg\_freq
    :   *Values:*

        enumerator BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ = 0x01
        :   8 Khz codec sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CFG\_FREQ\_11KHZ = 0x02
        :   11.025 Khz codec sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ = 0x03
        :   16 Khz codec sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CFG\_FREQ\_22KHZ = 0x04
        :   22.05 Khz codec sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ = 0x05
        :   24 Khz codec sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ = 0x06
        :   32 Khz codec sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ = 0x07
        :   44.1 Khz codec sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ = 0x08
        :   48 Khz codec sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CFG\_FREQ\_88KHZ = 0x09
        :   88.2 Khz codec sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CFG\_FREQ\_96KHZ = 0x0a
        :   96 Khz codec sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CFG\_FREQ\_176KHZ = 0x0b
        :   176.4 Khz codec sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CFG\_FREQ\_192KHZ = 0x0c
        :   192 Khz codec sampling frequency

        enumerator BT\_AUDIO\_CODEC\_CFG\_FREQ\_384KHZ = 0x0d
        :   384 Khz codec sampling frequency

    enum bt\_audio\_codec\_cfg\_frame\_dur
    :   *Values:*

        enumerator BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5 = 0x00
        :   7.5 msec Frame Duration configuration

        enumerator BT\_AUDIO\_CODEC\_CFG\_DURATION\_10 = 0x01
        :   10 msec Frame Duration configuration

    enum bt\_audio\_context
    :   Audio Context Type for Generic Audio.

        These values are defined by the Generic Audio Assigned Numbers, bluetooth.com

        *Values:*

        enumerator BT\_AUDIO\_CONTEXT\_TYPE\_PROHIBITED = 0

        enumerator BT\_AUDIO\_CONTEXT\_TYPE\_UNSPECIFIED = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)

        enumerator BT\_AUDIO\_CONTEXT\_TYPE\_CONVERSATIONAL = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)

        enumerator BT\_AUDIO\_CONTEXT\_TYPE\_MEDIA = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)

        enumerator BT\_AUDIO\_CONTEXT\_TYPE\_GAME = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(3)

        enumerator BT\_AUDIO\_CONTEXT\_TYPE\_INSTRUCTIONAL = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(4)

        enumerator BT\_AUDIO\_CONTEXT\_TYPE\_VOICE\_ASSISTANTS = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(5)

        enumerator BT\_AUDIO\_CONTEXT\_TYPE\_LIVE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(6)

        enumerator BT\_AUDIO\_CONTEXT\_TYPE\_SOUND\_EFFECTS = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(7)

        enumerator BT\_AUDIO\_CONTEXT\_TYPE\_NOTIFICATIONS = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(8)

        enumerator BT\_AUDIO\_CONTEXT\_TYPE\_RINGTONE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(9)

        enumerator BT\_AUDIO\_CONTEXT\_TYPE\_ALERTS = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(10)

        enumerator BT\_AUDIO\_CONTEXT\_TYPE\_EMERGENCY\_ALARM = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(11)

    enum bt\_audio\_parental\_rating
    :   Parental rating defined by the Generic Audio assigned numbers (bluetooth.com).

        The numbering scheme is aligned with Annex F of EN 300 707 v1.2.1 which defined parental rating for viewing.

        *Values:*

        enumerator BT\_AUDIO\_PARENTAL\_RATING\_NO\_RATING = 0x00

        enumerator BT\_AUDIO\_PARENTAL\_RATING\_AGE\_ANY = 0x01

        enumerator BT\_AUDIO\_PARENTAL\_RATING\_AGE\_5\_OR\_ABOVE = 0x02

        enumerator BT\_AUDIO\_PARENTAL\_RATING\_AGE\_6\_OR\_ABOVE = 0x03

        enumerator BT\_AUDIO\_PARENTAL\_RATING\_AGE\_7\_OR\_ABOVE = 0x04

        enumerator BT\_AUDIO\_PARENTAL\_RATING\_AGE\_8\_OR\_ABOVE = 0x05

        enumerator BT\_AUDIO\_PARENTAL\_RATING\_AGE\_9\_OR\_ABOVE = 0x06

        enumerator BT\_AUDIO\_PARENTAL\_RATING\_AGE\_10\_OR\_ABOVE = 0x07

        enumerator BT\_AUDIO\_PARENTAL\_RATING\_AGE\_11\_OR\_ABOVE = 0x08

        enumerator BT\_AUDIO\_PARENTAL\_RATING\_AGE\_12\_OR\_ABOVE = 0x09

        enumerator BT\_AUDIO\_PARENTAL\_RATING\_AGE\_13\_OR\_ABOVE = 0x0A

        enumerator BT\_AUDIO\_PARENTAL\_RATING\_AGE\_14\_OR\_ABOVE = 0x0B

        enumerator BT\_AUDIO\_PARENTAL\_RATING\_AGE\_15\_OR\_ABOVE = 0x0C

        enumerator BT\_AUDIO\_PARENTAL\_RATING\_AGE\_16\_OR\_ABOVE = 0x0D

        enumerator BT\_AUDIO\_PARENTAL\_RATING\_AGE\_17\_OR\_ABOVE = 0x0E

        enumerator BT\_AUDIO\_PARENTAL\_RATING\_AGE\_18\_OR\_ABOVE = 0x0F

    enum bt\_audio\_active\_state
    :   Audio Active State defined by the Generic Audio assigned numbers (bluetooth.com).

        *Values:*

        enumerator BT\_AUDIO\_ACTIVE\_STATE\_DISABLED = 0x00

        enumerator BT\_AUDIO\_ACTIVE\_STATE\_ENABLED = 0x01

    enum bt\_audio\_metadata\_type
    :   Codec metadata type IDs.

        Metadata types defined by the Generic Audio assigned numbers (bluetooth.com).

        *Values:*

        enumerator BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT = 0x01
        :   Preferred audio context.

            Bitfield of preferred audio contexts.

            If 0, the context type is not a preferred use case for this codec configuration.

            See the BT\_AUDIO\_CONTEXT\_\* for valid values.

        enumerator BT\_AUDIO\_METADATA\_TYPE\_STREAM\_CONTEXT = 0x02
        :   Streaming audio context.

            Bitfield of streaming audio contexts.

            If 0, the context type is not a preferred use case for this codec configuration.

            See the BT\_AUDIO\_CONTEXT\_\* for valid values.

        enumerator BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO = 0x03
        :   UTF-8 encoded title or summary of stream content.

        enumerator BT\_AUDIO\_METADATA\_TYPE\_STREAM\_LANG = 0x04
        :   Stream language.

            3 octet lower case language code defined by ISO 639-3

        enumerator BT\_AUDIO\_METADATA\_TYPE\_CCID\_LIST = 0x05
        :   Array of 8-bit CCID values.

        enumerator BT\_AUDIO\_METADATA\_TYPE\_PARENTAL\_RATING = 0x06
        :   Parental rating.

            See [bt\_audio\_parental\_rating](#group__bt__audio_1ga6d4aff1f93dc0b902e4b5d1355f15760) for valid values.

        enumerator BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO\_URI = 0x07
        :   UTF-8 encoded URI for additional Program information.

        enumerator BT\_AUDIO\_METADATA\_TYPE\_AUDIO\_STATE = 0x08
        :   Audio active state.

            See [bt\_audio\_active\_state](#group__bt__audio_1ga16d403ec4db7be997682331ad365ff5f) for valid values.

        enumerator BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_IMMEDIATE = 0x09
        :   Broadcast Audio Immediate Rendering flag.

        enumerator BT\_AUDIO\_METADATA\_TYPE\_EXTENDED = 0xFE
        :   Extended metadata.

        enumerator BT\_AUDIO\_METADATA\_TYPE\_VENDOR = 0xFF
        :   Vendor specific metadata.

    enum bt\_audio\_location
    :   Location values for BT Audio.

        These values are defined by the Generic Audio Assigned Numbers, bluetooth.com

        *Values:*

        enumerator BT\_AUDIO\_LOCATION\_MONO\_AUDIO = 0

        enumerator BT\_AUDIO\_LOCATION\_FRONT\_LEFT = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)

        enumerator BT\_AUDIO\_LOCATION\_FRONT\_RIGHT = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)

        enumerator BT\_AUDIO\_LOCATION\_FRONT\_CENTER = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)

        enumerator BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_1 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(3)

        enumerator BT\_AUDIO\_LOCATION\_BACK\_LEFT = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(4)

        enumerator BT\_AUDIO\_LOCATION\_BACK\_RIGHT = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(5)

        enumerator BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_OF\_CENTER = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(6)

        enumerator BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_OF\_CENTER = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(7)

        enumerator BT\_AUDIO\_LOCATION\_BACK\_CENTER = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(8)

        enumerator BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_2 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(9)

        enumerator BT\_AUDIO\_LOCATION\_SIDE\_LEFT = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(10)

        enumerator BT\_AUDIO\_LOCATION\_SIDE\_RIGHT = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(11)

        enumerator BT\_AUDIO\_LOCATION\_TOP\_FRONT\_LEFT = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(12)

        enumerator BT\_AUDIO\_LOCATION\_TOP\_FRONT\_RIGHT = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(13)

        enumerator BT\_AUDIO\_LOCATION\_TOP\_FRONT\_CENTER = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(14)

        enumerator BT\_AUDIO\_LOCATION\_TOP\_CENTER = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(15)

        enumerator BT\_AUDIO\_LOCATION\_TOP\_BACK\_LEFT = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(16)

        enumerator BT\_AUDIO\_LOCATION\_TOP\_BACK\_RIGHT = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(17)

        enumerator BT\_AUDIO\_LOCATION\_TOP\_SIDE\_LEFT = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(18)

        enumerator BT\_AUDIO\_LOCATION\_TOP\_SIDE\_RIGHT = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(19)

        enumerator BT\_AUDIO\_LOCATION\_TOP\_BACK\_CENTER = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(20)

        enumerator BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_CENTER = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(21)

        enumerator BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_LEFT = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(22)

        enumerator BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_RIGHT = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(23)

        enumerator BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_WIDE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(24)

        enumerator BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_WIDE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(25)

        enumerator BT\_AUDIO\_LOCATION\_LEFT\_SURROUND = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(26)

        enumerator BT\_AUDIO\_LOCATION\_RIGHT\_SURROUND = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(27)

    enum bt\_audio\_dir
    :   Audio Capability type.

        *Values:*

        enumerator BT\_AUDIO\_DIR\_SINK = 0x01

        enumerator BT\_AUDIO\_DIR\_SOURCE = 0x02

    enum bt\_audio\_codec\_qos\_framing
    :   Codec QoS Framing.

        *Values:*

        enumerator BT\_AUDIO\_CODEC\_QOS\_FRAMING\_UNFRAMED = 0x00

        enumerator BT\_AUDIO\_CODEC\_QOS\_FRAMING\_FRAMED = 0x01

    enum [anonymous]
    :   Codec QoS Preferred PHY.

        *Values:*

        enumerator BT\_AUDIO\_CODEC\_QOS\_1M = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)

        enumerator BT\_AUDIO\_CODEC\_QOS\_2M = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)

        enumerator BT\_AUDIO\_CODEC\_QOS\_CODED = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)

    Functions

    int bt\_audio\_data\_parse(const uint8\_t ltv[], size\_t size, bool (\*func)(struct [bt\_data](gap.md#c.bt_data "bt_data") \*data, void \*user\_data), void \*user\_data)
    :   Helper for parsing length-type-value data.

        Parameters:
        :   - **ltv** – Length-type-value (LTV) encoded data.
            - **size** – Size of the `ltv` data.
            - **func** – Callback function which will be called for each element that’s found in the data. The callback should return true to continue parsing, or false to stop parsing.
            - **user\_data** – User data to be passed to the callback.

        Return values:
        :   - **0** – if all entries were parsed.
            - **-EINVAL** – if the data is incorrectly encoded
            - **-ECANCELED** – if parsing was prematurely cancelled by the callback

    struct bt\_audio\_codec\_octets\_per\_codec\_frame
    :   *#include <audio.h>*

        Public Members

        uint16\_t min
        :   Minimum number of octets supported per codec frame.

        uint16\_t max
        :   Maximum number of octets supported per codec frame.

    struct bt\_audio\_codec\_cap
    :   *#include <audio.h>*

        Codec capability structure.

        Public Members

        uint8\_t path\_id
        :   Data path ID.

            BT\_ISO\_DATA\_PATH\_HCI for HCI path, or any other value for vendor specific ID.

        bool ctlr\_transcode
        :   Whether or not the local controller should transcode.

            This effectively sets the coding format for the ISO data path to BT\_HCI\_CODING\_FORMAT\_TRANSPARENT if false, else uses the [bt\_audio\_codec\_cfg::id](#structbt__audio__codec__cfg_1aa2f99ec31ff3eb9b7b738bc8a1170f20).

        uint8\_t id
        :   Codec ID.

        uint16\_t cid
        :   Codec Company ID.

        uint16\_t vid
        :   Codec Company Vendor ID.

    struct bt\_audio\_codec\_cfg
    :   *#include <audio.h>*

        Codec specific configuration structure.

        Public Members

        uint8\_t path\_id
        :   Data path ID.

            BT\_ISO\_DATA\_PATH\_HCI for HCI path, or any other value for vendor specific ID.

        bool ctlr\_transcode
        :   Whether or not the local controller should transcode.

            This effectively sets the coding format for the ISO data path to BT\_HCI\_CODING\_FORMAT\_TRANSPARENT if false, else uses the [bt\_audio\_codec\_cfg::id](#structbt__audio__codec__cfg_1aa2f99ec31ff3eb9b7b738bc8a1170f20).

        uint8\_t id
        :   Codec ID.

        uint16\_t cid
        :   Codec Company ID.

        uint16\_t vid
        :   Codec Company Vendor ID.

    struct bt\_audio\_codec\_qos
    :   *#include <audio.h>*

        Codec QoS structure.

        Public Members

        uint8\_t phy
        :   QoS PHY.

        enum [bt\_audio\_codec\_qos\_framing](#c.bt_audio_codec_qos_framing) framing
        :   QoS Framing.

        uint8\_t rtn
        :   QoS Retransmission Number.

        uint16\_t sdu
        :   QoS SDU.

        uint32\_t interval
        :   QoS Frame Interval.

        uint32\_t pd
        :   QoS Presentation Delay in microseconds.

            Value range 0 to [BT\_AUDIO\_PD\_MAX](#group__bt__audio_1gaaa0414a4baef5a867fd1c6b1865d2dbc).

    struct bt\_audio\_codec\_qos\_pref
    :   *#include <audio.h>*

        Audio Stream Quality of Service Preference structure.

        Public Members

        bool unframed\_supported
        :   Unframed PDUs supported.

            Unlike the other fields, this is not a preference but whether the codec supports unframed ISOAL PDUs.

        uint8\_t phy
        :   Preferred PHY.

        uint8\_t rtn
        :   Preferred Retransmission Number.

        uint16\_t latency
        :   Preferred Transport Latency.

        uint32\_t pd\_min
        :   Minimum Presentation Delay in microseconds.

            Unlike the other fields, this is not a preference but a minimum requirement.

            Value range 0 to [BT\_AUDIO\_PD\_MAX](#group__bt__audio_1gaaa0414a4baef5a867fd1c6b1865d2dbc), or [BT\_AUDIO\_PD\_PREF\_NONE](#group__bt__audio_1ga663ab7bf74d56f36ee6cc80b369cbc16) to indicate no preference.

        uint32\_t pd\_max
        :   Maximum Presentation Delay.

            Unlike the other fields, this is not a preference but a maximum requirement.

            Value range 0 to [BT\_AUDIO\_PD\_MAX](#group__bt__audio_1gaaa0414a4baef5a867fd1c6b1865d2dbc), or [BT\_AUDIO\_PD\_PREF\_NONE](#group__bt__audio_1ga663ab7bf74d56f36ee6cc80b369cbc16) to indicate no preference.

        uint32\_t pref\_pd\_min
        :   Preferred minimum Presentation Delay.

            Value range 0 to [BT\_AUDIO\_PD\_MAX](#group__bt__audio_1gaaa0414a4baef5a867fd1c6b1865d2dbc).

        uint32\_t pref\_pd\_max
        :   Preferred maximum Presentation Delay.

            Value range 0 to [BT\_AUDIO\_PD\_MAX](#group__bt__audio_1gaaa0414a4baef5a867fd1c6b1865d2dbc).

*group* bt\_audio\_codec\_cfg
:   Audio codec Config APIs.

    Functions to parse codec config data when formatted as LTV wrapped into [Codec config parsing APIs](#group__bt__audio__codec__cfg).

    Functions

    int bt\_audio\_codec\_cfg\_freq\_to\_freq\_hz(enum [bt\_audio\_codec\_cfg\_freq](#c.bt_audio_codec_cfg_freq) freq)
    :   Convert assigned numbers frequency to frequency value.

        Parameters:
        :   - **freq** – The assigned numbers frequency to convert.

        Return values:
        :   - **-EINVAL** – if arguments are invalid.
            - **The** – converted frequency value in Hz.

    int bt\_audio\_codec\_cfg\_freq\_hz\_to\_freq(uint32\_t freq\_hz)
    :   Convert frequency value to assigned numbers frequency.

        Parameters:
        :   - **freq\_hz** – The frequency value to convert.

        Return values:
        :   - **-EINVAL** – if arguments are invalid.
            - **The** – assigned numbers frequency ([bt\_audio\_codec\_cfg\_freq](#group__bt__audio_1ga8e99fb678cc011bb8c9f6e1858bae0d7)).

    int bt\_audio\_codec\_cfg\_get\_freq(const struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg)
    :   Extract the frequency from a codec configuration.

        Parameters:
        :   - **codec\_cfg** – The codec configuration to extract data from.

        Return values:
        :   - **A** – [bt\_audio\_codec\_cfg\_freq](#group__bt__audio_1ga8e99fb678cc011bb8c9f6e1858bae0d7) value
            - **-EINVAL** – if arguments are invalid
            - **-ENODATA** – if not found
            - **-EBADMSG** – if found value has invalid size or value

    int bt\_audio\_codec\_cfg\_set\_freq(struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, enum [bt\_audio\_codec\_cfg\_freq](#c.bt_audio_codec_cfg_freq) freq)
    :   Set the frequency of a codec configuration.

        Parameters:
        :   - **codec\_cfg** – The codec configuration to set data for.
            - **freq** – The assigned numbers frequency to set.

        Return values:
        :   - **The** – data\_len of `codec_cfg` on success
            - **-EINVAL** – if arguments are invalid
            - **-ENOMEM** – if the new value could not set or added due to memory

    int bt\_audio\_codec\_cfg\_frame\_dur\_to\_frame\_dur\_us(enum [bt\_audio\_codec\_cfg\_frame\_dur](#c.bt_audio_codec_cfg_frame_dur) frame\_dur)
    :   Convert assigned numbers frame duration to duration in microseconds.

        Parameters:
        :   - **frame\_dur** – The assigned numbers frame duration to convert.

        Return values:
        :   - **-EINVAL** – if arguments are invalid.
            - **The** – converted frame duration value in microseconds.

    int bt\_audio\_codec\_cfg\_frame\_dur\_us\_to\_frame\_dur(uint32\_t frame\_dur\_us)
    :   Convert frame duration in microseconds to assigned numbers frame duration.

        Parameters:
        :   - **frame\_dur\_us** – The frame duration in microseconds to convert.

        Return values:
        :   - **-EINVAL** – if arguments are invalid.
            - **The** – assigned numbers frame duration ([bt\_audio\_codec\_cfg\_frame\_dur](#group__bt__audio_1ga83701b5eadfcbc9b84dc0b1a85ebeb74)).

    int bt\_audio\_codec\_cfg\_get\_frame\_dur(const struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg)
    :   Extract frame duration from BT codec config.

        Parameters:
        :   - **codec\_cfg** – The codec configuration to extract data from.

        Return values:
        :   - **A** – [bt\_audio\_codec\_cfg\_frame\_dur](#group__bt__audio_1ga83701b5eadfcbc9b84dc0b1a85ebeb74) value
            - **-EINVAL** – if arguments are invalid
            - **-ENODATA** – if not found
            - **-EBADMSG** – if found value has invalid size or value

    int bt\_audio\_codec\_cfg\_set\_frame\_dur(struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, enum [bt\_audio\_codec\_cfg\_frame\_dur](#c.bt_audio_codec_cfg_frame_dur) frame\_dur)
    :   Set the frame duration of a codec configuration.

        Parameters:
        :   - **codec\_cfg** – The codec configuration to set data for.
            - **frame\_dur** – The assigned numbers frame duration to set.

        Return values:
        :   - **The** – data\_len of `codec_cfg` on success
            - **-EINVAL** – if arguments are invalid
            - **-ENOMEM** – if the new value could not set or added due to memory

    int bt\_audio\_codec\_cfg\_get\_chan\_allocation(const struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, enum [bt\_audio\_location](#c.bt_audio_location) \*chan\_allocation)
    :   Extract channel allocation from BT codec config.

        The value returned is a bit field representing one or more audio locations as specified by [bt\_audio\_location](#group__bt__audio_1ga61230848c02098352320fe751332c4e8) Shall match one or more of the bits set in BT\_PAC\_SNK\_LOC/BT\_PAC\_SRC\_LOC.

        Up to the configured [BT\_AUDIO\_CODEC\_CAP\_TYPE\_CHAN\_COUNT](#group__bt__audio_1ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191) number of channels can be present.

        Parameters:
        :   - **codec\_cfg** – The codec configuration to extract data from.
            - **chan\_allocation** – Pointer to the variable to store the extracted value in.

        Return values:
        :   - **0** – if value is found and stored in the pointer provided
            - **-EINVAL** – if arguments are invalid
            - **-ENODATA** – if not found
            - **-EBADMSG** – if found value has invalid size or value

    int bt\_audio\_codec\_cfg\_set\_chan\_allocation(struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, enum [bt\_audio\_location](#c.bt_audio_location) chan\_allocation)
    :   Set the channel allocation of a codec configuration.

        Parameters:
        :   - **codec\_cfg** – The codec configuration to set data for.
            - **chan\_allocation** – The channel allocation to set.

        Return values:
        :   - **The** – data\_len of `codec_cfg` on success
            - **-EINVAL** – if arguments are invalid
            - **-ENOMEM** – if the new value could not set or added due to memory

    int bt\_audio\_codec\_cfg\_get\_octets\_per\_frame(const struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg)
    :   Extract frame size in octets from BT codec config.

        The overall SDU size will be octets\_per\_frame \* blocks\_per\_sdu.

        The Bluetooth specificationa are not clear about this value - it does not state that the codec shall use this SDU size only. A codec like LC3 supports variable bit-rate (per SDU) hence it might be allowed for an encoder to reduce the frame size below this value. Hence it is recommended to use the received SDU size and divide by blocks\_per\_sdu rather than relying on this octets\_per\_sdu value to be fixed.

        Parameters:
        :   - **codec\_cfg** – The codec configuration to extract data from.

        Return values:
        :   - **Frame** – length in octets
            - **-EINVAL** – if arguments are invalid
            - **-ENODATA** – if not found
            - **-EBADMSG** – if found value has invalid size or value

    int bt\_audio\_codec\_cfg\_set\_octets\_per\_frame(struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, uint16\_t octets\_per\_frame)
    :   Set the octets per codec frame of a codec configuration.

        Parameters:
        :   - **codec\_cfg** – The codec configuration to set data for.
            - **octets\_per\_frame** – The octets per codec frame to set.

        Return values:
        :   - **The** – data\_len of `codec_cfg` on success
            - **-EINVAL** – if arguments are invalid
            - **-ENOMEM** – if the new value could not set or added due to memory

    int bt\_audio\_codec\_cfg\_get\_frame\_blocks\_per\_sdu(const struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, bool fallback\_to\_default)
    :   Extract number of audio frame blockss in each SDU from BT codec config.

        The overall SDU size will be octets\_per\_frame \* frame\_blocks\_per\_sdu \* number-of-channels.

        If this value is not present a default value of 1 shall be used.

        A frame block is one or more frames that represents data for the same period of time but for different channels. If the stream have two audio channels and this value is two there will be four frames in the SDU.

        Parameters:
        :   - **codec\_cfg** – The codec configuration to extract data from.
            - **fallback\_to\_default** – If true this function will return the default value of 1 if the type is not found. In this case the function will only fail if a NULL pointer is provided.

        Return values:
        :   - **The** – count of codec frames in each SDU if value is found else of `fallback_to_default` is true then the value 1 is returned if frames per sdu is not found.
            - **-EINVAL** – if arguments are invalid
            - **-ENODATA** – if not found
            - **-EBADMSG** – if found value has invalid size or value

    int bt\_audio\_codec\_cfg\_set\_frame\_blocks\_per\_sdu(struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, uint8\_t frame\_blocks)
    :   Set the frame blocks per SDU of a codec configuration.

        Parameters:
        :   - **codec\_cfg** – The codec configuration to set data for.
            - **frame\_blocks** – The frame blocks per SDU to set.

        Return values:
        :   - **The** – data\_len of `codec_cfg` on success
            - **-EINVAL** – if arguments are invalid
            - **-ENOMEM** – if the new value could not set or added due to memory

    int bt\_audio\_codec\_cfg\_get\_val(const struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, enum [bt\_audio\_codec\_cfg\_type](#c.bt_audio_codec_cfg_type) type, const uint8\_t \*\*data)
    :   Lookup a specific codec configuration value.

        Parameters:
        :   - **codec\_cfg** – **[in]** The codec data to search in.
            - **type** – **[in]** The type id to look for
            - **data** – **[out]** Pointer to the data-pointer to update when item is found

        Return values:
        :   - **Length** – of found `data` (may be 0)
            - **-EINVAL** – if arguments are invalid
            - **-ENODATA** – if not found

    int bt\_audio\_codec\_cfg\_set\_val(struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, enum [bt\_audio\_codec\_cfg\_type](#c.bt_audio_codec_cfg_type) type, const uint8\_t \*data, size\_t data\_len)
    :   Set or add a specific codec configuration value.

        Parameters:
        :   - **codec\_cfg** – The codec data to set the value in.
            - **type** – The type id to set
            - **data** – Pointer to the data-pointer to set
            - **data\_len** – Length of `data`

        Return values:
        :   - **The** – data\_len of `codec_cfg` on success
            - **-EINVAL** – if arguments are invalid
            - **-ENOMEM** – if the new value could not set or added due to memory

    int bt\_audio\_codec\_cfg\_unset\_val(struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, enum [bt\_audio\_codec\_cfg\_type](#c.bt_audio_codec_cfg_type) type)
    :   Unset a specific codec configuration value.

        The type and the value will be removed from the codec configuration.

        Parameters:
        :   - **codec\_cfg** – The codec data to set the value in.
            - **type** – The type id to unset.

        Return values:
        :   - **The** – data\_len of `codec_cfg` on success
            - **-EINVAL** – if arguments are invalid

    int bt\_audio\_codec\_cfg\_meta\_get\_val(const struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, uint8\_t type, const uint8\_t \*\*data)
    :   Lookup a specific metadata value based on type.

        Parameters:
        :   - **codec\_cfg** – **[in]** The codec data to search in.
            - **type** – **[in]** The type id to look for
            - **data** – **[out]** Pointer to the data-pointer to update when item is found

        Return values:
        :   - **Length** – of found `data` (may be 0)
            - **-EINVAL** – if arguments are invalid
            - **-ENODATA** – if not found

    int bt\_audio\_codec\_cfg\_meta\_set\_val(struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, enum [bt\_audio\_metadata\_type](#c.bt_audio_metadata_type) type, const uint8\_t \*data, size\_t data\_len)
    :   Set or add a specific codec configuration metadata value.

        Parameters:
        :   - **codec\_cfg** – The codec configuration to set the value in.
            - **type** – The type id to set.
            - **data** – Pointer to the data-pointer to set.
            - **data\_len** – Length of `data`.

        Return values:
        :   - **The** – meta\_len of `codec_cfg` on success
            - **-EINVAL** – if arguments are invalid
            - **-ENOMEM** – if the new value could not set or added due to memory

    int bt\_audio\_codec\_cfg\_meta\_unset\_val(struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, enum [bt\_audio\_metadata\_type](#c.bt_audio_metadata_type) type)
    :   Unset a specific codec configuration metadata value.

        The type and the value will be removed from the codec configuration metadata.

        Parameters:
        :   - **codec\_cfg** – The codec data to set the value in.
            - **type** – The type id to unset.

        Return values:
        :   - **The** – meta\_len of `codec_cfg` on success
            - **-EINVAL** – if arguments are invalid

    int bt\_audio\_codec\_cfg\_meta\_get\_pref\_context(const struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg)
    :   Extract preferred contexts.

        See [BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT](#group__bt__audio_1ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a) for more information about this value.

        Parameters:
        :   - **codec\_cfg** – The codec data to search in.

        Return values:
        :   - **The** – preferred context type if positive or 0
            - **-EINVAL** – if arguments are invalid
            - **-ENODATA** – if not found
            - **-EBADMSG** – if found value has invalid size

    int bt\_audio\_codec\_cfg\_meta\_set\_pref\_context(struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, enum [bt\_audio\_context](#c.bt_audio_context) ctx)
    :   Set the preferred context of a codec configuration metadata.

        Parameters:
        :   - **codec\_cfg** – The codec configuration to set data for.
            - **ctx** – The preferred context to set.

        Return values:
        :   - **The** – data\_len of `codec_cfg` on success
            - **-EINVAL** – if arguments are invalid
            - **-ENOMEM** – if the new value could not set or added due to memory

    int bt\_audio\_codec\_cfg\_meta\_get\_stream\_context(const struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg)
    :   Extract stream contexts.

        See [BT\_AUDIO\_METADATA\_TYPE\_STREAM\_CONTEXT](#group__bt__audio_1ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa) for more information about this value.

        Parameters:
        :   - **codec\_cfg** – The codec data to search in.

        Return values:
        :   - **The** – stream context type if positive or 0
            - **-EINVAL** – if arguments are invalid
            - **-ENODATA** – if not found
            - **-EBADMSG** – if found value has invalid size

    int bt\_audio\_codec\_cfg\_meta\_set\_stream\_context(struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, enum [bt\_audio\_context](#c.bt_audio_context) ctx)
    :   Set the stream context of a codec configuration metadata.

        Parameters:
        :   - **codec\_cfg** – The codec configuration to set data for.
            - **ctx** – The stream context to set.

        Return values:
        :   - **The** – data\_len of `codec_cfg` on success
            - **-EINVAL** – if arguments are invalid
            - **-ENOMEM** – if the new value could not set or added due to memory

    int bt\_audio\_codec\_cfg\_meta\_get\_program\_info(const struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, const uint8\_t \*\*program\_info)
    :   Extract program info.

        See [BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO](#group__bt__audio_1ggab53d0dd62bceff97cf8eed7d8cf80354a02f91ea7fb6be631687d843ad7bf4ac7) for more information about this value.

        Parameters:
        :   - **codec\_cfg** – **[in]** The codec data to search in.
            - **program\_info** – **[out]** Pointer to the UTF-8 formatted program info.

        Return values:
        :   - **The** – length of the `program_info` (may be 0)
            - **-EINVAL** – if arguments are invalid
            - **-ENODATA** – if not found

    int bt\_audio\_codec\_cfg\_meta\_set\_program\_info(struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, const uint8\_t \*program\_info, size\_t program\_info\_len)
    :   Set the program info of a codec configuration metadata.

        Parameters:
        :   - **codec\_cfg** – The codec configuration to set data for.
            - **program\_info** – The program info to set.
            - **program\_info\_len** – The length of `program_info`.

        Return values:
        :   - **The** – data\_len of `codec_cfg` on success
            - **-EINVAL** – if arguments are invalid
            - **-ENOMEM** – if the new value could not set or added due to memory

    int bt\_audio\_codec\_cfg\_meta\_get\_stream\_lang(const struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg)
    :   Extract stream language.

        See [BT\_AUDIO\_METADATA\_TYPE\_STREAM\_LANG](#group__bt__audio_1ggab53d0dd62bceff97cf8eed7d8cf80354ae98c430a422e3583d19d1b391b97edda) for more information about this value.

        Parameters:
        :   - **codec\_cfg** – The codec data to search in.

        Return values:
        :   - **The** – stream language if positive or 0
            - **-EINVAL** – if arguments are invalid
            - **-ENODATA** – if not found
            - **-EBADMSG** – if found value has invalid size

    int bt\_audio\_codec\_cfg\_meta\_set\_stream\_lang(struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, uint32\_t stream\_lang)
    :   Set the stream language of a codec configuration metadata.

        Parameters:
        :   - **codec\_cfg** – The codec configuration to set data for.
            - **stream\_lang** – The 24-bit stream language to set.

        Return values:
        :   - **The** – data\_len of `codec_cfg` on success
            - **-EINVAL** – if arguments are invalid
            - **-ENOMEM** – if the new value could not set or added due to memory

    int bt\_audio\_codec\_cfg\_meta\_get\_ccid\_list(const struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, const uint8\_t \*\*ccid\_list)
    :   Extract CCID list.

        See [BT\_AUDIO\_METADATA\_TYPE\_CCID\_LIST](#group__bt__audio_1ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b) for more information about this value.

        Parameters:
        :   - **codec\_cfg** – **[in]** The codec data to search in.
            - **ccid\_list** – **[out]** Pointer to the array containing 8-bit CCIDs.

        Return values:
        :   - **The** – length of the `ccid_list` (may be 0)
            - **-EINVAL** – if arguments are invalid
            - **-ENODATA** – if not found

    int bt\_audio\_codec\_cfg\_meta\_set\_ccid\_list(struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, const uint8\_t \*ccid\_list, size\_t ccid\_list\_len)
    :   Set the CCID list of a codec configuration metadata.

        Parameters:
        :   - **codec\_cfg** – The codec configuration to set data for.
            - **ccid\_list** – The program info to set.
            - **ccid\_list\_len** – The length of `ccid_list`.

        Return values:
        :   - **The** – data\_len of `codec_cfg` on success
            - **-EINVAL** – if arguments are invalid
            - **-ENOMEM** – if the new value could not set or added due to memory

    int bt\_audio\_codec\_cfg\_meta\_get\_parental\_rating(const struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg)
    :   Extract parental rating.

        See [BT\_AUDIO\_METADATA\_TYPE\_PARENTAL\_RATING](#group__bt__audio_1ggab53d0dd62bceff97cf8eed7d8cf80354a7a83f397dc5dbe6e6d60a994cccdc613) for more information about this value.

        Parameters:
        :   - **codec\_cfg** – The codec data to search in.

        Return values:
        :   - **The** – parental rating if positive or 0
            - **-EINVAL** – if arguments are invalid
            - **-ENODATA** – if not found
            - **-EBADMSG** – if found value has invalid size

    int bt\_audio\_codec\_cfg\_meta\_set\_parental\_rating(struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, enum [bt\_audio\_parental\_rating](#c.bt_audio_parental_rating) parental\_rating)
    :   Set the parental rating of a codec configuration metadata.

        Parameters:
        :   - **codec\_cfg** – The codec configuration to set data for.
            - **parental\_rating** – The parental rating to set.

        Return values:
        :   - **The** – data\_len of `codec_cfg` on success
            - **-EINVAL** – if arguments are invalid
            - **-ENOMEM** – if the new value could not set or added due to memory

    int bt\_audio\_codec\_cfg\_meta\_get\_program\_info\_uri(const struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, const uint8\_t \*\*program\_info\_uri)
    :   Extract program info URI.

        See [BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO\_URI](#group__bt__audio_1ggab53d0dd62bceff97cf8eed7d8cf80354a58971ea21b5045e56a0e1ca838358922) for more information about this value.

        Parameters:
        :   - **codec\_cfg** – **[in]** The codec data to search in.
            - **program\_info\_uri** – **[out]** Pointer to the UTF-8 formatted program info URI.

        Return values:
        :   - **The** – length of the `ccid_list` (may be 0)
            - **-EINVAL** – if arguments are invalid
            - **-ENODATA** – if not found

    int bt\_audio\_codec\_cfg\_meta\_set\_program\_info\_uri(struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, const uint8\_t \*program\_info\_uri, size\_t program\_info\_uri\_len)
    :   Set the program info URI of a codec configuration metadata.

        Parameters:
        :   - **codec\_cfg** – The codec configuration to set data for.
            - **program\_info\_uri** – The program info URI to set.
            - **program\_info\_uri\_len** – The length of `program_info_uri`.

        Return values:
        :   - **The** – data\_len of `codec_cfg` on success
            - **-EINVAL** – if arguments are invalid
            - **-ENOMEM** – if the new value could not set or added due to memory

    int bt\_audio\_codec\_cfg\_meta\_get\_audio\_active\_state(const struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg)
    :   Extract audio active state.

        See [BT\_AUDIO\_METADATA\_TYPE\_AUDIO\_STATE](#group__bt__audio_1ggab53d0dd62bceff97cf8eed7d8cf80354af220c40d351ec5e236cd41a5944da5fc) for more information about this value.

        Parameters:
        :   - **codec\_cfg** – The codec data to search in.

        Return values:
        :   - **The** – preferred context type if positive or 0
            - **-EINVAL** – if arguments are invalid
            - **-ENODATA** – if not found
            - **-EBADMSG** – if found value has invalid size

    int bt\_audio\_codec\_cfg\_meta\_set\_audio\_active\_state(struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, enum [bt\_audio\_active\_state](#c.bt_audio_active_state) state)
    :   Set the audio active state of a codec configuration metadata.

        Parameters:
        :   - **codec\_cfg** – The codec configuration to set data for.
            - **state** – The audio active state to set.

        Return values:
        :   - **The** – data\_len of `codec_cfg` on success
            - **-EINVAL** – if arguments are invalid
            - **-ENOMEM** – if the new value could not set or added due to memory

    int bt\_audio\_codec\_cfg\_meta\_get\_bcast\_audio\_immediate\_rend\_flag(const struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg)
    :   Extract broadcast audio immediate rendering flag.

        See [BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_IMMEDIATE](#group__bt__audio_1ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1) for more information about this value.

        Parameters:
        :   - **codec\_cfg** – The codec data to search in.

        Return values:
        :   - **0** – if the flag was found
            - **-EINVAL** – if arguments are invalid
            - **-ENODATA** – if not the flag was not found

    int bt\_audio\_codec\_cfg\_meta\_set\_bcast\_audio\_immediate\_rend\_flag(struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg)
    :   Set the broadcast audio immediate rendering flag of a codec configuration metadata.

        Parameters:
        :   - **codec\_cfg** – The codec configuration to set data for.

        Return values:
        :   - **The** – data\_len of `codec_cfg` on success
            - **-EINVAL** – if arguments are invalid
            - **-ENOMEM** – if the new value could not set or added due to memory

    int bt\_audio\_codec\_cfg\_meta\_get\_extended(const struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, const uint8\_t \*\*extended\_meta)
    :   Extract extended metadata.

        See [BT\_AUDIO\_METADATA\_TYPE\_EXTENDED](#group__bt__audio_1ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39) for more information about this value.

        Parameters:
        :   - **codec\_cfg** – **[in]** The codec data to search in.
            - **extended\_meta** – **[out]** Pointer to the extended metadata.

        Return values:
        :   - **The** – length of the `ccid_list` (may be 0)
            - **-EINVAL** – if arguments are invalid
            - **-ENODATA** – if not found

    int bt\_audio\_codec\_cfg\_meta\_set\_extended(struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, const uint8\_t \*extended\_meta, size\_t extended\_meta\_len)
    :   Set the extended metadata of a codec configuration metadata.

        Parameters:
        :   - **codec\_cfg** – The codec configuration to set data for.
            - **extended\_meta** – The extended metadata to set.
            - **extended\_meta\_len** – The length of `extended_meta`.

        Return values:
        :   - **The** – data\_len of `codec_cfg` on success
            - **-EINVAL** – if arguments are invalid
            - **-ENOMEM** – if the new value could not set or added due to memory

    int bt\_audio\_codec\_cfg\_meta\_get\_vendor(const struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, const uint8\_t \*\*vendor\_meta)
    :   Extract vendor specific metadata.

        See [BT\_AUDIO\_METADATA\_TYPE\_VENDOR](#group__bt__audio_1ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286) for more information about this value.

        Parameters:
        :   - **codec\_cfg** – **[in]** The codec data to search in.
            - **vendor\_meta** – **[out]** Pointer to the vendor specific metadata.

        Return values:
        :   - **The** – length of the `ccid_list` (may be 0)
            - **-EINVAL** – if arguments are invalid
            - **-ENODATA** – if not found

    int bt\_audio\_codec\_cfg\_meta\_set\_vendor(struct [bt\_audio\_codec\_cfg](#c.bt_audio_codec_cfg) \*codec\_cfg, const uint8\_t \*vendor\_meta, size\_t vendor\_meta\_len)
    :   Set the vendor specific metadata of a codec configuration metadata.

        Parameters:
        :   - **codec\_cfg** – The codec configuration to set data for.
            - **vendor\_meta** – The vendor specific metadata to set.
            - **vendor\_meta\_len** – The length of `vendor_meta`.

        Return values:
        :   - **The** – data\_len of `codec_cfg` on success
            - **-EINVAL** – if arguments are invalid
            - **-ENOMEM** – if the new value could not set or added due to memory
