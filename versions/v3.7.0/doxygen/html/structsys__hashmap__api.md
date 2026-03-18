---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structsys__hashmap__api.html
original_path: doxygen/html/structsys__hashmap__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sys\_hashmap\_api Struct Reference

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [Hashmap](group__hashmap__apis.md)

Generic Hashmap API.
[More...](#details)

`#include <[hash_map_api.h](hash__map__api_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_hashmap\_iterator\_t](group__hashmap__apis.md#gaffc18fa6c36de71c94a836dff30f4dba) | [iter](#a1487c726730c010f286609d5cc77a109) |
|  | Iterator constructor (in-place). |
| [sys\_hashmap\_clear\_t](group__hashmap__apis.md#gac5c7ec25ad44115e83cda666d8175c79) | [clear](#a7b39c2920e8a65d7c4e01912a3ea4136) |
|  | Clear the hash table, freeing all resources. |
| [sys\_hashmap\_insert\_t](group__hashmap__apis.md#gacbd944beac0fd5377a19c662f444b50b) | [insert](#acdf4df23107858b3a1d891b3ce437dad) |
|  | Insert a key-value pair into the Hashmap. |
| [sys\_hashmap\_remove\_t](group__hashmap__apis.md#ga8ee3886c08a1e0635db3a43858f76055) | [remove](#a20443bacc5669e724ac74573539f0fb7) |
|  | Remove a key-value pair from the Hashmap. |
| [sys\_hashmap\_get\_t](group__hashmap__apis.md#gab24ce66e67e900d24c6fe3dde10a6cac) | [get](#af014aabea50f5b0568316104986de41d) |
|  | Retrieve the value associated with a given key from the Hashmap. |

## Detailed Description

Generic Hashmap API.

## Field Documentation

## [◆ ](#a7b39c2920e8a65d7c4e01912a3ea4136)clear

| [sys\_hashmap\_clear\_t](group__hashmap__apis.md#gac5c7ec25ad44115e83cda666d8175c79) sys\_hashmap\_api::clear |
| --- |

Clear the hash table, freeing all resources.

## [◆ ](#af014aabea50f5b0568316104986de41d)get

| [sys\_hashmap\_get\_t](group__hashmap__apis.md#gab24ce66e67e900d24c6fe3dde10a6cac) sys\_hashmap\_api::get |
| --- |

Retrieve the value associated with a given key from the Hashmap.

## [◆ ](#acdf4df23107858b3a1d891b3ce437dad)insert

| [sys\_hashmap\_insert\_t](group__hashmap__apis.md#gacbd944beac0fd5377a19c662f444b50b) sys\_hashmap\_api::insert |
| --- |

Insert a key-value pair into the Hashmap.

## [◆ ](#a1487c726730c010f286609d5cc77a109)iter

| [sys\_hashmap\_iterator\_t](group__hashmap__apis.md#gaffc18fa6c36de71c94a836dff30f4dba) sys\_hashmap\_api::iter |
| --- |

Iterator constructor (in-place).

## [◆ ](#a20443bacc5669e724ac74573539f0fb7)remove

| [sys\_hashmap\_remove\_t](group__hashmap__apis.md#ga8ee3886c08a1e0635db3a43858f76055) sys\_hashmap\_api::remove |
| --- |

Remove a key-value pair from the Hashmap.

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[hash\_map\_api.h](hash__map__api_8h_source.md)

- [sys\_hashmap\_api](structsys__hashmap__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
