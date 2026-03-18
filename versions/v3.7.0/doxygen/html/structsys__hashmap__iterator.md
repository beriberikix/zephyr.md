---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structsys__hashmap__iterator.html
original_path: doxygen/html/structsys__hashmap__iterator.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sys\_hashmap\_iterator Struct Reference

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [Hashmap](group__hashmap__apis.md)

Generic Hashmap iterator interface.
[More...](#details)

`#include <[hash_map_api.h](hash__map__api_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [sys\_hashmap](structsys__hashmap.md) \* | [map](#a0e868afd37b06566caff62be0fd4290c) |
|  | Pointer to the associated Hashmap. |
| void(\* | [next](#a8c79527ba05d0dcfe2f13e0fe387efa4) )(struct [sys\_hashmap\_iterator](structsys__hashmap__iterator.md) \*it) |
|  | Modify the iterator in-place to point to the next Hashmap entry. |
| void \* | [state](#a19938b219d6b249721968cce1abece9e) |
|  | Implementation-specific iterator state. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [key](#a47684d01a30deca036f58b98b845e958) |
|  | Key associated with the current entry. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [value](#a9987d100e22822f07182278cbb431b24) |
|  | Value associated with the current entry. |
| const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [size](#a4145137c2d1c95a7658902287cea2096) |
|  | Number of entries in the map. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [pos](#a0bc36e419dcb98e120342be0dba1604d) |
|  | Number of entries already iterated. |

## Detailed Description

Generic Hashmap iterator interface.

Note
:   *next* should not be used without first checking [sys\_hashmap\_iterator\_has\_next](group__hashmap__apis.md#ga15020630e76f826893c58faded3737ed "sys_hashmap_iterator_has_next")

## Field Documentation

## [◆ ](#a47684d01a30deca036f58b98b845e958)key

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sys\_hashmap\_iterator::key |
| --- |

Key associated with the current entry.

## [◆ ](#a0e868afd37b06566caff62be0fd4290c)map

| const struct [sys\_hashmap](structsys__hashmap.md)\* sys\_hashmap\_iterator::map |
| --- |

Pointer to the associated Hashmap.

## [◆ ](#a8c79527ba05d0dcfe2f13e0fe387efa4)next

| void(\* sys\_hashmap\_iterator::next) (struct [sys\_hashmap\_iterator](structsys__hashmap__iterator.md) \*it) |
| --- |

Modify the iterator in-place to point to the next Hashmap entry.

## [◆ ](#a0bc36e419dcb98e120342be0dba1604d)pos

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sys\_hashmap\_iterator::pos |
| --- |

Number of entries already iterated.

## [◆ ](#a4145137c2d1c95a7658902287cea2096)size

| const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sys\_hashmap\_iterator::size |
| --- |

Number of entries in the map.

## [◆ ](#a19938b219d6b249721968cce1abece9e)state

| void\* sys\_hashmap\_iterator::state |
| --- |

Implementation-specific iterator state.

## [◆ ](#a9987d100e22822f07182278cbb431b24)value

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sys\_hashmap\_iterator::value |
| --- |

Value associated with the current entry.

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[hash\_map\_api.h](hash__map__api_8h_source.md)

- [sys\_hashmap\_iterator](structsys__hashmap__iterator.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
