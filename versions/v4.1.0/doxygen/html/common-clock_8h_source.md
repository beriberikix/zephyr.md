---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/common-clock_8h_source.html
original_path: doxygen/html/common-clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

common-clock.h

[Go to the documentation of this file.](common-clock_8h.md)

1/\*

2 \* Copyright (c) 2024 Silicon Laboratories Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_SILABS\_COMMON\_CLOCK\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_SILABS\_COMMON\_CLOCK\_H\_

9

10/\*

11 \* DT macros for clock branches.

12 \* Must stay in sync with the enum sl\_clock\_branch\_t in the Silicon Labs HAL to be

13 \* interpreted correctly by the clock control driver.

14 \*/

[ 15](common-clock_8h.md#a9ae4718ce3eed8108bb86222d50e2098)#define CLOCK\_BRANCH\_SYSCLK 0

[ 16](common-clock_8h.md#a91972b1f1c8092580abbe30cfde99b2e)#define CLOCK\_BRANCH\_HCLK 1

[ 17](common-clock_8h.md#a84dc580deecd214156bb9d7b3d3c6b00)#define CLOCK\_BRANCH\_HCLKRADIO 2

[ 18](common-clock_8h.md#a8ae9a78ca89559a0c043cfbf7f4f0149)#define CLOCK\_BRANCH\_PCLK 3

[ 19](common-clock_8h.md#af47e31e42bff380a450374b997c9a62b)#define CLOCK\_BRANCH\_LSPCLK 4

[ 20](common-clock_8h.md#add6f564d9a54107b60f23e96650884bc)#define CLOCK\_BRANCH\_TRACECLK 5

[ 21](common-clock_8h.md#af76f7e0cd93d94fde5358ab2e8862e71)#define CLOCK\_BRANCH\_ADCCLK 6

[ 22](common-clock_8h.md#ac9b7d1af2508b712c3757745601d74d1)#define CLOCK\_BRANCH\_EXPORTCLK 7

[ 23](common-clock_8h.md#a2288b081fb7811e461618a698cf2d68f)#define CLOCK\_BRANCH\_EM01GRPACLK 8

[ 24](common-clock_8h.md#abbd5d61291505f2c78bc44ae3eadb5cb)#define CLOCK\_BRANCH\_EM01GRPBCLK 9

[ 25](common-clock_8h.md#a2f919498355d8112cfb0e20277863fca)#define CLOCK\_BRANCH\_EM01GRPCCLK 10

[ 26](common-clock_8h.md#a1999b720415f08a0115d61f2b081ca8f)#define CLOCK\_BRANCH\_EM01GRPDCLK 11

[ 27](common-clock_8h.md#a69896c1bf0709d5b4f46d95645718076)#define CLOCK\_BRANCH\_EM23GRPACLK 12

[ 28](common-clock_8h.md#a791b0697adeddf7b424ffa2c31ebc794)#define CLOCK\_BRANCH\_EM4GRPACLK 13

[ 29](common-clock_8h.md#a2543cbe70d32186c539795fc7e3fb01a)#define CLOCK\_BRANCH\_QSPISYSCLK 14

[ 30](common-clock_8h.md#aca2c7930c6f9f22d82a84d0d6b59fc02)#define CLOCK\_BRANCH\_IADCCLK 15

[ 31](common-clock_8h.md#a4ce1e4380d4f10200e8955fe1c4e0ec3)#define CLOCK\_BRANCH\_WDOG0CLK 16

[ 32](common-clock_8h.md#ae39802322698451abf5a6531157c7adc)#define CLOCK\_BRANCH\_WDOG1CLK 17

[ 33](common-clock_8h.md#ab378f4ac4c47c3972d7ad21419fb569f)#define CLOCK\_BRANCH\_RTCCCLK 18

[ 34](common-clock_8h.md#afbf91ecb5f4d8d2ece258c4a28e012ed)#define CLOCK\_BRANCH\_SYSRTCCLK 19

[ 35](common-clock_8h.md#a17be2555fd6316645f596c4f8715d105)#define CLOCK\_BRANCH\_EUART0CLK 20

[ 36](common-clock_8h.md#a9c788fabfbf9ca14c2e6a4d7e21f69df)#define CLOCK\_BRANCH\_EUSART0CLK 21

[ 37](common-clock_8h.md#a5d16954e4cae59bba0411fcf4004c166)#define CLOCK\_BRANCH\_DPLLREFCLK 22

[ 38](common-clock_8h.md#afc4afa41743b9e8bd65f657469570cbf)#define CLOCK\_BRANCH\_I2C0CLK 23

[ 39](common-clock_8h.md#a62c66b574633b7862d455ca92ecb7ca6)#define CLOCK\_BRANCH\_LCDCLK 24

[ 40](common-clock_8h.md#ad9fc418b7b97d9691aa2dbed560c9d2d)#define CLOCK\_BRANCH\_PIXELRZCLK 25

[ 41](common-clock_8h.md#afd28e8ca37027ae7211200072dedafcf)#define CLOCK\_BRANCH\_PCNT0CLK 26

[ 42](common-clock_8h.md#a28e66400d1616baa0afdd25d54283a2d)#define CLOCK\_BRANCH\_PRORTCCLK 27

[ 43](common-clock_8h.md#a4be96634ea45a011a014480c9085df51)#define CLOCK\_BRANCH\_SYSTICKCLK 28

[ 44](common-clock_8h.md#aa6229452489aaa2281b1627ef3a5a78c)#define CLOCK\_BRANCH\_LESENSEHFCLK 29

[ 45](common-clock_8h.md#a52cade1ae02584fb7d7d9cdc8dae0ac8)#define CLOCK\_BRANCH\_VDAC0CLK 30

[ 46](common-clock_8h.md#aebe06aa36e0952f79e76518ce8a29336)#define CLOCK\_BRANCH\_VDAC1CLK 31

[ 47](common-clock_8h.md#a60632170b51f5f443acf34fc76c9dea2)#define CLOCK\_BRANCH\_USB0CLK 32

[ 48](common-clock_8h.md#a274ca09dab6568f7142a2734ecdad428)#define CLOCK\_BRANCH\_FLPLLREFCLK 33

[ 49](common-clock_8h.md#a60be0eac710342c0175d620897b5a259)#define CLOCK\_BRANCH\_INVALID 34

50

[ 51](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503)#define CLOCK\_BIT\_MASK 0x03FUL

[ 52](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256)#define CLOCK\_REG\_MASK 0x1C0UL

53

54#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_SILABS\_COMMON\_CLOCK\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [silabs](dir_9d9a53d793dad9345737df2b8d108293.md)
- [common-clock.h](common-clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
