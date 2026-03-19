---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__mem__blocks__apis.html
original_path: doxygen/html/group__mem__blocks__apis.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Memory Blocks APIs

[Operating System Services](group__os__services.md) » [Memory Management](group__memory__management.md)

| Macros | |
| --- | --- |
| #define | [SYS\_MEM\_BLOCKS\_DEFINE](#gab49fdcd86522d318051ca6a6ddf41c7c)(name, blk\_sz, num\_blks, buf\_align) |
|  | Create a memory block object with a new backing buffer. |
| #define | [SYS\_MEM\_BLOCKS\_DEFINE\_STATIC](#gaa6b90846448323837dab3a17c3065359)(name, blk\_sz, num\_blks, buf\_align) |
|  | Create a static memory block object with a new backing buffer. |
| #define | [SYS\_MEM\_BLOCKS\_DEFINE\_WITH\_EXT\_BUF](#gae6b688b2925308c9007071bab681dcdd)(name, blk\_sz, num\_blks, buf) |
|  | Create a memory block object with a providing backing buffer. |
| #define | [SYS\_MEM\_BLOCKS\_DEFINE\_STATIC\_WITH\_EXT\_BUF](#gaad3cfb34553bd97290b388bec910b8cc)(name, blk\_sz, num\_blks, buf) |
|  | Create a static memory block object with a providing backing buffer. |

| Typedefs | |
| --- | --- |
| typedef struct sys\_mem\_blocks | [sys\_mem\_blocks\_t](#ga5748df756d2f9aa10fddf2f39bf8a074) |
|  | Memory Blocks Allocator. |
| typedef struct sys\_multi\_mem\_blocks | [sys\_multi\_mem\_blocks\_t](#ga00d9c0bafe800dffa3676d37983499a8) |
|  | Multi Memory Blocks Allocator. |
| typedef [sys\_mem\_blocks\_t](#ga5748df756d2f9aa10fddf2f39bf8a074) \*(\* | [sys\_multi\_mem\_blocks\_choice\_fn\_t](#ga2e58484681d0d9629af9a8c7c14453d9)) (struct sys\_multi\_mem\_blocks \*[group](structgroup.md), void \*cfg) |
|  | Multi memory blocks allocator choice function. |

| Functions | |
| --- | --- |
| int | [sys\_mem\_blocks\_alloc](#ga3e53a5c65bb0e88fbf20e66b016c1dff) ([sys\_mem\_blocks\_t](#ga5748df756d2f9aa10fddf2f39bf8a074) \*mem\_block, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count, void \*\*out\_blocks) |
|  | Allocate multiple memory blocks. |
| int | [sys\_mem\_blocks\_alloc\_contiguous](#ga72614d0c120f40209837b77d0333bb23) ([sys\_mem\_blocks\_t](#ga5748df756d2f9aa10fddf2f39bf8a074) \*mem\_block, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count, void \*\*out\_block) |
|  | Allocate a contiguous set of memory blocks. |
| int | [sys\_mem\_blocks\_get](#ga0ae169fbe2b3d3a68815ba0898ef5338) ([sys\_mem\_blocks\_t](#ga5748df756d2f9aa10fddf2f39bf8a074) \*mem\_block, void \*in\_block, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count) |
|  | Force allocation of a specified blocks in a memory block object. |
| int | [sys\_mem\_blocks\_is\_region\_free](#ga7a8ff3370747ae382ed24ad7b8b34746) ([sys\_mem\_blocks\_t](#ga5748df756d2f9aa10fddf2f39bf8a074) \*mem\_block, void \*in\_block, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count) |
|  | check if the region is free |
| int | [sys\_mem\_blocks\_free](#gadd799f4f2423277ed5daf08a0d150b9c) ([sys\_mem\_blocks\_t](#ga5748df756d2f9aa10fddf2f39bf8a074) \*mem\_block, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count, void \*\*in\_blocks) |
|  | Free multiple memory blocks. |
| int | [sys\_mem\_blocks\_free\_contiguous](#ga39e7f8dfe3bda8eabc2372f9a1e87342) ([sys\_mem\_blocks\_t](#ga5748df756d2f9aa10fddf2f39bf8a074) \*mem\_block, void \*block, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count) |
|  | Free contiguous multiple memory blocks. |
| void | [sys\_multi\_mem\_blocks\_init](#gad39867e3cd1e1e69e6fb3746c05abed0) ([sys\_multi\_mem\_blocks\_t](#ga00d9c0bafe800dffa3676d37983499a8) \*[group](structgroup.md), [sys\_multi\_mem\_blocks\_choice\_fn\_t](#ga2e58484681d0d9629af9a8c7c14453d9) choice\_fn) |
|  | Initialize multi memory blocks allocator group. |
| void | [sys\_multi\_mem\_blocks\_add\_allocator](#ga03967e8b917a1592638586c9cfbba4bb) ([sys\_multi\_mem\_blocks\_t](#ga00d9c0bafe800dffa3676d37983499a8) \*[group](structgroup.md), [sys\_mem\_blocks\_t](#ga5748df756d2f9aa10fddf2f39bf8a074) \*alloc) |
|  | Add an allocator to an allocator group. |
| int | [sys\_multi\_mem\_blocks\_alloc](#gafa96b1567b57c4466c9640fd1f5408b2) ([sys\_multi\_mem\_blocks\_t](#ga00d9c0bafe800dffa3676d37983499a8) \*[group](structgroup.md), void \*cfg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count, void \*\*out\_blocks, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*blk\_size) |
|  | Allocate memory from multi memory blocks allocator group. |
| int | [sys\_multi\_mem\_blocks\_free](#ga8dedc28ed45e9e6350b584b1082b4d4f) ([sys\_multi\_mem\_blocks\_t](#ga00d9c0bafe800dffa3676d37983499a8) \*[group](structgroup.md), [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count, void \*\*in\_blocks) |
|  | Free memory allocated from multi memory blocks allocator group. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gab49fdcd86522d318051ca6a6ddf41c7c)SYS\_MEM\_BLOCKS\_DEFINE

| #define SYS\_MEM\_BLOCKS\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *blk\_sz*, |
|  |  |  | *num\_blks*, |
|  |  |  | *buf\_align* ) |

`#include <[mem_blocks.h](mem__blocks_8h.md)>`

**Value:**

\_SYS\_MEM\_BLOCKS\_DEFINE(name, blk\_sz, num\_blks, buf\_align,)

Create a memory block object with a new backing buffer.

Parameters
:   | name | Name of the memory block object. |
    | --- | --- |
    | blk\_sz | Size of each memory block (in bytes). |
    | num\_blks | Total number of memory blocks. |
    | buf\_align | Alignment of the memory block buffer (power of 2). |

## [◆ ](#gaa6b90846448323837dab3a17c3065359)SYS\_MEM\_BLOCKS\_DEFINE\_STATIC

| #define SYS\_MEM\_BLOCKS\_DEFINE\_STATIC | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *blk\_sz*, |
|  |  |  | *num\_blks*, |
|  |  |  | *buf\_align* ) |

`#include <[mem_blocks.h](mem__blocks_8h.md)>`

**Value:**

\_SYS\_MEM\_BLOCKS\_DEFINE(name, blk\_sz, num\_blks, buf\_align, static)

Create a static memory block object with a new backing buffer.

Parameters
:   | name | Name of the memory block object. |
    | --- | --- |
    | blk\_sz | Size of each memory block (in bytes). |
    | num\_blks | Total number of memory blocks. |
    | buf\_align | Alignment of the memory block buffer (power of 2). |

## [◆ ](#gaad3cfb34553bd97290b388bec910b8cc)SYS\_MEM\_BLOCKS\_DEFINE\_STATIC\_WITH\_EXT\_BUF

| #define SYS\_MEM\_BLOCKS\_DEFINE\_STATIC\_WITH\_EXT\_BUF | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *blk\_sz*, |
|  |  |  | *num\_blks*, |
|  |  |  | *buf* ) |

`#include <[mem_blocks.h](mem__blocks_8h.md)>`

**Value:**

\_SYS\_MEM\_BLOCKS\_DEFINE\_WITH\_EXT\_BUF(name, blk\_sz, num\_blks, buf, static)

Create a static memory block object with a providing backing buffer.

Parameters
:   | name | Name of the memory block object. |
    | --- | --- |
    | blk\_sz | Size of each memory block (in bytes). |
    | num\_blks | Total number of memory blocks. |
    | buf | Backing buffer of type [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d). |

## [◆ ](#gae6b688b2925308c9007071bab681dcdd)SYS\_MEM\_BLOCKS\_DEFINE\_WITH\_EXT\_BUF

| #define SYS\_MEM\_BLOCKS\_DEFINE\_WITH\_EXT\_BUF | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *blk\_sz*, |
|  |  |  | *num\_blks*, |
|  |  |  | *buf* ) |

`#include <[mem_blocks.h](mem__blocks_8h.md)>`

**Value:**

\_SYS\_MEM\_BLOCKS\_DEFINE\_WITH\_EXT\_BUF(name, blk\_sz, num\_blks, buf,)

Create a memory block object with a providing backing buffer.

Parameters
:   | name | Name of the memory block object. |
    | --- | --- |
    | blk\_sz | Size of each memory block (in bytes). |
    | num\_blks | Total number of memory blocks. |
    | buf | Backing buffer of type [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d). |

## Typedef Documentation

## [◆ ](#ga5748df756d2f9aa10fddf2f39bf8a074)sys\_mem\_blocks\_t

| typedef struct sys\_mem\_blocks [sys\_mem\_blocks\_t](#ga5748df756d2f9aa10fddf2f39bf8a074) |
| --- |

`#include <[mem_blocks.h](mem__blocks_8h.md)>`

Memory Blocks Allocator.

## [◆ ](#ga2e58484681d0d9629af9a8c7c14453d9)sys\_multi\_mem\_blocks\_choice\_fn\_t

| typedef [sys\_mem\_blocks\_t](#ga5748df756d2f9aa10fddf2f39bf8a074) \*(\* sys\_multi\_mem\_blocks\_choice\_fn\_t) (struct sys\_multi\_mem\_blocks \*[group](structgroup.md), void \*cfg) |
| --- |

`#include <[mem_blocks.h](mem__blocks_8h.md)>`

Multi memory blocks allocator choice function.

This is a user-provided functions whose responsibility is selecting a specific memory blocks allocator based on the opaque cfg value, which is specified by the user as an argument to [sys\_multi\_mem\_blocks\_alloc()](#gafa96b1567b57c4466c9640fd1f5408b2). The callback returns a pointer to the chosen allocator where the allocation is performed.

NULL may be returned, which will cause the allocation to fail and a -EINVAL reported to the calling code.

Parameters
:   | [group](structgroup.md "Group structure.") | Multi memory blocks allocator structure. |
    | --- | --- |
    | cfg | An opaque user-provided value. It may be interpreted in any way by the application. |

Returns
:   A pointer to the chosen allocator, or NULL if none is chosen.

## [◆ ](#ga00d9c0bafe800dffa3676d37983499a8)sys\_multi\_mem\_blocks\_t

| typedef struct sys\_multi\_mem\_blocks [sys\_multi\_mem\_blocks\_t](#ga00d9c0bafe800dffa3676d37983499a8) |
| --- |

`#include <[mem_blocks.h](mem__blocks_8h.md)>`

Multi Memory Blocks Allocator.

## Function Documentation

## [◆ ](#ga3e53a5c65bb0e88fbf20e66b016c1dff)sys\_mem\_blocks\_alloc()

| int sys\_mem\_blocks\_alloc | ( | [sys\_mem\_blocks\_t](#ga5748df756d2f9aa10fddf2f39bf8a074) \* | *mem\_block*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *count*, |
|  |  | void \*\* | *out\_blocks* ) |

`#include <[mem_blocks.h](mem__blocks_8h.md)>`

Allocate multiple memory blocks.

Allocate multiple memory blocks, and place their pointers into the output array.

Parameters
:   | [in] | mem\_block | Pointer to memory block object. |
    | --- | --- | --- |
    | [in] | count | Number of blocks to allocate. |
    | [out] | out\_blocks | Output array to be populated by pointers to the memory blocks. It must have at least `count` elements. |

Return values
:   | 0 | Successful |
    | --- | --- |
    | -EINVAL | Invalid argument supplied. |
    | -ENOMEM | Not enough blocks for allocation. |

## [◆ ](#ga72614d0c120f40209837b77d0333bb23)sys\_mem\_blocks\_alloc\_contiguous()

| int sys\_mem\_blocks\_alloc\_contiguous | ( | [sys\_mem\_blocks\_t](#ga5748df756d2f9aa10fddf2f39bf8a074) \* | *mem\_block*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *count*, |
|  |  | void \*\* | *out\_block* ) |

`#include <[mem_blocks.h](mem__blocks_8h.md)>`

Allocate a contiguous set of memory blocks.

Allocate multiple memory blocks, and place their pointers into the output array.

Parameters
:   | [in] | mem\_block | Pointer to memory block object. |
    | --- | --- | --- |
    | [in] | count | Number of blocks to allocate. |
    | [out] | out\_block | Output pointer to the start of the allocated block set |

Return values
:   | 0 | Successful |
    | --- | --- |
    | -EINVAL | Invalid argument supplied. |
    | -ENOMEM | Not enough contiguous blocks for allocation. |

## [◆ ](#gadd799f4f2423277ed5daf08a0d150b9c)sys\_mem\_blocks\_free()

| int sys\_mem\_blocks\_free | ( | [sys\_mem\_blocks\_t](#ga5748df756d2f9aa10fddf2f39bf8a074) \* | *mem\_block*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *count*, |
|  |  | void \*\* | *in\_blocks* ) |

`#include <[mem_blocks.h](mem__blocks_8h.md)>`

Free multiple memory blocks.

Free multiple memory blocks according to the array of memory block pointers.

Parameters
:   | [in] | mem\_block | Pointer to memory block object. |
    | --- | --- | --- |
    | [in] | count | Number of blocks to free. |
    | [in] | in\_blocks | Input array of pointers to the memory blocks. |

Return values
:   | 0 | Successful |
    | --- | --- |
    | -EINVAL | Invalid argument supplied. |
    | -EFAULT | Invalid pointers supplied. |

## [◆ ](#ga39e7f8dfe3bda8eabc2372f9a1e87342)sys\_mem\_blocks\_free\_contiguous()

| int sys\_mem\_blocks\_free\_contiguous | ( | [sys\_mem\_blocks\_t](#ga5748df756d2f9aa10fddf2f39bf8a074) \* | *mem\_block*, |
| --- | --- | --- | --- |
|  |  | void \* | *block*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *count* ) |

`#include <[mem_blocks.h](mem__blocks_8h.md)>`

Free contiguous multiple memory blocks.

Free contiguous multiple memory blocks

Parameters
:   | [in] | mem\_block | Pointer to memory block object. |
    | --- | --- | --- |
    | [in] | block | Pointer to the first memory block |
    | [in] | count | Number of blocks to free. |

Return values
:   | 0 | Successful |
    | --- | --- |
    | -EINVAL | Invalid argument supplied. |
    | -EFAULT | Invalid pointer supplied. |

## [◆ ](#ga0ae169fbe2b3d3a68815ba0898ef5338)sys\_mem\_blocks\_get()

| int sys\_mem\_blocks\_get | ( | [sys\_mem\_blocks\_t](#ga5748df756d2f9aa10fddf2f39bf8a074) \* | *mem\_block*, |
| --- | --- | --- | --- |
|  |  | void \* | *in\_block*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *count* ) |

`#include <[mem_blocks.h](mem__blocks_8h.md)>`

Force allocation of a specified blocks in a memory block object.

Allocate a specified blocks in a memory block object. Note: use caution when mixing sys\_mem\_blocks\_get and sys\_mem\_blocks\_alloc, allocation may take any of the free memory space

Parameters
:   | [in] | mem\_block | Pointer to memory block object. |
    | --- | --- | --- |
    | [in] | in\_block | Address of the first required block to allocate |
    | [in] | count | Number of blocks to allocate. |

Return values
:   | 0 | Successful |
    | --- | --- |
    | -EINVAL | Invalid argument supplied. |
    | -ENOMEM | Some of blocks are taken and cannot be allocated |

## [◆ ](#ga7a8ff3370747ae382ed24ad7b8b34746)sys\_mem\_blocks\_is\_region\_free()

| int sys\_mem\_blocks\_is\_region\_free | ( | [sys\_mem\_blocks\_t](#ga5748df756d2f9aa10fddf2f39bf8a074) \* | *mem\_block*, |
| --- | --- | --- | --- |
|  |  | void \* | *in\_block*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *count* ) |

`#include <[mem_blocks.h](mem__blocks_8h.md)>`

check if the region is free

Parameters
:   | [in] | mem\_block | Pointer to memory block object. |
    | --- | --- | --- |
    | [in] | in\_block | Address of the first block to check |
    | [in] | count | Number of blocks to check. |

Return values
:   | 1 | All memory blocks are free |
    | --- | --- |
    | 0 | At least one of the memory blocks is taken |

## [◆ ](#ga03967e8b917a1592638586c9cfbba4bb)sys\_multi\_mem\_blocks\_add\_allocator()

| void sys\_multi\_mem\_blocks\_add\_allocator | ( | [sys\_multi\_mem\_blocks\_t](#ga00d9c0bafe800dffa3676d37983499a8) \* | *group*, |
| --- | --- | --- | --- |
|  |  | [sys\_mem\_blocks\_t](#ga5748df756d2f9aa10fddf2f39bf8a074) \* | *alloc* ) |

`#include <[mem_blocks.h](mem__blocks_8h.md)>`

Add an allocator to an allocator group.

This adds a known allocator to an existing multi memory blocks allocator group.

Parameters
:   | [group](structgroup.md "Group structure.") | Multi memory blocks allocator structure. |
    | --- | --- |
    | alloc | Allocator to add |

## [◆ ](#gafa96b1567b57c4466c9640fd1f5408b2)sys\_multi\_mem\_blocks\_alloc()

| int sys\_multi\_mem\_blocks\_alloc | ( | [sys\_multi\_mem\_blocks\_t](#ga00d9c0bafe800dffa3676d37983499a8) \* | *group*, |
| --- | --- | --- | --- |
|  |  | void \* | *cfg*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *count*, |
|  |  | void \*\* | *out\_blocks*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *blk\_size* ) |

`#include <[mem_blocks.h](mem__blocks_8h.md)>`

Allocate memory from multi memory blocks allocator group.

Just as for [sys\_mem\_blocks\_alloc()](#ga3e53a5c65bb0e88fbf20e66b016c1dff), allocates multiple blocks of memory. Takes an opaque configuration pointer passed to the choice function, which is used by integration code to choose an allocator.

Parameters
:   | [in] | [group](structgroup.md "Group structure.") | Multi memory blocks allocator structure. |
    | --- | --- | --- |
    | [in] | cfg | Opaque configuration parameter, as for [sys\_multi\_mem\_blocks\_choice\_fn\_t](#ga2e58484681d0d9629af9a8c7c14453d9) |
    | [in] | count | Number of blocks to allocate |
    | [out] | out\_blocks | Output array to be populated by pointers to the memory blocks. It must have at least `count` elements. |
    | [out] | blk\_size | If not NULL, output the block size of the chosen allocator. |

Return values
:   | 0 | Successful |
    | --- | --- |
    | -EINVAL | Invalid argument supplied, or no allocator chosen. |
    | -ENOMEM | Not enough blocks for allocation. |

## [◆ ](#ga8dedc28ed45e9e6350b584b1082b4d4f)sys\_multi\_mem\_blocks\_free()

| int sys\_multi\_mem\_blocks\_free | ( | [sys\_multi\_mem\_blocks\_t](#ga00d9c0bafe800dffa3676d37983499a8) \* | *group*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *count*, |
|  |  | void \*\* | *in\_blocks* ) |

`#include <[mem_blocks.h](mem__blocks_8h.md)>`

Free memory allocated from multi memory blocks allocator group.

Free previous allocated memory blocks from [sys\_multi\_mem\_blocks\_alloc()](#gafa96b1567b57c4466c9640fd1f5408b2).

Note that all blocks in `in_blocks` must be from the same allocator.

Parameters
:   | [in] | [group](structgroup.md "Group structure.") | Multi memory blocks allocator structure. |
    | --- | --- | --- |
    | [in] | count | Number of blocks to free. |
    | [in] | in\_blocks | Input array of pointers to the memory blocks. |

Return values
:   | 0 | Successful |
    | --- | --- |
    | -EINVAL | Invalid argument supplied, or no allocator chosen. |
    | -EFAULT | Invalid pointer(s) supplied. |

## [◆ ](#gad39867e3cd1e1e69e6fb3746c05abed0)sys\_multi\_mem\_blocks\_init()

| void sys\_multi\_mem\_blocks\_init | ( | [sys\_multi\_mem\_blocks\_t](#ga00d9c0bafe800dffa3676d37983499a8) \* | *group*, |
| --- | --- | --- | --- |
|  |  | [sys\_multi\_mem\_blocks\_choice\_fn\_t](#ga2e58484681d0d9629af9a8c7c14453d9) | *choice\_fn* ) |

`#include <[mem_blocks.h](mem__blocks_8h.md)>`

Initialize multi memory blocks allocator group.

Initialize a sys\_multi\_mem\_block struct with the specified choice function. Note that individual allocator must be added later with sys\_multi\_mem\_blocks\_add\_allocator.

Parameters
:   | [group](structgroup.md "Group structure.") | Multi memory blocks allocator structure. |
    | --- | --- |
    | choice\_fn | A [sys\_multi\_mem\_blocks\_choice\_fn\_t](#ga2e58484681d0d9629af9a8c7c14453d9) callback used to select the allocator to be used at allocation time |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
