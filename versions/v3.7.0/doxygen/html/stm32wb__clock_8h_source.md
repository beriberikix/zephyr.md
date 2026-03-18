---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/stm32wb__clock_8h_source.html
original_path: doxygen/html/stm32wb__clock_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32wb\_clock.h

[Go to the documentation of this file.](stm32wb__clock_8h.md)

1/\*

2 \* Copyright (c) 2022 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32WB\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32WB\_CLOCK\_H\_

8

9#include "[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)"

10

[ 12](stm32wb__clock_8h.md#a186de4b3566a20794e4483a9569abe3c)#define STM32\_CLOCK\_BUS\_AHB1 0x048

[ 13](stm32wb__clock_8h.md#a5e58ef1846c185b04bed598b26ee9205)#define STM32\_CLOCK\_BUS\_AHB2 0x04c

[ 14](stm32wb__clock_8h.md#ab2a3c819828eb0186ac3a3f15f4b4569)#define STM32\_CLOCK\_BUS\_AHB3 0x050

[ 15](stm32wb__clock_8h.md#ac763945fc36124f9c978c423826faa95)#define STM32\_CLOCK\_BUS\_APB1 0x058

[ 16](stm32wb__clock_8h.md#ad25510091b50e823c9860089a9f23deb)#define STM32\_CLOCK\_BUS\_APB1\_2 0x05c

[ 17](stm32wb__clock_8h.md#adb7becb609763568b91303041c9cd4db)#define STM32\_CLOCK\_BUS\_APB2 0x060

18

[ 19](stm32wb__clock_8h.md#acc0577552371fcda95685f6424ecb4b2)#define STM32\_PERIPH\_BUS\_MIN STM32\_CLOCK\_BUS\_AHB1

[ 20](stm32wb__clock_8h.md#a561265772438ab8995251760c7f3dc30)#define STM32\_PERIPH\_BUS\_MAX STM32\_CLOCK\_BUS\_APB2

21

23/\* RM0434, § Clock configuration register (RCC\_CCIPRx) \*/

24

26/\* defined in stm32\_common\_clocks.h \*/

28/\* Low speed clocks defined in stm32\_common\_clocks.h \*/

[ 29](stm32wb__clock_8h.md#a7bc1dd03186b763b407a044ddffb4ab2)#define STM32\_SRC\_HSI (STM32\_SRC\_LSI + 1)

[ 30](stm32wb__clock_8h.md#ae12e6bda1c30174c98303f692a42960f)#define STM32\_SRC\_HSI48 (STM32\_SRC\_HSI + 1)

[ 31](stm32wb__clock_8h.md#a542b4426a15d849545af2fd6012c520c)#define STM32\_SRC\_MSI (STM32\_SRC\_HSI48 + 1)

[ 32](stm32wb__clock_8h.md#aa7e82706a146d0f40dc7e9755b3be9a6)#define STM32\_SRC\_HSE (STM32\_SRC\_MSI + 1)

[ 34](stm32wb__clock_8h.md#a6cd4e305697f314401e5654b4dd5f25d)#define STM32\_SRC\_PCLK (STM32\_SRC\_HSE + 1)

[ 36](stm32wb__clock_8h.md#a473d0d57680b535a9e9298600a1e1aab)#define STM32\_SRC\_PLL\_P (STM32\_SRC\_PCLK + 1)

[ 37](stm32wb__clock_8h.md#ab3a03011d2d433feaff934c3828e1f27)#define STM32\_SRC\_PLL\_Q (STM32\_SRC\_PLL\_P + 1)

[ 38](stm32wb__clock_8h.md#aca252b1d875fbd9dce6350f1845e5439)#define STM32\_SRC\_PLL\_R (STM32\_SRC\_PLL\_Q + 1)

39/\* TODO: PLLSAI clocks \*/

40

[ 41](stm32wb__clock_8h.md#a33d66849c63db64784317260b06ceb24)#define STM32\_CLOCK\_REG\_MASK 0xFFU

[ 42](stm32wb__clock_8h.md#a2e73bdb1691751ffd616a5c4e2762423)#define STM32\_CLOCK\_REG\_SHIFT 0U

[ 43](stm32wb__clock_8h.md#af3001a7541ea4df9e4948fd559352f60)#define STM32\_CLOCK\_SHIFT\_MASK 0x1FU

[ 44](stm32wb__clock_8h.md#a147846b77bd51e42c85bea5aca50ad4f)#define STM32\_CLOCK\_SHIFT\_SHIFT 8U

[ 45](stm32wb__clock_8h.md#a63ecbd205c0dd6cb3eab7bcbfdce38b9)#define STM32\_CLOCK\_MASK\_MASK 0x7U

[ 46](stm32wb__clock_8h.md#abfdb31d824fc5c6cf809a1dcff022b5d)#define STM32\_CLOCK\_MASK\_SHIFT 13U

[ 47](stm32wb__clock_8h.md#a6b4f80c7dbd047ca1ebac0b233ad1d1b)#define STM32\_CLOCK\_VAL\_MASK 0x7U

[ 48](stm32wb__clock_8h.md#adf2ca8c7f707b82b7ec4820dfc32929a)#define STM32\_CLOCK\_VAL\_SHIFT 16U

49

[ 63](stm32wb__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)#define STM32\_CLOCK(val, mask, shift, reg) \

64 ((((reg) & STM32\_CLOCK\_REG\_MASK) << STM32\_CLOCK\_REG\_SHIFT) | \

65 (((shift) & STM32\_CLOCK\_SHIFT\_MASK) << STM32\_CLOCK\_SHIFT\_SHIFT) | \

66 (((mask) & STM32\_CLOCK\_MASK\_MASK) << STM32\_CLOCK\_MASK\_SHIFT) | \

67 (((val) & STM32\_CLOCK\_VAL\_MASK) << STM32\_CLOCK\_VAL\_SHIFT))

68

[ 70](stm32wb__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260)#define CCIPR\_REG 0x88

71

[ 73](stm32wb__clock_8h.md#a70a10f70b4f5058508e8983ad0a4de3a)#define BDCR\_REG 0x90

74

[ 76](stm32wb__clock_8h.md#a16c4f3ac8a8c6255620516b3a32b7a70)#define CSR\_REG 0x94

77

[ 80](stm32wb__clock_8h.md#a17f3ec5f86995a2c4087f2988a9486c5)#define USART1\_SEL(val) STM32\_CLOCK(val, 3, 0, CCIPR\_REG)

[ 81](stm32wb__clock_8h.md#aac31ca48bf87a722f6e0519f25f764dd)#define LPUART1\_SEL(val) STM32\_CLOCK(val, 3, 10, CCIPR\_REG)

[ 82](stm32wb__clock_8h.md#a3fbef8f2542fc6921236bd2709acf64c)#define I2C1\_SEL(val) STM32\_CLOCK(val, 3, 12, CCIPR\_REG)

[ 83](stm32wb__clock_8h.md#aa12a1d2ac790880b7148d1e5660eb941)#define I2C3\_SEL(val) STM32\_CLOCK(val, 3, 16, CCIPR\_REG)

[ 84](stm32wb__clock_8h.md#a042804bf8a52b3dd28033f8814442bfb)#define LPTIM1\_SEL(val) STM32\_CLOCK(val, 3, 18, CCIPR\_REG)

[ 85](stm32wb__clock_8h.md#aa713f6ff001bfa6352747e7a66e3f98a)#define LPTIM2\_SEL(val) STM32\_CLOCK(val, 3, 20, CCIPR\_REG)

[ 86](stm32wb__clock_8h.md#ab8e49f6309adb53edd9ad3d051d451db)#define SAI1\_SEL(val) STM32\_CLOCK(val, 3, 22, CCIPR\_REG)

[ 87](stm32wb__clock_8h.md#a3f3b40e4fdebc11d7a2dd4a86e1fefc8)#define CLK48\_SEL(val) STM32\_CLOCK(val, 3, 26, CCIPR\_REG)

[ 88](stm32wb__clock_8h.md#a635d17ad991ded52d41a6e7b0bec5773)#define ADC\_SEL(val) STM32\_CLOCK(val, 3, 28, CCIPR\_REG)

[ 89](stm32wb__clock_8h.md#abfff4355a498febbcf4ebcb237930a57)#define RNG\_SEL(val) STM32\_CLOCK(val, 3, 30, CCIPR\_REG)

[ 91](stm32wb__clock_8h.md#a4836377699efa295c56d340e150695b0)#define RTC\_SEL(val) STM32\_CLOCK(val, 3, 8, BDCR\_REG)

[ 93](stm32wb__clock_8h.md#a1812acd6f7e09cbe8f6f6c4fc7fe6f13)#define RFWKP\_SEL(val) STM32\_CLOCK(val, 3, 14, CSR\_REG)

94

95#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32WB\_CLOCK\_H\_ \*/

[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32wb\_clock.h](stm32wb__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
