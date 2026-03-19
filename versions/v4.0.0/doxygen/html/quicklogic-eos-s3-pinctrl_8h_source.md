---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/quicklogic-eos-s3-pinctrl_8h_source.html
original_path: doxygen/html/quicklogic-eos-s3-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

quicklogic-eos-s3-pinctrl.h

[Go to the documentation of this file.](quicklogic-eos-s3-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2023 Antmicro <www.antmicro.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_QUICKLOGIC\_EOS\_S3\_PINCTRL\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_QUICKLOGIC\_EOS\_S3\_PINCTRL\_H\_

9

10#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

11

[ 12](quicklogic-eos-s3-pinctrl_8h.md#a42e8d57fbc0ce7fea27c8e5487008c38)#define IO\_MUX\_REG\_MAX\_OFFSET 107

[ 13](quicklogic-eos-s3-pinctrl_8h.md#ab345030af28df16546437382d1c935a9)#define IO\_MUX\_MAX\_PAD\_NR 45

14

[ 15](quicklogic-eos-s3-pinctrl_8h.md#a76393e634c1e77ca47d7106c27889936)#define FUNC\_SEL\_UART\_RX (77 << 13)

16

[ 17](quicklogic-eos-s3-pinctrl_8h.md#a32684ea1b082834fcadc1d17ab2f6ea7)#define QUICKLOGIC\_EOS\_S3\_PINMUX(pin, fun) (pin) (fun)

18

[ 19](quicklogic-eos-s3-pinctrl_8h.md#ac3cce2e16d9678b674a6b73e9675cb56)#define UART\_TX\_PAD44 QUICKLOGIC\_EOS\_S3\_PINMUX(44, 0x3)

[ 20](quicklogic-eos-s3-pinctrl_8h.md#a4c89eee6f06d8e99b1d042b385622cae)#define UART\_RX\_PAD45 QUICKLOGIC\_EOS\_S3\_PINMUX(45, FUNC\_SEL\_UART\_RX | BIT(2))

[ 21](quicklogic-eos-s3-pinctrl_8h.md#ac8ede25f5a027513c1815e1ecd59f8b7)#define USB\_PU\_CTRL\_PAD23 QUICKLOGIC\_EOS\_S3\_PINMUX(23, 0x0)

[ 22](quicklogic-eos-s3-pinctrl_8h.md#ac9f2cd78de5e93b13ac7683e1439b21d)#define USB\_DN\_PAD28 QUICKLOGIC\_EOS\_S3\_PINMUX(28, 0x0)

[ 23](quicklogic-eos-s3-pinctrl_8h.md#ac814f848b3db7d98dada168dad9e0b74)#define USB\_DP\_PAD31 QUICKLOGIC\_EOS\_S3\_PINMUX(31, 0x0)

24

25#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_QUICKLOGIC\_EOS\_S3\_PINCTRL\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [quicklogic-eos-s3-pinctrl.h](quicklogic-eos-s3-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
