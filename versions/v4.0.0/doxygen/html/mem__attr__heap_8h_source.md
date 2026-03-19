---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mem__attr__heap_8h_source.html
original_path: doxygen/html/mem__attr__heap_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mem\_attr\_heap.h

[Go to the documentation of this file.](mem__attr__heap_8h.md)

1/\*

2 \* Copyright (c) 2023 Carlo Caione, <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_MEM\_ATTR\_HEAP\_H\_

8#define ZEPHYR\_INCLUDE\_MEM\_ATTR\_HEAP\_H\_

9

16

17#include <[zephyr/mem\_mgmt/mem\_attr.h](mem__attr_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

[ 33](group__memory__attr__heap.md#ga85301dfc19493a84e89f965ed793d576)int [mem\_attr\_heap\_pool\_init](group__memory__attr__heap.md#ga85301dfc19493a84e89f965ed793d576)(void);

34

[ 48](group__memory__attr__heap.md#gac03747a12f19735fc1a66d324b19f367)void \*[mem\_attr\_heap\_alloc](group__memory__attr__heap.md#gac03747a12f19735fc1a66d324b19f367)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) attr, size\_t bytes);

49

[ 64](group__memory__attr__heap.md#ga6ef058b960a23ae8c0e57a71f5518dab)void \*[mem\_attr\_heap\_aligned\_alloc](group__memory__attr__heap.md#ga6ef058b960a23ae8c0e57a71f5518dab)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) attr, size\_t align, size\_t bytes);

65

[ 76](group__memory__attr__heap.md#ga2a7ef3301abfdd263d86f529dc1ea0f8)void [mem\_attr\_heap\_free](group__memory__attr__heap.md#ga2a7ef3301abfdd263d86f529dc1ea0f8)(void \*block);

77

[ 88](group__memory__attr__heap.md#gac0d2db398f90a5bc76677c23552fba99)const struct [mem\_attr\_region\_t](structmem__attr__region__t.md) \*[mem\_attr\_heap\_get\_region](group__memory__attr__heap.md#gac0d2db398f90a5bc76677c23552fba99)(void \*addr);

89

90#ifdef \_\_cplusplus

91}

92#endif

93

97

98#endif /\* ZEPHYR\_INCLUDE\_MEM\_ATTR\_HEAP\_H\_ \*/

[mem\_attr\_heap\_free](group__memory__attr__heap.md#ga2a7ef3301abfdd263d86f529dc1ea0f8)

void mem\_attr\_heap\_free(void \*block)

Free the allocated memory.

[mem\_attr\_heap\_aligned\_alloc](group__memory__attr__heap.md#ga6ef058b960a23ae8c0e57a71f5518dab)

void \* mem\_attr\_heap\_aligned\_alloc(uint32\_t attr, size\_t align, size\_t bytes)

Allocate aligned memory with a specified attribute, size and alignment.

[mem\_attr\_heap\_pool\_init](group__memory__attr__heap.md#ga85301dfc19493a84e89f965ed793d576)

int mem\_attr\_heap\_pool\_init(void)

Init the memory pool.

[mem\_attr\_heap\_alloc](group__memory__attr__heap.md#gac03747a12f19735fc1a66d324b19f367)

void \* mem\_attr\_heap\_alloc(uint32\_t attr, size\_t bytes)

Allocate memory with a specified attribute and size.

[mem\_attr\_heap\_get\_region](group__memory__attr__heap.md#gac0d2db398f90a5bc76677c23552fba99)

const struct mem\_attr\_region\_t \* mem\_attr\_heap\_get\_region(void \*addr)

Get a specific memory region descriptor for a provided address.

[mem\_attr.h](mem__attr_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[mem\_attr\_region\_t](structmem__attr__region__t.md)

memory-attr region structure.

**Definition** mem\_attr.h:56

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mem\_mgmt](dir_5ee27bc867ccb4004a26ac2b9a5fc96f.md)
- [mem\_attr\_heap.h](mem__attr__heap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
