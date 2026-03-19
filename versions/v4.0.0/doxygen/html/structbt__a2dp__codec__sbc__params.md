---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__a2dp__codec__sbc__params.html
original_path: doxygen/html/structbt__a2dp__codec__sbc__params.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_a2dp\_codec\_sbc\_params Struct Reference

SBC Codec.
[More...](#details)

`#include <[a2dp_codec_sbc.h](a2dp__codec__sbc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [config](#a80b0705befa9c573e4653a5f88f81e8d) [2] |
|  | First two octets of configuration. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [min\_bitpool](#a026f28b42a3e8b41a2597cfa4ca01f95) |
|  | Minimum Bitpool Value. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [max\_bitpool](#a34319bc3d168e5eb7d3ef2cae521ca96) |
|  | Maximum Bitpool Value. |

## Detailed Description

SBC Codec.

## Field Documentation

## [◆ ](#a80b0705befa9c573e4653a5f88f81e8d)config

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_a2dp\_codec\_sbc\_params::config[2] |
| --- |

First two octets of configuration.

## [◆ ](#a34319bc3d168e5eb7d3ef2cae521ca96)max\_bitpool

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_a2dp\_codec\_sbc\_params::max\_bitpool |
| --- |

Maximum Bitpool Value.

## [◆ ](#a026f28b42a3e8b41a2597cfa4ca01f95)min\_bitpool

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_a2dp\_codec\_sbc\_params::min\_bitpool |
| --- |

Minimum Bitpool Value.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[a2dp\_codec\_sbc.h](a2dp__codec__sbc_8h_source.md)

- [bt\_a2dp\_codec\_sbc\_params](structbt__a2dp__codec__sbc__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
