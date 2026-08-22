---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/bflb__bl60x__clock_8h_source.html
original_path: doxygen/html/bflb__bl60x__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bflb\_bl60x\_clock.h

[Go to the documentation of this file.](bflb__bl60x__clock_8h.md)

1/\*

2 \* Copyright (c) 2025 MASSDRIVER EI (massdriver.space)

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_BFLB\_BL60X\_CLOCK\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_BFLB\_BL60X\_CLOCK\_H\_

9

10#include "[bflb\_clock\_common.h](bflb__clock__common_8h.md)"

11

[ 12](bflb__bl60x__clock_8h.md#aeacd7c41a31cecf69b9a9a78d67736a2)#define BL60X\_CLKID\_CLK\_ROOT BFLB\_CLKID\_CLK\_ROOT

[ 13](bflb__bl60x__clock_8h.md#accf2556fddba4992a60cf336291751cd)#define BL60X\_CLKID\_CLK\_RC32M BFLB\_CLKID\_CLK\_RC32M

[ 14](bflb__bl60x__clock_8h.md#a8fe00248514b4c133f8551163c433eee)#define BL60X\_CLKID\_CLK\_CRYSTAL BFLB\_CLKID\_CLK\_CRYSTAL

[ 15](bflb__bl60x__clock_8h.md#aa0eef44026316125a2583b82469c218c)#define BL60X\_CLKID\_CLK\_BCLK BFLB\_CLKID\_CLK\_BCLK

[ 16](bflb__bl60x__clock_8h.md#a529098e27dfab5df2ef931c90e14b6fe)#define BL60X\_CLKID\_CLK\_PLL 4

17

[ 18](bflb__bl60x__clock_8h.md#adb1c50774a143abc7a8f559e4b2206ee)#define BL60X\_PLL\_48MHz 0

[ 19](bflb__bl60x__clock_8h.md#ab92ca02f476bb7591a3d00d78a8ae550)#define BL60X\_PLL\_120MHz 1

[ 20](bflb__bl60x__clock_8h.md#a362f074d57af0b7fdd50357bee5b9278)#define BL60X\_PLL\_160MHz 2

[ 21](bflb__bl60x__clock_8h.md#a2c853319aeeb8418933cca735f86f78a)#define BL60X\_PLL\_192MHz 3

22

23#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_BFLB\_BL60X\_CLOCK\_H\_ \*/

[bflb\_clock\_common.h](bflb__clock__common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [bflb\_bl60x\_clock.h](bflb__bl60x__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
