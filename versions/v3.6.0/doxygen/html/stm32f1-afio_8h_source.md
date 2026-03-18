---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/stm32f1-afio_8h_source.html
original_path: doxygen/html/stm32f1-afio_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32f1-afio.h

[Go to the documentation of this file.](stm32f1-afio_8h.md)

1/\*

2 \* Copyright (c) 2021 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_STM32\_AFIO\_H\_

8#define ZEPHYR\_STM32\_AFIO\_H\_

9

[ 10](stm32f1-afio_8h.md#ade5f8ba7372fa491075880f76e550b6c)#define STM32\_REMAP\_REG\_MASK 0x1U

[ 11](stm32f1-afio_8h.md#acbb01f8e98a95fe5460465e4ca2ba3e0)#define STM32\_REMAP\_REG\_SHIFT 0U

[ 12](stm32f1-afio_8h.md#a3cebc2d1cda7877f745ea12092794223)#define STM32\_REMAP\_SHIFT\_MASK 0x1FU

[ 13](stm32f1-afio_8h.md#a1e14e8db39fbc3e33132adc10ad7067d)#define STM32\_REMAP\_SHIFT\_SHIFT 1U

[ 14](stm32f1-afio_8h.md#a6e9613bf8369a7d1efa96cb90345a97a)#define STM32\_REMAP\_MASK\_MASK 0x3U

[ 15](stm32f1-afio_8h.md#a3ffdee2c3eb7a004285180731366c15d)#define STM32\_REMAP\_MASK\_SHIFT 6U

[ 16](stm32f1-afio_8h.md#a9cb1b934dd4621ebfae5115459efbd6e)#define STM32\_REMAP\_VAL\_MASK 0x3U

[ 17](stm32f1-afio_8h.md#a144bfbe208a98ddc641ff538aa4738cc)#define STM32\_REMAP\_VAL\_SHIFT 8U

18

[ 32](stm32f1-afio_8h.md#a200a3a748707c11bfd3129c16fc6a835)#define STM32\_REMAP(val, mask, shift, reg) \

33 ((((reg) & STM32\_REMAP\_REG\_MASK) << STM32\_REMAP\_REG\_SHIFT) | \

34 (((shift) & STM32\_REMAP\_SHIFT\_MASK) << STM32\_REMAP\_SHIFT\_SHIFT) | \

35 (((mask) & STM32\_REMAP\_MASK\_MASK) << STM32\_REMAP\_MASK\_SHIFT) | \

36 (((val) & STM32\_REMAP\_VAL\_MASK) << STM32\_REMAP\_VAL\_SHIFT))

37

38

39/\* Accessors for remap value \*/

40

[ 46](stm32f1-afio_8h.md#a9d21e2ff45da0e873e6c8d1012c001f5)#define STM32\_REMAP\_REG\_GET(remap) \

47 (((remap) >> STM32\_REMAP\_REG\_SHIFT) & STM32\_REMAP\_REG\_MASK)

48

[ 54](stm32f1-afio_8h.md#a7a61290a7587f5680a8ff183d1c2907d)#define STM32\_REMAP\_SHIFT\_GET(remap) \

55 (((remap) >> STM32\_REMAP\_SHIFT\_SHIFT) & STM32\_REMAP\_SHIFT\_MASK)

56

[ 62](stm32f1-afio_8h.md#a71aeec8660001f84d3c55f426fdb7137)#define STM32\_REMAP\_MASK\_GET(remap) \

63 (((remap) >> STM32\_REMAP\_MASK\_SHIFT) & STM32\_REMAP\_MASK\_MASK)

64

[ 70](stm32f1-afio_8h.md#a60b741decc8673b9f9a99b7a05d5e9fc)#define STM32\_REMAP\_VAL\_GET(remap) \

71 (((remap) >> STM32\_REMAP\_VAL\_SHIFT) & STM32\_REMAP\_VAL\_MASK)

72

73

74/\* Remap values definitions, according to RM0008.pdf \*/

75

[ 76](stm32f1-afio_8h.md#a2c91303d8a35d5fcbfa8621173d3fe07)#define STM32\_AFIO\_MAPR 0U

[ 77](stm32f1-afio_8h.md#aa60a0ba8748fc37c64efcd19947e664e)#define STM32\_AFIO\_MAPR2 1U

78

[ 80](stm32f1-afio_8h.md#a1a8dfdc80d2d337f72699eca6ed3d957)#define NO\_REMAP 0

81

[ 83](stm32f1-afio_8h.md#ae6f376590d4b2ec77260306a119ad235)#define SPI1\_REMAP0 STM32\_REMAP(0U, 0x1U, 0U, STM32\_AFIO\_MAPR)

[ 85](stm32f1-afio_8h.md#ab655e58c31c71abbecb333cc6f91d9c4)#define SPI1\_REMAP1 STM32\_REMAP(1U, 0x1U, 0U, STM32\_AFIO\_MAPR)

86

[ 88](stm32f1-afio_8h.md#ad235d9e97ed9df493d76cd77f70ca951)#define I2C1\_REMAP0 STM32\_REMAP(0U, 0x1U, 1U, STM32\_AFIO\_MAPR)

[ 90](stm32f1-afio_8h.md#a312613c6dc75976919fec8f63fcb2010)#define I2C1\_REMAP1 STM32\_REMAP(1U, 0x1U, 1U, STM32\_AFIO\_MAPR)

91

[ 93](stm32f1-afio_8h.md#a5a79382b9eb0e4e502b8c84697a73433)#define USART1\_REMAP0 STM32\_REMAP(0U, 0x1U, 2U, STM32\_AFIO\_MAPR)

[ 95](stm32f1-afio_8h.md#ab002c165fc3d6a9e043164560a211f68)#define USART1\_REMAP1 STM32\_REMAP(1U, 0x1U, 2U, STM32\_AFIO\_MAPR)

96

[ 98](stm32f1-afio_8h.md#afd7dc4010b32a1f10510cc39e1c911da)#define USART2\_REMAP0 STM32\_REMAP(0U, 0x1U, 3U, STM32\_AFIO\_MAPR)

[ 100](stm32f1-afio_8h.md#a472167bf97fff0caba80fe06a56b8084)#define USART2\_REMAP1 STM32\_REMAP(1U, 0x1U, 3U, STM32\_AFIO\_MAPR)

101

[ 103](stm32f1-afio_8h.md#a45b45e1ad6629299c0efd15b2233cd0e)#define USART3\_REMAP0 STM32\_REMAP(0U, 0x3U, 4U, STM32\_AFIO\_MAPR)

[ 105](stm32f1-afio_8h.md#a3953583002841a586c85cbbb5d5fc931)#define USART3\_REMAP1 STM32\_REMAP(1U, 0x3U, 4U, STM32\_AFIO\_MAPR)

[ 107](stm32f1-afio_8h.md#a9642c16b4169ed0552056f8ee638ceb2)#define USART3\_REMAP2 STM32\_REMAP(3U, 0x3U, 4U, STM32\_AFIO\_MAPR)

108

[ 110](stm32f1-afio_8h.md#a65b1a18a202a22d8c9add530fd0a8313)#define TIM1\_REMAP0 STM32\_REMAP(0U, 0x3U, 6U, STM32\_AFIO\_MAPR)

[ 112](stm32f1-afio_8h.md#aa7a6c64fab50803704cfc5f6a3fe4c9f)#define TIM1\_REMAP1 STM32\_REMAP(1U, 0x3U, 6U, STM32\_AFIO\_MAPR)

[ 114](stm32f1-afio_8h.md#a8de28395b1ecc659fbe3e4b33a8aaf76)#define TIM1\_REMAP2 STM32\_REMAP(3U, 0x3U, 6U, STM32\_AFIO\_MAPR)

115

[ 117](stm32f1-afio_8h.md#a9ac0bc54a91246b78d863ba3a215ea96)#define TIM2\_REMAP0 STM32\_REMAP(0U, 0x3U, 8U, STM32\_AFIO\_MAPR)

[ 119](stm32f1-afio_8h.md#a6fad8ce0389fa7b6d5a80c501ed99ce9)#define TIM2\_REMAP1 STM32\_REMAP(1U, 0x3U, 8U, STM32\_AFIO\_MAPR)

[ 121](stm32f1-afio_8h.md#ae47bd66bc1f02dc89a624c7639ad492b)#define TIM2\_REMAP2 STM32\_REMAP(2U, 0x3U, 8U, STM32\_AFIO\_MAPR)

[ 123](stm32f1-afio_8h.md#ae3739bffc6fef7ca2aed06327fe26259)#define TIM2\_REMAP3 STM32\_REMAP(3U, 0x3U, 8U, STM32\_AFIO\_MAPR)

124

[ 126](stm32f1-afio_8h.md#a535bdd60f1276bf660814c665c3ca349)#define TIM3\_REMAP0 STM32\_REMAP(0U, 0x3U, 10U, STM32\_AFIO\_MAPR)

[ 128](stm32f1-afio_8h.md#a068f135e7a2273b9eab28b934b0a7e53)#define TIM3\_REMAP1 STM32\_REMAP(1U, 0x3U, 10U, STM32\_AFIO\_MAPR)

[ 130](stm32f1-afio_8h.md#a5c8aa22a44a0b6ef2fbc169aeebdc2ea)#define TIM3\_REMAP2 STM32\_REMAP(2U, 0x3U, 10U, STM32\_AFIO\_MAPR)

[ 132](stm32f1-afio_8h.md#a811f621a99ec1b18a4b5fd4e52456a9f)#define TIM3\_REMAP3 STM32\_REMAP(3U, 0x3U, 10U, STM32\_AFIO\_MAPR)

133

[ 135](stm32f1-afio_8h.md#af19b67747576ad37c76dccc4c8a1ea16)#define TIM4\_REMAP0 STM32\_REMAP(0U, 0x1U, 12U, STM32\_AFIO\_MAPR)

[ 137](stm32f1-afio_8h.md#aafb51d9eacaf920f3c78425ecaf5478e)#define TIM4\_REMAP1 STM32\_REMAP(1U, 0x1U, 12U, STM32\_AFIO\_MAPR)

138

[ 140](stm32f1-afio_8h.md#a6e8abc893ec0c03751427ff220eaf34a)#define CAN\_REMAP0 STM32\_REMAP(0U, 0x3U, 13U, STM32\_AFIO\_MAPR)

[ 142](stm32f1-afio_8h.md#a20407640b3d6f5a1c326546a8b3a10e9)#define CAN\_REMAP1 STM32\_REMAP(2U, 0x3U, 13U, STM32\_AFIO\_MAPR)

[ 144](stm32f1-afio_8h.md#aa1aaf1eeddccdbfd3621145c709dc48d)#define CAN\_REMAP2 STM32\_REMAP(3U, 0x3U, 13U, STM32\_AFIO\_MAPR)

145

[ 147](stm32f1-afio_8h.md#a536898ad320fddd9754cca453f1b9223)#define CAN1\_REMAP0 CAN\_REMAP0

[ 148](stm32f1-afio_8h.md#a5b032fc54211b2ac4964bc924f09a75d)#define CAN1\_REMAP1 CAN\_REMAP1

[ 149](stm32f1-afio_8h.md#ab16bbfb04e8b2b73bdd560a9a14c4df1)#define CAN1\_REMAP2 CAN\_REMAP2

150

[ 152](stm32f1-afio_8h.md#a663f8f668fe27ac44a70990db3d19a40)#define ETH\_REMAP0 STM32\_REMAP(0U, 0x1U, 21U, STM32\_AFIO\_MAPR)

[ 154](stm32f1-afio_8h.md#abcf6340d39300d1c33b0592160614de9)#define ETH\_REMAP1 STM32\_REMAP(1U, 0x1U, 21U, STM32\_AFIO\_MAPR)

155

[ 157](stm32f1-afio_8h.md#a1c2991b25909c6297e22542cfa418548)#define CAN2\_REMAP0 STM32\_REMAP(0U, 0x1U, 22U, STM32\_AFIO\_MAPR)

[ 159](stm32f1-afio_8h.md#aa048c7e4fb84a22c8ad40e9c0fc5e51a)#define CAN2\_REMAP1 STM32\_REMAP(1U, 0x1U, 22U, STM32\_AFIO\_MAPR)

160

[ 162](stm32f1-afio_8h.md#a7dcb5bfc48d08c9d4dbe793b8d232a45)#define SPI3\_REMAP0 STM32\_REMAP(0U, 0x1U, 28U, STM32\_AFIO\_MAPR)

[ 164](stm32f1-afio_8h.md#a401e4124c07719248294b0ee08ebc83c)#define SPI3\_REMAP1 STM32\_REMAP(1U, 0x1U, 28U, STM32\_AFIO\_MAPR)

165

[ 167](stm32f1-afio_8h.md#ac3b499810e4bcae2211adb6c02eb7815)#define I2S3\_REMAP0 SPI3\_REMAP0

[ 169](stm32f1-afio_8h.md#a47c88171fa34dbd74f7c163a9227ae28)#define I2S3\_REMAP1 SPI3\_REMAP1

170

[ 172](stm32f1-afio_8h.md#a075dc7fea001772986dfe31d9d9e8f9a)#define TIM9\_REMAP0 STM32\_REMAP(0U, 0x1U, 5U, STM32\_AFIO\_MAPR2)

[ 174](stm32f1-afio_8h.md#ad443ec934247e04996bf85b5ce9ef721)#define TIM9\_REMAP1 STM32\_REMAP(1U, 0x1U, 5U, STM32\_AFIO\_MAPR2)

175

[ 177](stm32f1-afio_8h.md#af5450df359cf37725a34f89b1af168e7)#define TIM10\_REMAP0 STM32\_REMAP(0U, 0x1U, 6U, STM32\_AFIO\_MAPR2)

[ 179](stm32f1-afio_8h.md#a691a581fe6dd08fd9a5a048abc5eaa3e)#define TIM10\_REMAP1 STM32\_REMAP(1U, 0x1U, 6U, STM32\_AFIO\_MAPR2)

180

[ 182](stm32f1-afio_8h.md#a01e4adf5326f92d144d45ba4b898ed8e)#define TIM11\_REMAP0 STM32\_REMAP(0U, 0x1U, 7U, STM32\_AFIO\_MAPR2)

[ 184](stm32f1-afio_8h.md#a7dcef4a23add63b6eb1254e6146dbe71)#define TIM11\_REMAP1 STM32\_REMAP(1U, 0x1U, 7U, STM32\_AFIO\_MAPR2)

185

[ 187](stm32f1-afio_8h.md#a2a6704eee24037ee9edd3873a5245ea0)#define TIM13\_REMAP0 STM32\_REMAP(0U, 0x1U, 8U, STM32\_AFIO\_MAPR2)

[ 189](stm32f1-afio_8h.md#acdcdd0184a5d75722dd1cbdbe2f8212f)#define TIM13\_REMAP1 STM32\_REMAP(1U, 0x1U, 8U, STM32\_AFIO\_MAPR2)

190

[ 192](stm32f1-afio_8h.md#a6c0341b14e851b4093e72932d05de5f5)#define TIM14\_REMAP0 STM32\_REMAP(0U, 0x1U, 9U, STM32\_AFIO\_MAPR2)

[ 194](stm32f1-afio_8h.md#ab047fa455523413d447f676fe9907c84)#define TIM14\_REMAP1 STM32\_REMAP(1U, 0x1U, 9U, STM32\_AFIO\_MAPR2)

195

[ 197](stm32f1-afio_8h.md#aa7da41d73e1ab29fef6020695f32f773)#define TIM15\_REMAP0 STM32\_REMAP(0U, 0x1U, 0U, STM32\_AFIO\_MAPR2)

[ 199](stm32f1-afio_8h.md#a87f392ac52f61d12709744f1ae8470af)#define TIM15\_REMAP1 STM32\_REMAP(1U, 0x1U, 0U, STM32\_AFIO\_MAPR2)

200

[ 202](stm32f1-afio_8h.md#a26d271515c8666e49cff39a1e5bb8112)#define TIM16\_REMAP0 STM32\_REMAP(0U, 0x1U, 1U, STM32\_AFIO\_MAPR2)

[ 204](stm32f1-afio_8h.md#a9459d0003315751cc5969c7ce1146947)#define TIM16\_REMAP1 STM32\_REMAP(1U, 0x1U, 1U, STM32\_AFIO\_MAPR2)

205

[ 207](stm32f1-afio_8h.md#a0c0e509d60821ac498a4fa03c4d5a47b)#define TIM17\_REMAP0 STM32\_REMAP(0U, 0x1U, 2U, STM32\_AFIO\_MAPR2)

[ 209](stm32f1-afio_8h.md#ae5da6d9ae0c81a39ba7c7f51135be110)#define TIM17\_REMAP1 STM32\_REMAP(1U, 0x1U, 2U, STM32\_AFIO\_MAPR2)

210

211#endif /\* ZEPHYR\_STM32\_AFIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [stm32f1-afio.h](stm32f1-afio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
