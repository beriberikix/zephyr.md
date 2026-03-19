---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32l0__clock_8h_source.html
original_path: doxygen/html/stm32l0__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32l0\_clock.h

[Go to the documentation of this file.](stm32l0__clock_8h.md)

1/\*

2 \* Copyright (c) 2022 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32L0\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32L0\_CLOCK\_H\_

8

9#include "[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)"

10

[ 12](stm32l0__clock_8h.md#afe5b12955e87bbfcee6107cc30e45566)#define STM32\_CLOCK\_BUS\_IOP 0x02c

[ 13](stm32l0__clock_8h.md#a186de4b3566a20794e4483a9569abe3c)#define STM32\_CLOCK\_BUS\_AHB1 0x030

[ 14](stm32l0__clock_8h.md#adb7becb609763568b91303041c9cd4db)#define STM32\_CLOCK\_BUS\_APB2 0x034

[ 15](stm32l0__clock_8h.md#ac763945fc36124f9c978c423826faa95)#define STM32\_CLOCK\_BUS\_APB1 0x038

16

[ 17](stm32l0__clock_8h.md#acc0577552371fcda95685f6424ecb4b2)#define STM32\_PERIPH\_BUS\_MIN STM32\_CLOCK\_BUS\_IOP

[ 18](stm32l0__clock_8h.md#a561265772438ab8995251760c7f3dc30)#define STM32\_PERIPH\_BUS\_MAX STM32\_CLOCK\_BUS\_APB1

19

21/\* RM0367, §7.3.20 Clock configuration register (RCC\_CCIPR) \*/

22

24/\* defined in stm32\_common\_clocks.h \*/

25

27/\* Low speed clocks defined in stm32\_common\_clocks.h \*/

[ 28](stm32l0__clock_8h.md#aa7e82706a146d0f40dc7e9755b3be9a6)#define STM32\_SRC\_HSE (STM32\_SRC\_LSI + 1)

[ 29](stm32l0__clock_8h.md#a7bc1dd03186b763b407a044ddffb4ab2)#define STM32\_SRC\_HSI (STM32\_SRC\_HSE + 1)

[ 30](stm32l0__clock_8h.md#ae12e6bda1c30174c98303f692a42960f)#define STM32\_SRC\_HSI48 (STM32\_SRC\_HSI + 1)

[ 32](stm32l0__clock_8h.md#a6cd4e305697f314401e5654b4dd5f25d)#define STM32\_SRC\_PCLK (STM32\_SRC\_HSI48 + 1)

33

[ 35](stm32l0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260)#define CCIPR\_REG 0x4C

36

[ 38](stm32l0__clock_8h.md#a16c4f3ac8a8c6255620516b3a32b7a70)#define CSR\_REG 0x50

39

[ 42](stm32l0__clock_8h.md#a17f3ec5f86995a2c4087f2988a9486c5)#define USART1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 0, CCIPR\_REG)

[ 43](stm32l0__clock_8h.md#ad67d92dfc439018a7a231e661d10d7f9)#define USART2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 2, CCIPR\_REG)

[ 44](stm32l0__clock_8h.md#aac31ca48bf87a722f6e0519f25f764dd)#define LPUART1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 10, CCIPR\_REG)

[ 45](stm32l0__clock_8h.md#a3fbef8f2542fc6921236bd2709acf64c)#define I2C1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 12, CCIPR\_REG)

[ 46](stm32l0__clock_8h.md#aa12a1d2ac790880b7148d1e5660eb941)#define I2C3\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 16, CCIPR\_REG)

[ 47](stm32l0__clock_8h.md#a042804bf8a52b3dd28033f8814442bfb)#define LPTIM1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 18, CCIPR\_REG)

[ 48](stm32l0__clock_8h.md#a3e4eee46bbec297ebd6da48abdff1dbb)#define HSI48\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 26, CCIPR\_REG)

[ 50](stm32l0__clock_8h.md#a4836377699efa295c56d340e150695b0)#define RTC\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 16, CSR\_REG)

51

52#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32L0\_CLOCK\_H\_ \*/

[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32l0\_clock.h](stm32l0__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
