---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/stm32f7__clock_8h_source.html
original_path: doxygen/html/stm32f7__clock_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32f7\_clock.h

[Go to the documentation of this file.](stm32f7__clock_8h.md)

1/\*

2 \* Copyright (c) 2022 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32F7\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32F7\_CLOCK\_H\_

8

9#include "[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)"

10

12

[ 14](stm32f7__clock_8h.md#a186de4b3566a20794e4483a9569abe3c)#define STM32\_CLOCK\_BUS\_AHB1 0x030

[ 15](stm32f7__clock_8h.md#a5e58ef1846c185b04bed598b26ee9205)#define STM32\_CLOCK\_BUS\_AHB2 0x034

[ 16](stm32f7__clock_8h.md#ab2a3c819828eb0186ac3a3f15f4b4569)#define STM32\_CLOCK\_BUS\_AHB3 0x038

[ 17](stm32f7__clock_8h.md#ac763945fc36124f9c978c423826faa95)#define STM32\_CLOCK\_BUS\_APB1 0x040

[ 18](stm32f7__clock_8h.md#adb7becb609763568b91303041c9cd4db)#define STM32\_CLOCK\_BUS\_APB2 0x044

[ 19](stm32f7__clock_8h.md#af7165e22b71d1beaf0dd4f59d5b4db6d)#define STM32\_CLOCK\_BUS\_APB3 0x0A8

20

[ 21](stm32f7__clock_8h.md#acc0577552371fcda95685f6424ecb4b2)#define STM32\_PERIPH\_BUS\_MIN STM32\_CLOCK\_BUS\_AHB1

[ 22](stm32f7__clock_8h.md#a561265772438ab8995251760c7f3dc30)#define STM32\_PERIPH\_BUS\_MAX STM32\_CLOCK\_BUS\_APB3

23

25/\* RM0386, 0390, 0402, 0430 § Dedicated Clock configuration register (RCC\_DCKCFGRx) \*/

26

28/\* defined in stm32\_common\_clocks.h \*/

29

31/\* Low speed clocks defined in stm32\_common\_clocks.h \*/

[ 32](stm32f7__clock_8h.md#a7bc1dd03186b763b407a044ddffb4ab2)#define STM32\_SRC\_HSI (STM32\_SRC\_LSI + 1)

[ 34](stm32f7__clock_8h.md#a473d0d57680b535a9e9298600a1e1aab)#define STM32\_SRC\_PLL\_P (STM32\_SRC\_HSI + 1)

[ 35](stm32f7__clock_8h.md#ab3a03011d2d433feaff934c3828e1f27)#define STM32\_SRC\_PLL\_Q (STM32\_SRC\_PLL\_P + 1)

[ 36](stm32f7__clock_8h.md#aca252b1d875fbd9dce6350f1845e5439)#define STM32\_SRC\_PLL\_R (STM32\_SRC\_PLL\_Q + 1)

[ 38](stm32f7__clock_8h.md#a6cd4e305697f314401e5654b4dd5f25d)#define STM32\_SRC\_PCLK (STM32\_SRC\_PLL\_R + 1)

39

40

[ 41](stm32f7__clock_8h.md#a33d66849c63db64784317260b06ceb24)#define STM32\_CLOCK\_REG\_MASK 0xFFU

[ 42](stm32f7__clock_8h.md#a2e73bdb1691751ffd616a5c4e2762423)#define STM32\_CLOCK\_REG\_SHIFT 0U

[ 43](stm32f7__clock_8h.md#af3001a7541ea4df9e4948fd559352f60)#define STM32\_CLOCK\_SHIFT\_MASK 0x1FU

[ 44](stm32f7__clock_8h.md#a147846b77bd51e42c85bea5aca50ad4f)#define STM32\_CLOCK\_SHIFT\_SHIFT 8U

[ 45](stm32f7__clock_8h.md#a63ecbd205c0dd6cb3eab7bcbfdce38b9)#define STM32\_CLOCK\_MASK\_MASK 0x7U

[ 46](stm32f7__clock_8h.md#abfdb31d824fc5c6cf809a1dcff022b5d)#define STM32\_CLOCK\_MASK\_SHIFT 13U

[ 47](stm32f7__clock_8h.md#a6b4f80c7dbd047ca1ebac0b233ad1d1b)#define STM32\_CLOCK\_VAL\_MASK 0x7U

[ 48](stm32f7__clock_8h.md#adf2ca8c7f707b82b7ec4820dfc32929a)#define STM32\_CLOCK\_VAL\_SHIFT 16U

49

[ 63](stm32f7__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)#define STM32\_CLOCK(val, mask, shift, reg) \

64 ((((reg) & STM32\_CLOCK\_REG\_MASK) << STM32\_CLOCK\_REG\_SHIFT) | \

65 (((shift) & STM32\_CLOCK\_SHIFT\_MASK) << STM32\_CLOCK\_SHIFT\_SHIFT) | \

66 (((mask) & STM32\_CLOCK\_MASK\_MASK) << STM32\_CLOCK\_MASK\_SHIFT) | \

67 (((val) & STM32\_CLOCK\_VAL\_MASK) << STM32\_CLOCK\_VAL\_SHIFT))

68

[ 70](stm32f7__clock_8h.md#afb2336a33a23f9671b26010594232ba3)#define CFGR\_REG 0x08

71

[ 73](stm32f7__clock_8h.md#a70a10f70b4f5058508e8983ad0a4de3a)#define BDCR\_REG 0x70

74

[ 77](stm32f7__clock_8h.md#a2d34d604e16d874235b74bdbc8103bed)#define I2S\_SEL(val) STM32\_CLOCK(val, 1, 23, CFGR\_REG)

[ 79](stm32f7__clock_8h.md#a4836377699efa295c56d340e150695b0)#define RTC\_SEL(val) STM32\_CLOCK(val, 3, 8, BDCR\_REG)

80

[ 82](stm32f7__clock_8h.md#a459ad2c7f14d65f7389f6397d8808c0a)#define DCKCFGR1\_REG 0x8C

[ 83](stm32f7__clock_8h.md#a3a648b98a1f91abbce18297038ba3e5f)#define DCKCFGR2\_REG 0x90

84

[ 87](stm32f7__clock_8h.md#a17f3ec5f86995a2c4087f2988a9486c5)#define USART1\_SEL(val) STM32\_CLOCK(val, 3, 0, DCKCFGR2\_REG)

[ 88](stm32f7__clock_8h.md#ad67d92dfc439018a7a231e661d10d7f9)#define USART2\_SEL(val) STM32\_CLOCK(val, 3, 2, DCKCFGR2\_REG)

[ 89](stm32f7__clock_8h.md#ad2f356c0bc0e43d6f629cdb840846526)#define USART3\_SEL(val) STM32\_CLOCK(val, 3, 4, DCKCFGR2\_REG)

[ 90](stm32f7__clock_8h.md#aced9e983095cb40bc18f3a66e3818c98)#define USART4\_SEL(val) STM32\_CLOCK(val, 3, 6, DCKCFGR2\_REG)

[ 91](stm32f7__clock_8h.md#a6a45e0ef8bd196574e241aefdb3a5350)#define USART5\_SEL(val) STM32\_CLOCK(val, 3, 8, DCKCFGR2\_REG)

[ 92](stm32f7__clock_8h.md#a99c9026d61766ec9b91872ee64ad63eb)#define USART6\_SEL(val) STM32\_CLOCK(val, 3, 10, DCKCFGR2\_REG)

[ 93](stm32f7__clock_8h.md#a085ea149cac54d39aef4cb9f5c03402c)#define USART7\_SEL(val) STM32\_CLOCK(val, 3, 12, DCKCFGR2\_REG)

[ 94](stm32f7__clock_8h.md#adf99875c4c7a62e255871678fe848645)#define USART8\_SEL(val) STM32\_CLOCK(val, 3, 14, DCKCFGR2\_REG)

[ 95](stm32f7__clock_8h.md#a3fbef8f2542fc6921236bd2709acf64c)#define I2C1\_SEL(val) STM32\_CLOCK(val, 3, 16, DCKCFGR2\_REG)

[ 96](stm32f7__clock_8h.md#abdd79c9ce90458b53e81123d181fed98)#define I2C2\_SEL(val) STM32\_CLOCK(val, 3, 18, DCKCFGR2\_REG)

[ 97](stm32f7__clock_8h.md#aa12a1d2ac790880b7148d1e5660eb941)#define I2C3\_SEL(val) STM32\_CLOCK(val, 3, 20, DCKCFGR2\_REG)

[ 98](stm32f7__clock_8h.md#a55880006ae28021de4d148924c06001e)#define I2C4\_SEL(val) STM32\_CLOCK(val, 3, 22, DCKCFGR2\_REG)

[ 99](stm32f7__clock_8h.md#a042804bf8a52b3dd28033f8814442bfb)#define LPTIM1\_SEL(val) STM32\_CLOCK(val, 3, 24, DCKCFGR2\_REG)

[ 100](stm32f7__clock_8h.md#affd653e901474991857a29deba53cf82)#define CEC\_SEL(val) STM32\_CLOCK(val, 1, 26, DCKCFGR2\_REG)

[ 101](stm32f7__clock_8h.md#a9629b95b8e2c432e890c69727b52a4d4)#define CK48M\_SEL(val) STM32\_CLOCK(val, 1, 27, DCKCFGR2\_REG)

[ 102](stm32f7__clock_8h.md#a1a4999da331afff86581c8a6cea6afe9)#define SDMMC1\_SEL(val) STM32\_CLOCK(val, 1, 28, DCKCFGR2\_REG)

[ 103](stm32f7__clock_8h.md#a7319710d63129ad13039565cad2b4950)#define SDMMC2\_SEL(val) STM32\_CLOCK(val, 1, 29, DCKCFGR2\_REG)

[ 104](stm32f7__clock_8h.md#a2e82c24eb0c9e22635966752eebb2a05)#define DSI\_SEL(val) STM32\_CLOCK(val, 1, 30, DCKCFGR2\_REG)

105

106#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32F7\_CLOCK\_H\_ \*/

[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32f7\_clock.h](stm32f7__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
