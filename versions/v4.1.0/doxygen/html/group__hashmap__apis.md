---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__hashmap__apis.html
original_path: doxygen/html/group__hashmap__apis.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Hashmap

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md)

Hashmap (Hash Table) API.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Hash Functions](group__hash__functions.md) |
|  | [Hashmap Implementations](group__hashmap__implementations.md) |

| Data Structures | |
| --- | --- |
| struct | [sys\_hashmap](structsys__hashmap.md) |
|  | Generic Hashmap. [More...](structsys__hashmap.md#details) |
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
| #define | [SYS\_HASHMAP\_DEFINE\_ADVANCED](#gab21c79f226ca02c0225014c77f5b53d6)(\_name, \_api, \_config\_type, \_data\_type, \_hash\_func, \_alloc\_func, ...) |
|  | Declare a Hashmap (advanced). |
| #define | [SYS\_HASHMAP\_DEFINE\_STATIC\_ADVANCED](#gacd16dd5377fe160a2154053ba20fcbd7)(\_name, \_api, \_config\_type, \_data\_type, \_hash\_func, \_alloc\_func, ...) |
|  | Declare a Hashmap statically (advanced). |
| #define | [SYS\_HASHMAP\_DEFINE](#ga2d2eb11eccb9a9040a1b5e0b6529d500)(\_name) |
|  | Declare a Hashmap. |
| #define | [SYS\_HASHMAP\_DEFINE\_STATIC](#ga5e653d2dad44c32b42dfd15107f6ba3c)(\_name) |
|  | Declare a Hashmap statically. |
| #define | [SYS\_HASHMAP\_DEFAULT\_ALLOCATOR](#gadcb3c72b93993222ebfe8a5e58389308)   [sys\_hashmap\_default\_allocator](#gad24a1d4e49b9ce811e1a5770480d00bd) |
|  | The default Hashmap allocator. |
| #define | [SYS\_HASHMAP\_DEFAULT\_LOAD\_FACTOR](#ga2f1e3b37ac9eb4c939883b1696c87b86)   75 |
|  | The default Hashmap load factor (in hundredths). |
| #define | [SYS\_HASHMAP\_CONFIG](#ga9cabdd6d7577372220065db79983f006)(\_max\_size, \_load\_factor) |
|  | Initializer for `[sys_hashmap_config](structsys__hashmap__config.md "Generic Hashmap configuration.")`. |

| Typedefs | |
| --- | --- |
| typedef void \*(\* | [sys\_hashmap\_allocator\_t](#ga813a4f65e3672651ef37c06dccdcfebc)) (void \*ptr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) new\_size) |
|  | Allocator interface for [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |
| typedef void(\* | [sys\_hashmap\_iterator\_t](#gaffc18fa6c36de71c94a836dff30f4dba)) (const struct [sys\_hashmap](structsys__hashmap.md) \*map, struct [sys\_hashmap\_iterator](structsys__hashmap__iterator.md) \*it) |
|  | In-place iterator constructor for [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |
| typedef void(\* | [sys\_hashmap\_callback\_t](#ga6e813ebb133febdcac0bd2e6b552a0d1)) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) key, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value, void \*cookie) |
|  | Callback interface for [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |
| typedef void(\* | [sys\_hashmap\_clear\_t](#gac5c7ec25ad44115e83cda666d8175c79)) (struct [sys\_hashmap](structsys__hashmap.md) \*map, [sys\_hashmap\_callback\_t](#ga6e813ebb133febdcac0bd2e6b552a0d1) cb, void \*cookie) |
|  | Clear all entries contained in a [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |
| typedef int(\* | [sys\_hashmap\_insert\_t](#gacbd944beac0fd5377a19c662f444b50b)) (struct [sys\_hashmap](structsys__hashmap.md) \*map, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) key, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*old\_value) |
|  | Insert a new entry into a [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [sys\_hashmap\_remove\_t](#ga8ee3886c08a1e0635db3a43858f76055)) (struct [sys\_hashmap](structsys__hashmap.md) \*map, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) key, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value) |
|  | Remove an entry from a [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [sys\_hashmap\_get\_t](#gab24ce66e67e900d24c6fe3dde10a6cac)) (const struct [sys\_hashmap](structsys__hashmap.md) \*map, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) key, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value) |
|  | Get a value from a [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |

| Functions | |
| --- | --- |
| static void \* | [sys\_hashmap\_default\_allocator](#gad24a1d4e49b9ce811e1a5770480d00bd) (void \*ptr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
| static void | [sys\_hashmap\_foreach](#gadee4fa23549a92afbe89a71125a859cd) (const struct [sys\_hashmap](structsys__hashmap.md) \*map, [sys\_hashmap\_callback\_t](#ga6e813ebb133febdcac0bd2e6b552a0d1) cb, void \*cookie) |
|  | Iterate over all values contained in a [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |
| static void | [sys\_hashmap\_clear](#gad859ec4ac776c876874bb3a88071a8aa) (struct [sys\_hashmap](structsys__hashmap.md) \*map, [sys\_hashmap\_callback\_t](#ga6e813ebb133febdcac0bd2e6b552a0d1) cb, void \*cookie) |
|  | Clear all entries contained in a [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |
| static int | [sys\_hashmap\_insert](#ga4868b88473fe8d160ec77bce495165cf) (struct [sys\_hashmap](structsys__hashmap.md) \*map, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) key, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*old\_value) |
|  | Insert a new entry into a [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_hashmap\_remove](#ga45db255d4a6108f8da789eda01184c0b) (struct [sys\_hashmap](structsys__hashmap.md) \*map, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) key, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value) |
|  | Remove an entry from a [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_hashmap\_get](#ga51125854595615092330070f380cb231) (const struct [sys\_hashmap](structsys__hashmap.md) \*map, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) key, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value) |
|  | Get a value from a [sys\_hashmap](structsys__hashmap.md "sys_hashmap"). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_hashmap\_contains\_key](#ga95e77f9fc362673a81bf287da20fcc38) (const struct [sys\_hashmap](structsys__hashmap.md) \*map, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) key) |
|  | Check if `map` contains a value associated with `key`. |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [sys\_hashmap\_size](#ga4957bc7166ed61e66002a81dcb93bffb) (const struct [sys\_hashmap](structsys__hashmap.md) \*map) |
|  | Query the number of entries contained within `map`. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_hashmap\_is\_empty](#ga5f382228a7265d2b27b9678dad442849) (const struct [sys\_hashmap](structsys__hashmap.md) \*map) |
|  | Check if `map` is empty. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sys\_hashmap\_load\_factor](#ga48e6e8e55744fe270dc158bb7f31e265) (const struct [sys\_hashmap](structsys__hashmap.md) \*map) |
|  | Query the load factor of `map`. |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [sys\_hashmap\_num\_buckets](#ga7527eff4dc4d0b1818cb7d9813f688b9) (const struct [sys\_hashmap](structsys__hashmap.md) \*map) |
|  | Query the number of buckets used in `map`. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_hashmap\_should\_rehash](#gaee95e9b7494773f717028c764513d7ad) (const struct [sys\_hashmap](structsys__hashmap.md) \*map, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) grow, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_reserved, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*new\_num\_buckets) |
|  | Decide whether the Hashmap should be resized. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_hashmap\_iterator\_has\_next](#ga15020630e76f826893c58faded3737ed) (const struct [sys\_hashmap\_iterator](structsys__hashmap__iterator.md) \*it) |
|  | Check if a Hashmap iterator has a next entry. |

## Detailed Description

Hashmap (Hash Table) API.

Hashmaps (a.k.a Hash Tables) sacrifice space for speed. All operations on a Hashmap (insert, delete, search) are O(1) complexity (on average).

## Macro Definition Documentation

## [◆ ](#ga9cabdd6d7577372220065db79983f006)SYS\_HASHMAP\_CONFIG

| #define SYS\_HASHMAP\_CONFIG | ( |  | *\_max\_size*, |
| --- | --- | --- | --- |
|  |  |  | *\_load\_factor* ) |

`#include <[hash_map_api.h](hash__map__api_8h.md)>`

**Value:**

{ \

.max\_size = ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9))\_max\_size, .load\_factor = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))\_load\_factor, \

.initial\_n\_buckets = [NHPOT](group__sys-util.md#ga2ab444fed50a82cc1fe0e952fd03127d)([DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)(100, \_load\_factor)), \

}

[NHPOT](group__sys-util.md#ga2ab444fed50a82cc1fe0e952fd03127d)

#define NHPOT(x)

Compute next highest power of two.

**Definition** util.h:729

[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)

#define DIV\_ROUND\_UP(n, d)

Divide and round up.

**Definition** util.h:352

[size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)

Size of off\_t must be equal or less than size of size\_t

**Definition** retained\_mem.h:28

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

Initializer for `[sys_hashmap_config](structsys__hashmap__config.md "Generic Hashmap configuration.")`.

This macro helps to initialize a structure of type `[sys_hashmap_config](structsys__hashmap__config.md "Generic Hashmap configuration.")`.

Parameters
:   | \_max\_size | Maximum number of entries |
    | --- | --- |
    | \_load\_factor | Maximum load factor of expressed in hundredths |

## [◆ ](#gadcb3c72b93993222ebfe8a5e58389308)SYS\_HASHMAP\_DEFAULT\_ALLOCATOR

| #define SYS\_HASHMAP\_DEFAULT\_ALLOCATOR   [sys\_hashmap\_default\_allocator](#gad24a1d4e49b9ce811e1a5770480d00bd) |
| --- |

`#include <[hash_map.h](hash__map_8h.md)>`

The default Hashmap allocator.

## [◆ ](#ga2f1e3b37ac9eb4c939883b1696c87b86)SYS\_HASHMAP\_DEFAULT\_LOAD\_FACTOR

| #define SYS\_HASHMAP\_DEFAULT\_LOAD\_FACTOR   75 |
| --- |

`#include <[hash_map.h](hash__map_8h.md)>`

The default Hashmap load factor (in hundredths).

## [◆ ](#ga2d2eb11eccb9a9040a1b5e0b6529d500)SYS\_HASHMAP\_DEFINE

| #define SYS\_HASHMAP\_DEFINE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hash_map.h](hash__map_8h.md)>`

**Value:**

SYS\_HASHMAP\_DEFAULT\_DEFINE(\_name)

Declare a Hashmap.

Declare a Hashmap with default parameters.

Parameters
:   | \_name | Name of the Hashmap. |
    | --- | --- |

## [◆ ](#gab21c79f226ca02c0225014c77f5b53d6)SYS\_HASHMAP\_DEFINE\_ADVANCED

| #define SYS\_HASHMAP\_DEFINE\_ADVANCED | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_api*, |
|  |  |  | *\_config\_type*, |
|  |  |  | *\_data\_type*, |
|  |  |  | *\_hash\_func*, |
|  |  |  | *\_alloc\_func*, |
|  |  |  | ... ) |

`#include <[hash_map.h](hash__map_8h.md)>`

**Value:**

const struct \_config\_type \_name##\_config = \_\_VA\_ARGS\_\_; \

struct \_data\_type \_name##\_data; \

struct [sys\_hashmap](structsys__hashmap.md) \_name = { \

.api = (const struct [sys\_hashmap\_api](structsys__hashmap__api.md) \*)(\_api), \

.config = (const struct [sys\_hashmap\_config](structsys__hashmap__config.md) \*)&\_name##\_config, \

.data = (struct [sys\_hashmap\_data](structsys__hashmap__data.md) \*)&\_name##\_data, \

.[hash\_func](structsys__hashmap.md#a56028566cb14b8722503e527445bbfc9) = (\_hash\_func), \

.alloc\_func = (\_alloc\_func), \

}

[sys\_hashmap\_api](structsys__hashmap__api.md)

Generic Hashmap API.

**Definition** hash\_map\_api.h:168

[sys\_hashmap\_config](structsys__hashmap__config.md)

Generic Hashmap configuration.

**Definition** hash\_map\_api.h:197

[sys\_hashmap\_data](structsys__hashmap__data.md)

Generic Hashmap data.

**Definition** hash\_map\_api.h:225

[sys\_hashmap](structsys__hashmap.md)

Generic Hashmap.

**Definition** hash\_map.h:125

[sys\_hashmap::hash\_func](structsys__hashmap.md#a56028566cb14b8722503e527445bbfc9)

sys\_hash\_func32\_t hash\_func

Hash function.

**Definition** hash\_map.h:133

Declare a Hashmap (advanced).

Declare a Hashmap with control over advanced parameters.

Note
:   The allocator `_alloc` is used for allocating internal Hashmap entries and does not interact with any user-provided keys or values.

Parameters
:   | \_name | Name of the Hashmap. |
    | --- | --- |
    | \_api | API pointer of type [sys\_hashmap\_api](structsys__hashmap__api.md "sys_hashmap_api"). |
    | \_config\_type | Variant of [sys\_hashmap\_config](structsys__hashmap__config.md "sys_hashmap_config"). |
    | \_data\_type | Variant of [sys\_hashmap\_data](structsys__hashmap__data.md "sys_hashmap_data"). |
    | \_hash\_func | Hash function pointer of type [sys\_hash\_func32\_t](group__hash__functions.md#ga2566ca73d30b47ae66659e26fc985fad "sys_hash_func32_t"). |
    | \_alloc\_func | Allocator function pointer of type [sys\_hashmap\_allocator\_t](#ga813a4f65e3672651ef37c06dccdcfebc). |
    | ... | Variant-specific details for `_config_type`. |

## [◆ ](#ga5e653d2dad44c32b42dfd15107f6ba3c)SYS\_HASHMAP\_DEFINE\_STATIC

| #define SYS\_HASHMAP\_DEFINE\_STATIC | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hash_map.h](hash__map_8h.md)>`

**Value:**

SYS\_HASHMAP\_DEFAULT\_DEFINE\_STATIC(\_name)

Declare a Hashmap statically.

Declare a Hashmap statically with default parameters.

Parameters
:   | \_name | Name of the Hashmap. |
    | --- | --- |

## [◆ ](#gacd16dd5377fe160a2154053ba20fcbd7)SYS\_HASHMAP\_DEFINE\_STATIC\_ADVANCED

| #define SYS\_HASHMAP\_DEFINE\_STATIC\_ADVANCED | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_api*, |
|  |  |  | *\_config\_type*, |
|  |  |  | *\_data\_type*, |
|  |  |  | *\_hash\_func*, |
|  |  |  | *\_alloc\_func*, |
|  |  |  | ... ) |

`#include <[hash_map.h](hash__map_8h.md)>`

**Value:**

static const struct \_config\_type \_name##\_config = \_\_VA\_ARGS\_\_; \

static struct \_data\_type \_name##\_data; \

static struct [sys\_hashmap](structsys__hashmap.md) \_name = { \

.api = (const struct [sys\_hashmap\_api](structsys__hashmap__api.md) \*)(\_api), \

.config = (const struct [sys\_hashmap\_config](structsys__hashmap__config.md) \*)&\_name##\_config, \

.data = (struct [sys\_hashmap\_data](structsys__hashmap__data.md) \*)&\_name##\_data, \

.[hash\_func](structsys__hashmap.md#a56028566cb14b8722503e527445bbfc9) = (\_hash\_func), \

.alloc\_func = (\_alloc\_func), \

}

Declare a Hashmap statically (advanced).

Declare a Hashmap statically with control over advanced parameters.

Note
:   The allocator `_alloc` is used for allocating internal Hashmap entries and does not interact with any user-provided keys or values.

Parameters
:   | \_name | Name of the Hashmap. |
    | --- | --- |
    | \_api | API pointer of type [sys\_hashmap\_api](structsys__hashmap__api.md "sys_hashmap_api"). |
    | \_config\_type | Variant of [sys\_hashmap\_config](structsys__hashmap__config.md "sys_hashmap_config"). |
    | \_data\_type | Variant of [sys\_hashmap\_data](structsys__hashmap__data.md "sys_hashmap_data"). |
    | \_hash\_func | Hash function pointer of type [sys\_hash\_func32\_t](group__hash__functions.md#ga2566ca73d30b47ae66659e26fc985fad "sys_hash_func32_t"). |
    | \_alloc\_func | Allocator function pointer of type [sys\_hashmap\_allocator\_t](#ga813a4f65e3672651ef37c06dccdcfebc). |
    | ... | Variant-specific details for `_config_type`. |

## Typedef Documentation

## [◆ ](#ga813a4f65e3672651ef37c06dccdcfebc)sys\_hashmap\_allocator\_t

| typedef void \*(\* sys\_hashmap\_allocator\_t) (void \*ptr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) new\_size) |
| --- |

`#include <[hash_map_api.h](hash__map__api_8h.md)>`

Allocator interface for [sys\_hashmap](structsys__hashmap.md "sys_hashmap").

The Hashmap allocator can be any allocator that behaves similarly to [realloc()](stdlib_8h.md#ad28fed1039f35d754710633141b4edf0) with the additional specification that the allocator behaves like [free()](stdlib_8h.md#afbedc913aa4651b3c3b4b3aecd9b4711) when `new_size` is zero.

Parameters
:   | ptr | Previously allocated memory region or [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) to make a new vallocation. |
    | --- | --- |
    | new\_size | the new size of the allocation, in bytes. |

See also
:   [realloc](https://en.cppreference.com/w/c/memory/realloc)

## [◆ ](#ga6e813ebb133febdcac0bd2e6b552a0d1)sys\_hashmap\_callback\_t

| typedef void(\* sys\_hashmap\_callback\_t) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) key, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value, void \*cookie) |
| --- |

`#include <[hash_map_api.h](hash__map__api_8h.md)>`

Callback interface for [sys\_hashmap](structsys__hashmap.md "sys_hashmap").

This callback is used by some Hashmap methods.

Parameters
:   | key | Key corresponding to `value` |
    | --- | --- |
    | value | Value corresponding to `key` |
    | cookie | User-specified variable |

## [◆ ](#gac5c7ec25ad44115e83cda666d8175c79)sys\_hashmap\_clear\_t

| typedef void(\* sys\_hashmap\_clear\_t) (struct [sys\_hashmap](structsys__hashmap.md) \*map, [sys\_hashmap\_callback\_t](#ga6e813ebb133febdcac0bd2e6b552a0d1) cb, void \*cookie) |
| --- |

`#include <[hash_map_api.h](hash__map__api_8h.md)>`

Clear all entries contained in a [sys\_hashmap](structsys__hashmap.md "sys_hashmap").

Note
:   If the values in a particular Hashmap are

Parameters
:   | map | Hashmap to clear |
    | --- | --- |
    | cb | Callback to call for each entry |
    | cookie | User-specified variable |

## [◆ ](#gab24ce66e67e900d24c6fe3dde10a6cac)sys\_hashmap\_get\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* sys\_hashmap\_get\_t) (const struct [sys\_hashmap](structsys__hashmap.md) \*map, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) key, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value) |
| --- |

`#include <[hash_map_api.h](hash__map__api_8h.md)>`

Get a value from a [sys\_hashmap](structsys__hashmap.md "sys_hashmap").

Look-up the [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1 "uint64_t") associated with `key`, if one exists.

Parameters
:   | map | Hashmap to search through |
    | --- | --- |
    | key | Key with which to search `map` |
    | value | Location to store a potential value associated with `key` or [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if `map` contains a value associated with `key`. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if `map` does not contain a value associated with `key`. |

## [◆ ](#gacbd944beac0fd5377a19c662f444b50b)sys\_hashmap\_insert\_t

| typedef int(\* sys\_hashmap\_insert\_t) (struct [sys\_hashmap](structsys__hashmap.md) \*map, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) key, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*old\_value) |
| --- |

`#include <[hash_map_api.h](hash__map__api_8h.md)>`

Insert a new entry into a [sys\_hashmap](structsys__hashmap.md "sys_hashmap").

Insert a new `key` - `value` pair into `map`.

Parameters
:   | map | Hashmap to insert into |
    | --- | --- |
    | key | Key to associate with `value` |
    | value | Value to associate with `key` |
    | old\_value | Location to store the value previously associated with `key` or [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) |

Return values
:   | 0 | if `value` was inserted for an existing key, in which case `old_value` will contain the previous value |
    | --- | --- |
    | 1 | if a new entry was inserted for the `key` - `value` pair |
    | -ENOMEM | if memory allocation failed |

## [◆ ](#gaffc18fa6c36de71c94a836dff30f4dba)sys\_hashmap\_iterator\_t

| typedef void(\* sys\_hashmap\_iterator\_t) (const struct [sys\_hashmap](structsys__hashmap.md) \*map, struct [sys\_hashmap\_iterator](structsys__hashmap__iterator.md) \*it) |
| --- |

`#include <[hash_map_api.h](hash__map__api_8h.md)>`

In-place iterator constructor for [sys\_hashmap](structsys__hashmap.md "sys_hashmap").

Construct an iterator, `it`, for `map`.

Parameters
:   | map | Hashmap to iterate over. |
    | --- | --- |
    | it | Iterator to initialize. |

## [◆ ](#ga8ee3886c08a1e0635db3a43858f76055)sys\_hashmap\_remove\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* sys\_hashmap\_remove\_t) (struct [sys\_hashmap](structsys__hashmap.md) \*map, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) key, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value) |
| --- |

`#include <[hash_map_api.h](hash__map__api_8h.md)>`

Remove an entry from a [sys\_hashmap](structsys__hashmap.md "sys_hashmap").

Erase the entry associated with key `key`, if one exists.

Parameters
:   | map | Hashmap to remove from |
    | --- | --- |
    | key | Key to remove from `map` |
    | value | Location to store a potential value associated with `key` or [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if `map` was modified as a result of this operation. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if `map` does not contain a value associated with `key`. |

## Function Documentation

## [◆ ](#gad859ec4ac776c876874bb3a88071a8aa)sys\_hashmap\_clear()

| | void sys\_hashmap\_clear | ( | struct [sys\_hashmap](structsys__hashmap.md) \* | *map*, | | --- | --- | --- | --- | |  |  | [sys\_hashmap\_callback\_t](#ga6e813ebb133febdcac0bd2e6b552a0d1) | *cb*, | |  |  | void \* | *cookie* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[hash_map.h](hash__map_8h.md)>`

Clear all entries contained in a [sys\_hashmap](structsys__hashmap.md "sys_hashmap").

Note
:   If the values in a particular Hashmap are

Parameters
:   | map | Hashmap to clear |
    | --- | --- |
    | cb | Callback to call for each entry |
    | cookie | User-specified variable |

## [◆ ](#ga95e77f9fc362673a81bf287da20fcc38)sys\_hashmap\_contains\_key()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_hashmap\_contains\_key | ( | const struct [sys\_hashmap](structsys__hashmap.md) \* | *map*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *key* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[hash_map.h](hash__map_8h.md)>`

Check if `map` contains a value associated with `key`.

Parameters
:   | map | Hashmap to search through |
    | --- | --- |
    | key | Key with which to search `map` |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if `map` contains a value associated with `key`. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if `map` does not contain a value associated with `key`. |

## [◆ ](#gad24a1d4e49b9ce811e1a5770480d00bd)sys\_hashmap\_default\_allocator()

| | void \* sys\_hashmap\_default\_allocator | ( | void \* | *ptr*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[hash_map.h](hash__map_8h.md)>`

## [◆ ](#gadee4fa23549a92afbe89a71125a859cd)sys\_hashmap\_foreach()

| | void sys\_hashmap\_foreach | ( | const struct [sys\_hashmap](structsys__hashmap.md) \* | *map*, | | --- | --- | --- | --- | |  |  | [sys\_hashmap\_callback\_t](#ga6e813ebb133febdcac0bd2e6b552a0d1) | *cb*, | |  |  | void \* | *cookie* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[hash_map.h](hash__map_8h.md)>`

Iterate over all values contained in a [sys\_hashmap](structsys__hashmap.md "sys_hashmap").

Parameters
:   | map | Hashmap to iterate over |
    | --- | --- |
    | cb | Callback to call for each entry |
    | cookie | User-specified variable |

## [◆ ](#ga51125854595615092330070f380cb231)sys\_hashmap\_get()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_hashmap\_get | ( | const struct [sys\_hashmap](structsys__hashmap.md) \* | *map*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *key*, | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[hash_map.h](hash__map_8h.md)>`

Get a value from a [sys\_hashmap](structsys__hashmap.md "sys_hashmap").

Look-up the [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1 "uint64_t") associated with `key`, if one exists.

Parameters
:   | map | Hashmap to search through |
    | --- | --- |
    | key | Key with which to search `map` |
    | value | Location to store a potential value associated with `key` or [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if `map` contains a value associated with `key`. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if `map` does not contain a value associated with `key`. |

## [◆ ](#ga4868b88473fe8d160ec77bce495165cf)sys\_hashmap\_insert()

| | int sys\_hashmap\_insert | ( | struct [sys\_hashmap](structsys__hashmap.md) \* | *map*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *key*, | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *value*, | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *old\_value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[hash_map.h](hash__map_8h.md)>`

Insert a new entry into a [sys\_hashmap](structsys__hashmap.md "sys_hashmap").

Insert a new `key` - `value` pair into `map`.

Parameters
:   | map | Hashmap to insert into |
    | --- | --- |
    | key | Key to associate with `value` |
    | value | Value to associate with `key` |
    | old\_value | Location to store the value previously associated with `key` or [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) |

Return values
:   | 0 | if `value` was inserted for an existing key, in which case `old_value` will contain the previous value |
    | --- | --- |
    | 1 | if a new entry was inserted for the `key` - `value` pair |
    | -ENOMEM | if memory allocation failed |
    | -ENOSPC | if the size limit has been reached |

## [◆ ](#ga5f382228a7265d2b27b9678dad442849)sys\_hashmap\_is\_empty()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_hashmap\_is\_empty | ( | const struct [sys\_hashmap](structsys__hashmap.md) \* | *map* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[hash_map.h](hash__map_8h.md)>`

Check if `map` is empty.

Parameters
:   | map | Hashmap to query |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if `map` is empty. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if `map` is not empty. |

## [◆ ](#ga15020630e76f826893c58faded3737ed)sys\_hashmap\_iterator\_has\_next()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_hashmap\_iterator\_has\_next | ( | const struct [sys\_hashmap\_iterator](structsys__hashmap__iterator.md) \* | *it* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[hash_map_api.h](hash__map__api_8h.md)>`

Check if a Hashmap iterator has a next entry.

Parameters
:   | it | Hashmap iterator |
    | --- | --- |

Returns
:   true if there is a next entry
:   false if there is no next entry

## [◆ ](#ga48e6e8e55744fe270dc158bb7f31e265)sys\_hashmap\_load\_factor()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sys\_hashmap\_load\_factor | ( | const struct [sys\_hashmap](structsys__hashmap.md) \* | *map* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[hash_map.h](hash__map_8h.md)>`

Query the load factor of `map`.

Note
:   To convert the load factor to a floating-point value use sys\_hash\_load\_factor(map) / 100.0f.

Parameters
:   | map | Hashmap to query |
    | --- | --- |

Returns
:   Load factor of `map` expressed in hundredths.

## [◆ ](#ga7527eff4dc4d0b1818cb7d9813f688b9)sys\_hashmap\_num\_buckets()

| | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sys\_hashmap\_num\_buckets | ( | const struct [sys\_hashmap](structsys__hashmap.md) \* | *map* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[hash_map.h](hash__map_8h.md)>`

Query the number of buckets used in `map`.

Parameters
:   | map | Hashmap to query |
    | --- | --- |

Returns
:   Number of buckets used in `map`

## [◆ ](#ga45db255d4a6108f8da789eda01184c0b)sys\_hashmap\_remove()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_hashmap\_remove | ( | struct [sys\_hashmap](structsys__hashmap.md) \* | *map*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *key*, | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[hash_map.h](hash__map_8h.md)>`

Remove an entry from a [sys\_hashmap](structsys__hashmap.md "sys_hashmap").

Erase the entry associated with key `key`, if one exists.

Parameters
:   | map | Hashmap to remove from |
    | --- | --- |
    | key | Key to remove from `map` |
    | value | Location to store a potential value associated with `key` or [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if `map` was modified as a result of this operation. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if `map` does not contain a value associated with `key`. |

## [◆ ](#gaee95e9b7494773f717028c764513d7ad)sys\_hashmap\_should\_rehash()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_hashmap\_should\_rehash | ( | const struct [sys\_hashmap](structsys__hashmap.md) \* | *map*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *grow*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_reserved*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *new\_num\_buckets* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[hash_map.h](hash__map_8h.md)>`

Decide whether the Hashmap should be resized.

This is a simple opportunistic method that implementations can choose to use. It will grow and shrink the Hashmap by a factor of 2 when insertion / removal would exceed / fall into the specified load factor.

Note
:   Users should call this prior to inserting a new key-value pair and after removing a key-value pair.
:   The number of reserved entries is implementation-defined, but it is only considered as part of the load factor when growing the hash table.

Parameters
:   |  | map | Hashmap to examine |
    | --- | --- | --- |
    |  | grow | true if an entry is to be added. false if an entry has been removed |
    |  | num\_reserved | the number of reserved entries |
    | [out] | new\_num\_buckets | variable Hashmap size |

Returns
:   true if the Hashmap should be rehashed
:   false if the Hashmap should not be rehashed

## [◆ ](#ga4957bc7166ed61e66002a81dcb93bffb)sys\_hashmap\_size()

| | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sys\_hashmap\_size | ( | const struct [sys\_hashmap](structsys__hashmap.md) \* | *map* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[hash_map.h](hash__map_8h.md)>`

Query the number of entries contained within `map`.

Parameters
:   | map | Hashmap to search through |
    | --- | --- |

Returns
:   the number of entries contained within `map`.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
