---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/gecko-pinctrl_8h_source.html
original_path: doxygen/html/gecko-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gecko-pinctrl.h

[Go to the documentation of this file.](gecko-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2022 Silicon Labs

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

[ 27](gecko-pinctrl_8h.md#af582c317ab79a3961ea00645514fc3f6)#define GECKO\_FUN\_POS 24U

[ 29](gecko-pinctrl_8h.md#a87d929d0a1bc9808a854ce582a0c8251)#define GECKO\_FUN\_MSK 0xFFU

30

[ 32](gecko-pinctrl_8h.md#af4fc3615fcff891841b6226b363f9f4c)#define GECKO\_PIN\_POS 0U

[ 34](gecko-pinctrl_8h.md#a9e62aad832626ee3f12e55b8e0102b68)#define GECKO\_PIN\_MSK 0xFFU

35

[ 37](gecko-pinctrl_8h.md#aafabc892e5cc1298ff87a10afdd203ca)#define GECKO\_PORT\_POS 8U

[ 39](gecko-pinctrl_8h.md#a750badf0aada694862e9cc8135ef435c)#define GECKO\_PORT\_MSK 0xFFU

40

[ 42](gecko-pinctrl_8h.md#a12208aabccc02edd6c64a857f14455f7)#define GECKO\_LOC\_POS 0U

[ 44](gecko-pinctrl_8h.md#adef6df5f1daf2e87dbed89b433ef7d84)#define GECKO\_LOC\_MSK 0xFFU

45

47

52

[ 54](gecko-pinctrl_8h.md#a2b19bb5a846aab3b44a3628c586df77b)#define GECKO\_FUN\_UART\_TX 0U

[ 56](gecko-pinctrl_8h.md#a68699f16723f6a99594f068dd0c95b2a)#define GECKO\_FUN\_UART\_RX 1U

[ 58](gecko-pinctrl_8h.md#a65f270929aae6f65e659f1f6393d34fa)#define GECKO\_FUN\_UART\_RTS 2U

[ 60](gecko-pinctrl_8h.md#ad4dc9908bb86aea93aaa896ea7755a29)#define GECKO\_FUN\_UART\_CTS 3U

[ 62](gecko-pinctrl_8h.md#a3cf2407ef84050edc079bd0e372b514b)#define GECKO\_FUN\_UART\_LOC 4U

63

[ 64](gecko-pinctrl_8h.md#a469abb3acc66dfe55f73918b8b2bf5ec)#define GECKO\_FUN\_SPI\_MISO 5U

[ 65](gecko-pinctrl_8h.md#ac694f5ec91bde5c9e3de7af7fed94b6b)#define GECKO\_FUN\_SPI\_MOSI 6U

[ 66](gecko-pinctrl_8h.md#a3a5f06615a2add43e56c58a8b497f14b)#define GECKO\_FUN\_SPI\_CSN 7U

[ 67](gecko-pinctrl_8h.md#a71471924b76182052cbad22824d5992e)#define GECKO\_FUN\_SPI\_SCK 8U

68

[ 69](gecko-pinctrl_8h.md#a3c29c6046d30a743df9aaae55c2b0803)#define GECKO\_FUN\_I2C\_SDA 9U

[ 70](gecko-pinctrl_8h.md#a455a393df63ad05434c993ff18b9d3b5)#define GECKO\_FUN\_I2C\_SCL 10U

[ 71](gecko-pinctrl_8h.md#a405973ead4fd3aa22f2d976257929185)#define GECKO\_FUN\_I2C\_SDA\_LOC 11U

[ 72](gecko-pinctrl_8h.md#a3216f884cccdd06204765849deec56b0)#define GECKO\_FUN\_I2C\_SCL\_LOC 12U

73

75

[ 83](gecko-pinctrl_8h.md#ac1af8b10c541907308332856fa9affe7)#define GECKO\_PSEL(fun, port, pin) \

84 (((GECKO\_PORT\_##port & GECKO\_PORT\_MSK) << GECKO\_PORT\_POS) | \

85 ((GECKO\_PIN(##pin##) & GECKO\_PIN\_MSK) << GECKO\_PIN\_POS) | \

86 ((GECKO\_FUN\_##fun & GECKO\_FUN\_MSK) << GECKO\_FUN\_POS))

87

[ 94](gecko-pinctrl_8h.md#a0c4e8fbbb218ce88bd4059bda8170e6d)#define GECKO\_LOC(fun, loc) \

95 (((GECKO\_LOCATION(##loc##) & GECKO\_LOC\_MSK) << GECKO\_LOC\_POS) | \

96 ((GECKO\_FUN\_##fun##\_LOC & GECKO\_FUN\_MSK) << GECKO\_FUN\_POS))

97

98#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_GECKO\_PINCTRL\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [gecko-pinctrl.h](gecko-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
