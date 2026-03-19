---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/memory-attr-sw_8h_source.html
original_path: doxygen/html/memory-attr-sw_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

memory-attr-sw.h

[Go to the documentation of this file.](memory-attr-sw_8h.md)

1/\*

2 \* Copyright (c) 2023 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEM\_ATTR\_SW\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEM\_ATTR\_SW\_H\_

8

9#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

10#include <[zephyr/dt-bindings/memory-attr/memory-attr.h](memory-attr_8h.md)>

11

12/\*

13 \* Software specific memory attributes.

14 \*/

[ 15](memory-attr-sw_8h.md#a35cd6e6c03a9304267a6a33edaae65b8)#define DT\_MEM\_SW\_MASK DT\_MEM\_SW\_ATTR\_MASK

[ 16](memory-attr-sw_8h.md#ad6c8b22aa5dc6c5bb8abd5c3ed297478)#define DT\_MEM\_SW\_GET(x) ((x) & DT\_MEM\_SW\_ATTR\_MASK)

[ 17](memory-attr-sw_8h.md#ad7c4ae7ee3908612be90ef166d417881)#define DT\_MEM\_SW(x) ((x) << DT\_MEM\_SW\_ATTR\_SHIFT)

18

[ 19](memory-attr-sw_8h.md#adccfc787238048f59167e5913bf74e41)#define ATTR\_SW\_ALLOC\_CACHE BIT(0)

[ 20](memory-attr-sw_8h.md#af308d88c0732fb69e96577c594ca1a48)#define ATTR\_SW\_ALLOC\_NON\_CACHE BIT(1)

[ 21](memory-attr-sw_8h.md#a92d7fb61ed72428bfaf9d397fb6c32c6)#define ATTR\_SW\_ALLOC\_DMA BIT(2)

22

[ 23](memory-attr-sw_8h.md#a616d67585f6370117e5e341861b0baad)#define DT\_MEM\_SW\_ALLOC\_CACHE DT\_MEM\_SW(ATTR\_SW\_ALLOC\_CACHE)

[ 24](memory-attr-sw_8h.md#aa1dbfaea4961ee2545831d585ba0c710)#define DT\_MEM\_SW\_ALLOC\_NON\_CACHE DT\_MEM\_SW(ATTR\_SW\_ALLOC\_NON\_CACHE)

[ 25](memory-attr-sw_8h.md#a308104aa9d2ef98de2d024e7186e35b8)#define DT\_MEM\_SW\_ALLOC\_DMA DT\_MEM\_SW(ATTR\_SW\_ALLOC\_DMA)

26

27#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEM\_ATTR\_SW\_H\_ \*/

[memory-attr.h](memory-attr_8h.md)

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [memory-attr](dir_505b2faf98fd683dcb4dcae28f4fc25d.md)
- [memory-attr-sw.h](memory-attr-sw_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
