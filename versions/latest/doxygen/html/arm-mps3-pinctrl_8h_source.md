---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/arm-mps3-pinctrl_8h_source.html
original_path: doxygen/html/arm-mps3-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm-mps3-pinctrl.h

[Go to the documentation of this file.](arm-mps3-pinctrl_8h.md)

1/\*

2 \* Copyright 2025 Arm Limited and/or its affiliates <open-source-office@arm.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

[ 7](arm-mps3-pinctrl_8h.md#a92d23b008eed86044d67552ec703f2ab)#define MPS3\_ALT\_FUNC\_POS 0

[ 8](arm-mps3-pinctrl_8h.md#af29520fbd24c4ed2559ff1dcefa9c901)#define MPS3\_ALT\_FUNC\_MASK 0x7

9

[ 10](arm-mps3-pinctrl_8h.md#a271fc39e2ac01cf6973857666445b92a)#define MPS3\_EXP\_NUM\_POS 3

[ 11](arm-mps3-pinctrl_8h.md#a38ff399b3140635abe0858e73ad02b5a)#define MPS3\_EXP\_NUM\_MASK 0x1F8

12

[ 13](arm-mps3-pinctrl_8h.md#a67c22b434c59a2eee7c6b60e2b70ae59)#define MPS3\_PINCTRL\_FUNC\_UART 0

[ 14](arm-mps3-pinctrl_8h.md#a89a852a0ee4d66c8031b09f6db24331a)#define MPS3\_PINCTRL\_FUNC\_GPIO 1

[ 15](arm-mps3-pinctrl_8h.md#a23b4c2379a045e9c16bd53d4c5226252)#define MPS3\_PINCTRL\_FUNC\_I2C 2

[ 16](arm-mps3-pinctrl_8h.md#a9a5e1735229d515e14606ba2c5347195)#define MPS3\_PINCTRL\_FUNC\_SPI 3

[ 17](arm-mps3-pinctrl_8h.md#a7ba2947efe4589c519c8a4531def43a9)#define MPS3\_PINCTRL\_FUNC\_PMOD 4

18

[ 19](arm-mps3-pinctrl_8h.md#ad10638589bc1eaa0bc10ef0529cb816c)#define MPS3\_PINMUX(alt\_func, exp\_num) (exp\_num << MPS3\_EXP\_NUM\_POS | \

20 alt\_func << MPS3\_ALT\_FUNC\_POS)

21

22/\* GPIO 0 \*/

[ 23](arm-mps3-pinctrl_8h.md#a34c7b3c59e141cc0dbae7e0edc2ad129)#define PMOD1\_IO1\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_PMOD, 0)

[ 24](arm-mps3-pinctrl_8h.md#a4424b55dd5454cd7fa120a23cd5df6f4)#define PMOD1\_IO0\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_PMOD, 1)

[ 25](arm-mps3-pinctrl_8h.md#a02b3cca65f1c7756a3ffe36b7987222b)#define PMOD1\_SS\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_PMOD, 3)

[ 26](arm-mps3-pinctrl_8h.md#a0695f557cb8f855300365e2be11bc9bb)#define PMOD0\_IO2\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_PMOD, 7)

[ 27](arm-mps3-pinctrl_8h.md#a585aef742cc326eee64903f1fcef6883)#define PMOD0\_IO3\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_PMOD, 8)

[ 28](arm-mps3-pinctrl_8h.md#a91e253309b1e5b615c204836c13900da)#define PMOD1\_SCK\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_PMOD, 9)

[ 29](arm-mps3-pinctrl_8h.md#a4b78ddad746105930ae289c4afd4d4ca)#define PMOD0\_SS\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_PMOD, 10)

[ 30](arm-mps3-pinctrl_8h.md#a1957ed3aa96ccfb786632620782c0f49)#define PMOD0\_IO0\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_PMOD, 11)

[ 31](arm-mps3-pinctrl_8h.md#a4284a74f7ee7d951f316a5fa721f5b4c)#define PMOD0\_IO1\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_PMOD, 12)

[ 32](arm-mps3-pinctrl_8h.md#a9115e37a39f5044fe5a31dff174fc773)#define PMOD0\_SCK\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_PMOD, 13)

[ 33](arm-mps3-pinctrl_8h.md#a8056404e55f29ba58bbd4ea106bccbe0)#define PMOD1\_IO3\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_PMOD, 14)

[ 34](arm-mps3-pinctrl_8h.md#a882a514f7c45b8969b030d3e715fd6ab)#define PMOD1\_IO2\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_PMOD, 15)

35

[ 36](arm-mps3-pinctrl_8h.md#aad1ef19e8c46127baf5ddb680f4a9c2e)#define UART3\_RXD\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_UART, 0)

[ 37](arm-mps3-pinctrl_8h.md#aab7f8b8584aa06a033aa1e93200eb0d6)#define UART3\_TXD\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_UART, 1)

[ 38](arm-mps3-pinctrl_8h.md#ae1f9ab03b508c087a9190d742b67fc2a)#define SPI3\_SS\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_SPI, 10)

[ 39](arm-mps3-pinctrl_8h.md#a95f2fe6603f5ab5de9c410dfaf87dc52)#define SPI3\_MOSI\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_SPI, 11)

[ 40](arm-mps3-pinctrl_8h.md#a14c932b34877e7b1f004bdf3edfdcd4b)#define SPI3\_MISO\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_SPI, 12)

[ 41](arm-mps3-pinctrl_8h.md#ac3801e4481859951369757ac96612165)#define SPI3\_SCK\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_SPI, 13)

[ 42](arm-mps3-pinctrl_8h.md#a8c2f848c26c691ce333e05fe17c9341d)#define SBCON2\_SDA\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_I2C, 14)

[ 43](arm-mps3-pinctrl_8h.md#a301bb93777a77d4fcbed8617edbe319a)#define SBCON2\_SCL\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_I2C, 15)

44

45

46/\* GPIO 1 \*/

[ 47](arm-mps3-pinctrl_8h.md#a960b6b4bf5810595c274fab5842189e4)#define UART4\_RXD\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_UART, 16)

[ 48](arm-mps3-pinctrl_8h.md#a8f2f8e4cb191c641dad8dff6c4753e38)#define UART4\_TXD\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_UART, 17)

[ 49](arm-mps3-pinctrl_8h.md#a525321e1403275e09014f3ff1fa88d78)#define SPI4\_SS\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_SPI, 26)

[ 50](arm-mps3-pinctrl_8h.md#aa73c8c56e661787cc05b131f86a8478c)#define SPI4\_MOSI\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_SPI, 27)

[ 51](arm-mps3-pinctrl_8h.md#a9709eee41e54142558c4930f1b034043)#define SPI4\_MISO\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_SPI, 28)

[ 52](arm-mps3-pinctrl_8h.md#aa48a51e34a517797511e7214ad00b7de)#define SPI4\_SCK\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_SPI, 29)

[ 53](arm-mps3-pinctrl_8h.md#a1f600b98990e17441e52f65cc0dabddb)#define SBCON3\_SDA\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_I2C, 30)

[ 54](arm-mps3-pinctrl_8h.md#a42708eb48f46a3dd04242b446389057b)#define SBCON3\_SCL\_EXP MPS3\_PINMUX(MPS3\_PINCTRL\_FUNC\_I2C, 31)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [arm-mps3-pinctrl.h](arm-mps3-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
