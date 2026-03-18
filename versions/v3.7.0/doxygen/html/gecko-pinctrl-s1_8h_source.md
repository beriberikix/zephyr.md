---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/gecko-pinctrl-s1_8h_source.html
original_path: doxygen/html/gecko-pinctrl-s1_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gecko-pinctrl-s1.h

[Go to the documentation of this file.](gecko-pinctrl-s1_8h.md)

1/\*

2 \* Copyright (c) 2023 Silicon Labs

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_GECKO\_PINCTRL\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_GECKO\_PINCTRL\_H\_

8

9/\*

10 \* The whole GECKO\_pin configuration information is encoded in a 32-bit bitfield

11 \* organized as follows:

12 \*

13 \* - 31..24: Pin function.

14 \* - 23..16: Reserved.

15 \* - 15..8: Port for UART\_RX/UART\_TX functions.

16 \* - 7..0: Pin number for UART\_RX/UART\_TX functions.

17 \* - 15..8: Reserved for UART\_LOC function.

18 \* - 7..0: Loc for UART\_LOC function.

19 \*/

20

25

[ 27](gecko-pinctrl-s1_8h.md#af582c317ab79a3961ea00645514fc3f6)#define GECKO\_FUN\_POS 24U

[ 29](gecko-pinctrl-s1_8h.md#a87d929d0a1bc9808a854ce582a0c8251)#define GECKO\_FUN\_MSK 0xFFU

30

[ 32](gecko-pinctrl-s1_8h.md#af4fc3615fcff891841b6226b363f9f4c)#define GECKO\_PIN\_POS 0U

[ 34](gecko-pinctrl-s1_8h.md#a9e62aad832626ee3f12e55b8e0102b68)#define GECKO\_PIN\_MSK 0xFFU

35

[ 37](gecko-pinctrl-s1_8h.md#aafabc892e5cc1298ff87a10afdd203ca)#define GECKO\_PORT\_POS 8U

[ 39](gecko-pinctrl-s1_8h.md#a750badf0aada694862e9cc8135ef435c)#define GECKO\_PORT\_MSK 0xFFU

40

[ 42](gecko-pinctrl-s1_8h.md#a12208aabccc02edd6c64a857f14455f7)#define GECKO\_LOC\_POS 0U

[ 44](gecko-pinctrl-s1_8h.md#adef6df5f1daf2e87dbed89b433ef7d84)#define GECKO\_LOC\_MSK 0xFFU

45

47

52

[ 54](gecko-pinctrl-s1_8h.md#a2b19bb5a846aab3b44a3628c586df77b)#define GECKO\_FUN\_UART\_TX 0U

[ 56](gecko-pinctrl-s1_8h.md#a68699f16723f6a99594f068dd0c95b2a)#define GECKO\_FUN\_UART\_RX 1U

[ 58](gecko-pinctrl-s1_8h.md#a65f270929aae6f65e659f1f6393d34fa)#define GECKO\_FUN\_UART\_RTS 2U

[ 60](gecko-pinctrl-s1_8h.md#ad4dc9908bb86aea93aaa896ea7755a29)#define GECKO\_FUN\_UART\_CTS 3U

[ 62](gecko-pinctrl-s1_8h.md#ac7e6a762e1e7e63f9172d736354820b3)#define GECKO\_FUN\_UART\_RX\_LOC 4U

[ 64](gecko-pinctrl-s1_8h.md#a59225761dc92d12b23be60f2616c0f9f)#define GECKO\_FUN\_UART\_TX\_LOC 5U

[ 66](gecko-pinctrl-s1_8h.md#a8edacb8e79f7d7a84736104949157870)#define GECKO\_FUN\_UART\_RTS\_LOC 6U

[ 68](gecko-pinctrl-s1_8h.md#a3ef104d8e946ef746ba9e71bb5c469f5)#define GECKO\_FUN\_UART\_CTS\_LOC 7U

69

[ 70](gecko-pinctrl-s1_8h.md#ad356cf8a63077cd810a13c32d7591e47)#define GECKO\_FUN\_SPIM\_MISO 8U

[ 71](gecko-pinctrl-s1_8h.md#a2a24765e466f1264e300d4975429c67c)#define GECKO\_FUN\_SPIM\_MOSI 9U

[ 72](gecko-pinctrl-s1_8h.md#a570a5464219faf2252412f09f6281646)#define GECKO\_FUN\_SPIM\_CS 10U

[ 73](gecko-pinctrl-s1_8h.md#ab77e588c302f3d18d18b72efa943e0db)#define GECKO\_FUN\_SPIM\_SCK 11U

74

[ 75](gecko-pinctrl-s1_8h.md#a1a9fef5c16e0ab5f2987b4f9ffdc6d22)#define GECKO\_FUN\_LEUART\_RX\_LOC 12U

[ 76](gecko-pinctrl-s1_8h.md#a49bd14236c6fb7efb44418c05f1a91da)#define GECKO\_FUN\_LEUART\_TX\_LOC 13U

77

[ 78](gecko-pinctrl-s1_8h.md#a61eedadfb95bdd6fe6e183e9c22fb7ed)#define GECKO\_FUN\_SPIS\_MISO 14U

[ 79](gecko-pinctrl-s1_8h.md#a8958587b66b8cd4942b4c9ce9826f689)#define GECKO\_FUN\_SPIS\_MOSI 15U

[ 80](gecko-pinctrl-s1_8h.md#af67b9548ffaecb030464cd5f52b16285)#define GECKO\_FUN\_SPIS\_CS 16U

[ 81](gecko-pinctrl-s1_8h.md#ae77d65d5717e27242322424179de1cbe)#define GECKO\_FUN\_SPIS\_SCK 17U

82

[ 83](gecko-pinctrl-s1_8h.md#afb0d7445bbbba745b9cc08cb5aa01f44)#define GECKO\_FUN\_SPI\_MISO\_LOC 18U

[ 84](gecko-pinctrl-s1_8h.md#a518ae94f50c55f1a19ff70d898bacf34)#define GECKO\_FUN\_SPI\_MOSI\_LOC 19U

[ 85](gecko-pinctrl-s1_8h.md#ad6df2bcea0c8e0e68107d70eab753f5f)#define GECKO\_FUN\_SPI\_CS\_LOC 20U

[ 86](gecko-pinctrl-s1_8h.md#a73dea09e9111d11f41fd52ee9a296570)#define GECKO\_FUN\_SPI\_SCK\_LOC 21U

87

[ 88](gecko-pinctrl-s1_8h.md#a3c29c6046d30a743df9aaae55c2b0803)#define GECKO\_FUN\_I2C\_SDA 22U

[ 89](gecko-pinctrl-s1_8h.md#a455a393df63ad05434c993ff18b9d3b5)#define GECKO\_FUN\_I2C\_SCL 23U

[ 90](gecko-pinctrl-s1_8h.md#a405973ead4fd3aa22f2d976257929185)#define GECKO\_FUN\_I2C\_SDA\_LOC 24U

[ 91](gecko-pinctrl-s1_8h.md#a3216f884cccdd06204765849deec56b0)#define GECKO\_FUN\_I2C\_SCL\_LOC 25U

92

93

95

[ 103](gecko-pinctrl-s1_8h.md#ac1af8b10c541907308332856fa9affe7)#define GECKO\_PSEL(fun, port, pin) \

104 (((GECKO\_PORT\_##port & GECKO\_PORT\_MSK) << GECKO\_PORT\_POS) | \

105 ((GECKO\_PIN(##pin##) & GECKO\_PIN\_MSK) << GECKO\_PIN\_POS) | \

106 ((GECKO\_FUN\_##fun & GECKO\_FUN\_MSK) << GECKO\_FUN\_POS))

107

[ 114](gecko-pinctrl-s1_8h.md#a0c4e8fbbb218ce88bd4059bda8170e6d)#define GECKO\_LOC(fun, loc) \

115 (((GECKO\_LOCATION(##loc##) & GECKO\_LOC\_MSK) << GECKO\_LOC\_POS) | \

116 ((GECKO\_FUN\_##fun##\_LOC & GECKO\_FUN\_MSK) << GECKO\_FUN\_POS))

117

118#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_GECKO\_PINCTRL\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [gecko-pinctrl-s1.h](gecko-pinctrl-s1_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
