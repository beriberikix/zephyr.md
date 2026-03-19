---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/imx8qm-pinctrl_8h_source.html
original_path: doxygen/html/imx8qm-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

[ 13](imx8qm-pinctrl_8h.md#aed4925b750ea0891fb3ba4a0fd8f764a)#define SC\_P\_SAI1\_RXD 128

[ 14](imx8qm-pinctrl_8h.md#a0025af9b5e4dd7337bc1b9169dc71187)#define SC\_P\_SAI1\_TXC 130

[ 15](imx8qm-pinctrl_8h.md#a0605b159e3c9e47701a635f1e3257d45)#define SC\_P\_SAI1\_TXD 131

[ 16](imx8qm-pinctrl_8h.md#aecab8f8eab601ffa895159e7d2960c15)#define SC\_P\_SAI1\_TXFS 132

17

18/\* mux values \*/

[ 19](imx8qm-pinctrl_8h.md#ade79c71c9c8fef95730c568d93f39b7a)#define IMX8QM\_DMA\_LPUART2\_RX\_UART0\_RTS\_B 2 /\* UART0\_RTS\_B ---> DMA\_LPUART2\_RX \*/

[ 20](imx8qm-pinctrl_8h.md#a8f0955628d1e5e10c30b5ed202fe0367)#define IMX8QM\_DMA\_LPUART2\_TX\_UART0\_CTS\_B 2 /\* DMA\_LPUART2\_TX ---> UART0\_CTS\_B \*/

[ 21](imx8qm-pinctrl_8h.md#abd4fdce8af139357ea1369cd9f0fd206)#define IMX8QM\_AUD\_SAI1\_RXD\_SAI1\_RXD 0 /\* AUD\_SAI1\_RXD <--- SAI1\_RXD \*/

[ 22](imx8qm-pinctrl_8h.md#a4f6cf25efafff77eb236fc78e360a411)#define IMX8QM\_AUD\_SAI1\_TXC\_SAI1\_TXC 0 /\* AUD\_SAI1\_TXC <---> SAI1\_TXC \*/

[ 23](imx8qm-pinctrl_8h.md#ac88247cbec30b3f0eea8cade6d3db323)#define IMX8QM\_AUD\_SAI1\_TXD\_SAI1\_TXD 0 /\* AUD\_SAI1\_TXD ---> SAI1\_TXD \*/

[ 24](imx8qm-pinctrl_8h.md#a808edbb666867aecf498972f2244a12b)#define IMX8QM\_AUD\_SAI1\_TXFS\_SAI1\_TXFS 0 /\* AUD\_SAI1\_TXFS <---> SAI1\_TXFS \*/

25

26#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_IMX8QM\_PINCTRL\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [imx8qm-pinctrl.h](imx8qm-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
