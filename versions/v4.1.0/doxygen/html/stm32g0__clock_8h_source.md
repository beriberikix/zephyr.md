---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32g0__clock_8h_source.html
original_path: doxygen/html/stm32g0__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32g0\_clock.h

[Go to the documentation of this file.](stm32g0__clock_8h.md)

1/\*

2 \* Copyright (c) 2022 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32G0\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32G0\_CLOCK\_H\_

8

9#include "[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)"

10

[ 12](stm32g0__clock_8h.md#afe5b12955e87bbfcee6107cc30e45566)#define STM32\_CLOCK\_BUS\_IOP 0x034

[ 13](stm32g0__clock_8h.md#a186de4b3566a20794e4483a9569abe3c)#define STM32\_CLOCK\_BUS\_AHB1 0x038

[ 14](stm32g0__clock_8h.md#ac763945fc36124f9c978c423826faa95)#define STM32\_CLOCK\_BUS\_APB1 0x03c

[ 15](stm32g0__clock_8h.md#ad25510091b50e823c9860089a9f23deb)#define STM32\_CLOCK\_BUS\_APB1\_2 0x040

16

[ 17](stm32g0__clock_8h.md#acc0577552371fcda95685f6424ecb4b2)#define STM32\_PERIPH\_BUS\_MIN STM32\_CLOCK\_BUS\_IOP

[ 18](stm32g0__clock_8h.md#a561265772438ab8995251760c7f3dc30)#define STM32\_PERIPH\_BUS\_MAX STM32\_CLOCK\_BUS\_APB1\_2

19

21/\* RM0444, §5.4.21/22 Clock configuration register (RCC\_CCIPRx) \*/

22

24/\* defined in stm32\_common\_clocks.h \*/

26/\* Low speed clocks defined in stm32\_common\_clocks.h \*/

[ 27](stm32g0__clock_8h.md#a7bc1dd03186b763b407a044ddffb4ab2)#define STM32\_SRC\_HSI (STM32\_SRC\_LSI + 1)

[ 28](stm32g0__clock_8h.md#ae12e6bda1c30174c98303f692a42960f)#define STM32\_SRC\_HSI48 (STM32\_SRC\_HSI + 1)

[ 29](stm32g0__clock_8h.md#a542b4426a15d849545af2fd6012c520c)#define STM32\_SRC\_MSI (STM32\_SRC\_HSI48 + 1)

[ 30](stm32g0__clock_8h.md#aa7e82706a146d0f40dc7e9755b3be9a6)#define STM32\_SRC\_HSE (STM32\_SRC\_MSI + 1)

[ 32](stm32g0__clock_8h.md#a6cd4e305697f314401e5654b4dd5f25d)#define STM32\_SRC\_PCLK (STM32\_SRC\_HSE + 1)

[ 34](stm32g0__clock_8h.md#a473d0d57680b535a9e9298600a1e1aab)#define STM32\_SRC\_PLL\_P (STM32\_SRC\_PCLK + 1)

[ 35](stm32g0__clock_8h.md#ab3a03011d2d433feaff934c3828e1f27)#define STM32\_SRC\_PLL\_Q (STM32\_SRC\_PLL\_P + 1)

[ 36](stm32g0__clock_8h.md#aca252b1d875fbd9dce6350f1845e5439)#define STM32\_SRC\_PLL\_R (STM32\_SRC\_PLL\_Q + 1)

37

[ 39](stm32g0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260)#define CCIPR\_REG 0x54

[ 40](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89)#define CCIPR2\_REG 0x58

41

[ 43](stm32g0__clock_8h.md#a70a10f70b4f5058508e8983ad0a4de3a)#define BDCR\_REG 0x5C

44

[ 47](stm32g0__clock_8h.md#a17f3ec5f86995a2c4087f2988a9486c5)#define USART1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 0, CCIPR\_REG)

[ 48](stm32g0__clock_8h.md#ad67d92dfc439018a7a231e661d10d7f9)#define USART2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 2, CCIPR\_REG)

[ 49](stm32g0__clock_8h.md#ad2f356c0bc0e43d6f629cdb840846526)#define USART3\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 4, CCIPR\_REG)

[ 50](stm32g0__clock_8h.md#affd653e901474991857a29deba53cf82)#define CEC\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 6, CCIPR\_REG)

[ 51](stm32g0__clock_8h.md#a943b7dd4da1aab29a6e29096d37cf7b3)#define LPUART2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 8, CCIPR\_REG)

[ 52](stm32g0__clock_8h.md#aac31ca48bf87a722f6e0519f25f764dd)#define LPUART1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 10, CCIPR\_REG)

[ 53](stm32g0__clock_8h.md#a3fbef8f2542fc6921236bd2709acf64c)#define I2C1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 12, CCIPR\_REG)

[ 54](stm32g0__clock_8h.md#ab6681395c0ed012d399bb8da480cc577)#define I2C2\_I2S1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 14, CCIPR\_REG)

[ 55](stm32g0__clock_8h.md#a042804bf8a52b3dd28033f8814442bfb)#define LPTIM1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 18, CCIPR\_REG)

[ 56](stm32g0__clock_8h.md#aa713f6ff001bfa6352747e7a66e3f98a)#define LPTIM2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 20, CCIPR\_REG)

[ 57](stm32g0__clock_8h.md#a72d364c49d3cb708b3b522240c7f2487)#define TIM1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 22, CCIPR\_REG)

[ 58](stm32g0__clock_8h.md#aec6c3536cdaa8545becc5d4575947ee1)#define TIM15\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 24, CCIPR\_REG)

[ 59](stm32g0__clock_8h.md#abfff4355a498febbcf4ebcb237930a57)#define RNG\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 26, CCIPR\_REG)

[ 60](stm32g0__clock_8h.md#a635d17ad991ded52d41a6e7b0bec5773)#define ADC\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 30, CCIPR\_REG)

[ 62](stm32g0__clock_8h.md#abee394167f826cac3ec58db3e89dd092)#define I2S1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 0, CCIPR2\_REG)

[ 63](stm32g0__clock_8h.md#a00a15803773ade4655e63cc48b8e59ea)#define I2S2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 2, CCIPR2\_REG)

[ 64](stm32g0__clock_8h.md#ac1df6369669b4b3febd0525426e76499)#define FDCAN\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 8, CCIPR2\_REG)

[ 65](stm32g0__clock_8h.md#a3247ad782f1e2c7db84989d03831139b)#define USB\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 12, CCIPR2\_REG)

[ 67](stm32g0__clock_8h.md#a4836377699efa295c56d340e150695b0)#define RTC\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 8, BDCR\_REG)

68

69#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32G0\_CLOCK\_H\_ \*/

[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32g0\_clock.h](stm32g0__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
