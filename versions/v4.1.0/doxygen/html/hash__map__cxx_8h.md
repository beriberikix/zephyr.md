---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/hash__map__cxx_8h.html
original_path: doxygen/html/hash__map__cxx_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hash\_map\_cxx.h File Reference

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [Hashmap](group__hashmap__apis.md) » [Hashmap Implementations](group__hashmap__implementations.md)

C++ Hashmap.
[More...](#details)

`#include <stddef.h>`  
`#include <[zephyr/sys/hash_function.h](hash__function_8h_source.md)>`  
`#include <[zephyr/sys/hash_map_api.h](hash__map__api_8h_source.md)>`

[Go to the source code of this file.](hash__map__cxx_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SYS\_HASHMAP\_CXX\_DEFINE\_ADVANCED](#ad528dfdf1ce8accb00db14b19cd56283)(\_name, \_hash\_func, \_alloc\_func, ...) |
|  | Declare a C++ Hashmap (advanced). |
| #define | [SYS\_HASHMAP\_CXX\_DEFINE\_STATIC\_ADVANCED](#ad675ea9b18e4183170e0e7ae6ad5bc96)(\_name, \_hash\_func, \_alloc\_func, ...) |
|  | Declare a C++ Hashmap (advanced). |
| #define | [SYS\_HASHMAP\_CXX\_DEFINE\_STATIC](#aa45fa7446daaee2ad7cf90e14c6a60ac)(\_name) |
|  | Declare a C++ Hashmap statically. |
| #define | [SYS\_HASHMAP\_CXX\_DEFINE](#a10ff440e16c333ab59d3c3c2f60dedf1)(\_name) |
|  | Declare a C++ Hashmap. |

| Variables | |
| --- | --- |
| const struct [sys\_hashmap\_api](structsys__hashmap__api.md) | [sys\_hashmap\_cxx\_api](#a53cf8ff9450b396239a928d7d079297c) |

## Detailed Description

C++ Hashmap.

This is a C wrapper around std::unordered\_map. It is mainly used for benchmarking purposes.

Note
:   Enable with `CONFIG_SYS_HASH_MAP_CXX`

## Macro Definition Documentation

## [◆ ](#a10ff440e16c333ab59d3c3c2f60dedf1)SYS\_HASHMAP\_CXX\_DEFINE

| #define SYS\_HASHMAP\_CXX\_DEFINE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[SYS\_HASHMAP\_CXX\_DEFINE\_ADVANCED](#ad528dfdf1ce8accb00db14b19cd56283)( \

\_name, [sys\_hash32](group__hash__functions.md#gadd3f6fd78ce2c0bf10e1c82a9c50f39d), [SYS\_HASHMAP\_DEFAULT\_ALLOCATOR](group__hashmap__apis.md#gadcb3c72b93993222ebfe8a5e58389308), \

[SYS\_HASHMAP\_CONFIG](group__hashmap__apis.md#ga9cabdd6d7577372220065db79983f006)([SIZE\_MAX](stdint_8h.md#a3c75bb398badb69c7577b21486f9963f), [SYS\_HASHMAP\_DEFAULT\_LOAD\_FACTOR](group__hashmap__apis.md#ga2f1e3b37ac9eb4c939883b1696c87b86)))

[sys\_hash32](group__hash__functions.md#gadd3f6fd78ce2c0bf10e1c82a9c50f39d)

static uint32\_t sys\_hash32(const void \*str, size\_t n)

System default 32-bit hash function.

**Definition** hash\_function.h:119

[SYS\_HASHMAP\_DEFAULT\_LOAD\_FACTOR](group__hashmap__apis.md#ga2f1e3b37ac9eb4c939883b1696c87b86)

#define SYS\_HASHMAP\_DEFAULT\_LOAD\_FACTOR

The default Hashmap load factor (in hundredths).

**Definition** hash\_map.h:122

[SYS\_HASHMAP\_CONFIG](group__hashmap__apis.md#ga9cabdd6d7577372220065db79983f006)

#define SYS\_HASHMAP\_CONFIG(\_max\_size, \_load\_factor)

Initializer for sys\_hashmap\_config.

**Definition** hash\_map\_api.h:214

[SYS\_HASHMAP\_DEFAULT\_ALLOCATOR](group__hashmap__apis.md#gadcb3c72b93993222ebfe8a5e58389308)

#define SYS\_HASHMAP\_DEFAULT\_ALLOCATOR

The default Hashmap allocator.

**Definition** hash\_map.h:119

[SYS\_HASHMAP\_CXX\_DEFINE\_ADVANCED](#ad528dfdf1ce8accb00db14b19cd56283)

#define SYS\_HASHMAP\_CXX\_DEFINE\_ADVANCED(\_name, \_hash\_func, \_alloc\_func,...)

Declare a C++ Hashmap (advanced).

**Definition** hash\_map\_cxx.h:43

[SIZE\_MAX](stdint_8h.md#a3c75bb398badb69c7577b21486f9963f)

#define SIZE\_MAX

**Definition** stdint.h:70

Declare a C++ Hashmap.

Declare a C++ Hashmap with default parameters.

Parameters
:   | \_name | Name of the Hashmap. |
    | --- | --- |

## [◆ ](#ad528dfdf1ce8accb00db14b19cd56283)SYS\_HASHMAP\_CXX\_DEFINE\_ADVANCED

| #define SYS\_HASHMAP\_CXX\_DEFINE\_ADVANCED | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_hash\_func*, |
|  |  |  | *\_alloc\_func*, |
|  |  |  | ... ) |

**Value:**

[SYS\_HASHMAP\_DEFINE\_ADVANCED](group__hashmap__apis.md#gab21c79f226ca02c0225014c77f5b53d6)(\_name, &[sys\_hashmap\_cxx\_api](#a53cf8ff9450b396239a928d7d079297c), [sys\_hashmap\_config](structsys__hashmap__config.md), \

[sys\_hashmap\_data](structsys__hashmap__data.md), \_hash\_func, \_alloc\_func, \_\_VA\_ARGS\_\_)

[SYS\_HASHMAP\_DEFINE\_ADVANCED](group__hashmap__apis.md#gab21c79f226ca02c0225014c77f5b53d6)

#define SYS\_HASHMAP\_DEFINE\_ADVANCED(\_name, \_api, \_config\_type, \_data\_type, \_hash\_func, \_alloc\_func,...)

Declare a Hashmap (advanced).

**Definition** hash\_map.h:47

[sys\_hashmap\_cxx\_api](#a53cf8ff9450b396239a928d7d079297c)

const struct sys\_hashmap\_api sys\_hashmap\_cxx\_api

[sys\_hashmap\_config](structsys__hashmap__config.md)

Generic Hashmap configuration.

**Definition** hash\_map\_api.h:197

[sys\_hashmap\_data](structsys__hashmap__data.md)

Generic Hashmap data.

**Definition** hash\_map\_api.h:225

Declare a C++ Hashmap (advanced).

Declare a C++ Hashmap with control over advanced parameters.

Note
:   The allocator `_alloc` is used for allocating internal Hashmap entries and does not interact with any user-provided keys or values.

Parameters
:   | \_name | Name of the Hashmap. |
    | --- | --- |
    | \_hash\_func | Hash function pointer of type [sys\_hash\_func32\_t](group__hash__functions.md#ga2566ca73d30b47ae66659e26fc985fad "sys_hash_func32_t"). |
    | \_alloc\_func | Allocator function pointer of type [sys\_hashmap\_allocator\_t](group__hashmap__apis.md#ga813a4f65e3672651ef37c06dccdcfebc "sys_hashmap_allocator_t"). |
    | ... | Variant-specific details for [sys\_hashmap\_config](structsys__hashmap__config.md "sys_hashmap_config"). |

## [◆ ](#aa45fa7446daaee2ad7cf90e14c6a60ac)SYS\_HASHMAP\_CXX\_DEFINE\_STATIC

| #define SYS\_HASHMAP\_CXX\_DEFINE\_STATIC | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[SYS\_HASHMAP\_CXX\_DEFINE\_STATIC\_ADVANCED](#ad675ea9b18e4183170e0e7ae6ad5bc96)( \

\_name, [sys\_hash32](group__hash__functions.md#gadd3f6fd78ce2c0bf10e1c82a9c50f39d), [SYS\_HASHMAP\_DEFAULT\_ALLOCATOR](group__hashmap__apis.md#gadcb3c72b93993222ebfe8a5e58389308), \

[SYS\_HASHMAP\_CONFIG](group__hashmap__apis.md#ga9cabdd6d7577372220065db79983f006)([SIZE\_MAX](stdint_8h.md#a3c75bb398badb69c7577b21486f9963f), [SYS\_HASHMAP\_DEFAULT\_LOAD\_FACTOR](group__hashmap__apis.md#ga2f1e3b37ac9eb4c939883b1696c87b86)))

[SYS\_HASHMAP\_CXX\_DEFINE\_STATIC\_ADVANCED](#ad675ea9b18e4183170e0e7ae6ad5bc96)

#define SYS\_HASHMAP\_CXX\_DEFINE\_STATIC\_ADVANCED(\_name, \_hash\_func, \_alloc\_func,...)

Declare a C++ Hashmap (advanced).

**Definition** hash\_map\_cxx.h:60

Declare a C++ Hashmap statically.

Declare a C++ Hashmap statically with default parameters.

Parameters
:   | \_name | Name of the Hashmap. |
    | --- | --- |

## [◆ ](#ad675ea9b18e4183170e0e7ae6ad5bc96)SYS\_HASHMAP\_CXX\_DEFINE\_STATIC\_ADVANCED

| #define SYS\_HASHMAP\_CXX\_DEFINE\_STATIC\_ADVANCED | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_hash\_func*, |
|  |  |  | *\_alloc\_func*, |
|  |  |  | ... ) |

**Value:**

[SYS\_HASHMAP\_DEFINE\_STATIC\_ADVANCED](group__hashmap__apis.md#gacd16dd5377fe160a2154053ba20fcbd7)(\_name, &[sys\_hashmap\_cxx\_api](#a53cf8ff9450b396239a928d7d079297c), [sys\_hashmap\_config](structsys__hashmap__config.md), \

[sys\_hashmap\_data](structsys__hashmap__data.md), \_hash\_func, \_alloc\_func, \_\_VA\_ARGS\_\_)

[SYS\_HASHMAP\_DEFINE\_STATIC\_ADVANCED](group__hashmap__apis.md#gacd16dd5377fe160a2154053ba20fcbd7)

#define SYS\_HASHMAP\_DEFINE\_STATIC\_ADVANCED(\_name, \_api, \_config\_type, \_data\_type, \_hash\_func, \_alloc\_func,...)

Declare a Hashmap statically (advanced).

**Definition** hash\_map.h:75

Declare a C++ Hashmap (advanced).

Declare a C++ Hashmap with control over advanced parameters.

Note
:   The allocator `_alloc` is used for allocating internal Hashmap entries and does not interact with any user-provided keys or values.

Parameters
:   | \_name | Name of the Hashmap. |
    | --- | --- |
    | \_hash\_func | Hash function pointer of type [sys\_hash\_func32\_t](group__hash__functions.md#ga2566ca73d30b47ae66659e26fc985fad "sys_hash_func32_t"). |
    | \_alloc\_func | Allocator function pointer of type [sys\_hashmap\_allocator\_t](group__hashmap__apis.md#ga813a4f65e3672651ef37c06dccdcfebc "sys_hashmap_allocator_t"). |
    | ... | Details for [sys\_hashmap\_config](structsys__hashmap__config.md "sys_hashmap_config"). |

## Variable Documentation

## [◆ ](#a53cf8ff9450b396239a928d7d079297c)sys\_hashmap\_cxx\_api

| | const struct [sys\_hashmap\_api](structsys__hashmap__api.md) sys\_hashmap\_cxx\_api | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [hash\_map\_cxx.h](hash__map__cxx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
