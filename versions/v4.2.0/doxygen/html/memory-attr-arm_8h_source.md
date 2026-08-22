---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/memory-attr-arm_8h_source.html
original_path: doxygen/html/memory-attr-arm_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

memory-attr-arm.h

[Go to the documentation of this file.](memory-attr-arm_8h.md)

1/\*

2 \* Copyright (c) 2023 Carlo Caione <ccaione@baylibre.com>

3 \* Copyright 2025 Arm Limited and/or its affiliates <open-source-office@arm.com>

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEM\_ATTR\_ARM\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEM\_ATTR\_ARM\_H\_

9

10#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

11#include <[zephyr/dt-bindings/memory-attr/memory-attr.h](memory-attr_8h.md)>

12

13/\*

14 \* Architecture specific ARM MPU related attributes.

15 \*

16 \* This list is to seamlessly support the MPU regions configuration using DT and

17 \* the `zephyr,memory-attr` property.

18 \*

19 \* This is legacy and it should NOT be extended further. If new MPU region

20 \* types must be added, these must rely on the generic memory attributes.

21 \*/

[ 22](memory-attr-arm_8h.md#a9a01f8cd34e900d2074c23bec1020bf1)#define DT\_MEM\_ARM\_MASK DT\_MEM\_ARCH\_ATTR\_MASK

[ 23](memory-attr-arm_8h.md#ac9237bf43ea0801606a72bb1aa408952)#define DT\_MEM\_ARM\_GET(x) ((x) & DT\_MEM\_ARM\_MASK)

[ 24](memory-attr-arm_8h.md#a4676991c272cbdae9890dc320a827a11)#define DT\_MEM\_ARM(x) ((x) << DT\_MEM\_ARCH\_ATTR\_SHIFT)

25

[ 26](memory-attr-arm_8h.md#a7da536df6516679b7256651cd76a3ce0)#define ATTR\_MPU\_RAM BIT(0)

[ 27](memory-attr-arm_8h.md#a0539bc3fbc9a9ed421869b7a88bc01bf)#define ATTR\_MPU\_RAM\_NOCACHE BIT(1)

[ 28](memory-attr-arm_8h.md#a42ee73c11a945c9d636a3806d5bf7eb6)#define ATTR\_MPU\_FLASH BIT(2)

[ 29](memory-attr-arm_8h.md#a5d7a78767be0cff6b4c6523761cf3055)#define ATTR\_MPU\_PPB BIT(3)

[ 30](memory-attr-arm_8h.md#ac5fd54c9e182c46e6d48cd94713fb164)#define ATTR\_MPU\_IO BIT(4)

[ 31](memory-attr-arm_8h.md#ac7e9b3c506fd8ba0170c248cb681e347)#define ATTR\_MPU\_EXTMEM BIT(5)

[ 32](memory-attr-arm_8h.md#a8c878a0e159ceb6ac78a188b1a5ad659)#define ATTR\_MPU\_RAM\_PXN BIT(6)

33

[ 34](memory-attr-arm_8h.md#ab3669734951faa3f55f85db9fe005daa)#define DT\_MEM\_ARM\_MPU\_RAM DT\_MEM\_ARM(ATTR\_MPU\_RAM)

[ 35](memory-attr-arm_8h.md#af60fb9c11ef84238647855f52a338904)#define DT\_MEM\_ARM\_MPU\_RAM\_NOCACHE DT\_MEM\_ARM(ATTR\_MPU\_RAM\_NOCACHE)

[ 36](memory-attr-arm_8h.md#a2bc421f5582d90604dc95b796a475221)#define DT\_MEM\_ARM\_MPU\_FLASH DT\_MEM\_ARM(ATTR\_MPU\_FLASH)

[ 37](memory-attr-arm_8h.md#a7b0f983bdde1aab0cf703006aa79c363)#define DT\_MEM\_ARM\_MPU\_PPB DT\_MEM\_ARM(ATTR\_MPU\_PPB)

[ 38](memory-attr-arm_8h.md#a21a8d85ff9c329bb4ebd9f9f4a9b2e9c)#define DT\_MEM\_ARM\_MPU\_IO DT\_MEM\_ARM(ATTR\_MPU\_IO)

[ 39](memory-attr-arm_8h.md#add7dd0c9f14a8696d1827d3d5bfbb263)#define DT\_MEM\_ARM\_MPU\_EXTMEM DT\_MEM\_ARM(ATTR\_MPU\_EXTMEM)

[ 40](memory-attr-arm_8h.md#aee3d2c7c52a670df6d18fb7f336cbe9c)#define DT\_MEM\_ARM\_MPU\_RAM\_PXN DT\_MEM\_ARM(ATTR\_MPU\_RAM\_PXN)

[ 41](memory-attr-arm_8h.md#ab24037ec20705fdf979d453046cd979a)#define DT\_MEM\_ARM\_MPU\_UNKNOWN DT\_MEM\_ARCH\_ATTR\_UNKNOWN

42

43#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEM\_ATTR\_ARM\_H\_ \*/

[memory-attr.h](memory-attr_8h.md)

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [memory-attr](dir_505b2faf98fd683dcb4dcae28f4fc25d.md)
- [memory-attr-arm.h](memory-attr-arm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
