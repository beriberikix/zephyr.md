---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__multi__heap__wrapper.html
original_path: doxygen/html/group__multi__heap__wrapper.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Multi-Heap Wrapper

[Operating System Services](group__os__services.md) » [Heap Management](group__heaps.md)

| Data Structures | |
| --- | --- |
| struct | [sys\_multi\_heap\_rec](structsys__multi__heap__rec.md) |
| struct | [sys\_multi\_heap](structsys__multi__heap.md) |

| Typedefs | |
| --- | --- |
| typedef void \*(\* | [sys\_multi\_heap\_fn\_t](#ga2d8ac07e590ef36ba6f35ae88235564e)) (struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap, void \*cfg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Multi-heap choice function. |

| Functions | |
| --- | --- |
| void | [sys\_multi\_heap\_init](#ga50ded513b50c7aed7d89386bb8f425cc) (struct [sys\_multi\_heap](structsys__multi__heap.md) \*heap, [sys\_multi\_heap\_fn\_t](#ga2d8ac07e590ef36ba6f35ae88235564e) choice\_fn) |
|  | Initialize multi-heap. |
| void | [sys\_multi\_heap\_add\_heap](#gacd6b92e8090a56e1eb59a18166d659d1) (struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap, struct [sys\_heap](structsys__heap.md) \*heap, void \*user\_data) |
|  | Add [sys\_heap](structsys__heap.md) to multi heap. |
| void \* | [sys\_multi\_heap\_alloc](#ga050d7499b982ed62f85d5fc15f79548b) (struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap, void \*cfg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Allocate memory from multi heap. |
| void \* | [sys\_multi\_heap\_aligned\_alloc](#ga9f958dbfa86e12236b8e356375b8d04c) (struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap, void \*cfg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Allocate aligned memory from multi heap. |
| const struct [sys\_multi\_heap\_rec](structsys__multi__heap__rec.md) \* | [sys\_multi\_heap\_get\_heap](#gad98b78be5c0ed50e1e0715a15c289b3a) (const struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap, void \*addr) |
|  | Get a specific heap for provided address. |
| void | [sys\_multi\_heap\_free](#gac6f913a3bbf247807ba80408a242db73) (struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap, void \*block) |
|  | Free memory allocated from multi heap. |

## Detailed Description

## Typedef Documentation

## [◆ ](#ga2d8ac07e590ef36ba6f35ae88235564e)sys\_multi\_heap\_fn\_t

| typedef void \*(\* sys\_multi\_heap\_fn\_t) (struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap, void \*cfg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
| --- |

`#include <[multi_heap.h](multi__heap_8h.md)>`

Multi-heap choice function.

This is a user-provided functions whose responsibility is selecting a specific [sys\_heap](structsys__heap.md) backend based on the opaque cfg value, which is specified by the user as an argument to [sys\_multi\_heap\_alloc()](#ga050d7499b982ed62f85d5fc15f79548b), and performing the allocation on behalf of the caller. The callback is free to choose any registered heap backend to perform the allocation, and may choose to pad the user-provided values as needed, and to use an aligned allocation where required by the specified configuration.

NULL may be returned, which will cause the allocation to fail and a NULL reported to the calling code.

Parameters
:   | mheap | Multi-heap structure. |
    | --- | --- |
    | cfg | An opaque user-provided value. It may be interpreted in any way by the application |
    | align | Alignment of requested memory (or zero for no alignment) |
    | size | The user-specified allocation size in bytes |

Returns
:   A pointer to the allocated memory

## Function Documentation

## [◆ ](#gacd6b92e8090a56e1eb59a18166d659d1)sys\_multi\_heap\_add\_heap()

| void sys\_multi\_heap\_add\_heap | ( | struct [sys\_multi\_heap](structsys__multi__heap.md) \* | *mheap*, |
| --- | --- | --- | --- |
|  |  | struct [sys\_heap](structsys__heap.md) \* | *heap*, |
|  |  | void \* | *user\_data* ) |

`#include <[multi_heap.h](multi__heap_8h.md)>`

Add [sys\_heap](structsys__heap.md) to multi heap.

This adds a known [sys\_heap](structsys__heap.md) backend to an existing multi heap, allowing the multi heap internals to track the bounds of the heap and determine which heap (if any) from which a freed block was allocated.

Parameters
:   | mheap | A [sys\_multi\_heap](structsys__multi__heap.md) to which to add a heap |
    | --- | --- |
    | heap | The heap to add |
    | user\_data | pointer to any data for the heap |

## [◆ ](#ga9f958dbfa86e12236b8e356375b8d04c)sys\_multi\_heap\_aligned\_alloc()

| void \* sys\_multi\_heap\_aligned\_alloc | ( | struct [sys\_multi\_heap](structsys__multi__heap.md) \* | *mheap*, |
| --- | --- | --- | --- |
|  |  | void \* | *cfg*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *align*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bytes* ) |

`#include <[multi_heap.h](multi__heap_8h.md)>`

Allocate aligned memory from multi heap.

Just as for [sys\_multi\_heap\_alloc()](#ga050d7499b982ed62f85d5fc15f79548b), allocates a block of memory of the specified size in bytes. Takes an additional parameter specifying a power of two alignment, in bytes.

Parameters
:   | mheap | Multi heap pointer |
    | --- | --- |
    | cfg | Opaque configuration parameter, as for [sys\_multi\_heap\_fn\_t](#ga2d8ac07e590ef36ba6f35ae88235564e) |
    | align | Power of two alignment for the returned pointer, in bytes |
    | bytes | Requested size of the allocation, in bytes |

Returns
:   A valid pointer to heap memory, or NULL if no memory is available

## [◆ ](#ga050d7499b982ed62f85d5fc15f79548b)sys\_multi\_heap\_alloc()

| void \* sys\_multi\_heap\_alloc | ( | struct [sys\_multi\_heap](structsys__multi__heap.md) \* | *mheap*, |
| --- | --- | --- | --- |
|  |  | void \* | *cfg*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bytes* ) |

`#include <[multi_heap.h](multi__heap_8h.md)>`

Allocate memory from multi heap.

Just as for [sys\_heap\_alloc()](group__low__level__heap__allocator.md#ga6b8bdf02c9be5576fddbe711904a3aad "Allocate memory from a sys_heap."), allocates a block of memory of the specified size in bytes. Takes an opaque configuration pointer passed to the multi heap choice function, which is used by integration code to choose a heap backend.

Parameters
:   | mheap | Multi heap pointer |
    | --- | --- |
    | cfg | Opaque configuration parameter, as for [sys\_multi\_heap\_fn\_t](#ga2d8ac07e590ef36ba6f35ae88235564e) |
    | bytes | Requested size of the allocation, in bytes |

Returns
:   A valid pointer to heap memory, or NULL if no memory is available

## [◆ ](#gac6f913a3bbf247807ba80408a242db73)sys\_multi\_heap\_free()

| void sys\_multi\_heap\_free | ( | struct [sys\_multi\_heap](structsys__multi__heap.md) \* | *mheap*, |
| --- | --- | --- | --- |
|  |  | void \* | *block* ) |

`#include <[multi_heap.h](multi__heap_8h.md)>`

Free memory allocated from multi heap.

Returns the specified block, which must be the return value of a previously successful [sys\_multi\_heap\_alloc()](#ga050d7499b982ed62f85d5fc15f79548b) or [sys\_multi\_heap\_aligned\_alloc()](#ga9f958dbfa86e12236b8e356375b8d04c) call, to the heap backend from which it was allocated.

Accepts NULL as a block parameter, which is specified to have no effect.

Parameters
:   | mheap | Multi heap pointer |
    | --- | --- |
    | block | Block to free, must be a pointer to a block allocated by sys\_multi\_heap\_alloc |

## [◆ ](#gad98b78be5c0ed50e1e0715a15c289b3a)sys\_multi\_heap\_get\_heap()

| const struct [sys\_multi\_heap\_rec](structsys__multi__heap__rec.md) \* sys\_multi\_heap\_get\_heap | ( | const struct [sys\_multi\_heap](structsys__multi__heap.md) \* | *mheap*, |
| --- | --- | --- | --- |
|  |  | void \* | *addr* ) |

`#include <[multi_heap.h](multi__heap_8h.md)>`

Get a specific heap for provided address.

Finds a single system heap (with user\_data) controlling the provided pointer

Parameters
:   | mheap | Multi heap pointer |
    | --- | --- |
    | addr | address to be found, must be a pointer to a block allocated by sys\_multi\_heap\_alloc |

Returns
:   0 multi\_heap\_rec pointer to a structure to be filled with return data or NULL if the heap has not been found

## [◆ ](#ga50ded513b50c7aed7d89386bb8f425cc)sys\_multi\_heap\_init()

| void sys\_multi\_heap\_init | ( | struct [sys\_multi\_heap](structsys__multi__heap.md) \* | *heap*, |
| --- | --- | --- | --- |
|  |  | [sys\_multi\_heap\_fn\_t](#ga2d8ac07e590ef36ba6f35ae88235564e) | *choice\_fn* ) |

`#include <[multi_heap.h](multi__heap_8h.md)>`

Initialize multi-heap.

Initialize a [sys\_multi\_heap](structsys__multi__heap.md) struct with the specified choice function. Note that individual heaps must be added later with sys\_multi\_heap\_add\_heap so that the heap bounds can be tracked by the multi heap code.

Note
:   In general a multiheap is likely to be instantiated semi-statically from system configuration (for example, via linker-provided bounds on available memory in different regions, or from devicetree definitions of hardware-provided addressable memory, etc...). The general expectation is that a soc- or board-level platform device will be initialized at system boot from these upstream configuration sources and not that an application will assemble a multi-heap on its own.

Parameters
:   | heap | A [sys\_multi\_heap](structsys__multi__heap.md) to initialize |
    | --- | --- |
    | choice\_fn | A [sys\_multi\_heap\_fn\_t](#ga2d8ac07e590ef36ba6f35ae88235564e) callback used to select heaps at allocation time |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
