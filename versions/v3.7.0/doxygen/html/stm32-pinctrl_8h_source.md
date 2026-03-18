---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/stm32-pinctrl_8h_source.html
original_path: doxygen/html/stm32-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32-pinctrl.h

[Go to the documentation of this file.](stm32-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2017 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_STM32\_PINCTRL\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_STM32\_PINCTRL\_H\_

9

10#include <[zephyr/dt-bindings/pinctrl/stm32-pinctrl-common.h](stm32-pinctrl-common_8h.md)>

11

12/\* Adapted from Linux: include/dt-bindings/pinctrl/stm32-pinfunc.h \*/

13

17

[ 18](stm32-pinctrl_8h.md#a856e7793927d195e31a0ab801d9320b1)#define STM32\_AF0 0x0

[ 19](stm32-pinctrl_8h.md#ac341ff4da52832f09596ddb8f66d0704)#define STM32\_AF1 0x1

[ 20](stm32-pinctrl_8h.md#af6aa5ae98ba243f120737e8b0ad6644c)#define STM32\_AF2 0x2

[ 21](stm32-pinctrl_8h.md#a3d65bb83c9f0515e218f300171a90b75)#define STM32\_AF3 0x3

[ 22](stm32-pinctrl_8h.md#a286f6ec684e9c7297261f9ed7372e609)#define STM32\_AF4 0x4

[ 23](stm32-pinctrl_8h.md#a9a48f460272ef966b8dd2ead78c8e8e9)#define STM32\_AF5 0x5

[ 24](stm32-pinctrl_8h.md#a5c5b864b9d9d1431a8d905967cae69a4)#define STM32\_AF6 0x6

[ 25](stm32-pinctrl_8h.md#ade35007347e4f04e0e7f2e4f87a4dec3)#define STM32\_AF7 0x7

[ 26](stm32-pinctrl_8h.md#aef1775a7a3af9daed7d72c123db23f08)#define STM32\_AF8 0x8

[ 27](stm32-pinctrl_8h.md#adeb65582e22de51dd619bfd7c49a0653)#define STM32\_AF9 0x9

[ 28](stm32-pinctrl_8h.md#ad8732007cc06358d29379d025203df15)#define STM32\_AF10 0xa

[ 29](stm32-pinctrl_8h.md#ab7bb316e4f29094d7d7a8b08522eec69)#define STM32\_AF11 0xb

[ 30](stm32-pinctrl_8h.md#aaf99ab7b7abc0f5b211afba7dbc75dff)#define STM32\_AF12 0xc

[ 31](stm32-pinctrl_8h.md#a84a34bd261316ab1353d45bbd03437a5)#define STM32\_AF13 0xd

[ 32](stm32-pinctrl_8h.md#a5bc95c95792938f333095422499de8e6)#define STM32\_AF14 0xe

[ 33](stm32-pinctrl_8h.md#a2a2f2b85e7e92f1a7a7baa69ed8c4655)#define STM32\_AF15 0xf

[ 34](stm32-pinctrl_8h.md#a3cef198576d1117a64e34d3981ae69d2)#define STM32\_ANALOG 0x10

[ 35](stm32-pinctrl_8h.md#a6b8fe886fca3bab7d631a90cdfca6a0f)#define STM32\_GPIO 0x11

36

41

[ 42](stm32-pinctrl_8h.md#a1b9d630e0c184195bfece6550ae74870)#define STM32\_MODE\_SHIFT 0U

[ 43](stm32-pinctrl_8h.md#a12472016d6448c797707d2d062d6011d)#define STM32\_MODE\_MASK 0x1FU

[ 44](stm32-pinctrl_8h.md#a608cb76ac837e5b0b8ebbbc982ac1dc6)#define STM32\_LINE\_SHIFT 5U

[ 45](stm32-pinctrl_8h.md#a51d75677040be2ea1204ab667fd1d6f6)#define STM32\_LINE\_MASK 0xFU

[ 46](stm32-pinctrl_8h.md#a0fa09fe492147c76a6b2f191e39d3b9f)#define STM32\_PORT\_SHIFT 9U

[ 47](stm32-pinctrl_8h.md#ad7a035f83320bdf867b030bb0dac5221)#define STM32\_PORT\_MASK 0x1FU

48

[ 62](stm32-pinctrl_8h.md#a0a29e4e3ef1b1e901bf203640bc84dd9)#define STM32\_PINMUX(port, line, mode) \

63 (((((port) - 'A') & STM32\_PORT\_MASK) << STM32\_PORT\_SHIFT) | \

64 (((line) & STM32\_LINE\_MASK) << STM32\_LINE\_SHIFT) | \

65 (((STM32\_ ## mode) & STM32\_MODE\_MASK) << STM32\_MODE\_SHIFT))

66

80

81/\* GPIO Mode \*/

[ 82](stm32-pinctrl_8h.md#a90a61faade25953a971ea39959200da8)#define STM32\_MODER\_INPUT\_MODE (0x0 << STM32\_MODER\_SHIFT)

[ 83](stm32-pinctrl_8h.md#af0c2579f30fd0c4c9908fa5d76a55aa5)#define STM32\_MODER\_OUTPUT\_MODE (0x1 << STM32\_MODER\_SHIFT)

[ 84](stm32-pinctrl_8h.md#a26d39411b37f40082178a0fe7a3b135f)#define STM32\_MODER\_ALT\_MODE (0x2 << STM32\_MODER\_SHIFT)

[ 85](stm32-pinctrl_8h.md#a4507703ea2b3399214ff460fcd78cb91)#define STM32\_MODER\_ANALOG\_MODE (0x3 << STM32\_MODER\_SHIFT)

[ 86](stm32-pinctrl_8h.md#aa5f2e2e47c7915df1f36ce5bb3214a8e)#define STM32\_MODER\_MASK 0x3

[ 87](stm32-pinctrl_8h.md#a7384d84f720e2660ae4d8e1b7fa2d280)#define STM32\_MODER\_SHIFT 4

88

89/\* GPIO Output type \*/

[ 90](stm32-pinctrl_8h.md#a1c2241544c16a546dd7716f9e1c79f4f)#define STM32\_OTYPER\_PUSH\_PULL (0x0 << STM32\_OTYPER\_SHIFT)

[ 91](stm32-pinctrl_8h.md#a202967dcb384d745131708a5ff33f857)#define STM32\_OTYPER\_OPEN\_DRAIN (0x1 << STM32\_OTYPER\_SHIFT)

[ 92](stm32-pinctrl_8h.md#a54ef12cf7862967900cd66bab6fbafb0)#define STM32\_OTYPER\_MASK 0x1

[ 93](stm32-pinctrl_8h.md#a9f4ba8355e6794e8ea92387b3d07fe53)#define STM32\_OTYPER\_SHIFT 6

94

95/\* GPIO speed \*/

[ 96](stm32-pinctrl_8h.md#a5297c898e88bb795d379b7d6179a2c77)#define STM32\_OSPEEDR\_LOW\_SPEED (0x0 << STM32\_OSPEEDR\_SHIFT)

[ 97](stm32-pinctrl_8h.md#a0f99d4fd8cb8821346caed2e8f4fbc8d)#define STM32\_OSPEEDR\_MEDIUM\_SPEED (0x1 << STM32\_OSPEEDR\_SHIFT)

[ 98](stm32-pinctrl_8h.md#a1b9a5be0e0ea97b03f4b88c8dc11599c)#define STM32\_OSPEEDR\_HIGH\_SPEED (0x2 << STM32\_OSPEEDR\_SHIFT)

[ 99](stm32-pinctrl_8h.md#a51b0180d689496d60874b0a153d876fb)#define STM32\_OSPEEDR\_VERY\_HIGH\_SPEED (0x3 << STM32\_OSPEEDR\_SHIFT)

[ 100](stm32-pinctrl_8h.md#a0e0319c5fc5b03907eecc9ac932a60a5)#define STM32\_OSPEEDR\_MASK 0x3

[ 101](stm32-pinctrl_8h.md#abbe5962daa9f7aaffc63ed5b28cca34c)#define STM32\_OSPEEDR\_SHIFT 7

102

103/\* GPIO High impedance/Pull-up/pull-down \*/

[ 104](stm32-pinctrl_8h.md#ae597a50176d61956806f1d9ae5b66d6b)#define STM32\_PUPDR\_NO\_PULL (0x0 << STM32\_PUPDR\_SHIFT)

[ 105](stm32-pinctrl_8h.md#a5f5cf4b1701e7fbd3c4e50ea3d7717ed)#define STM32\_PUPDR\_PULL\_UP (0x1 << STM32\_PUPDR\_SHIFT)

[ 106](stm32-pinctrl_8h.md#a941f508cbf744960077d072b59118df8)#define STM32\_PUPDR\_PULL\_DOWN (0x2 << STM32\_PUPDR\_SHIFT)

[ 107](stm32-pinctrl_8h.md#a7d5d3673847fcb1680ea6c8ce1e58fa7)#define STM32\_PUPDR\_MASK 0x3

[ 108](stm32-pinctrl_8h.md#a21164826201e6cdd17a59f2405f82208)#define STM32\_PUPDR\_SHIFT 9

109

110/\* GPIO plain output value \*/

[ 111](stm32-pinctrl_8h.md#a48ba1ca7035db7a74e9a79ea4ec7e3a5)#define STM32\_ODR\_0 (0x0 << STM32\_ODR\_SHIFT)

[ 112](stm32-pinctrl_8h.md#ab705ff660828b74fe36bdb6584db4467)#define STM32\_ODR\_1 (0x1 << STM32\_ODR\_SHIFT)

[ 113](stm32-pinctrl_8h.md#a2228a72e108e811ee0f31092fa6f9dd9)#define STM32\_ODR\_MASK 0x1

[ 114](stm32-pinctrl_8h.md#a6ae722db87e6732c90c96dd85d5424b3)#define STM32\_ODR\_SHIFT 11

115

116#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_STM32\_PINCTRL\_H\_ \*/

[stm32-pinctrl-common.h](stm32-pinctrl-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [stm32-pinctrl.h](stm32-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
