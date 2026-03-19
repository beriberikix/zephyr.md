---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/renesas-rzt2m-pinctrl_8h_source.html
original_path: doxygen/html/renesas-rzt2m-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas-rzt2m-pinctrl.h

[Go to the documentation of this file.](renesas-rzt2m-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2023 Antmicro <www.antmicro.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef \_\_RENESAS\_RZT2M\_PINCTRL\_H\_\_

8#define \_\_RENESAS\_RZT2M\_PINCTRL\_H\_\_

9

[ 10](renesas-rzt2m-pinctrl_8h.md#a3f45a2e9a92ee5884dd6020bfb77f683)#define RZT2M\_PINMUX(port, pin, func) ((port << 16) | (pin << 8) | func)

11

[ 12](renesas-rzt2m-pinctrl_8h.md#ade0a78ce111ddccc167c5b3a6ef1b7b0)#define UART0TX\_P16\_5 RZT2M\_PINMUX(16, 5, 1)

[ 13](renesas-rzt2m-pinctrl_8h.md#a3881268da0d5cdb51afb0114281dcb02)#define UART0RX\_P16\_6 RZT2M\_PINMUX(16, 6, 2)

14

[ 15](renesas-rzt2m-pinctrl_8h.md#a5c55cbae38d8df4f6678f379cb4e5ed2)#define UART3TX\_P18\_0 RZT2M\_PINMUX(18, 0, 4)

[ 16](renesas-rzt2m-pinctrl_8h.md#a86e9102e5f4f409facbffd2e4347071d)#define UART3RX\_P17\_7 RZT2M\_PINMUX(17, 7, 4)

17

18#endif /\* \_\_RENESAS\_RZT2M\_PINCTRL\_H\_\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas-rzt2m-pinctrl.h](renesas-rzt2m-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
