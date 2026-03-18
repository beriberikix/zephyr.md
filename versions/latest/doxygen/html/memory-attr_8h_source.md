---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/memory-attr_8h_source.html
original_path: doxygen/html/memory-attr_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

memory-attr.h

[Go to the documentation of this file.](memory-attr_8h.md)

1/\*

2 \* Copyright (c) 2023 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEM\_ATTR\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEM\_ATTR\_H\_

8

9#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

10

11/\*

12 \* Generic memory attributes.

13 \*

14 \* Generic memory attributes that should be common to all architectures.

15 \*/

[ 16](memory-attr_8h.md#adf502f055c516d85610d8a9b5bb7e546)#define DT\_MEM\_ATTR\_MASK GENMASK(15, 0)

[ 17](memory-attr_8h.md#a971bc033e3971ff32aec78a917590f1a)#define DT\_MEM\_ATTR\_GET(x) ((x) & DT\_MEM\_ATTR\_MASK)

[ 18](memory-attr_8h.md#ada810aa72a8c0f34fcab7ffe3a3a582e)#define DT\_MEM\_ATTR\_SHIFT (0)

19

[ 20](memory-attr_8h.md#a74b1e3dceed92cf63ed018e971c89573)#define DT\_MEM\_CACHEABLE BIT(0) /\* cacheable \*/

[ 21](memory-attr_8h.md#a6090422ffdac9177b6a6528b3ea4cc77)#define DT\_MEM\_NON\_VOLATILE BIT(1) /\* non-volatile \*/

[ 22](memory-attr_8h.md#a2d0c09a13622358e4ef50da93455e5dd)#define DT\_MEM\_OOO BIT(2) /\* out-of-order \*/

[ 23](memory-attr_8h.md#a292b651c06018870fb199b61eb2a20e3)#define DT\_MEM\_DMA BIT(3) /\* DMA-able \*/

[ 24](memory-attr_8h.md#acedd7086cb2240a69896611c58a654a1)#define DT\_MEM\_UNKNOWN BIT(15) /\* must be last \*/

25/\* to be continued \*/

26

27/\*

28 \* Software specific memory attributes.

29 \*

30 \* Software can define their own memory attributes if needed using the

31 \* provided mask.

32 \*/

[ 33](memory-attr_8h.md#a2020f22247371f4200f9968f75ac9bcb)#define DT\_MEM\_SW\_ATTR\_MASK GENMASK(19, 16)

[ 34](memory-attr_8h.md#a05f246d5ab8ac568eb4174584d543c56)#define DT\_MEM\_SW\_ATTR\_GET(x) ((x) & DT\_MEM\_SW\_ATTR\_MASK)

[ 35](memory-attr_8h.md#a0586962ab2fa5990de15ea20c727f224)#define DT\_MEM\_SW\_ATTR\_SHIFT (16)

[ 36](memory-attr_8h.md#ae3f39518836c19ee2616f0ad11fda5dc)#define DT\_MEM\_SW\_ATTR\_UNKNOWN BIT(19)

37

38/\*

39 \* Architecture specific memory attributes.

40 \*

41 \* Architectures can define their own memory attributes if needed using the

42 \* provided mask.

43 \*

44 \* See for example `include/zephyr/dt-bindings/memory-attr/memory-attr-arm.h`

45 \*/

[ 46](memory-attr_8h.md#aa180a5da02572a4fe600573e2521abbe)#define DT\_MEM\_ARCH\_ATTR\_MASK GENMASK(31, 20)

[ 47](memory-attr_8h.md#a5c56e38ef80dc9feb6f3353cac1ddbdf)#define DT\_MEM\_ARCH\_ATTR\_GET(x) ((x) & DT\_MEM\_ARCH\_ATTR\_MASK)

[ 48](memory-attr_8h.md#a06e4088178d1ec01ec5cafe289c8eebe)#define DT\_MEM\_ARCH\_ATTR\_SHIFT (20)

[ 49](memory-attr_8h.md#aaefc7bf33d8fa6d5151338cd23b84474)#define DT\_MEM\_ARCH\_ATTR\_UNKNOWN BIT(31)

50

51#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEM\_ATTR\_H\_ \*/

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [memory-attr](dir_505b2faf98fd683dcb4dcae28f4fc25d.md)
- [memory-attr.h](memory-attr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
