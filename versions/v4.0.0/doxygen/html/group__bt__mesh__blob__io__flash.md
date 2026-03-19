---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bt__mesh__blob__io__flash.html
original_path: doxygen/html/group__bt__mesh__blob__io__flash.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bluetooth Mesh BLOB flash stream

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_blob\_io\_flash](structbt__mesh__blob__io__flash.md) |
|  | BLOB flash stream. [More...](structbt__mesh__blob__io__flash.md#details) |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_blob\_io\_flash\_init](#ga8d99fd3dc35230447f7e7ef9f2c4bc81) (struct [bt\_mesh\_blob\_io\_flash](structbt__mesh__blob__io__flash.md) \*flash, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) area\_id, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset) |
|  | Initialize a flash stream. |

## Detailed Description

## Function Documentation

## [◆ ](#ga8d99fd3dc35230447f7e7ef9f2c4bc81)bt\_mesh\_blob\_io\_flash\_init()

| int bt\_mesh\_blob\_io\_flash\_init | ( | struct [bt\_mesh\_blob\_io\_flash](structbt__mesh__blob__io__flash.md) \* | *flash*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *area\_id*, |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *offset* ) |

`#include <[blob_io_flash.h](blob__io__flash_8h.md)>`

Initialize a flash stream.

Parameters
:   | flash | Flash stream. |
    | --- | --- |
    | area\_id | Flash partition identifier. See [flash\_area\_open](group__flash__area__api.md#ga6fe2593210688eb85e03bea5f96ea2f7 "flash_area_open"). |
    | offset | Offset into the flash area, in bytes. |

Returns
:   0 on success or (negative) error code otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
