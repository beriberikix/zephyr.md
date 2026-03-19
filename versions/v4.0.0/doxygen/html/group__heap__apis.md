---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__heap__apis.html
original_path: doxygen/html/group__heap__apis.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Heap APIs

[Kernel APIs](group__kernel__apis.md)

| Data Structures | |
| --- | --- |
| struct | [k\_heap](structk__heap.md) |

| Macros | |
| --- | --- |
| #define | [K\_HEAP\_DEFINE](#ga795d7f1e6d5b7b19a7a50198d7829a0f)(name, bytes) |
|  | Define a static [k\_heap](structk__heap.md). |
| #define | [K\_HEAP\_DEFINE\_NOCACHE](#ga968f4c6a201fdf6862d62dd5d9f8d032)(name, bytes) |
|  | Define a static [k\_heap](structk__heap.md) in uncached memory. |

| Functions | |
| --- | --- |
| void | [k\_heap\_init](#ga9273e06dc8d6a351499f2f5abfdcb39f) (struct [k\_heap](structk__heap.md) \*h, void \*mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Initialize a [k\_heap](structk__heap.md). |
| void \* | [k\_heap\_aligned\_alloc](#gaf77211a72441de389857bc13e10be4e6) (struct [k\_heap](structk__heap.md) \*h, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate aligned memory from a [k\_heap](structk__heap.md). |
| void \* | [k\_heap\_alloc](#ga22b83564e50ae6177388dfe63e32a512) (struct [k\_heap](structk__heap.md) \*h, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate memory from a [k\_heap](structk__heap.md). |
| void \* | [k\_heap\_realloc](#gabea4b2beae8ab138f2796fbeaa95d262) (struct [k\_heap](structk__heap.md) \*h, void \*ptr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Reallocate memory from a [k\_heap](structk__heap.md). |
| void | [k\_heap\_free](#ga6cf917a0b3d91a0101192bd4808ada9c) (struct [k\_heap](structk__heap.md) \*h, void \*mem) |
|  | Free memory allocated by [k\_heap\_alloc()](#ga22b83564e50ae6177388dfe63e32a512). |
| void \* | [k\_aligned\_alloc](#gae16d486aa250f9c07fa6a57342bcd3b4) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate memory from the heap with a specified alignment. |
| void \* | [k\_malloc](#gaa8edf1e63e5d5dd78d7adcfd787394ee) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate memory from the heap. |
| void | [k\_free](#ga79b63cc93b3358cf82d74f40e73b69d5) (void \*ptr) |
|  | Free memory allocated from heap. |
| void \* | [k\_calloc](#gad031d50ed62d08202a5dcf992c20246c) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) nmemb, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate memory from heap, array style. |
| void \* | [k\_realloc](#ga852a7a60dce5853b6925897b24a54e02) (void \*ptr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Expand the size of an existing allocation. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga795d7f1e6d5b7b19a7a50198d7829a0f)K\_HEAP\_DEFINE

| #define K\_HEAP\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *bytes* ) |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

Z\_HEAP\_DEFINE\_IN\_SECT(name, bytes, \

\_\_noinit\_named(kheap\_buf\_##name))

Define a static [k\_heap](structk__heap.md).

This macro defines and initializes a static memory region and [k\_heap](structk__heap.md) of the requested size. After kernel start, &name can be used as if [k\_heap\_init()](#ga9273e06dc8d6a351499f2f5abfdcb39f) had been called.

Note that this macro enforces a minimum size on the memory region to accommodate metadata requirements. Very small heaps will be padded to fit.

Parameters
:   | name | Symbol name for the struct [k\_heap](structk__heap.md) object |
    | --- | --- |
    | bytes | Size of memory region, in bytes |

## [◆ ](#ga968f4c6a201fdf6862d62dd5d9f8d032)K\_HEAP\_DEFINE\_NOCACHE

| #define K\_HEAP\_DEFINE\_NOCACHE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *bytes* ) |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

Z\_HEAP\_DEFINE\_IN\_SECT(name, bytes, \_\_nocache)

Define a static [k\_heap](structk__heap.md) in uncached memory.

This macro defines and initializes a static memory region and [k\_heap](structk__heap.md) of the requested size in uncached memory. After kernel start, &name can be used as if [k\_heap\_init()](#ga9273e06dc8d6a351499f2f5abfdcb39f) had been called.

Note that this macro enforces a minimum size on the memory region to accommodate metadata requirements. Very small heaps will be padded to fit.

Parameters
:   | name | Symbol name for the struct [k\_heap](structk__heap.md) object |
    | --- | --- |
    | bytes | Size of memory region, in bytes |

## Function Documentation

## [◆ ](#gae16d486aa250f9c07fa6a57342bcd3b4)k\_aligned\_alloc()

| void \* k\_aligned\_alloc | ( | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *align*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[kernel.h](kernel_8h.md)>`

Allocate memory from the heap with a specified alignment.

This routine provides semantics similar to [aligned\_alloc()](stdlib_8h.md#a8006724372b77924155bd8618fe57516); memory is allocated from the heap with a specified alignment. However, one minor difference is that [k\_aligned\_alloc()](#gae16d486aa250f9c07fa6a57342bcd3b4) accepts any non-zero `size`, whereas [aligned\_alloc()](stdlib_8h.md#a8006724372b77924155bd8618fe57516) only accepts a `size` that is an integral multiple of `align`.

Above, [aligned\_alloc()](stdlib_8h.md#a8006724372b77924155bd8618fe57516) refers to: C11 standard (ISO/IEC 9899:2011): 7.22.3.1 The aligned\_alloc function (p: 347-348)

Parameters
:   | align | Alignment of memory requested (in bytes). |
    | --- | --- |
    | size | Amount of memory requested (in bytes). |

Returns
:   Address of the allocated memory if successful; otherwise NULL.

## [◆ ](#gad031d50ed62d08202a5dcf992c20246c)k\_calloc()

| void \* k\_calloc | ( | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *nmemb*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[kernel.h](kernel_8h.md)>`

Allocate memory from heap, array style.

This routine provides traditional [calloc()](stdlib_8h.md#a2807e26a012717736641384f91ab2563) semantics. Memory is allocated from the heap memory pool and zeroed.

Parameters
:   | nmemb | Number of elements in the requested array |
    | --- | --- |
    | size | Size of each array element (in bytes). |

Returns
:   Address of the allocated memory if successful; otherwise NULL.

## [◆ ](#ga79b63cc93b3358cf82d74f40e73b69d5)k\_free()

| void k\_free | ( | void \* | *ptr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Free memory allocated from heap.

This routine provides traditional [free()](stdlib_8h.md#afbedc913aa4651b3c3b4b3aecd9b4711) semantics. The memory being returned must have been allocated from the heap memory pool.

If *ptr* is NULL, no operation is performed.

Parameters
:   | ptr | Pointer to previously allocated memory. |
    | --- | --- |

## [◆ ](#gaf77211a72441de389857bc13e10be4e6)k\_heap\_aligned\_alloc()

| | void \* k\_heap\_aligned\_alloc | ( | struct [k\_heap](structk__heap.md) \* | *h*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *align*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bytes*, | |  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Allocate aligned memory from a [k\_heap](structk__heap.md).

Behaves in all ways like [k\_heap\_alloc()](#ga22b83564e50ae6177388dfe63e32a512), except that the returned memory (if available) will have a starting address in memory which is a multiple of the specified power-of-two alignment value in bytes. The resulting memory can be returned to the heap using [k\_heap\_free()](#ga6cf917a0b3d91a0101192bd4808ada9c).

Note
:   *timeout* must be set to K\_NO\_WAIT if called from ISR.
:   When CONFIG\_MULTITHREADING=n any *timeout* is treated as K\_NO\_WAIT.

Function properties (list may not be complete)

Parameters
:   | h | Heap from which to allocate |
    | --- | --- |
    | align | Alignment in bytes, must be a power of two |
    | bytes | Number of bytes requested |
    | timeout | How long to wait, or K\_NO\_WAIT |

Returns
:   Pointer to memory the caller can now use

## [◆ ](#ga22b83564e50ae6177388dfe63e32a512)k\_heap\_alloc()

| | void \* k\_heap\_alloc | ( | struct [k\_heap](structk__heap.md) \* | *h*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bytes*, | |  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Allocate memory from a [k\_heap](structk__heap.md).

Allocates and returns a memory buffer from the memory region owned by the heap. If no memory is available immediately, the call will block for the specified timeout (constructed via the standard timeout API, or K\_NO\_WAIT or K\_FOREVER) waiting for memory to be freed. If the allocation cannot be performed by the expiration of the timeout, NULL will be returned. Allocated memory is aligned on a multiple of pointer sizes.

Note
:   *timeout* must be set to K\_NO\_WAIT if called from ISR.
:   When CONFIG\_MULTITHREADING=n any *timeout* is treated as K\_NO\_WAIT.

Function properties (list may not be complete)

Parameters
:   | h | Heap from which to allocate |
    | --- | --- |
    | bytes | Desired size of block to allocate |
    | timeout | How long to wait, or K\_NO\_WAIT |

Returns
:   A pointer to valid heap memory, or NULL

## [◆ ](#ga6cf917a0b3d91a0101192bd4808ada9c)k\_heap\_free()

| void k\_heap\_free | ( | struct [k\_heap](structk__heap.md) \* | *h*, |
| --- | --- | --- | --- |
|  |  | void \* | *mem* ) |

`#include <[kernel.h](kernel_8h.md)>`

Free memory allocated by [k\_heap\_alloc()](#ga22b83564e50ae6177388dfe63e32a512).

Returns the specified memory block, which must have been returned from [k\_heap\_alloc()](#ga22b83564e50ae6177388dfe63e32a512), to the heap for use by other callers. Passing a NULL block is legal, and has no effect.

Parameters
:   | h | Heap to which to return the memory |
    | --- | --- |
    | mem | A valid memory block, or NULL |

## [◆ ](#ga9273e06dc8d6a351499f2f5abfdcb39f)k\_heap\_init()

| void k\_heap\_init | ( | struct [k\_heap](structk__heap.md) \* | *h*, |
| --- | --- | --- | --- |
|  |  | void \* | *mem*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bytes* ) |

`#include <[kernel.h](kernel_8h.md)>`

Initialize a [k\_heap](structk__heap.md).

This constructs a synchronized [k\_heap](structk__heap.md) object over a memory region specified by the user. Note that while any alignment and size can be passed as valid parameters, internal alignment restrictions inside the inner [sys\_heap](structsys__heap.md) mean that not all bytes may be usable as allocated memory.

Parameters
:   | h | Heap struct to initialize |
    | --- | --- |
    | mem | Pointer to memory. |
    | bytes | Size of memory region, in bytes |

## [◆ ](#gabea4b2beae8ab138f2796fbeaa95d262)k\_heap\_realloc()

| | void \* k\_heap\_realloc | ( | struct [k\_heap](structk__heap.md) \* | *h*, | | --- | --- | --- | --- | |  |  | void \* | *ptr*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bytes*, | |  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Reallocate memory from a [k\_heap](structk__heap.md).

Reallocates and returns a memory buffer from the memory region owned by the heap. If no memory is available immediately, the call will block for the specified timeout (constructed via the standard timeout API, or K\_NO\_WAIT or K\_FOREVER) waiting for memory to be freed. If the allocation cannot be performed by the expiration of the timeout, NULL will be returned. Reallocated memory is aligned on a multiple of pointer sizes.

Note
:   *timeout* must be set to K\_NO\_WAIT if called from ISR.
:   When CONFIG\_MULTITHREADING=n any *timeout* is treated as K\_NO\_WAIT.

Function properties (list may not be complete)

Parameters
:   | h | Heap from which to allocate |
    | --- | --- |
    | ptr | Original pointer returned from a previous allocation |
    | bytes | Desired size of block to allocate |
    | timeout | How long to wait, or K\_NO\_WAIT |

Returns
:   Pointer to memory the caller can now use, or NULL

## [◆ ](#gaa8edf1e63e5d5dd78d7adcfd787394ee)k\_malloc()

| void \* k\_malloc | ( | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Allocate memory from the heap.

This routine provides traditional [malloc()](stdlib_8h.md#a9c36d0fe3ec4675cbffdc9b52f5fb399) semantics. Memory is allocated from the heap memory pool. Allocated memory is aligned on a multiple of pointer sizes.

Parameters
:   | size | Amount of memory requested (in bytes). |
    | --- | --- |

Returns
:   Address of the allocated memory if successful; otherwise NULL.

## [◆ ](#ga852a7a60dce5853b6925897b24a54e02)k\_realloc()

| void \* k\_realloc | ( | void \* | *ptr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[kernel.h](kernel_8h.md)>`

Expand the size of an existing allocation.

Returns a pointer to a new memory region with the same contents, but a different allocated size. If the new allocation can be expanded in place, the pointer returned will be identical. Otherwise the data will be copies to a new block and the old one will be freed as per [sys\_heap\_free()](group__low__level__heap__allocator.md#gab654da64adf74e67ae12f263eb420560 "Free memory into a sys_heap."). If the specified size is smaller than the original, the block will be truncated in place and the remaining memory returned to the heap. If the allocation of a new block fails, then NULL will be returned and the old block will not be freed or modified.

Parameters
:   | ptr | Original pointer returned from a previous allocation |
    | --- | --- |
    | size | Amount of memory requested (in bytes). |

Returns
:   Pointer to memory the caller can now use, or NULL.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
