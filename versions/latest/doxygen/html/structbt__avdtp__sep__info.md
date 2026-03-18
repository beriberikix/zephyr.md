---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__avdtp__sep__info.html
original_path: doxygen/html/structbt__avdtp__sep__info.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_avdtp\_sep\_info Struct Reference

AVDTP stream endpoint information.
[More...](#details)

`#include <[avdtp.h](avdtp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [inuse](#ab644a59a54d943e3d4729a198bda59cd):1 |
|  | End Point usage status. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [id](#a03bf1e8c29eaff7ef3b48f21dff7aa49):6 |
|  | Stream End Point ID that is the identifier of the stream endpoint. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [reserved](#a3d6c6832a40cdb31976a447459576e0f):1 |
|  | Reserved. |
| enum [bt\_avdtp\_sep\_type](avdtp_8h.md#a28b828df32df5a40e8487dc4dee78757) | [tsep](#add86d89b0e062f034aa85bf7121313ee) |
|  | Stream End-point Type that indicates if the stream end-point is SNK or SRC. |
| enum [bt\_avdtp\_media\_type](avdtp_8h.md#a6e9f13217ede2687e206b6a8cbd9137f) | [media\_type](#a8cd4323a80ad4138095d5aceb08a64b6) |
|  | Media-type of the End Point Only [BT\_AVDTP\_AUDIO](avdtp_8h.md#a6e9f13217ede2687e206b6a8cbd9137faf77a41d832f11dfa01946a6dc7ceee58 "BT_AVDTP_AUDIO") is supported now. |

## Detailed Description

AVDTP stream endpoint information.

Don't need to care endianness because it is not used for data parsing.

## Field Documentation

## [◆ ](#a03bf1e8c29eaff7ef3b48f21dff7aa49)id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_avdtp\_sep\_info::id |
| --- |

Stream End Point ID that is the identifier of the stream endpoint.

## [◆ ](#ab644a59a54d943e3d4729a198bda59cd)inuse

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_avdtp\_sep\_info::inuse |
| --- |

End Point usage status.

## [◆ ](#a8cd4323a80ad4138095d5aceb08a64b6)media\_type

| enum [bt\_avdtp\_media\_type](avdtp_8h.md#a6e9f13217ede2687e206b6a8cbd9137f) bt\_avdtp\_sep\_info::media\_type |
| --- |

Media-type of the End Point Only [BT\_AVDTP\_AUDIO](avdtp_8h.md#a6e9f13217ede2687e206b6a8cbd9137faf77a41d832f11dfa01946a6dc7ceee58 "BT_AVDTP_AUDIO") is supported now.

## [◆ ](#a3d6c6832a40cdb31976a447459576e0f)reserved

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_avdtp\_sep\_info::reserved |
| --- |

Reserved.

## [◆ ](#add86d89b0e062f034aa85bf7121313ee)tsep

| enum [bt\_avdtp\_sep\_type](avdtp_8h.md#a28b828df32df5a40e8487dc4dee78757) bt\_avdtp\_sep\_info::tsep |
| --- |

Stream End-point Type that indicates if the stream end-point is SNK or SRC.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[avdtp.h](avdtp_8h_source.md)

- [bt\_avdtp\_sep\_info](structbt__avdtp__sep__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
