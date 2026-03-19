---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stm32f10x__clock_8h_source.html
original_path: doxygen/html/stm32f10x__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32f10x\_clock.h

[Go to the documentation of this file.](stm32f10x__clock_8h.md)

1/\*

2 \* SPDX-License-Identifier: Apache-2.0

3 \*

4 \* Copyright (C) 2024, Joakim Andersson

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32F10X\_CLOCK\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32F10X\_CLOCK\_H\_

9

10#include "[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)"

11/\* Ensure correct order by including generic F1 definitions first. \*/

12#include "[stm32f1\_clock.h](stm32f1__clock_8h.md)"

13

15/\* Low speed clocks defined in stm32\_common\_clocks.h \*/

16/\* Common clocks with stm32f1x defined in stm32f1\_clock.h \*/

[ 17](stm32f10x__clock_8h.md#acabf91f55d604e7e6b3930d5fb4051c5)#define STM32\_SRC\_PLL2CLK (STM32\_SRC\_PLLCLK + 1)

[ 18](stm32f10x__clock_8h.md#ae5acc6d7e207c27d90f2e6d77fac9d5d)#define STM32\_SRC\_PLL3CLK (STM32\_SRC\_PLL2CLK + 1)

[ 19](stm32f10x__clock_8h.md#a3afc97af21308c71d21b59d53946efad)#define STM32\_SRC\_EXT\_HSE (STM32\_SRC\_PLL3CLK + 1)

20

22#undef MCO1\_SEL /\* Need to redefine generic F1 MCO\_SEL for connectivity line devices. \*/

[ 23](stm32f10x__clock_8h.md#acc5c7aed4e842ca212471d7a58504821)#define MCO1\_SEL(val) STM32\_MCO\_CFGR(val, 0xF, 24, CFGR1\_REG)

24/\* No MCO prescaler support on STM32F1 series. \*/

25

26#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32F10X\_CLOCK\_H\_ \*/

[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)

[stm32f1\_clock.h](stm32f1__clock_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32f10x\_clock.h](stm32f10x__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
