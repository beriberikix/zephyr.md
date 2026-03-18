---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/mchp-xec-pinctrl_8h_source.html
original_path: doxygen/html/mchp-xec-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mchp-xec-pinctrl.h

[Go to the documentation of this file.](mchp-xec-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2021 Microchip Technology Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_MCHP\_XEC\_PINCTRL\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_MCHP\_XEC\_PINCTRL\_H\_

9

10#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

11

[ 12](mchp-xec-pinctrl_8h.md#adbdaffd4bf6308e5e57f501313339871)#define MCHP\_GPIO 0x0

[ 13](mchp-xec-pinctrl_8h.md#ae0c0be33001f69f4225644ab74f59078)#define MCHP\_AF0 0x0

[ 14](mchp-xec-pinctrl_8h.md#ad1d584cc5e02df71255e0608a04d019f)#define MCHP\_AF1 0x1

[ 15](mchp-xec-pinctrl_8h.md#ad1888b8f9e981d4a54534fca01aab1c4)#define MCHP\_AF2 0x2

[ 16](mchp-xec-pinctrl_8h.md#a9e4512829a2dba4904ab16718c2f54fd)#define MCHP\_AF3 0x3

[ 17](mchp-xec-pinctrl_8h.md#a68e1df87c0a06668cc3897fd8805bc16)#define MCHP\_AF4 0x4

[ 18](mchp-xec-pinctrl_8h.md#adb552a66660db8468dabfae0edcaba71)#define MCHP\_AF5 0x5

[ 19](mchp-xec-pinctrl_8h.md#a1b8833d1dee0e4c9ab63ffc50c8472a5)#define MCHP\_AF6 0x6

[ 20](mchp-xec-pinctrl_8h.md#a3ebbede5ab9560d1ed0889c488e5d658)#define MCHP\_AF7 0x7

[ 21](mchp-xec-pinctrl_8h.md#a57390da1563b872353fdec5d2ce039d0)#define MCHP\_AFMAX 0x8

22

[ 23](mchp-xec-pinctrl_8h.md#a0a93d1975f3a17c0b9ef3a1d79f0b317)#define MCHP\_XEC\_NO\_PUD\_POS 12

[ 24](mchp-xec-pinctrl_8h.md#a6ed13159931220304752a351806670f7)#define MCHP\_XEC\_PD\_POS 13

[ 25](mchp-xec-pinctrl_8h.md#adade4a3941f7c3d9aee288f8f5dd4296)#define MCHP\_XEC\_PU\_POS 14

[ 26](mchp-xec-pinctrl_8h.md#a17adecf816e4f0fd7bb59be66e0701e8)#define MCHP\_XEC\_PUSH\_PULL\_POS 15

[ 27](mchp-xec-pinctrl_8h.md#a539983dc25059710c8286ed12e30449e)#define MCHP\_XEC\_OPEN\_DRAIN\_POS 16

[ 28](mchp-xec-pinctrl_8h.md#ae7d712bf52abcb49e7f57ccef503c025)#define MCHP\_XEC\_OUT\_DIS\_POS 17

[ 29](mchp-xec-pinctrl_8h.md#ababa1d9223423a8fad3264494f9c9e4a)#define MCHP\_XEC\_OUT\_EN\_POS 18

[ 30](mchp-xec-pinctrl_8h.md#ac396fb8f6698d9915f620eb59548a5aa)#define MCHP\_XEC\_OUT\_HI\_POS 19

[ 31](mchp-xec-pinctrl_8h.md#a6b4f5d75d5f9d3620fd60ec08926fbf6)#define MCHP\_XEC\_OUT\_LO\_POS 20

32/\* bit[21] unused \*/

[ 33](mchp-xec-pinctrl_8h.md#aa10630a4dcb92b97e911ec9d38e15a82)#define MCHP\_XEC\_SLEW\_RATE\_POS 22

[ 34](mchp-xec-pinctrl_8h.md#ac916331403b2dfc814a67e541708558d)#define MCHP\_XEC\_SLEW\_RATE\_MSK0 0x3

[ 35](mchp-xec-pinctrl_8h.md#a0d7c618b2bd4a89b24fb0ed3d92609c0)#define MCHP\_XEC\_SLEW\_RATE\_SLOW0 0x1

[ 36](mchp-xec-pinctrl_8h.md#ad359dd0f6c31e1234f0a6cd8c269043e)#define MCHP\_XEC\_SLEW\_RATE\_FAST0 0x2

[ 37](mchp-xec-pinctrl_8h.md#a7e4732960045246965fcf13ef93542bc)#define MCHP\_XEC\_DRV\_STR\_POS 24

[ 38](mchp-xec-pinctrl_8h.md#ac740c2c3b0a7256f3ab485ba671bccce)#define MCHP\_XEC\_DRV\_STR\_MSK0 0x7

[ 39](mchp-xec-pinctrl_8h.md#a77200792cd3b645a76e6e720bf386e2c)#define MCHP\_XEC\_DRV\_STR0\_1X 0x1 /\* 2 or 4(PIO-24) mA \*/

[ 40](mchp-xec-pinctrl_8h.md#a8e804be498ef9a9aa66df2ccf7e2e591)#define MCHP\_XEC\_DRV\_STR0\_2X 0x2 /\* 4 or 8(PIO-24) mA \*/

[ 41](mchp-xec-pinctrl_8h.md#a435fe00b4172ea7c0e43a6720933a09a)#define MCHP\_XEC\_DRV\_STR0\_4X 0x3 /\* 8 or 16(PIO-24) mA \*/

[ 42](mchp-xec-pinctrl_8h.md#a25e8e2002a525cb37ab412d46f71c61b)#define MCHP\_XEC\_DRV\_STR0\_6X 0x4 /\* 12 or 24(PIO-24) mA \*/

[ 43](mchp-xec-pinctrl_8h.md#aec3b775918e3cf9e49275509d6cf18a7)#define MCHP\_XEC\_PIN\_LOW\_POWER\_POS 27

[ 44](mchp-xec-pinctrl_8h.md#a78cd838c620e6f0af49a1765ad2843a9)#define MCHP\_XEC\_FUNC\_INV\_POS 29

45

[ 46](mchp-xec-pinctrl_8h.md#a7e0762ea1ba02d68a6c13c5d0805c60a)#define MCHP\_XEC\_PINMUX\_PORT\_POS 0

[ 47](mchp-xec-pinctrl_8h.md#a27cbf07ff9a28f24d115d788de5567f2)#define MCHP\_XEC\_PINMUX\_PORT\_MSK 0xf

[ 48](mchp-xec-pinctrl_8h.md#a3504bf6d5897c23173f05009a4862c31)#define MCHP\_XEC\_PINMUX\_PIN\_POS 4

[ 49](mchp-xec-pinctrl_8h.md#a8537436b6e3c94e965c0a27992b04d35)#define MCHP\_XEC\_PINMUX\_PIN\_MSK 0x1f

[ 50](mchp-xec-pinctrl_8h.md#a4a8aea0c15ea3d89d4bac2629fa43c18)#define MCHP\_XEC\_PINMUX\_FUNC\_POS 9

[ 51](mchp-xec-pinctrl_8h.md#ab39f30494ce30f88f18cbfdd835cbb6f)#define MCHP\_XEC\_PINMUX\_FUNC\_MSK 0x7

52

53/\* n is octal pin number or equivalent in another base.

54 \* MCHP XEC documentation specifies pin numbers in octal.

55 \* f is function number

56 \* b[3:0] = pin bank

57 \* b[8:4] = pin position in bank

58 \* b[11:9] = function

59 \*/

[ 60](mchp-xec-pinctrl_8h.md#a9ce81e5379ef60140ed6251e30825fe9)#define MCHP\_XEC\_PINMUX(n, f) \

61 (((((n) >> 5) & MCHP\_XEC\_PINMUX\_PORT\_MSK) << MCHP\_XEC\_PINMUX\_PORT\_POS) | \

62 (((n) & MCHP\_XEC\_PINMUX\_PIN\_MSK) << MCHP\_XEC\_PINMUX\_PIN\_POS) | \

63 (((f) & MCHP\_XEC\_PINMUX\_FUNC\_MSK) << MCHP\_XEC\_PINMUX\_FUNC\_POS))

64

65

[ 66](mchp-xec-pinctrl_8h.md#a04e9b92f5d748649eb516e628141d6f8)#define MCHP\_XEC\_PINMUX\_PORT(p) \

67 (((p) >> MCHP\_XEC\_PINMUX\_PORT\_POS) & MCHP\_XEC\_PINMUX\_PORT\_MSK)

68

[ 69](mchp-xec-pinctrl_8h.md#a06fabe0e1bb56de3c56fc278d3f2da6f)#define MCHP\_XEC\_PINMUX\_PIN(p) \

70 (((p) >> MCHP\_XEC\_PINMUX\_PIN\_POS) & MCHP\_XEC\_PINMUX\_PIN\_MSK)

71

[ 72](mchp-xec-pinctrl_8h.md#a90649c60bd81e6cc2dca37ea32d8ad25)#define MCHP\_XEC\_PINMUX\_FUNC(p) \

73 (((p) >> MCHP\_XEC\_PINMUX\_FUNC\_POS) & MCHP\_XEC\_PINMUX\_FUNC\_MSK)

74

[ 75](mchp-xec-pinctrl_8h.md#a8f8edb939c9f5f9702253a24dc9bde3d)#define MEC\_XEC\_PINMUX\_PORT\_PIN(p) \

76 ((p) & ((MCHP\_XEC\_PINMUX\_PORT\_MSK << MCHP\_XEC\_PINMUX\_PORT\_POS) | \

77 (MCHP\_XEC\_PINMUX\_PIN\_MSK << MCHP\_XEC\_PINMUX\_PIN\_POS)))

78

79#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_MCHP\_XEC\_PINCTRL\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [mchp-xec-pinctrl.h](mchp-xec-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
