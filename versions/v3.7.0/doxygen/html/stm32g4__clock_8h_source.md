---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/stm32g4__clock_8h_source.html
original_path: doxygen/html/stm32g4__clock_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32g4\_clock.h

[Go to the documentation of this file.](stm32g4__clock_8h.md)

1/\*

2 \* Copyright (c) 2022 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32G4\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32G4\_CLOCK\_H\_

8

9#include "[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)"

10

[ 12](stm32g4__clock_8h.md#a186de4b3566a20794e4483a9569abe3c)#define STM32\_CLOCK\_BUS\_AHB1 0x048

[ 13](stm32g4__clock_8h.md#a5e58ef1846c185b04bed598b26ee9205)#define STM32\_CLOCK\_BUS\_AHB2 0x04c

[ 14](stm32g4__clock_8h.md#ab2a3c819828eb0186ac3a3f15f4b4569)#define STM32\_CLOCK\_BUS\_AHB3 0x050

[ 15](stm32g4__clock_8h.md#ac763945fc36124f9c978c423826faa95)#define STM32\_CLOCK\_BUS\_APB1 0x058

[ 16](stm32g4__clock_8h.md#ad25510091b50e823c9860089a9f23deb)#define STM32\_CLOCK\_BUS\_APB1\_2 0x05c

[ 17](stm32g4__clock_8h.md#adb7becb609763568b91303041c9cd4db)#define STM32\_CLOCK\_BUS\_APB2 0x060

18

[ 19](stm32g4__clock_8h.md#acc0577552371fcda95685f6424ecb4b2)#define STM32\_PERIPH\_BUS\_MIN STM32\_CLOCK\_BUS\_AHB1

[ 20](stm32g4__clock_8h.md#a561265772438ab8995251760c7f3dc30)#define STM32\_PERIPH\_BUS\_MAX STM32\_CLOCK\_BUS\_APB2

21

23/\* RM0440, § Clock configuration register (RCC\_CCIPRx) \*/

24

26/\* defined in stm32\_common\_clocks.h \*/

27

29/\* Low speed clocks defined in stm32\_common\_clocks.h \*/

[ 30](stm32g4__clock_8h.md#a7bc1dd03186b763b407a044ddffb4ab2)#define STM32\_SRC\_HSI (STM32\_SRC\_LSI + 1)

[ 31](stm32g4__clock_8h.md#ae12e6bda1c30174c98303f692a42960f)#define STM32\_SRC\_HSI48 (STM32\_SRC\_HSI + 1)

[ 32](stm32g4__clock_8h.md#aa7e82706a146d0f40dc7e9755b3be9a6)#define STM32\_SRC\_HSE (STM32\_SRC\_HSI48 + 1)

[ 33](stm32g4__clock_8h.md#a542b4426a15d849545af2fd6012c520c)#define STM32\_SRC\_MSI (STM32\_SRC\_HSE + 1)

[ 35](stm32g4__clock_8h.md#a6cd4e305697f314401e5654b4dd5f25d)#define STM32\_SRC\_PCLK (STM32\_SRC\_MSI + 1)

[ 37](stm32g4__clock_8h.md#a473d0d57680b535a9e9298600a1e1aab)#define STM32\_SRC\_PLL\_P (STM32\_SRC\_PCLK + 1)

[ 38](stm32g4__clock_8h.md#ab3a03011d2d433feaff934c3828e1f27)#define STM32\_SRC\_PLL\_Q (STM32\_SRC\_PLL\_P + 1)

[ 39](stm32g4__clock_8h.md#aca252b1d875fbd9dce6350f1845e5439)#define STM32\_SRC\_PLL\_R (STM32\_SRC\_PLL\_Q + 1)

40/\* TODO: PLLSAI clocks \*/

41

[ 42](stm32g4__clock_8h.md#a33d66849c63db64784317260b06ceb24)#define STM32\_CLOCK\_REG\_MASK 0xFFU

[ 43](stm32g4__clock_8h.md#a2e73bdb1691751ffd616a5c4e2762423)#define STM32\_CLOCK\_REG\_SHIFT 0U

[ 44](stm32g4__clock_8h.md#af3001a7541ea4df9e4948fd559352f60)#define STM32\_CLOCK\_SHIFT\_MASK 0x1FU

[ 45](stm32g4__clock_8h.md#a147846b77bd51e42c85bea5aca50ad4f)#define STM32\_CLOCK\_SHIFT\_SHIFT 8U

[ 46](stm32g4__clock_8h.md#a63ecbd205c0dd6cb3eab7bcbfdce38b9)#define STM32\_CLOCK\_MASK\_MASK 0x7U

[ 47](stm32g4__clock_8h.md#abfdb31d824fc5c6cf809a1dcff022b5d)#define STM32\_CLOCK\_MASK\_SHIFT 13U

[ 48](stm32g4__clock_8h.md#a6b4f80c7dbd047ca1ebac0b233ad1d1b)#define STM32\_CLOCK\_VAL\_MASK 0x7U

[ 49](stm32g4__clock_8h.md#adf2ca8c7f707b82b7ec4820dfc32929a)#define STM32\_CLOCK\_VAL\_SHIFT 16U

50

[ 64](stm32g4__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)#define STM32\_CLOCK(val, mask, shift, reg) \

65 ((((reg) & STM32\_CLOCK\_REG\_MASK) << STM32\_CLOCK\_REG\_SHIFT) | \

66 (((shift) & STM32\_CLOCK\_SHIFT\_MASK) << STM32\_CLOCK\_SHIFT\_SHIFT) | \

67 (((mask) & STM32\_CLOCK\_MASK\_MASK) << STM32\_CLOCK\_MASK\_SHIFT) | \

68 (((val) & STM32\_CLOCK\_VAL\_MASK) << STM32\_CLOCK\_VAL\_SHIFT))

69

[ 71](stm32g4__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260)#define CCIPR\_REG 0x88

[ 72](stm32g4__clock_8h.md#a60349691a29a48b727f302acb8025b89)#define CCIPR2\_REG 0x9C

73

[ 75](stm32g4__clock_8h.md#a70a10f70b4f5058508e8983ad0a4de3a)#define BDCR\_REG 0x90

76

[ 79](stm32g4__clock_8h.md#a17f3ec5f86995a2c4087f2988a9486c5)#define USART1\_SEL(val) STM32\_CLOCK(val, 3, 0, CCIPR\_REG)

[ 80](stm32g4__clock_8h.md#ad67d92dfc439018a7a231e661d10d7f9)#define USART2\_SEL(val) STM32\_CLOCK(val, 3, 2, CCIPR\_REG)

[ 81](stm32g4__clock_8h.md#ad2f356c0bc0e43d6f629cdb840846526)#define USART3\_SEL(val) STM32\_CLOCK(val, 3, 4, CCIPR\_REG)

[ 82](stm32g4__clock_8h.md#aced9e983095cb40bc18f3a66e3818c98)#define USART4\_SEL(val) STM32\_CLOCK(val, 3, 6, CCIPR\_REG)

[ 83](stm32g4__clock_8h.md#a6a45e0ef8bd196574e241aefdb3a5350)#define USART5\_SEL(val) STM32\_CLOCK(val, 3, 8, CCIPR\_REG)

[ 84](stm32g4__clock_8h.md#aac31ca48bf87a722f6e0519f25f764dd)#define LPUART1\_SEL(val) STM32\_CLOCK(val, 3, 10, CCIPR\_REG)

[ 85](stm32g4__clock_8h.md#a3fbef8f2542fc6921236bd2709acf64c)#define I2C1\_SEL(val) STM32\_CLOCK(val, 3, 12, CCIPR\_REG)

[ 86](stm32g4__clock_8h.md#abdd79c9ce90458b53e81123d181fed98)#define I2C2\_SEL(val) STM32\_CLOCK(val, 3, 14, CCIPR\_REG)

[ 87](stm32g4__clock_8h.md#aa12a1d2ac790880b7148d1e5660eb941)#define I2C3\_SEL(val) STM32\_CLOCK(val, 3, 16, CCIPR\_REG)

[ 88](stm32g4__clock_8h.md#a042804bf8a52b3dd28033f8814442bfb)#define LPTIM1\_SEL(val) STM32\_CLOCK(val, 3, 18, CCIPR\_REG)

[ 89](stm32g4__clock_8h.md#ab8e49f6309adb53edd9ad3d051d451db)#define SAI1\_SEL(val) STM32\_CLOCK(val, 3, 20, CCIPR\_REG)

[ 90](stm32g4__clock_8h.md#a082b9f1996ab134c3884ad5a4360b6e5)#define I2S23\_SEL(val) STM32\_CLOCK(val, 3, 22, CCIPR\_REG)

[ 91](stm32g4__clock_8h.md#ac1df6369669b4b3febd0525426e76499)#define FDCAN\_SEL(val) STM32\_CLOCK(val, 3, 24, CCIPR\_REG)

[ 92](stm32g4__clock_8h.md#a3f3b40e4fdebc11d7a2dd4a86e1fefc8)#define CLK48\_SEL(val) STM32\_CLOCK(val, 3, 26, CCIPR\_REG)

[ 93](stm32g4__clock_8h.md#a937fbb74cf970ef8033c16c68b27400f)#define ADC12\_SEL(val) STM32\_CLOCK(val, 3, 28, CCIPR\_REG)

[ 94](stm32g4__clock_8h.md#a783a036bee08f7f5ef9c556816d7441f)#define ADC34\_SEL(val) STM32\_CLOCK(val, 3, 30, CCIPR\_REG)

[ 96](stm32g4__clock_8h.md#a55880006ae28021de4d148924c06001e)#define I2C4\_SEL(val) STM32\_CLOCK(val, 3, 0, CCIPR2\_REG)

[ 97](stm32g4__clock_8h.md#ae66e7abfb9009e737cff676fb4e5155f)#define QSPI\_SEL(val) STM32\_CLOCK(val, 3, 20, CCIPR2\_REG)

[ 99](stm32g4__clock_8h.md#a4836377699efa295c56d340e150695b0)#define RTC\_SEL(val) STM32\_CLOCK(val, 3, 8, BDCR\_REG)

100

101#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32G4\_CLOCK\_H\_ \*/

[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32g4\_clock.h](stm32g4__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
