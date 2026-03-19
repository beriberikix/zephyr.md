---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32f3__clock_8h_source.html
original_path: doxygen/html/stm32f3__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32f3\_clock.h

[Go to the documentation of this file.](stm32f3__clock_8h.md)

1/\*

2 \* Copyright (c) 2022 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32F3\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32F3\_CLOCK\_H\_

8

9#include "[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)"

10

[ 12](stm32f3__clock_8h.md#a186de4b3566a20794e4483a9569abe3c)#define STM32\_CLOCK\_BUS\_AHB1 0x014

[ 13](stm32f3__clock_8h.md#adb7becb609763568b91303041c9cd4db)#define STM32\_CLOCK\_BUS\_APB2 0x018

[ 14](stm32f3__clock_8h.md#ac763945fc36124f9c978c423826faa95)#define STM32\_CLOCK\_BUS\_APB1 0x01c

15

[ 16](stm32f3__clock_8h.md#acc0577552371fcda95685f6424ecb4b2)#define STM32\_PERIPH\_BUS\_MIN STM32\_CLOCK\_BUS\_AHB1

[ 17](stm32f3__clock_8h.md#a561265772438ab8995251760c7f3dc30)#define STM32\_PERIPH\_BUS\_MAX STM32\_CLOCK\_BUS\_APB1

18

20/\* RM0316, §9.4.13 Clock configuration register (RCC\_CFGR3) \*/

21

23/\* Defined in stm32\_common\_clocks.h \*/

24

26/\* Low speed clocks defined in stm32\_common\_clocks.h \*/

[ 27](stm32f3__clock_8h.md#a7bc1dd03186b763b407a044ddffb4ab2)#define STM32\_SRC\_HSI (STM32\_SRC\_LSI + 1)

28/\* #define STM32\_SRC\_HSI48 TDB \*/

[ 30](stm32f3__clock_8h.md#a6cd4e305697f314401e5654b4dd5f25d)#define STM32\_SRC\_PCLK (STM32\_SRC\_HSI + 1)

[ 32](stm32f3__clock_8h.md#a4353a5ed9fb962c65382c60186c40c05)#define STM32\_SRC\_PLLCLK (STM32\_SRC\_PCLK + 1)

33

[ 35](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3)#define CFGR\_REG 0x04

[ 36](stm32f3__clock_8h.md#a949ab0a4140278eb878cd5f9f3809a00)#define CFGR3\_REG 0x30

37

[ 39](stm32f3__clock_8h.md#a70a10f70b4f5058508e8983ad0a4de3a)#define BDCR\_REG 0x20

40

[ 43](stm32f3__clock_8h.md#a2d34d604e16d874235b74bdbc8103bed)#define I2S\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 23, CFGR\_REG)

[ 44](stm32f3__clock_8h.md#acc5c7aed4e842ca212471d7a58504821)#define MCO1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 24, CFGR\_REG)

[ 45](stm32f3__clock_8h.md#a2805cf7e0b5ed0a9bb4bfff863327081)#define MCO1\_PRE(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 28, CFGR\_REG)

[ 47](stm32f3__clock_8h.md#a17f3ec5f86995a2c4087f2988a9486c5)#define USART1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 0, CFGR3\_REG)

[ 48](stm32f3__clock_8h.md#a3fbef8f2542fc6921236bd2709acf64c)#define I2C1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 4, CFGR3\_REG)

[ 49](stm32f3__clock_8h.md#abdd79c9ce90458b53e81123d181fed98)#define I2C2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 5, CFGR3\_REG)

[ 50](stm32f3__clock_8h.md#aa12a1d2ac790880b7148d1e5660eb941)#define I2C3\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 6, CFGR3\_REG)

[ 51](stm32f3__clock_8h.md#a72d364c49d3cb708b3b522240c7f2487)#define TIM1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 8, CFGR3\_REG)

[ 52](stm32f3__clock_8h.md#a4265e0738cb6943d25db9a1425529034)#define TIM8\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 9, CFGR3\_REG)

[ 53](stm32f3__clock_8h.md#aec6c3536cdaa8545becc5d4575947ee1)#define TIM15\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 10, CFGR3\_REG)

[ 54](stm32f3__clock_8h.md#accdaf25454de23be65aa2865389c9c3d)#define TIM16\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 11, CFGR3\_REG)

[ 55](stm32f3__clock_8h.md#a584d523b64f1a5d31e44ba0ddb24a189)#define TIM17\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 13, CFGR3\_REG)

[ 56](stm32f3__clock_8h.md#a0044430b188b9104418943111be2cc01)#define TIM20\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 15, CFGR3\_REG)

[ 57](stm32f3__clock_8h.md#ad67d92dfc439018a7a231e661d10d7f9)#define USART2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 16, CFGR3\_REG)

[ 58](stm32f3__clock_8h.md#ad2f356c0bc0e43d6f629cdb840846526)#define USART3\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 18, CFGR3\_REG)

[ 59](stm32f3__clock_8h.md#aced9e983095cb40bc18f3a66e3818c98)#define USART4\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 20, CFGR3\_REG)

[ 60](stm32f3__clock_8h.md#a6a45e0ef8bd196574e241aefdb3a5350)#define USART5\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 22, CFGR3\_REG)

[ 61](stm32f3__clock_8h.md#ae9e7ae1c9e0378ef4ec0d435d4449a16)#define TIM2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 24, CFGR3\_REG)

[ 62](stm32f3__clock_8h.md#abc0a25466b329ed2797a6f223f7c7e3a)#define TIM3\_4\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 25, CFGR3\_REG)

[ 64](stm32f3__clock_8h.md#a4836377699efa295c56d340e150695b0)#define RTC\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 8, BDCR\_REG)

65

66#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32F3\_CLOCK\_H\_ \*/

[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32f3\_clock.h](stm32f3__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
