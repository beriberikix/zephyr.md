---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ene-kb106x-pinctrl_8h_source.html
original_path: doxygen/html/ene-kb106x-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ene-kb106x-pinctrl.h

[Go to the documentation of this file.](ene-kb106x-pinctrl_8h.md)

1/\*

2 \* Copyright (c) ENE Technology Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ENE\_KB106X\_PINCTRL\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ENE\_KB106X\_PINCTRL\_H\_

9

10#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

11

[ 12](ene-kb106x-pinctrl_8h.md#ab5585e56327f2b23ec89ba9debba0ee2)#define PINMUX\_FUNC\_GPIO 0x00

[ 13](ene-kb106x-pinctrl_8h.md#a98cfa6f81cd2d924b4b8410cc58dcced)#define PINMUX\_FUNC\_A 0x00

[ 14](ene-kb106x-pinctrl_8h.md#a1f94697f2a9f866e751fad5fa50ac54a)#define PINMUX\_FUNC\_B 0x01

[ 15](ene-kb106x-pinctrl_8h.md#ad65d0f30a98080f3e21e2db0d6f63e90)#define PINMUX\_FUNC\_C 0x02

[ 16](ene-kb106x-pinctrl_8h.md#abcab76c799f9fefa55d8814c820f212a)#define PINMUX\_FUNC\_D 0x03

[ 17](ene-kb106x-pinctrl_8h.md#a74d6d35ca16164b0a0b68ee271b16e0d)#define PINMUX\_FUNC\_MAX 0x04

18

[ 19](ene-kb106x-pinctrl_8h.md#abac4bfb212bc96557b44d5f912939202)#define ENE\_KB106X\_NO\_PUD\_POS 12

[ 20](ene-kb106x-pinctrl_8h.md#a3d996e8da6fd27b2e409f95d60c6d969)#define ENE\_KB106X\_PD\_POS 13

[ 21](ene-kb106x-pinctrl_8h.md#ae8011d97ae2c4a1626a5c060c75be8da)#define ENE\_KB106X\_PU\_POS 14

[ 22](ene-kb106x-pinctrl_8h.md#a2ba1fa41dfd21090130f7ae0849ccb9a)#define ENE\_KB106X\_PUSH\_PULL\_POS 15

[ 23](ene-kb106x-pinctrl_8h.md#a88576538346e2c249ef5307487619dce)#define ENE\_KB106X\_OPEN\_DRAIN\_POS 16

[ 24](ene-kb106x-pinctrl_8h.md#a969b0d246bc93d27662806924490134b)#define ENE\_KB106X\_OUT\_DIS\_POS 17

[ 25](ene-kb106x-pinctrl_8h.md#a57c26614d9fe66812dfdd6addc57e724)#define ENE\_KB106X\_OUT\_EN\_POS 18

[ 26](ene-kb106x-pinctrl_8h.md#a5a6ed3b1af11083f5f424a47280369f5)#define ENE\_KB106X\_OUT\_HI\_POS 19

[ 27](ene-kb106x-pinctrl_8h.md#a61b2e54a54dee416d674fb71fe450319)#define ENE\_KB106X\_OUT\_LO\_POS 20

[ 28](ene-kb106x-pinctrl_8h.md#aad562cc00835aa70b1ebfc0d73cacb87)#define ENE\_KB106X\_PIN\_LOW\_POWER\_POS 21

[ 29](ene-kb106x-pinctrl_8h.md#a040e843e147d311107bc2217440a3feb)#define ENE\_KB106X\_IN\_DIS\_POS 22

[ 30](ene-kb106x-pinctrl_8h.md#af66fd6f73d773180f6b4c2a5e55d2ee7)#define ENE\_KB106X\_IN\_EN\_POS 23

[ 31](ene-kb106x-pinctrl_8h.md#a7fda7bb531cdddc3c040352b33c6bc34)#define ENE\_KB106X\_DRIVING\_POS 31

32

[ 33](ene-kb106x-pinctrl_8h.md#a87c5ce1628625ff0bf8ab57e58c952a3)#define ENE\_KB106X\_PINMUX\_PORT\_POS 5

[ 34](ene-kb106x-pinctrl_8h.md#a14853b5c05a4c4d8a70ac2b257a0e2b2)#define ENE\_KB106X\_PINMUX\_PORT\_MSK 0x7

[ 35](ene-kb106x-pinctrl_8h.md#afe8dfa7a9f85d9bff0a3a066fbd5b4be)#define ENE\_KB106X\_PINMUX\_PIN\_POS 0

[ 36](ene-kb106x-pinctrl_8h.md#a48b9755d0765d1a78b259a7864e966f2)#define ENE\_KB106X\_PINMUX\_PIN\_MSK 0x1f

[ 37](ene-kb106x-pinctrl_8h.md#a02262fa6f75e8574b61f65cc94eaa233)#define ENE\_KB106X\_PINMUX\_FUNC\_POS 8

[ 38](ene-kb106x-pinctrl_8h.md#a744daeb1e891195cf3735ffb7440f746)#define ENE\_KB106X\_PINMUX\_FUNC\_MSK 0xf

39

[ 40](ene-kb106x-pinctrl_8h.md#a346c95084c7edb51010f04201c298205)#define ENE\_KB106X\_EXTENDED\_BANK 0x80

41

42/\*

43 \* f is function number

44 \* b[7:5] = pin bank

45 \* b[4:0] = pin position in bank

46 \* b[11:8] = function

47 \*/

[ 48](ene-kb106x-pinctrl_8h.md#a2df12498c98fe54610bf619d68f76a55)#define ENE\_KB106X\_PINMUX(n, f) \

49 (((((n) >> 5) & ENE\_KB106X\_PINMUX\_PORT\_MSK) << ENE\_KB106X\_PINMUX\_PORT\_POS) | \

50 (((n) & ENE\_KB106X\_PINMUX\_PIN\_MSK) << ENE\_KB106X\_PINMUX\_PIN\_POS) | \

51 (((f) & ENE\_KB106X\_PINMUX\_FUNC\_MSK) << ENE\_KB106X\_PINMUX\_FUNC\_POS))

52

53#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ENE\_KB106X\_PINCTRL\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [ene-kb106x-pinctrl.h](ene-kb106x-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
