---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ch32v20x__30x-pinctrl_8h_source.html
original_path: doxygen/html/ch32v20x__30x-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ch32v20x\_30x-pinctrl.h

[Go to the documentation of this file.](ch32v20x__30x-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2024 MASSDRIVER EI (massdriver.space)

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef \_\_CH32V20X\_V30X\_PINCTRL\_H\_\_

8#define \_\_CH32V20X\_V30X\_PINCTRL\_H\_\_

9

[ 10](ch32v20x__30x-pinctrl_8h.md#a51465d6128a82cfb9710d7ca9ca7b4aa)#define CH32V20X\_V30X\_PINMUX\_PORT\_PA 0

[ 11](ch32v20x__30x-pinctrl_8h.md#afa37f91197b4584e90ef095032ca02e0)#define CH32V20X\_V30X\_PINMUX\_PORT\_PB 1

[ 12](ch32v20x__30x-pinctrl_8h.md#aecad12e41fe4ba815f057491a34f281c)#define CH32V20X\_V30X\_PINMUX\_PORT\_PC 2

[ 13](ch32v20x__30x-pinctrl_8h.md#a5bf35962643cf2a1577615b97fcd3d15)#define CH32V20X\_V30X\_PINMUX\_PORT\_PD 3

[ 14](ch32v20x__30x-pinctrl_8h.md#ac520674a33958bc026399a648a07b115)#define CH32V20X\_V30X\_PINMUX\_PORT\_PE 4

15

16/\*

17 \* Defines the starting bit for the remap field.

18 \*/

[ 19](ch32v20x__30x-pinctrl_8h.md#a2a7f444a213f9e3dc0ac0f654d468297)#define CH32V20X\_V30X\_PINMUX\_SPI1\_RM 0

[ 20](ch32v20x__30x-pinctrl_8h.md#a1308a25911c2af107a4e3b4019e798df)#define CH32V20X\_V30X\_PINMUX\_I2C1\_RM 1

[ 21](ch32v20x__30x-pinctrl_8h.md#af96162c26eb155d96d78280a6c81b8d3)#define CH32V20X\_V30X\_PINMUX\_USART1\_RM 2

[ 22](ch32v20x__30x-pinctrl_8h.md#aaa4c34821e9cd24909f0342e74a18704)#define CH32V20X\_V30X\_PINMUX\_USART2\_RM 3

[ 23](ch32v20x__30x-pinctrl_8h.md#ad8a684efe6e3e1b662d7261ebf1aca06)#define CH32V20X\_V30X\_PINMUX\_USART3\_RM 4

[ 24](ch32v20x__30x-pinctrl_8h.md#a9e0a1aa2a2a6789faa74519653b653ce)#define CH32V20X\_V30X\_PINMUX\_TIM1\_RM 6

[ 25](ch32v20x__30x-pinctrl_8h.md#ab424c2cb5b1297b5d388c0694a0a09dc)#define CH32V20X\_V30X\_PINMUX\_TIM2\_RM 8

[ 26](ch32v20x__30x-pinctrl_8h.md#a50ed541429fa56c1bf7e8064c4db8cf0)#define CH32V20X\_V30X\_PINMUX\_TIM3\_RM 10

[ 27](ch32v20x__30x-pinctrl_8h.md#a0aa42acdf961b719f4706b664f514de2)#define CH32V20X\_V30X\_PINMUX\_TIM4\_RM 12

[ 28](ch32v20x__30x-pinctrl_8h.md#a2bb35cb974123c21b7b42ed1977e55ff)#define CH32V20X\_V30X\_PINMUX\_CAN1\_RM 13

[ 29](ch32v20x__30x-pinctrl_8h.md#a5b58b9f00fa85d32b6de2bd8a4e6a7f3)#define CH32V20X\_V30X\_PINMUX\_PD01\_RM 15

[ 30](ch32v20x__30x-pinctrl_8h.md#a42b9496a0806df58d91f9432c2a43b25)#define CH32V20X\_V30X\_PINMUX\_TIM5CH4\_RM 16

[ 31](ch32v20x__30x-pinctrl_8h.md#aed0b936e5ed2909a538124b21c7514e6)#define CH32V20X\_V30X\_PINMUX\_ETH\_RM 21

[ 32](ch32v20x__30x-pinctrl_8h.md#a27ba3b552cda9c6dd6d9e875a73970f7)#define CH32V20X\_V30X\_PINMUX\_CAN2\_RM 22

[ 33](ch32v20x__30x-pinctrl_8h.md#a4a176150aca39fb1135538dae5df2730)#define CH32V20X\_V30X\_PINMUX\_RMII\_RM 23

[ 34](ch32v20x__30x-pinctrl_8h.md#af320afd706be0a66326a4e9c4b5e41e1)#define CH32V20X\_V30X\_PINMUX\_SDI\_RM 24

[ 35](ch32v20x__30x-pinctrl_8h.md#a64659231d644a6bc087c530586dc2845)#define CH32V20X\_V30X\_PINMUX\_SPI3\_RM 28

36

[ 37](ch32v20x__30x-pinctrl_8h.md#a49dcde5a8581770ca5979c36bf3cbb5c)#define CH32V20X\_V30X\_PINMUX\_TIM8\_RM (32 + 2)

[ 38](ch32v20x__30x-pinctrl_8h.md#ad12b391f1e7ee468ff25dbee28ce641a)#define CH32V20X\_V30X\_PINMUX\_TIM9\_RM (32 + 3)

[ 39](ch32v20x__30x-pinctrl_8h.md#ab4f78a4fbfe5c3815ad9884f30cef9e2)#define CH32V20X\_V30X\_PINMUX\_TIM10\_RM (32 + 5)

[ 40](ch32v20x__30x-pinctrl_8h.md#a0a2c71e866bb42efd91483ef8cfaa853)#define CH32V20X\_V30X\_PINMUX\_USART4\_RM (32 + 16)

[ 41](ch32v20x__30x-pinctrl_8h.md#a69e01bfa023d67fc3dec394b6aeb2f52)#define CH32V20X\_V30X\_PINMUX\_USART5\_RM (32 + 18)

[ 42](ch32v20x__30x-pinctrl_8h.md#ab9c3425aa0e07a0eea053bfd7948e1c8)#define CH32V20X\_V30X\_PINMUX\_USART6\_RM (32 + 20)

[ 43](ch32v20x__30x-pinctrl_8h.md#aedb3ebd24640066d9955b12d5ff90ac5)#define CH32V20X\_V30X\_PINMUX\_USART7\_RM (32 + 22)

[ 44](ch32v20x__30x-pinctrl_8h.md#ab14648532a5d434ab818ff0c3e5aba06)#define CH32V20X\_V30X\_PINMUX\_USART8\_RM (32 + 24)

[ 45](ch32v20x__30x-pinctrl_8h.md#ad7a80a2483f94cdf3d0ead920607b503)#define CH32V20X\_V30X\_PINMUX\_USART1\_RM1 (32 + 26)

46

47/\* Port number with 0-4 \*/

[ 48](ch32v20x__30x-pinctrl_8h.md#aed4e26861d162fbe61cdaed1ca7415fa)#define CH32V20X\_V30X\_PINCTRL\_PORT\_SHIFT 0

[ 49](ch32v20x__30x-pinctrl_8h.md#aee3e7baf3cb46d68881c3300a34a57e3)#define CH32V20X\_V30X\_PINCTRL\_PORT\_MASK GENMASK(2, 0)

50/\* Pin number 0-15 \*/

[ 51](ch32v20x__30x-pinctrl_8h.md#ae710e3da4900682f8503796b4c951bd6)#define CH32V20X\_V30X\_PINCTRL\_PIN\_SHIFT 3

[ 52](ch32v20x__30x-pinctrl_8h.md#a583b92cec570b397721550fb9d39cab5)#define CH32V20X\_V30X\_PINCTRL\_PIN\_MASK GENMASK(6, 3)

53/\* Base remap bit 0-31 \*/

[ 54](ch32v20x__30x-pinctrl_8h.md#a9863eb0dd6cde14ed8ac05d436eebd2c)#define CH32V20X\_V30X\_PINCTRL\_RM\_BASE\_SHIFT 7

[ 55](ch32v20x__30x-pinctrl_8h.md#a46f82eabff0640473e72992b7b0bf9dd)#define CH32V20X\_V30X\_PINCTRL\_RM\_BASE\_MASK GENMASK(11, 7)

56/\* Remap Register ID \*/

[ 57](ch32v20x__30x-pinctrl_8h.md#a4c1a993daf3adc53145f22b86f620dc8)#define CH32V20X\_V30X\_PINCTRL\_PCFR\_ID\_SHIFT 12

[ 58](ch32v20x__30x-pinctrl_8h.md#ab1770db62df727fc107b67b92ae0d4a7)#define CH32V20X\_V30X\_PINCTRL\_PCFR\_ID\_MASK GENMASK(12, 12)

59/\* Function remapping ID 0-3 \*/

[ 60](ch32v20x__30x-pinctrl_8h.md#a6ece24490a0e2eeccf07bf327089128e)#define CH32V20X\_V30X\_PINCTRL\_RM\_SHIFT 13

[ 61](ch32v20x__30x-pinctrl_8h.md#ad98a181c7388919af30f022fd7b32ceb)#define CH32V20X\_V30X\_PINCTRL\_RM\_MASK GENMASK(14, 13)

62

[ 63](ch32v20x__30x-pinctrl_8h.md#aead19428a45b399d4df27973fa931366)#define CH32V20X\_V30X\_PINMUX\_DEFINE(port, pin, rm, remapping) \

64 ((CH32V20X\_V30X\_PINMUX\_PORT\_##port << CH32V20X\_V30X\_PINCTRL\_PORT\_SHIFT) | \

65 (pin << CH32V20X\_V30X\_PINCTRL\_PIN\_SHIFT) | \

66 (CH32V20X\_V30X\_PINMUX\_##rm##\_RM << CH32V20X\_V30X\_PINCTRL\_RM\_BASE\_SHIFT) | \

67 (remapping << CH32V20X\_V30X\_PINCTRL\_RM\_SHIFT))

68

69/\* Pin swaps.

70 \* Warning: Some of those do not apply to all packages.

71 \* Verify using reference manual and use CH32V20X\_V30X\_PINMUX\_DEFINE directly if needed.

72 \*/

73

[ 74](ch32v20x__30x-pinctrl_8h.md#ac8eaf66ded1cd82dcda033ee3228ccda)#define USART1\_CK\_PA8\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 8, USART1, 0)

[ 75](ch32v20x__30x-pinctrl_8h.md#ae96f0469b5ef268c392f8cbce90cb18a)#define USART1\_CK\_PA8\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 8, USART1, 1)

[ 76](ch32v20x__30x-pinctrl_8h.md#a4da5a86ccb996ed2bb7c2d41c356f47d)#define USART1\_CK\_PA10\_2 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 10, USART1, 2)

[ 77](ch32v20x__30x-pinctrl_8h.md#a23577b87c657bc0509af1ebbf58e2c11)#define USART1\_CK\_PA5\_3 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 5, USART1, 3)

[ 78](ch32v20x__30x-pinctrl_8h.md#ac3627106c2b6001349a9706ec7c716eb)#define USART1\_TX\_PA9\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 9, USART1, 0)

[ 79](ch32v20x__30x-pinctrl_8h.md#aece6bffe4fb0877a3843ff499d0384ba)#define USART1\_TX\_PB6\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 6, USART1, 1)

[ 80](ch32v20x__30x-pinctrl_8h.md#a36b894c4b5c81449779f2e9809607571)#define USART1\_TX\_PB15\_2 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 15, USART1, 2)

[ 81](ch32v20x__30x-pinctrl_8h.md#a4033d1eefcca124727e5d7981e981ef7)#define USART1\_TX\_PA6\_3 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 6, USART1, 3)

[ 82](ch32v20x__30x-pinctrl_8h.md#acb0548d28ad57cdb81c7b6c12c40e3e7)#define USART1\_RX\_PA10\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 10, USART1, 0)

[ 83](ch32v20x__30x-pinctrl_8h.md#a5536d402f5b2bf7e67cdf243954c54ba)#define USART1\_RX\_PB7\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 7, USART1, 1)

[ 84](ch32v20x__30x-pinctrl_8h.md#ac2be3c7067c605ab450148e897eb13a5)#define USART1\_RX\_PA8\_2 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 8, USART1, 2)

[ 85](ch32v20x__30x-pinctrl_8h.md#ae872cedd985ac7ff68d571abc88d7f81)#define USART1\_RX\_PA7\_3 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 7, USART1, 3)

[ 86](ch32v20x__30x-pinctrl_8h.md#abb19b8d9ff453d38122297ee107e3ca4)#define USART1\_CTS\_PA11\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 11, USART1, 0)

[ 87](ch32v20x__30x-pinctrl_8h.md#ad640c4a937e206b1c1e3cf27d169164e)#define USART1\_CTS\_PA11\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 11, USART1, 1)

[ 88](ch32v20x__30x-pinctrl_8h.md#a509c2c823062f6490647104ce8f9899e)#define USART1\_CTS\_PA5\_2 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 5, USART1, 2)

[ 89](ch32v20x__30x-pinctrl_8h.md#a4d299092c48151c29aedeb56db337d55)#define USART1\_CTS\_PC4\_3 CH32V20X\_V30X\_PINMUX\_DEFINE(PC, 4, USART1, 3)

[ 90](ch32v20x__30x-pinctrl_8h.md#a04254c5f7645e65ec667a493fe38950e)#define USART1\_RTS\_PA12\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 12, USART1, 0)

[ 91](ch32v20x__30x-pinctrl_8h.md#aa30d3556c7bf59052a58eedc34dd02f4)#define USART1\_RTS\_PA12\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 12, USART1, 1)

[ 92](ch32v20x__30x-pinctrl_8h.md#a6d9bdc7d4595608d83baef9390b383e1)#define USART1\_RTS\_PA9\_2 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 9, USART1, 2)

[ 93](ch32v20x__30x-pinctrl_8h.md#a904b5f1a89a4441251ac3269546fb0b5)#define USART1\_RTS\_PC5\_3 CH32V20X\_V30X\_PINMUX\_DEFINE(PC, 5, USART1, 3)

94

[ 95](ch32v20x__30x-pinctrl_8h.md#a8f7886ce98a2950b3098b4bb42859917)#define USART2\_CK\_PA4\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 4, USART2, 0)

[ 96](ch32v20x__30x-pinctrl_8h.md#a07491bf721085882bea6381d3b3cce0c)#define USART2\_CK\_PD7\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PD, 7, USART2, 1)

[ 97](ch32v20x__30x-pinctrl_8h.md#adc33b0832c21dd3b4fd3935b26a84f25)#define USART2\_TX\_PA2\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 2, USART2, 0)

[ 98](ch32v20x__30x-pinctrl_8h.md#a94064af45e454f3e36ef5b695e743c0b)#define USART2\_TX\_PD5\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PD, 5, USART2, 1)

[ 99](ch32v20x__30x-pinctrl_8h.md#a26731782e798e51edaadf9127848172d)#define USART2\_RX\_PA3\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 3, USART2, 0)

[ 100](ch32v20x__30x-pinctrl_8h.md#a5c7b8fdbd05005f1853642c21bb0b862)#define USART2\_RX\_PD6\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PD, 6, USART2, 1)

[ 101](ch32v20x__30x-pinctrl_8h.md#a6012830b6bdfd0d93e5be3f078c88ec7)#define USART2\_CTS\_PA0\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 0, USART2, 0)

[ 102](ch32v20x__30x-pinctrl_8h.md#a801f8c2688c56b96f70927549b8800b8)#define USART2\_CTS\_PD3\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PD, 3, USART2, 1)

[ 103](ch32v20x__30x-pinctrl_8h.md#a248b2b2fac1d9ad350289ac8525e2836)#define USART2\_RTS\_PA1\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 1, USART2, 0)

[ 104](ch32v20x__30x-pinctrl_8h.md#a84fec9d47966e5e5eba5092717738145)#define USART2\_RTS\_PD4\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PD, 4, USART2, 1)

105

[ 106](ch32v20x__30x-pinctrl_8h.md#a580a9e888b66b1ef940931e3c50d8a82)#define USART3\_CK\_PB12\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 12, USART3, 0)

[ 107](ch32v20x__30x-pinctrl_8h.md#a08b3340ddbefe14a7f83586221221cdd)#define USART3\_CK\_PC12\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PC, 12, USART3, 1)

[ 108](ch32v20x__30x-pinctrl_8h.md#ae1537bd4075304b75652ee8aff3b261a)#define USART3\_CK\_PD10\_2 CH32V20X\_V30X\_PINMUX\_DEFINE(PD, 10, USART3, 2)

[ 109](ch32v20x__30x-pinctrl_8h.md#a1d7e571ecbf24a1d466cf9566f13e1f1)#define USART3\_CK\_PD10\_3 CH32V20X\_V30X\_PINMUX\_DEFINE(PD, 10, USART3, 3)

[ 110](ch32v20x__30x-pinctrl_8h.md#ab7c80815efdb45672039bdaf7ceba5f1)#define USART3\_TX\_PB10\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 10, USART3, 0)

[ 111](ch32v20x__30x-pinctrl_8h.md#a8aa67f2e647f44b4d16140045a2fb468)#define USART3\_TX\_PC10\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PC, 10, USART3, 1)

[ 112](ch32v20x__30x-pinctrl_8h.md#ae631de9e8b622e7cd15aa9b7f692539c)#define USART3\_TX\_PA13\_2 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 13, USART3, 2)

[ 113](ch32v20x__30x-pinctrl_8h.md#a397d500c79df8421593d1434e8942d1c)#define USART3\_TX\_PD8\_3 CH32V20X\_V30X\_PINMUX\_DEFINE(PD, 8, USART3, 3)

[ 114](ch32v20x__30x-pinctrl_8h.md#a47c0599acde3f902153a9610ac80df1b)#define USART3\_RX\_PB11\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 11, USART3, 0)

[ 115](ch32v20x__30x-pinctrl_8h.md#af1ba30de0f3a5b6b8a2ad20bd6713f94)#define USART3\_RX\_PC11\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PC, 11, USART3, 1)

[ 116](ch32v20x__30x-pinctrl_8h.md#a88082cbdf55eeb523ab7051cff2272d2)#define USART3\_RX\_PA14\_2 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 14, USART3, 2)

[ 117](ch32v20x__30x-pinctrl_8h.md#aba830c296a9165d71b21bd8df9ca12f4)#define USART3\_RX\_PD9\_3 CH32V20X\_V30X\_PINMUX\_DEFINE(PD, 9, USART3, 3)

[ 118](ch32v20x__30x-pinctrl_8h.md#af8780a32c2e2a1dbc68f59a144316f19)#define USART3\_CTS\_PB13\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 13, USART3, 0)

[ 119](ch32v20x__30x-pinctrl_8h.md#a4bbbcfffa1e1483b88fb8f0453ec1d3d)#define USART3\_CTS\_PB13\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 13, USART3, 1)

[ 120](ch32v20x__30x-pinctrl_8h.md#a4389762fb29eba0d1f8be00c22f45ec6)#define USART3\_CTS\_PD11\_2 CH32V20X\_V30X\_PINMUX\_DEFINE(PD, 11, USART3, 2)

[ 121](ch32v20x__30x-pinctrl_8h.md#a117529fad1b8c89c4339656c7ae07857)#define USART3\_CTS\_PD11\_3 CH32V20X\_V30X\_PINMUX\_DEFINE(PD, 11, USART3, 3)

[ 122](ch32v20x__30x-pinctrl_8h.md#a4af2a76c45bbb4e038eb42fba1eea73c)#define USART3\_RTS\_PB14\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 14, USART3, 0)

[ 123](ch32v20x__30x-pinctrl_8h.md#a8cf5857521ff942113408d4f3e52533a)#define USART3\_RTS\_PB14\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 14, USART3, 1)

[ 124](ch32v20x__30x-pinctrl_8h.md#a8800e10c20836f8c86fce48c630e7078)#define USART3\_RTS\_PD12\_2 CH32V20X\_V30X\_PINMUX\_DEFINE(PD, 12, USART3, 2)

[ 125](ch32v20x__30x-pinctrl_8h.md#a66a9f0aa73ea935668afa4f13b14b0fc)#define USART3\_RTS\_PD12\_3 CH32V20X\_V30X\_PINMUX\_DEFINE(PD, 12, USART3, 3)

126

[ 127](ch32v20x__30x-pinctrl_8h.md#a547b6ac443241af9a051877918eee5d8)#define USART4\_CK\_PB2\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 2, USART4, 0)

[ 128](ch32v20x__30x-pinctrl_8h.md#a683abc4491e3289bb732e4f959e03a9c)#define USART4\_CK\_PA6\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 6, USART4, 1)

[ 129](ch32v20x__30x-pinctrl_8h.md#af05a509db46018d13c1357788d9c6289)#define USART4\_TX\_PB0\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 0, USART4, 0)

[ 130](ch32v20x__30x-pinctrl_8h.md#abff3a5c3a66d1b183ae062b14263abdb)#define USART4\_TX\_PA5\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 5, USART4, 1)

[ 131](ch32v20x__30x-pinctrl_8h.md#a0c29c5fd685bd479dbddcdbc41ee900c)#define USART4\_RX\_PB1\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 1, USART4, 0)

[ 132](ch32v20x__30x-pinctrl_8h.md#a44e24fe0eae98f3a6b3a70e3df4d5228)#define USART4\_RX\_PB5\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 5, USART4, 1)

[ 133](ch32v20x__30x-pinctrl_8h.md#abe9d71f51fbe3e6112db2226fa6e35b5)#define USART4\_CTS\_PB3\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 3, USART4, 0)

[ 134](ch32v20x__30x-pinctrl_8h.md#a253a8b074943ec750169e2cde7c9dd2d)#define USART4\_CTS\_PA7\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 7, USART4, 1)

[ 135](ch32v20x__30x-pinctrl_8h.md#a0e9db468adce46846dcafdd9c43c46b3)#define USART4\_RTS\_PB4\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 4, USART4, 0)

[ 136](ch32v20x__30x-pinctrl_8h.md#a784e69c773ce7b6c63d23ca48e72056e)#define USART4\_RTS\_PA15\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 15, USART4, 1)

137

[ 138](ch32v20x__30x-pinctrl_8h.md#ad8c55ae1430938f5b9f764b0234283e8)#define USART5\_TX\_PC12\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PC, 12, USART5, 0)

[ 139](ch32v20x__30x-pinctrl_8h.md#a67df4f835f2fa90a15db190c9d04b80d)#define USART5\_TX\_PB4\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 4, USART5, 1)

[ 140](ch32v20x__30x-pinctrl_8h.md#a4e34ebfacdbf4ef3e78e6ec900c482ec)#define USART5\_TX\_PE8\_2 CH32V20X\_V30X\_PINMUX\_DEFINE(PE, 8, USART5, 2)

[ 141](ch32v20x__30x-pinctrl_8h.md#a55030a56854915d44e19507ea5fc75c9)#define USART5\_RX\_PD2\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PD, 2, USART5, 0)

[ 142](ch32v20x__30x-pinctrl_8h.md#aea07a85f2671481ab41cfd62d373b641)#define USART5\_RX\_PB5\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 5, USART5, 1)

[ 143](ch32v20x__30x-pinctrl_8h.md#a09a8c32c77f64e21588393c0d32339b8)#define USART5\_RX\_PE9\_2 CH32V20X\_V30X\_PINMUX\_DEFINE(PE, 9, USART5, 2)

144

[ 145](ch32v20x__30x-pinctrl_8h.md#a3a6f92e08bc164fe20aede0cb42b6d81)#define USART6\_TX\_PC0\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PC, 0, USART6, 0)

[ 146](ch32v20x__30x-pinctrl_8h.md#aaad0fe1c95b3ac2bc83ec3cfab41e061)#define USART6\_TX\_PB8\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 8, USART6, 1)

[ 147](ch32v20x__30x-pinctrl_8h.md#a10df9035f85d31246965d708133bd510)#define USART6\_TX\_PE10\_2 CH32V20X\_V30X\_PINMUX\_DEFINE(PE, 10, USART6, 2)

[ 148](ch32v20x__30x-pinctrl_8h.md#a7d6f6d9909f0000c5c2c1e8ac78685de)#define USART6\_RX\_PC1\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PC, 1, USART6, 0)

[ 149](ch32v20x__30x-pinctrl_8h.md#ab0f678ab8aeae007072bb891a46742c4)#define USART6\_RX\_PB9\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 9, USART6, 1)

[ 150](ch32v20x__30x-pinctrl_8h.md#a5951b1689db8bd4b422e27a51b561437)#define USART6\_RX\_PE11\_2 CH32V20X\_V30X\_PINMUX\_DEFINE(PE, 11, USART6, 2)

151

[ 152](ch32v20x__30x-pinctrl_8h.md#a86e0de0d1a0128b303807205cb9e573c)#define USART7\_TX\_PC2\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PC, 2, USART7, 0)

[ 153](ch32v20x__30x-pinctrl_8h.md#a163be1cb202ce604be3744ce74e75486)#define USART7\_TX\_PA6\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 6, USART7, 1)

[ 154](ch32v20x__30x-pinctrl_8h.md#a8a7e6b5fafd8e9cab2552a865f3293d5)#define USART7\_TX\_PE12\_2 CH32V20X\_V30X\_PINMUX\_DEFINE(PE, 12, USART7, 2)

[ 155](ch32v20x__30x-pinctrl_8h.md#ac8424da9bd7bdde9f697626a0787f54d)#define USART7\_RX\_PC3\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PC, 3, USART7, 0)

[ 156](ch32v20x__30x-pinctrl_8h.md#a908193b49e33d616695e4bb58a7fc47a)#define USART7\_RX\_PA7\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 7, USART7, 1)

[ 157](ch32v20x__30x-pinctrl_8h.md#a7a950c16abd0839161d13e640b069b7f)#define USART7\_RX\_PE13\_2 CH32V20X\_V30X\_PINMUX\_DEFINE(PE, 13, USART7, 2)

158

[ 159](ch32v20x__30x-pinctrl_8h.md#af438c57148832499d61fb50ee9c230ef)#define USART8\_TX\_PC4\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PC, 4, USART8, 0)

[ 160](ch32v20x__30x-pinctrl_8h.md#a5fdb620d2332aae4f14d1e9ebe8b883f)#define USART8\_TX\_PA14\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 14, USART8, 1)

[ 161](ch32v20x__30x-pinctrl_8h.md#a8ffebc0ed60335de5b7ba068409204d3)#define USART8\_TX\_PE14\_2 CH32V20X\_V30X\_PINMUX\_DEFINE(PE, 14, USART8, 2)

[ 162](ch32v20x__30x-pinctrl_8h.md#a2f668ecfa52250b0ca929d3d7e81e00c)#define USART8\_RX\_PC5\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PC, 5, USART8, 0)

[ 163](ch32v20x__30x-pinctrl_8h.md#a312761241a791c70aa7ee1ff28e89d4d)#define USART8\_RX\_PA15\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 15, USART8, 1)

[ 164](ch32v20x__30x-pinctrl_8h.md#a38ef75bad029269b54fcfc14d9431e1e)#define USART8\_RX\_PE15\_2 CH32V20X\_V30X\_PINMUX\_DEFINE(PE, 15, USART8, 2)

165

[ 166](ch32v20x__30x-pinctrl_8h.md#a6738b061a38f230297958fa01ff94aba)#define SPI1\_NSS\_PA4\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 4, SPI1, 0)

[ 167](ch32v20x__30x-pinctrl_8h.md#a9c191c312d56b0f40550993182801356)#define SPI1\_NSS\_PA15\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 15, SPI1, 1)

[ 168](ch32v20x__30x-pinctrl_8h.md#a7894cd7ac6cf19bb0860347924697c48)#define SPI1\_SCK\_PA5\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 5, SPI1, 0)

[ 169](ch32v20x__30x-pinctrl_8h.md#a655e98715e57595ee35af7019e4cdc81)#define SPI1\_SCK\_PB3\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 3, SPI1, 1)

[ 170](ch32v20x__30x-pinctrl_8h.md#a01bf9d6164b671e3ccd2089fe9fa22f4)#define SPI1\_MISO\_PA6\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 6, SPI1, 0)

[ 171](ch32v20x__30x-pinctrl_8h.md#aafda7603993bb21615e786a316350ed2)#define SPI1\_MISO\_PB4\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 4, SPI1, 1)

[ 172](ch32v20x__30x-pinctrl_8h.md#ac67869a89839ab30686031d0744e3abe)#define SPI1\_MOSI\_PA7\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 7, SPI1, 0)

[ 173](ch32v20x__30x-pinctrl_8h.md#a6839b1de6217dc7828eecf1b8e6d0562)#define SPI1\_MOSI\_PB5\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 5, SPI1, 1)

174

[ 175](ch32v20x__30x-pinctrl_8h.md#a2bc552ff9173c80de1c12ed880235593)#define I2C1\_SCL\_PB6\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 6, I2C1, 0)

[ 176](ch32v20x__30x-pinctrl_8h.md#a0a42a45f5826edc8690f2799b76a9d74)#define I2C1\_SCL\_PB8\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 8, I2C1, 1)

[ 177](ch32v20x__30x-pinctrl_8h.md#aaa9a448550e938000a0f75352506368b)#define I2C1\_SDA\_PB7\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 7, I2C1, 0)

[ 178](ch32v20x__30x-pinctrl_8h.md#aa07a9ebed46c5c0a3c1384202d7203b3)#define I2C1\_SDA\_PB9\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 9, I2C1, 1)

179

180#define SPI1\_NSS\_PA4\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 4, SPI1, 0)

181#define SPI1\_NSS\_PA15\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 15, SPI1, 1)

182#define SPI1\_SCK\_PA5\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 5, SPI1, 0)

183#define SPI1\_SCK\_PB3\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 3, SPI1, 1)

184#define SPI1\_MISO\_PA6\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 6, SPI1, 0)

185#define SPI1\_MISO\_PB4\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 4, SPI1, 1)

186#define SPI1\_MOSI\_PA7\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 7, SPI1, 0)

187#define SPI1\_MOSI\_PB5\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 5, SPI1, 1)

188

[ 189](ch32v20x__30x-pinctrl_8h.md#a66484c8d7e2b182e504ad25e8c1cf5f1)#define SPI2\_NSS\_PB12\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 12, SPI2, 0)

[ 190](ch32v20x__30x-pinctrl_8h.md#af772daaf3aee53543bd82e206dd75c19)#define SPI2\_SCK\_PB13\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 13, SPI2, 0)

[ 191](ch32v20x__30x-pinctrl_8h.md#a0d6207021d716a7f64ca2357fddfd948)#define SPI2\_MISO\_PB14\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 14, SPI2, 0)

[ 192](ch32v20x__30x-pinctrl_8h.md#ad4d63545952d4c0d2143b977e8a82bc0)#define SPI2\_MOSI\_PB15\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 15, SPI2, 0)

193

[ 194](ch32v20x__30x-pinctrl_8h.md#a3fa58903d033adfed328f2f9ef8cc6ba)#define SPI3\_NSS\_PA15\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 15, SPI3, 0)

[ 195](ch32v20x__30x-pinctrl_8h.md#a838eb3e7d07eab8bb37fa607200ad3f2)#define SPI3\_NSS\_PA4\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PA, 4, SPI3, 1)

[ 196](ch32v20x__30x-pinctrl_8h.md#add04b6160f147706be45c76acee57a37)#define SPI3\_SCK\_PB3\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 3, SPI3, 0)

[ 197](ch32v20x__30x-pinctrl_8h.md#aaba079fb263dc43c0728fa7a74206001)#define SPI3\_SCK\_PC10\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PC, 10, SPI3, 1)

[ 198](ch32v20x__30x-pinctrl_8h.md#a2f6ffac645bac53fa701cc700f860075)#define SPI3\_MISO\_PB4\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 4, SPI3, 0)

[ 199](ch32v20x__30x-pinctrl_8h.md#a27bdb0b5d492bbdeec6a3879cda97d46)#define SPI3\_MISO\_PC11\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PC, 11, SPI3, 1)

[ 200](ch32v20x__30x-pinctrl_8h.md#a323878752b8ee4a7222a836fc4841027)#define SPI3\_MOSI\_PB5\_0 CH32V20X\_V30X\_PINMUX\_DEFINE(PB, 5, SPI3, 0)

[ 201](ch32v20x__30x-pinctrl_8h.md#aaa2437a458d2f47cd613fbf0c1da654e)#define SPI3\_MOSI\_PC12\_1 CH32V20X\_V30X\_PINMUX\_DEFINE(PC, 12, SPI3, 1)

202

203#endif /\* \_\_CH32V20X\_V30X\_PINCTRL\_H\_\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [ch32v20x\_30x-pinctrl.h](ch32v20x__30x-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
