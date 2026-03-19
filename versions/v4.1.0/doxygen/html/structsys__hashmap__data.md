---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsys__hashmap__data.html
original_path: doxygen/html/structsys__hashmap__data.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sys\_hashmap\_data Struct Reference

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [Hashmap](group__hashmap__apis.md)

Generic Hashmap data.
[More...](#details)

`#include <[hash_map_api.h](hash__map__api_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [buckets](#ad6f00cc9bfa4e654a3bdcd5c8803f326) |
|  | Pointer for implementation-specific Hashmap storage. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [n\_buckets](#a79892de2c54612860f0dd48bce88aeea) |
|  | The number of buckets currently allocated. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [size](#ac453e2dc52f989617feebedc6eeb2929) |
|  | The number of entries currently in the Hashmap. |

## Detailed Description

Generic Hashmap data.

Note
:   When *size* is zero, *buckets* should be [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4).

## Field Documentation

## [◆ ](#ad6f00cc9bfa4e654a3bdcd5c8803f326)buckets

| void\* sys\_hashmap\_data::buckets |
| --- |

Pointer for implementation-specific Hashmap storage.

## [◆ ](#a79892de2c54612860f0dd48bce88aeea)n\_buckets

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sys\_hashmap\_data::n\_buckets |
| --- |

The number of buckets currently allocated.

## [◆ ](#ac453e2dc52f989617feebedc6eeb2929)size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sys\_hashmap\_data::size |
| --- |

The number of entries currently in the Hashmap.

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[hash\_map\_api.h](hash__map__api_8h_source.md)

- [sys\_hashmap\_data](structsys__hashmap__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
