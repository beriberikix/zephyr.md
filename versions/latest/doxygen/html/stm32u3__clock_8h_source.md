---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/stm32u3__clock_8h_source.html
original_path: doxygen/html/stm32u3__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32u3\_clock.h

[Go to the documentation of this file.](stm32u3__clock_8h.md)

1/\*

2 \* Copyright (c) 2025 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32U3\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32U3\_CLOCK\_H\_

8

9#include "[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)"

10

12

13/\* RM0487, Figure 36 Clock tree for STM32U3 Series \*/

14

16/\* defined in stm32\_common\_clocks.h \*/

[ 18](stm32u3__clock_8h.md#aa7e82706a146d0f40dc7e9755b3be9a6)#define STM32\_SRC\_HSE (STM32\_SRC\_LSI + 1)

[ 19](stm32u3__clock_8h.md#a5e1f2346bda03742e59614bf3d727be0)#define STM32\_SRC\_HSI16 (STM32\_SRC\_HSE + 1)

[ 20](stm32u3__clock_8h.md#ae12e6bda1c30174c98303f692a42960f)#define STM32\_SRC\_HSI48 (STM32\_SRC\_HSI16 + 1)

[ 21](stm32u3__clock_8h.md#a632bcd9ada69ab27033a3d46406fd4fb)#define STM32\_SRC\_MSIS (STM32\_SRC\_HSI48 + 1)

[ 22](stm32u3__clock_8h.md#a6cdbd60c77934e2e1ecbdf281c670550)#define STM32\_SRC\_MSIK (STM32\_SRC\_MSIS + 1)

[ 24](stm32u3__clock_8h.md#a2c2165a735dc0763cd972d464ececc5d)#define STM32\_SRC\_HCLK (STM32\_SRC\_MSIK + 1)

[ 25](stm32u3__clock_8h.md#a72ffaa9863e167f47e06e91151b47831)#define STM32\_SRC\_PCLK1 (STM32\_SRC\_HCLK + 1)

[ 26](stm32u3__clock_8h.md#a68f7335900538f3beb2c2d09e33376b3)#define STM32\_SRC\_PCLK2 (STM32\_SRC\_PCLK1 + 1)

[ 27](stm32u3__clock_8h.md#ae54654dc761dca391f56e95ebd6db625)#define STM32\_SRC\_PCLK3 (STM32\_SRC\_PCLK2 + 1)

29/\* #define STM32\_SRC\_ICLK TBD \*/

30

[ 32](stm32u3__clock_8h.md#a186de4b3566a20794e4483a9569abe3c)#define STM32\_CLOCK\_BUS\_AHB1 0x088

[ 33](stm32u3__clock_8h.md#af24118ede113167b5e40758432031ca9)#define STM32\_CLOCK\_BUS\_AHB1\_2 0x094

[ 34](stm32u3__clock_8h.md#a5e58ef1846c185b04bed598b26ee9205)#define STM32\_CLOCK\_BUS\_AHB2 0x08C

[ 35](stm32u3__clock_8h.md#a76e35461c02d9c020948f980c864e9b3)#define STM32\_CLOCK\_BUS\_AHB2\_2 0x090

[ 36](stm32u3__clock_8h.md#ac763945fc36124f9c978c423826faa95)#define STM32\_CLOCK\_BUS\_APB1 0x09C

[ 37](stm32u3__clock_8h.md#ad25510091b50e823c9860089a9f23deb)#define STM32\_CLOCK\_BUS\_APB1\_2 0x0A0

[ 38](stm32u3__clock_8h.md#adb7becb609763568b91303041c9cd4db)#define STM32\_CLOCK\_BUS\_APB2 0x0A4

[ 39](stm32u3__clock_8h.md#af7165e22b71d1beaf0dd4f59d5b4db6d)#define STM32\_CLOCK\_BUS\_APB3 0x0A8

40

[ 41](stm32u3__clock_8h.md#acc0577552371fcda95685f6424ecb4b2)#define STM32\_PERIPH\_BUS\_MIN STM32\_CLOCK\_BUS\_AHB1

[ 42](stm32u3__clock_8h.md#a561265772438ab8995251760c7f3dc30)#define STM32\_PERIPH\_BUS\_MAX STM32\_CLOCK\_BUS\_APB3

43

[ 45](stm32u3__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2)#define CCIPR1\_REG 0x100

[ 46](stm32u3__clock_8h.md#a60349691a29a48b727f302acb8025b89)#define CCIPR2\_REG 0x104

[ 47](stm32u3__clock_8h.md#a302577067fac290b578130da822dc146)#define CCIPR3\_REG 0x108

48

[ 50](stm32u3__clock_8h.md#a70a10f70b4f5058508e8983ad0a4de3a)#define BDCR\_REG 0x110

51

[ 53](stm32u3__clock_8h.md#a6b894fe6e036f03831faddf28bce43c6)#define CFGR1\_REG 0x0C

54

[ 57](stm32u3__clock_8h.md#a17f3ec5f86995a2c4087f2988a9486c5)#define USART1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 0, CCIPR1\_REG)

[ 58](stm32u3__clock_8h.md#ad2f356c0bc0e43d6f629cdb840846526)#define USART3\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 2, CCIPR1\_REG)

[ 59](stm32u3__clock_8h.md#a091d597b4979c49951f880bc6ccb4d71)#define UART4\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 4, CCIPR1\_REG)

[ 60](stm32u3__clock_8h.md#a136c2c36c89ebdf2c5b97686bbce0209)#define UART5\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 6, CCIPR1\_REG)

[ 61](stm32u3__clock_8h.md#a576dca08c22370326fefc540bf056b81)#define I3C1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 8, CCIPR1\_REG)

[ 62](stm32u3__clock_8h.md#a3fbef8f2542fc6921236bd2709acf64c)#define I2C1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 10, CCIPR1\_REG)

[ 63](stm32u3__clock_8h.md#abdd79c9ce90458b53e81123d181fed98)#define I2C2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 12, CCIPR1\_REG)

[ 64](stm32u3__clock_8h.md#a647bc22bf65d67e9e2c5361d0dce925d)#define I3C2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 14, CCIPR1\_REG)

[ 65](stm32u3__clock_8h.md#ad3e84eac634b9d943acea9b2ab884fb5)#define SPI2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 16, CCIPR1\_REG)

[ 66](stm32u3__clock_8h.md#aa713f6ff001bfa6352747e7a66e3f98a)#define LPTIM2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 18, CCIPR1\_REG)

[ 67](stm32u3__clock_8h.md#a5199102173e9dbe957230f356e14d910)#define SPI1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 20, CCIPR1\_REG)

[ 68](stm32u3__clock_8h.md#a9319a91fb044022ba812f616cf192f65)#define SYSTICK\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 22, CCIPR1\_REG)

[ 69](stm32u3__clock_8h.md#a11874554108542cecbce3f012940ab0c)#define FDCAN1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 24, CCIPR1\_REG)

[ 70](stm32u3__clock_8h.md#a467698cc8a5140a9aa169cb63de049f4)#define ICLK\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 26, CCIPR1\_REG)

[ 71](stm32u3__clock_8h.md#a1f29287e499d74135f886c7a12dee2db)#define USB1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 28, CCIPR1\_REG)

[ 72](stm32u3__clock_8h.md#ad39b85aaa947648b1b833b1414116f51)#define TIMIC\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 29, CCIPR1\_REG)

[ 74](stm32u3__clock_8h.md#a2965fce3cbae0a73506ddf383c78783f)#define ADF1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 0, CCIPR2\_REG)

[ 75](stm32u3__clock_8h.md#aaa096904d8a97bedc81f9a565e65c332)#define SPI3\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 3, CCIPR2\_REG)

[ 76](stm32u3__clock_8h.md#ab8e49f6309adb53edd9ad3d051d451db)#define SAI1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 5, CCIPR2\_REG)

[ 77](stm32u3__clock_8h.md#abfff4355a498febbcf4ebcb237930a57)#define RNG\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 11, CCIPR2\_REG)

[ 78](stm32u3__clock_8h.md#a454d6254cea3749ac4502fb51739e27c)#define ADCDAC\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 16, CCIPR2\_REG)

[ 79](stm32u3__clock_8h.md#a485e470fc68329d8eb13203614f36d20)#define DAC1SH\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 19, CCIPR2\_REG)

[ 80](stm32u3__clock_8h.md#a121f4f2f299d0ab56293512df1ac6b2c)#define OCTOSPI\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 20, CCIPR2\_REG)

[ 82](stm32u3__clock_8h.md#aac31ca48bf87a722f6e0519f25f764dd)#define LPUART1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 0, CCIPR3\_REG)

[ 83](stm32u3__clock_8h.md#aa12a1d2ac790880b7148d1e5660eb941)#define I2C3\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 6, CCIPR3\_REG)

[ 84](stm32u3__clock_8h.md#a7f929ce6942d82e8eeedbd8b563ce093)#define LPTIM34\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 8, CCIPR3\_REG)

[ 85](stm32u3__clock_8h.md#a042804bf8a52b3dd28033f8814442bfb)#define LPTIM1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 10, CCIPR3\_REG)

[ 87](stm32u3__clock_8h.md#a4836377699efa295c56d340e150695b0)#define RTC\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 8, BDCR\_REG)

88

[ 90](stm32u3__clock_8h.md#acc5c7aed4e842ca212471d7a58504821)#define MCO1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0xF, 24, CFGR1\_REG)

[ 91](stm32u3__clock_8h.md#a2805cf7e0b5ed0a9bb4bfff863327081)#define MCO1\_PRE(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 28, CFGR1\_REG)

92

93/\* MCO prescaler : division factor \*/

[ 94](stm32u3__clock_8h.md#aa6d6446aa7a1c84324475f6e8665fbb7)#define MCO\_PRE\_DIV\_1 0

[ 95](stm32u3__clock_8h.md#a36db847c7932669759f64844a15c42c3)#define MCO\_PRE\_DIV\_2 1

[ 96](stm32u3__clock_8h.md#a74c5b485d9169c489ab19e788b43c657)#define MCO\_PRE\_DIV\_4 2

[ 97](stm32u3__clock_8h.md#ad1bb69ff2fe6748978c31666f201947c)#define MCO\_PRE\_DIV\_8 3

[ 98](stm32u3__clock_8h.md#a111fd8dc5850b16b1308c8eaba8a9458)#define MCO\_PRE\_DIV\_16 4

[ 99](stm32u3__clock_8h.md#acd636581f9cbba9e66519929ecf620e2)#define MCO\_PRE\_DIV\_32 5

[ 100](stm32u3__clock_8h.md#ac2e5fb8f588e90b951a8962d1d0ce61e)#define MCO\_PRE\_DIV\_64 6

[ 101](stm32u3__clock_8h.md#a14d17d0a8cc9a70ddab9a1d2bf29661a)#define MCO\_PRE\_DIV\_128 7

102

103#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32U3\_CLOCK\_H\_ \*/

[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32u3\_clock.h](stm32u3__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
