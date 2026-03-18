---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structsys__hashmap.html
original_path: doxygen/html/structsys__hashmap.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sys\_hashmap Struct Reference

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [Hashmap](group__hashmap__apis.md)

Generic Hashmap.
[More...](#details)

`#include <[hash_map.h](hash__map_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [sys\_hashmap\_api](structsys__hashmap__api.md) \* | [api](#a88b8b0e3773a5f388bd5362b7283c5a9) |
|  | Hashmap API. |
| const struct [sys\_hashmap\_config](structsys__hashmap__config.md) \* | [config](#ae52ee56fa68b011dc388a1ef0a01a7d2) |
|  | Hashmap configuration. |
| struct [sys\_hashmap\_data](structsys__hashmap__data.md) \* | [data](#a405d543f6015d0defa362e4285b0d6cd) |
|  | Hashmap data. |
| [sys\_hash\_func32\_t](group__hash__functions.md#ga2566ca73d30b47ae66659e26fc985fad) | [hash\_func](#a56028566cb14b8722503e527445bbfc9) |
|  | Hash function. |
| [sys\_hashmap\_allocator\_t](group__hashmap__apis.md#ga813a4f65e3672651ef37c06dccdcfebc) | [alloc\_func](#ad1cf742360a600ee20c89d68ea42b3f8) |
|  | Allocator. |

## Detailed Description

Generic Hashmap.

## Field Documentation

## [◆ ](#ad1cf742360a600ee20c89d68ea42b3f8)alloc\_func

| [sys\_hashmap\_allocator\_t](group__hashmap__apis.md#ga813a4f65e3672651ef37c06dccdcfebc) sys\_hashmap::alloc\_func |
| --- |

Allocator.

## [◆ ](#a88b8b0e3773a5f388bd5362b7283c5a9)api

| const struct [sys\_hashmap\_api](structsys__hashmap__api.md)\* sys\_hashmap::api |
| --- |

Hashmap API.

## [◆ ](#ae52ee56fa68b011dc388a1ef0a01a7d2)config

| const struct [sys\_hashmap\_config](structsys__hashmap__config.md)\* sys\_hashmap::config |
| --- |

Hashmap configuration.

## [◆ ](#a405d543f6015d0defa362e4285b0d6cd)data

| struct [sys\_hashmap\_data](structsys__hashmap__data.md)\* sys\_hashmap::data |
| --- |

Hashmap data.

## [◆ ](#a56028566cb14b8722503e527445bbfc9)hash\_func

| [sys\_hash\_func32\_t](group__hash__functions.md#ga2566ca73d30b47ae66659e26fc985fad) sys\_hashmap::hash\_func |
| --- |

Hash function.

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[hash\_map.h](hash__map_8h_source.md)

- [sys\_hashmap](structsys__hashmap.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
