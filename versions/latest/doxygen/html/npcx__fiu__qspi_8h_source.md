---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/npcx__fiu__qspi_8h_source.html
original_path: doxygen/html/npcx__fiu__qspi_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

npcx\_fiu\_qspi.h

[Go to the documentation of this file.](npcx__fiu__qspi_8h.md)

1/\*

2 \* Copyright (c) 2023 Nuvoton Technology Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NPCK\_FIU\_QSPI\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NPCK\_FIU\_QSPI\_H\_

8

9#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

10

11/\* Software controlled Chip-Select number for UMA transactions \*/

[ 12](npcx__fiu__qspi_8h.md#ab2702585eae967c9749836860a1475b9)#define NPCX\_QSPI\_SW\_CS0 BIT(0)

[ 13](npcx__fiu__qspi_8h.md#a8273de16e9b279e5fbfe63db34d398cb)#define NPCX\_QSPI\_SW\_CS1 BIT(1)

[ 14](npcx__fiu__qspi_8h.md#a146d0d39da877413dd09637ef4243414)#define NPCX\_QSPI\_SW\_CS2 BIT(2)

[ 15](npcx__fiu__qspi_8h.md#abe20f1ebc30af0e7d951a35d7dc4261e)#define NPCX\_QSPI\_SW\_CS\_MASK (NPCX\_QSPI\_SW\_CS0 | NPCX\_QSPI\_SW\_CS1 | NPCX\_QSPI\_SW\_CS2)

16

17/\* Supported flash interfaces for UMA transactions \*/

[ 18](npcx__fiu__qspi_8h.md#a48455b5bf574e67c6463c69ebb8b348b)#define NPCX\_QSPI\_SEC\_FLASH\_SL BIT(4)

19

20/\* Supported read mode for Direct Read Access \*/

[ 21](npcx__fiu__qspi_8h.md#a2197dbcc86f29bb20e8445e52a31d18b)#define NPCX\_RD\_MODE\_NORMAL 0

[ 22](npcx__fiu__qspi_8h.md#aef0c37fff59a0b1c17c495d2be6f3665)#define NPCX\_RD\_MODE\_FAST 1

[ 23](npcx__fiu__qspi_8h.md#a9b766e793cc32a60785b93385752085d)#define NPCX\_RD\_MODE\_FAST\_DUAL 3

24

25#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NPCK\_FIU\_QSPI\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [flash\_controller](dir_cd262f46d6d541746154471716dc2a72.md)
- [npcx\_fiu\_qspi.h](npcx__fiu__qspi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
