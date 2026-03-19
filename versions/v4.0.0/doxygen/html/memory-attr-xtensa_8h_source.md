---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/memory-attr-xtensa_8h_source.html
original_path: doxygen/html/memory-attr-xtensa_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

memory-attr-xtensa.h

[Go to the documentation of this file.](memory-attr-xtensa_8h.md)

1/\*

2 \* Copyright (c) 2023 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEM\_ATTR\_XTENSA\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEM\_ATTR\_XTENSA\_H\_

8

9#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

10#include <[zephyr/dt-bindings/memory-attr/memory-attr.h](memory-attr_8h.md)>

11

12/\*

13 \* Architecture specific Xtensa related attributes.

14 \*/

[ 15](memory-attr-xtensa_8h.md#a90663eb795734c0f1f8f7cdc50584d87)#define DT\_MEM\_XTENSA\_MASK DT\_MEM\_ARCH\_ATTR\_MASK

[ 16](memory-attr-xtensa_8h.md#aebb8ec5798ba120fd7f2c020a81349f4)#define DT\_MEM\_XTENSA\_GET(x) ((x) & DT\_MEM\_XTENSA\_MASK)

[ 17](memory-attr-xtensa_8h.md#a4d678d277f4a6dacf2057bae24c2d3c0)#define DT\_MEM\_XTENSA(x) ((x) << DT\_MEM\_ARCH\_ATTR\_SHIFT)

18

[ 19](memory-attr-xtensa_8h.md#a4698c95aff86fd63ba1e35b7b195fa07)#define ATTR\_XTENSA\_INSTR\_ROM BIT(0)

[ 20](memory-attr-xtensa_8h.md#a674b85213c6aee2f9078c45d5e21bff3)#define ATTR\_XTENSA\_INSTR\_RAM BIT(1)

[ 21](memory-attr-xtensa_8h.md#a22e41d116f0a78fc13ed4d3f344e2490)#define ATTR\_XTENSA\_DATA\_ROM BIT(2)

[ 22](memory-attr-xtensa_8h.md#ac22caa2071000be7deb736dd6340ac4c)#define ATTR\_XTENSA\_DATA\_RAM BIT(3)

[ 23](memory-attr-xtensa_8h.md#a2c2b3b4c4421e704ef7f015500a5fc53)#define ATTR\_XTENSA\_XLMI BIT(4)

24

[ 25](memory-attr-xtensa_8h.md#aa9a1851e86f36be439f024af0d998ee4)#define DT\_MEM\_XTENSA\_INSTR\_ROM DT\_MEM\_XTENSA(ATTR\_XTENSA\_INSTR\_ROM)

[ 26](memory-attr-xtensa_8h.md#a2566e023ccb0cb9529bc9b1d710d27c3)#define DT\_MEM\_XTENSA\_INSTR\_RAM DT\_MEM\_XTENSA(ATTR\_XTENSA\_INSTR\_RAM)

[ 27](memory-attr-xtensa_8h.md#a94f99c060768b249c055eb88bf551de8)#define DT\_MEM\_XTENSA\_DATA\_ROM DT\_MEM\_XTENSA(ATTR\_XTENSA\_DATA\_ROM)

[ 28](memory-attr-xtensa_8h.md#a3b64411ba4c118b0ef9058e3f8c9ebc8)#define DT\_MEM\_XTENSA\_DATA\_RAM DT\_MEM\_XTENSA(ATTR\_XTENSA\_DATA\_RAM)

[ 29](memory-attr-xtensa_8h.md#a9e63ac329fa36ad194865c40695bad09)#define DT\_MEM\_XTENSA\_XLMI DT\_MEM\_XTENSA(ATTR\_XTENSA\_XLMI)

[ 30](memory-attr-xtensa_8h.md#a272c0689cf885783d2c25598d9506eae)#define DT\_MEM\_XTENSA\_UNKNOWN DT\_MEM\_ARCH\_ATTR\_UNKNOWN

31

32#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEM\_ATTR\_XTENSA\_H\_ \*/

[memory-attr.h](memory-attr_8h.md)

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [memory-attr](dir_505b2faf98fd683dcb4dcae28f4fc25d.md)
- [memory-attr-xtensa.h](memory-attr-xtensa_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
