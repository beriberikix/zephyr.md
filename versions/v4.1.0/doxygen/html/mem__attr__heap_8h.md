---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mem__attr__heap_8h.html
original_path: doxygen/html/mem__attr__heap_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mem\_attr\_heap.h File Reference

`#include <[zephyr/mem_mgmt/mem_attr.h](mem__attr_8h_source.md)>`

[Go to the source code of this file.](mem__attr__heap_8h_source.md)

| Functions | |
| --- | --- |
| int | [mem\_attr\_heap\_pool\_init](group__memory__attr__heap.md#ga85301dfc19493a84e89f965ed793d576) (void) |
|  | Init the memory pool. |
| void \* | [mem\_attr\_heap\_alloc](group__memory__attr__heap.md#gac03747a12f19735fc1a66d324b19f367) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) attr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Allocate memory with a specified attribute and size. |
| void \* | [mem\_attr\_heap\_aligned\_alloc](group__memory__attr__heap.md#ga6ef058b960a23ae8c0e57a71f5518dab) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) attr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Allocate aligned memory with a specified attribute, size and alignment. |
| void | [mem\_attr\_heap\_free](group__memory__attr__heap.md#ga2a7ef3301abfdd263d86f529dc1ea0f8) (void \*block) |
|  | Free the allocated memory. |
| const struct [mem\_attr\_region\_t](structmem__attr__region__t.md) \* | [mem\_attr\_heap\_get\_region](group__memory__attr__heap.md#gac0d2db398f90a5bc76677c23552fba99) (void \*addr) |
|  | Get a specific memory region descriptor for a provided address. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mem\_mgmt](dir_5ee27bc867ccb4004a26ac2b9a5fc96f.md)
- [mem\_attr\_heap.h](mem__attr__heap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
