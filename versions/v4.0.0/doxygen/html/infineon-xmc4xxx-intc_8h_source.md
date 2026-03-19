---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/infineon-xmc4xxx-intc_8h_source.html
original_path: doxygen/html/infineon-xmc4xxx-intc_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

infineon-xmc4xxx-intc.h

[Go to the documentation of this file.](infineon-xmc4xxx-intc_8h.md)

1/\*

2 \* Copyright (c) 2022 Schlumberger

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_INFINEON\_XMC4XXX\_INTC\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_INFINEON\_XMC4XXX\_INTC\_H\_

9

[ 10](infineon-xmc4xxx-intc_8h.md#ab656d7c0db9ceac360de0e3bb11e05c8)#define XMC4XXX\_INTC\_PORT\_POS 0

[ 11](infineon-xmc4xxx-intc_8h.md#a0874a1bfc7a1590132fb5802fb490791)#define XMC4XXX\_INTC\_PORT\_MASK 0xf

12

[ 13](infineon-xmc4xxx-intc_8h.md#aa5617e14917f6cedae4ab8db3eafa250)#define XMC4XXX\_INTC\_PIN\_POS 4

[ 14](infineon-xmc4xxx-intc_8h.md#aa8feb63e6eb01cbc5b9226ffdc499f0f)#define XMC4XXX\_INTC\_PIN\_MASK 0xf

15

[ 16](infineon-xmc4xxx-intc_8h.md#aa20a96b7bec4cbbf75cf879cf448a379)#define XMC4XXX\_INTC\_LINE\_POS 8

[ 17](infineon-xmc4xxx-intc_8h.md#a2cae357860189d1b94dce0ee4a3867e0)#define XMC4XXX\_INTC\_LINE\_MASK 0x7

18

[ 19](infineon-xmc4xxx-intc_8h.md#a9b1fa99740e6196ae816c3d89eaf8588)#define XMC4XXX\_INTC\_ERU\_SRC\_POS 11

[ 20](infineon-xmc4xxx-intc_8h.md#a95edfadbd314bf4ea27d88b1dce66e35)#define XMC4XXX\_INTC\_ERU\_SRC\_MASK 0x7

21

[ 22](infineon-xmc4xxx-intc_8h.md#a908ab6f538ea2a135d002b9c4d9bdea0)#define XMC4XXX\_INTC\_GET\_PORT(mx) ((mx >> XMC4XXX\_INTC\_PORT\_POS) & XMC4XXX\_INTC\_PORT\_MASK)

[ 23](infineon-xmc4xxx-intc_8h.md#a415130dd3eeae518bb469122bfb44223)#define XMC4XXX\_INTC\_GET\_PIN(mx) ((mx >> XMC4XXX\_INTC\_PIN\_POS) & XMC4XXX\_INTC\_PIN\_MASK)

[ 24](infineon-xmc4xxx-intc_8h.md#a7ff570440afc268c833d4991c58792d2)#define XMC4XXX\_INTC\_GET\_LINE(mx) ((mx >> XMC4XXX\_INTC\_LINE\_POS) & XMC4XXX\_INTC\_LINE\_MASK)

[ 25](infineon-xmc4xxx-intc_8h.md#afe9fae2864cfa87bc9a458c24d6bdc5e)#define XMC4XXX\_INTC\_GET\_ERU\_SRC(mx) ((mx >> XMC4XXX\_INTC\_ERU\_SRC\_POS) & XMC4XXX\_INTC\_ERU\_SRC\_MASK)

26

[ 27](infineon-xmc4xxx-intc_8h.md#ac7cbe5628158a8852ea3ea8fafd4e2b1)#define XMC4XXX\_INTC\_SET\_LINE\_MAP(port, pin, eru\_src, line) \

28 ((port) << XMC4XXX\_INTC\_PORT\_POS | (pin) << XMC4XXX\_INTC\_PIN\_POS | \

29 (eru\_src) << XMC4XXX\_INTC\_ERU\_SRC\_POS | (line) << XMC4XXX\_INTC\_LINE\_POS)

30

31#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_INFINEON\_XMC4XXX\_INTC\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [infineon-xmc4xxx-intc.h](infineon-xmc4xxx-intc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
