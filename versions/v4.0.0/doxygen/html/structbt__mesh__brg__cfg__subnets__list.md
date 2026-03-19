---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__brg__cfg__subnets__list.html
original_path: doxygen/html/structbt__mesh__brg__cfg__subnets__list.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_brg\_cfg\_subnets\_list Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bridge Configuration common header](group__bt__mesh__brg__cfg.md)

Bridged Subnets List response.
[More...](#details)

`#include <[brg_cfg.h](brg__cfg_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_mesh\_brg\_cfg\_filter\_netkey](structbt__mesh__brg__cfg__filter__netkey.md) | [net\_idx\_filter](#aa0ccb8e8b74365dfc7a4e2f5f38c50c6) |
|  | Filter applied NetKey Indexes, and NetKey Index used for filtering. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [start\_idx](#a9f4cb39c12130ebba6c9d275a4a6b310) |
|  | Start offset in units of bridges. |
| struct [net\_buf\_simple](structnet__buf__simple.md) \* | [list](#a00ebe6255aabcd1cab49f08e4dc7e21b) |
|  | Pointer to allocated buffer for storing filtered of NetKey Indexes. |

## Detailed Description

Bridged Subnets List response.

## Field Documentation

## [◆ ](#a00ebe6255aabcd1cab49f08e4dc7e21b)list

| struct [net\_buf\_simple](structnet__buf__simple.md)\* bt\_mesh\_brg\_cfg\_subnets\_list::list |
| --- |

Pointer to allocated buffer for storing filtered of NetKey Indexes.

## [◆ ](#aa0ccb8e8b74365dfc7a4e2f5f38c50c6)net\_idx\_filter

| struct [bt\_mesh\_brg\_cfg\_filter\_netkey](structbt__mesh__brg__cfg__filter__netkey.md) bt\_mesh\_brg\_cfg\_subnets\_list::net\_idx\_filter |
| --- |

Filter applied NetKey Indexes, and NetKey Index used for filtering.

## [◆ ](#a9f4cb39c12130ebba6c9d275a4a6b310)start\_idx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_brg\_cfg\_subnets\_list::start\_idx |
| --- |

Start offset in units of bridges.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[brg\_cfg.h](brg__cfg_8h_source.md)

- [bt\_mesh\_brg\_cfg\_subnets\_list](structbt__mesh__brg__cfg__subnets__list.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
