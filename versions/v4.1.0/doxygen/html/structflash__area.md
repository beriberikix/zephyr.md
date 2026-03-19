---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structflash__area.html
original_path: doxygen/html/structflash__area.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

flash\_area Struct Reference

[Operating System Services](group__os__services.md) » [Storage APIs](group__storage__apis.md) » [flash area Interface](group__flash__area__api.md)

Flash partition.
[More...](#details)

`#include <[flash_map.h](flash__map_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [fa\_id](#acfe73a1f4f00fdf58129b21e5b71f5d4) |
|  | ID number. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [pad16](#af98b8f20c0219bfcdd2fc20037845a99) |
| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | [fa\_off](#a3a362ad9aa44725a0b0188042a2ee257) |
|  | Start offset from the beginning of the flash device. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [fa\_size](#a6c3c23c4c628f48c92505dddf4b24edf) |
|  | Total size. |
| const struct [device](structdevice.md) \* | [fa\_dev](#a941637492ab4e321e3b08de19cd769d2) |
|  | Backing flash device. |

## Detailed Description

Flash partition.

This structure represents a fixed-size partition on a flash device. Each partition contains one or more flash sectors.

## Field Documentation

## [◆ ](#a941637492ab4e321e3b08de19cd769d2)fa\_dev

| const struct [device](structdevice.md)\* flash\_area::fa\_dev |
| --- |

Backing flash device.

## [◆ ](#acfe73a1f4f00fdf58129b21e5b71f5d4)fa\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) flash\_area::fa\_id |
| --- |

ID number.

## [◆ ](#a3a362ad9aa44725a0b0188042a2ee257)fa\_off

| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) flash\_area::fa\_off |
| --- |

Start offset from the beginning of the flash device.

## [◆ ](#a6c3c23c4c628f48c92505dddf4b24edf)fa\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) flash\_area::fa\_size |
| --- |

Total size.

## [◆ ](#af98b8f20c0219bfcdd2fc20037845a99)pad16

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) flash\_area::pad16 |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/storage/[flash\_map.h](flash__map_8h_source.md)

- [flash\_area](structflash__area.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
