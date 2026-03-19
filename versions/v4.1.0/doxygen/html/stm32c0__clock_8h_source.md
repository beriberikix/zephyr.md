---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32c0__clock_8h_source.html
original_path: doxygen/html/stm32c0__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32c0\_clock.h

[Go to the documentation of this file.](stm32c0__clock_8h.md)

1/\*

2 \* Copyright (c) 2023 Benjamin Björnsson <benjamin.bjornsson@gmail.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32C0\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32C0\_CLOCK\_H\_

8

9#include "[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)"

10

[ 12](stm32c0__clock_8h.md#afe5b12955e87bbfcee6107cc30e45566)#define STM32\_CLOCK\_BUS\_IOP 0x034

[ 13](stm32c0__clock_8h.md#a186de4b3566a20794e4483a9569abe3c)#define STM32\_CLOCK\_BUS\_AHB1 0x038

[ 14](stm32c0__clock_8h.md#ac763945fc36124f9c978c423826faa95)#define STM32\_CLOCK\_BUS\_APB1 0x03c

[ 15](stm32c0__clock_8h.md#ad25510091b50e823c9860089a9f23deb)#define STM32\_CLOCK\_BUS\_APB1\_2 0x040

16

[ 17](stm32c0__clock_8h.md#acc0577552371fcda95685f6424ecb4b2)#define STM32\_PERIPH\_BUS\_MIN STM32\_CLOCK\_BUS\_IOP

[ 18](stm32c0__clock_8h.md#a561265772438ab8995251760c7f3dc30)#define STM32\_PERIPH\_BUS\_MAX STM32\_CLOCK\_BUS\_APB1\_2

19

21/\* RM0490, §5.4.21/22 Clock configuration register (RCC\_CCIPRx) \*/

22

24/\* defined in stm32\_common\_clocks.h \*/

26/\* Low speed clocks defined in stm32\_common\_clocks.h \*/

[ 27](stm32c0__clock_8h.md#a7bc1dd03186b763b407a044ddffb4ab2)#define STM32\_SRC\_HSI (STM32\_SRC\_LSI + 1)

[ 28](stm32c0__clock_8h.md#aa7e82706a146d0f40dc7e9755b3be9a6)#define STM32\_SRC\_HSE (STM32\_SRC\_HSI + 1)

[ 30](stm32c0__clock_8h.md#a6cd4e305697f314401e5654b4dd5f25d)#define STM32\_SRC\_PCLK (STM32\_SRC\_HSE + 1)

31

[ 33](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260)#define CCIPR\_REG 0x54

34

[ 36](stm32c0__clock_8h.md#aef1dabdfdb37922d3876f12a7ef193b4)#define CSR1\_REG 0x5C

37

[ 39](stm32c0__clock_8h.md#a6b894fe6e036f03831faddf28bce43c6)#define CFGR1\_REG 0x08

40

[ 43](stm32c0__clock_8h.md#a17f3ec5f86995a2c4087f2988a9486c5)#define USART1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 0, CCIPR\_REG)

[ 44](stm32c0__clock_8h.md#a3fbef8f2542fc6921236bd2709acf64c)#define I2C1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 12, CCIPR\_REG)

[ 45](stm32c0__clock_8h.md#ab6681395c0ed012d399bb8da480cc577)#define I2C2\_I2S1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 14, CCIPR\_REG)

[ 46](stm32c0__clock_8h.md#a635d17ad991ded52d41a6e7b0bec5773)#define ADC\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 30, CCIPR\_REG)

[ 48](stm32c0__clock_8h.md#a4836377699efa295c56d340e150695b0)#define RTC\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 8, CSR1\_REG)

49

[ 51](stm32c0__clock_8h.md#acc5c7aed4e842ca212471d7a58504821)#define MCO1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 24, CFGR1\_REG)

[ 52](stm32c0__clock_8h.md#a2805cf7e0b5ed0a9bb4bfff863327081)#define MCO1\_PRE(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 28, CFGR1\_REG)

[ 53](stm32c0__clock_8h.md#ab5fc05cb6aa1154c54c29b95f3154a75)#define MCO2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 16, CFGR1\_REG)

[ 54](stm32c0__clock_8h.md#ab02a0ccbb8588979ca4742c72c59589f)#define MCO2\_PRE(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 20, CFGR1\_REG)

55

56/\* MCO prescaler : division factor \*/

[ 57](stm32c0__clock_8h.md#aa6d6446aa7a1c84324475f6e8665fbb7)#define MCO\_PRE\_DIV\_1 0

[ 58](stm32c0__clock_8h.md#a36db847c7932669759f64844a15c42c3)#define MCO\_PRE\_DIV\_2 1

[ 59](stm32c0__clock_8h.md#a74c5b485d9169c489ab19e788b43c657)#define MCO\_PRE\_DIV\_4 2

[ 60](stm32c0__clock_8h.md#ad1bb69ff2fe6748978c31666f201947c)#define MCO\_PRE\_DIV\_8 3

[ 61](stm32c0__clock_8h.md#a111fd8dc5850b16b1308c8eaba8a9458)#define MCO\_PRE\_DIV\_16 4

[ 62](stm32c0__clock_8h.md#acd636581f9cbba9e66519929ecf620e2)#define MCO\_PRE\_DIV\_32 5

[ 63](stm32c0__clock_8h.md#ac2e5fb8f588e90b951a8962d1d0ce61e)#define MCO\_PRE\_DIV\_64 6

[ 64](stm32c0__clock_8h.md#a14d17d0a8cc9a70ddab9a1d2bf29661a)#define MCO\_PRE\_DIV\_128 7

65

66#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32C0\_CLOCK\_H\_ \*/

[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32c0\_clock.h](stm32c0__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
