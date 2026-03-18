---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/imx__ccm__rev2_8h_source.html
original_path: doxygen/html/imx__ccm__rev2_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

imx\_ccm\_rev2.h

[Go to the documentation of this file.](imx__ccm__rev2_8h.md)

1/\*

2 \* Copyright (c) 2021, NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_IMX\_CCM\_REV2\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_IMX\_CCM\_REV2\_H\_

9

10/\* Peripheral:

11 \* range: 0 - 0xFF, starting from 0

12 \*

13 \* Instance:

14 \* range: 0 - 0xFF, starting from 0

15 \*/

[ 16](imx__ccm__rev2_8h.md#aa31bf3cf51ff3af717f0d4037eeaa1c9)#define IMX\_CCM\_PERIPHERAL\_MASK 0xFF00UL

[ 17](imx__ccm__rev2_8h.md#a30f30d268fb9aae738f27161e6028f73)#define IMX\_CCM\_INSTANCE\_MASK 0xFFUL

18

[ 19](imx__ccm__rev2_8h.md#ab1e95e431d7486c814c969d0d9c57559)#define IMX\_CCM\_CORESYS\_CLK 0

[ 20](imx__ccm__rev2_8h.md#afcda3a44b4029872bfa5d219f10dd506)#define IMX\_CCM\_PLATFORM\_CLK 0x1UL

[ 21](imx__ccm__rev2_8h.md#a0f9e44ec176274d3792bb2dd3e21a28b)#define IMX\_CCM\_BUS\_CLK 0x2UL

22/\* LPUART \*/

[ 23](imx__ccm__rev2_8h.md#a01fa41a7ad66c54b1c19455b6160bbc2)#define IMX\_CCM\_LPUART\_CLK 0x300UL

[ 24](imx__ccm__rev2_8h.md#a96e62b5b478ee548a1e52b7189a73817)#define IMX\_CCM\_LPUART1\_CLK 0x300UL

[ 25](imx__ccm__rev2_8h.md#a46255999d02ae6161981374872e065cf)#define IMX\_CCM\_LPUART2\_CLK 0x301UL

[ 26](imx__ccm__rev2_8h.md#a6676eb59f3d665c2a9bba7aae24228ca)#define IMX\_CCM\_LPUART3\_CLK 0x302UL

[ 27](imx__ccm__rev2_8h.md#a9647111e5a5af6e8e67e059009490974)#define IMX\_CCM\_LPUART4\_CLK 0x303UL

[ 28](imx__ccm__rev2_8h.md#acd84397a25a81c7f315c7740049d570a)#define IMX\_CCM\_LPUART5\_CLK 0x304UL

[ 29](imx__ccm__rev2_8h.md#a3c6916f6ff4fae75dc51177e25d51642)#define IMX\_CCM\_LPUART6\_CLK 0x305UL

[ 30](imx__ccm__rev2_8h.md#a4f2f07925d50b73cdc218d1f99cedf98)#define IMX\_CCM\_LPUART7\_CLK 0x306UL

[ 31](imx__ccm__rev2_8h.md#a8db4fa3e674535ba490d89a52979cad0)#define IMX\_CCM\_LPUART8\_CLK 0x307UL

[ 32](imx__ccm__rev2_8h.md#a0a6f1a1a8141d825058fd5a2c2ca3914)#define IMX\_CCM\_LPUART9\_CLK 0x308UL

[ 33](imx__ccm__rev2_8h.md#a24307153d0dbf07b908ab1876ae1a4bc)#define IMX\_CCM\_LPUART10\_CLK 0x309UL

[ 34](imx__ccm__rev2_8h.md#af539f30a7a6cd9ee4aba7f2415b5b3e6)#define IMX\_CCM\_LPUART11\_CLK 0x30aUL

[ 35](imx__ccm__rev2_8h.md#a68c212e56058fd3f59c8bb7bd7f25984)#define IMX\_CCM\_LPUART12\_CLK 0x30bUL

36

37/\* LPI2C \*/

[ 38](imx__ccm__rev2_8h.md#ac970114caf03b14bf6d3f2ff04f548dc)#define IMX\_CCM\_LPI2C\_CLK 0x400UL

[ 39](imx__ccm__rev2_8h.md#a0868c0eeb69b0e67d6e2d022a9e55035)#define IMX\_CCM\_LPI2C1\_CLK 0x400UL

[ 40](imx__ccm__rev2_8h.md#a1a684ee49ada9866d61df70c8757bbf6)#define IMX\_CCM\_LPI2C2\_CLK 0x401UL

[ 41](imx__ccm__rev2_8h.md#a5d809939798eacedbbf59f38a57fb5ba)#define IMX\_CCM\_LPI2C3\_CLK 0x402UL

[ 42](imx__ccm__rev2_8h.md#aac755270370e533fb3f78e471f0efac7)#define IMX\_CCM\_LPI2C4\_CLK 0x403UL

[ 43](imx__ccm__rev2_8h.md#a4a73ff0aa1615dfc1171689dbb76636b)#define IMX\_CCM\_LPI2C5\_CLK 0x404UL

[ 44](imx__ccm__rev2_8h.md#a61d52e2b71b0eef06d76c8261df4ac1b)#define IMX\_CCM\_LPI2C6\_CLK 0x405UL

[ 45](imx__ccm__rev2_8h.md#a002cc9eac38583fca551917c1a1fa299)#define IMX\_CCM\_LPI2C7\_CLK 0x406UL

[ 46](imx__ccm__rev2_8h.md#ae7cecaf7c7b40bbc2654c3417ac729cc)#define IMX\_CCM\_LPI2C8\_CLK 0x407UL

47

48/\* LPSPI \*/

[ 49](imx__ccm__rev2_8h.md#a169487d4c020dee2492e36202fa39158)#define IMX\_CCM\_LPSPI\_CLK 0x500UL

[ 50](imx__ccm__rev2_8h.md#aaa28d51204ece1b636cfb18ae1c40c36)#define IMX\_CCM\_LPSPI1\_CLK 0x500UL

[ 51](imx__ccm__rev2_8h.md#af9033f72e88c27d5b423201a23ac8a31)#define IMX\_CCM\_LPSPI2\_CLK 0x501UL

[ 52](imx__ccm__rev2_8h.md#a95f654b51e3b94c4f031734761b7db28)#define IMX\_CCM\_LPSPI3\_CLK 0x502UL

[ 53](imx__ccm__rev2_8h.md#a7ef7e62f3bc8b4dc6033628bb54d9f48)#define IMX\_CCM\_LPSPI4\_CLK 0x503UL

[ 54](imx__ccm__rev2_8h.md#ab77afa02a9375dac8d5241db2f6dcb1e)#define IMX\_CCM\_LPSPI5\_CLK 0x504UL

[ 55](imx__ccm__rev2_8h.md#aeaef0fae23329ccf26957f53414bb50e)#define IMX\_CCM\_LPSPI6\_CLK 0x505UL

[ 56](imx__ccm__rev2_8h.md#a6d0905600641bf75064eb4c595e8137f)#define IMX\_CCM\_LPSPI7\_CLK 0x506UL

[ 57](imx__ccm__rev2_8h.md#a29897a97b6c47d61bc7e05785b54ea50)#define IMX\_CCM\_LPSPI8\_CLK 0x507UL

58

59/\* USDHC \*/

[ 60](imx__ccm__rev2_8h.md#a3f07127852de7ae5516c376589f1f780)#define IMX\_CCM\_USDHC1\_CLK 0x600UL

[ 61](imx__ccm__rev2_8h.md#a4596ce38e656971ec5330dab452bd04c)#define IMX\_CCM\_USDHC2\_CLK 0x601UL

62

63/\* DMA \*/

[ 64](imx__ccm__rev2_8h.md#aa82ff051d04371deee96c754d93abb57)#define IMX\_CCM\_EDMA\_CLK 0x700UL

[ 65](imx__ccm__rev2_8h.md#a6bd4f0c4c8fa888f986dedce8e0fc950)#define IMX\_CCM\_EDMA\_LPSR\_CLK 0x701UL

66

67/\* PWM \*/

[ 68](imx__ccm__rev2_8h.md#acbc9256c26bb1232c5ca0eb8bfe52c22)#define IMX\_CCM\_PWM\_CLK 0x800UL

69

70/\* CAN \*/

[ 71](imx__ccm__rev2_8h.md#aded96aef4768dd5f01d14a163cd7487d)#define IMX\_CCM\_CAN\_CLK 0x900UL

[ 72](imx__ccm__rev2_8h.md#a8b4a233a49bf6b078b2b0b51883a49c7)#define IMX\_CCM\_CAN1\_CLK 0x900UL

[ 73](imx__ccm__rev2_8h.md#ae82e9c205254fb85adaedc423cfc7e27)#define IMX\_CCM\_CAN2\_CLK 0x901UL

[ 74](imx__ccm__rev2_8h.md#a16a7e40f69be4d33dd9a9e6aeff03d5e)#define IMX\_CCM\_CAN3\_CLK 0x902UL

75

76/\* GPT \*/

[ 77](imx__ccm__rev2_8h.md#aadc28bb4c97c89e86a8a437262a3afad)#define IMX\_CCM\_GPT\_CLK 0x1000UL

[ 78](imx__ccm__rev2_8h.md#a63ddd8dcc8dca4c5a206348d67c0b57d)#define IMX\_CCM\_GPT1\_CLK 0x1000UL

[ 79](imx__ccm__rev2_8h.md#a8fafcbbe14088a3372e681d0f4071ac3)#define IMX\_CCM\_GPT2\_CLK 0x1001UL

[ 80](imx__ccm__rev2_8h.md#a08cba39dbed192509df1e404d49625d0)#define IMX\_CCM\_GPT3\_CLK 0x1002UL

[ 81](imx__ccm__rev2_8h.md#a454f61392489e49a6534b1c115e6e868)#define IMX\_CCM\_GPT4\_CLK 0x1003UL

[ 82](imx__ccm__rev2_8h.md#a491b53b9f223744586578ea0c1db987f)#define IMX\_CCM\_GPT5\_CLK 0x1004UL

[ 83](imx__ccm__rev2_8h.md#a5892393e285e3cb1b9fcb5a65e29b66e)#define IMX\_CCM\_GPT6\_CLK 0x1005UL

84

85/\* SAI \*/

[ 86](imx__ccm__rev2_8h.md#a398527cf42962caf290b9ce1e5d7f9ac)#define IMX\_CCM\_SAI1\_CLK 0x2000UL

[ 87](imx__ccm__rev2_8h.md#aae6ea492162692b3ae2dc6aed60cc08d)#define IMX\_CCM\_SAI2\_CLK 0x2001UL

[ 88](imx__ccm__rev2_8h.md#a28779c577a92d4806239fe6e254d1a84)#define IMX\_CCM\_SAI3\_CLK 0x2002UL

[ 89](imx__ccm__rev2_8h.md#a598ae9134610f955e78e46a37c063098)#define IMX\_CCM\_SAI4\_CLK 0x2003UL

90

91/\* ENET \*/

[ 92](imx__ccm__rev2_8h.md#aaeff78179dff600c88c1d1986b3976cd)#define IMX\_CCM\_ENET\_CLK 0x3000UL

[ 93](imx__ccm__rev2_8h.md#a2a4beef16589b00f9aca825e7419e9ff)#define IMX\_CCM\_ENET\_PLL 0x3001UL

94

95/\* FLEXSPI \*/

[ 96](imx__ccm__rev2_8h.md#a5f86bba59cc685682df75e66a5d64cea)#define IMX\_CCM\_FLEXSPI\_CLK 0x4000UL

[ 97](imx__ccm__rev2_8h.md#aa471a61b4b453551839b29322ec21422)#define IMX\_CCM\_FLEXSPI2\_CLK 0x4001UL

98

99#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_IMX\_CCM\_REV2\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [imx\_ccm\_rev2.h](imx__ccm__rev2_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
