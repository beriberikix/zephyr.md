---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structosdp__event__cardread.html
original_path: doxygen/html/structosdp__event__cardread.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

osdp\_event\_cardread Struct Reference

OSDP event cardread.
[More...](#details)

`#include <[osdp.h](osdp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int | [reader\_no](#ac6be298c814fcc933d6919a2c7fbb24c) |
|  | Reader number. |
| enum [osdp\_event\_cardread\_format\_e](osdp_8h.md#a976512dfb1a4dc3ea9326d72a0abb5e7) | [format](#a7a94e50e9729468baac011dde4806f00) |
|  | Format of the card being read. |
| int | [direction](#a025b2965987644fe08581b93d1067cb1) |
|  | Direction of data in *data* array. |
| int | [length](#a025f3a460042fda69212db1c20d40bc5) |
|  | Length of card data in bytes or bits depending on *format*. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data](#af431337d9312618312360ef723f15b98) [64] |
|  | Card data of *length* bytes or bits bits depending on *format*. |

## Detailed Description

OSDP event cardread.

Note
:   When *format* is set to OSDP\_CARD\_FMT\_RAW\_UNSPECIFIED or OSDP\_CARD\_FMT\_RAW\_WIEGAND, the length is expressed in bits. OTOH, when it is set to OSDP\_CARD\_FMT\_ASCII, the length is in bytes. The number of bytes to read from the *data* field must be interpreted accordingly.

## Field Documentation

## [◆ ](#af431337d9312618312360ef723f15b98)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_event\_cardread::data[64] |
| --- |

Card data of *length* bytes or bits bits depending on *format*.

## [◆ ](#a025b2965987644fe08581b93d1067cb1)direction

| int osdp\_event\_cardread::direction |
| --- |

Direction of data in *data* array.

- 0 - Forward
- 1 - Backward

## [◆ ](#a7a94e50e9729468baac011dde4806f00)format

| enum [osdp\_event\_cardread\_format\_e](osdp_8h.md#a976512dfb1a4dc3ea9326d72a0abb5e7) osdp\_event\_cardread::format |
| --- |

Format of the card being read.

## [◆ ](#a025f3a460042fda69212db1c20d40bc5)length

| int osdp\_event\_cardread::length |
| --- |

Length of card data in bytes or bits depending on *format*.

## [◆ ](#ac6be298c814fcc933d6919a2c7fbb24c)reader\_no

| int osdp\_event\_cardread::reader\_no |
| --- |

Reader number.

0 = First Reader, 1 = Second Reader, etc.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/[osdp.h](osdp_8h_source.md)

- [osdp\_event\_cardread](structosdp__event__cardread.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
