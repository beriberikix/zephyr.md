---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsys__hashmap__config.html
original_path: doxygen/html/structsys__hashmap__config.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sys\_hashmap\_config Struct Reference

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [Hashmap](group__hashmap__apis.md)

Generic Hashmap configuration.
[More...](#details)

`#include <[hash_map_api.h](hash__map__api_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [max\_size](#a5ee7a97a936d1b9b97e0669561cc0689) |
|  | Maximum number of entries. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [load\_factor](#a5a8683d82932ae397b92722269385baa) |
|  | Maximum load factor expressed in hundredths. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [initial\_n\_buckets](#a0a9911024bfc4c55f4a1fc179eaa6e10) |
|  | Initial number of buckets to allocate. |

## Detailed Description

Generic Hashmap configuration.

When there is a known limit imposed on the number of entries in the Hashmap, users should specify that via *max\_size*. When the Hashmap should have no artificial limitation in size (and be bounded only by the provided allocator), users should specify [SIZE\_MAX](stdint_8h.md#a3c75bb398badb69c7577b21486f9963f) here.

The *load\_factor* is defined as the size of the Hashmap divided by the number of buckets. In this case, the size of the Hashmap is defined as the number of valid entries plus the number of invalidated entries.

The *initial\_n\_buckets* is defined as the number of buckets to allocate when moving from size 0 to size 1 such that the maximum *load\_factor* property is preserved.

## Field Documentation

## [◆ ](#a0a9911024bfc4c55f4a1fc179eaa6e10)initial\_n\_buckets

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sys\_hashmap\_config::initial\_n\_buckets |
| --- |

Initial number of buckets to allocate.

## [◆ ](#a5a8683d82932ae397b92722269385baa)load\_factor

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sys\_hashmap\_config::load\_factor |
| --- |

Maximum load factor expressed in hundredths.

## [◆ ](#a5ee7a97a936d1b9b97e0669561cc0689)max\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sys\_hashmap\_config::max\_size |
| --- |

Maximum number of entries.

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[hash\_map\_api.h](hash__map__api_8h_source.md)

- [sys\_hashmap\_config](structsys__hashmap__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
