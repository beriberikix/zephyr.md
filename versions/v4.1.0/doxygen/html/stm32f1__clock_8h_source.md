---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32f1__clock_8h_source.html
original_path: doxygen/html/stm32f1__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32f1\_clock.h

[Go to the documentation of this file.](stm32f1__clock_8h.md)

1/\*

2 \* Copyright (c) 2022 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32F1\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32F1\_CLOCK\_H\_

8

9#include "[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)"

10

12

[ 14](stm32f1__clock_8h.md#a186de4b3566a20794e4483a9569abe3c)#define STM32\_CLOCK\_BUS\_AHB1 0x014

[ 15](stm32f1__clock_8h.md#adb7becb609763568b91303041c9cd4db)#define STM32\_CLOCK\_BUS\_APB2 0x018

[ 16](stm32f1__clock_8h.md#ac763945fc36124f9c978c423826faa95)#define STM32\_CLOCK\_BUS\_APB1 0x01c

17

[ 18](stm32f1__clock_8h.md#acc0577552371fcda95685f6424ecb4b2)#define STM32\_PERIPH\_BUS\_MIN STM32\_CLOCK\_BUS\_AHB1

[ 19](stm32f1__clock_8h.md#a561265772438ab8995251760c7f3dc30)#define STM32\_PERIPH\_BUS\_MAX STM32\_CLOCK\_BUS\_APB1

20

22/\* defined in stm32\_common\_clocks.h \*/

23

25/\* Low speed clocks defined in stm32\_common\_clocks.h \*/

[ 26](stm32f1__clock_8h.md#a7bc1dd03186b763b407a044ddffb4ab2)#define STM32\_SRC\_HSI (STM32\_SRC\_LSI + 1)

[ 27](stm32f1__clock_8h.md#aa7e82706a146d0f40dc7e9755b3be9a6)#define STM32\_SRC\_HSE (STM32\_SRC\_HSI + 1)

[ 28](stm32f1__clock_8h.md#a3afc97af21308c71d21b59d53946efad)#define STM32\_SRC\_EXT\_HSE (STM32\_SRC\_HSE + 1)

[ 29](stm32f1__clock_8h.md#a4353a5ed9fb962c65382c60186c40c05)#define STM32\_SRC\_PLLCLK (STM32\_SRC\_EXT\_HSE + 1)

30

[ 32](stm32f1__clock_8h.md#a6b894fe6e036f03831faddf28bce43c6)#define CFGR1\_REG 0x04

[ 33](stm32f1__clock_8h.md#a89a06f5dfb71fe9a519f0a275ed2643d)#define CFGR2\_REG 0x2C

34

[ 36](stm32f1__clock_8h.md#a70a10f70b4f5058508e8983ad0a4de3a)#define BDCR\_REG 0x20

37

[ 40](stm32f1__clock_8h.md#a00a15803773ade4655e63cc48b8e59ea)#define I2S2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 17, CFGR2\_REG)

[ 41](stm32f1__clock_8h.md#a4c5411f3f5f66357967714a6c73f5a15)#define I2S3\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 18, CFGR2\_REG)

[ 43](stm32f1__clock_8h.md#a4836377699efa295c56d340e150695b0)#define RTC\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 8, BDCR\_REG)

44

[ 46](stm32f1__clock_8h.md#acc5c7aed4e842ca212471d7a58504821)#define MCO1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 24, CFGR1\_REG)

47/\* No MCO prescaler support on STM32F1 series. \*/

48

49#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32F1\_CLOCK\_H\_ \*/

[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32f1\_clock.h](stm32f1__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
