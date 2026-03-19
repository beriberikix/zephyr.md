---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sys__heap_8h.html
original_path: doxygen/html/sys__heap_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sys\_heap.h File Reference

`#include <stddef.h>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/mem_stats.h](mem__stats_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`

[Go to the source code of this file.](sys__heap_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sys\_heap](structsys__heap.md) |

| Macros | |
| --- | --- |
| #define | [sys\_heap\_realloc](group__low__level__heap__allocator.md#ga0b6c4f17521a4ea996f5abf15883737a)(heap, ptr, bytes) |

| Functions | |
| --- | --- |
| void | [sys\_heap\_init](group__low__level__heap__allocator.md#ga520768606a3c28b084cf11f8ec82fae6) (struct [sys\_heap](structsys__heap.md) \*heap, void \*mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Initialize [sys\_heap](structsys__heap.md). |
| void \* | [sys\_heap\_alloc](group__low__level__heap__allocator.md#ga6b8bdf02c9be5576fddbe711904a3aad) (struct [sys\_heap](structsys__heap.md) \*heap, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Allocate memory from a [sys\_heap](structsys__heap.md). |
| void \* | [sys\_heap\_aligned\_alloc](group__low__level__heap__allocator.md#ga92a973158860c6863e1aba8516311076) (struct [sys\_heap](structsys__heap.md) \*heap, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Allocate aligned memory from a [sys\_heap](structsys__heap.md). |
| void | [sys\_heap\_free](group__low__level__heap__allocator.md#gab654da64adf74e67ae12f263eb420560) (struct [sys\_heap](structsys__heap.md) \*heap, void \*mem) |
|  | Free memory into a [sys\_heap](structsys__heap.md). |
| void \* | [sys\_heap\_aligned\_realloc](group__low__level__heap__allocator.md#ga16e1408c3ad5541daac756e46b33b612) (struct [sys\_heap](structsys__heap.md) \*heap, void \*ptr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Expand the size of an existing allocation. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [sys\_heap\_usable\_size](group__low__level__heap__allocator.md#gaf8cb77365c04022181e2fc45e3fbce4a) (struct [sys\_heap](structsys__heap.md) \*heap, void \*mem) |
|  | Return allocated memory size. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_heap\_validate](group__low__level__heap__allocator.md#ga81de9cc56f9fb88ae12ea70cc85d1db1) (struct [sys\_heap](structsys__heap.md) \*heap) |
|  | Validate heap integrity. |
| void | [sys\_heap\_stress](group__low__level__heap__allocator.md#gae2f307f7b25e4927d3dbe650567b6308) (void \*(\*alloc\_fn)(void \*arg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes), void(\*free\_fn)(void \*arg, void \*p), void \*arg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) total\_bytes, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) op\_count, void \*scratch\_mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) scratch\_bytes, int target\_percent, struct z\_heap\_stress\_result \*result) |
|  | [sys\_heap](structsys__heap.md) stress test rig |
| void | [sys\_heap\_print\_info](group__low__level__heap__allocator.md#gaf36db704bd892b657ccaa7a4cebc45e5) (struct [sys\_heap](structsys__heap.md) \*heap, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) dump\_chunks) |
|  | Print heap internal structure information to the console. |
| int | [sys\_heap\_array\_save](group__low__level__heap__allocator.md#gabb384fcc481e46051938b7b83efa1770) (struct [sys\_heap](structsys__heap.md) \*heap) |
|  | Save the heap pointer. |
| int | [sys\_heap\_array\_get](group__low__level__heap__allocator.md#ga4b528274c83766c28748ffa7b4b9631b) (struct [sys\_heap](structsys__heap.md) \*\*\*heap) |
|  | Get the array of saved heap pointers. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [sys\_heap.h](sys__heap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
