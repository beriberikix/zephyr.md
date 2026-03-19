---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/imx8qxp-pinctrl_8h_source.html
original_path: doxygen/html/imx8qxp-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

imx8qxp-pinctrl.h

[Go to the documentation of this file.](imx8qxp-pinctrl_8h.md)

1/\*

2 \* Copyright 2023 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_IMX8QXP\_PINCTRL\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_IMX8QXP\_PINCTRL\_H\_

9

10/\* values for pad field \*/

[ 11](imx8qxp-pinctrl_8h.md#aed4925b750ea0891fb3ba4a0fd8f764a)#define SC\_P\_SAI1\_RXD 86

[ 12](imx8qxp-pinctrl_8h.md#ac10ea2dbe0fe7573b504833ff2686abf)#define SC\_P\_SAI1\_RXC 87

[ 13](imx8qxp-pinctrl_8h.md#acc9613444ebb12360d27006ec13fdc24)#define SC\_P\_SAI1\_RXFS 88

[ 14](imx8qxp-pinctrl_8h.md#a87a3edc8ce026af85fadad64b3de8df4)#define SC\_P\_SPI0\_CS1 96

[ 15](imx8qxp-pinctrl_8h.md#a439d8a14a740c03a41d84a3f58d2d64f)#define SC\_P\_UART2\_TX 113

[ 16](imx8qxp-pinctrl_8h.md#a42bb2e2da91a5928dda46bba414ac396)#define SC\_P\_UART2\_RX 114

17

18/\* mux values \*/

[ 19](imx8qxp-pinctrl_8h.md#a7b942182de88baca5cd8da3715048750)#define IMX8QXP\_DMA\_LPUART2\_RX\_UART2\_RX 0 /\* UART2\_RX ---> DMA\_LPUART2\_RX \*/

[ 20](imx8qxp-pinctrl_8h.md#ac3cca516631d1c243db966e16b4f7b3c)#define IMX8QXP\_DMA\_LPUART2\_TX\_UART2\_TX 0 /\* DMA\_LPUART2\_TX ---> UART2\_TX \*/

[ 21](imx8qxp-pinctrl_8h.md#a27bf71ba10f35a11d1fd48b6bb7a68ce)#define IMX8QXP\_ADMA\_SAI1\_TXFS\_SAI1\_RXFS 1 /\* ADMA\_SAI1\_TXFS <---> SAI1\_RXFS \*/

[ 22](imx8qxp-pinctrl_8h.md#a365a0d17e3bc273abe7d2ea2fc895552)#define IMX8QXP\_ADMA\_SAI1\_RXD\_SAI1\_RXD 0 /\* ADMA\_SAI1\_RXD <--- SAI1\_RXD \*/

[ 23](imx8qxp-pinctrl_8h.md#a302270f6db91a71ecf3294653ee542d5)#define IMX8QXP\_ADMA\_SAI1\_TXC\_SAI1\_RXC 1 /\* ADMA\_SAI1\_TXC <---> SAI1\_RXC \*/

[ 24](imx8qxp-pinctrl_8h.md#a4e8796484812bbde8369067b9b232177)#define IMX8QXP\_ADMA\_SAI1\_TXD\_SPI0\_CS1 2 /\* ADMA\_SAI1\_TXD ---> SPI0\_CS1 \*/

25

26#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_IMX8QXP\_PINCTRL\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [imx8qxp-pinctrl.h](imx8qxp-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
