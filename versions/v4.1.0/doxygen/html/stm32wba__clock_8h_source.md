---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32wba__clock_8h_source.html
original_path: doxygen/html/stm32wba__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32wba\_clock.h

[Go to the documentation of this file.](stm32wba__clock_8h.md)

1/\*

2 \* Copyright (c) 2023 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32WBA\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32WBA\_CLOCK\_H\_

8

9#include "[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)"

10

12

13/\* RM0493, Figure 30, clock tree \*/

14

16/\* defined in stm32\_common\_clocks.h \*/

18/\* Low speed clocks defined in stm32\_common\_clocks.h \*/

[ 19](stm32wba__clock_8h.md#aa7e82706a146d0f40dc7e9755b3be9a6)#define STM32\_SRC\_HSE (STM32\_SRC\_LSI + 1)

[ 20](stm32wba__clock_8h.md#a5e1f2346bda03742e59614bf3d727be0)#define STM32\_SRC\_HSI16 (STM32\_SRC\_HSE + 1)

[ 22](stm32wba__clock_8h.md#af4cce65567b57af5b512a97d3aadbbc9)#define STM32\_SRC\_HCLK1 (STM32\_SRC\_HSI16 + 1)

[ 23](stm32wba__clock_8h.md#a9a565ff797b5d040c194e11a969e2a4f)#define STM32\_SRC\_HCLK5 (STM32\_SRC\_HCLK1 + 1)

[ 24](stm32wba__clock_8h.md#a72ffaa9863e167f47e06e91151b47831)#define STM32\_SRC\_PCLK1 (STM32\_SRC\_HCLK5 + 1)

[ 25](stm32wba__clock_8h.md#a68f7335900538f3beb2c2d09e33376b3)#define STM32\_SRC\_PCLK2 (STM32\_SRC\_PCLK1 + 1)

[ 26](stm32wba__clock_8h.md#a78478906687374cfcdbec3d498895200)#define STM32\_SRC\_PCLK7 (STM32\_SRC\_PCLK2 + 1)

[ 28](stm32wba__clock_8h.md#aa074615a92c5ff479f4fbed6fdf27f62)#define STM32\_SRC\_PLL1\_P (STM32\_SRC\_PCLK7 + 1)

[ 29](stm32wba__clock_8h.md#a6edb3dc598055ceeb82045fdee647637)#define STM32\_SRC\_PLL1\_Q (STM32\_SRC\_PLL1\_P + 1)

[ 30](stm32wba__clock_8h.md#a6063632b32a970b9abbf711bab8a77c9)#define STM32\_SRC\_PLL1\_R (STM32\_SRC\_PLL1\_Q + 1)

31

[ 32](stm32wba__clock_8h.md#a58011c928870ee9a5f3f94298ee98ba2)#define STM32\_SRC\_CLOCK\_MIN STM32\_SRC\_PLL1\_P

[ 33](stm32wba__clock_8h.md#aa6f33e6e948988ae8a962860ce5ce4fc)#define STM32\_SRC\_CLOCK\_MAX STM32\_SRC\_SYSCLK

34

[ 36](stm32wba__clock_8h.md#a186de4b3566a20794e4483a9569abe3c)#define STM32\_CLOCK\_BUS\_AHB1 0x088

[ 37](stm32wba__clock_8h.md#a5e58ef1846c185b04bed598b26ee9205)#define STM32\_CLOCK\_BUS\_AHB2 0x08C

[ 38](stm32wba__clock_8h.md#a49bccabc3065f192086f16929a7b762d)#define STM32\_CLOCK\_BUS\_AHB4 0x094

[ 39](stm32wba__clock_8h.md#a623a8ba4dc47622dfbf76801f1582f58)#define STM32\_CLOCK\_BUS\_AHB5 0x098

[ 40](stm32wba__clock_8h.md#ac763945fc36124f9c978c423826faa95)#define STM32\_CLOCK\_BUS\_APB1 0x09C

[ 41](stm32wba__clock_8h.md#ad25510091b50e823c9860089a9f23deb)#define STM32\_CLOCK\_BUS\_APB1\_2 0x0A0

[ 42](stm32wba__clock_8h.md#adb7becb609763568b91303041c9cd4db)#define STM32\_CLOCK\_BUS\_APB2 0x0A4

[ 43](stm32wba__clock_8h.md#a9f9e2ac99429770af882a00dfadb1552)#define STM32\_CLOCK\_BUS\_APB7 0x0A8

44

[ 45](stm32wba__clock_8h.md#acc0577552371fcda95685f6424ecb4b2)#define STM32\_PERIPH\_BUS\_MIN STM32\_CLOCK\_BUS\_AHB1

[ 46](stm32wba__clock_8h.md#a561265772438ab8995251760c7f3dc30)#define STM32\_PERIPH\_BUS\_MAX STM32\_CLOCK\_BUS\_APB7

47

[ 49](stm32wba__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2)#define CCIPR1\_REG 0xE0

[ 50](stm32wba__clock_8h.md#a60349691a29a48b727f302acb8025b89)#define CCIPR2\_REG 0xE4

[ 51](stm32wba__clock_8h.md#a302577067fac290b578130da822dc146)#define CCIPR3\_REG 0xE8

[ 53](stm32wba__clock_8h.md#a6ec3713a2b3ac22d283abeb2d0e129bf)#define BCDR1\_REG 0xF0

54

[ 57](stm32wba__clock_8h.md#a17f3ec5f86995a2c4087f2988a9486c5)#define USART1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 0, CCIPR1\_REG)

[ 58](stm32wba__clock_8h.md#ad67d92dfc439018a7a231e661d10d7f9)#define USART2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 2, CCIPR1\_REG)

[ 59](stm32wba__clock_8h.md#a3fbef8f2542fc6921236bd2709acf64c)#define I2C1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 10, CCIPR1\_REG)

[ 60](stm32wba__clock_8h.md#aa713f6ff001bfa6352747e7a66e3f98a)#define LPTIM2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 18, CCIPR1\_REG)

[ 61](stm32wba__clock_8h.md#a5199102173e9dbe957230f356e14d910)#define SPI1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 20, CCIPR1\_REG)

[ 62](stm32wba__clock_8h.md#a9319a91fb044022ba812f616cf192f65)#define SYSTICK\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 22, CCIPR1\_REG)

[ 63](stm32wba__clock_8h.md#ad39b85aaa947648b1b833b1414116f51)#define TIMIC\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 31, CCIPR1\_REG)

[ 65](stm32wba__clock_8h.md#abfff4355a498febbcf4ebcb237930a57)#define RNG\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 12, CCIPR2\_REG)

[ 67](stm32wba__clock_8h.md#aac31ca48bf87a722f6e0519f25f764dd)#define LPUART1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 0, CCIPR3\_REG)

[ 68](stm32wba__clock_8h.md#aaa096904d8a97bedc81f9a565e65c332)#define SPI3\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 3, CCIPR3\_REG)

[ 69](stm32wba__clock_8h.md#aa12a1d2ac790880b7148d1e5660eb941)#define I2C3\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 6, CCIPR3\_REG)

[ 70](stm32wba__clock_8h.md#a042804bf8a52b3dd28033f8814442bfb)#define LPTIM1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 10, CCIPR3\_REG)

[ 71](stm32wba__clock_8h.md#a635d17ad991ded52d41a6e7b0bec5773)#define ADC\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 12, CCIPR3\_REG)

[ 73](stm32wba__clock_8h.md#a4836377699efa295c56d340e150695b0)#define RTC\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 8, BCDR1\_REG)

[ 75](stm32wba__clock_8h.md#a6b894fe6e036f03831faddf28bce43c6)#define CFGR1\_REG 0x1C

[ 77](stm32wba__clock_8h.md#acc5c7aed4e842ca212471d7a58504821)#define MCO1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0xF, 24, CFGR1\_REG)

[ 78](stm32wba__clock_8h.md#a2805cf7e0b5ed0a9bb4bfff863327081)#define MCO1\_PRE(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 28, CFGR1\_REG)

79

80/\* MCO prescaler : division factor \*/

[ 81](stm32wba__clock_8h.md#aa6d6446aa7a1c84324475f6e8665fbb7)#define MCO\_PRE\_DIV\_1 0

[ 82](stm32wba__clock_8h.md#a36db847c7932669759f64844a15c42c3)#define MCO\_PRE\_DIV\_2 1

[ 83](stm32wba__clock_8h.md#a74c5b485d9169c489ab19e788b43c657)#define MCO\_PRE\_DIV\_4 2

[ 84](stm32wba__clock_8h.md#ad1bb69ff2fe6748978c31666f201947c)#define MCO\_PRE\_DIV\_8 3

[ 85](stm32wba__clock_8h.md#a111fd8dc5850b16b1308c8eaba8a9458)#define MCO\_PRE\_DIV\_16 4

86

87/\* MCO clock output \*/

[ 88](stm32wba__clock_8h.md#a53d7140c4e0ee2e9da56c79819c62658)#define MCO\_SEL\_SYSCLKPRE 1

[ 89](stm32wba__clock_8h.md#adf2625b4cceede7fc3ba63f688a4e4e9)#define MCO\_SEL\_HSI16 3

[ 90](stm32wba__clock_8h.md#a21781f8cb4ed3c916d94ecfdd919d245)#define MCO\_SEL\_HSE32 4

[ 91](stm32wba__clock_8h.md#a6a5c7799714251e9577823a70ae43deb)#define MCO\_SEL\_PLL1RCLK 5

[ 92](stm32wba__clock_8h.md#a2d2499a8c8748def496cbcdde1582a47)#define MCO\_SEL\_LSI 6

[ 93](stm32wba__clock_8h.md#aaa9ea448ff6849b35f63fdfe07bc9bf2)#define MCO\_SEL\_LSE 7

[ 94](stm32wba__clock_8h.md#a9fdaaf9ec6ae71d7ef4baf491c828d5a)#define MCO\_SEL\_PLL1PCLK 8

[ 95](stm32wba__clock_8h.md#ace6964cb5c6328adc762e4917e9ed663)#define MCO\_SEL\_PLL1QCLK 9

[ 96](stm32wba__clock_8h.md#a80e8fec39e1a6711e20669cc3431c16b)#define MCO\_SEL\_HCLK5 10

97

98

99#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32WBA\_CLOCK\_H\_ \*/

[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32wba\_clock.h](stm32wba__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
