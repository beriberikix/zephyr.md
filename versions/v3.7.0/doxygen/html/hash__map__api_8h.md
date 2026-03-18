---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/hash__map__api_8h.html
original_path: doxygen/html/hash__map__api_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hash\_map\_api.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/sys/hash_function.h](hash__function_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`

[Go to the source code of this file.](hash__map__api_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sys\_hashmap\_iterator](structsys__hashmap__iterator.md) |
|  | Generic Hashmap iterator interface. [More...](structsys__hashmap__iterator.md#details) |
| struct | [sys\_hashmap\_api](structsys__hashmap__api.md) |
|  | Generic Hashmap API. [More...](structsys__hashmap__api.md#details) |
| struct | [sys\_hashmap\_config](structsys__hashmap__config.md) |
|  | Generic Hashmap configuration. [More...](structsys__hashmap__config.md#details) |
| struct | [sys\_hashmap\_data](structsys__hashmap__data.md) |
|  | Generic Hashmap data. [More...](structsys__hashmap__data.md#details) |

| Macros | |
| --- | --- |
| #define | [SYS\_HASHMAP\_CONFIG](group__hashmap__apis.md#ga9cabdd6d7577372220065db79983f006)(\_max\_size, \_load\_factor) |
|  | Initializer for `[sys_hashmap_config](structsys__hashmap__config.md "Generic Hashmap configuration.")`. |

| Typedefs | |
| --- | --- |
| typedef void \*(\* | [sys\_hashmap\_allocator\_t](group__hashmap__apis.md#ga813a4f65e3672651ef37c06dccdcfebc)) (void \*ptr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) new\_size) |
|  | Allocator interface for [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |
| typedef void(\* | [sys\_hashmap\_iterator\_t](group__hashmap__apis.md#gaffc18fa6c36de71c94a836dff30f4dba)) (const struct [sys\_hashmap](structsys__hashmap.md) \*map, struct [sys\_hashmap\_iterator](structsys__hashmap__iterator.md) \*it) |
|  | In-place iterator constructor for [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |
| typedef void(\* | [sys\_hashmap\_callback\_t](group__hashmap__apis.md#ga6e813ebb133febdcac0bd2e6b552a0d1)) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) key, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value, void \*cookie) |
|  | Callback interface for [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |
| typedef void(\* | [sys\_hashmap\_clear\_t](group__hashmap__apis.md#gac5c7ec25ad44115e83cda666d8175c79)) (struct [sys\_hashmap](structsys__hashmap.md) \*map, [sys\_hashmap\_callback\_t](group__hashmap__apis.md#ga6e813ebb133febdcac0bd2e6b552a0d1) cb, void \*cookie) |
|  | Clear all entries contained in a [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |
| typedef int(\* | [sys\_hashmap\_insert\_t](group__hashmap__apis.md#gacbd944beac0fd5377a19c662f444b50b)) (struct [sys\_hashmap](structsys__hashmap.md) \*map, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) key, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*old\_value) |
|  | Insert a new entry into a [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [sys\_hashmap\_remove\_t](group__hashmap__apis.md#ga8ee3886c08a1e0635db3a43858f76055)) (struct [sys\_hashmap](structsys__hashmap.md) \*map, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) key, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value) |
|  | Remove an entry from a [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [sys\_hashmap\_get\_t](group__hashmap__apis.md#gab24ce66e67e900d24c6fe3dde10a6cac)) (const struct [sys\_hashmap](structsys__hashmap.md) \*map, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) key, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value) |
|  | Get a value from a [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_hashmap\_iterator\_has\_next](group__hashmap__apis.md#ga15020630e76f826893c58faded3737ed) (const struct [sys\_hashmap\_iterator](structsys__hashmap__iterator.md) \*it) |
|  | Check if a Hashmap iterator has a next entry. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [hash\_map\_api.h](hash__map__api_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
