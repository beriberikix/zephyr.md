---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__audio__codec__cap.html
original_path: doxygen/html/group__bt__audio__codec__cap.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Codec capability parsing APIs

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Audio](group__bt__audio.md)

Audio codec capabilities APIs.
[More...](#details)

| Functions | |
| --- | --- |
| int | [bt\_audio\_codec\_cap\_get\_val](#gac3bf5dd414271bb1dcbc6590994cff6b) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data) |
|  | Lookup a specific value based on type. |
| int | [bt\_audio\_codec\_cap\_set\_val](#ga0c2c816b0b2b85aa5dd38f21caceea40) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_len) |
|  | Set or add a specific codec capability value. |
| int | [bt\_audio\_codec\_cap\_unset\_val](#gabc9962212ad65339ff02ba1389d5f9f8) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015) type) |
|  | Unset a specific codec capability value. |
| int | [bt\_audio\_codec\_cap\_get\_freq](#gaa1dbf81c437c983af0144bf62433666c) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap) |
|  | Extract the frequency from a codec capability. |
| int | [bt\_audio\_codec\_cap\_set\_freq](#gac0655c0bd6552ab8a265076d7d0cd1b2) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_codec\_cap\_freq](group__bt__audio.md#gaafc1106d5d305874ee2f540c850ff5b4) freq) |
|  | Set the supported frequencies of a codec capability. |
| int | [bt\_audio\_codec\_cap\_get\_frame\_dur](#ga12336de7d908bda94427caee4dc080e0) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap) |
|  | Extract the frequency from a codec capability. |
| int | [bt\_audio\_codec\_cap\_set\_frame\_dur](#ga53e5df6cc4cfbed12b59a6a506657772) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_codec\_cap\_frame\_dur](group__bt__audio.md#gaf37e8e19f956afb3c3a413cbaa1a21f5) frame\_dur) |
|  | Set the frame duration of a codec capability. |
| int | [bt\_audio\_codec\_cap\_get\_supported\_audio\_chan\_counts](#ga63d5e083f03ec06939ee1cd0355c8c2a) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) fallback\_to\_default) |
|  | Extract the frequency from a codec capability. |
| int | [bt\_audio\_codec\_cap\_set\_supported\_audio\_chan\_counts](#gaf6b2717823f9f3136237ed6a6515449e) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_codec\_cap\_chan\_count](group__bt__audio.md#gae695b5d17359967703f2509db1671fa5) chan\_count) |
|  | Set the channel count of a codec capability. |
| int | [bt\_audio\_codec\_cap\_get\_octets\_per\_frame](#gaa949089f2c6c143041e6cb61338e0ddc) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, struct [bt\_audio\_codec\_octets\_per\_codec\_frame](structbt__audio__codec__octets__per__codec__frame.md) \*codec\_frame) |
|  | Extract the supported octets per codec frame from a codec capability. |
| int | [bt\_audio\_codec\_cap\_set\_octets\_per\_frame](#gac1c42460cd3c55bbfbd467f84ab2d78d) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const struct [bt\_audio\_codec\_octets\_per\_codec\_frame](structbt__audio__codec__octets__per__codec__frame.md) \*codec\_frame) |
|  | Set the octets per codec frame of a codec capability. |
| int | [bt\_audio\_codec\_cap\_get\_max\_codec\_frames\_per\_sdu](#ga194d938896ee65601bdce96d68c84885) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) fallback\_to\_default) |
|  | Extract the maximum codec frames per SDU from a codec capability. |
| int | [bt\_audio\_codec\_cap\_set\_max\_codec\_frames\_per\_sdu](#ga3785bc41f56f8f2a09248396dadb31da) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) codec\_frames\_per\_sdu) |
|  | Set the maximum codec frames per SDU of a codec capability. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_val](#ga5c2ecbb4d0cef26dd2cc5d023e70a163) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data) |
|  | Lookup a specific metadata value based on type. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_val](#ga1fdfd8c36f4131bcf4ffd2b7f176b631) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_len) |
|  | Set or add a specific codec capability metadata value. |
| int | [bt\_audio\_codec\_cap\_meta\_unset\_val](#ga40848f5375d1e58622c580112c282f2e) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) type) |
|  | Unset a specific codec capability metadata value. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_pref\_context](#gaaa8c6783241b1b70349354b3e36c696c) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap) |
|  | Extract preferred contexts. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_pref\_context](#ga7fe0d4553d6accf5c89645cbf86149bf) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) ctx) |
|  | Set the preferred context of a codec capability metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_stream\_context](#ga88ee657b5bd3f847bb75c9620ddb142f) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap) |
|  | Extract stream contexts. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_stream\_context](#ga5cc7f360049c38c8de631ea33dbc44ab) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) ctx) |
|  | Set the stream context of a codec capability metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_program\_info](#ga33725c3b2c06d6c22030bb5a77d702b0) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*program\_info) |
|  | Extract program info. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_program\_info](#ga43d2ec3a4d621c26843de82db7fd2189) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*program\_info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) program\_info\_len) |
|  | Set the program info of a codec capability metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_lang](#gafb631b55b69b256c60b9cf3c7f418ff8) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*lang) |
|  | Extract language. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_lang](#ga8182b2bed20449b8581b89677893c130) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) lang[3]) |
|  | Set the language of a codec capability metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_ccid\_list](#ga3095dea36e60e75cbfe786d3c2f11866) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*ccid\_list) |
|  | Extract CCID list. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_ccid\_list](#ga00a8ad22713dab761c81d1b8481c037d) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ccid\_list, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ccid\_list\_len) |
|  | Set the CCID list of a codec capability metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_parental\_rating](#gab34d0369ce08efcd407d33956d32632e) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap) |
|  | Extract parental rating. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_parental\_rating](#ga5e267dfad978cd3d52be9c31a4fac0be) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760) parental\_rating) |
|  | Set the parental rating of a codec capability metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_program\_info\_uri](#gadb39b0ee1f65cdd2457fdf2c3142c040) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*program\_info\_uri) |
|  | Extract program info URI. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_program\_info\_uri](#gafbb0d6282d989e8bc70caada2845b337) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*program\_info\_uri, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) program\_info\_uri\_len) |
|  | Set the program info URI of a codec capability metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_audio\_active\_state](#ga88bb1da63b7ea0f95dd236aa1024cfb8) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap) |
|  | Extract audio active state. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_audio\_active\_state](#gacd3de0306a22d1a1d9ba09b4ac4f4e09) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_active\_state](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Set the audio active state of a codec capability metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_bcast\_audio\_immediate\_rend\_flag](#gab4ccc7cb7d779acb20185ae808dd8bbe) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap) |
|  | Extract broadcast audio immediate rendering flag. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_bcast\_audio\_immediate\_rend\_flag](#gaa1d382b4fa53f7cbe8426df53a3317ce) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap) |
|  | Set the broadcast audio immediate rendering flag of a codec capability metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_assisted\_listening\_stream](#ga4f1ea56f2c1c21420f078d35081ceee5) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap) |
|  | Extract assisted listening stream. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_assisted\_listening\_stream](#ga3346db1f59cb35b9b9e5255424adb6e4) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_assisted\_listening\_stream](group__bt__audio.md#ga207fbf0fbca9b24cba02c7f1d184e7f5) val) |
|  | Set the assisted listening stream value of a codec capability metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_broadcast\_name](#ga3c8df3fe79f0bb96c4e15e7c2502bf89) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*broadcast\_name) |
|  | Extract broadcast name. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_broadcast\_name](#ga461add2808a1eca8993222d2b31d5a5f) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*broadcast\_name, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) broadcast\_name\_len) |
|  | Set the broadcast name of a codec capability metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_extended](#ga69aecd7e98f90a5162ff8ea3373b43d4) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*extended\_meta) |
|  | Extract extended metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_extended](#gac00aabc7329027852a7caf5cdff2bc26) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*extended\_meta, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) extended\_meta\_len) |
|  | Set the extended metadata of a codec capability metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_vendor](#gab8c80a0f55041f026d453fd88cdeb727) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*vendor\_meta) |
|  | Extract vendor specific metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_vendor](#ga1f06789782541beab9aab4914f91bb57) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*vendor\_meta, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) vendor\_meta\_len) |
|  | Set the vendor specific metadata of a codec capability metadata. |

## Detailed Description

Audio codec capabilities APIs.

Functions to parse codec capability data when formatted as LTV wrapped into [Codec capability parsing APIs](group__bt__audio__codec__cap.md "Codec capability parsing APIs").

## Function Documentation

## [◆ ](#ga12336de7d908bda94427caee4dc080e0)bt\_audio\_codec\_cap\_get\_frame\_dur()

| int bt\_audio\_codec\_cap\_get\_frame\_dur | ( | const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract the frequency from a codec capability.

Parameters
:   | codec\_cap | The codec capabilities to extract data from. |
    | --- | --- |

Return values
:   | durations | Bitfield of supported frame durations if 0 or positive |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENODATA | Data not found |
    | -EBADMSG | The found value has invalid size or value |

## [◆ ](#gaa1dbf81c437c983af0144bf62433666c)bt\_audio\_codec\_cap\_get\_freq()

| int bt\_audio\_codec\_cap\_get\_freq | ( | const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract the frequency from a codec capability.

Parameters
:   | codec\_cap | The codec capabilities to extract data from. |
    | --- | --- |

Return values
:   | frequencies | Bitfield of supported frequencies ([bt\_audio\_codec\_cap\_freq](group__bt__audio.md#gaafc1106d5d305874ee2f540c850ff5b4 "bt_audio_codec_cap_freq")) if 0 or positive |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENODATA | Data not found |
    | -EBADMSG | The found value has invalid size or value |

## [◆ ](#ga194d938896ee65601bdce96d68c84885)bt\_audio\_codec\_cap\_get\_max\_codec\_frames\_per\_sdu()

| int bt\_audio\_codec\_cap\_get\_max\_codec\_frames\_per\_sdu | ( | const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *fallback\_to\_default* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract the maximum codec frames per SDU from a codec capability.

Parameters
:   | codec\_cap | The codec capabilities to extract data from. |
    | --- | --- |
    | fallback\_to\_default | If true this function will provide the default value of 1 if the type is not found when `codec_cap.id` is [BT\_HCI\_CODING\_FORMAT\_LC3](hci__types_8h.md#a1fa62d6f28ef56ebe9c18d5ab86fbf8e "BT_HCI_CODING_FORMAT_LC3"). |

Return values
:   | codec\_frames\_per\_sdu | Maximum number of codec frames per SDU supported |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENODATA | Data not found |
    | -EBADMSG | The found value has invalid size or value |

## [◆ ](#gaa949089f2c6c143041e6cb61338e0ddc)bt\_audio\_codec\_cap\_get\_octets\_per\_frame()

| int bt\_audio\_codec\_cap\_get\_octets\_per\_frame | ( | const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_audio\_codec\_octets\_per\_codec\_frame](structbt__audio__codec__octets__per__codec__frame.md) \* | *codec\_frame* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract the supported octets per codec frame from a codec capability.

Parameters
:   | [in] | codec\_cap | The codec capabilities to extract data from. |
    | --- | --- | --- |
    | [out] | codec\_frame | Struct to place the resulting values in |

Return values
:   | 0 | Success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENODATA | Data not found |
    | -EBADMSG | The found value has invalid size or value |

## [◆ ](#ga63d5e083f03ec06939ee1cd0355c8c2a)bt\_audio\_codec\_cap\_get\_supported\_audio\_chan\_counts()

| int bt\_audio\_codec\_cap\_get\_supported\_audio\_chan\_counts | ( | const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *fallback\_to\_default* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract the frequency from a codec capability.

Parameters
:   | codec\_cap | The codec capabilities to extract data from. |
    | --- | --- |
    | fallback\_to\_default | If true this function will provide the default value of 1 if the type is not found when `codec_cap.id` is [BT\_HCI\_CODING\_FORMAT\_LC3](hci__types_8h.md#a1fa62d6f28ef56ebe9c18d5ab86fbf8e "BT_HCI_CODING_FORMAT_LC3"). |

Return values
:   | channel\_counts | Number of supported channel counts if 0 or positive |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENODATA | Data not found |
    | -EBADMSG | The found value has invalid size or value |

## [◆ ](#gac3bf5dd414271bb1dcbc6590994cff6b)bt\_audio\_codec\_cap\_get\_val()

| int bt\_audio\_codec\_cap\_get\_val | ( | const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015) | *type*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *data* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Lookup a specific value based on type.

Parameters
:   | [in] | codec\_cap | The codec data to search in. |
    | --- | --- | --- |
    | [in] | type | The type id to look for |
    | [out] | data | Pointer to the data-pointer to update when item is found |

Return values
:   | len | Length of found `data` (may be 0) |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENODATA | Data not found |

## [◆ ](#ga4f1ea56f2c1c21420f078d35081ceee5)bt\_audio\_codec\_cap\_meta\_get\_assisted\_listening\_stream()

| int bt\_audio\_codec\_cap\_meta\_get\_assisted\_listening\_stream | ( | const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract assisted listening stream.

See [BT\_AUDIO\_METADATA\_TYPE\_ASSISTED\_LISTENING\_STREAM](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a40aad5cb3574e6e4e7bc955bc12760bf "BT_AUDIO_METADATA_TYPE_ASSISTED_LISTENING_STREAM") for more information about this value.

Parameters
:   | codec\_cap | The codec data to search in. |
    | --- | --- |

Return values
:   | value | The assisted listening stream value if positive or 0 |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENODATA | Data not found |
    | -EBADMSG | The found value has invalid size |

## [◆ ](#ga88bb1da63b7ea0f95dd236aa1024cfb8)bt\_audio\_codec\_cap\_meta\_get\_audio\_active\_state()

| int bt\_audio\_codec\_cap\_meta\_get\_audio\_active\_state | ( | const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract audio active state.

See [BT\_AUDIO\_METADATA\_TYPE\_AUDIO\_STATE](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354af220c40d351ec5e236cd41a5944da5fc "BT_AUDIO_METADATA_TYPE_AUDIO_STATE") for more information about this value.

Parameters
:   | codec\_cap | The codec data to search in. |
    | --- | --- |

Return values
:   | context | The preferred context type if positive or 0 |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENODATA | Data not found |
    | -EBADMSG | The found value has invalid size |

## [◆ ](#gab4ccc7cb7d779acb20185ae808dd8bbe)bt\_audio\_codec\_cap\_meta\_get\_bcast\_audio\_immediate\_rend\_flag()

| int bt\_audio\_codec\_cap\_meta\_get\_bcast\_audio\_immediate\_rend\_flag | ( | const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract broadcast audio immediate rendering flag.

See [BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_IMMEDIATE](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1 "BT_AUDIO_METADATA_TYPE_BROADCAST_IMMEDIATE") for more information about this value.

Parameters
:   | codec\_cap | The codec data to search in. |
    | --- | --- |

Return values
:   | 0 | The flag was found |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENODATA | The flag was not found |

## [◆ ](#ga3c8df3fe79f0bb96c4e15e7c2502bf89)bt\_audio\_codec\_cap\_meta\_get\_broadcast\_name()

| int bt\_audio\_codec\_cap\_meta\_get\_broadcast\_name | ( | const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *broadcast\_name* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract broadcast name.

See [BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_NAME](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354ada34d453c8ce75a155c59c371a67d8a6 "BT_AUDIO_METADATA_TYPE_BROADCAST_NAME") for more information about this value.

Parameters
:   | [in] | codec\_cap | The codec data to search in. |
    | --- | --- | --- |
    | [out] | broadcast\_name | Pointer to the UTF-8 formatted broadcast name. |

Return values
:   | length | The length of the `broadcast_name` (may be 0) |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENODATA | Data not found |

## [◆ ](#ga3095dea36e60e75cbfe786d3c2f11866)bt\_audio\_codec\_cap\_meta\_get\_ccid\_list()

| int bt\_audio\_codec\_cap\_meta\_get\_ccid\_list | ( | const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *ccid\_list* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract CCID list.

See [BT\_AUDIO\_METADATA\_TYPE\_CCID\_LIST](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b "BT_AUDIO_METADATA_TYPE_CCID_LIST") for more information about this value.

Parameters
:   | [in] | codec\_cap | The codec data to search in. |
    | --- | --- | --- |
    | [out] | ccid\_list | Pointer to the array containing 8-bit CCIDs. |

Return values
:   | len | The length of the `ccid_list` (may be 0) |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENODATA | Data not found |

## [◆ ](#ga69aecd7e98f90a5162ff8ea3373b43d4)bt\_audio\_codec\_cap\_meta\_get\_extended()

| int bt\_audio\_codec\_cap\_meta\_get\_extended | ( | const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *extended\_meta* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract extended metadata.

See [BT\_AUDIO\_METADATA\_TYPE\_EXTENDED](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39 "BT_AUDIO_METADATA_TYPE_EXTENDED") for more information about this value.

Parameters
:   | [in] | codec\_cap | The codec data to search in. |
    | --- | --- | --- |
    | [out] | extended\_meta | Pointer to the extended metadata. |

Return values
:   | len | The length of the `extended_meta` (may be 0) |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENODATA | Data not found |

## [◆ ](#gafb631b55b69b256c60b9cf3c7f418ff8)bt\_audio\_codec\_cap\_meta\_get\_lang()

| int bt\_audio\_codec\_cap\_meta\_get\_lang | ( | const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *lang* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract language.

See [BT\_AUDIO\_METADATA\_TYPE\_LANG](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354af38d342d907c3903121a03bb8394efb1 "BT_AUDIO_METADATA_TYPE_LANG") for more information about this value.

Parameters
:   | [in] | codec\_cap | The codec data to search in. |
    | --- | --- | --- |
    | [out] | lang | Pointer to the language bytes (of length BT\_AUDIO\_LANG\_SIZE) |

Return values
:   | 0 | Success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENODATA | Data not found |
    | -EBADMSG | The found value has invalid size |

## [◆ ](#gab34d0369ce08efcd407d33956d32632e)bt\_audio\_codec\_cap\_meta\_get\_parental\_rating()

| int bt\_audio\_codec\_cap\_meta\_get\_parental\_rating | ( | const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract parental rating.

See [BT\_AUDIO\_METADATA\_TYPE\_PARENTAL\_RATING](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a7a83f397dc5dbe6e6d60a994cccdc613 "BT_AUDIO_METADATA_TYPE_PARENTAL_RATING") for more information about this value.

Parameters
:   | codec\_cap | The codec data to search in. |
    | --- | --- |

Return values
:   | The | parental rating if positive or 0 |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENODATA | Data not found |
    | -EBADMSG | The found value has invalid size |

## [◆ ](#gaaa8c6783241b1b70349354b3e36c696c)bt\_audio\_codec\_cap\_meta\_get\_pref\_context()

| int bt\_audio\_codec\_cap\_meta\_get\_pref\_context | ( | const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract preferred contexts.

See [BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a "BT_AUDIO_METADATA_TYPE_PREF_CONTEXT") for more information about this value.

Parameters
:   | codec\_cap | The codec data to search in. |
    | --- | --- |

Return values
:   | The | preferred context type if positive or 0 |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENODATA | Data not found |
    | -EBADMSG | The found value has invalid size |

## [◆ ](#ga33725c3b2c06d6c22030bb5a77d702b0)bt\_audio\_codec\_cap\_meta\_get\_program\_info()

| int bt\_audio\_codec\_cap\_meta\_get\_program\_info | ( | const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *program\_info* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract program info.

See [BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a02f91ea7fb6be631687d843ad7bf4ac7 "BT_AUDIO_METADATA_TYPE_PROGRAM_INFO") for more information about this value.

Parameters
:   | [in] | codec\_cap | The codec data to search in. |
    | --- | --- | --- |
    | [out] | program\_info | Pointer to the UTF-8 formatted program info. |

Return values
:   | len | The length of the `program_info` (may be 0) |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENODATA | Data not found |

## [◆ ](#gadb39b0ee1f65cdd2457fdf2c3142c040)bt\_audio\_codec\_cap\_meta\_get\_program\_info\_uri()

| int bt\_audio\_codec\_cap\_meta\_get\_program\_info\_uri | ( | const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *program\_info\_uri* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract program info URI.

See [BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO\_URI](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a58971ea21b5045e56a0e1ca838358922 "BT_AUDIO_METADATA_TYPE_PROGRAM_INFO_URI") for more information about this value.

Parameters
:   | [in] | codec\_cap | The codec data to search in. |
    | --- | --- | --- |
    | [out] | program\_info\_uri | Pointer to the UTF-8 formatted program info URI. |

Return values
:   | len | The length of the `program_info_uri` (may be 0) |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENODATA | Data not found |

## [◆ ](#ga88ee657b5bd3f847bb75c9620ddb142f)bt\_audio\_codec\_cap\_meta\_get\_stream\_context()

| int bt\_audio\_codec\_cap\_meta\_get\_stream\_context | ( | const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract stream contexts.

See [BT\_AUDIO\_METADATA\_TYPE\_STREAM\_CONTEXT](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa "BT_AUDIO_METADATA_TYPE_STREAM_CONTEXT") for more information about this value.

Parameters
:   | codec\_cap | The codec data to search in. |
    | --- | --- |

Return values
:   | context | The stream context type if positive or 0 |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENODATA | Data not found |
    | -EBADMSG | The found value has invalid size |

## [◆ ](#ga5c2ecbb4d0cef26dd2cc5d023e70a163)bt\_audio\_codec\_cap\_meta\_get\_val()

| int bt\_audio\_codec\_cap\_meta\_get\_val | ( | const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *type*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *data* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Lookup a specific metadata value based on type.

Parameters
:   | [in] | codec\_cap | The codec data to search in. |
    | --- | --- | --- |
    | [in] | type | The type id to look for |
    | [out] | data | Pointer to the data-pointer to update when item is found |

Return values
:   | len | Length of found `data` (may be 0) |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENODATA | Data not found |

## [◆ ](#gab8c80a0f55041f026d453fd88cdeb727)bt\_audio\_codec\_cap\_meta\_get\_vendor()

| int bt\_audio\_codec\_cap\_meta\_get\_vendor | ( | const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *vendor\_meta* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Extract vendor specific metadata.

See [BT\_AUDIO\_METADATA\_TYPE\_VENDOR](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286 "BT_AUDIO_METADATA_TYPE_VENDOR") for more information about this value.

Parameters
:   | [in] | codec\_cap | The codec data to search in. |
    | --- | --- | --- |
    | [out] | vendor\_meta | Pointer to the vendor specific metadata. |

Return values
:   | len | The length of the `vendor_meta` (may be 0) |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENODATA | Data not found |

## [◆ ](#ga3346db1f59cb35b9b9e5255424adb6e4)bt\_audio\_codec\_cap\_meta\_set\_assisted\_listening\_stream()

| int bt\_audio\_codec\_cap\_meta\_set\_assisted\_listening\_stream | ( | struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_assisted\_listening\_stream](group__bt__audio.md#ga207fbf0fbca9b24cba02c7f1d184e7f5) | *val* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the assisted listening stream value of a codec capability metadata.

Parameters
:   | codec\_cap | The codec capability to set data for. |
    | --- | --- |
    | val | The assisted listening stream value to set. |

Return values
:   | data\_len | The `codec_cap.data_len` on success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENOMEM | The new value could not be set or added due to lack of memory |

## [◆ ](#gacd3de0306a22d1a1d9ba09b4ac4f4e09)bt\_audio\_codec\_cap\_meta\_set\_audio\_active\_state()

| int bt\_audio\_codec\_cap\_meta\_set\_audio\_active\_state | ( | struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_active\_state](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f) | *state* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the audio active state of a codec capability metadata.

Parameters
:   | codec\_cap | The codec capability to set data for. |
    | --- | --- |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | The audio active state to set. |

Return values
:   | data\_len | The `codec_cap.data_len` on success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENOMEM | The new value could not be set or added due to lack of memory |

## [◆ ](#gaa1d382b4fa53f7cbe8426df53a3317ce)bt\_audio\_codec\_cap\_meta\_set\_bcast\_audio\_immediate\_rend\_flag()

| int bt\_audio\_codec\_cap\_meta\_set\_bcast\_audio\_immediate\_rend\_flag | ( | struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the broadcast audio immediate rendering flag of a codec capability metadata.

Parameters
:   | codec\_cap | The codec capability to set data for. |
    | --- | --- |

Return values
:   | data\_len | The `codec_cap.data_len` on success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENOMEM | The new value could not be set or added due to lack of memory |

## [◆ ](#ga461add2808a1eca8993222d2b31d5a5f)bt\_audio\_codec\_cap\_meta\_set\_broadcast\_name()

| int bt\_audio\_codec\_cap\_meta\_set\_broadcast\_name | ( | struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *broadcast\_name*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *broadcast\_name\_len* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the broadcast name of a codec capability metadata.

Parameters
:   | codec\_cap | The codec capability to set data for. |
    | --- | --- |
    | broadcast\_name | The broadcast name to set. |
    | broadcast\_name\_len | The length of `broadcast_name`. |

Return values
:   | data\_len | The `codec_cap.data_len` on success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENOMEM | The new value could not be set or added due to lack of memory |

## [◆ ](#ga00a8ad22713dab761c81d1b8481c037d)bt\_audio\_codec\_cap\_meta\_set\_ccid\_list()

| int bt\_audio\_codec\_cap\_meta\_set\_ccid\_list | ( | struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *ccid\_list*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *ccid\_list\_len* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the CCID list of a codec capability metadata.

Parameters
:   | codec\_cap | The codec capability to set data for. |
    | --- | --- |
    | ccid\_list | The program info to set. |
    | ccid\_list\_len | The length of `ccid_list`. |

Return values
:   | data\_len | The `codec_cap.data_len` on success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENOMEM | The new value could not be set or added due to lack of memory |

## [◆ ](#gac00aabc7329027852a7caf5cdff2bc26)bt\_audio\_codec\_cap\_meta\_set\_extended()

| int bt\_audio\_codec\_cap\_meta\_set\_extended | ( | struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *extended\_meta*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *extended\_meta\_len* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the extended metadata of a codec capability metadata.

Parameters
:   | codec\_cap | The codec capability to set data for. |
    | --- | --- |
    | extended\_meta | The extended metadata to set. |
    | extended\_meta\_len | The length of `extended_meta`. |

Return values
:   | data\_len | The `codec_cap.data_len` on success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENOMEM | The new value could not be set or added due to lack of memory |

## [◆ ](#ga8182b2bed20449b8581b89677893c130)bt\_audio\_codec\_cap\_meta\_set\_lang()

| int bt\_audio\_codec\_cap\_meta\_set\_lang | ( | struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *lang*[3] ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the language of a codec capability metadata.

Parameters
:   | codec\_cap | The codec capability to set data for. |
    | --- | --- |
    | lang | The 24-bit language to set. |

Return values
:   | data\_len | The `codec_cap.data_len` on success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENOMEM | The new value could not be set or added due to lack of memory |

## [◆ ](#ga5e267dfad978cd3d52be9c31a4fac0be)bt\_audio\_codec\_cap\_meta\_set\_parental\_rating()

| int bt\_audio\_codec\_cap\_meta\_set\_parental\_rating | ( | struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760) | *parental\_rating* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the parental rating of a codec capability metadata.

Parameters
:   | codec\_cap | The codec capability to set data for. |
    | --- | --- |
    | parental\_rating | The parental rating to set. |

Return values
:   | data\_len | The `codec_cap.data_len` on success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENOMEM | The new value could not be set or added due to lack of memory |

## [◆ ](#ga7fe0d4553d6accf5c89645cbf86149bf)bt\_audio\_codec\_cap\_meta\_set\_pref\_context()

| int bt\_audio\_codec\_cap\_meta\_set\_pref\_context | ( | struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) | *ctx* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the preferred context of a codec capability metadata.

Parameters
:   | codec\_cap | The codec capability to set data for. |
    | --- | --- |
    | ctx | The preferred context to set. |

Return values
:   | data\_len | The `codec_cap.data_len` on success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENOMEM | The new value could not be set or added due to lack of memory |

## [◆ ](#ga43d2ec3a4d621c26843de82db7fd2189)bt\_audio\_codec\_cap\_meta\_set\_program\_info()

| int bt\_audio\_codec\_cap\_meta\_set\_program\_info | ( | struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *program\_info*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *program\_info\_len* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the program info of a codec capability metadata.

Parameters
:   | codec\_cap | The codec capability to set data for. |
    | --- | --- |
    | program\_info | The program info to set. |
    | program\_info\_len | The length of `program_info`. |

Return values
:   | data\_len | The `codec_cap.data_len` on success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENOMEM | The new value could not be set or added due to lack of memory |

## [◆ ](#gafbb0d6282d989e8bc70caada2845b337)bt\_audio\_codec\_cap\_meta\_set\_program\_info\_uri()

| int bt\_audio\_codec\_cap\_meta\_set\_program\_info\_uri | ( | struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *program\_info\_uri*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *program\_info\_uri\_len* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the program info URI of a codec capability metadata.

Parameters
:   | codec\_cap | The codec capability to set data for. |
    | --- | --- |
    | program\_info\_uri | The program info URI to set. |
    | program\_info\_uri\_len | The length of `program_info_uri`. |

Return values
:   | data\_len | The `codec_cap.data_len` on success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENOMEM | The new value could not be set or added due to lack of memory |

## [◆ ](#ga5cc7f360049c38c8de631ea33dbc44ab)bt\_audio\_codec\_cap\_meta\_set\_stream\_context()

| int bt\_audio\_codec\_cap\_meta\_set\_stream\_context | ( | struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) | *ctx* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the stream context of a codec capability metadata.

Parameters
:   | codec\_cap | The codec capability to set data for. |
    | --- | --- |
    | ctx | The stream context to set. |

Return values
:   | data\_len | The `codec_cap.data_len` on success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENOMEM | The new value could not be set or added due to lack of memory |

## [◆ ](#ga1fdfd8c36f4131bcf4ffd2b7f176b631)bt\_audio\_codec\_cap\_meta\_set\_val()

| int bt\_audio\_codec\_cap\_meta\_set\_val | ( | struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) | *type*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_len* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set or add a specific codec capability metadata value.

Parameters
:   | codec\_cap | The codec capability to set the value in. |
    | --- | --- |
    | type | The type id to set. |
    | data | Pointer to the data-pointer to set. |
    | data\_len | Length of `data`. |

Return values
:   | meta\_len | The `codec_cap.meta_len` on success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENOMEM | The new value could not be set or added due to lack of memory |

## [◆ ](#ga1f06789782541beab9aab4914f91bb57)bt\_audio\_codec\_cap\_meta\_set\_vendor()

| int bt\_audio\_codec\_cap\_meta\_set\_vendor | ( | struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *vendor\_meta*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *vendor\_meta\_len* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the vendor specific metadata of a codec capability metadata.

Parameters
:   | codec\_cap | The codec capability to set data for. |
    | --- | --- |
    | vendor\_meta | The vendor specific metadata to set. |
    | vendor\_meta\_len | The length of `vendor_meta`. |

Return values
:   | data\_len | The `codec_cap.data_len` on success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENOMEM | The new value could not be set or added due to lack of memory |

## [◆ ](#ga40848f5375d1e58622c580112c282f2e)bt\_audio\_codec\_cap\_meta\_unset\_val()

| int bt\_audio\_codec\_cap\_meta\_unset\_val | ( | struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) | *type* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Unset a specific codec capability metadata value.

The type and the value will be removed from the codec capability metadata.

Parameters
:   | codec\_cap | The codec data to set the value in. |
    | --- | --- |
    | type | The type id to unset. |

Return values
:   | meta\_len | The of `codec_cap.meta_len` on success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |

## [◆ ](#ga53e5df6cc4cfbed12b59a6a506657772)bt\_audio\_codec\_cap\_set\_frame\_dur()

| int bt\_audio\_codec\_cap\_set\_frame\_dur | ( | struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_codec\_cap\_frame\_dur](group__bt__audio.md#gaf37e8e19f956afb3c3a413cbaa1a21f5) | *frame\_dur* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the frame duration of a codec capability.

Parameters
:   | codec\_cap | The codec capabilities to set data for. |
    | --- | --- |
    | frame\_dur | The frame duration to set. |

Return values
:   | data\_len | The `codec_cap.data_len` on success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENOMEM | The new value could not be set or added due to lack of memory |

## [◆ ](#gac0655c0bd6552ab8a265076d7d0cd1b2)bt\_audio\_codec\_cap\_set\_freq()

| int bt\_audio\_codec\_cap\_set\_freq | ( | struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_codec\_cap\_freq](group__bt__audio.md#gaafc1106d5d305874ee2f540c850ff5b4) | *freq* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the supported frequencies of a codec capability.

Parameters
:   | codec\_cap | The codec capabilities to set data for. |
    | --- | --- |
    | freq | The supported frequencies to set. |

Return values
:   | data\_len | The `codec_cap.data_len` on success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENOMEM | The new value could not be set or added due to lack of memory |

## [◆ ](#ga3785bc41f56f8f2a09248396dadb31da)bt\_audio\_codec\_cap\_set\_max\_codec\_frames\_per\_sdu()

| int bt\_audio\_codec\_cap\_set\_max\_codec\_frames\_per\_sdu | ( | struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *codec\_frames\_per\_sdu* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the maximum codec frames per SDU of a codec capability.

Parameters
:   | codec\_cap | The codec capabilities to set data for. |
    | --- | --- |
    | codec\_frames\_per\_sdu | The maximum codec frames per SDU to set. |

Return values
:   | data\_len | The `codec_cap.data_len` on success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENOMEM | The new value could not be set or added due to lack of memory |

## [◆ ](#gac1c42460cd3c55bbfbd467f84ab2d78d)bt\_audio\_codec\_cap\_set\_octets\_per\_frame()

| int bt\_audio\_codec\_cap\_set\_octets\_per\_frame | ( | struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_audio\_codec\_octets\_per\_codec\_frame](structbt__audio__codec__octets__per__codec__frame.md) \* | *codec\_frame* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the octets per codec frame of a codec capability.

Parameters
:   | codec\_cap | The codec capabilities to set data for. |
    | --- | --- |
    | codec\_frame | The octets per codec frame to set. |

Return values
:   | data\_len | The `codec_cap.data_len` on success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENOMEM | The new value could not be set or added due to lack of memory |

## [◆ ](#gaf6b2717823f9f3136237ed6a6515449e)bt\_audio\_codec\_cap\_set\_supported\_audio\_chan\_counts()

| int bt\_audio\_codec\_cap\_set\_supported\_audio\_chan\_counts | ( | struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_codec\_cap\_chan\_count](group__bt__audio.md#gae695b5d17359967703f2509db1671fa5) | *chan\_count* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set the channel count of a codec capability.

Parameters
:   | codec\_cap | The codec capabilities to set data for. |
    | --- | --- |
    | chan\_count | The channel count frequency to set. |

Return values
:   | data\_len | The `codec_cap.data_len` on success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENOMEM | The new value could not be set or added due to lack of memory |

## [◆ ](#ga0c2c816b0b2b85aa5dd38f21caceea40)bt\_audio\_codec\_cap\_set\_val()

| int bt\_audio\_codec\_cap\_set\_val | ( | struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015) | *type*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_len* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Set or add a specific codec capability value.

Parameters
:   | codec\_cap | The codec data to set the value in. |
    | --- | --- |
    | type | The type id to set |
    | data | Pointer to the data-pointer to set |
    | data\_len | Length of `data` |

Return values
:   | data\_len | The `codec_cap.data_len` on success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENOMEM | The new value could not be set or added due to lack of memory |

## [◆ ](#gabc9962212ad65339ff02ba1389d5f9f8)bt\_audio\_codec\_cap\_unset\_val()

| int bt\_audio\_codec\_cap\_unset\_val | ( | struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \* | *codec\_cap*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015) | *type* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Unset a specific codec capability value.

The type and the value will be removed from the codec capability.

Parameters
:   | codec\_cap | The codec data to set the value in. |
    | --- | --- |
    | type | The type id to unset. |

Return values
:   | data\_len | The `codec_cap.data_len` on success |
    | --- | --- |
    | -EINVAL | Arguments are invalid |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
