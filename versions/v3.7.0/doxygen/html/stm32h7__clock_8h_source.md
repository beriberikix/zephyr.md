---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/stm32h7__clock_8h_source.html
original_path: doxygen/html/stm32h7__clock_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32h7\_clock.h

[Go to the documentation of this file.](stm32h7__clock_8h.md)

1/\*

2 \* Copyright (c) 2022 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32H7\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32H7\_CLOCK\_H\_

8

9#include "[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)"

10

12

13/\* RM0468, Table 56 Kernel clock dictribution summary \*/

14

16/\* defined in stm32\_common\_clocks.h \*/

17

19/\* Low speed clocks defined in stm32\_common\_clocks.h \*/

[ 20](stm32h7__clock_8h.md#aa7e82706a146d0f40dc7e9755b3be9a6)#define STM32\_SRC\_HSE (STM32\_SRC\_LSI + 1)

[ 21](stm32h7__clock_8h.md#ae12e6bda1c30174c98303f692a42960f)#define STM32\_SRC\_HSI48 (STM32\_SRC\_HSE + 1)

[ 22](stm32h7__clock_8h.md#ab574ca48f488778e54bdabcd78588ed4)#define STM32\_SRC\_HSI\_KER (STM32\_SRC\_HSI48 + 1) /\* HSI + HSIKERON \*/

[ 23](stm32h7__clock_8h.md#a469a687b3d587b881bd607634251faf4)#define STM32\_SRC\_CSI\_KER (STM32\_SRC\_HSI\_KER + 1) /\* CSI + CSIKERON \*/

[ 25](stm32h7__clock_8h.md#aa074615a92c5ff479f4fbed6fdf27f62)#define STM32\_SRC\_PLL1\_P (STM32\_SRC\_CSI\_KER + 1)

[ 26](stm32h7__clock_8h.md#a6edb3dc598055ceeb82045fdee647637)#define STM32\_SRC\_PLL1\_Q (STM32\_SRC\_PLL1\_P + 1)

[ 27](stm32h7__clock_8h.md#a6063632b32a970b9abbf711bab8a77c9)#define STM32\_SRC\_PLL1\_R (STM32\_SRC\_PLL1\_Q + 1)

[ 28](stm32h7__clock_8h.md#ae568673a4eca1b42afc59faabb5810ac)#define STM32\_SRC\_PLL2\_P (STM32\_SRC\_PLL1\_R + 1)

[ 29](stm32h7__clock_8h.md#aaf0a956dda42c2a031cabce49dd3e717)#define STM32\_SRC\_PLL2\_Q (STM32\_SRC\_PLL2\_P + 1)

[ 30](stm32h7__clock_8h.md#a57af8944eefa865aa75b6286c13a53cd)#define STM32\_SRC\_PLL2\_R (STM32\_SRC\_PLL2\_Q + 1)

[ 31](stm32h7__clock_8h.md#a17c753e0bb8547ea9452f48a65a0a206)#define STM32\_SRC\_PLL3\_P (STM32\_SRC\_PLL2\_R + 1)

[ 32](stm32h7__clock_8h.md#a9a31a3adebff6a1eee31c287673412c9)#define STM32\_SRC\_PLL3\_Q (STM32\_SRC\_PLL3\_P + 1)

[ 33](stm32h7__clock_8h.md#a604c22ff137a35cd1725b70991696f9a)#define STM32\_SRC\_PLL3\_R (STM32\_SRC\_PLL3\_Q + 1)

[ 35](stm32h7__clock_8h.md#a8b7025d7f4be00a152c53097a414668e)#define STM32\_SRC\_CKPER (STM32\_SRC\_PLL3\_R + 1)

37/\* #define STM32\_SRC\_I2SCKIN TBD \*/

38/\* #define STM32\_SRC\_SPDIFRX TBD \*/

39

40

[ 42](stm32h7__clock_8h.md#ab2a3c819828eb0186ac3a3f15f4b4569)#define STM32\_CLOCK\_BUS\_AHB3 0x0D4

[ 43](stm32h7__clock_8h.md#a186de4b3566a20794e4483a9569abe3c)#define STM32\_CLOCK\_BUS\_AHB1 0x0D8

[ 44](stm32h7__clock_8h.md#a5e58ef1846c185b04bed598b26ee9205)#define STM32\_CLOCK\_BUS\_AHB2 0x0DC

[ 45](stm32h7__clock_8h.md#a49bccabc3065f192086f16929a7b762d)#define STM32\_CLOCK\_BUS\_AHB4 0x0E0

[ 46](stm32h7__clock_8h.md#af7165e22b71d1beaf0dd4f59d5b4db6d)#define STM32\_CLOCK\_BUS\_APB3 0x0E4

[ 47](stm32h7__clock_8h.md#ac763945fc36124f9c978c423826faa95)#define STM32\_CLOCK\_BUS\_APB1 0x0E8

[ 48](stm32h7__clock_8h.md#ad25510091b50e823c9860089a9f23deb)#define STM32\_CLOCK\_BUS\_APB1\_2 0x0EC

[ 49](stm32h7__clock_8h.md#adb7becb609763568b91303041c9cd4db)#define STM32\_CLOCK\_BUS\_APB2 0x0F0

[ 50](stm32h7__clock_8h.md#a537105e6125ce3b95a2d69435f47dd51)#define STM32\_CLOCK\_BUS\_APB4 0x0F4 /\* TBD: To remove ? \*/

[ 52](stm32h7__clock_8h.md#a72ffaa9863e167f47e06e91151b47831)#define STM32\_SRC\_PCLK1 STM32\_CLOCK\_BUS\_APB1

[ 53](stm32h7__clock_8h.md#a68f7335900538f3beb2c2d09e33376b3)#define STM32\_SRC\_PCLK2 STM32\_CLOCK\_BUS\_APB2

[ 54](stm32h7__clock_8h.md#af15978643f6f5a5f9fa427cb59fa17c7)#define STM32\_SRC\_HCLK3 STM32\_CLOCK\_BUS\_AHB3

[ 55](stm32h7__clock_8h.md#ae54654dc761dca391f56e95ebd6db625)#define STM32\_SRC\_PCLK3 STM32\_CLOCK\_BUS\_APB3

[ 56](stm32h7__clock_8h.md#a4c6b45a1c2d1e1eeccdd946eb52ef85e)#define STM32\_SRC\_PCLK4 STM32\_CLOCK\_BUS\_APB4

57

[ 58](stm32h7__clock_8h.md#acc0577552371fcda95685f6424ecb4b2)#define STM32\_PERIPH\_BUS\_MIN STM32\_CLOCK\_BUS\_AHB3

[ 59](stm32h7__clock_8h.md#a561265772438ab8995251760c7f3dc30)#define STM32\_PERIPH\_BUS\_MAX STM32\_CLOCK\_BUS\_APB4

60

[ 61](stm32h7__clock_8h.md#a33d66849c63db64784317260b06ceb24)#define STM32\_CLOCK\_REG\_MASK 0xFFU

[ 62](stm32h7__clock_8h.md#a2e73bdb1691751ffd616a5c4e2762423)#define STM32\_CLOCK\_REG\_SHIFT 0U

[ 63](stm32h7__clock_8h.md#af3001a7541ea4df9e4948fd559352f60)#define STM32\_CLOCK\_SHIFT\_MASK 0x1FU

[ 64](stm32h7__clock_8h.md#a147846b77bd51e42c85bea5aca50ad4f)#define STM32\_CLOCK\_SHIFT\_SHIFT 8U

[ 65](stm32h7__clock_8h.md#a63ecbd205c0dd6cb3eab7bcbfdce38b9)#define STM32\_CLOCK\_MASK\_MASK 0x7U

[ 66](stm32h7__clock_8h.md#abfdb31d824fc5c6cf809a1dcff022b5d)#define STM32\_CLOCK\_MASK\_SHIFT 13U

[ 67](stm32h7__clock_8h.md#a6b4f80c7dbd047ca1ebac0b233ad1d1b)#define STM32\_CLOCK\_VAL\_MASK 0x7U

[ 68](stm32h7__clock_8h.md#adf2ca8c7f707b82b7ec4820dfc32929a)#define STM32\_CLOCK\_VAL\_SHIFT 16U

69

[ 83](stm32h7__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)#define STM32\_CLOCK(val, mask, shift, reg) \

84 ((((reg) & STM32\_CLOCK\_REG\_MASK) << STM32\_CLOCK\_REG\_SHIFT) | \

85 (((shift) & STM32\_CLOCK\_SHIFT\_MASK) << STM32\_CLOCK\_SHIFT\_SHIFT) | \

86 (((mask) & STM32\_CLOCK\_MASK\_MASK) << STM32\_CLOCK\_MASK\_SHIFT) | \

87 (((val) & STM32\_CLOCK\_VAL\_MASK) << STM32\_CLOCK\_VAL\_SHIFT))

88

[ 90](stm32h7__clock_8h.md#a9a43f736d68c30870b3f1ee545b2cff9)#define D1CCIPR\_REG 0x4C

[ 91](stm32h7__clock_8h.md#ab1fb4611db93643e87a5435ebf0eecef)#define D2CCIP1R\_REG 0x50

[ 92](stm32h7__clock_8h.md#a44f6b0e94c505441a7ff7f14d26a5f51)#define D2CCIP2R\_REG 0x54

[ 93](stm32h7__clock_8h.md#aeda9dd86b920e734a85ce06acbd75eda)#define D3CCIPR\_REG 0x58

94

[ 96](stm32h7__clock_8h.md#a70a10f70b4f5058508e8983ad0a4de3a)#define BDCR\_REG 0x70

97

[ 100](stm32h7__clock_8h.md#a0de89c03e0cd384de7f594aa5c5e82de)#define FMC\_SEL(val) STM32\_CLOCK(val, 3, 0, D1CCIPR\_REG)

[ 101](stm32h7__clock_8h.md#ae66e7abfb9009e737cff676fb4e5155f)#define QSPI\_SEL(val) STM32\_CLOCK(val, 3, 4, D1CCIPR\_REG)

[ 102](stm32h7__clock_8h.md#a2e82c24eb0c9e22635966752eebb2a05)#define DSI\_SEL(val) STM32\_CLOCK(val, 1, 8, D1CCIPR\_REG)

[ 103](stm32h7__clock_8h.md#a42688c1d17e09ab58029feedd7491c0b)#define SDMMC\_SEL(val) STM32\_CLOCK(val, 1, 16, D1CCIPR\_REG)

[ 104](stm32h7__clock_8h.md#adc32e4d489d72766d6df1783eedf7628)#define CKPER\_SEL(val) STM32\_CLOCK(val, 3, 28, D1CCIPR\_REG)

105/\* Device domain clocks selection helpers (RM0468.pdf) \*/

[ 106](stm32h7__clock_8h.md#a098cb5d65a4a2b4cd7da394289eb38ff)#define OSPI\_SEL(val) STM32\_CLOCK(val, 3, 4, D1CCIPR\_REG)

[ 108](stm32h7__clock_8h.md#ab8e49f6309adb53edd9ad3d051d451db)#define SAI1\_SEL(val) STM32\_CLOCK(val, 7, 0, D2CCIP1R\_REG)

[ 109](stm32h7__clock_8h.md#a8a4600ad412c94bae8c79918ec2bd867)#define SAI23\_SEL(val) STM32\_CLOCK(val, 7, 6, D2CCIP1R\_REG)

[ 110](stm32h7__clock_8h.md#a3852b519c300afd2fd1757c717076b0f)#define SPI123\_SEL(val) STM32\_CLOCK(val, 7, 12, D2CCIP1R\_REG)

[ 111](stm32h7__clock_8h.md#a6919b0ea063667adb88c7c2d79877426)#define SPI45\_SEL(val) STM32\_CLOCK(val, 7, 16, D2CCIP1R\_REG)

[ 112](stm32h7__clock_8h.md#a37e4a34b034dee8d7f0b1fa1378e6ff6)#define SPDIF\_SEL(val) STM32\_CLOCK(val, 3, 20, D2CCIP1R\_REG)

[ 113](stm32h7__clock_8h.md#a5364dd3606acfca9d1c00e60255a6634)#define DFSDM1\_SEL(val) STM32\_CLOCK(val, 1, 24, D2CCIP1R\_REG)

[ 114](stm32h7__clock_8h.md#ac1df6369669b4b3febd0525426e76499)#define FDCAN\_SEL(val) STM32\_CLOCK(val, 3, 28, D2CCIP1R\_REG)

[ 115](stm32h7__clock_8h.md#a5ab7d8af86893729938fec97b28ef605)#define SWP\_SEL(val) STM32\_CLOCK(val, 1, 31, D2CCIP1R\_REG)

[ 117](stm32h7__clock_8h.md#a80d004ccf51b0621ce404db882bf8b72)#define USART2345678\_SEL(val) STM32\_CLOCK(val, 7, 0, D2CCIP2R\_REG)

[ 118](stm32h7__clock_8h.md#ae5f861161482b8888ff3aa5ea79b49a3)#define USART16\_SEL(val) STM32\_CLOCK(val, 7, 3, D2CCIP2R\_REG)

[ 119](stm32h7__clock_8h.md#abfff4355a498febbcf4ebcb237930a57)#define RNG\_SEL(val) STM32\_CLOCK(val, 3, 8, D2CCIP2R\_REG)

[ 120](stm32h7__clock_8h.md#a6ee55f4ccc3fa2c0a3a5387ba0fd587e)#define I2C123\_SEL(val) STM32\_CLOCK(val, 3, 12, D2CCIP2R\_REG)

[ 121](stm32h7__clock_8h.md#a3247ad782f1e2c7db84989d03831139b)#define USB\_SEL(val) STM32\_CLOCK(val, 3, 20, D2CCIP2R\_REG)

[ 122](stm32h7__clock_8h.md#affd653e901474991857a29deba53cf82)#define CEC\_SEL(val) STM32\_CLOCK(val, 3, 22, D2CCIP2R\_REG)

[ 123](stm32h7__clock_8h.md#a042804bf8a52b3dd28033f8814442bfb)#define LPTIM1\_SEL(val) STM32\_CLOCK(val, 7, 28, D2CCIP2R\_REG)

[ 125](stm32h7__clock_8h.md#aac31ca48bf87a722f6e0519f25f764dd)#define LPUART1\_SEL(val) STM32\_CLOCK(val, 7, 0, D3CCIPR\_REG)

[ 126](stm32h7__clock_8h.md#a55880006ae28021de4d148924c06001e)#define I2C4\_SEL(val) STM32\_CLOCK(val, 3, 8, D3CCIPR\_REG)

[ 127](stm32h7__clock_8h.md#aa713f6ff001bfa6352747e7a66e3f98a)#define LPTIM2\_SEL(val) STM32\_CLOCK(val, 7, 10, D3CCIPR\_REG)

[ 128](stm32h7__clock_8h.md#af321430d682d7447d63282a0f380bc8a)#define LPTIM345\_SEL(val) STM32\_CLOCK(val, 7, 13, D3CCIPR\_REG)

[ 129](stm32h7__clock_8h.md#a635d17ad991ded52d41a6e7b0bec5773)#define ADC\_SEL(val) STM32\_CLOCK(val, 3, 16, D3CCIPR\_REG)

[ 130](stm32h7__clock_8h.md#ae118097634082d8365c0418902ca23c7)#define SAI4A\_SEL(val) STM32\_CLOCK(val, 7, 21, D3CCIPR\_REG)

[ 131](stm32h7__clock_8h.md#ad2946a4efd35a3a9cd22b00a24675236)#define SAI4B\_SEL(val) STM32\_CLOCK(val, 7, 24, D3CCIPR\_REG)

[ 132](stm32h7__clock_8h.md#ab43d49ec71267eb1d8002909cc3360bf)#define SPI6\_SEL(val) STM32\_CLOCK(val, 7, 28, D3CCIPR\_REG)

[ 134](stm32h7__clock_8h.md#a4836377699efa295c56d340e150695b0)#define RTC\_SEL(val) STM32\_CLOCK(val, 3, 8, BDCR\_REG)

135

136#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32H7\_CLOCK\_H\_ \*/

[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32h7\_clock.h](stm32h7__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
