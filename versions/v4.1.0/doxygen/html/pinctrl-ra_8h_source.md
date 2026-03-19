---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/pinctrl-ra_8h_source.html
original_path: doxygen/html/pinctrl-ra_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-ra.h

[Go to the documentation of this file.](pinctrl-ra_8h.md)

1/\*

2 \* Copyright (c) 2024-2025 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef \_\_ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_RA\_PINCTRL\_H\_\_

8#define \_\_ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_RA\_PINCTRL\_H\_\_

9

[ 10](pinctrl-ra_8h.md#a677d4ff97e792bb9b3369b5f2f17018e)#define RA\_PORT\_NUM\_POS 0

[ 11](pinctrl-ra_8h.md#a0473c603687c04018b96071a0c99d600)#define RA\_PORT\_NUM\_MASK 0xf

12

[ 13](pinctrl-ra_8h.md#a1e51a7480d6f3d77eea8d7dd52b2623c)#define RA\_PIN\_NUM\_POS 4

[ 14](pinctrl-ra_8h.md#a61830f3cee48ee8caa7af15ae5220565)#define RA\_PIN\_NUM\_MASK 0xf

15

[ 16](pinctrl-ra_8h.md#afaed554a358de18c6cc6548f6b25bd76)#define RA\_PSEL\_HIZ\_JTAG\_SWD 0x0

[ 17](pinctrl-ra_8h.md#adc038a51dabd0d6c074d6ed90dc7746e)#define RA\_PSEL\_ADC 0x0

[ 18](pinctrl-ra_8h.md#a5ed7ea99d44dfa9c50099a827827a105)#define RA\_PSEL\_DAC 0x0

[ 19](pinctrl-ra_8h.md#ab93cf559fecab2cd319dde64cb32fb05)#define RA\_PSEL\_AGT 0x1

[ 20](pinctrl-ra_8h.md#a4c29ecef20fa0ad9e2c52e4bed5607c0)#define RA\_PSEL\_GPT0 0x2

[ 21](pinctrl-ra_8h.md#a2c7f41c5813ff56a3434eed762554dc7)#define RA\_PSEL\_GPT1 0x3

[ 22](pinctrl-ra_8h.md#a16cf995560956577ef10fd4396c17c53)#define RA\_PSEL\_SCI\_0 0x4

[ 23](pinctrl-ra_8h.md#afdf9e4b96799435f94e8db4973ca9f5b)#define RA\_PSEL\_SCI\_2 0x4

[ 24](pinctrl-ra_8h.md#acb904b70cfddea59211b81bd2101aed4)#define RA\_PSEL\_SCI\_4 0x4

[ 25](pinctrl-ra_8h.md#a69aee47b66ab1e6a8ebe4c9062145fb4)#define RA\_PSEL\_SCI\_6 0x4

[ 26](pinctrl-ra_8h.md#a1282209663de934b4b523045a1816b68)#define RA\_PSEL\_SCI\_8 0x4

[ 27](pinctrl-ra_8h.md#a858885382f50f3376ce2d1b0125dfc49)#define RA\_PSEL\_SCI\_1 0x5

[ 28](pinctrl-ra_8h.md#a6860ab1d96ecddbe976d8cc292629990)#define RA\_PSEL\_SCI\_3 0x5

[ 29](pinctrl-ra_8h.md#a4b74f4742e6336e571bb731ae0a71961)#define RA\_PSEL\_SCI\_5 0x5

[ 30](pinctrl-ra_8h.md#a55f438cc9fcb43e350152129fedc4fcc)#define RA\_PSEL\_SCI\_7 0x5

[ 31](pinctrl-ra_8h.md#ad72d8611591a97878b493c610019e682)#define RA\_PSEL\_SCI\_9 0x5

[ 32](pinctrl-ra_8h.md#a2f891a502696032fc264a48961078a54)#define RA\_PSEL\_SPI 0x6

[ 33](pinctrl-ra_8h.md#a6905e3e86fa46127217081707d3454e9)#define RA\_PSEL\_I2C 0x7

[ 34](pinctrl-ra_8h.md#a869043eaf8f376149eb9e8b3a09df41e)#define RA\_PSEL\_CLKOUT\_RTC 0x9

[ 35](pinctrl-ra_8h.md#a8aa63c1bf6b5fdca37dec1d66417bec9)#define RA\_PSEL\_CAC\_ADC 0xa

[ 36](pinctrl-ra_8h.md#aa9d9429f973eb499e1bcf99fc4a38085)#define RA\_PSEL\_CAC\_DAC 0xa

[ 37](pinctrl-ra_8h.md#a02d5cce81df69f0cdace1aed46613422)#define RA\_PSEL\_BUS 0xb

[ 38](pinctrl-ra_8h.md#a02cd530e8a72c739351a41967d9b811a)#define RA\_PSEL\_CANFD 0x10

[ 39](pinctrl-ra_8h.md#af34c827566a453f61f7a6aff92bba180)#define RA\_PSEL\_QSPI 0x11

[ 40](pinctrl-ra_8h.md#a047eb43ed2d5734bf59ff55284628737)#define RA\_PSEL\_SSIE 0x12

[ 41](pinctrl-ra_8h.md#a7b4d3662537c785aa5e8ac284c8068b3)#define RA\_PSEL\_USBFS 0x13

[ 42](pinctrl-ra_8h.md#ad95c25a2066430bc076c4bfc63647298)#define RA\_PSEL\_USBHS 0x14

[ 43](pinctrl-ra_8h.md#a985004a21e22a2e1cf63e18f86aa9cbe)#define RA\_PSEL\_SDHI 0x15

[ 44](pinctrl-ra_8h.md#a59d92838618726010e2adcc18807780e)#define RA\_PSEL\_ETH\_MII 0x16

[ 45](pinctrl-ra_8h.md#a0f6039ed42d661f8cfd736cbca79139b)#define RA\_PSEL\_ETH\_RMII 0x17

[ 46](pinctrl-ra_8h.md#ac55a667e4ac45fe9d6b485493507432d)#define RA\_PSEL\_GLCDC 0x19

[ 47](pinctrl-ra_8h.md#afd7fed80f75f05d2e003f554c30f50b8)#define RA\_PSEL\_OSPI 0x1c

48

[ 49](pinctrl-ra_8h.md#adec701d28121ee10eee96c4c4781316f)#define RA\_PSEL\_POS 8

[ 50](pinctrl-ra_8h.md#a9082fcf206510ad3b42d48817a3f6e18)#define RA\_PSEL\_MASK 0x1f

51

[ 52](pinctrl-ra_8h.md#aba5d1993a94006b39534addf1d8e6e1b)#define RA\_MODE\_POS 13

[ 53](pinctrl-ra_8h.md#a02a2c8ef99c23f120890e0a2d82b76af)#define RA\_MODE\_MASK 0x1

54

[ 55](pinctrl-ra_8h.md#a9125cbda50cb1752ced9dfaa948be2e2)#define RA\_PSEL(psel, port\_num, pin\_num) \

56 (1 << RA\_MODE\_POS | psel << RA\_PSEL\_POS | port\_num << RA\_PORT\_NUM\_POS | \

57 pin\_num << RA\_PIN\_NUM\_POS)

58

59#endif /\* \_\_ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_RA\_PINCTRL\_H\_\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas](dir_17f48eb154be6cea623223db5de209e7.md)
- [pinctrl-ra.h](pinctrl-ra_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
