---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/imx8qxp-pinctrl_8h_source.html
original_path: doxygen/html/imx8qxp-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

imx8qxp-pinctrl.h

[Go to the documentation of this file.](imx8qxp-pinctrl_8h.md)

1/\*

2 \* Copyright 2023, 2025 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_IMX8QXP\_PINCTRL\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_IMX8QXP\_PINCTRL\_H\_

9

10/\* values for pad field \*/

[ 11](imx8qxp-pinctrl_8h.md#ab701a7700915e279fd94a55242271391)#define SC\_P\_ESAI0\_FSR 55

[ 12](imx8qxp-pinctrl_8h.md#a5edfd221c1748aaebd1e7ca50bee160d)#define SC\_P\_ESAI0\_FST 56

[ 13](imx8qxp-pinctrl_8h.md#a7327c9ca8c3a7cf526af8fd06f49979a)#define SC\_P\_ESAI0\_SCKR 57

[ 14](imx8qxp-pinctrl_8h.md#a03d21c813e46bd8d0e559ab650cd51cf)#define SC\_P\_ESAI0\_SCKT 58

[ 15](imx8qxp-pinctrl_8h.md#a47791f7f5bb5e5f5b0b4f3d141939613)#define SC\_P\_ESAI0\_TX0 59

[ 16](imx8qxp-pinctrl_8h.md#aae959f150f24fa5573c82673d2015191)#define SC\_P\_ESAI0\_TX1 60

[ 17](imx8qxp-pinctrl_8h.md#a309087617f868dfc8dfa66431ffb722e)#define SC\_P\_ESAI0\_TX2\_RX3 61

[ 18](imx8qxp-pinctrl_8h.md#a9fbef245436e89128f04a293d3ce221d)#define SC\_P\_ESAI0\_TX3\_RX2 62

[ 19](imx8qxp-pinctrl_8h.md#ac19274d9c02ae4740501114d638d283a)#define SC\_P\_ESAI0\_TX4\_RX1 63

[ 20](imx8qxp-pinctrl_8h.md#a9b4e197a3fdd8d4d41d53cb0e56ce47f)#define SC\_P\_ESAI0\_TX5\_RX0 64

[ 21](imx8qxp-pinctrl_8h.md#aed4925b750ea0891fb3ba4a0fd8f764a)#define SC\_P\_SAI1\_RXD 86

[ 22](imx8qxp-pinctrl_8h.md#ac10ea2dbe0fe7573b504833ff2686abf)#define SC\_P\_SAI1\_RXC 87

[ 23](imx8qxp-pinctrl_8h.md#acc9613444ebb12360d27006ec13fdc24)#define SC\_P\_SAI1\_RXFS 88

[ 24](imx8qxp-pinctrl_8h.md#a87a3edc8ce026af85fadad64b3de8df4)#define SC\_P\_SPI0\_CS1 96

[ 25](imx8qxp-pinctrl_8h.md#a439d8a14a740c03a41d84a3f58d2d64f)#define SC\_P\_UART2\_TX 113

[ 26](imx8qxp-pinctrl_8h.md#a42bb2e2da91a5928dda46bba414ac396)#define SC\_P\_UART2\_RX 114

27

28/\* mux values \*/

[ 29](imx8qxp-pinctrl_8h.md#a7b942182de88baca5cd8da3715048750)#define IMX8QXP\_DMA\_LPUART2\_RX\_UART2\_RX 0 /\* UART2\_RX ---> DMA\_LPUART2\_RX \*/

[ 30](imx8qxp-pinctrl_8h.md#ac3cca516631d1c243db966e16b4f7b3c)#define IMX8QXP\_DMA\_LPUART2\_TX\_UART2\_TX 0 /\* DMA\_LPUART2\_TX ---> UART2\_TX \*/

[ 31](imx8qxp-pinctrl_8h.md#a27bf71ba10f35a11d1fd48b6bb7a68ce)#define IMX8QXP\_ADMA\_SAI1\_TXFS\_SAI1\_RXFS 1 /\* ADMA\_SAI1\_TXFS <---> SAI1\_RXFS \*/

[ 32](imx8qxp-pinctrl_8h.md#a365a0d17e3bc273abe7d2ea2fc895552)#define IMX8QXP\_ADMA\_SAI1\_RXD\_SAI1\_RXD 0 /\* ADMA\_SAI1\_RXD <--- SAI1\_RXD \*/

[ 33](imx8qxp-pinctrl_8h.md#a302270f6db91a71ecf3294653ee542d5)#define IMX8QXP\_ADMA\_SAI1\_TXC\_SAI1\_RXC 1 /\* ADMA\_SAI1\_TXC <---> SAI1\_RXC \*/

[ 34](imx8qxp-pinctrl_8h.md#a4e8796484812bbde8369067b9b232177)#define IMX8QXP\_ADMA\_SAI1\_TXD\_SPI0\_CS1 2 /\* ADMA\_SAI1\_TXD ---> SPI0\_CS1 \*/

[ 35](imx8qxp-pinctrl_8h.md#a962e53d832c142a0fd9cdef3f916b51d)#define IMX8QXP\_ADMA\_ESAI0\_FSR\_ESAI0\_FSR 0

[ 36](imx8qxp-pinctrl_8h.md#a8278312265ffa6e770ddbc285cc34bac)#define IMX8QXP\_ADMA\_ESAI0\_FST\_ESAI0\_FST 0

[ 37](imx8qxp-pinctrl_8h.md#ad70b586ebedc94f3d3e30d5f121b82ac)#define IMX8QXP\_ADMA\_ESAI0\_SCKR\_ESAI0\_SCKR 0

[ 38](imx8qxp-pinctrl_8h.md#a6d06f1e2f8c6c2935f2241114a9e16a5)#define IMX8QXP\_ADMA\_ESAI0\_SCKT\_ESAI0\_SCKT 0

[ 39](imx8qxp-pinctrl_8h.md#a00bb9f97c122aa04f16b025d43409da4)#define IMX8QXP\_ADMA\_ESAI0\_TX0\_ESAI0\_TX0 0

[ 40](imx8qxp-pinctrl_8h.md#a08bbf15b8a35868cf78879f84a913e36)#define IMX8QXP\_ADMA\_ESAI0\_TX1\_ESAI0\_TX1 0

[ 41](imx8qxp-pinctrl_8h.md#ad5eddfb8c65b08ea938a0e548fa0a787)#define IMX8QXP\_ADMA\_ESAI0\_TX2\_RX3\_ESAI0\_TX2\_RX3 0

[ 42](imx8qxp-pinctrl_8h.md#a2cbc1e5c3012d193e5d7c2395d985b5e)#define IMX8QXP\_ADMA\_ESAI0\_TX3\_RX2\_ESAI0\_TX3\_RX2 0

[ 43](imx8qxp-pinctrl_8h.md#a6ef5e2a862f0bf07726b456916a65e52)#define IMX8QXP\_ADMA\_ESAI0\_TX4\_RX1\_ESAI0\_TX4\_RX1 0

[ 44](imx8qxp-pinctrl_8h.md#afb4ff3c4a0f8ca346e41e5444a36f797)#define IMX8QXP\_ADMA\_ESAI0\_TX5\_RX0\_ESAI0\_TX5\_RX0 0

45

46#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_IMX8QXP\_PINCTRL\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [imx8qxp-pinctrl.h](imx8qxp-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
