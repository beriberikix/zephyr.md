---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__a2dp__ep.html
original_path: doxygen/html/structbt__a2dp__ep.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_a2dp\_ep Struct Reference

Stream End Point.
[More...](#details)

`#include <[a2dp.h](a2dp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [codec\_type](#a912cf7cd18a58a1cc1a5e326e8bebb73) |
|  | Code Type [bt\_a2dp\_codec\_type](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6 "bt_a2dp_codec_type"). |
| struct [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md) \* | [codec\_cap](#ae4dcc7f4bca5cc34cf05c2277379a1b3) |
|  | Capabilities. |
| struct [bt\_avdtp\_sep](structbt__avdtp__sep.md) | [sep](#a2565b03e09e5abcf239c4c671b348c50) |
|  | AVDTP Stream End Point Identifier. |
| struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \* | [stream](#a4902b9fde9be1aa9b7a35c22a21cd4a6) |

## Detailed Description

Stream End Point.

## Field Documentation

## [◆ ](#ae4dcc7f4bca5cc34cf05c2277379a1b3)codec\_cap

| struct [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md)\* bt\_a2dp\_ep::codec\_cap |
| --- |

Capabilities.

## [◆ ](#a912cf7cd18a58a1cc1a5e326e8bebb73)codec\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_a2dp\_ep::codec\_type |
| --- |

Code Type [bt\_a2dp\_codec\_type](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6 "bt_a2dp_codec_type").

## [◆ ](#a2565b03e09e5abcf239c4c671b348c50)sep

| struct [bt\_avdtp\_sep](structbt__avdtp__sep.md) bt\_a2dp\_ep::sep |
| --- |

AVDTP Stream End Point Identifier.

## [◆ ](#a4902b9fde9be1aa9b7a35c22a21cd4a6)stream

| struct [bt\_a2dp\_stream](structbt__a2dp__stream.md)\* bt\_a2dp\_ep::stream |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[a2dp.h](a2dp_8h_source.md)

- [bt\_a2dp\_ep](structbt__a2dp__ep.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
