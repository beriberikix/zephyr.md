---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/max32-pinctrl_8h_source.html
original_path: doxygen/html/max32-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

max32-pinctrl.h

[Go to the documentation of this file.](max32-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2023-2024 Analog Devices, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_MAX32\_PINCTRL\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_MAX32\_PINCTRL\_H\_

9

[ 13](max32-pinctrl_8h.md#a7087cd825f7f43739fa57ce0a4e4297d)#define MAX32\_MODE\_GPIO 0x00

[ 14](max32-pinctrl_8h.md#a4e3439dc886a1ed097d698847ab3cb92)#define MAX32\_MODE\_AF1 0x01

[ 15](max32-pinctrl_8h.md#af4e13cd1ef71b77ae882aadb467e5115)#define MAX32\_MODE\_AF2 0x02

[ 16](max32-pinctrl_8h.md#a33afd156fac8c0ccb588230b3f787947)#define MAX32\_MODE\_AF3 0x03

[ 17](max32-pinctrl_8h.md#a6112caaab6ce78c337c40adfa1977a90)#define MAX32\_MODE\_AF4 0x04

[ 18](max32-pinctrl_8h.md#aae02581685aaeb495a8ea2bbabe0999b)#define MAX32\_MODE\_AF5 0x05

19

[ 23](max32-pinctrl_8h.md#ac45646bd5514a406cbb87dc24a3a2f4c)#define MAX32\_MODE\_SHIFT 0U

[ 24](max32-pinctrl_8h.md#a071a95ac6147954a5b9086cc27f02ce0)#define MAX32\_MODE\_MASK 0x0FU

[ 25](max32-pinctrl_8h.md#ad103d747f01d57dc2cbc547fde45c988)#define MAX32\_PORT\_SHIFT 4U

[ 26](max32-pinctrl_8h.md#a668dddf52782f061e623e8d0837ba513)#define MAX32\_PORT\_MASK 0x0FU

[ 27](max32-pinctrl_8h.md#aa3b3d363ef790d1def3402ceb47b2f97)#define MAX32\_PIN\_SHIFT 8U

[ 28](max32-pinctrl_8h.md#abf4c75ee139d0abcc10ab3c4fe116ae2)#define MAX32\_PIN\_MASK 0xFFU

29

[ 43](max32-pinctrl_8h.md#a6af2b3feddf92906fe3ba315b8debc41)#define MAX32\_PINMUX(port, pin, mode) \

44 ((((port)&MAX32\_PORT\_MASK) << MAX32\_PORT\_SHIFT) | \

45 (((pin)&MAX32\_PIN\_MASK) << MAX32\_PIN\_SHIFT) | \

46 (((MAX32\_MODE\_##mode) & MAX32\_MODE\_MASK) << MAX32\_MODE\_SHIFT))

47

[ 48](max32-pinctrl_8h.md#a9e2b0cc6ad6fb0e043f805be98900cad)#define MAX32\_PINMUX\_PORT(pinmux) (((pinmux) >> MAX32\_PORT\_SHIFT) & MAX32\_PORT\_MASK)

[ 49](max32-pinctrl_8h.md#ae9b72f2da84eca73ba5d0958946d2d6e)#define MAX32\_PINMUX\_PIN(pinmux) (((pinmux) >> MAX32\_PIN\_SHIFT) & MAX32\_PIN\_MASK)

[ 50](max32-pinctrl_8h.md#a1f3ef03ff93e7fe57781eb831aaf5afb)#define MAX32\_PINMUX\_MODE(pinmux) (((pinmux) >> MAX32\_MODE\_SHIFT) & MAX32\_MODE\_MASK)

51

52/\* Selects the voltage rail used for the pin \*/

[ 53](max32-pinctrl_8h.md#a4e18fd313d30f6f69376cd769ea2347c)#define MAX32\_VSEL\_VDDIO 0

[ 54](max32-pinctrl_8h.md#a6c2d4fea363165d857f5a79608d52aa0)#define MAX32\_VSEL\_VDDIOH 1

55

[ 59](max32-pinctrl_8h.md#a05fd9141c140ccf54d0723a3511d0c9b)#define MAX32\_INPUT\_ENABLE\_SHIFT 0x00

[ 60](max32-pinctrl_8h.md#a6ffa10ef6074415084575c88a12069cc)#define MAX32\_BIAS\_PULL\_UP\_SHIFT 0x01

[ 61](max32-pinctrl_8h.md#afa7dd8f4020995627e8b9f2ee60316bd)#define MAX32\_BIAS\_PULL\_DOWN\_SHIFT 0x02

[ 62](max32-pinctrl_8h.md#a3f1a5cd6c9da2ad726155b40a9cea865)#define MAX32\_OUTPUT\_ENABLE\_SHIFT 0x03

[ 63](max32-pinctrl_8h.md#a88dcd8d7eee992eecd0e430a667d3353)#define MAX32\_POWER\_SOURCE\_SHIFT 0x04

[ 64](max32-pinctrl_8h.md#aa8cf639ff885ef23a51857b56bc6f113)#define MAX32\_OUTPUT\_HIGH\_SHIFT 0x05

[ 65](max32-pinctrl_8h.md#a1082e5021dc5bcceb337a6286c3d69a2)#define MAX32\_DRV\_STRENGTH\_SHIFT 0x06 /\* 2 bits \*/

[ 66](max32-pinctrl_8h.md#a41e4cdd4682a676f295de9d728ba6455)#define MAX32\_DRV\_STRENGTH\_MASK 0x03

67

68#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_MAX32\_PINCTRL\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [max32-pinctrl.h](max32-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
