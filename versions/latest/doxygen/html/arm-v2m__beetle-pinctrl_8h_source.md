---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/arm-v2m__beetle-pinctrl_8h_source.html
original_path: doxygen/html/arm-v2m__beetle-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm-v2m\_beetle-pinctrl.h

[Go to the documentation of this file.](arm-v2m__beetle-pinctrl_8h.md)

1/\*

2 \* Copyright 2025 Arm Limited and/or its affiliates <open-source-office@arm.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

[ 7](arm-v2m__beetle-pinctrl_8h.md#a4d45c8721029feeca3d1959350be7cdb)#define V2M\_BEETLE\_ALT\_FUNC\_POS 0

[ 8](arm-v2m__beetle-pinctrl_8h.md#a3519227256ace189f093cc0fd02d6d9b)#define V2M\_BEETLE\_ALT\_FUNC\_MASK 0x7

9

[ 10](arm-v2m__beetle-pinctrl_8h.md#a00493ab00f529a1434e963a5e23c2254)#define V2M\_BEETLE\_EXP\_NUM\_POS 3

[ 11](arm-v2m__beetle-pinctrl_8h.md#ac813f27b4634c45f01b6cdbf8b02a32d)#define V2M\_BEETLE\_EXP\_NUM\_MASK 0x1F8

12

[ 13](arm-v2m__beetle-pinctrl_8h.md#a5327a4bbbcbc2476488a0cd0f3c13070)#define V2M\_BEETLE\_PINCTRL\_FUNC\_UART 0

[ 14](arm-v2m__beetle-pinctrl_8h.md#a2a2d0a5be6132e815212772d900eecb8)#define V2M\_BEETLE\_PINCTRL\_FUNC\_GPIO 1

[ 15](arm-v2m__beetle-pinctrl_8h.md#a5114f026181617cf4a9f6f4a8dd714d0)#define V2M\_BEETLE\_PINCTRL\_FUNC\_I2C 2

[ 16](arm-v2m__beetle-pinctrl_8h.md#a57a16dc76ecc4a21ab4fc765bff9c829)#define V2M\_BEETLE\_PINCTRL\_FUNC\_SPI 3

[ 17](arm-v2m__beetle-pinctrl_8h.md#ac40b2ed7fcb2585dd2735705db9871bf)#define V2M\_BEETLE\_PINCTRL\_FUNC\_QSPI 4

18

[ 19](arm-v2m__beetle-pinctrl_8h.md#ab203c77381bb94d20180804cc0cde072)#define V2M\_BEETLE\_PINMUX(alt\_func, exp\_num) (exp\_num << V2M\_BEETLE\_EXP\_NUM\_POS | \

20 alt\_func << V2M\_BEETLE\_ALT\_FUNC\_POS)

21

22

23

24/\* GPIO 0 \*/

[ 25](arm-v2m__beetle-pinctrl_8h.md#a0dad432d22c364a59b07d3743e503603)#define UART0\_RXD\_EXP V2M\_BEETLE\_PINMUX(V2M\_BEETLE\_PINCTRL\_FUNC\_UART, 0)

[ 26](arm-v2m__beetle-pinctrl_8h.md#ab987c26da052b07e7db9b1954209616d)#define UART0\_TXD\_EXP V2M\_BEETLE\_PINMUX(V2M\_BEETLE\_PINCTRL\_FUNC\_UART, 1)

[ 27](arm-v2m__beetle-pinctrl_8h.md#af0727866d5c48f3b1cd2c9383929b1a1)#define SPI0\_SS\_EXP V2M\_BEETLE\_PINMUX(V2M\_BEETLE\_PINCTRL\_FUNC\_SPI, 10)

[ 28](arm-v2m__beetle-pinctrl_8h.md#a02ab28fc35a282d7b7839707fd0afed8)#define SPI0\_MOSI\_EXP V2M\_BEETLE\_PINMUX(V2M\_BEETLE\_PINCTRL\_FUNC\_SPI, 11)

[ 29](arm-v2m__beetle-pinctrl_8h.md#ac6071179ce140b6174432836b52bc6d0)#define SPI0\_MISO\_EXP V2M\_BEETLE\_PINMUX(V2M\_BEETLE\_PINCTRL\_FUNC\_SPI, 12)

[ 30](arm-v2m__beetle-pinctrl_8h.md#a9956a46d931b038e35d49ea8fbef264f)#define SPI0\_SCK\_EXP V2M\_BEETLE\_PINMUX(V2M\_BEETLE\_PINCTRL\_FUNC\_SPI, 13)

[ 31](arm-v2m__beetle-pinctrl_8h.md#aca1f71982f2db9090ba8bc263c3715c2)#define SBCON0\_SDA\_EXP V2M\_BEETLE\_PINMUX(V2M\_BEETLE\_PINCTRL\_FUNC\_I2C, 14)

[ 32](arm-v2m__beetle-pinctrl_8h.md#a8b5d683cf0d16eb4a93b60edb0d72db8)#define SBCON0\_SCL\_EXP V2M\_BEETLE\_PINMUX(V2M\_BEETLE\_PINCTRL\_FUNC\_I2C, 15)

33

34/\* GPIO 1 \*/

[ 35](arm-v2m__beetle-pinctrl_8h.md#a554686dd42decffbdbe18b3c5f47977a)#define UART1\_RXD\_EXP V2M\_BEETLE\_PINMUX(V2M\_BEETLE\_PINCTRL\_FUNC\_UART, 16)

[ 36](arm-v2m__beetle-pinctrl_8h.md#aec12e8c4da51b0ae607b339d26815347)#define UART1\_TXD\_EXP V2M\_BEETLE\_PINMUX(V2M\_BEETLE\_PINCTRL\_FUNC\_UART, 17)

[ 37](arm-v2m__beetle-pinctrl_8h.md#a17f827e6dcc9ae2463d6bcd94f8ba037)#define SPI1\_SS\_EXP V2M\_BEETLE\_PINMUX(V2M\_BEETLE\_PINCTRL\_FUNC\_SPI, 18)

[ 38](arm-v2m__beetle-pinctrl_8h.md#a8f68d50b9c3f09f0ffe77a987823f93e)#define SPI1\_MOSI\_EXP V2M\_BEETLE\_PINMUX(V2M\_BEETLE\_PINCTRL\_FUNC\_SPI, 19)

[ 39](arm-v2m__beetle-pinctrl_8h.md#a8157da231573f62c43ffcebbcedd05da)#define SPI1\_MISO\_EXP V2M\_BEETLE\_PINMUX(V2M\_BEETLE\_PINCTRL\_FUNC\_SPI, 20)

[ 40](arm-v2m__beetle-pinctrl_8h.md#a084304a2cf66e2fe433da0608f42e5ab)#define SPI1\_SCK\_EXP V2M\_BEETLE\_PINMUX(V2M\_BEETLE\_PINCTRL\_FUNC\_SPI, 21)

[ 41](arm-v2m__beetle-pinctrl_8h.md#a2c977cc24d8b14abab79d0f448bc7b44)#define SBCON1\_SDA\_EXP V2M\_BEETLE\_PINMUX(V2M\_BEETLE\_PINCTRL\_FUNC\_I2C, 22)

[ 42](arm-v2m__beetle-pinctrl_8h.md#a8b9dd6b30421420c05d12acc0914dfd8)#define SBCON1\_SCL\_EXP V2M\_BEETLE\_PINMUX(V2M\_BEETLE\_PINCTRL\_FUNC\_I2C, 23)

[ 43](arm-v2m__beetle-pinctrl_8h.md#af510dd775ec30cc3ceb8c68c47fe4b22)#define QSPI\_CS2\_EXP V2M\_BEETLE\_PINMUX(V2M\_BEETLE\_PINCTRL\_FUNC\_QSPI, 24)

[ 44](arm-v2m__beetle-pinctrl_8h.md#a4ea213a977a5cb15e946fe6fbc7ba09a)#define QSPI\_CS1\_EXP V2M\_BEETLE\_PINMUX(V2M\_BEETLE\_PINCTRL\_FUNC\_QSPI, 25)

[ 45](arm-v2m__beetle-pinctrl_8h.md#a012803411d173f382177b751d3f8026f)#define QSPI\_IOF0\_EXP V2M\_BEETLE\_PINMUX(V2M\_BEETLE\_PINCTRL\_FUNC\_QSPI, 26)

[ 46](arm-v2m__beetle-pinctrl_8h.md#af238b53e6959f12a79aeac8eb3a65b44)#define QSPI\_IOF1\_EXP V2M\_BEETLE\_PINMUX(V2M\_BEETLE\_PINCTRL\_FUNC\_QSPI, 27)

[ 47](arm-v2m__beetle-pinctrl_8h.md#aab4ad8f508a988e4bced0f54de8f78cd)#define QSPI\_IOF2\_EXP V2M\_BEETLE\_PINMUX(V2M\_BEETLE\_PINCTRL\_FUNC\_QSPI, 28)

[ 48](arm-v2m__beetle-pinctrl_8h.md#a50ec2d09cffaee393178776d1e71fc03)#define QSPI\_IOF3\_EXP V2M\_BEETLE\_PINMUX(V2M\_BEETLE\_PINCTRL\_FUNC\_QSPI, 29)

[ 49](arm-v2m__beetle-pinctrl_8h.md#acf11fd281d37f262aabec2842292a40d)#define QSPI\_SCK\_EXP V2M\_BEETLE\_PINMUX(V2M\_BEETLE\_PINCTRL\_FUNC\_QSPI, 30)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [arm-v2m\_beetle-pinctrl.h](arm-v2m__beetle-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
