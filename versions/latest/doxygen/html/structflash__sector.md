---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structflash__sector.html
original_path: doxygen/html/structflash__sector.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

flash\_sector Struct Reference

[Operating System Services](group__os__services.md) » [Storage APIs](group__storage__apis.md) » [flash area Interface](group__flash__area__api.md)

Structure for transfer flash sector boundaries.
[More...](#details)

`#include <[flash_map.h](flash__map_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | [fs\_off](#a2e9899681d4ec66fac277a7a52e1830b) |
|  | Sector offset from the beginning of the flash device. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [fs\_size](#ab1fef4b1b6978d25b5f809d778888f75) |
|  | Sector size in bytes. |

## Detailed Description

Structure for transfer flash sector boundaries.

This template is used for presentation of flash memory structure. It consumes much less RAM than [flash\_area](structflash__area.md "flash_area")

## Field Documentation

## [◆ ](#a2e9899681d4ec66fac277a7a52e1830b)fs\_off

| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) flash\_sector::fs\_off |
| --- |

Sector offset from the beginning of the flash device.

## [◆ ](#ab1fef4b1b6978d25b5f809d778888f75)fs\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) flash\_sector::fs\_size |
| --- |

Sector size in bytes.

---

The documentation for this struct was generated from the following file:

- zephyr/storage/[flash\_map.h](flash__map_8h_source.md)

- [flash\_sector](structflash__sector.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
