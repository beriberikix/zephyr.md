---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/hash__map_8h.html
original_path: doxygen/html/hash__map_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hash\_map.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[stdlib.h](stdlib_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/sys/hash_map_api.h](hash__map__api_8h_source.md)>`  
`#include <[zephyr/sys/hash_map_cxx.h](hash__map__cxx_8h_source.md)>`  
`#include <[zephyr/sys/hash_map_oa_lp.h](hash__map__oa__lp_8h_source.md)>`  
`#include <[zephyr/sys/hash_map_sc.h](hash__map__sc_8h_source.md)>`

[Go to the source code of this file.](hash__map_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sys\_hashmap](structsys__hashmap.md) |
|  | Generic Hashmap. [More...](structsys__hashmap.md#details) |

| Macros | |
| --- | --- |
| #define | [SYS\_HASHMAP\_DEFINE\_ADVANCED](group__hashmap__apis.md#gab21c79f226ca02c0225014c77f5b53d6)(\_name, \_api, \_config\_type, \_data\_type, \_hash\_func, \_alloc\_func, ...) |
|  | Declare a Hashmap (advanced). |
| #define | [SYS\_HASHMAP\_DEFINE\_STATIC\_ADVANCED](group__hashmap__apis.md#gacd16dd5377fe160a2154053ba20fcbd7)(\_name, \_api, \_config\_type, \_data\_type, \_hash\_func, \_alloc\_func, ...) |
|  | Declare a Hashmap statically (advanced). |
| #define | [SYS\_HASHMAP\_DEFINE](group__hashmap__apis.md#ga2d2eb11eccb9a9040a1b5e0b6529d500)(\_name) |
|  | Declare a Hashmap. |
| #define | [SYS\_HASHMAP\_DEFINE\_STATIC](group__hashmap__apis.md#ga5e653d2dad44c32b42dfd15107f6ba3c)(\_name) |
|  | Declare a Hashmap statically. |
| #define | [SYS\_HASHMAP\_DEFAULT\_ALLOCATOR](group__hashmap__apis.md#gadcb3c72b93993222ebfe8a5e58389308)   [sys\_hashmap\_default\_allocator](group__hashmap__apis.md#gad24a1d4e49b9ce811e1a5770480d00bd) |
|  | The default Hashmap allocator. |
| #define | [SYS\_HASHMAP\_DEFAULT\_LOAD\_FACTOR](group__hashmap__apis.md#ga2f1e3b37ac9eb4c939883b1696c87b86)   75 |
|  | The default Hashmap load factor (in hundredths). |

| Functions | |
| --- | --- |
| static void \* | [sys\_hashmap\_default\_allocator](group__hashmap__apis.md#gad24a1d4e49b9ce811e1a5770480d00bd) (void \*ptr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
| static void | [sys\_hashmap\_foreach](group__hashmap__apis.md#gadee4fa23549a92afbe89a71125a859cd) (const struct [sys\_hashmap](structsys__hashmap.md) \*map, [sys\_hashmap\_callback\_t](group__hashmap__apis.md#ga6e813ebb133febdcac0bd2e6b552a0d1) cb, void \*cookie) |
|  | Iterate over all values contained in a [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |
| static void | [sys\_hashmap\_clear](group__hashmap__apis.md#gad859ec4ac776c876874bb3a88071a8aa) (struct [sys\_hashmap](structsys__hashmap.md) \*map, [sys\_hashmap\_callback\_t](group__hashmap__apis.md#ga6e813ebb133febdcac0bd2e6b552a0d1) cb, void \*cookie) |
|  | Clear all entries contained in a [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |
| static int | [sys\_hashmap\_insert](group__hashmap__apis.md#ga4868b88473fe8d160ec77bce495165cf) (struct [sys\_hashmap](structsys__hashmap.md) \*map, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) key, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*old\_value) |
|  | Insert a new entry into a [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_hashmap\_remove](group__hashmap__apis.md#ga45db255d4a6108f8da789eda01184c0b) (struct [sys\_hashmap](structsys__hashmap.md) \*map, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) key, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value) |
|  | Remove an entry from a [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_hashmap\_get](group__hashmap__apis.md#ga51125854595615092330070f380cb231) (const struct [sys\_hashmap](structsys__hashmap.md) \*map, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) key, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value) |
|  | Get a value from a [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_hashmap\_contains\_key](group__hashmap__apis.md#ga95e77f9fc362673a81bf287da20fcc38) (const struct [sys\_hashmap](structsys__hashmap.md) \*map, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) key) |
|  | Check if `map` contains a value associated with `key`. |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [sys\_hashmap\_size](group__hashmap__apis.md#ga4957bc7166ed61e66002a81dcb93bffb) (const struct [sys\_hashmap](structsys__hashmap.md) \*map) |
|  | Query the number of entries contained within `map`. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_hashmap\_is\_empty](group__hashmap__apis.md#ga5f382228a7265d2b27b9678dad442849) (const struct [sys\_hashmap](structsys__hashmap.md) \*map) |
|  | Check if `map` is empty. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sys\_hashmap\_load\_factor](group__hashmap__apis.md#ga48e6e8e55744fe270dc158bb7f31e265) (const struct [sys\_hashmap](structsys__hashmap.md) \*map) |
|  | Query the load factor of `map`. |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [sys\_hashmap\_num\_buckets](group__hashmap__apis.md#ga7527eff4dc4d0b1818cb7d9813f688b9) (const struct [sys\_hashmap](structsys__hashmap.md) \*map) |
|  | Query the number of buckets used in `map`. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_hashmap\_should\_rehash](group__hashmap__apis.md#gaee95e9b7494773f717028c764513d7ad) (const struct [sys\_hashmap](structsys__hashmap.md) \*map, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) grow, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_reserved, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*new\_num\_buckets) |
|  | Decide whether the Hashmap should be resized. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [hash\_map.h](hash__map_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
