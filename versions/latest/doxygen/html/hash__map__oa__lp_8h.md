---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/hash__map__oa__lp_8h.html
original_path: doxygen/html/hash__map__oa__lp_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hash\_map\_oa\_lp.h File Reference

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [Hashmap](group__hashmap__apis.md) » [Hashmap Implementations](group__hashmap__implementations.md)

Open-Addressing / Linear Probe Hashmap Implementation.
[More...](#details)

`#include <stddef.h>`  
`#include <[zephyr/sys/hash_function.h](hash__function_8h_source.md)>`  
`#include <[zephyr/sys/hash_map_api.h](hash__map__api_8h_source.md)>`

[Go to the source code of this file.](hash__map__oa__lp_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sys\_hashmap\_oa\_lp\_data](structsys__hashmap__oa__lp__data.md) |

| Macros | |
| --- | --- |
| #define | [SYS\_HASHMAP\_OA\_LP\_DEFINE\_ADVANCED](#aa9287e614c6ea567ae022be887c730fc)(\_name, \_hash\_func, \_alloc\_func, ...) |
|  | Declare a Open Addressing Linear Probe Hashmap (advanced). |
| #define | [SYS\_HASHMAP\_OA\_LP\_DEFINE\_STATIC\_ADVANCED](#a6ad7aa3485e69dcb0a204276aae74128)(\_name, \_hash\_func, \_alloc\_func, ...) |
|  | Declare a Open Addressing Linear Probe Hashmap (advanced). |
| #define | [SYS\_HASHMAP\_OA\_LP\_DEFINE\_STATIC](#a19cd65566823c760ee3961214992952b)(\_name) |
|  | Declare a Open Addressing Linear Probe Hashmap statically. |
| #define | [SYS\_HASHMAP\_OA\_LP\_DEFINE](#a591f4c0f17011fbec639ecd5a61a9c07)(\_name) |
|  | Declare a Open Addressing Linear Probe Hashmap. |

| Variables | |
| --- | --- |
| const struct [sys\_hashmap\_api](structsys__hashmap__api.md) | [sys\_hashmap\_oa\_lp\_api](#ab4383b628d3da139a3bf276eefde82f9) |

## Detailed Description

Open-Addressing / Linear Probe Hashmap Implementation.

Note
:   Enable with `CONFIG_SYS_HASH_MAP_OA_LP`

## Macro Definition Documentation

## [◆ ](#a591f4c0f17011fbec639ecd5a61a9c07)SYS\_HASHMAP\_OA\_LP\_DEFINE

| #define SYS\_HASHMAP\_OA\_LP\_DEFINE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[SYS\_HASHMAP\_OA\_LP\_DEFINE\_ADVANCED](#aa9287e614c6ea567ae022be887c730fc)( \

\_name, [sys\_hash32](group__hash__functions.md#gadd3f6fd78ce2c0bf10e1c82a9c50f39d), [SYS\_HASHMAP\_DEFAULT\_ALLOCATOR](group__hashmap__apis.md#gadcb3c72b93993222ebfe8a5e58389308), \

[SYS\_HASHMAP\_CONFIG](group__hashmap__apis.md#ga9cabdd6d7577372220065db79983f006)([SIZE\_MAX](stdint_8h.md#a3c75bb398badb69c7577b21486f9963f), [SYS\_HASHMAP\_DEFAULT\_LOAD\_FACTOR](group__hashmap__apis.md#ga2f1e3b37ac9eb4c939883b1696c87b86)))

[sys\_hash32](group__hash__functions.md#gadd3f6fd78ce2c0bf10e1c82a9c50f39d)

static uint32\_t sys\_hash32(const void \*str, size\_t n)

System default 32-bit hash function.

**Definition** hash\_function.h:119

[SYS\_HASHMAP\_DEFAULT\_LOAD\_FACTOR](group__hashmap__apis.md#ga2f1e3b37ac9eb4c939883b1696c87b86)

#define SYS\_HASHMAP\_DEFAULT\_LOAD\_FACTOR

The default Hashmap load factor (in hundredths).

**Definition** hash\_map.h:121

[SYS\_HASHMAP\_CONFIG](group__hashmap__apis.md#ga9cabdd6d7577372220065db79983f006)

#define SYS\_HASHMAP\_CONFIG(\_max\_size, \_load\_factor)

Initializer for sys\_hashmap\_config.

**Definition** hash\_map\_api.h:214

[SYS\_HASHMAP\_DEFAULT\_ALLOCATOR](group__hashmap__apis.md#gadcb3c72b93993222ebfe8a5e58389308)

#define SYS\_HASHMAP\_DEFAULT\_ALLOCATOR

The default Hashmap allocator.

**Definition** hash\_map.h:118

[SYS\_HASHMAP\_OA\_LP\_DEFINE\_ADVANCED](#aa9287e614c6ea567ae022be887c730fc)

#define SYS\_HASHMAP\_OA\_LP\_DEFINE\_ADVANCED(\_name, \_hash\_func, \_alloc\_func,...)

Declare a Open Addressing Linear Probe Hashmap (advanced).

**Definition** hash\_map\_oa\_lp.h:47

[SIZE\_MAX](stdint_8h.md#a3c75bb398badb69c7577b21486f9963f)

#define SIZE\_MAX

**Definition** stdint.h:70

Declare a Open Addressing Linear Probe Hashmap.

Declare a Open Addressing Linear Probe Hashmap with default parameters.

Parameters
:   | \_name | Name of the Hashmap. |
    | --- | --- |

## [◆ ](#aa9287e614c6ea567ae022be887c730fc)SYS\_HASHMAP\_OA\_LP\_DEFINE\_ADVANCED

| #define SYS\_HASHMAP\_OA\_LP\_DEFINE\_ADVANCED | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_hash\_func*, |
|  |  |  | *\_alloc\_func*, |
|  |  |  | ... ) |

**Value:**

[SYS\_HASHMAP\_DEFINE\_ADVANCED](group__hashmap__apis.md#gab21c79f226ca02c0225014c77f5b53d6)(\_name, &[sys\_hashmap\_oa\_lp\_api](#ab4383b628d3da139a3bf276eefde82f9), [sys\_hashmap\_config](structsys__hashmap__config.md), \

[sys\_hashmap\_oa\_lp\_data](structsys__hashmap__oa__lp__data.md), \_hash\_func, \_alloc\_func, \_\_VA\_ARGS\_\_)

[SYS\_HASHMAP\_DEFINE\_ADVANCED](group__hashmap__apis.md#gab21c79f226ca02c0225014c77f5b53d6)

#define SYS\_HASHMAP\_DEFINE\_ADVANCED(\_name, \_api, \_config\_type, \_data\_type, \_hash\_func, \_alloc\_func,...)

Declare a Hashmap (advanced).

**Definition** hash\_map.h:46

[sys\_hashmap\_oa\_lp\_api](#ab4383b628d3da139a3bf276eefde82f9)

const struct sys\_hashmap\_api sys\_hashmap\_oa\_lp\_api

[sys\_hashmap\_config](structsys__hashmap__config.md)

Generic Hashmap configuration.

**Definition** hash\_map\_api.h:197

[sys\_hashmap\_oa\_lp\_data](structsys__hashmap__oa__lp__data.md)

**Definition** hash\_map\_oa\_lp.h:27

Declare a Open Addressing Linear Probe Hashmap (advanced).

Declare a Open Addressing Linear Probe Hashmap with control over advanced parameters.

Note
:   The allocator `_alloc` is used for allocating internal Hashmap entries and does not interact with any user-provided keys or values.

Parameters
:   | \_name | Name of the Hashmap. |
    | --- | --- |
    | \_hash\_func | Hash function pointer of type [sys\_hash\_func32\_t](group__hash__functions.md#ga2566ca73d30b47ae66659e26fc985fad "sys_hash_func32_t"). |
    | \_alloc\_func | Allocator function pointer of type [sys\_hashmap\_allocator\_t](group__hashmap__apis.md#ga813a4f65e3672651ef37c06dccdcfebc "sys_hashmap_allocator_t"). |
    | ... | Variant-specific details for [sys\_hashmap\_config](structsys__hashmap__config.md "sys_hashmap_config"). |

## [◆ ](#a19cd65566823c760ee3961214992952b)SYS\_HASHMAP\_OA\_LP\_DEFINE\_STATIC

| #define SYS\_HASHMAP\_OA\_LP\_DEFINE\_STATIC | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[SYS\_HASHMAP\_OA\_LP\_DEFINE\_STATIC\_ADVANCED](#a6ad7aa3485e69dcb0a204276aae74128)( \

\_name, [sys\_hash32](group__hash__functions.md#gadd3f6fd78ce2c0bf10e1c82a9c50f39d), [SYS\_HASHMAP\_DEFAULT\_ALLOCATOR](group__hashmap__apis.md#gadcb3c72b93993222ebfe8a5e58389308), \

[SYS\_HASHMAP\_CONFIG](group__hashmap__apis.md#ga9cabdd6d7577372220065db79983f006)([SIZE\_MAX](stdint_8h.md#a3c75bb398badb69c7577b21486f9963f), [SYS\_HASHMAP\_DEFAULT\_LOAD\_FACTOR](group__hashmap__apis.md#ga2f1e3b37ac9eb4c939883b1696c87b86)))

[SYS\_HASHMAP\_OA\_LP\_DEFINE\_STATIC\_ADVANCED](#a6ad7aa3485e69dcb0a204276aae74128)

#define SYS\_HASHMAP\_OA\_LP\_DEFINE\_STATIC\_ADVANCED(\_name, \_hash\_func, \_alloc\_func,...)

Declare a Open Addressing Linear Probe Hashmap (advanced).

**Definition** hash\_map\_oa\_lp.h:64

Declare a Open Addressing Linear Probe Hashmap statically.

Declare a Open Addressing Linear Probe Hashmap statically with default parameters.

Parameters
:   | \_name | Name of the Hashmap. |
    | --- | --- |

## [◆ ](#a6ad7aa3485e69dcb0a204276aae74128)SYS\_HASHMAP\_OA\_LP\_DEFINE\_STATIC\_ADVANCED

| #define SYS\_HASHMAP\_OA\_LP\_DEFINE\_STATIC\_ADVANCED | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_hash\_func*, |
|  |  |  | *\_alloc\_func*, |
|  |  |  | ... ) |

**Value:**

[SYS\_HASHMAP\_DEFINE\_STATIC\_ADVANCED](group__hashmap__apis.md#gacd16dd5377fe160a2154053ba20fcbd7)(\_name, &[sys\_hashmap\_oa\_lp\_api](#ab4383b628d3da139a3bf276eefde82f9), [sys\_hashmap\_config](structsys__hashmap__config.md), \

[sys\_hashmap\_oa\_lp\_data](structsys__hashmap__oa__lp__data.md), \_hash\_func, \_alloc\_func, \

\_\_VA\_ARGS\_\_)

[SYS\_HASHMAP\_DEFINE\_STATIC\_ADVANCED](group__hashmap__apis.md#gacd16dd5377fe160a2154053ba20fcbd7)

#define SYS\_HASHMAP\_DEFINE\_STATIC\_ADVANCED(\_name, \_api, \_config\_type, \_data\_type, \_hash\_func, \_alloc\_func,...)

Declare a Hashmap statically (advanced).

**Definition** hash\_map.h:74

Declare a Open Addressing Linear Probe Hashmap (advanced).

Declare a Open Addressing Linear Probe Hashmap with control over advanced parameters.

Note
:   The allocator `_alloc` is used for allocating internal Hashmap entries and does not interact with any user-provided keys or values.

Parameters
:   | \_name | Name of the Hashmap. |
    | --- | --- |
    | \_hash\_func | Hash function pointer of type [sys\_hash\_func32\_t](group__hash__functions.md#ga2566ca73d30b47ae66659e26fc985fad "sys_hash_func32_t"). |
    | \_alloc\_func | Allocator function pointer of type [sys\_hashmap\_allocator\_t](group__hashmap__apis.md#ga813a4f65e3672651ef37c06dccdcfebc "sys_hashmap_allocator_t"). |
    | ... | Details for [sys\_hashmap\_config](structsys__hashmap__config.md "sys_hashmap_config"). |

## Variable Documentation

## [◆ ](#ab4383b628d3da139a3bf276eefde82f9)sys\_hashmap\_oa\_lp\_api

| | const struct [sys\_hashmap\_api](structsys__hashmap__api.md) sys\_hashmap\_oa\_lp\_api | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [hash\_map\_oa\_lp.h](hash__map__oa__lp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
