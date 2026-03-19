---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/silabs-pinctrl-siwx91x_8h_source.html
original_path: doxygen/html/silabs-pinctrl-siwx91x_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

silabs-pinctrl-siwx91x.h

[Go to the documentation of this file.](silabs-pinctrl-siwx91x_8h.md)

1/\*

2 \* Copyright (c) 2024 Silicon Laboratories Inc.

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef INCLUDE\_ZEPHYR\_DT\_BINDINGS\_PINCTRL\_SILABS\_PINCTRL\_SIWX91X\_H\_

7#define INCLUDE\_ZEPHYR\_DT\_BINDINGS\_PINCTRL\_SILABS\_PINCTRL\_SIWX91X\_H\_

8

9#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

10

11#if !defined(FIELD\_PREP)

12/\* Upstream does not make these macros available to DeviceTree \*/

[ 13](silabs-pinctrl-siwx91x_8h.md#a92235ab2e350fbdc01ddf0f894e5e4c0)#define LSB\_GET(value) ((value) & -(value))

[ 14](silabs-pinctrl-siwx91x_8h.md#aa49a456f06f7bdbedfcf3517e461947e)#define FIELD\_GET(mask, value) (((value) & (mask)) / LSB\_GET(mask))

[ 15](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)#define FIELD\_PREP(mask, value) (((value) \* LSB\_GET(mask)) & (mask))

16#endif

17

[ 18](silabs-pinctrl-siwx91x_8h.md#a50d5c19898298b48138dbd1e35a1789d)#define SIWX91X\_PINCTRL\_PORT\_MASK 0x0000000FUL

[ 19](silabs-pinctrl-siwx91x_8h.md#a7ccfd879f82aa28433bb31b86861a6b3)#define SIWX91X\_PINCTRL\_PIN\_MASK 0x000000F0UL

[ 20](silabs-pinctrl-siwx91x_8h.md#a6c1b75f5d3e9c46c74a5bd67161f23d6)#define SIWX91X\_PINCTRL\_ULPPIN\_MASK 0x00000F00UL

[ 21](silabs-pinctrl-siwx91x_8h.md#a2f7374a4ef333a2972e406a826e2f697)#define SIWX91X\_PINCTRL\_MODE\_MASK 0x0003F000UL

[ 22](silabs-pinctrl-siwx91x_8h.md#a6d3ea759c0a75addbe3495b9817fa90a)#define SIWX91X\_PINCTRL\_ULPMODE\_MASK 0x00FC0000UL

[ 23](silabs-pinctrl-siwx91x_8h.md#a9a5fa9fa0c3d65eae582fedd3585cd0d)#define SIWX91X\_PINCTRL\_PAD\_MASK 0xFF000000UL

24

25/\* Declare an integer representing the pinctrl/gpio state of a signal on SiWx91x.

26 \* @param mode HP GPIO mode, 0xFF if HP GPIO mux isn't used

27 \* @param ulpmode ULP GPIO mode, 0xFF if ULP GPIO mux isn't used

28 \* @param pad HP pad number, 0xFF if HP pad isn't used, 0 if host pad

29 \* @param port GPIO port number (0-4)

30 \* @param pin HP GPIO pin number, value is unused if mode is 0xFF

31 \* @param ulppin ULP GPIO pin number, value is unused if ulpmode is 0xFF

32 \*/

[ 33](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)#define SIWX91X\_GPIO(mode, ulpmode, pad, port, pin, ulppin) \

34 (FIELD\_PREP(SIWX91X\_PINCTRL\_PORT\_MASK, port) | FIELD\_PREP(SIWX91X\_PINCTRL\_PIN\_MASK, pin) | \

35 FIELD\_PREP(SIWX91X\_PINCTRL\_ULPPIN\_MASK, ulppin) | \

36 FIELD\_PREP(SIWX91X\_PINCTRL\_MODE\_MASK, mode) | \

37 FIELD\_PREP(SIWX91X\_PINCTRL\_ULPMODE\_MASK, ulpmode) | \

38 FIELD\_PREP(SIWX91X\_PINCTRL\_PAD\_MASK, pad))

39

40#endif /\* INCLUDE\_ZEPHYR\_DT\_BINDINGS\_PINCTRL\_SILABS\_PINCTRL\_SIWX91X\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [silabs-pinctrl-siwx91x.h](silabs-pinctrl-siwx91x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
