---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mem__blocks_8h.html
original_path: doxygen/html/mem__blocks_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mem\_blocks.h File Reference

Memory Blocks Allocator.
[More...](#details)

`#include <stddef.h>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/math/ilog2.h](ilog2_8h_source.md)>`  
`#include <[zephyr/sys/bitarray.h](bitarray_8h_source.md)>`  
`#include <[zephyr/sys/mem_stats.h](mem__stats_8h_source.md)>`

[Go to the source code of this file.](mem__blocks_8h_source.md)

| Macros | |
| --- | --- |
| #define | [MAX\_MULTI\_ALLOCATORS](#a0a18ac0266ab6532cdd93302ca012112)   8 |
| #define | [SYS\_MEM\_BLOCKS\_DEFINE](group__mem__blocks__apis.md#gab49fdcd86522d318051ca6a6ddf41c7c)(name, blk\_sz, num\_blks, buf\_align) |
|  | Create a memory block object with a new backing buffer. |
| #define | [SYS\_MEM\_BLOCKS\_DEFINE\_STATIC](group__mem__blocks__apis.md#gaa6b90846448323837dab3a17c3065359)(name, blk\_sz, num\_blks, buf\_align) |
|  | Create a static memory block object with a new backing buffer. |
| #define | [SYS\_MEM\_BLOCKS\_DEFINE\_WITH\_EXT\_BUF](group__mem__blocks__apis.md#gae6b688b2925308c9007071bab681dcdd)(name, blk\_sz, num\_blks, buf) |
|  | Create a memory block object with a providing backing buffer. |
| #define | [SYS\_MEM\_BLOCKS\_DEFINE\_STATIC\_WITH\_EXT\_BUF](group__mem__blocks__apis.md#gaad3cfb34553bd97290b388bec910b8cc)(name, blk\_sz, num\_blks, buf) |
|  | Create a static memory block object with a providing backing buffer. |

| Typedefs | |
| --- | --- |
| typedef struct sys\_mem\_blocks | [sys\_mem\_blocks\_t](group__mem__blocks__apis.md#ga5748df756d2f9aa10fddf2f39bf8a074) |
|  | Memory Blocks Allocator. |
| typedef struct sys\_multi\_mem\_blocks | [sys\_multi\_mem\_blocks\_t](group__mem__blocks__apis.md#ga00d9c0bafe800dffa3676d37983499a8) |
|  | Multi Memory Blocks Allocator. |
| typedef [sys\_mem\_blocks\_t](group__mem__blocks__apis.md#ga5748df756d2f9aa10fddf2f39bf8a074) \*(\* | [sys\_multi\_mem\_blocks\_choice\_fn\_t](group__mem__blocks__apis.md#ga2e58484681d0d9629af9a8c7c14453d9)) (struct sys\_multi\_mem\_blocks \*group, void \*cfg) |
|  | Multi memory blocks allocator choice function. |

| Functions | |
| --- | --- |
| int | [sys\_mem\_blocks\_alloc](group__mem__blocks__apis.md#ga3e53a5c65bb0e88fbf20e66b016c1dff) ([sys\_mem\_blocks\_t](group__mem__blocks__apis.md#ga5748df756d2f9aa10fddf2f39bf8a074) \*mem\_block, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count, void \*\*out\_blocks) |
|  | Allocate multiple memory blocks. |
| int | [sys\_mem\_blocks\_alloc\_contiguous](group__mem__blocks__apis.md#ga72614d0c120f40209837b77d0333bb23) ([sys\_mem\_blocks\_t](group__mem__blocks__apis.md#ga5748df756d2f9aa10fddf2f39bf8a074) \*mem\_block, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count, void \*\*out\_block) |
|  | Allocate a contiguous set of memory blocks. |
| int | [sys\_mem\_blocks\_get](group__mem__blocks__apis.md#ga0ae169fbe2b3d3a68815ba0898ef5338) ([sys\_mem\_blocks\_t](group__mem__blocks__apis.md#ga5748df756d2f9aa10fddf2f39bf8a074) \*mem\_block, void \*in\_block, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count) |
|  | Force allocation of a specified blocks in a memory block object. |
| int | [sys\_mem\_blocks\_is\_region\_free](group__mem__blocks__apis.md#ga7a8ff3370747ae382ed24ad7b8b34746) ([sys\_mem\_blocks\_t](group__mem__blocks__apis.md#ga5748df756d2f9aa10fddf2f39bf8a074) \*mem\_block, void \*in\_block, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count) |
|  | check if the region is free |
| int | [sys\_mem\_blocks\_free](group__mem__blocks__apis.md#gadd799f4f2423277ed5daf08a0d150b9c) ([sys\_mem\_blocks\_t](group__mem__blocks__apis.md#ga5748df756d2f9aa10fddf2f39bf8a074) \*mem\_block, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count, void \*\*in\_blocks) |
|  | Free multiple memory blocks. |
| int | [sys\_mem\_blocks\_free\_contiguous](group__mem__blocks__apis.md#ga39e7f8dfe3bda8eabc2372f9a1e87342) ([sys\_mem\_blocks\_t](group__mem__blocks__apis.md#ga5748df756d2f9aa10fddf2f39bf8a074) \*mem\_block, void \*block, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count) |
|  | Free contiguous multiple memory blocks. |
| void | [sys\_multi\_mem\_blocks\_init](group__mem__blocks__apis.md#gad39867e3cd1e1e69e6fb3746c05abed0) ([sys\_multi\_mem\_blocks\_t](group__mem__blocks__apis.md#ga00d9c0bafe800dffa3676d37983499a8) \*group, [sys\_multi\_mem\_blocks\_choice\_fn\_t](group__mem__blocks__apis.md#ga2e58484681d0d9629af9a8c7c14453d9) choice\_fn) |
|  | Initialize multi memory blocks allocator group. |
| void | [sys\_multi\_mem\_blocks\_add\_allocator](group__mem__blocks__apis.md#ga03967e8b917a1592638586c9cfbba4bb) ([sys\_multi\_mem\_blocks\_t](group__mem__blocks__apis.md#ga00d9c0bafe800dffa3676d37983499a8) \*group, [sys\_mem\_blocks\_t](group__mem__blocks__apis.md#ga5748df756d2f9aa10fddf2f39bf8a074) \*alloc) |
|  | Add an allocator to an allocator group. |
| int | [sys\_multi\_mem\_blocks\_alloc](group__mem__blocks__apis.md#gafa96b1567b57c4466c9640fd1f5408b2) ([sys\_multi\_mem\_blocks\_t](group__mem__blocks__apis.md#ga00d9c0bafe800dffa3676d37983499a8) \*group, void \*cfg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count, void \*\*out\_blocks, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*blk\_size) |
|  | Allocate memory from multi memory blocks allocator group. |
| int | [sys\_multi\_mem\_blocks\_free](group__mem__blocks__apis.md#ga8dedc28ed45e9e6350b584b1082b4d4f) ([sys\_multi\_mem\_blocks\_t](group__mem__blocks__apis.md#ga00d9c0bafe800dffa3676d37983499a8) \*group, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count, void \*\*in\_blocks) |
|  | Free memory allocated from multi memory blocks allocator group. |

## Detailed Description

Memory Blocks Allocator.

## Macro Definition Documentation

## [◆ ](#a0a18ac0266ab6532cdd93302ca012112)MAX\_MULTI\_ALLOCATORS

| #define MAX\_MULTI\_ALLOCATORS   8 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [mem\_blocks.h](mem__blocks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
