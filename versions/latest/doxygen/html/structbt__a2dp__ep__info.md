---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__a2dp__ep__info.html
original_path: doxygen/html/structbt__a2dp__ep__info.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_a2dp\_ep\_info Struct Reference

`#include <[a2dp.h](a2dp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [codec\_type](#aca4f893b087a8429dd104b67114e36d7) |
|  | Code Type [bt\_a2dp\_codec\_type](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6 "bt_a2dp_codec_type"). |
| struct [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md) | [codec\_cap](#a7647012b4ea73a0124e2a3239a3bad7b) |
|  | Codec capabilities, if SBC, use function of [a2dp\_codec\_sbc.h](a2dp__codec__sbc_8h.md "Advance Audio Distribution Profile - SBC Codec header.") to parse it. |
| struct [bt\_avdtp\_sep\_info](structbt__avdtp__sep__info.md) | [sep\_info](#a114c3b267587efa71922e31e474fd8e4) |
|  | Stream End Point Information. |

## Field Documentation

## [◆ ](#a7647012b4ea73a0124e2a3239a3bad7b)codec\_cap

| struct [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md) bt\_a2dp\_ep\_info::codec\_cap |
| --- |

Codec capabilities, if SBC, use function of [a2dp\_codec\_sbc.h](a2dp__codec__sbc_8h.md "Advance Audio Distribution Profile - SBC Codec header.") to parse it.

## [◆ ](#aca4f893b087a8429dd104b67114e36d7)codec\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_a2dp\_ep\_info::codec\_type |
| --- |

Code Type [bt\_a2dp\_codec\_type](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6 "bt_a2dp_codec_type").

## [◆ ](#a114c3b267587efa71922e31e474fd8e4)sep\_info

| struct [bt\_avdtp\_sep\_info](structbt__avdtp__sep__info.md) bt\_a2dp\_ep\_info::sep\_info |
| --- |

Stream End Point Information.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[a2dp.h](a2dp_8h_source.md)

- [bt\_a2dp\_ep\_info](structbt__a2dp__ep__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
