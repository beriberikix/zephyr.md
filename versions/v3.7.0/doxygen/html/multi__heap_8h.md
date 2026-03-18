---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/multi__heap_8h.html
original_path: doxygen/html/multi__heap_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

multi\_heap.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](multi__heap_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sys\_multi\_heap\_rec](structsys__multi__heap__rec.md) |
| struct | [sys\_multi\_heap](structsys__multi__heap.md) |

| Macros | |
| --- | --- |
| #define | [MAX\_MULTI\_HEAPS](#a4baed7cc76ab2037f126508a48bf4b09)   8 |

| Typedefs | |
| --- | --- |
| typedef void \*(\* | [sys\_multi\_heap\_fn\_t](group__multi__heap__wrapper.md#ga2d8ac07e590ef36ba6f35ae88235564e)) (struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap, void \*cfg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Multi-heap choice function. |

| Functions | |
| --- | --- |
| void | [sys\_multi\_heap\_init](group__multi__heap__wrapper.md#ga50ded513b50c7aed7d89386bb8f425cc) (struct [sys\_multi\_heap](structsys__multi__heap.md) \*heap, [sys\_multi\_heap\_fn\_t](group__multi__heap__wrapper.md#ga2d8ac07e590ef36ba6f35ae88235564e) choice\_fn) |
|  | Initialize multi-heap. |
| void | [sys\_multi\_heap\_add\_heap](group__multi__heap__wrapper.md#gacd6b92e8090a56e1eb59a18166d659d1) (struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap, struct [sys\_heap](structsys__heap.md) \*heap, void \*user\_data) |
|  | Add [sys\_heap](structsys__heap.md) to multi heap. |
| void \* | [sys\_multi\_heap\_alloc](group__multi__heap__wrapper.md#ga050d7499b982ed62f85d5fc15f79548b) (struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap, void \*cfg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Allocate memory from multi heap. |
| void \* | [sys\_multi\_heap\_aligned\_alloc](group__multi__heap__wrapper.md#ga9f958dbfa86e12236b8e356375b8d04c) (struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap, void \*cfg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Allocate aligned memory from multi heap. |
| const struct [sys\_multi\_heap\_rec](structsys__multi__heap__rec.md) \* | [sys\_multi\_heap\_get\_heap](group__multi__heap__wrapper.md#gad98b78be5c0ed50e1e0715a15c289b3a) (const struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap, void \*addr) |
|  | Get a specific heap for provided address. |
| void | [sys\_multi\_heap\_free](group__multi__heap__wrapper.md#gac6f913a3bbf247807ba80408a242db73) (struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap, void \*block) |
|  | Free memory allocated from multi heap. |

## Macro Definition Documentation

## [◆ ](#a4baed7cc76ab2037f126508a48bf4b09)MAX\_MULTI\_HEAPS

| #define MAX\_MULTI\_HEAPS   8 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [multi\_heap.h](multi__heap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
