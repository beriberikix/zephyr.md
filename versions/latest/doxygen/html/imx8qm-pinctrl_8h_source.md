---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/imx8qm-pinctrl_8h_source.html
original_path: doxygen/html/imx8qm-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

imx8qm-pinctrl.h

[Go to the documentation of this file.](imx8qm-pinctrl_8h.md)

1/\*

2 \* Copyright 2023 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_IMX8QM\_PINCTRL\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_IMX8QM\_PINCTRL\_H\_

9

10/\* values for pad field \*/

[ 11](imx8qm-pinctrl_8h.md#a9e6adbd17d8af3d80e25e214f920b099)#define SC\_P\_UART0\_RTS\_B 23

[ 12](imx8qm-pinctrl_8h.md#abc16d007f79b8dac3f53ef88452622a4)#define SC\_P\_UART0\_CTS\_B 24

13

14/\* mux values \*/

[ 15](imx8qm-pinctrl_8h.md#ade79c71c9c8fef95730c568d93f39b7a)#define IMX8QM\_DMA\_LPUART2\_RX\_UART0\_RTS\_B 2 /\* UART0\_RTS\_B ---> DMA\_LPUART2\_RX \*/

[ 16](imx8qm-pinctrl_8h.md#a8f0955628d1e5e10c30b5ed202fe0367)#define IMX8QM\_DMA\_LPUART2\_TX\_UART0\_CTS\_B 2 /\* DMA\_LPUART2\_TX ---> UART0\_CTS\_B \*/

17

18#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_IMX8QM\_PINCTRL\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [imx8qm-pinctrl.h](imx8qm-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
