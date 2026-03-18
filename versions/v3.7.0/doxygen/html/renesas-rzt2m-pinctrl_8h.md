---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/renesas-rzt2m-pinctrl_8h.html
original_path: doxygen/html/renesas-rzt2m-pinctrl_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas-rzt2m-pinctrl.h File Reference

[Go to the source code of this file.](renesas-rzt2m-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RZT2M\_PINMUX](#a3f45a2e9a92ee5884dd6020bfb77f683)(port, pin, func) |
| #define | [UART0TX\_P16\_5](#ade0a78ce111ddccc167c5b3a6ef1b7b0)   [RZT2M\_PINMUX](#a3f45a2e9a92ee5884dd6020bfb77f683)(16, 5, 1) |
| #define | [UART0RX\_P16\_6](#a3881268da0d5cdb51afb0114281dcb02)   [RZT2M\_PINMUX](#a3f45a2e9a92ee5884dd6020bfb77f683)(16, 6, 2) |
| #define | [UART3TX\_P18\_0](#a5c55cbae38d8df4f6678f379cb4e5ed2)   [RZT2M\_PINMUX](#a3f45a2e9a92ee5884dd6020bfb77f683)(18, 0, 4) |
| #define | [UART3RX\_P17\_7](#a86e9102e5f4f409facbffd2e4347071d)   [RZT2M\_PINMUX](#a3f45a2e9a92ee5884dd6020bfb77f683)(17, 7, 4) |

## Macro Definition Documentation

## [◆ ](#a3f45a2e9a92ee5884dd6020bfb77f683)RZT2M\_PINMUX

| #define RZT2M\_PINMUX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin*, |
|  |  |  | *func* ) |

**Value:**

((port << 16) | (pin << 8) | func)

## [◆ ](#a3881268da0d5cdb51afb0114281dcb02)UART0RX\_P16\_6

| #define UART0RX\_P16\_6   [RZT2M\_PINMUX](#a3f45a2e9a92ee5884dd6020bfb77f683)(16, 6, 2) |
| --- |

## [◆ ](#ade0a78ce111ddccc167c5b3a6ef1b7b0)UART0TX\_P16\_5

| #define UART0TX\_P16\_5   [RZT2M\_PINMUX](#a3f45a2e9a92ee5884dd6020bfb77f683)(16, 5, 1) |
| --- |

## [◆ ](#a86e9102e5f4f409facbffd2e4347071d)UART3RX\_P17\_7

| #define UART3RX\_P17\_7   [RZT2M\_PINMUX](#a3f45a2e9a92ee5884dd6020bfb77f683)(17, 7, 4) |
| --- |

## [◆ ](#a5c55cbae38d8df4f6678f379cb4e5ed2)UART3TX\_P18\_0

| #define UART3TX\_P18\_0   [RZT2M\_PINMUX](#a3f45a2e9a92ee5884dd6020bfb77f683)(18, 0, 4) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas-rzt2m-pinctrl.h](renesas-rzt2m-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
