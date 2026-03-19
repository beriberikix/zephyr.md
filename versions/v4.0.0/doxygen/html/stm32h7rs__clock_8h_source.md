---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stm32h7rs__clock_8h_source.html
original_path: doxygen/html/stm32h7rs__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32h7rs\_clock.h

[Go to the documentation of this file.](stm32h7rs__clock_8h.md)

1/\*

2 \* Copyright (c) 2024 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32H7RS\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32H7RS\_CLOCK\_H\_

8

9#include "[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)"

10

12

13/\* RM0477 \*/

14

16/\* defined in stm32\_common\_clocks.h \*/

17

19/\* Low speed clocks defined in stm32\_common\_clocks.h \*/

[ 20](stm32h7rs__clock_8h.md#aa7e82706a146d0f40dc7e9755b3be9a6)#define STM32\_SRC\_HSE (STM32\_SRC\_LSI + 1)

[ 21](stm32h7rs__clock_8h.md#ae12e6bda1c30174c98303f692a42960f)#define STM32\_SRC\_HSI48 (STM32\_SRC\_HSE + 1)

[ 22](stm32h7rs__clock_8h.md#ab574ca48f488778e54bdabcd78588ed4)#define STM32\_SRC\_HSI\_KER (STM32\_SRC\_HSI48 + 1) /\* HSI + HSIKERON \*/

[ 23](stm32h7rs__clock_8h.md#a469a687b3d587b881bd607634251faf4)#define STM32\_SRC\_CSI\_KER (STM32\_SRC\_HSI\_KER + 1) /\* CSI + CSIKERON \*/

[ 25](stm32h7rs__clock_8h.md#aa074615a92c5ff479f4fbed6fdf27f62)#define STM32\_SRC\_PLL1\_P (STM32\_SRC\_CSI\_KER + 1)

[ 26](stm32h7rs__clock_8h.md#a6edb3dc598055ceeb82045fdee647637)#define STM32\_SRC\_PLL1\_Q (STM32\_SRC\_PLL1\_P + 1)

[ 27](stm32h7rs__clock_8h.md#a6063632b32a970b9abbf711bab8a77c9)#define STM32\_SRC\_PLL1\_R (STM32\_SRC\_PLL1\_Q + 1)

[ 28](stm32h7rs__clock_8h.md#a1f1f827655145092dcab97dfe64e1635)#define STM32\_SRC\_PLL1\_S (STM32\_SRC\_PLL1\_R + 1)

[ 29](stm32h7rs__clock_8h.md#ae568673a4eca1b42afc59faabb5810ac)#define STM32\_SRC\_PLL2\_P (STM32\_SRC\_PLL1\_S + 1)

[ 30](stm32h7rs__clock_8h.md#aaf0a956dda42c2a031cabce49dd3e717)#define STM32\_SRC\_PLL2\_Q (STM32\_SRC\_PLL2\_P + 1)

[ 31](stm32h7rs__clock_8h.md#a57af8944eefa865aa75b6286c13a53cd)#define STM32\_SRC\_PLL2\_R (STM32\_SRC\_PLL2\_Q + 1)

[ 32](stm32h7rs__clock_8h.md#a889eff1dbeacc7caa4c4c7652a0d97cd)#define STM32\_SRC\_PLL2\_S (STM32\_SRC\_PLL2\_R + 1)

[ 33](stm32h7rs__clock_8h.md#a723ae1f1b3d7270a9ea197c7fff27e8b)#define STM32\_SRC\_PLL2\_T (STM32\_SRC\_PLL2\_S + 1)

[ 34](stm32h7rs__clock_8h.md#a17c753e0bb8547ea9452f48a65a0a206)#define STM32\_SRC\_PLL3\_P (STM32\_SRC\_PLL2\_T + 1)

[ 35](stm32h7rs__clock_8h.md#a9a31a3adebff6a1eee31c287673412c9)#define STM32\_SRC\_PLL3\_Q (STM32\_SRC\_PLL3\_P + 1)

[ 36](stm32h7rs__clock_8h.md#a604c22ff137a35cd1725b70991696f9a)#define STM32\_SRC\_PLL3\_R (STM32\_SRC\_PLL3\_Q + 1)

[ 37](stm32h7rs__clock_8h.md#a4f7f8d0ce944e5cdb1a3722d0487c73f)#define STM32\_SRC\_PLL3\_S (STM32\_SRC\_PLL3\_R + 1)

38

[ 40](stm32h7rs__clock_8h.md#a8b7025d7f4be00a152c53097a414668e)#define STM32\_SRC\_CKPER (STM32\_SRC\_PLL3\_S + 1)

42

[ 44](stm32h7rs__clock_8h.md#a186de4b3566a20794e4483a9569abe3c)#define STM32\_CLOCK\_BUS\_AHB1 0x138

[ 45](stm32h7rs__clock_8h.md#a5e58ef1846c185b04bed598b26ee9205)#define STM32\_CLOCK\_BUS\_AHB2 0x13C

[ 46](stm32h7rs__clock_8h.md#ab2a3c819828eb0186ac3a3f15f4b4569)#define STM32\_CLOCK\_BUS\_AHB3 0x158

[ 47](stm32h7rs__clock_8h.md#a49bccabc3065f192086f16929a7b762d)#define STM32\_CLOCK\_BUS\_AHB4 0x140

[ 48](stm32h7rs__clock_8h.md#a623a8ba4dc47622dfbf76801f1582f58)#define STM32\_CLOCK\_BUS\_AHB5 0x134

[ 49](stm32h7rs__clock_8h.md#ac763945fc36124f9c978c423826faa95)#define STM32\_CLOCK\_BUS\_APB1 0x148

[ 50](stm32h7rs__clock_8h.md#ad25510091b50e823c9860089a9f23deb)#define STM32\_CLOCK\_BUS\_APB1\_2 0x14C

[ 51](stm32h7rs__clock_8h.md#adb7becb609763568b91303041c9cd4db)#define STM32\_CLOCK\_BUS\_APB2 0x150

[ 52](stm32h7rs__clock_8h.md#a537105e6125ce3b95a2d69435f47dd51)#define STM32\_CLOCK\_BUS\_APB4 0x154

[ 53](stm32h7rs__clock_8h.md#a02ec780a692439efebf0bf8181bf7803)#define STM32\_CLOCK\_BUS\_APB5 0x144

[ 54](stm32h7rs__clock_8h.md#acc0577552371fcda95685f6424ecb4b2)#define STM32\_PERIPH\_BUS\_MIN STM32\_CLOCK\_BUS\_AHB5

[ 55](stm32h7rs__clock_8h.md#a561265772438ab8995251760c7f3dc30)#define STM32\_PERIPH\_BUS\_MAX STM32\_CLOCK\_BUS\_AHB3

56

[ 57](stm32h7rs__clock_8h.md#a33d66849c63db64784317260b06ceb24)#define STM32\_CLOCK\_REG\_MASK 0xFFU

[ 58](stm32h7rs__clock_8h.md#a2e73bdb1691751ffd616a5c4e2762423)#define STM32\_CLOCK\_REG\_SHIFT 0U

[ 59](stm32h7rs__clock_8h.md#af3001a7541ea4df9e4948fd559352f60)#define STM32\_CLOCK\_SHIFT\_MASK 0x1FU

[ 60](stm32h7rs__clock_8h.md#a147846b77bd51e42c85bea5aca50ad4f)#define STM32\_CLOCK\_SHIFT\_SHIFT 8U

[ 61](stm32h7rs__clock_8h.md#a63ecbd205c0dd6cb3eab7bcbfdce38b9)#define STM32\_CLOCK\_MASK\_MASK 0x7U

[ 62](stm32h7rs__clock_8h.md#abfdb31d824fc5c6cf809a1dcff022b5d)#define STM32\_CLOCK\_MASK\_SHIFT 13U

[ 63](stm32h7rs__clock_8h.md#a6b4f80c7dbd047ca1ebac0b233ad1d1b)#define STM32\_CLOCK\_VAL\_MASK 0x7U

[ 64](stm32h7rs__clock_8h.md#adf2ca8c7f707b82b7ec4820dfc32929a)#define STM32\_CLOCK\_VAL\_SHIFT 16U

65

[ 79](stm32h7rs__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)#define STM32\_DOMAIN\_CLOCK(val, mask, shift, reg) \

80 ((((reg) & STM32\_CLOCK\_REG\_MASK) << STM32\_CLOCK\_REG\_SHIFT) | \

81 (((shift) & STM32\_CLOCK\_SHIFT\_MASK) << STM32\_CLOCK\_SHIFT\_SHIFT) | \

82 (((mask) & STM32\_CLOCK\_MASK\_MASK) << STM32\_CLOCK\_MASK\_SHIFT) | \

83 (((val) & STM32\_CLOCK\_VAL\_MASK) << STM32\_CLOCK\_VAL\_SHIFT))

84

[ 86](stm32h7rs__clock_8h.md#a9a43f736d68c30870b3f1ee545b2cff9)#define D1CCIPR\_REG 0x4C

[ 87](stm32h7rs__clock_8h.md#a48fb7022d239e385aa7f41d21e43cefd)#define D2CCIPR\_REG 0x50

[ 88](stm32h7rs__clock_8h.md#aeda9dd86b920e734a85ce06acbd75eda)#define D3CCIPR\_REG 0x54

[ 89](stm32h7rs__clock_8h.md#af95b3aebb687a8508719c0e93bda8b74)#define D4CCIPR\_REG 0x58

90

[ 92](stm32h7rs__clock_8h.md#a70a10f70b4f5058508e8983ad0a4de3a)#define BDCR\_REG 0x70

93

[ 95](stm32h7rs__clock_8h.md#afb2336a33a23f9671b26010594232ba3)#define CFGR\_REG 0x10

96

98

99/\* TODO to be completed \*/

100

[ 102](stm32h7rs__clock_8h.md#a0de89c03e0cd384de7f594aa5c5e82de)#define FMC\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 0, D1CCIPR\_REG)

[ 103](stm32h7rs__clock_8h.md#a42688c1d17e09ab58029feedd7491c0b)#define SDMMC\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 1, 2, D1CCIPR\_REG)

[ 104](stm32h7rs__clock_8h.md#a15df14366d6921bac34208b0c1af0ebb)#define XSPI1\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 4, D1CCIPR\_REG)

[ 105](stm32h7rs__clock_8h.md#a58f2e1e8be7e4e9b50783f03afc687ff)#define XSPI2\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 6, D1CCIPR\_REG)

[ 106](stm32h7rs__clock_8h.md#a635d17ad991ded52d41a6e7b0bec5773)#define ADC\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 24, D1CCIPR\_REG)

[ 107](stm32h7rs__clock_8h.md#adc32e4d489d72766d6df1783eedf7628)#define CKPER\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 28, D1CCIPR\_REG)

108

[ 110](stm32h7rs__clock_8h.md#af81b9ee44136b6468393f807e70bbbf0)#define USART234578\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 7, 0, D2CCIPR\_REG)

[ 111](stm32h7rs__clock_8h.md#ad760ef96e4fd9ca527e7d9c746d1c9f3)#define SPI23\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 7, 4, D2CCIPR\_REG)

[ 112](stm32h7rs__clock_8h.md#a490889daf5612d2f0f08b3cab473ef10)#define I2C23\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 8, D2CCIPR\_REG)

[ 113](stm32h7rs__clock_8h.md#a3fbef8f2542fc6921236bd2709acf64c)#define I2C1\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 12, D2CCIPR\_REG)

[ 114](stm32h7rs__clock_8h.md#a576dca08c22370326fefc540bf056b81)#define I3C1\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 12, D2CCIPR\_REG)

[ 115](stm32h7rs__clock_8h.md#a042804bf8a52b3dd28033f8814442bfb)#define LPTIM1\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 7, 16, D2CCIPR\_REG)

[ 116](stm32h7rs__clock_8h.md#ac1df6369669b4b3febd0525426e76499)#define FDCAN\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 22, D2CCIPR\_REG)

117

[ 119](stm32h7rs__clock_8h.md#a17f3ec5f86995a2c4087f2988a9486c5)#define USART1\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 7, 0, D3CCIPR\_REG)

[ 120](stm32h7rs__clock_8h.md#a6919b0ea063667adb88c7c2d79877426)#define SPI45\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 7, 4, D3CCIPR\_REG)

[ 121](stm32h7rs__clock_8h.md#a5199102173e9dbe957230f356e14d910)#define SPI1\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 7, 8, D3CCIPR\_REG)

[ 122](stm32h7rs__clock_8h.md#ab8e49f6309adb53edd9ad3d051d451db)#define SAI1\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 7, 16, D3CCIPR\_REG)

[ 123](stm32h7rs__clock_8h.md#a4fb9a6b79339e822f0ae426e8bba7486)#define SAI2\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 7, 20, D3CCIPR\_REG)

124

[ 126](stm32h7rs__clock_8h.md#aac31ca48bf87a722f6e0519f25f764dd)#define LPUART1\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 7, 0, D4CCIPR\_REG)

[ 127](stm32h7rs__clock_8h.md#ab43d49ec71267eb1d8002909cc3360bf)#define SPI6\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 7, 4, D4CCIPR\_REG)

[ 128](stm32h7rs__clock_8h.md#a07706332b9bea6a82d90e93b9ea70293)#define LPTIM23\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 7, 8, D4CCIPR\_REG)

[ 129](stm32h7rs__clock_8h.md#ad44ca291fceaacfa1794f08034143dc8)#define LPTIM45\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 7, 12, D4CCIPR\_REG)

130

[ 132](stm32h7rs__clock_8h.md#a4836377699efa295c56d340e150695b0)#define RTC\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 8, BDCR\_REG)

133

[ 135](stm32h7rs__clock_8h.md#acc5c7aed4e842ca212471d7a58504821)#define MCO1\_SEL(val) STM32\_MCO\_CFGR(val, 0x7, 22, CFGR\_REG)

[ 136](stm32h7rs__clock_8h.md#a2805cf7e0b5ed0a9bb4bfff863327081)#define MCO1\_PRE(val) STM32\_MCO\_CFGR(val, 0xF, 18, CFGR\_REG)

[ 137](stm32h7rs__clock_8h.md#ab5fc05cb6aa1154c54c29b95f3154a75)#define MCO2\_SEL(val) STM32\_MCO\_CFGR(val, 0x7, 29, CFGR\_REG)

[ 138](stm32h7rs__clock_8h.md#ab02a0ccbb8588979ca4742c72c59589f)#define MCO2\_PRE(val) STM32\_MCO\_CFGR(val, 0xF, 25, CFGR\_REG)

139

140#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32H7RS\_CLOCK\_H\_ \*/

[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32h7rs\_clock.h](stm32h7rs__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
