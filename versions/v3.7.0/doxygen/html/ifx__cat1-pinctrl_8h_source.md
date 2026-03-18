---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ifx__cat1-pinctrl_8h_source.html
original_path: doxygen/html/ifx__cat1-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ifx\_cat1-pinctrl.h

[Go to the documentation of this file.](ifx__cat1-pinctrl_8h.md)

1/\* Copyright 2022 Cypress Semiconductor Corporation (an Infineon company) or

2 \* an affiliate of Cypress Semiconductor Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

10

[ 14](ifx__cat1-pinctrl_8h.md#a6ba3e93a5498c6c5bd5e8f3d0c00ac2a)#define SOC\_PINMUX\_PORT\_POS (0)

[ 15](ifx__cat1-pinctrl_8h.md#a4199ffda078d925e8dfb58194117de1a)#define SOC\_PINMUX\_PORT\_MASK (0xFFul << SOC\_PINMUX\_PORT\_POS)

[ 16](ifx__cat1-pinctrl_8h.md#a5266efcdc6dbcd64d8fc61c814b37dc7)#define SOC\_PINMUX\_PIN\_POS (8)

[ 17](ifx__cat1-pinctrl_8h.md#a881a5ee83663d0eac3a2cfd530e23266)#define SOC\_PINMUX\_PIN\_MASK (0xFFul << SOC\_PINMUX\_PIN\_POS)

[ 18](ifx__cat1-pinctrl_8h.md#a2af56d2b85a6e4ba3a2f1fdd191f8c98)#define SOC\_PINMUX\_HSIOM\_FUNC\_POS (16)

[ 19](ifx__cat1-pinctrl_8h.md#a6baa74b565ac921b7e3b8b5fc65327a6)#define SOC\_PINMUX\_HSIOM\_MASK (0xFFul << SOC\_PINMUX\_HSIOM\_FUNC\_POS)

[ 20](ifx__cat1-pinctrl_8h.md#a38673a696cc1caa97e13eb6ef937007a)#define SOC\_PINMUX\_SIGNAL\_POS (24)

[ 21](ifx__cat1-pinctrl_8h.md#aca26c39aa27a6520ea0f57b7ab058672)#define SOC\_PINMUX\_SIGNAL\_MASK (0xFFul << SOC\_PINMUX\_SIGNAL\_POS)

22

[ 26](ifx__cat1-pinctrl_8h.md#ac0d2af1bfb229de155412af7f00e4fe0)#define HSIOM\_SEL\_GPIO (0)

[ 27](ifx__cat1-pinctrl_8h.md#a441de7f56a1c7c75cdae4d9f93ccfade)#define HSIOM\_SEL\_GPIO\_DSI (1)

[ 28](ifx__cat1-pinctrl_8h.md#a959873e5156c6e3c24dd2773bb1ba516)#define HSIOM\_SEL\_DSI\_DSI (2)

[ 29](ifx__cat1-pinctrl_8h.md#a022f7af586ee9b46f689d187e8dd73d8)#define HSIOM\_SEL\_DSI\_GPIO (3)

[ 30](ifx__cat1-pinctrl_8h.md#a8806729fcb666c9de823be5dd55c873d)#define HSIOM\_SEL\_AMUXA (4)

[ 31](ifx__cat1-pinctrl_8h.md#a862eb93443c5c9575ff990b776b6203b)#define HSIOM\_SEL\_AMUXB (5)

[ 32](ifx__cat1-pinctrl_8h.md#a4ba8695f92c0f347dd25ef981d67d1b0)#define HSIOM\_SEL\_AMUXA\_DSI (6)

[ 33](ifx__cat1-pinctrl_8h.md#af7a28a087a8867a14423e9ab471cce54)#define HSIOM\_SEL\_AMUXB\_DSI (7)

[ 34](ifx__cat1-pinctrl_8h.md#a3080ad4afafa572482ea1a5b49f6a1ce)#define HSIOM\_SEL\_ACT\_0 (8)

[ 35](ifx__cat1-pinctrl_8h.md#a990e35fecfcc37ca08fe709eee746618)#define HSIOM\_SEL\_ACT\_1 (9)

[ 36](ifx__cat1-pinctrl_8h.md#a696aeb76109bf339ebf0fcd20979f211)#define HSIOM\_SEL\_ACT\_2 (10)

[ 37](ifx__cat1-pinctrl_8h.md#a25e956bc540c9570392a1722b7e94670)#define HSIOM\_SEL\_ACT\_3 (11)

[ 38](ifx__cat1-pinctrl_8h.md#afb33417be16e7fa6423fadd2ef4a0f5b)#define HSIOM\_SEL\_DS\_0 (12)

[ 39](ifx__cat1-pinctrl_8h.md#aa06be65ae17fc2dc1861c2af2e364652)#define HSIOM\_SEL\_DS\_1 (13)

[ 40](ifx__cat1-pinctrl_8h.md#a07f591dc1f8a9f9eda13063d8c58c4eb)#define HSIOM\_SEL\_DS\_2 (14)

[ 41](ifx__cat1-pinctrl_8h.md#a157da2f7e72fa8f19dfd682ec4444319)#define HSIOM\_SEL\_DS\_3 (15)

[ 42](ifx__cat1-pinctrl_8h.md#a3336f2e2d4886e0e46819ee4f4d96734)#define HSIOM\_SEL\_ACT\_4 (16)

[ 43](ifx__cat1-pinctrl_8h.md#a1040ff80864b6a1d85eb4c07f4278ea1)#define HSIOM\_SEL\_ACT\_5 (17)

[ 44](ifx__cat1-pinctrl_8h.md#a575188296b25564faa9b3a3b4817b5e4)#define HSIOM\_SEL\_ACT\_6 (18)

[ 45](ifx__cat1-pinctrl_8h.md#ae9c0f6360d56214106b09861eedb911a)#define HSIOM\_SEL\_ACT\_7 (19)

[ 46](ifx__cat1-pinctrl_8h.md#a8d36acbee0c4de7088ddc08a8b1c07a6)#define HSIOM\_SEL\_ACT\_8 (20)

[ 47](ifx__cat1-pinctrl_8h.md#aff276e6f5cdc671648a428c22fc2776e)#define HSIOM\_SEL\_ACT\_9 (21)

[ 48](ifx__cat1-pinctrl_8h.md#a42c5af47fba8b69dacb3064e332193fd)#define HSIOM\_SEL\_ACT\_10 (22)

[ 49](ifx__cat1-pinctrl_8h.md#a48052c8dd78b1403de4d675571b7e6e2)#define HSIOM\_SEL\_ACT\_11 (23)

[ 50](ifx__cat1-pinctrl_8h.md#a6fc1302224b4d7585c25c3dc2ea340e7)#define HSIOM\_SEL\_ACT\_12 (24)

[ 51](ifx__cat1-pinctrl_8h.md#ae4fb8f65206098cace15b3e0f1c12a3e)#define HSIOM\_SEL\_ACT\_13 (25)

[ 52](ifx__cat1-pinctrl_8h.md#a7c3ffb4e79372b4cc4d1a7b4554911d5)#define HSIOM\_SEL\_ACT\_14 (26)

[ 53](ifx__cat1-pinctrl_8h.md#ab3285eea99f44cbe985eb097d1166a3d)#define HSIOM\_SEL\_ACT\_15 (27)

[ 54](ifx__cat1-pinctrl_8h.md#a0f134c65358e450ca55341bbfec1cd0e)#define HSIOM\_SEL\_DS\_4 (28)

[ 55](ifx__cat1-pinctrl_8h.md#a4208fc8f94abf237d943bc5e8ffe3080)#define HSIOM\_SEL\_DS\_5 (29)

[ 56](ifx__cat1-pinctrl_8h.md#ac0153eaa52ef010bf58304a44ecb1e9b)#define HSIOM\_SEL\_DS\_6 (30)

[ 57](ifx__cat1-pinctrl_8h.md#a8c067c1737f0f1573e056a384954fd81)#define HSIOM\_SEL\_DS\_7 (31)

58

[ 62](ifx__cat1-pinctrl_8h.md#ac58363c207e4f8ea82394859044b2690)#define DT\_CAT1\_DRIVE\_MODE\_INFO(peripheral\_signal) \

63 CAT1\_PIN\_MAP\_DRIVE\_MODE\_##peripheral\_signal

64

[ 68](ifx__cat1-pinctrl_8h.md#a33b355e05d5b955a6b8d48f3613c2d9a)#define DT\_CAT1\_PINMUX(port, pin, hsiom) \

69 ((port << SOC\_PINMUX\_PORT\_POS) | \

70 (pin << SOC\_PINMUX\_PIN\_POS) | \

71 (hsiom << SOC\_PINMUX\_HSIOM\_FUNC\_POS))

72

73/\* Redefine DT GPIO label (Px) to CYHAL port macros (CYHAL\_PORT\_x) \*/

[ 74](ifx__cat1-pinctrl_8h.md#a1583b00a62bc1138f99bbfcd8ef81a6a)#define P0 CYHAL\_PORT\_0

[ 75](ifx__cat1-pinctrl_8h.md#a6c2a9f7efd46f0160f3037869924d6ce)#define P1 CYHAL\_PORT\_1

[ 76](ifx__cat1-pinctrl_8h.md#ae00a52dba55d31948c377fa85d385b87)#define P2 CYHAL\_PORT\_2

[ 77](ifx__cat1-pinctrl_8h.md#a0707a89c2f63bd260108e9dbb669358e)#define P3 CYHAL\_PORT\_3

[ 78](ifx__cat1-pinctrl_8h.md#acbc14a33d017f5f2dabce1cb0d85718e)#define P4 CYHAL\_PORT\_4

[ 79](ifx__cat1-pinctrl_8h.md#a49ce5f7954a95865f12be8083ccb2719)#define P5 CYHAL\_PORT\_5

[ 80](ifx__cat1-pinctrl_8h.md#ab276be36e56dfdd17d860fbc82c3a22d)#define P6 CYHAL\_PORT\_6

[ 81](ifx__cat1-pinctrl_8h.md#a017ae5a42bc27ff7402656a779fec303)#define P7 CYHAL\_PORT\_7

[ 82](ifx__cat1-pinctrl_8h.md#ae04365e5a91d08e332a28f00efe389fe)#define P8 CYHAL\_PORT\_8

[ 83](ifx__cat1-pinctrl_8h.md#a8b201e09e2f1d58d8f3ad3a14c02b86b)#define P9 CYHAL\_PORT\_9

[ 84](ifx__cat1-pinctrl_8h.md#a5bb9f89248afa8d7e5a821fd459b085f)#define P10 CYHAL\_PORT\_10

[ 85](ifx__cat1-pinctrl_8h.md#aca6db006bc37d2b337fca225a79856c8)#define P11 CYHAL\_PORT\_11

[ 86](ifx__cat1-pinctrl_8h.md#a20c70bba8105b63590b5a49d99f563b5)#define P12 CYHAL\_PORT\_12

[ 87](ifx__cat1-pinctrl_8h.md#aa729f895b03c9230ebcf8c798f7bd1bb)#define P13 CYHAL\_PORT\_13

[ 88](ifx__cat1-pinctrl_8h.md#af108487a116bc015d7abd21ee2ab374e)#define P14 CYHAL\_PORT\_14

[ 89](ifx__cat1-pinctrl_8h.md#a3059522b4d1048ecf60259f3805147d6)#define P15 CYHAL\_PORT\_15

[ 90](ifx__cat1-pinctrl_8h.md#a0f8aefca2c1a1d922ca9ecac68caa584)#define P16 CYHAL\_PORT\_16

[ 91](ifx__cat1-pinctrl_8h.md#ac8f5bddb889a3da7918ae32ca6c5cc97)#define P17 CYHAL\_PORT\_17

[ 92](ifx__cat1-pinctrl_8h.md#ae6f383959ce67f3403d4cf1e7aacb1cb)#define P18 CYHAL\_PORT\_18

[ 93](ifx__cat1-pinctrl_8h.md#af04bd18711f898d17e1d28ac27b2064d)#define P19 CYHAL\_PORT\_19

[ 94](ifx__cat1-pinctrl_8h.md#a33f788605a598e63ac41746fa80a2748)#define P20 CYHAL\_PORT\_20

95

96/\* Returns CYHAL GPIO from Board device tree GPIO configuration

97 \* CYHAL\_GET\_GPIO(port\_number, pin\_number),

98 \* port\_number = ((REG ADDR of node) - (REG ADDR of gpio\_prt0)) / (REG SIZE of gpio\_prt0)

99 \* pin\_number = DT\_PHA\_BY\_IDX(node, gpios\_prop, 0, pin)

100 \*/

[ 101](ifx__cat1-pinctrl_8h.md#a19da54df2a9e4e46dd945bdbb56f276c)#define DT\_GET\_CYHAL\_GPIO\_FROM\_DT\_GPIOS(node, gpios\_prop) \

102 CYHAL\_GET\_GPIO( \

103 (DT\_REG\_ADDR\_BY\_IDX(DT\_GPIO\_CTLR\_BY\_IDX(node, gpios\_prop, 0), 0) - \

104 DT\_REG\_ADDR\_BY\_IDX(DT\_NODELABEL(gpio\_prt0), 0)) / \

105 DT\_REG\_ADDR\_BY\_IDX(DT\_NODELABEL(gpio\_prt0), 1), \

106 DT\_PHA\_BY\_IDX(node, gpios\_prop, 0, pin) \

107 )

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [ifx\_cat1-pinctrl.h](ifx__cat1-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
