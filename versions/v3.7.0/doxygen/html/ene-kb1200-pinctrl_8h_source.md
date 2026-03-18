---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ene-kb1200-pinctrl_8h_source.html
original_path: doxygen/html/ene-kb1200-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ene-kb1200-pinctrl.h

[Go to the documentation of this file.](ene-kb1200-pinctrl_8h.md)

1/\*

2 \* Copyright (c) ENE Technology Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ENE\_KB1200\_PINCTRL\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ENE\_KB1200\_PINCTRL\_H\_

9

10#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

11

[ 12](ene-kb1200-pinctrl_8h.md#ab5585e56327f2b23ec89ba9debba0ee2)#define PINMUX\_FUNC\_GPIO 0x00

[ 13](ene-kb1200-pinctrl_8h.md#a98cfa6f81cd2d924b4b8410cc58dcced)#define PINMUX\_FUNC\_A 0x00

[ 14](ene-kb1200-pinctrl_8h.md#a1f94697f2a9f866e751fad5fa50ac54a)#define PINMUX\_FUNC\_B 0x01

[ 15](ene-kb1200-pinctrl_8h.md#ad65d0f30a98080f3e21e2db0d6f63e90)#define PINMUX\_FUNC\_C 0x02

[ 16](ene-kb1200-pinctrl_8h.md#abcab76c799f9fefa55d8814c820f212a)#define PINMUX\_FUNC\_D 0x03

[ 17](ene-kb1200-pinctrl_8h.md#a74d6d35ca16164b0a0b68ee271b16e0d)#define PINMUX\_FUNC\_MAX 0x04

18

[ 19](ene-kb1200-pinctrl_8h.md#a4079f1e59701aa562027b6ad1656caad)#define ENE\_KB1200\_NO\_PUD\_POS 12

[ 20](ene-kb1200-pinctrl_8h.md#a49849bc4e85bd82ebc9bb4d14dd2668c)#define ENE\_KB1200\_PD\_POS 13

[ 21](ene-kb1200-pinctrl_8h.md#af4297d42dd80877ce174a3d855df01b6)#define ENE\_KB1200\_PU\_POS 14

[ 22](ene-kb1200-pinctrl_8h.md#a2fd07082dd0f55f0fcb33847476d52b1)#define ENE\_KB1200\_PUSH\_PULL\_POS 15

[ 23](ene-kb1200-pinctrl_8h.md#af0eeb505113d97cdbe2afa0436718829)#define ENE\_KB1200\_OPEN\_DRAIN\_POS 16

[ 24](ene-kb1200-pinctrl_8h.md#ae7915329e0bf4a3961fdcf3a3bd706ac)#define ENE\_KB1200\_OUT\_DIS\_POS 17

[ 25](ene-kb1200-pinctrl_8h.md#af87d58a86781f6db2b698aeb598d8f80)#define ENE\_KB1200\_OUT\_EN\_POS 18

[ 26](ene-kb1200-pinctrl_8h.md#ae7289ea9757e87dba5eca26b0d8ea869)#define ENE\_KB1200\_OUT\_HI\_POS 19

[ 27](ene-kb1200-pinctrl_8h.md#a31048a09bc76aa17796ac29093c94c17)#define ENE\_KB1200\_OUT\_LO\_POS 20

[ 28](ene-kb1200-pinctrl_8h.md#ab68aefd0fa096ce5541f07d4b65881c0)#define ENE\_KB1200\_PIN\_LOW\_POWER\_POS 21

29

[ 30](ene-kb1200-pinctrl_8h.md#ade268ffe7669879fbef2c7bf4600ffc2)#define ENE\_KB1200\_PINMUX\_PORT\_POS 5

[ 31](ene-kb1200-pinctrl_8h.md#ad673befbb525dba683cc65b64fdd3abd)#define ENE\_KB1200\_PINMUX\_PORT\_MSK 0x7

[ 32](ene-kb1200-pinctrl_8h.md#abee9ef573bd89f90dc1bc2d65cfb2507)#define ENE\_KB1200\_PINMUX\_PIN\_POS 0

[ 33](ene-kb1200-pinctrl_8h.md#ac1666ff38512cea6f97afc30b22dda0f)#define ENE\_KB1200\_PINMUX\_PIN\_MSK 0x1f

[ 34](ene-kb1200-pinctrl_8h.md#aff29cfeb36d2bb8a9ac5792b30f6c627)#define ENE\_KB1200\_PINMUX\_FUNC\_POS 8

[ 35](ene-kb1200-pinctrl_8h.md#aa077424a43590e43f9067f3ab0a655ff)#define ENE\_KB1200\_PINMUX\_FUNC\_MSK 0xf

36

37/\*

38 \* f is function number

39 \* b[7:5] = pin bank

40 \* b[4:0] = pin position in bank

41 \* b[11:8] = function

42 \*/

[ 43](ene-kb1200-pinctrl_8h.md#a2c86608b7173b6e66f3e55015035a41b)#define ENE\_KB1200\_PINMUX(n, f) \

44 (((((n) >> 5) & ENE\_KB1200\_PINMUX\_PORT\_MSK) << ENE\_KB1200\_PINMUX\_PORT\_POS) | \

45 (((n) & ENE\_KB1200\_PINMUX\_PIN\_MSK) << ENE\_KB1200\_PINMUX\_PIN\_POS) | \

46 (((f) & ENE\_KB1200\_PINMUX\_FUNC\_MSK) << ENE\_KB1200\_PINMUX\_FUNC\_POS))

47

48#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ENE\_KB1200\_PINCTRL\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [ene-kb1200-pinctrl.h](ene-kb1200-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
