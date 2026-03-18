---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/numicro-pinctrl_8h_source.html
original_path: doxygen/html/numicro-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

numicro-pinctrl.h

[Go to the documentation of this file.](numicro-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2022 SEAL AG

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_NUMICRO\_PINCTRL\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_NUMICRO\_PINCTRL\_H\_

9

[ 10](numicro-pinctrl_8h.md#ade38f6532bffc69965d508f87d8e1df8)#define NUMICRO\_MFP\_SHIFT 0U

[ 11](numicro-pinctrl_8h.md#ac9f4334d26beb00d4dea13d857d5e7ec)#define NUMICRO\_MFP\_MASK 0xFU

[ 12](numicro-pinctrl_8h.md#a478aaec941e205a651ec9dd5e50739eb)#define NUMICRO\_PIN\_SHIFT 4U

[ 13](numicro-pinctrl_8h.md#ad6e70da52aa12c4b62e8793bd3d64435)#define NUMICRO\_PIN\_MASK 0xFU

[ 14](numicro-pinctrl_8h.md#aa189da0ec8b427feabb6e0bfe82d6e88)#define NUMICRO\_PORT\_SHIFT 8U

[ 15](numicro-pinctrl_8h.md#a82825df678162bc24705348ac1ac74ca)#define NUMICRO\_PORT\_MASK 0xFU

16

[ 30](numicro-pinctrl_8h.md#a0309131a80b52c3c5ba0561b7cbd943f)#define NUMICRO\_PINMUX(port, pin, mfp) \

31 (((((port) - 'A') & NUMICRO\_PORT\_MASK) << NUMICRO\_PORT\_SHIFT) | \

32 (((pin) & NUMICRO\_PIN\_MASK) << NUMICRO\_PIN\_SHIFT) | \

33 (((mfp) & NUMICRO\_MFP\_MASK) << NUMICRO\_MFP\_SHIFT))

34

[ 35](numicro-pinctrl_8h.md#a23e9fef3fcbdab7aec502bd71c9e64cc)#define NUMICRO\_PORT(pinmux) \

36 (((pinmux) >> NUMICRO\_PORT\_SHIFT) & NUMICRO\_PORT\_MASK)

[ 37](numicro-pinctrl_8h.md#a1ab973be84bf86ae6c286b26379ac0dd)#define NUMICRO\_PIN(pinmux) \

38 (((pinmux) >> NUMICRO\_PIN\_SHIFT) & NUMICRO\_PIN\_MASK)

[ 39](numicro-pinctrl_8h.md#ac2c31c43ea1a65f7a5e9dae18ff39b0c)#define NUMICRO\_MFP(pinmux) \

40 (((pinmux) >> NUMICRO\_MFP\_SHIFT) & NUMICRO\_MFP\_MASK)

41

42#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_NUMICRO\_PINCTRL\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [numicro-pinctrl.h](numicro-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
