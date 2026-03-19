---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__mesh__blob__io__flash.html
original_path: doxygen/html/structbt__mesh__blob__io__flash.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_blob\_io\_flash Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh BLOB flash stream](group__bt__mesh__blob__io__flash.md)

BLOB flash stream.
[More...](#details)

`#include <[blob_io_flash.h](blob__io__flash_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [area\_id](#a3b506d86d9cc7fb7206f96cbdd2cd3fe) |
|  | Flash area ID to write the BLOB to. |
| enum [bt\_mesh\_blob\_io\_mode](group__bt__mesh__blob.md#ga2618fb7365f180a73a7eecd11cf2f962) | [mode](#a511648b9e653993aee99eda5efe3b1e9) |
|  | Active stream mode. |
| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | [offset](#ac4eb40a7e53adce60c2fcd11eb0b6b57) |
|  | Offset into the flash area to place the BLOB at (in bytes). |
| const struct [flash\_area](structflash__area.md) \* | [area](#a99227cd93d2b6230be7bd5cef9fb8232) |
| struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) | [io](#a24abc17719dd627e3e3d7c8e61d4c96f) |

## Detailed Description

BLOB flash stream.

## Field Documentation

## [◆ ](#a99227cd93d2b6230be7bd5cef9fb8232)area

| const struct [flash\_area](structflash__area.md)\* bt\_mesh\_blob\_io\_flash::area |
| --- |

## [◆ ](#a3b506d86d9cc7fb7206f96cbdd2cd3fe)area\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_blob\_io\_flash::area\_id |
| --- |

Flash area ID to write the BLOB to.

## [◆ ](#a24abc17719dd627e3e3d7c8e61d4c96f)io

| struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) bt\_mesh\_blob\_io\_flash::io |
| --- |

## [◆ ](#a511648b9e653993aee99eda5efe3b1e9)mode

| enum [bt\_mesh\_blob\_io\_mode](group__bt__mesh__blob.md#ga2618fb7365f180a73a7eecd11cf2f962) bt\_mesh\_blob\_io\_flash::mode |
| --- |

Active stream mode.

## [◆ ](#ac4eb40a7e53adce60c2fcd11eb0b6b57)offset

| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) bt\_mesh\_blob\_io\_flash::offset |
| --- |

Offset into the flash area to place the BLOB at (in bytes).

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[blob\_io\_flash.h](blob__io__flash_8h_source.md)

- [bt\_mesh\_blob\_io\_flash](structbt__mesh__blob__io__flash.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
