---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stm32f1-pinctrl_8h_source.html
original_path: doxygen/html/stm32f1-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32f1-pinctrl.h

[Go to the documentation of this file.](stm32f1-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2017 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_STM32\_PINCTRLF1\_H\_

8#define ZEPHYR\_STM32\_PINCTRLF1\_H\_

9

10#include <[zephyr/dt-bindings/pinctrl/stm32-pinctrl-common.h](stm32-pinctrl-common_8h.md)>

11#include <[zephyr/dt-bindings/pinctrl/stm32f1-afio.h](stm32f1-afio_8h.md)>

12

13/\* Adapted from Linux: include/dt-bindings/pinctrl/stm32-pinfunc.h \*/

14

19

[ 20](stm32f1-pinctrl_8h.md#a1b9d630e0c184195bfece6550ae74870)#define STM32\_MODE\_SHIFT 0U

[ 21](stm32f1-pinctrl_8h.md#a12472016d6448c797707d2d062d6011d)#define STM32\_MODE\_MASK 0x3U

[ 22](stm32f1-pinctrl_8h.md#a608cb76ac837e5b0b8ebbbc982ac1dc6)#define STM32\_LINE\_SHIFT 2U

[ 23](stm32f1-pinctrl_8h.md#a51d75677040be2ea1204ab667fd1d6f6)#define STM32\_LINE\_MASK 0xFU

[ 24](stm32f1-pinctrl_8h.md#a0fa09fe492147c76a6b2f191e39d3b9f)#define STM32\_PORT\_SHIFT 6U

[ 25](stm32f1-pinctrl_8h.md#ad7a035f83320bdf867b030bb0dac5221)#define STM32\_PORT\_MASK 0xFU

[ 26](stm32f1-pinctrl_8h.md#ac805a8539bc58646fde819b259510f3c)#define STM32\_REMAP\_SHIFT 10U

[ 27](stm32f1-pinctrl_8h.md#a195e89eb01366f50937857a014a8c780)#define STM32\_REMAP\_MASK 0x3FFU

28

[ 44](stm32f1-pinctrl_8h.md#a66ff36e6fb75c1ebef645f7f8d89ace5)#define STM32F1\_PINMUX(port, line, mode, remap) \

45 (((((port) - 'A') & STM32\_PORT\_MASK) << STM32\_PORT\_SHIFT) | \

46 (((line) & STM32\_LINE\_MASK) << STM32\_LINE\_SHIFT) | \

47 (((mode) & STM32\_MODE\_MASK) << STM32\_MODE\_SHIFT) | \

48 (((remap) & STM32\_REMAP\_MASK) << STM32\_REMAP\_SHIFT))

49

53

[ 54](stm32f1-pinctrl_8h.md#ac7190c598c8618207180d135c0650dac)#define ALTERNATE 0x0 /\* Alternate function output \*/

[ 55](stm32f1-pinctrl_8h.md#aa253a7f9c099890d2575f29dda32f154)#define GPIO\_IN 0x1 /\* Input \*/

[ 56](stm32f1-pinctrl_8h.md#ad42aa2404559d4a465d5d45e857f2881)#define ANALOG 0x2 /\* Analog \*/

[ 57](stm32f1-pinctrl_8h.md#aa0d5e0e1b44c5015f31a44079fd2d9e6)#define GPIO\_OUT 0x3 /\* Output \*/

58

74

75/\* Port Mode \*/

[ 76](stm32f1-pinctrl_8h.md#aa9844618e3818188246a2f0e63f912b6)#define STM32\_MODE\_INPUT (0x0 << STM32\_MODE\_INOUT\_SHIFT)

[ 77](stm32f1-pinctrl_8h.md#acf96fd2b20693c4ca01c4a2ed63868fc)#define STM32\_MODE\_OUTPUT (0x1 << STM32\_MODE\_INOUT\_SHIFT)

[ 78](stm32f1-pinctrl_8h.md#a841c95812b5a687b1ff31f2d47400619)#define STM32\_MODE\_INOUT\_MASK 0x1

[ 79](stm32f1-pinctrl_8h.md#a0b6a084d6449a66092f2917fe97df807)#define STM32\_MODE\_INOUT\_SHIFT 0

80

81/\* Input Port configuration \*/

[ 82](stm32f1-pinctrl_8h.md#a856018b58252b011a09e497476537792)#define STM32\_CNF\_IN\_ANALOG (0x0 << STM32\_CNF\_IN\_SHIFT)

[ 83](stm32f1-pinctrl_8h.md#a7c00df479b30101b86ac3b10edee754a)#define STM32\_CNF\_IN\_FLOAT (0x1 << STM32\_CNF\_IN\_SHIFT)

[ 84](stm32f1-pinctrl_8h.md#ab7cd39547fa5551446d18f8177be0817)#define STM32\_CNF\_IN\_PUPD (0x2 << STM32\_CNF\_IN\_SHIFT)

[ 85](stm32f1-pinctrl_8h.md#ad3a214e677771609666090119836b681)#define STM32\_CNF\_IN\_MASK 0x3

[ 86](stm32f1-pinctrl_8h.md#ab02cc6e05b7f86fe5751b4997090cf32)#define STM32\_CNF\_IN\_SHIFT 1

87

88/\* Output Port configuration \*/

[ 89](stm32f1-pinctrl_8h.md#a3785ba0db5f78b533cc6edf70f130d89)#define STM32\_MODE\_OUTPUT\_MAX\_10 (0x0 << STM32\_MODE\_OSPEED\_SHIFT)

[ 90](stm32f1-pinctrl_8h.md#aa785e1cfc212b7d6eee9b4c651f21fde)#define STM32\_MODE\_OUTPUT\_MAX\_2 (0x1 << STM32\_MODE\_OSPEED\_SHIFT)

[ 91](stm32f1-pinctrl_8h.md#a859c5c65cb08906b2e32cf5a913f2676)#define STM32\_MODE\_OUTPUT\_MAX\_50 (0x2 << STM32\_MODE\_OSPEED\_SHIFT)

[ 92](stm32f1-pinctrl_8h.md#af2eb3a3d0357ac7feaf6568e451e3a66)#define STM32\_MODE\_OSPEED\_MASK 0x3

[ 93](stm32f1-pinctrl_8h.md#a8222a953484ca865a95621b67b477dff)#define STM32\_MODE\_OSPEED\_SHIFT 3

94

[ 95](stm32f1-pinctrl_8h.md#a31a0e44e3786b4964a378e40ac7e3039)#define STM32\_CNF\_PUSH\_PULL (0x0 << STM32\_CNF\_OUT\_0\_SHIFT)

[ 96](stm32f1-pinctrl_8h.md#a93420385c3de44310b8afe9662c42b5f)#define STM32\_CNF\_OPEN\_DRAIN (0x1 << STM32\_CNF\_OUT\_0\_SHIFT)

[ 97](stm32f1-pinctrl_8h.md#afbeddc9889f338ff54255b7790f8e3c2)#define STM32\_CNF\_OUT\_0\_MASK 0x1

[ 98](stm32f1-pinctrl_8h.md#a0caefc9c2aac184c27fbc5bcd58c6507)#define STM32\_CNF\_OUT\_0\_SHIFT 5

99

[ 100](stm32f1-pinctrl_8h.md#a44801ba78bae673cb7ff40582065e307)#define STM32\_CNF\_GP\_OUTPUT (0x0 << STM32\_CNF\_OUT\_1\_SHIFT)

[ 101](stm32f1-pinctrl_8h.md#a8f9dee20ce6a566b1b513775be332557)#define STM32\_CNF\_ALT\_FUNC (0x1 << STM32\_CNF\_OUT\_1\_SHIFT)

[ 102](stm32f1-pinctrl_8h.md#ae622832d07c96d971b2b19ee31d015d9)#define STM32\_CNF\_OUT\_1\_MASK 0x1

[ 103](stm32f1-pinctrl_8h.md#a3ae3d43708c37131013dfff3ad6dac65)#define STM32\_CNF\_OUT\_1\_SHIFT 6

104

105/\* GPIO High impedance/Pull-up/Pull-down \*/

[ 106](stm32f1-pinctrl_8h.md#a63de2d9375292f21b01416a00ceae2e6)#define STM32\_PUPD\_NO\_PULL (0x0 << STM32\_PUPD\_SHIFT)

[ 107](stm32f1-pinctrl_8h.md#a6b957a3e51de3ab1240683716ee4070a)#define STM32\_PUPD\_PULL\_UP (0x1 << STM32\_PUPD\_SHIFT)

[ 108](stm32f1-pinctrl_8h.md#aec7ac04636b53a680170c34048ec4ede)#define STM32\_PUPD\_PULL\_DOWN (0x2 << STM32\_PUPD\_SHIFT)

[ 109](stm32f1-pinctrl_8h.md#a64d43e1964d6ac8138030e5aace05b9a)#define STM32\_PUPD\_MASK 0x3

[ 110](stm32f1-pinctrl_8h.md#a66c8da0f11600f1e52df10c8a60816a4)#define STM32\_PUPD\_SHIFT 7

111

112/\* GPIO plain output value \*/

[ 113](stm32f1-pinctrl_8h.md#a48ba1ca7035db7a74e9a79ea4ec7e3a5)#define STM32\_ODR\_0 (0x0 << STM32\_ODR\_SHIFT)

[ 114](stm32f1-pinctrl_8h.md#ab705ff660828b74fe36bdb6584db4467)#define STM32\_ODR\_1 (0x1 << STM32\_ODR\_SHIFT)

[ 115](stm32f1-pinctrl_8h.md#a2228a72e108e811ee0f31092fa6f9dd9)#define STM32\_ODR\_MASK 0x1

[ 116](stm32f1-pinctrl_8h.md#a6ae722db87e6732c90c96dd85d5424b3)#define STM32\_ODR\_SHIFT 9

117

118#endif /\* ZEPHYR\_STM32\_PINCTRLF1\_H\_ \*/

[stm32-pinctrl-common.h](stm32-pinctrl-common_8h.md)

[stm32f1-afio.h](stm32f1-afio_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [stm32f1-pinctrl.h](stm32f1-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
