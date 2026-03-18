---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__shared__multi__heap.html
original_path: doxygen/html/group__shared__multi__heap.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Shared multi-heap interface

[Operating System Services](group__os__services.md) » [Heap Management](group__heaps.md)

Shared Multi-Heap (SMH) interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [shared\_multi\_heap\_region](structshared__multi__heap__region.md) |
|  | SMH region struct. [More...](structshared__multi__heap__region.md#details) |

| Macros | |
| --- | --- |
| #define | [MAX\_SHARED\_MULTI\_HEAP\_ATTR](#gae582ce2dfaaf9554d43aab717c85c17c)   [SMH\_REG\_ATTR\_NUM](#gga11861c5c373f9e5d81496ae1be7df1d4a0a41317e94fcdf459708be4a78b74c91) |
|  | Maximum number of standard attributes. |

| Enumerations | |
| --- | --- |
| enum | [shared\_multi\_heap\_attr](#ga11861c5c373f9e5d81496ae1be7df1d4) { [SMH\_REG\_ATTR\_CACHEABLE](#gga11861c5c373f9e5d81496ae1be7df1d4afb2e0bb04859ff231dee953279b8bf3a) , [SMH\_REG\_ATTR\_NON\_CACHEABLE](#gga11861c5c373f9e5d81496ae1be7df1d4a2625b9b8aea429ab748f9e39d55f0dff) , [SMH\_REG\_ATTR\_NUM](#gga11861c5c373f9e5d81496ae1be7df1d4a0a41317e94fcdf459708be4a78b74c91) } |
|  | SMH region attributes enumeration type. [More...](#ga11861c5c373f9e5d81496ae1be7df1d4) |

| Functions | |
| --- | --- |
| int | [shared\_multi\_heap\_pool\_init](#ga5b7f09666e3eac051b4c4942572f9ca3) (void) |
|  | Init the pool. |
| void \* | [shared\_multi\_heap\_alloc](#ga8cd3d321f5ae516cd55812d304289971) (enum [shared\_multi\_heap\_attr](#ga11861c5c373f9e5d81496ae1be7df1d4) attr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Allocate memory from the memory shared multi-heap pool. |
| void \* | [shared\_multi\_heap\_aligned\_alloc](#ga328b199253da06ed724e9b0157167ede) (enum [shared\_multi\_heap\_attr](#ga11861c5c373f9e5d81496ae1be7df1d4) attr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Allocate aligned memory from the memory shared multi-heap pool. |
| void | [shared\_multi\_heap\_free](#gab968bf26483d22939aaa7c2b1b6743ad) (void \*block) |
|  | Free memory from the shared multi-heap pool. |
| int | [shared\_multi\_heap\_add](#ga086362a2a8fce827a246039ef8757cc5) (struct [shared\_multi\_heap\_region](structshared__multi__heap__region.md) \*region, void \*user\_data) |
|  | Add an heap region to the shared multi-heap pool. |

## Detailed Description

Shared Multi-Heap (SMH) interface.

The shared multi-heap manager uses the multi-heap allocator to manage a set of memory regions with different capabilities / attributes (cacheable, non-cacheable, etc...).

All the different regions can be added at run-time to the shared multi-heap pool providing an opaque "attribute" value (an integer or enum value) that can be used by drivers or applications to request memory with certain capabilities.

This framework is commonly used as follow:

- At boot time some platform code initialize the shared multi-heap framework using [shared\_multi\_heap\_pool\_init](#ga5b7f09666e3eac051b4c4942572f9ca3) and add the memory regions to the pool with [shared\_multi\_heap\_add](#ga086362a2a8fce827a246039ef8757cc5), possibly gathering the needed information for the regions from the DT.
- Each memory region encoded in a [shared\_multi\_heap\_region](structshared__multi__heap__region.md "shared_multi_heap_region") structure. This structure is also carrying an opaque and user-defined integer value that is used to define the region capabilities (for example: cacheability, cpu affinity, etc...)
- When a driver or application needs some dynamic memory with a certain capability, it can use [shared\_multi\_heap\_alloc](#ga8cd3d321f5ae516cd55812d304289971) (or the aligned version) to request the memory by using the opaque parameter to select the correct set of attributes for the needed memory. The framework will take care of selecting the correct heap (thus memory region) to carve memory from, based on the opaque parameter and the runtime state of the heaps (available memory, heap state, etc...)

## Macro Definition Documentation

## [◆ ](#gae582ce2dfaaf9554d43aab717c85c17c)MAX\_SHARED\_MULTI\_HEAP\_ATTR

| #define MAX\_SHARED\_MULTI\_HEAP\_ATTR   [SMH\_REG\_ATTR\_NUM](#gga11861c5c373f9e5d81496ae1be7df1d4a0a41317e94fcdf459708be4a78b74c91) |
| --- |

`#include <[shared_multi_heap.h](shared__multi__heap_8h.md)>`

Maximum number of standard attributes.

## Enumeration Type Documentation

## [◆ ](#ga11861c5c373f9e5d81496ae1be7df1d4)shared\_multi\_heap\_attr

| enum [shared\_multi\_heap\_attr](#ga11861c5c373f9e5d81496ae1be7df1d4) |
| --- |

`#include <[shared_multi_heap.h](shared__multi__heap_8h.md)>`

SMH region attributes enumeration type.

Enumeration type for some common memory region attributes.

| Enumerator | |
| --- | --- |
| SMH\_REG\_ATTR\_CACHEABLE | cacheable |
| SMH\_REG\_ATTR\_NON\_CACHEABLE | non-cacheable |
| SMH\_REG\_ATTR\_NUM | must be the last item |

## Function Documentation

## [◆ ](#ga086362a2a8fce827a246039ef8757cc5)shared\_multi\_heap\_add()

| int shared\_multi\_heap\_add | ( | struct [shared\_multi\_heap\_region](structshared__multi__heap__region.md) \* | *region*, |
| --- | --- | --- | --- |
|  |  | void \* | *user\_data* ) |

`#include <[shared_multi_heap.h](shared__multi__heap_8h.md)>`

Add an heap region to the shared multi-heap pool.

This adds a shared multi-heap region to the multi-heap pool.

Parameters
:   | user\_data | pointer to any data for the heap. |
    | --- | --- |
    | region | pointer to the memory region to be added. |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EINVAL | when the region attribute is out-of-bound. |
    | -ENOMEM | when there are no more heaps available. |
    | other | errno codes |

## [◆ ](#ga328b199253da06ed724e9b0157167ede)shared\_multi\_heap\_aligned\_alloc()

| void \* shared\_multi\_heap\_aligned\_alloc | ( | enum [shared\_multi\_heap\_attr](#ga11861c5c373f9e5d81496ae1be7df1d4) | *attr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *align*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bytes* ) |

`#include <[shared_multi_heap.h](shared__multi__heap_8h.md)>`

Allocate aligned memory from the memory shared multi-heap pool.

Allocates a block of memory of the specified size in bytes and with a specified capability / attribute. Takes an additional parameter specifying a power of two alignment in bytes.

Parameters
:   | attr | capability / attribute requested for the memory block. |
    | --- | --- |
    | align | power of two alignment for the returned pointer, in bytes. |
    | bytes | requested size of the allocation in bytes. |

Return values
:   | ptr | a valid pointer to heap memory. |
    | --- | --- |
    | err | NULL if no memory is available. |

## [◆ ](#ga8cd3d321f5ae516cd55812d304289971)shared\_multi\_heap\_alloc()

| void \* shared\_multi\_heap\_alloc | ( | enum [shared\_multi\_heap\_attr](#ga11861c5c373f9e5d81496ae1be7df1d4) | *attr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bytes* ) |

`#include <[shared_multi_heap.h](shared__multi__heap_8h.md)>`

Allocate memory from the memory shared multi-heap pool.

Allocates a block of memory of the specified size in bytes and with a specified capability / attribute. The opaque attribute parameter is used by the backend to select the correct heap to allocate memory from.

Parameters
:   | attr | capability / attribute requested for the memory block. |
    | --- | --- |
    | bytes | requested size of the allocation in bytes. |

Return values
:   | ptr | a valid pointer to heap memory. |
    | --- | --- |
    | err | NULL if no memory is available. |

## [◆ ](#gab968bf26483d22939aaa7c2b1b6743ad)shared\_multi\_heap\_free()

| void shared\_multi\_heap\_free | ( | void \* | *block* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[shared_multi_heap.h](shared__multi__heap_8h.md)>`

Free memory from the shared multi-heap pool.

Used to free the passed block of memory that must be the return value of a previously call to [shared\_multi\_heap\_alloc](#ga8cd3d321f5ae516cd55812d304289971) or [shared\_multi\_heap\_aligned\_alloc](#ga328b199253da06ed724e9b0157167ede).

Parameters
:   | block | block to free, must be a pointer to a block allocated by shared\_multi\_heap\_alloc or shared\_multi\_heap\_aligned\_alloc. |
    | --- | --- |

## [◆ ](#ga5b7f09666e3eac051b4c4942572f9ca3)shared\_multi\_heap\_pool\_init()

| int shared\_multi\_heap\_pool\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[shared_multi_heap.h](shared__multi__heap_8h.md)>`

Init the pool.

This must be the first function to be called to initialize the shared multi-heap pool. All the individual heaps must be added later with [shared\_multi\_heap\_add](#ga086362a2a8fce827a246039ef8757cc5).

Note
:   As for the generic multi-heap allocator the expectation is that this function will be called at soc- or board-level.

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EALREADY | when the pool was already inited. |
    | other | errno codes |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
