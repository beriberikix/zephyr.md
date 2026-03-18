---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__low__level__heap__allocator.html
original_path: doxygen/html/group__low__level__heap__allocator.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Low Level Heap Allocator

[Operating System Services](group__os__services.md) » [Heap Management](group__heaps.md)

| Macros | |
| --- | --- |
| #define | [sys\_heap\_realloc](#ga0b6c4f17521a4ea996f5abf15883737a)(heap, ptr, bytes) |

| Functions | |
| --- | --- |
| void | [sys\_heap\_init](#ga520768606a3c28b084cf11f8ec82fae6) (struct [sys\_heap](structsys__heap.md) \*heap, void \*mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Initialize [sys\_heap](structsys__heap.md). |
| void \* | [sys\_heap\_alloc](#ga6b8bdf02c9be5576fddbe711904a3aad) (struct [sys\_heap](structsys__heap.md) \*heap, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Allocate memory from a [sys\_heap](structsys__heap.md). |
| void \* | [sys\_heap\_aligned\_alloc](#ga92a973158860c6863e1aba8516311076) (struct [sys\_heap](structsys__heap.md) \*heap, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Allocate aligned memory from a [sys\_heap](structsys__heap.md). |
| void | [sys\_heap\_free](#gab654da64adf74e67ae12f263eb420560) (struct [sys\_heap](structsys__heap.md) \*heap, void \*mem) |
|  | Free memory into a [sys\_heap](structsys__heap.md). |
| void \* | [sys\_heap\_aligned\_realloc](#ga16e1408c3ad5541daac756e46b33b612) (struct [sys\_heap](structsys__heap.md) \*heap, void \*ptr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Expand the size of an existing allocation. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [sys\_heap\_usable\_size](#gaf8cb77365c04022181e2fc45e3fbce4a) (struct [sys\_heap](structsys__heap.md) \*heap, void \*mem) |
|  | Return allocated memory size. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_heap\_validate](#ga9330ee91a1ef439efed89528e3e2a03a) (struct [sys\_heap](structsys__heap.md) \*heap) |
|  | Validate heap integrity. |
| void | [sys\_heap\_stress](#gae2f307f7b25e4927d3dbe650567b6308) (void \*(\*alloc\_fn)(void \*arg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes), void(\*free\_fn)(void \*arg, void \*p), void \*arg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) total\_bytes, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) op\_count, void \*scratch\_mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) scratch\_bytes, int target\_percent, struct z\_heap\_stress\_result \*result) |
|  | [sys\_heap](structsys__heap.md) stress test rig |
| void | [sys\_heap\_print\_info](#gaf36db704bd892b657ccaa7a4cebc45e5) (struct [sys\_heap](structsys__heap.md) \*heap, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) dump\_chunks) |
|  | Print heap internal structure information to the console. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga0b6c4f17521a4ea996f5abf15883737a)sys\_heap\_realloc

| #define sys\_heap\_realloc | ( |  | *heap*, |
| --- | --- | --- | --- |
|  |  |  | *ptr*, |
|  |  |  | *bytes* ) |

`#include <[sys_heap.h](sys__heap_8h.md)>`

**Value:**

[sys\_heap\_aligned\_realloc](#ga16e1408c3ad5541daac756e46b33b612)(heap, ptr, 0, bytes)

[sys\_heap\_aligned\_realloc](#ga16e1408c3ad5541daac756e46b33b612)

void \* sys\_heap\_aligned\_realloc(struct sys\_heap \*heap, void \*ptr, size\_t align, size\_t bytes)

Expand the size of an existing allocation.

## Function Documentation

## [◆ ](#ga92a973158860c6863e1aba8516311076)sys\_heap\_aligned\_alloc()

| void \* sys\_heap\_aligned\_alloc | ( | struct [sys\_heap](structsys__heap.md) \* | *heap*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *align*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bytes* ) |

`#include <[sys_heap.h](sys__heap_8h.md)>`

Allocate aligned memory from a [sys\_heap](structsys__heap.md).

Behaves in all ways like [sys\_heap\_alloc()](#ga6b8bdf02c9be5576fddbe711904a3aad), except that the returned memory (if available) will have a starting address in memory which is a multiple of the specified power-of-two alignment value in bytes. With align=0 this behaves exactly like [sys\_heap\_alloc()](#ga6b8bdf02c9be5576fddbe711904a3aad). The resulting memory can be returned to the heap using [sys\_heap\_free()](#gab654da64adf74e67ae12f263eb420560).

Parameters
:   | heap | Heap from which to allocate |
    | --- | --- |
    | align | Alignment in bytes, must be a power of two |
    | bytes | Number of bytes requested |

Returns
:   Pointer to memory the caller can now use

## [◆ ](#ga16e1408c3ad5541daac756e46b33b612)sys\_heap\_aligned\_realloc()

| void \* sys\_heap\_aligned\_realloc | ( | struct [sys\_heap](structsys__heap.md) \* | *heap*, |
| --- | --- | --- | --- |
|  |  | void \* | *ptr*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *align*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bytes* ) |

`#include <[sys_heap.h](sys__heap_8h.md)>`

Expand the size of an existing allocation.

Returns a pointer to a new memory region with the same contents, but a different allocated size. If the new allocation can be expanded in place, the pointer returned will be identical. Otherwise the data will be copies to a new block and the old one will be freed as per [sys\_heap\_free()](#gab654da64adf74e67ae12f263eb420560). If the specified size is smaller than the original, the block will be truncated in place and the remaining memory returned to the heap. If the allocation of a new block fails, then NULL will be returned and the old block will not be freed or modified.

Parameters
:   | heap | Heap from which to allocate |
    | --- | --- |
    | ptr | Original pointer returned from a previous allocation |
    | align | Alignment in bytes, must be a power of two |
    | bytes | Number of bytes requested for the new block |

Returns
:   Pointer to memory the caller can now use, or NULL

## [◆ ](#ga6b8bdf02c9be5576fddbe711904a3aad)sys\_heap\_alloc()

| void \* sys\_heap\_alloc | ( | struct [sys\_heap](structsys__heap.md) \* | *heap*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bytes* ) |

`#include <[sys_heap.h](sys__heap_8h.md)>`

Allocate memory from a [sys\_heap](structsys__heap.md).

Returns a pointer to a block of unused memory in the heap. This memory will not otherwise be used until it is freed with [sys\_heap\_free()](#gab654da64adf74e67ae12f263eb420560). If no memory can be allocated, NULL will be returned. The allocated memory is guaranteed to have a starting address which is a multiple of sizeof(void \*). If a bigger alignment is necessary then [sys\_heap\_aligned\_alloc()](#ga92a973158860c6863e1aba8516311076) should be used instead.

Note
:   The [sys\_heap](structsys__heap.md) implementation is not internally synchronized. No two [sys\_heap](structsys__heap.md) functions should operate on the same heap at the same time. All locking must be provided by the user.

Parameters
:   | heap | Heap from which to allocate |
    | --- | --- |
    | bytes | Number of bytes requested |

Returns
:   Pointer to memory the caller can now use

## [◆ ](#gab654da64adf74e67ae12f263eb420560)sys\_heap\_free()

| void sys\_heap\_free | ( | struct [sys\_heap](structsys__heap.md) \* | *heap*, |
| --- | --- | --- | --- |
|  |  | void \* | *mem* ) |

`#include <[sys_heap.h](sys__heap_8h.md)>`

Free memory into a [sys\_heap](structsys__heap.md).

De-allocates a pointer to memory previously returned from sys\_heap\_alloc such that it can be used for other purposes. The caller must not use the memory region after entry to this function.

Note
:   The [sys\_heap](structsys__heap.md) implementation is not internally synchronized. No two [sys\_heap](structsys__heap.md) functions should operate on the same heap at the same time. All locking must be provided by the user.

Parameters
:   | heap | Heap to which to return the memory |
    | --- | --- |
    | mem | A pointer previously returned from [sys\_heap\_alloc()](#ga6b8bdf02c9be5576fddbe711904a3aad) |

## [◆ ](#ga520768606a3c28b084cf11f8ec82fae6)sys\_heap\_init()

| void sys\_heap\_init | ( | struct [sys\_heap](structsys__heap.md) \* | *heap*, |
| --- | --- | --- | --- |
|  |  | void \* | *mem*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bytes* ) |

`#include <[sys_heap.h](sys__heap_8h.md)>`

Initialize [sys\_heap](structsys__heap.md).

Initializes a [sys\_heap](structsys__heap.md) struct to manage the specified memory.

Parameters
:   | heap | Heap to initialize |
    | --- | --- |
    | mem | Untyped pointer to unused memory |
    | bytes | Size of region pointed to by *mem* |

## [◆ ](#gaf36db704bd892b657ccaa7a4cebc45e5)sys\_heap\_print\_info()

| void sys\_heap\_print\_info | ( | struct [sys\_heap](structsys__heap.md) \* | *heap*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *dump\_chunks* ) |

`#include <[sys_heap.h](sys__heap_8h.md)>`

Print heap internal structure information to the console.

Print information on the heap structure such as its size, chunk buckets, chunk list and some statistics for debugging purpose.

Parameters
:   | heap | Heap to print information about |
    | --- | --- |
    | dump\_chunks | True to print the entire heap chunk list |

## [◆ ](#gae2f307f7b25e4927d3dbe650567b6308)sys\_heap\_stress()

| void sys\_heap\_stress | ( | void \*(\* | *alloc\_fn*)(void \*arg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes), |
| --- | --- | --- | --- |
|  |  | void(\* | *free\_fn*)(void \*arg, void \*p), |
|  |  | void \* | *arg*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *total\_bytes*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *op\_count*, |
|  |  | void \* | *scratch\_mem*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *scratch\_bytes*, |
|  |  | int | *target\_percent*, |
|  |  | struct z\_heap\_stress\_result \* | *result* ) |

`#include <[sys_heap.h](sys__heap_8h.md)>`

[sys\_heap](structsys__heap.md) stress test rig

Test rig for heap allocation validation. This will loop for *op\_count* cycles, in each iteration making a random choice to allocate or free a pointer of randomized (power law) size based on heuristics designed to keep the heap in a state where it is near *target\_percent* full. Allocation and free operations are provided by the caller as callbacks (i.e. this can in theory test any heap). Results, including counts of frees and successful/unsuccessful allocations, are returned via the *result* struct.

Parameters
:   | alloc\_fn | Callback to perform an allocation. Passes back the *arg* parameter as a context handle. |
    | --- | --- |
    | free\_fn | Callback to perform a free of a pointer returned from *alloc*. Passes back the *arg* parameter as a context handle. |
    | arg | Context handle to pass back to the callbacks |
    | total\_bytes | Size of the byte array the heap was initialized in |
    | op\_count | How many iterations to test |
    | scratch\_mem | A pointer to scratch memory to be used by the test. Should be about 1/2 the size of the heap for tests that need to stress fragmentation. |
    | scratch\_bytes | Size of the memory pointed to by *scratch\_mem* |
    | target\_percent | Percentage fill value (1-100) to which the random allocation choices will seek. High values will result in significant allocation failures and a very fragmented heap. |
    | result | Struct into which to store test results. |

## [◆ ](#gaf8cb77365c04022181e2fc45e3fbce4a)sys\_heap\_usable\_size()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sys\_heap\_usable\_size | ( | struct [sys\_heap](structsys__heap.md) \* | *heap*, |
| --- | --- | --- | --- |
|  |  | void \* | *mem* ) |

`#include <[sys_heap.h](sys__heap_8h.md)>`

Return allocated memory size.

Returns the size, in bytes, of a block returned from a successful [sys\_heap\_alloc()](#ga6b8bdf02c9be5576fddbe711904a3aad) or sys\_heap\_alloc\_aligned() call. The value returned is the size of the heap-managed memory, which may be larger than the number of bytes requested due to allocation granularity. The heap code is guaranteed to make no access to this region of memory until a subsequent [sys\_heap\_free()](#gab654da64adf74e67ae12f263eb420560) on the same pointer.

Parameters
:   | heap | Heap containing the block |
    | --- | --- |
    | mem | Pointer to memory allocated from this heap |

Returns
:   Size in bytes of the memory region

## [◆ ](#ga9330ee91a1ef439efed89528e3e2a03a)sys\_heap\_validate()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_heap\_validate | ( | struct [sys\_heap](structsys__heap.md) \* | *heap* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sys_heap.h](sys__heap_8h.md)>`

Validate heap integrity.

Validates the internal integrity of a [sys\_heap](structsys__heap.md). Intended for unit test and validation code, though potentially useful as a user API for applications with complicated runtime reliability requirements. Note: this cannot catch every possible error, but if it returns true then the heap is in a consistent state and can correctly handle any [sys\_heap\_alloc()](#ga6b8bdf02c9be5576fddbe711904a3aad) request and free any live pointer returned from a previous allocation.

Parameters
:   | heap | Heap to validate |
    | --- | --- |

Returns
:   true, if the heap is valid, otherwise false

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
