---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/stm32f427__clock_8h_source.html
original_path: doxygen/html/stm32f427__clock_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32f427\_clock.h

[Go to the documentation of this file.](stm32f427__clock_8h.md)

1/\*

2 \* Copyright (c) 2023 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32F427\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32F427\_CLOCK\_H\_

8

[ 10](stm32f427__clock_8h.md#af74c2b28a777155a9cf8c8f457b8da36)#define DCKCFGR\_REG 0x8C

11

[ 14](stm32f427__clock_8h.md#a0d2c702f898f3c1d387ff326f55f00df)#define CKDFSDM2A\_SEL(val) STM32\_CLOCK(val, 1, 14, DCKCFGR\_REG)

[ 15](stm32f427__clock_8h.md#a716c5e5a49ad72a1a372e1731383bbe7)#define CKDFSDM1A\_SEL(val) STM32\_CLOCK(val, 1, 15, DCKCFGR\_REG)

[ 16](stm32f427__clock_8h.md#a2462f0bc95f94819a2936e6018e1e92a)#define SAI1A\_SEL(val) STM32\_CLOCK(val, 3, 20, DCKCFGR\_REG)

[ 17](stm32f427__clock_8h.md#a3fb1995fff0878225d9557dffeb16210)#define SAI1B\_SEL(val) STM32\_CLOCK(val, 3, 22, DCKCFGR\_REG)

[ 18](stm32f427__clock_8h.md#a4b6468847f959179fffc020d5d14439c)#define CLK48M\_SEL(val) STM32\_CLOCK(val, 1, 27, DCKCFGR\_REG)

[ 19](stm32f427__clock_8h.md#a42688c1d17e09ab58029feedd7491c0b)#define SDMMC\_SEL(val) STM32\_CLOCK(val, 1, 28, DCKCFGR\_REG)

[ 20](stm32f427__clock_8h.md#a2e82c24eb0c9e22635966752eebb2a05)#define DSI\_SEL(val) STM32\_CLOCK(val, 1, 29, DCKCFGR\_REG)

21

22#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32F427\_CLOCK\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32f427\_clock.h](stm32f427__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
