---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stm32f410__clock_8h_source.html
original_path: doxygen/html/stm32f410__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32f410\_clock.h

[Go to the documentation of this file.](stm32f410__clock_8h.md)

1/\*

2 \* Copyright (c) 2023 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32F410\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32F410\_CLOCK\_H\_

8

[ 10](stm32f410__clock_8h.md#af74c2b28a777155a9cf8c8f457b8da36)#define DCKCFGR\_REG 0x8C

[ 11](stm32f410__clock_8h.md#a3a648b98a1f91abbce18297038ba3e5f)#define DCKCFGR2\_REG 0x94

12

[ 15](stm32f410__clock_8h.md#a0d2c702f898f3c1d387ff326f55f00df)#define CKDFSDM2A\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 1, 14, DCKCFGR\_REG)

[ 16](stm32f410__clock_8h.md#a716c5e5a49ad72a1a372e1731383bbe7)#define CKDFSDM1A\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 1, 15, DCKCFGR\_REG)

[ 17](stm32f410__clock_8h.md#a2462f0bc95f94819a2936e6018e1e92a)#define SAI1A\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 20, DCKCFGR\_REG)

[ 18](stm32f410__clock_8h.md#a3fb1995fff0878225d9557dffeb16210)#define SAI1B\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 22, DCKCFGR\_REG)

[ 19](stm32f410__clock_8h.md#abee394167f826cac3ec58db3e89dd092)#define I2S1\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 25, DCKCFGR\_REG)

[ 20](stm32f410__clock_8h.md#a00a15803773ade4655e63cc48b8e59ea)#define I2S2\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 27, DCKCFGR\_REG)

[ 21](stm32f410__clock_8h.md#a62f4679935575cef0f3c40b48494be49)#define CKDFSDM\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 1, 31, DCKCFGR\_REG)

22

[ 24](stm32f410__clock_8h.md#a8a02c7d6228c992585fc8275751121d4)#define I2CFMP1\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 22, DCKCFGR2\_REG)

[ 25](stm32f410__clock_8h.md#a9629b95b8e2c432e890c69727b52a4d4)#define CK48M\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 1, 27, DCKCFGR2\_REG)

[ 26](stm32f410__clock_8h.md#a9dbb3de5ec91ea2898c73fa87817af67)#define SDIO\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 1, 28, DCKCFGR2\_REG)

[ 27](stm32f410__clock_8h.md#a042804bf8a52b3dd28033f8814442bfb)#define LPTIM1\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 30, DCKCFGR2\_REG)

28

29/\* F4 generic I2S\_SEL is not compatible with F410 devices \*/

30#ifdef I2S\_SEL

31#undef I2S\_SEL

32#endif

33

34#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32F410\_CLOCK\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32f410\_clock.h](stm32f410__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
