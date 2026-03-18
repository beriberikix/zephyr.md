---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__has__preset__record.html
original_path: doxygen/html/structbt__has__preset__record.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_has\_preset\_record Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Hearing Access Service (HAS)](group__bt__has.md)

Preset record definition.
[More...](#details)

`#include <[has.h](has_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [index](#a68484827708a19a75f2cdf922f01e677) |
|  | Unique preset index. |
| enum [bt\_has\_properties](group__bt__has.md#ga7b8913a9f9bc4d5c066582780adcf274) | [properties](#ad3fc652d24a8b625b97abb02f0fb66bb) |
|  | Bitfield of preset properties. |
| const char \* | [name](#ac064f0ae2841627930fb3ca0370ef5ec) |
|  | Preset name. |

## Detailed Description

Preset record definition.

## Field Documentation

## [◆ ](#a68484827708a19a75f2cdf922f01e677)index

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_has\_preset\_record::index |
| --- |

Unique preset index.

## [◆ ](#ac064f0ae2841627930fb3ca0370ef5ec)name

| const char\* bt\_has\_preset\_record::name |
| --- |

Preset name.

## [◆ ](#ad3fc652d24a8b625b97abb02f0fb66bb)properties

| enum [bt\_has\_properties](group__bt__has.md#ga7b8913a9f9bc4d5c066582780adcf274) bt\_has\_preset\_record::properties |
| --- |

Bitfield of preset properties.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[has.h](has_8h_source.md)

- [bt\_has\_preset\_record](structbt__has__preset__record.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
