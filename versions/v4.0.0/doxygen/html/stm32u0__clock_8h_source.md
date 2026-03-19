---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stm32u0__clock_8h_source.html
original_path: doxygen/html/stm32u0__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32u0\_clock.h

[Go to the documentation of this file.](stm32u0__clock_8h.md)

1/\*

2 \* Copyright (c) 2024 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32U0\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32U0\_CLOCK\_H\_

8

9#include "[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)"

10

[ 12](stm32u0__clock_8h.md#a186de4b3566a20794e4483a9569abe3c)#define STM32\_CLOCK\_BUS\_AHB1 0x48

[ 13](stm32u0__clock_8h.md#afe5b12955e87bbfcee6107cc30e45566)#define STM32\_CLOCK\_BUS\_IOP 0x4C

[ 14](stm32u0__clock_8h.md#ac763945fc36124f9c978c423826faa95)#define STM32\_CLOCK\_BUS\_APB1 0x58

[ 15](stm32u0__clock_8h.md#ad25510091b50e823c9860089a9f23deb)#define STM32\_CLOCK\_BUS\_APB1\_2 0x60

16

[ 17](stm32u0__clock_8h.md#acc0577552371fcda95685f6424ecb4b2)#define STM32\_PERIPH\_BUS\_MIN STM32\_CLOCK\_BUS\_AHB1

[ 18](stm32u0__clock_8h.md#a561265772438ab8995251760c7f3dc30)#define STM32\_PERIPH\_BUS\_MAX STM32\_CLOCK\_BUS\_APB1\_2

19

21/\* RM0503, clock configuration register (RCC\_CCIPR) \*/

22

24/\* defined in stm32\_common\_clocks.h \*/

25

27/\* Low speed clocks defined in stm32\_common\_clocks.h \*/

[ 28](stm32u0__clock_8h.md#a7bc1dd03186b763b407a044ddffb4ab2)#define STM32\_SRC\_HSI (STM32\_SRC\_LSI + 1)

[ 29](stm32u0__clock_8h.md#ae12e6bda1c30174c98303f692a42960f)#define STM32\_SRC\_HSI48 (STM32\_SRC\_HSI + 1)

[ 30](stm32u0__clock_8h.md#a542b4426a15d849545af2fd6012c520c)#define STM32\_SRC\_MSI (STM32\_SRC\_HSI48 + 1)

[ 31](stm32u0__clock_8h.md#aa7e82706a146d0f40dc7e9755b3be9a6)#define STM32\_SRC\_HSE (STM32\_SRC\_MSI + 1)

[ 33](stm32u0__clock_8h.md#a6cd4e305697f314401e5654b4dd5f25d)#define STM32\_SRC\_PCLK (STM32\_SRC\_HSE + 1)

[ 35](stm32u0__clock_8h.md#a473d0d57680b535a9e9298600a1e1aab)#define STM32\_SRC\_PLL\_P (STM32\_SRC\_PCLK + 1)

[ 36](stm32u0__clock_8h.md#ab3a03011d2d433feaff934c3828e1f27)#define STM32\_SRC\_PLL\_Q (STM32\_SRC\_PLL\_P + 1)

[ 37](stm32u0__clock_8h.md#aca252b1d875fbd9dce6350f1845e5439)#define STM32\_SRC\_PLL\_R (STM32\_SRC\_PLL\_Q + 1)

38

[ 39](stm32u0__clock_8h.md#a33d66849c63db64784317260b06ceb24)#define STM32\_CLOCK\_REG\_MASK 0xFFU

[ 40](stm32u0__clock_8h.md#a2e73bdb1691751ffd616a5c4e2762423)#define STM32\_CLOCK\_REG\_SHIFT 0U

[ 41](stm32u0__clock_8h.md#af3001a7541ea4df9e4948fd559352f60)#define STM32\_CLOCK\_SHIFT\_MASK 0x1FU

[ 42](stm32u0__clock_8h.md#a147846b77bd51e42c85bea5aca50ad4f)#define STM32\_CLOCK\_SHIFT\_SHIFT 8U

[ 43](stm32u0__clock_8h.md#a63ecbd205c0dd6cb3eab7bcbfdce38b9)#define STM32\_CLOCK\_MASK\_MASK 0x7U

[ 44](stm32u0__clock_8h.md#abfdb31d824fc5c6cf809a1dcff022b5d)#define STM32\_CLOCK\_MASK\_SHIFT 13U

[ 45](stm32u0__clock_8h.md#a6b4f80c7dbd047ca1ebac0b233ad1d1b)#define STM32\_CLOCK\_VAL\_MASK 0x7U

[ 46](stm32u0__clock_8h.md#adf2ca8c7f707b82b7ec4820dfc32929a)#define STM32\_CLOCK\_VAL\_SHIFT 16U

47

[ 61](stm32u0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)#define STM32\_DOMAIN\_CLOCK(val, mask, shift, reg) \

62 ((((reg) & STM32\_CLOCK\_REG\_MASK) << STM32\_CLOCK\_REG\_SHIFT) | \

63 (((shift) & STM32\_CLOCK\_SHIFT\_MASK) << STM32\_CLOCK\_SHIFT\_SHIFT) | \

64 (((mask) & STM32\_CLOCK\_MASK\_MASK) << STM32\_CLOCK\_MASK\_SHIFT) | \

65 (((val) & STM32\_CLOCK\_VAL\_MASK) << STM32\_CLOCK\_VAL\_SHIFT))

66

[ 68](stm32u0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260)#define CCIPR\_REG 0x88

69

[ 71](stm32u0__clock_8h.md#a70a10f70b4f5058508e8983ad0a4de3a)#define BDCR\_REG 0x90

72

[ 75](stm32u0__clock_8h.md#a17f3ec5f86995a2c4087f2988a9486c5)#define USART1\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 0, CCIPR\_REG)

[ 76](stm32u0__clock_8h.md#ad67d92dfc439018a7a231e661d10d7f9)#define USART2\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 2, CCIPR\_REG)

[ 77](stm32u0__clock_8h.md#a253dee875d346493fef20c724b16152b)#define LPUART3\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 6, CCIPR\_REG)

[ 78](stm32u0__clock_8h.md#a943b7dd4da1aab29a6e29096d37cf7b3)#define LPUART2\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 8, CCIPR\_REG)

[ 79](stm32u0__clock_8h.md#aac31ca48bf87a722f6e0519f25f764dd)#define LPUART1\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 10, CCIPR\_REG)

[ 80](stm32u0__clock_8h.md#a3fbef8f2542fc6921236bd2709acf64c)#define I2C1\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 12, CCIPR\_REG)

[ 81](stm32u0__clock_8h.md#aa12a1d2ac790880b7148d1e5660eb941)#define I2C3\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 16, CCIPR\_REG)

[ 82](stm32u0__clock_8h.md#a042804bf8a52b3dd28033f8814442bfb)#define LPTIM1\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 18, CCIPR\_REG)

[ 83](stm32u0__clock_8h.md#aa713f6ff001bfa6352747e7a66e3f98a)#define LPTIM2\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 20, CCIPR\_REG)

[ 84](stm32u0__clock_8h.md#ac705aa5789ca3b11ac5115d22ec2a5e5)#define LPTIM3\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 22, CCIPR\_REG)

[ 85](stm32u0__clock_8h.md#a72d364c49d3cb708b3b522240c7f2487)#define TIM1\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 1, 24, CCIPR\_REG)

[ 86](stm32u0__clock_8h.md#aec6c3536cdaa8545becc5d4575947ee1)#define TIM15\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 1, 25, CCIPR\_REG)

[ 87](stm32u0__clock_8h.md#a3f3b40e4fdebc11d7a2dd4a86e1fefc8)#define CLK48\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 26, CCIPR\_REG)

[ 88](stm32u0__clock_8h.md#a635d17ad991ded52d41a6e7b0bec5773)#define ADC\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 28, CCIPR\_REG)

[ 90](stm32u0__clock_8h.md#a4836377699efa295c56d340e150695b0)#define RTC\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 8, CSR\_REG)

91

92#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32U0\_CLOCK\_H\_ \*/

[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32u0\_clock.h](stm32u0__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
