---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__cap__unicast__audio__start__stream__param.html
original_path: doxygen/html/structbt__cap__unicast__audio__start__stream__param.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_unicast\_audio\_start\_stream\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Stream specific parameters for the [bt\_cap\_initiator\_unicast\_audio\_start()](group__bt__cap.md#gae19686be7f8aef1cc92c70fea93e1184 "Setup and start unicast audio streams for a set of devices.") function.
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union [bt\_cap\_set\_member](unionbt__cap__set__member.md) | [member](#a9613a24e05a362a2f70d8e433ca6b42b) |
|  | Coordinated or ad-hoc set member. |
| struct [bt\_cap\_stream](structbt__cap__stream.md) \* | [stream](#a109acdedd1249ea8342f06de28989d4e) |
|  | Stream for the `member`. |
| struct bt\_bap\_ep \* | [ep](#aa9a13263d287a2ddb241a8dc13baeffb) |
|  | Endpoint reference for the `stream`. |
| struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | [codec\_cfg](#a5cf7ff347ff602bc4387e5b75f09205a) |
|  | Codec configuration. |

## Detailed Description

Stream specific parameters for the [bt\_cap\_initiator\_unicast\_audio\_start()](group__bt__cap.md#gae19686be7f8aef1cc92c70fea93e1184 "Setup and start unicast audio streams for a set of devices.") function.

## Field Documentation

## [◆ ](#a5cf7ff347ff602bc4387e5b75f09205a)codec\_cfg

| struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md)\* bt\_cap\_unicast\_audio\_start\_stream\_param::codec\_cfg |
| --- |

Codec configuration.

The `codec_cfg.meta` shall include a list of CCIDs ([BT\_AUDIO\_METADATA\_TYPE\_CCID\_LIST](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b "BT_AUDIO_METADATA_TYPE_CCID_LIST")) as well as a non-0 stream context ([BT\_AUDIO\_METADATA\_TYPE\_STREAM\_CONTEXT](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa "BT_AUDIO_METADATA_TYPE_STREAM_CONTEXT")) bitfield.

## [◆ ](#aa9a13263d287a2ddb241a8dc13baeffb)ep

| struct bt\_bap\_ep\* bt\_cap\_unicast\_audio\_start\_stream\_param::ep |
| --- |

Endpoint reference for the `stream`.

## [◆ ](#a9613a24e05a362a2f70d8e433ca6b42b)member

| union [bt\_cap\_set\_member](unionbt__cap__set__member.md) bt\_cap\_unicast\_audio\_start\_stream\_param::member |
| --- |

Coordinated or ad-hoc set member.

## [◆ ](#a109acdedd1249ea8342f06de28989d4e)stream

| struct [bt\_cap\_stream](structbt__cap__stream.md)\* bt\_cap\_unicast\_audio\_start\_stream\_param::stream |
| --- |

Stream for the `member`.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_unicast\_audio\_start\_stream\_param](structbt__cap__unicast__audio__start__stream__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
