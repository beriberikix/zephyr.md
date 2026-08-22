---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/arm-mps4-pinctrl_8h_source.html
original_path: doxygen/html/arm-mps4-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm-mps4-pinctrl.h

[Go to the documentation of this file.](arm-mps4-pinctrl_8h.md)

1/\*

2 \* Copyright 2025 Arm Limited and/or its affiliates <open-source-office@arm.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

[ 7](arm-mps4-pinctrl_8h.md#a8afa19b922051b18516de109ef91cfb2)#define MPS4\_ALT\_FUNC\_POS 0

[ 8](arm-mps4-pinctrl_8h.md#a7499c07aa7f241ae37a8600ab3516025)#define MPS4\_ALT\_FUNC\_MASK 0x7

9

[ 10](arm-mps4-pinctrl_8h.md#a1b4bb85578599bcbe2d5abcd82ae5059)#define MPS4\_EXP\_NUM\_POS 3

[ 11](arm-mps4-pinctrl_8h.md#a835b77789dd9e689e35f4fbdf8ae4b0c)#define MPS4\_EXP\_NUM\_MASK 0x1F8

12

[ 13](arm-mps4-pinctrl_8h.md#aacc441eeb486384a97b6d495b7ede5b6)#define MPS4\_PINCTRL\_FUNC\_UART 0

[ 14](arm-mps4-pinctrl_8h.md#abce528e0feff0ea28504196171437878)#define MPS4\_PINCTRL\_FUNC\_GPIO 1

[ 15](arm-mps4-pinctrl_8h.md#acd848d6b9cd67310c7678c9c814d019d)#define MPS4\_PINCTRL\_FUNC\_I2C 2

[ 16](arm-mps4-pinctrl_8h.md#af70280000f1f8d002f0eee7938595220)#define MPS4\_PINCTRL\_FUNC\_SPI 3

17

[ 18](arm-mps4-pinctrl_8h.md#aeea5b5140183c5d992cc3b786d43a9ba)#define MPS4\_PINMUX(alt\_func, exp\_num) (exp\_num << MPS4\_EXP\_NUM\_POS | \

19 alt\_func << MPS4\_ALT\_FUNC\_POS)

20

21/\* GPIO 0 \*/

[ 22](arm-mps4-pinctrl_8h.md#aad1ef19e8c46127baf5ddb680f4a9c2e)#define UART3\_RXD\_EXP MPS4\_PINMUX(MPS4\_PINCTRL\_FUNC\_UART, 0)

[ 23](arm-mps4-pinctrl_8h.md#aab7f8b8584aa06a033aa1e93200eb0d6)#define UART3\_TXD\_EXP MPS4\_PINMUX(MPS4\_PINCTRL\_FUNC\_UART, 1)

[ 24](arm-mps4-pinctrl_8h.md#ae1f9ab03b508c087a9190d742b67fc2a)#define SPI3\_SS\_EXP MPS4\_PINMUX(MPS4\_PINCTRL\_FUNC\_SPI, 10)

[ 25](arm-mps4-pinctrl_8h.md#a95f2fe6603f5ab5de9c410dfaf87dc52)#define SPI3\_MOSI\_EXP MPS4\_PINMUX(MPS4\_PINCTRL\_FUNC\_SPI, 11)

[ 26](arm-mps4-pinctrl_8h.md#a14c932b34877e7b1f004bdf3edfdcd4b)#define SPI3\_MISO\_EXP MPS4\_PINMUX(MPS4\_PINCTRL\_FUNC\_SPI, 12)

[ 27](arm-mps4-pinctrl_8h.md#ac3801e4481859951369757ac96612165)#define SPI3\_SCK\_EXP MPS4\_PINMUX(MPS4\_PINCTRL\_FUNC\_SPI, 13)

[ 28](arm-mps4-pinctrl_8h.md#a8c2f848c26c691ce333e05fe17c9341d)#define SBCON2\_SDA\_EXP MPS4\_PINMUX(MPS4\_PINCTRL\_FUNC\_I2C, 14)

[ 29](arm-mps4-pinctrl_8h.md#a301bb93777a77d4fcbed8617edbe319a)#define SBCON2\_SCL\_EXP MPS4\_PINMUX(MPS4\_PINCTRL\_FUNC\_I2C, 15)

30

31

32/\* GPIO 1 \*/

[ 33](arm-mps4-pinctrl_8h.md#a960b6b4bf5810595c274fab5842189e4)#define UART4\_RXD\_EXP MPS4\_PINMUX(MPS4\_PINCTRL\_FUNC\_UART, 16)

[ 34](arm-mps4-pinctrl_8h.md#a8f2f8e4cb191c641dad8dff6c4753e38)#define UART4\_TXD\_EXP MPS4\_PINMUX(MPS4\_PINCTRL\_FUNC\_UART, 17)

[ 35](arm-mps4-pinctrl_8h.md#a525321e1403275e09014f3ff1fa88d78)#define SPI4\_SS\_EXP MPS4\_PINMUX(MPS4\_PINCTRL\_FUNC\_SPI, 26)

[ 36](arm-mps4-pinctrl_8h.md#aa73c8c56e661787cc05b131f86a8478c)#define SPI4\_MOSI\_EXP MPS4\_PINMUX(MPS4\_PINCTRL\_FUNC\_SPI, 27)

[ 37](arm-mps4-pinctrl_8h.md#a9709eee41e54142558c4930f1b034043)#define SPI4\_MISO\_EXP MPS4\_PINMUX(MPS4\_PINCTRL\_FUNC\_SPI, 28)

[ 38](arm-mps4-pinctrl_8h.md#aa48a51e34a517797511e7214ad00b7de)#define SPI4\_SCK\_EXP MPS4\_PINMUX(MPS4\_PINCTRL\_FUNC\_SPI, 29)

[ 39](arm-mps4-pinctrl_8h.md#a1f600b98990e17441e52f65cc0dabddb)#define SBCON3\_SDA\_EXP MPS4\_PINMUX(MPS4\_PINCTRL\_FUNC\_I2C, 30)

[ 40](arm-mps4-pinctrl_8h.md#a42708eb48f46a3dd04242b446389057b)#define SBCON3\_SCL\_EXP MPS4\_PINMUX(MPS4\_PINCTRL\_FUNC\_I2C, 31)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [arm-mps4-pinctrl.h](arm-mps4-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
