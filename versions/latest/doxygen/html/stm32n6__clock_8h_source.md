---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32n6__clock_8h_source.html
original_path: doxygen/html/stm32n6__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32n6\_clock.h

[Go to the documentation of this file.](stm32n6__clock_8h.md)

1/\*

2 \* Copyright (c) 2024 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32N6\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32N6\_CLOCK\_H\_

8

9#include "[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)"

10

12

13/\* RM0468, Table 56 Kernel clock distribution summary \*/

14

16/\* defined in stm32\_common\_clocks.h \*/

[ 18](stm32n6__clock_8h.md#aa7e82706a146d0f40dc7e9755b3be9a6)#define STM32\_SRC\_HSE (STM32\_SRC\_LSI + 1)

[ 19](stm32n6__clock_8h.md#a7bc1dd03186b763b407a044ddffb4ab2)#define STM32\_SRC\_HSI (STM32\_SRC\_HSE + 1)

[ 20](stm32n6__clock_8h.md#a542b4426a15d849545af2fd6012c520c)#define STM32\_SRC\_MSI (STM32\_SRC\_HSI + 1)

[ 22](stm32n6__clock_8h.md#a19b07a1053f648e063c71884f58644f5)#define STM32\_SRC\_PLL1 (STM32\_SRC\_MSI + 1)

[ 23](stm32n6__clock_8h.md#ad3883851983b32dec66ee645f123ae55)#define STM32\_SRC\_PLL2 (STM32\_SRC\_PLL1 + 1)

[ 24](stm32n6__clock_8h.md#a848b0c6079f693252c1aea11ff1f22d3)#define STM32\_SRC\_PLL3 (STM32\_SRC\_PLL2 + 1)

[ 25](stm32n6__clock_8h.md#a45ea694120a93c1971fe65ec82d1c4d1)#define STM32\_SRC\_PLL4 (STM32\_SRC\_PLL3 + 1)

[ 27](stm32n6__clock_8h.md#a8b7025d7f4be00a152c53097a414668e)#define STM32\_SRC\_CKPER (STM32\_SRC\_PLL4 + 1)

[ 28](stm32n6__clock_8h.md#aa13b836db0b585e0998b17edb43c41d7)#define STM32\_SRC\_IC1 (STM32\_SRC\_CKPER + 1)

[ 29](stm32n6__clock_8h.md#aed86ff6d9d94396b0dfa38a94fc3c121)#define STM32\_SRC\_IC2 (STM32\_SRC\_IC1 + 1)

[ 30](stm32n6__clock_8h.md#a5cbf858b015f3d890d5584d1a817ee28)#define STM32\_SRC\_IC3 (STM32\_SRC\_IC2 + 1)

[ 31](stm32n6__clock_8h.md#aa04f6065e9e9c206bbd4b977231a4407)#define STM32\_SRC\_IC4 (STM32\_SRC\_IC3 + 1)

[ 32](stm32n6__clock_8h.md#ac1865fa9a7e303b05f1bc6ff6cca5cdc)#define STM32\_SRC\_IC5 (STM32\_SRC\_IC4 + 1)

[ 33](stm32n6__clock_8h.md#abd8ade42581f7a8375d8548c7968ae54)#define STM32\_SRC\_IC6 (STM32\_SRC\_IC5 + 1)

[ 34](stm32n6__clock_8h.md#a590359462bd90dc5e50055e35d794077)#define STM32\_SRC\_IC7 (STM32\_SRC\_IC6 + 1)

[ 35](stm32n6__clock_8h.md#a2b8c5564a40658105375154f69169d4c)#define STM32\_SRC\_IC8 (STM32\_SRC\_IC7 + 1)

[ 36](stm32n6__clock_8h.md#a161620be8255ff4c06bbb9fbe22cea3b)#define STM32\_SRC\_IC9 (STM32\_SRC\_IC8 + 1)

[ 37](stm32n6__clock_8h.md#a155f8b76c1702064125e99b5facec123)#define STM32\_SRC\_IC10 (STM32\_SRC\_IC9 + 1)

[ 38](stm32n6__clock_8h.md#aac341fc606e3cf6ee2ef69603d60a250)#define STM32\_SRC\_IC11 (STM32\_SRC\_IC10 + 1)

[ 39](stm32n6__clock_8h.md#a95e0637f72e0f6fbc80f9ce771abc111)#define STM32\_SRC\_IC12 (STM32\_SRC\_IC11 + 1)

[ 40](stm32n6__clock_8h.md#a3d76a5bd14d0e0f5a61e38ae33190223)#define STM32\_SRC\_IC13 (STM32\_SRC\_IC12 + 1)

[ 41](stm32n6__clock_8h.md#aac5bc01ec42163ed149440284bdf8592)#define STM32\_SRC\_IC14 (STM32\_SRC\_IC13 + 1)

[ 42](stm32n6__clock_8h.md#af1fba356ba1dc06132d763d02df1234c)#define STM32\_SRC\_IC15 (STM32\_SRC\_IC14 + 1)

[ 43](stm32n6__clock_8h.md#a47414e92c3cff773978026dede6272ee)#define STM32\_SRC\_IC16 (STM32\_SRC\_IC15 + 1)

[ 44](stm32n6__clock_8h.md#a04b6c1123aa4c7db12e1fb83a9afd838)#define STM32\_SRC\_IC17 (STM32\_SRC\_IC16 + 1)

[ 45](stm32n6__clock_8h.md#add609ce4fd1723b9662335ab0a835523)#define STM32\_SRC\_IC18 (STM32\_SRC\_IC17 + 1)

[ 46](stm32n6__clock_8h.md#aee9cb50a33915e66260a0205041091d7)#define STM32\_SRC\_IC19 (STM32\_SRC\_IC18 + 1)

[ 47](stm32n6__clock_8h.md#a9aedd874a88b96145f31a76585806ff3)#define STM32\_SRC\_IC20 (STM32\_SRC\_IC19 + 1)

48

[ 50](stm32n6__clock_8h.md#a186de4b3566a20794e4483a9569abe3c)#define STM32\_CLOCK\_BUS\_AHB1 0x250

[ 51](stm32n6__clock_8h.md#a5e58ef1846c185b04bed598b26ee9205)#define STM32\_CLOCK\_BUS\_AHB2 0x254

[ 52](stm32n6__clock_8h.md#ab2a3c819828eb0186ac3a3f15f4b4569)#define STM32\_CLOCK\_BUS\_AHB3 0x258

[ 53](stm32n6__clock_8h.md#a49bccabc3065f192086f16929a7b762d)#define STM32\_CLOCK\_BUS\_AHB4 0x25C

[ 54](stm32n6__clock_8h.md#a623a8ba4dc47622dfbf76801f1582f58)#define STM32\_CLOCK\_BUS\_AHB5 0x260

[ 55](stm32n6__clock_8h.md#ac763945fc36124f9c978c423826faa95)#define STM32\_CLOCK\_BUS\_APB1 0x264

[ 56](stm32n6__clock_8h.md#ad25510091b50e823c9860089a9f23deb)#define STM32\_CLOCK\_BUS\_APB1\_2 0x268

[ 57](stm32n6__clock_8h.md#adb7becb609763568b91303041c9cd4db)#define STM32\_CLOCK\_BUS\_APB2 0x26C

[ 58](stm32n6__clock_8h.md#af7165e22b71d1beaf0dd4f59d5b4db6d)#define STM32\_CLOCK\_BUS\_APB3 0x270

[ 59](stm32n6__clock_8h.md#a537105e6125ce3b95a2d69435f47dd51)#define STM32\_CLOCK\_BUS\_APB4 0x274

[ 60](stm32n6__clock_8h.md#a4dc3ff62777a32dfc4e76b281a564c86)#define STM32\_CLOCK\_BUS\_APB4\_2 0x278

[ 61](stm32n6__clock_8h.md#a02ec780a692439efebf0bf8181bf7803)#define STM32\_CLOCK\_BUS\_APB5 0x27C

62

[ 63](stm32n6__clock_8h.md#a3931aa4b01e07a95df585779323a7f48)#define STM32\_CLOCK\_LP\_BUS\_SHIFT 0x40

64

[ 65](stm32n6__clock_8h.md#acc0577552371fcda95685f6424ecb4b2)#define STM32\_PERIPH\_BUS\_MIN STM32\_CLOCK\_BUS\_AHB1

[ 66](stm32n6__clock_8h.md#a561265772438ab8995251760c7f3dc30)#define STM32\_PERIPH\_BUS\_MAX STM32\_CLOCK\_BUS\_APB5

67

[ 69](stm32n6__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2)#define CCIPR1\_REG 0x144

[ 70](stm32n6__clock_8h.md#a60349691a29a48b727f302acb8025b89)#define CCIPR2\_REG 0x148

[ 71](stm32n6__clock_8h.md#a302577067fac290b578130da822dc146)#define CCIPR3\_REG 0x14C

[ 72](stm32n6__clock_8h.md#a92eb5c50a767e0f704356d52398f9723)#define CCIPR4\_REG 0x150

[ 73](stm32n6__clock_8h.md#a62e39113c018ae0b2c31254ff003d148)#define CCIPR5\_REG 0x154

[ 74](stm32n6__clock_8h.md#ab00ea8c2d2b0918b738001b972aacf6b)#define CCIPR6\_REG 0x158

[ 75](stm32n6__clock_8h.md#a3fcb658bb097cce8697024fe6b7b44c3)#define CCIPR7\_REG 0x15C

[ 76](stm32n6__clock_8h.md#a43a90b0127d5a177fbebc8c2fac53a79)#define CCIPR8\_REG 0x160

[ 77](stm32n6__clock_8h.md#a3a5cc0435932cbd3235d59f6ce043351)#define CCIPR9\_REG 0x164

[ 78](stm32n6__clock_8h.md#a7cb03c6ceaa338c1850b28a2758e11a8)#define CCIPR12\_REG 0x170

[ 79](stm32n6__clock_8h.md#ac5db8f44fd62365a2b508969767acceb)#define CCIPR13\_REG 0x174

[ 80](stm32n6__clock_8h.md#a07372cf80165afcc7f9297f5b1c33128)#define CCIPR14\_REG 0x178

81

[ 84](stm32n6__clock_8h.md#a2965fce3cbae0a73506ddf383c78783f)#define ADF1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 0, CCIPR1\_REG)

[ 85](stm32n6__clock_8h.md#a937fbb74cf970ef8033c16c68b27400f)#define ADC12\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 4, CCIPR1\_REG)

[ 86](stm32n6__clock_8h.md#a5b9758e95788f06d93382daec60fdf3f)#define DCMIPP\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 20, CCIPR1\_REG)

[ 88](stm32n6__clock_8h.md#aee7f83f9ca88503a6c8b29ba1e220743)#define ETH1PTP\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 0, CCIPR2\_REG)

[ 89](stm32n6__clock_8h.md#a0005c1d3bc4ed6b8c5c30c07051aa4ea)#define ETH1CLK\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 12, CCIPR2\_REG)

[ 90](stm32n6__clock_8h.md#a4e9282866e4f40cf5d6fd0a655fa6fa1)#define ETH1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 16, CCIPR2\_REG)

[ 91](stm32n6__clock_8h.md#ae853e04c239d4321ca2b58c6fcdbe197)#define ETH1REFCLK\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 20, CCIPR2\_REG)

[ 92](stm32n6__clock_8h.md#af972ee87a5e3d879b50b3232af19a794)#define ETH1GTXCLK\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 24, CCIPR2\_REG)

[ 94](stm32n6__clock_8h.md#ac1df6369669b4b3febd0525426e76499)#define FDCAN\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 0, CCIPR3\_REG)

[ 95](stm32n6__clock_8h.md#a0de89c03e0cd384de7f594aa5c5e82de)#define FMC\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 4, CCIPR3\_REG)

[ 97](stm32n6__clock_8h.md#a3fbef8f2542fc6921236bd2709acf64c)#define I2C1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 0, CCIPR4\_REG)

[ 98](stm32n6__clock_8h.md#abdd79c9ce90458b53e81123d181fed98)#define I2C2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 4, CCIPR4\_REG)

[ 99](stm32n6__clock_8h.md#aa12a1d2ac790880b7148d1e5660eb941)#define I2C3\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 8, CCIPR4\_REG)

[ 100](stm32n6__clock_8h.md#a55880006ae28021de4d148924c06001e)#define I2C4\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 12, CCIPR4\_REG)

[ 101](stm32n6__clock_8h.md#a576dca08c22370326fefc540bf056b81)#define I3C1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 16, CCIPR4\_REG)

[ 102](stm32n6__clock_8h.md#a647bc22bf65d67e9e2c5361d0dce925d)#define I3C2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 20, CCIPR4\_REG)

[ 103](stm32n6__clock_8h.md#ac299465bc5d655ecc6dd1e8e7a347e0c)#define LTDC\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 24, CCIPR4\_REG)

[ 105](stm32n6__clock_8h.md#acc5c7aed4e842ca212471d7a58504821)#define MCO1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 0, CCIPR5\_REG)

[ 106](stm32n6__clock_8h.md#ab5fc05cb6aa1154c54c29b95f3154a75)#define MCO2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 8, CCIPR5\_REG)

[ 107](stm32n6__clock_8h.md#a75330910b0ff85fa8a8ccd99f3754970)#define MDF1SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 16, CCIPR5\_REG)

[ 109](stm32n6__clock_8h.md#a15df14366d6921bac34208b0c1af0ebb)#define XSPI1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 0, CCIPR6\_REG)

[ 110](stm32n6__clock_8h.md#a58f2e1e8be7e4e9b50783f03afc687ff)#define XSPI2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 4, CCIPR6\_REG)

[ 111](stm32n6__clock_8h.md#abc02f0330af9bc5e21bccf01204441bc)#define XSPI3\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 8, CCIPR6\_REG)

[ 112](stm32n6__clock_8h.md#a3a59519ef352041f5fc6b73847feff36)#define OTGPHY1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 12, CCIPR6\_REG)

[ 113](stm32n6__clock_8h.md#a0dfca2709116f9933488ac82b894ab75)#define OTGPHY1CKREF\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 16, CCIPR6\_REG)

[ 114](stm32n6__clock_8h.md#a3378b1ba6ba842c341b02c8b3423794c)#define OTGPHY2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 20, CCIPR6\_REG)

[ 115](stm32n6__clock_8h.md#a462cc4388ed9cd167341e583aeb2b9e3)#define OTGPHY2CKREF\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 24, CCIPR6\_REG)

[ 117](stm32n6__clock_8h.md#a822d6e1a5aaaec0e634ea961e18902f6)#define PER\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 0, CCIPR7\_REG)

[ 118](stm32n6__clock_8h.md#af67616db4defc072c759f2f6b6006a9d)#define PSSI\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 4, CCIPR7\_REG)

[ 119](stm32n6__clock_8h.md#a4836377699efa295c56d340e150695b0)#define RTC\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 8, CCIPR7\_REG)

[ 120](stm32n6__clock_8h.md#ab8e49f6309adb53edd9ad3d051d451db)#define SAI1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 20, CCIPR7\_REG)

[ 121](stm32n6__clock_8h.md#a4fb9a6b79339e822f0ae426e8bba7486)#define SAI2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 24, CCIPR7\_REG)

[ 123](stm32n6__clock_8h.md#a1a4999da331afff86581c8a6cea6afe9)#define SDMMC1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 0, CCIPR8\_REG)

[ 124](stm32n6__clock_8h.md#a7319710d63129ad13039565cad2b4950)#define SDMMC2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 4, CCIPR8\_REG)

[ 126](stm32n6__clock_8h.md#a9559c1e35f44860aee803e7269e9cede)#define SPDIFRX1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 0, CCIPR9\_REG)

[ 127](stm32n6__clock_8h.md#a5199102173e9dbe957230f356e14d910)#define SPI1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 4, CCIPR9\_REG)

[ 128](stm32n6__clock_8h.md#ad3e84eac634b9d943acea9b2ab884fb5)#define SPI2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 8, CCIPR9\_REG)

[ 129](stm32n6__clock_8h.md#aaa096904d8a97bedc81f9a565e65c332)#define SPI3\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 12, CCIPR9\_REG)

[ 130](stm32n6__clock_8h.md#a55086a94321a6e1af527a46c644f6c5e)#define SPI4\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 16, CCIPR9\_REG)

[ 131](stm32n6__clock_8h.md#ac7193e508815171a4d73795d24086136)#define SPI5\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 20, CCIPR9\_REG)

[ 132](stm32n6__clock_8h.md#ab43d49ec71267eb1d8002909cc3360bf)#define SPI6\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 24, CCIPR9\_REG)

[ 134](stm32n6__clock_8h.md#a042804bf8a52b3dd28033f8814442bfb)#define LPTIM1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 8, CCIPR12\_REG)

[ 135](stm32n6__clock_8h.md#aa713f6ff001bfa6352747e7a66e3f98a)#define LPTIM2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 12, CCIPR12\_REG)

[ 136](stm32n6__clock_8h.md#ac705aa5789ca3b11ac5115d22ec2a5e5)#define LPTIM3\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 16, CCIPR12\_REG)

[ 137](stm32n6__clock_8h.md#a7c23812b481c3743f393d301d7cf7e27)#define LPTIM4\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 20, CCIPR12\_REG)

[ 138](stm32n6__clock_8h.md#ad508257c2f92e7ced0f6317ea3397965)#define LPTIM5\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 24, CCIPR12\_REG)

[ 140](stm32n6__clock_8h.md#a17f3ec5f86995a2c4087f2988a9486c5)#define USART1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 0, CCIPR13\_REG)

[ 141](stm32n6__clock_8h.md#ad67d92dfc439018a7a231e661d10d7f9)#define USART2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 4, CCIPR13\_REG)

[ 142](stm32n6__clock_8h.md#ad2f356c0bc0e43d6f629cdb840846526)#define USART3\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 8, CCIPR13\_REG)

[ 143](stm32n6__clock_8h.md#a091d597b4979c49951f880bc6ccb4d71)#define UART4\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 12, CCIPR13\_REG)

[ 144](stm32n6__clock_8h.md#a136c2c36c89ebdf2c5b97686bbce0209)#define UART5\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 16, CCIPR13\_REG)

[ 145](stm32n6__clock_8h.md#a99c9026d61766ec9b91872ee64ad63eb)#define USART6\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 20, CCIPR13\_REG)

[ 146](stm32n6__clock_8h.md#a2d0071bb5cc287b8be749d8abcca6eab)#define UART7\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 24, CCIPR13\_REG)

[ 147](stm32n6__clock_8h.md#a1b66b237c80c002bc2b422d8fbf61824)#define UART8\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 28, CCIPR13\_REG)

[ 149](stm32n6__clock_8h.md#a866e45ef86e20589a96ae4533382fb5b)#define UART9\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 0, CCIPR14\_REG)

[ 150](stm32n6__clock_8h.md#a5eef37bd8c6a90bf0de08faf5d05f410)#define USART10\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 4, CCIPR14\_REG)

[ 151](stm32n6__clock_8h.md#aac31ca48bf87a722f6e0519f25f764dd)#define LPUART1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 7, 8, CCIPR14\_REG)

152

[ 154](stm32n6__clock_8h.md#a3e7bf66713ac3a485e415ff3635fff0e)#define ICxCFGR\_REG(ic) (0xC4 + ((ic) - 1) \* 4)

155

[ 157](stm32n6__clock_8h.md#aaa6058bcba48e870acb5ee09a338bf0c)#define ICx\_PLLy\_SEL(ic, pll) STM32\_DT\_CLOCK\_SELECT((pll) - 1, 3, 28, ICxCFGR\_REG(ic))

158

[ 160](stm32n6__clock_8h.md#a6b894fe6e036f03831faddf28bce43c6)#define CFGR1\_REG 0x20

161

[ 163](stm32n6__clock_8h.md#a640e40ac4ae8af3906b84267d5ee7bea)#define CPU\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 16, CFGR1\_REG)

164

165#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32N6\_CLOCK\_H\_ \*/

[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32n6\_clock.h](stm32n6__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
