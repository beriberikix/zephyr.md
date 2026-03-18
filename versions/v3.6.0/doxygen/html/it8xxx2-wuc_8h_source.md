---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/it8xxx2-wuc_8h_source.html
original_path: doxygen/html/it8xxx2-wuc_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

it8xxx2-wuc.h

[Go to the documentation of this file.](it8xxx2-wuc_8h.md)

1/\*

2 \* Copyright (c) 2022 ITE Corporation. All Rights Reserved.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_IT8XXX2\_WUC\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_IT8XXX2\_WUC\_H\_

9

10#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

11

[ 13](it8xxx2-wuc_8h.md#a61868a556512e102778c74ea81c0583f)#define IT8XXX2\_WUC\_UNUSED\_REG 0

14

[ 20](it8xxx2-wuc_8h.md#a679ab1940f920cfe6c0fa1d5ed14a468)#define WUC\_TYPE\_EDGE\_RISING BIT(0)

[ 22](it8xxx2-wuc_8h.md#a21b4240f97f62e69f23ea614de699955)#define WUC\_TYPE\_EDGE\_FALLING BIT(1)

[ 24](it8xxx2-wuc_8h.md#a824c451f35efc9b287cd694a0c674095)#define WUC\_TYPE\_EDGE\_BOTH (WUC\_TYPE\_EDGE\_RISING | WUC\_TYPE\_EDGE\_FALLING)

25

27

28#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_IT8XXX2\_WUC\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [it8xxx2-wuc.h](it8xxx2-wuc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
