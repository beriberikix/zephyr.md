---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/imx8qm-pinctrl_8h_source.html
original_path: doxygen/html/imx8qm-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

imx8qm-pinctrl.h

[Go to the documentation of this file.](imx8qm-pinctrl_8h.md)

1/\*

2 \* Copyright 2023, 2025 NXP

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

[ 13](imx8qm-pinctrl_8h.md#ab701a7700915e279fd94a55242271391)#define SC\_P\_ESAI0\_FSR 104

[ 14](imx8qm-pinctrl_8h.md#a5edfd221c1748aaebd1e7ca50bee160d)#define SC\_P\_ESAI0\_FST 105

[ 15](imx8qm-pinctrl_8h.md#a7327c9ca8c3a7cf526af8fd06f49979a)#define SC\_P\_ESAI0\_SCKR 106

[ 16](imx8qm-pinctrl_8h.md#a03d21c813e46bd8d0e559ab650cd51cf)#define SC\_P\_ESAI0\_SCKT 107

[ 17](imx8qm-pinctrl_8h.md#a47791f7f5bb5e5f5b0b4f3d141939613)#define SC\_P\_ESAI0\_TX0 108

[ 18](imx8qm-pinctrl_8h.md#aae959f150f24fa5573c82673d2015191)#define SC\_P\_ESAI0\_TX1 109

[ 19](imx8qm-pinctrl_8h.md#a309087617f868dfc8dfa66431ffb722e)#define SC\_P\_ESAI0\_TX2\_RX3 110

[ 20](imx8qm-pinctrl_8h.md#a9fbef245436e89128f04a293d3ce221d)#define SC\_P\_ESAI0\_TX3\_RX2 111

[ 21](imx8qm-pinctrl_8h.md#ac19274d9c02ae4740501114d638d283a)#define SC\_P\_ESAI0\_TX4\_RX1 112

[ 22](imx8qm-pinctrl_8h.md#a9b4e197a3fdd8d4d41d53cb0e56ce47f)#define SC\_P\_ESAI0\_TX5\_RX0 113

[ 23](imx8qm-pinctrl_8h.md#aed4925b750ea0891fb3ba4a0fd8f764a)#define SC\_P\_SAI1\_RXD 128

[ 24](imx8qm-pinctrl_8h.md#a0025af9b5e4dd7337bc1b9169dc71187)#define SC\_P\_SAI1\_TXC 130

[ 25](imx8qm-pinctrl_8h.md#a0605b159e3c9e47701a635f1e3257d45)#define SC\_P\_SAI1\_TXD 131

[ 26](imx8qm-pinctrl_8h.md#aecab8f8eab601ffa895159e7d2960c15)#define SC\_P\_SAI1\_TXFS 132

27

28/\* mux values \*/

[ 29](imx8qm-pinctrl_8h.md#ade79c71c9c8fef95730c568d93f39b7a)#define IMX8QM\_DMA\_LPUART2\_RX\_UART0\_RTS\_B 2 /\* UART0\_RTS\_B ---> DMA\_LPUART2\_RX \*/

[ 30](imx8qm-pinctrl_8h.md#a8f0955628d1e5e10c30b5ed202fe0367)#define IMX8QM\_DMA\_LPUART2\_TX\_UART0\_CTS\_B 2 /\* DMA\_LPUART2\_TX ---> UART0\_CTS\_B \*/

[ 31](imx8qm-pinctrl_8h.md#abd4fdce8af139357ea1369cd9f0fd206)#define IMX8QM\_AUD\_SAI1\_RXD\_SAI1\_RXD 0 /\* AUD\_SAI1\_RXD <--- SAI1\_RXD \*/

[ 32](imx8qm-pinctrl_8h.md#a4f6cf25efafff77eb236fc78e360a411)#define IMX8QM\_AUD\_SAI1\_TXC\_SAI1\_TXC 0 /\* AUD\_SAI1\_TXC <---> SAI1\_TXC \*/

[ 33](imx8qm-pinctrl_8h.md#ac88247cbec30b3f0eea8cade6d3db323)#define IMX8QM\_AUD\_SAI1\_TXD\_SAI1\_TXD 0 /\* AUD\_SAI1\_TXD ---> SAI1\_TXD \*/

[ 34](imx8qm-pinctrl_8h.md#a808edbb666867aecf498972f2244a12b)#define IMX8QM\_AUD\_SAI1\_TXFS\_SAI1\_TXFS 0 /\* AUD\_SAI1\_TXFS <---> SAI1\_TXFS \*/

[ 35](imx8qm-pinctrl_8h.md#af00c612ab16adbf44d42b304fc3512a5)#define IMX8QM\_AUD\_ESAI0\_FSR\_ESAI0\_FSR 0

[ 36](imx8qm-pinctrl_8h.md#ae4e565cf769e86cc182b8d48f1102129)#define IMX8QM\_AUD\_ESAI0\_FST\_ESAI0\_FST 0

[ 37](imx8qm-pinctrl_8h.md#a99c81ba9aa2c81ce196985e95d533ad5)#define IMX8QM\_AUD\_ESAI0\_SCKR\_ESAI0\_SCKR 0

[ 38](imx8qm-pinctrl_8h.md#a813be1005bb9e8aa5512879078c038bd)#define IMX8QM\_AUD\_ESAI0\_SCKT\_ESAI0\_SCKT 0

[ 39](imx8qm-pinctrl_8h.md#aebc56edf6502422fd4be53aede4390f1)#define IMX8QM\_AUD\_ESAI0\_TX0\_ESAI\_TX0 0

[ 40](imx8qm-pinctrl_8h.md#ad436ace2b95ce101ef2412e56cfcf6ef)#define IMX8QM\_AUD\_ESAI0\_TX1\_ESAI\_TX1 0

[ 41](imx8qm-pinctrl_8h.md#a0167555c895d6abb65cb299f871af947)#define IMX8QM\_AUD\_ESAI0\_TX2\_RX3\_ESAI0\_TX2\_RX3 0

[ 42](imx8qm-pinctrl_8h.md#a20d33062c78dea5e68b10a7bb23d6d74)#define IMX8QM\_AUD\_ESAI0\_TX3\_RX2\_ESAI0\_TX3\_RX2 0

[ 43](imx8qm-pinctrl_8h.md#a2276261ab1c472e7c2abb27f6bda2aa9)#define IMX8QM\_AUD\_ESAI0\_TX4\_RX1\_ESAI0\_TX4\_RX1 0

[ 44](imx8qm-pinctrl_8h.md#aeb6c3d448b1e6b0bbf106fe4a2ad1511)#define IMX8QM\_AUD\_ESAI0\_TX5\_RX0\_ESAI0\_TX5\_RX0 0

45

46#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_IMX8QM\_PINCTRL\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [imx8qm-pinctrl.h](imx8qm-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
