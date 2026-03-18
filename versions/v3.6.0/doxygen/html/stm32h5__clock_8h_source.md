---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/stm32h5__clock_8h_source.html
original_path: doxygen/html/stm32h5__clock_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32h5\_clock.h

[Go to the documentation of this file.](stm32h5__clock_8h.md)

1/\*

2 \* Copyright (c) 2023 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32H5\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32H5\_CLOCK\_H\_

8

9#include "[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)"

10

12

13/\* RM0481/0492, Table 47 Kernel clock distribution summary \*/

14

16/\* defined in stm32\_common\_clocks.h \*/

18/\* Low speed clocks defined in stm32\_common\_clocks.h \*/

[ 19](stm32h5__clock_8h.md#aa7e82706a146d0f40dc7e9755b3be9a6)#define STM32\_SRC\_HSE (STM32\_SRC\_LSI + 1)

[ 20](stm32h5__clock_8h.md#ac1c5062f5053fe96a5c2ba12d868eeda)#define STM32\_SRC\_CSI (STM32\_SRC\_HSE + 1)

[ 21](stm32h5__clock_8h.md#a7bc1dd03186b763b407a044ddffb4ab2)#define STM32\_SRC\_HSI (STM32\_SRC\_CSI + 1)

[ 22](stm32h5__clock_8h.md#ae12e6bda1c30174c98303f692a42960f)#define STM32\_SRC\_HSI48 (STM32\_SRC\_HSI + 1)

[ 24](stm32h5__clock_8h.md#aa074615a92c5ff479f4fbed6fdf27f62)#define STM32\_SRC\_PLL1\_P (STM32\_SRC\_HSI48 + 1)

[ 25](stm32h5__clock_8h.md#a6edb3dc598055ceeb82045fdee647637)#define STM32\_SRC\_PLL1\_Q (STM32\_SRC\_PLL1\_P + 1)

[ 26](stm32h5__clock_8h.md#a6063632b32a970b9abbf711bab8a77c9)#define STM32\_SRC\_PLL1\_R (STM32\_SRC\_PLL1\_Q + 1)

[ 27](stm32h5__clock_8h.md#ae568673a4eca1b42afc59faabb5810ac)#define STM32\_SRC\_PLL2\_P (STM32\_SRC\_PLL1\_R + 1)

[ 28](stm32h5__clock_8h.md#aaf0a956dda42c2a031cabce49dd3e717)#define STM32\_SRC\_PLL2\_Q (STM32\_SRC\_PLL2\_P + 1)

[ 29](stm32h5__clock_8h.md#a57af8944eefa865aa75b6286c13a53cd)#define STM32\_SRC\_PLL2\_R (STM32\_SRC\_PLL2\_Q + 1)

[ 30](stm32h5__clock_8h.md#a17c753e0bb8547ea9452f48a65a0a206)#define STM32\_SRC\_PLL3\_P (STM32\_SRC\_PLL2\_R + 1)

[ 31](stm32h5__clock_8h.md#a9a31a3adebff6a1eee31c287673412c9)#define STM32\_SRC\_PLL3\_Q (STM32\_SRC\_PLL3\_P + 1)

[ 32](stm32h5__clock_8h.md#a604c22ff137a35cd1725b70991696f9a)#define STM32\_SRC\_PLL3\_R (STM32\_SRC\_PLL3\_Q + 1)

[ 34](stm32h5__clock_8h.md#a8b7025d7f4be00a152c53097a414668e)#define STM32\_SRC\_CKPER (STM32\_SRC\_PLL3\_R + 1)

35

36

[ 38](stm32h5__clock_8h.md#a186de4b3566a20794e4483a9569abe3c)#define STM32\_CLOCK\_BUS\_AHB1 0x088

[ 39](stm32h5__clock_8h.md#a5e58ef1846c185b04bed598b26ee9205)#define STM32\_CLOCK\_BUS\_AHB2 0x08C

[ 40](stm32h5__clock_8h.md#a49bccabc3065f192086f16929a7b762d)#define STM32\_CLOCK\_BUS\_AHB4 0x094

[ 41](stm32h5__clock_8h.md#ac763945fc36124f9c978c423826faa95)#define STM32\_CLOCK\_BUS\_APB1 0x09c

[ 42](stm32h5__clock_8h.md#ad25510091b50e823c9860089a9f23deb)#define STM32\_CLOCK\_BUS\_APB1\_2 0x0A0

[ 43](stm32h5__clock_8h.md#adb7becb609763568b91303041c9cd4db)#define STM32\_CLOCK\_BUS\_APB2 0x0A4

[ 44](stm32h5__clock_8h.md#af7165e22b71d1beaf0dd4f59d5b4db6d)#define STM32\_CLOCK\_BUS\_APB3 0x0A8

45

[ 46](stm32h5__clock_8h.md#acc0577552371fcda95685f6424ecb4b2)#define STM32\_PERIPH\_BUS\_MIN STM32\_CLOCK\_BUS\_AHB1

[ 47](stm32h5__clock_8h.md#a561265772438ab8995251760c7f3dc30)#define STM32\_PERIPH\_BUS\_MAX STM32\_CLOCK\_BUS\_APB3

48

[ 49](stm32h5__clock_8h.md#a33d66849c63db64784317260b06ceb24)#define STM32\_CLOCK\_REG\_MASK 0xFFU

[ 50](stm32h5__clock_8h.md#a2e73bdb1691751ffd616a5c4e2762423)#define STM32\_CLOCK\_REG\_SHIFT 0U

[ 51](stm32h5__clock_8h.md#af3001a7541ea4df9e4948fd559352f60)#define STM32\_CLOCK\_SHIFT\_MASK 0x1FU

[ 52](stm32h5__clock_8h.md#a147846b77bd51e42c85bea5aca50ad4f)#define STM32\_CLOCK\_SHIFT\_SHIFT 8U

[ 53](stm32h5__clock_8h.md#a63ecbd205c0dd6cb3eab7bcbfdce38b9)#define STM32\_CLOCK\_MASK\_MASK 0x7U

[ 54](stm32h5__clock_8h.md#abfdb31d824fc5c6cf809a1dcff022b5d)#define STM32\_CLOCK\_MASK\_SHIFT 13U

[ 55](stm32h5__clock_8h.md#a6b4f80c7dbd047ca1ebac0b233ad1d1b)#define STM32\_CLOCK\_VAL\_MASK 0x7U

[ 56](stm32h5__clock_8h.md#adf2ca8c7f707b82b7ec4820dfc32929a)#define STM32\_CLOCK\_VAL\_SHIFT 16U

57

[ 71](stm32h5__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)#define STM32\_CLOCK(val, mask, shift, reg) \

72 ((((reg) & STM32\_CLOCK\_REG\_MASK) << STM32\_CLOCK\_REG\_SHIFT) | \

73 (((shift) & STM32\_CLOCK\_SHIFT\_MASK) << STM32\_CLOCK\_SHIFT\_SHIFT) | \

74 (((mask) & STM32\_CLOCK\_MASK\_MASK) << STM32\_CLOCK\_MASK\_SHIFT) | \

75 (((val) & STM32\_CLOCK\_VAL\_MASK) << STM32\_CLOCK\_VAL\_SHIFT))

76

[ 78](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2)#define CCIPR1\_REG 0xD8

[ 79](stm32h5__clock_8h.md#a60349691a29a48b727f302acb8025b89)#define CCIPR2\_REG 0xDC

[ 80](stm32h5__clock_8h.md#a302577067fac290b578130da822dc146)#define CCIPR3\_REG 0xE0

[ 81](stm32h5__clock_8h.md#a92eb5c50a767e0f704356d52398f9723)#define CCIPR4\_REG 0xE4

[ 82](stm32h5__clock_8h.md#a62e39113c018ae0b2c31254ff003d148)#define CCIPR5\_REG 0xE8

83

[ 85](stm32h5__clock_8h.md#a70a10f70b4f5058508e8983ad0a4de3a)#define BDCR\_REG 0xF0

86

[ 89](stm32h5__clock_8h.md#a17f3ec5f86995a2c4087f2988a9486c5)#define USART1\_SEL(val) STM32\_CLOCK(val, 7, 0, CCIPR1\_REG)

[ 90](stm32h5__clock_8h.md#ad67d92dfc439018a7a231e661d10d7f9)#define USART2\_SEL(val) STM32\_CLOCK(val, 7, 3, CCIPR1\_REG)

[ 91](stm32h5__clock_8h.md#ad2f356c0bc0e43d6f629cdb840846526)#define USART3\_SEL(val) STM32\_CLOCK(val, 7, 6, CCIPR1\_REG)

[ 92](stm32h5__clock_8h.md#aced9e983095cb40bc18f3a66e3818c98)#define USART4\_SEL(val) STM32\_CLOCK(val, 7, 9, CCIPR1\_REG)

[ 93](stm32h5__clock_8h.md#a6a45e0ef8bd196574e241aefdb3a5350)#define USART5\_SEL(val) STM32\_CLOCK(val, 7, 12, CCIPR1\_REG)

[ 94](stm32h5__clock_8h.md#a99c9026d61766ec9b91872ee64ad63eb)#define USART6\_SEL(val) STM32\_CLOCK(val, 7, 15, CCIPR1\_REG)

[ 95](stm32h5__clock_8h.md#a085ea149cac54d39aef4cb9f5c03402c)#define USART7\_SEL(val) STM32\_CLOCK(val, 7, 18, CCIPR1\_REG)

[ 96](stm32h5__clock_8h.md#adf99875c4c7a62e255871678fe848645)#define USART8\_SEL(val) STM32\_CLOCK(val, 7, 21, CCIPR1\_REG)

[ 97](stm32h5__clock_8h.md#a2bb43ceb46c7cb47f946c868a9e5b0aa)#define USART9\_SEL(val) STM32\_CLOCK(val, 7, 24, CCIPR1\_REG)

[ 98](stm32h5__clock_8h.md#a5eef37bd8c6a90bf0de08faf5d05f410)#define USART10\_SEL(val) STM32\_CLOCK(val, 7, 27, CCIPR1\_REG)

[ 99](stm32h5__clock_8h.md#ad39b85aaa947648b1b833b1414116f51)#define TIMIC\_SEL(val) STM32\_CLOCK(val, 1, 31, CCIPR1\_REG)

100

[ 102](stm32h5__clock_8h.md#adc9bd02facff6c4513f4fe8cb43fe9be)#define USART11\_SEL(val) STM32\_CLOCK(val, 7, 0, CCIPR2\_REG)

[ 103](stm32h5__clock_8h.md#a2ce5c32e9d923116b1ef96e415876866)#define USART12\_SEL(val) STM32\_CLOCK(val, 7, 4, CCIPR2\_REG)

[ 104](stm32h5__clock_8h.md#a042804bf8a52b3dd28033f8814442bfb)#define LPTIM1\_SEL(val) STM32\_CLOCK(val, 7, 8, CCIPR2\_REG)

[ 105](stm32h5__clock_8h.md#aa713f6ff001bfa6352747e7a66e3f98a)#define LPTIM2\_SEL(val) STM32\_CLOCK(val, 7, 12, CCIPR2\_REG)

[ 106](stm32h5__clock_8h.md#ac705aa5789ca3b11ac5115d22ec2a5e5)#define LPTIM3\_SEL(val) STM32\_CLOCK(val, 7, 16, CCIPR2\_REG)

[ 107](stm32h5__clock_8h.md#a7c23812b481c3743f393d301d7cf7e27)#define LPTIM4\_SEL(val) STM32\_CLOCK(val, 7, 20, CCIPR2\_REG)

[ 108](stm32h5__clock_8h.md#ad508257c2f92e7ced0f6317ea3397965)#define LPTIM5\_SEL(val) STM32\_CLOCK(val, 7, 24, CCIPR2\_REG)

[ 109](stm32h5__clock_8h.md#a6ed1256c9ec56f7377d16aa4993379b1)#define LPTIM6\_SEL(val) STM32\_CLOCK(val, 7, 28, CCIPR2\_REG)

110

[ 112](stm32h5__clock_8h.md#a5199102173e9dbe957230f356e14d910)#define SPI1\_SEL(val) STM32\_CLOCK(val, 7, 0, CCIPR3\_REG)

[ 113](stm32h5__clock_8h.md#ad3e84eac634b9d943acea9b2ab884fb5)#define SPI2\_SEL(val) STM32\_CLOCK(val, 7, 3, CCIPR3\_REG)

[ 114](stm32h5__clock_8h.md#aaa096904d8a97bedc81f9a565e65c332)#define SPI3\_SEL(val) STM32\_CLOCK(val, 7, 6, CCIPR3\_REG)

[ 115](stm32h5__clock_8h.md#a55086a94321a6e1af527a46c644f6c5e)#define SPI4\_SEL(val) STM32\_CLOCK(val, 7, 9, CCIPR3\_REG)

[ 116](stm32h5__clock_8h.md#ac7193e508815171a4d73795d24086136)#define SPI5\_SEL(val) STM32\_CLOCK(val, 7, 12, CCIPR3\_REG)

[ 117](stm32h5__clock_8h.md#ab43d49ec71267eb1d8002909cc3360bf)#define SPI6\_SEL(val) STM32\_CLOCK(val, 7, 15, CCIPR2\_REG)

[ 118](stm32h5__clock_8h.md#aac31ca48bf87a722f6e0519f25f764dd)#define LPUART1\_SEL(val) STM32\_CLOCK(val, 7, 24, CCIPR3\_REG)

119

[ 121](stm32h5__clock_8h.md#a50fd0ec19b392357f55331cc031b34fd)#define OCTOSPI1\_SEL(val) STM32\_CLOCK(val, 3, 0, CCIPR4\_REG)

[ 122](stm32h5__clock_8h.md#a9319a91fb044022ba812f616cf192f65)#define SYSTICK\_SEL(val) STM32\_CLOCK(val, 3, 2, CCIPR4\_REG)

[ 123](stm32h5__clock_8h.md#a3247ad782f1e2c7db84989d03831139b)#define USB\_SEL(val) STM32\_CLOCK(val, 3, 4, CCIPR4\_REG)

[ 124](stm32h5__clock_8h.md#a1a4999da331afff86581c8a6cea6afe9)#define SDMMC1\_SEL(val) STM32\_CLOCK(val, 1, 6, CCIPR4\_REG)

[ 125](stm32h5__clock_8h.md#a7319710d63129ad13039565cad2b4950)#define SDMMC2\_SEL(val) STM32\_CLOCK(val, 1, 7, CCIPR4\_REG)

[ 126](stm32h5__clock_8h.md#a3fbef8f2542fc6921236bd2709acf64c)#define I2C1\_SEL(val) STM32\_CLOCK(val, 3, 16, CCIPR4\_REG)

[ 127](stm32h5__clock_8h.md#abdd79c9ce90458b53e81123d181fed98)#define I2C2\_SEL(val) STM32\_CLOCK(val, 3, 18, CCIPR4\_REG)

[ 128](stm32h5__clock_8h.md#aa12a1d2ac790880b7148d1e5660eb941)#define I2C3\_SEL(val) STM32\_CLOCK(val, 3, 20, CCIPR4\_REG)

[ 129](stm32h5__clock_8h.md#a55880006ae28021de4d148924c06001e)#define I2C4\_SEL(val) STM32\_CLOCK(val, 3, 22, CCIPR4\_REG)

[ 130](stm32h5__clock_8h.md#a576dca08c22370326fefc540bf056b81)#define I3C1\_SEL(val) STM32\_CLOCK(val, 3, 24, CCIPR4\_REG)

131

[ 133](stm32h5__clock_8h.md#a454d6254cea3749ac4502fb51739e27c)#define ADCDAC\_SEL(val) STM32\_CLOCK(val, 7, 0, CCIPR5\_REG)

[ 134](stm32h5__clock_8h.md#a08f184d6404d9982facc8fe8a92ed5a8)#define DAC\_SEL(val) STM32\_CLOCK(val, 1, 3, CCIPR5\_REG)

[ 135](stm32h5__clock_8h.md#abfff4355a498febbcf4ebcb237930a57)#define RNG\_SEL(val) STM32\_CLOCK(val, 3, 4, CCIPR5\_REG)

[ 136](stm32h5__clock_8h.md#affd653e901474991857a29deba53cf82)#define CEC\_SEL(val) STM32\_CLOCK(val, 3, 6, CCIPR5\_REG)

[ 137](stm32h5__clock_8h.md#ac1df6369669b4b3febd0525426e76499)#define FDCAN\_SEL(val) STM32\_CLOCK(val, 3, 8, CCIPR5\_REG)

[ 138](stm32h5__clock_8h.md#ab8e49f6309adb53edd9ad3d051d451db)#define SAI1\_SEL(val) STM32\_CLOCK(val, 7, 16, CCIPR5\_REG)

[ 139](stm32h5__clock_8h.md#a4fb9a6b79339e822f0ae426e8bba7486)#define SAI2\_SEL(val) STM32\_CLOCK(val, 7, 19, CCIPR5\_REG)

[ 140](stm32h5__clock_8h.md#adc32e4d489d72766d6df1783eedf7628)#define CKPER\_SEL(val) STM32\_CLOCK(val, 3, 30, CCIPR5\_REG)

141

[ 143](stm32h5__clock_8h.md#a4836377699efa295c56d340e150695b0)#define RTC\_SEL(val) STM32\_CLOCK(val, 3, 8, BDCR\_REG)

144

145#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32H5\_CLOCK\_H\_ \*/

[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32h5\_clock.h](stm32h5__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
