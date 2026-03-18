---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__audio__codec__cfg.html
original_path: doxygen/html/group__bt__audio__codec__cfg.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Codec config parsing APIs

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Audio](group__bt__audio.md)

Audio codec Config APIs.
[More...](#details)

| Functions | |
| --- | --- |
| int | [bt\_audio\_codec\_cfg\_freq\_to\_freq\_hz](#ga2e557fe726a49dc99754da16f7cc60af) (enum [bt\_audio\_codec\_cfg\_freq](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7) freq) |
|  | Convert assigned numbers frequency to frequency value. |
| int | [bt\_audio\_codec\_cfg\_freq\_hz\_to\_freq](#ga99ab4f6d2a18f2a9b4e3da47f63fc9e0) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) freq\_hz) |
|  | Convert frequency value to assigned numbers frequency. |
| int | [bt\_audio\_codec\_cfg\_get\_freq](#gad8525a57d35e3e34ea591f7e20e2512d) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Extract the frequency from a codec configuration. |
| int | [bt\_audio\_codec\_cfg\_set\_freq](#gac119989d5dcfa36becf4edd0ae7c6138) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_codec\_cfg\_freq](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7) freq) |
|  | Set the frequency of a codec configuration. |
| int | [bt\_audio\_codec\_cfg\_frame\_dur\_to\_frame\_dur\_us](#ga225e05df1f0d1efb709c972187901495) (enum [bt\_audio\_codec\_cfg\_frame\_dur](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74) frame\_dur) |
|  | Convert assigned numbers frame duration to duration in microseconds. |
| int | [bt\_audio\_codec\_cfg\_frame\_dur\_us\_to\_frame\_dur](#ga0782a3d9254fb76b441c6c2492571556) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) frame\_dur\_us) |
|  | Convert frame duration in microseconds to assigned numbers frame duration. |
| int | [bt\_audio\_codec\_cfg\_get\_frame\_dur](#ga2dd3afe41b22e989fb46614f89550007) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Extract frame duration from BT codec config. |
| int | [bt\_audio\_codec\_cfg\_set\_frame\_dur](#ga7d8306f98cb00f06e68a1df417825f0d) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_codec\_cfg\_frame\_dur](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74) frame\_dur) |
|  | Set the frame duration of a codec configuration. |
| int | [bt\_audio\_codec\_cfg\_get\_chan\_allocation](#gae712e0f8e84aeb4ad2528da34907e29d) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) \*chan\_allocation, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) fallback\_to\_default) |
|  | Extract channel allocation from BT codec config. |
| int | [bt\_audio\_codec\_cfg\_set\_chan\_allocation](#gafbbcd69fac18ed0201a5e0156209b049) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) chan\_allocation) |
|  | Set the channel allocation of a codec configuration. |
| int | [bt\_audio\_codec\_cfg\_get\_octets\_per\_frame](#ga503be053422217502d6108b045791e02) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Extract frame size in octets from BT codec config. |
| int | [bt\_audio\_codec\_cfg\_set\_octets\_per\_frame](#ga866cdec28194056dc9e274d0436b45c2) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) octets\_per\_frame) |
|  | Set the octets per codec frame of a codec configuration. |
| int | [bt\_audio\_codec\_cfg\_get\_frame\_blocks\_per\_sdu](#gadba0723f9d8a9546b659fba139051374) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) fallback\_to\_default) |
|  | Extract number of audio frame blocks in each SDU from BT codec config. |
| int | [bt\_audio\_codec\_cfg\_set\_frame\_blocks\_per\_sdu](#gac9cf20bafbe24b34034bfb6ee7aaf03e) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) frame\_blocks) |
|  | Set the frame blocks per SDU of a codec configuration. |
| int | [bt\_audio\_codec\_cfg\_get\_val](#ga707c679db0193197b56acabfb08f8d1f) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data) |
|  | Lookup a specific codec configuration value. |
| int | [bt\_audio\_codec\_cfg\_set\_val](#gab10f22938780530b1d1b95695382902e) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_len) |
|  | Set or add a specific codec configuration value. |
| int | [bt\_audio\_codec\_cfg\_unset\_val](#gad3857d0ca008854df5966501caa261ba) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974) type) |
|  | Unset a specific codec configuration value. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_val](#gae98335e87394a491b4a311d867a5e32d) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data) |
|  | Lookup a specific metadata value based on type. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_val](#ga3e24c2ba8de502600e647cb2f84e3ec4) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_len) |
|  | Set or add a specific codec configuration metadata value. |
| int | [bt\_audio\_codec\_cfg\_meta\_unset\_val](#gab46f830daa1d9a907f47eb2a9eed7337) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) type) |
|  | Unset a specific codec configuration metadata value. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_pref\_context](#gaea087663426a49bb6ff4859800aecb84) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) fallback\_to\_default) |
|  | Extract preferred contexts. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_pref\_context](#gab40bad609f17d24e7e0e9ffcebe4e912) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) ctx) |
|  | Set the preferred context of a codec configuration metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_stream\_context](#ga4cc4e1bb941206e7f1541a57fc92b8e9) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Extract stream contexts. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_stream\_context](#ga5cd2af1bb44c6eb5bafe824f005a77f0) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) ctx) |
|  | Set the stream context of a codec configuration metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_program\_info](#ga03284b8474d65443d7ecc8bdfc6f04c6) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*program\_info) |
|  | Extract program info. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_program\_info](#ga2ca9e616d20d7513c60ce905f046ac7b) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*program\_info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) program\_info\_len) |
|  | Set the program info of a codec configuration metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_lang](#ga55e3cbaeacf15fcb1f24a16eb28db99c) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*lang) |
|  | Extract language. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_lang](#ga54b7eadf072c397879c1dababa2a3be0) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) lang[3]) |
|  | Set the language of a codec configuration metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_ccid\_list](#gaa0f9b9f608c7af881d5a928a3ae397b2) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*ccid\_list) |
|  | Extract CCID list. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_ccid\_list](#ga59716b95fcea3404ff8c078564b0e29c) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ccid\_list, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ccid\_list\_len) |
|  | Set the CCID list of a codec configuration metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_parental\_rating](#gaf0eecb02a05f0cc2b75ae9fb32c03913) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Extract parental rating. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_parental\_rating](#gab5d8b5877de4fe16c0e06a1d4f0d15ce) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760) parental\_rating) |
|  | Set the parental rating of a codec configuration metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_program\_info\_uri](#ga6bdbc0a0b929fdbdc75db479aec858df) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*program\_info\_uri) |
|  | Extract program info URI. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_program\_info\_uri](#ga99163729034e816eaef7195505d5ae20) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*program\_info\_uri, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) program\_info\_uri\_len) |
|  | Set the program info URI of a codec configuration metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_audio\_active\_state](#ga0fd6e6baf1b4f22d60768aaed6f42e8e) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Extract audio active state. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_audio\_active\_state](#gaf869e7ce0c9dd467fb03e8503d36c58a) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_active\_state](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Set the audio active state of a codec configuration metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_bcast\_audio\_immediate\_rend\_flag](#ga66143aa7dcc726e06a12660b8f90fc5a) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Extract broadcast audio immediate rendering flag. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_bcast\_audio\_immediate\_rend\_flag](#gaede61b65d2037c7fbf6c4c4e090990be) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Set the broadcast audio immediate rendering flag of a codec configuration metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_extended](#ga1f76f82bff63b876eb761a0bf0377428) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*extended\_meta) |
|  | Extract extended metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_extended](#gade9cb53287ab3356fb57ba8a454a3aad) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*extended\_meta, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) extended\_meta\_len) |
|  | Set the extended metadata of a codec configuration metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_vendor](#ga4a4982e3bd0e8c944b584196ef146f6c) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*vendor\_meta) |
|  | Extract vendor specific metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_vendor](#ga6935d1c40b3178b0c8fa877ee93d1e53) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*vendor\_meta, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) vendor\_meta\_len) |
|  | Set the vendor specific metadata of a codec configuration metadata. |

## Detailed Description

Audio codec Config APIs.

Functions to parse codec config data when formatted as LTV wrapped into [Codec config parsing APIs](group__bt__audio__codec__cfg.md "Codec config parsing APIs").

## Function Documentation

## [◆ ](#ga225e05df1f0d1efb709c972187901495)bt\_audio\_codec\_cfg\_frame\_dur\_to\_frame\_dur\_us()

| int bt\_audio\_codec\_cfg\_frame\_dur\_to\_frame\_dur\_us | ( | enum [bt\_audio\_codec\_cfg\_frame\_dur](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74) | *frame\_dur* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Convert assigned numbers frame duration to duration in microseconds.

Parameters
:   | frame\_dur | The assigned numbers frame duration to convert. |
    | --- | --- |

Return values
:   | -EINVAL | if arguments are invalid. |
    | --- | --- |
    | The | converted frame duration value in microseconds. |

## [◆ ](#ga0782a3d9254fb76b441c6c2492571556)bt\_audio\_codec\_cfg\_frame\_dur\_us\_to\_frame\_dur()

| int bt\_audio\_codec\_cfg\_frame\_dur\_us\_to\_frame\_dur | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *frame\_dur\_us* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Convert frame duration in microseconds to assigned numbers frame duration.

Parameters
:   | frame\_dur\_us | The frame duration in microseconds to convert. |
    | --- | --- |

Return values
:   | -EINVAL | if arguments are invalid. |
    | --- | --- |
    | The | assigned numbers frame duration ([bt\_audio\_codec\_cfg\_frame\_dur](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74 "bt_audio_codec_cfg_frame_dur")). |

## [◆ ](#ga99ab4f6d2a18f2a9b4e3da47f63fc9e0)bt\_audio\_codec\_cfg\_freq\_hz\_to\_freq()

| int bt\_audio\_codec\_cfg\_freq\_hz\_to\_freq | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *freq\_hz* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Convert frequency value to assigned numbers frequency.

Parameters
:   | freq\_hz | The frequency value to convert. |
    | --- | --- |

Return values
:   | -EINVAL | if arguments are invalid. |
    | --- | --- |
    | The | assigned numbers frequency ([bt\_audio\_codec\_cfg\_freq](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7 "bt_audio_codec_cfg_freq")). |

## [◆ ](#ga2e557fe726a49dc99754da16f7cc60af)bt\_audio\_codec\_cfg\_freq\_to\_freq\_hz()

| int bt\_audio\_codec\_cfg\_freq\_to\_freq\_hz | ( | enum [bt\_audio\_codec\_cfg\_freq](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7) | *freq* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Convert assigned numbers frequency to frequency value.

Parameters
:   | freq | The assigned numbers frequency to convert. |
    | --- | --- |

Return values
:   | -EINVAL | if arguments are invalid. |
    | --- | --- |
    | The | converted frequency value in Hz. |

## [◆ ](#gae712e0f8e84aeb4ad2528da34907e29d)bt\_audio\_codec\_cfg\_get\_chan\_allocation()

| int bt\_audio\_codec\_cfg\_get\_chan\_allocation | ( | const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) \* | *chan\_allocation*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *fallback\_to\_default* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract channel allocation from BT codec config.

The value returned is a bit field representing one or more audio locations as specified by [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location") Shall match one or more of the bits set in BT\_PAC\_SNK\_LOC/BT\_PAC\_SRC\_LOC.

Up to the configured [BT\_AUDIO\_CODEC\_CAP\_TYPE\_CHAN\_COUNT](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191 "BT_AUDIO_CODEC_CAP_TYPE_CHAN_COUNT") number of channels can be present.

Parameters
:   | codec\_cfg | The codec configuration to extract data from. |
    | --- | --- |
    | chan\_allocation | Pointer to the variable to store the extracted value in. |
    | fallback\_to\_default | If true this function will provide the default value of [BT\_AUDIO\_LOCATION\_MONO\_AUDIO](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8f476de613cdcb2f9f677d40291aa5df "BT_AUDIO_LOCATION_MONO_AUDIO") if the type is not found when `codec_cfg.id` is [BT\_HCI\_CODING\_FORMAT\_LC3](hci__types_8h.md#a1fa62d6f28ef56ebe9c18d5ab86fbf8e "BT_HCI_CODING_FORMAT_LC3"). |

Return values
:   | 0 | if value is found and stored in the pointer provided |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENODATA | if not found |
    | -EBADMSG | if found value has invalid size or value |

## [◆ ](#gadba0723f9d8a9546b659fba139051374)bt\_audio\_codec\_cfg\_get\_frame\_blocks\_per\_sdu()

| int bt\_audio\_codec\_cfg\_get\_frame\_blocks\_per\_sdu | ( | const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *fallback\_to\_default* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract number of audio frame blocks in each SDU from BT codec config.

The overall SDU size will be octets\_per\_frame \* frame\_blocks\_per\_sdu \* number-of-channels.

If this value is not present a default value of 1 shall be used.

A frame block is one or more frames that represents data for the same period of time but for different channels. If the stream have two audio channels and this value is two there will be four frames in the SDU.

Parameters
:   | codec\_cfg | The codec configuration to extract data from. |
    | --- | --- |
    | fallback\_to\_default | If true this function will return the default value of 1 if the type is not found when `codec_cfg.id` is [BT\_HCI\_CODING\_FORMAT\_LC3](hci__types_8h.md#a1fa62d6f28ef56ebe9c18d5ab86fbf8e "BT_HCI_CODING_FORMAT_LC3"). |

Return values
:   | The | count of codec frame blocks in each SDU. |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENODATA | if not found |
    | -EBADMSG | if found value has invalid size or value |

## [◆ ](#ga2dd3afe41b22e989fb46614f89550007)bt\_audio\_codec\_cfg\_get\_frame\_dur()

| int bt\_audio\_codec\_cfg\_get\_frame\_dur | ( | const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract frame duration from BT codec config.

Parameters
:   | codec\_cfg | The codec configuration to extract data from. |
    | --- | --- |

Return values
:   | A | [bt\_audio\_codec\_cfg\_frame\_dur](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74 "bt_audio_codec_cfg_frame_dur") value |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENODATA | if not found |
    | -EBADMSG | if found value has invalid size or value |

## [◆ ](#gad8525a57d35e3e34ea591f7e20e2512d)bt\_audio\_codec\_cfg\_get\_freq()

| int bt\_audio\_codec\_cfg\_get\_freq | ( | const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract the frequency from a codec configuration.

Parameters
:   | codec\_cfg | The codec configuration to extract data from. |
    | --- | --- |

Return values
:   | A | [bt\_audio\_codec\_cfg\_freq](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7 "bt_audio_codec_cfg_freq") value |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENODATA | if not found |
    | -EBADMSG | if found value has invalid size or value |

## [◆ ](#ga503be053422217502d6108b045791e02)bt\_audio\_codec\_cfg\_get\_octets\_per\_frame()

| int bt\_audio\_codec\_cfg\_get\_octets\_per\_frame | ( | const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract frame size in octets from BT codec config.

The overall SDU size will be octets\_per\_frame \* blocks\_per\_sdu.

The Bluetooth specifications are not clear about this value - it does not state that the codec shall use this SDU size only. A codec like LC3 supports variable bit-rate (per SDU) hence it might be allowed for an encoder to reduce the frame size below this value. Hence it is recommended to use the received SDU size and divide by blocks\_per\_sdu rather than relying on this octets\_per\_sdu value to be fixed.

Parameters
:   | codec\_cfg | The codec configuration to extract data from. |
    | --- | --- |

Return values
:   | Frame | length in octets |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENODATA | if not found |
    | -EBADMSG | if found value has invalid size or value |

## [◆ ](#ga707c679db0193197b56acabfb08f8d1f)bt\_audio\_codec\_cfg\_get\_val()

| int bt\_audio\_codec\_cfg\_get\_val | ( | const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974) | *type*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *data* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Lookup a specific codec configuration value.

Parameters
:   | [in] | codec\_cfg | The codec data to search in. |
    | --- | --- | --- |
    | [in] | type | The type id to look for |
    | [out] | data | Pointer to the data-pointer to update when item is found |

Return values
:   | Length | of found `data` (may be 0) |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENODATA | if not found |

## [◆ ](#ga0fd6e6baf1b4f22d60768aaed6f42e8e)bt\_audio\_codec\_cfg\_meta\_get\_audio\_active\_state()

| int bt\_audio\_codec\_cfg\_meta\_get\_audio\_active\_state | ( | const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract audio active state.

See [BT\_AUDIO\_METADATA\_TYPE\_AUDIO\_STATE](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354af220c40d351ec5e236cd41a5944da5fc "BT_AUDIO_METADATA_TYPE_AUDIO_STATE") for more information about this value.

Parameters
:   | codec\_cfg | The codec data to search in. |
    | --- | --- |

Return values
:   | The | preferred context type if positive or 0 |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENODATA | if not found |
    | -EBADMSG | if found value has invalid size |

## [◆ ](#ga66143aa7dcc726e06a12660b8f90fc5a)bt\_audio\_codec\_cfg\_meta\_get\_bcast\_audio\_immediate\_rend\_flag()

| int bt\_audio\_codec\_cfg\_meta\_get\_bcast\_audio\_immediate\_rend\_flag | ( | const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract broadcast audio immediate rendering flag.

See [BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_IMMEDIATE](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1 "BT_AUDIO_METADATA_TYPE_BROADCAST_IMMEDIATE") for more information about this value.

Parameters
:   | codec\_cfg | The codec data to search in. |
    | --- | --- |

Return values
:   | 0 | if the flag was found |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENODATA | if not the flag was not found |

## [◆ ](#gaa0f9b9f608c7af881d5a928a3ae397b2)bt\_audio\_codec\_cfg\_meta\_get\_ccid\_list()

| int bt\_audio\_codec\_cfg\_meta\_get\_ccid\_list | ( | const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *ccid\_list* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract CCID list.

See [BT\_AUDIO\_METADATA\_TYPE\_CCID\_LIST](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b "BT_AUDIO_METADATA_TYPE_CCID_LIST") for more information about this value.

Parameters
:   | [in] | codec\_cfg | The codec data to search in. |
    | --- | --- | --- |
    | [out] | ccid\_list | Pointer to the array containing 8-bit CCIDs. |

Return values
:   | The | length of the `ccid_list` (may be 0) |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENODATA | if not found |

## [◆ ](#ga1f76f82bff63b876eb761a0bf0377428)bt\_audio\_codec\_cfg\_meta\_get\_extended()

| int bt\_audio\_codec\_cfg\_meta\_get\_extended | ( | const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *extended\_meta* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract extended metadata.

See [BT\_AUDIO\_METADATA\_TYPE\_EXTENDED](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39 "BT_AUDIO_METADATA_TYPE_EXTENDED") for more information about this value.

Parameters
:   | [in] | codec\_cfg | The codec data to search in. |
    | --- | --- | --- |
    | [out] | extended\_meta | Pointer to the extended metadata. |

Return values
:   | The | length of the `ccid_list` (may be 0) |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENODATA | if not found |

## [◆ ](#ga55e3cbaeacf15fcb1f24a16eb28db99c)bt\_audio\_codec\_cfg\_meta\_get\_lang()

| int bt\_audio\_codec\_cfg\_meta\_get\_lang | ( | const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *lang* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract language.

See [BT\_AUDIO\_METADATA\_TYPE\_LANG](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354af38d342d907c3903121a03bb8394efb1 "BT_AUDIO_METADATA_TYPE_LANG") for more information about this value.

Parameters
:   | [in] | codec\_cfg | The codec data to search in. |
    | --- | --- | --- |
    | [out] | lang | Pointer to the language bytes (of length BT\_AUDIO\_LANG\_SIZE) |

Return values
:   | The | language if positive or 0 |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENODATA | if not found |
    | -EBADMSG | if found value has invalid size |

## [◆ ](#gaf0eecb02a05f0cc2b75ae9fb32c03913)bt\_audio\_codec\_cfg\_meta\_get\_parental\_rating()

| int bt\_audio\_codec\_cfg\_meta\_get\_parental\_rating | ( | const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract parental rating.

See [BT\_AUDIO\_METADATA\_TYPE\_PARENTAL\_RATING](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a7a83f397dc5dbe6e6d60a994cccdc613 "BT_AUDIO_METADATA_TYPE_PARENTAL_RATING") for more information about this value.

Parameters
:   | codec\_cfg | The codec data to search in. |
    | --- | --- |

Return values
:   | The | parental rating if positive or 0 |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENODATA | if not found |
    | -EBADMSG | if found value has invalid size |

## [◆ ](#gaea087663426a49bb6ff4859800aecb84)bt\_audio\_codec\_cfg\_meta\_get\_pref\_context()

| int bt\_audio\_codec\_cfg\_meta\_get\_pref\_context | ( | const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *fallback\_to\_default* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract preferred contexts.

See [BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a "BT_AUDIO_METADATA_TYPE_PREF_CONTEXT") for more information about this value.

Parameters
:   | codec\_cfg | The codec data to search in. |
    | --- | --- |
    | fallback\_to\_default | If true this function will provide the default value of [BT\_AUDIO\_CONTEXT\_TYPE\_UNSPECIFIED](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5 "BT_AUDIO_CONTEXT_TYPE_UNSPECIFIED") if the type is not found when `codec_cfg.id` is [BT\_HCI\_CODING\_FORMAT\_LC3](hci__types_8h.md#a1fa62d6f28ef56ebe9c18d5ab86fbf8e "BT_HCI_CODING_FORMAT_LC3"). |

Return values
:   | The | preferred context type if positive or 0 |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENODATA | if not found |
    | -EBADMSG | if found value has invalid size |

## [◆ ](#ga03284b8474d65443d7ecc8bdfc6f04c6)bt\_audio\_codec\_cfg\_meta\_get\_program\_info()

| int bt\_audio\_codec\_cfg\_meta\_get\_program\_info | ( | const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *program\_info* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract program info.

See [BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a02f91ea7fb6be631687d843ad7bf4ac7 "BT_AUDIO_METADATA_TYPE_PROGRAM_INFO") for more information about this value.

Parameters
:   | [in] | codec\_cfg | The codec data to search in. |
    | --- | --- | --- |
    | [out] | program\_info | Pointer to the UTF-8 formatted program info. |

Return values
:   | The | length of the `program_info` (may be 0) |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENODATA | if not found |

## [◆ ](#ga6bdbc0a0b929fdbdc75db479aec858df)bt\_audio\_codec\_cfg\_meta\_get\_program\_info\_uri()

| int bt\_audio\_codec\_cfg\_meta\_get\_program\_info\_uri | ( | const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *program\_info\_uri* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract program info URI.

See [BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO\_URI](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a58971ea21b5045e56a0e1ca838358922 "BT_AUDIO_METADATA_TYPE_PROGRAM_INFO_URI") for more information about this value.

Parameters
:   | [in] | codec\_cfg | The codec data to search in. |
    | --- | --- | --- |
    | [out] | program\_info\_uri | Pointer to the UTF-8 formatted program info URI. |

Return values
:   | The | length of the `ccid_list` (may be 0) |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENODATA | if not found |

## [◆ ](#ga4cc4e1bb941206e7f1541a57fc92b8e9)bt\_audio\_codec\_cfg\_meta\_get\_stream\_context()

| int bt\_audio\_codec\_cfg\_meta\_get\_stream\_context | ( | const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract stream contexts.

See [BT\_AUDIO\_METADATA\_TYPE\_STREAM\_CONTEXT](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa "BT_AUDIO_METADATA_TYPE_STREAM_CONTEXT") for more information about this value.

Parameters
:   | codec\_cfg | The codec data to search in. |
    | --- | --- |

Return values
:   | The | stream context type if positive or 0 |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENODATA | if not found |
    | -EBADMSG | if found value has invalid size |

## [◆ ](#gae98335e87394a491b4a311d867a5e32d)bt\_audio\_codec\_cfg\_meta\_get\_val()

| int bt\_audio\_codec\_cfg\_meta\_get\_val | ( | const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *type*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *data* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Lookup a specific metadata value based on type.

Parameters
:   | [in] | codec\_cfg | The codec data to search in. |
    | --- | --- | --- |
    | [in] | type | The type id to look for |
    | [out] | data | Pointer to the data-pointer to update when item is found |

Return values
:   | Length | of found `data` (may be 0) |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENODATA | if not found |

## [◆ ](#ga4a4982e3bd0e8c944b584196ef146f6c)bt\_audio\_codec\_cfg\_meta\_get\_vendor()

| int bt\_audio\_codec\_cfg\_meta\_get\_vendor | ( | const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *vendor\_meta* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract vendor specific metadata.

See [BT\_AUDIO\_METADATA\_TYPE\_VENDOR](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286 "BT_AUDIO_METADATA_TYPE_VENDOR") for more information about this value.

Parameters
:   | [in] | codec\_cfg | The codec data to search in. |
    | --- | --- | --- |
    | [out] | vendor\_meta | Pointer to the vendor specific metadata. |

Return values
:   | The | length of the `ccid_list` (may be 0) |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENODATA | if not found |

## [◆ ](#gaf869e7ce0c9dd467fb03e8503d36c58a)bt\_audio\_codec\_cfg\_meta\_set\_audio\_active\_state()

| int bt\_audio\_codec\_cfg\_meta\_set\_audio\_active\_state | ( | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_active\_state](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f) | *state* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the audio active state of a codec configuration metadata.

Parameters
:   | codec\_cfg | The codec configuration to set data for. |
    | --- | --- |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | The audio active state to set. |

Return values
:   | The | data\_len of `codec_cfg` on success |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENOMEM | if the new value could not set or added due to memory |

## [◆ ](#gaede61b65d2037c7fbf6c4c4e090990be)bt\_audio\_codec\_cfg\_meta\_set\_bcast\_audio\_immediate\_rend\_flag()

| int bt\_audio\_codec\_cfg\_meta\_set\_bcast\_audio\_immediate\_rend\_flag | ( | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the broadcast audio immediate rendering flag of a codec configuration metadata.

Parameters
:   | codec\_cfg | The codec configuration to set data for. |
    | --- | --- |

Return values
:   | The | data\_len of `codec_cfg` on success |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENOMEM | if the new value could not set or added due to memory |

## [◆ ](#ga59716b95fcea3404ff8c078564b0e29c)bt\_audio\_codec\_cfg\_meta\_set\_ccid\_list()

| int bt\_audio\_codec\_cfg\_meta\_set\_ccid\_list | ( | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *ccid\_list*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *ccid\_list\_len* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the CCID list of a codec configuration metadata.

Parameters
:   | codec\_cfg | The codec configuration to set data for. |
    | --- | --- |
    | ccid\_list | The program info to set. |
    | ccid\_list\_len | The length of `ccid_list`. |

Return values
:   | The | data\_len of `codec_cfg` on success |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENOMEM | if the new value could not set or added due to memory |

## [◆ ](#gade9cb53287ab3356fb57ba8a454a3aad)bt\_audio\_codec\_cfg\_meta\_set\_extended()

| int bt\_audio\_codec\_cfg\_meta\_set\_extended | ( | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *extended\_meta*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *extended\_meta\_len* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the extended metadata of a codec configuration metadata.

Parameters
:   | codec\_cfg | The codec configuration to set data for. |
    | --- | --- |
    | extended\_meta | The extended metadata to set. |
    | extended\_meta\_len | The length of `extended_meta`. |

Return values
:   | The | data\_len of `codec_cfg` on success |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENOMEM | if the new value could not set or added due to memory |

## [◆ ](#ga54b7eadf072c397879c1dababa2a3be0)bt\_audio\_codec\_cfg\_meta\_set\_lang()

| int bt\_audio\_codec\_cfg\_meta\_set\_lang | ( | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *lang*[3] ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the language of a codec configuration metadata.

Parameters
:   | codec\_cfg | The codec configuration to set data for. |
    | --- | --- |
    | lang | The 24-bit language to set. |

Return values
:   | The | data\_len of `codec_cfg` on success |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENOMEM | if the new value could not set or added due to memory |

## [◆ ](#gab5d8b5877de4fe16c0e06a1d4f0d15ce)bt\_audio\_codec\_cfg\_meta\_set\_parental\_rating()

| int bt\_audio\_codec\_cfg\_meta\_set\_parental\_rating | ( | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760) | *parental\_rating* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the parental rating of a codec configuration metadata.

Parameters
:   | codec\_cfg | The codec configuration to set data for. |
    | --- | --- |
    | parental\_rating | The parental rating to set. |

Return values
:   | The | data\_len of `codec_cfg` on success |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENOMEM | if the new value could not set or added due to memory |

## [◆ ](#gab40bad609f17d24e7e0e9ffcebe4e912)bt\_audio\_codec\_cfg\_meta\_set\_pref\_context()

| int bt\_audio\_codec\_cfg\_meta\_set\_pref\_context | ( | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) | *ctx* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the preferred context of a codec configuration metadata.

Parameters
:   | codec\_cfg | The codec configuration to set data for. |
    | --- | --- |
    | ctx | The preferred context to set. |

Return values
:   | The | data\_len of `codec_cfg` on success |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENOMEM | if the new value could not set or added due to memory |

## [◆ ](#ga2ca9e616d20d7513c60ce905f046ac7b)bt\_audio\_codec\_cfg\_meta\_set\_program\_info()

| int bt\_audio\_codec\_cfg\_meta\_set\_program\_info | ( | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *program\_info*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *program\_info\_len* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the program info of a codec configuration metadata.

Parameters
:   | codec\_cfg | The codec configuration to set data for. |
    | --- | --- |
    | program\_info | The program info to set. |
    | program\_info\_len | The length of `program_info`. |

Return values
:   | The | data\_len of `codec_cfg` on success |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENOMEM | if the new value could not set or added due to memory |

## [◆ ](#ga99163729034e816eaef7195505d5ae20)bt\_audio\_codec\_cfg\_meta\_set\_program\_info\_uri()

| int bt\_audio\_codec\_cfg\_meta\_set\_program\_info\_uri | ( | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *program\_info\_uri*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *program\_info\_uri\_len* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the program info URI of a codec configuration metadata.

Parameters
:   | codec\_cfg | The codec configuration to set data for. |
    | --- | --- |
    | program\_info\_uri | The program info URI to set. |
    | program\_info\_uri\_len | The length of `program_info_uri`. |

Return values
:   | The | data\_len of `codec_cfg` on success |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENOMEM | if the new value could not set or added due to memory |

## [◆ ](#ga5cd2af1bb44c6eb5bafe824f005a77f0)bt\_audio\_codec\_cfg\_meta\_set\_stream\_context()

| int bt\_audio\_codec\_cfg\_meta\_set\_stream\_context | ( | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) | *ctx* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the stream context of a codec configuration metadata.

Parameters
:   | codec\_cfg | The codec configuration to set data for. |
    | --- | --- |
    | ctx | The stream context to set. |

Return values
:   | The | data\_len of `codec_cfg` on success |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENOMEM | if the new value could not set or added due to memory |

## [◆ ](#ga3e24c2ba8de502600e647cb2f84e3ec4)bt\_audio\_codec\_cfg\_meta\_set\_val()

| int bt\_audio\_codec\_cfg\_meta\_set\_val | ( | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) | *type*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_len* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set or add a specific codec configuration metadata value.

Parameters
:   | codec\_cfg | The codec configuration to set the value in. |
    | --- | --- |
    | type | The type id to set. |
    | data | Pointer to the data-pointer to set. |
    | data\_len | Length of `data`. |

Return values
:   | The | meta\_len of `codec_cfg` on success |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENOMEM | if the new value could not set or added due to memory |

## [◆ ](#ga6935d1c40b3178b0c8fa877ee93d1e53)bt\_audio\_codec\_cfg\_meta\_set\_vendor()

| int bt\_audio\_codec\_cfg\_meta\_set\_vendor | ( | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *vendor\_meta*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *vendor\_meta\_len* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the vendor specific metadata of a codec configuration metadata.

Parameters
:   | codec\_cfg | The codec configuration to set data for. |
    | --- | --- |
    | vendor\_meta | The vendor specific metadata to set. |
    | vendor\_meta\_len | The length of `vendor_meta`. |

Return values
:   | The | data\_len of `codec_cfg` on success |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENOMEM | if the new value could not set or added due to memory |

## [◆ ](#gab46f830daa1d9a907f47eb2a9eed7337)bt\_audio\_codec\_cfg\_meta\_unset\_val()

| int bt\_audio\_codec\_cfg\_meta\_unset\_val | ( | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) | *type* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Unset a specific codec configuration metadata value.

The type and the value will be removed from the codec configuration metadata.

Parameters
:   | codec\_cfg | The codec data to set the value in. |
    | --- | --- |
    | type | The type id to unset. |

Return values
:   | The | meta\_len of `codec_cfg` on success |
    | --- | --- |
    | -EINVAL | if arguments are invalid |

## [◆ ](#gafbbcd69fac18ed0201a5e0156209b049)bt\_audio\_codec\_cfg\_set\_chan\_allocation()

| int bt\_audio\_codec\_cfg\_set\_chan\_allocation | ( | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) | *chan\_allocation* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the channel allocation of a codec configuration.

Parameters
:   | codec\_cfg | The codec configuration to set data for. |
    | --- | --- |
    | chan\_allocation | The channel allocation to set. |

Return values
:   | The | data\_len of `codec_cfg` on success |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENOMEM | if the new value could not set or added due to memory |

## [◆ ](#gac9cf20bafbe24b34034bfb6ee7aaf03e)bt\_audio\_codec\_cfg\_set\_frame\_blocks\_per\_sdu()

| int bt\_audio\_codec\_cfg\_set\_frame\_blocks\_per\_sdu | ( | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *frame\_blocks* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the frame blocks per SDU of a codec configuration.

Parameters
:   | codec\_cfg | The codec configuration to set data for. |
    | --- | --- |
    | frame\_blocks | The frame blocks per SDU to set. |

Return values
:   | The | data\_len of `codec_cfg` on success |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENOMEM | if the new value could not set or added due to memory |

## [◆ ](#ga7d8306f98cb00f06e68a1df417825f0d)bt\_audio\_codec\_cfg\_set\_frame\_dur()

| int bt\_audio\_codec\_cfg\_set\_frame\_dur | ( | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_codec\_cfg\_frame\_dur](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74) | *frame\_dur* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the frame duration of a codec configuration.

Parameters
:   | codec\_cfg | The codec configuration to set data for. |
    | --- | --- |
    | frame\_dur | The assigned numbers frame duration to set. |

Return values
:   | The | data\_len of `codec_cfg` on success |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENOMEM | if the new value could not set or added due to memory |

## [◆ ](#gac119989d5dcfa36becf4edd0ae7c6138)bt\_audio\_codec\_cfg\_set\_freq()

| int bt\_audio\_codec\_cfg\_set\_freq | ( | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_codec\_cfg\_freq](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7) | *freq* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the frequency of a codec configuration.

Parameters
:   | codec\_cfg | The codec configuration to set data for. |
    | --- | --- |
    | freq | The assigned numbers frequency to set. |

Return values
:   | The | data\_len of `codec_cfg` on success |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENOMEM | if the new value could not set or added due to memory |

## [◆ ](#ga866cdec28194056dc9e274d0436b45c2)bt\_audio\_codec\_cfg\_set\_octets\_per\_frame()

| int bt\_audio\_codec\_cfg\_set\_octets\_per\_frame | ( | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *octets\_per\_frame* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the octets per codec frame of a codec configuration.

Parameters
:   | codec\_cfg | The codec configuration to set data for. |
    | --- | --- |
    | octets\_per\_frame | The octets per codec frame to set. |

Return values
:   | The | data\_len of `codec_cfg` on success |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENOMEM | if the new value could not set or added due to memory |

## [◆ ](#gab10f22938780530b1d1b95695382902e)bt\_audio\_codec\_cfg\_set\_val()

| int bt\_audio\_codec\_cfg\_set\_val | ( | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974) | *type*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_len* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set or add a specific codec configuration value.

Parameters
:   | codec\_cfg | The codec data to set the value in. |
    | --- | --- |
    | type | The type id to set |
    | data | Pointer to the data-pointer to set |
    | data\_len | Length of `data` |

Return values
:   | The | data\_len of `codec_cfg` on success |
    | --- | --- |
    | -EINVAL | if arguments are invalid |
    | -ENOMEM | if the new value could not set or added due to memory |

## [◆ ](#gad3857d0ca008854df5966501caa261ba)bt\_audio\_codec\_cfg\_unset\_val()

| int bt\_audio\_codec\_cfg\_unset\_val | ( | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974) | *type* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Unset a specific codec configuration value.

The type and the value will be removed from the codec configuration.

Parameters
:   | codec\_cfg | The codec data to set the value in. |
    | --- | --- |
    | type | The type id to unset. |

Return values
:   | The | data\_len of `codec_cfg` on success |
    | --- | --- |
    | -EINVAL | if arguments are invalid |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
