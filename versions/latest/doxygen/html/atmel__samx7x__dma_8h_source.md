---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/atmel__samx7x__dma_8h_source.html
original_path: doxygen/html/atmel__samx7x__dma_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

atmel\_samx7x\_dma.h

[Go to the documentation of this file.](atmel__samx7x__dma_8h.md)

1/\*

2 \* Copyright (c) 2020 Linaro Limited

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ATMEL\_SAMX7X\_DMA\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ATMEL\_SAMX7X\_DMA\_H\_

8

[ 14](atmel__samx7x__dma_8h.md#a16b9db1626b4418e0774654c8e261f64)#define DMA\_PERID\_HSMCI\_TX\_RX 0

[ 15](atmel__samx7x__dma_8h.md#a2f87d5b1454bedeb193a2f1fe7dc4cfe)#define DMA\_PERID\_SPI0\_TX 1

[ 16](atmel__samx7x__dma_8h.md#a31d146fb80a3a2cf2555cf23c1e76200)#define DMA\_PERID\_SPI0\_RX 2

[ 17](atmel__samx7x__dma_8h.md#a35c0ef0b43ac8c255a1e604f178fb902)#define DMA\_PERID\_SPI1\_TX 3

[ 18](atmel__samx7x__dma_8h.md#a5f31ebe4c7df32c83c80edf4d5a80f44)#define DMA\_PERID\_SPI1\_RX 4

[ 19](atmel__samx7x__dma_8h.md#a8a7c3f53823d8b3522cbdbac0de7d329)#define DMA\_PERID\_QSPI\_TX 5

[ 20](atmel__samx7x__dma_8h.md#ac6df1a66062601ea550f7ede74bacc42)#define DMA\_PERID\_QSPI\_RX 6

[ 21](atmel__samx7x__dma_8h.md#ab42cb0cfbf34517f6419594b80347887)#define DMA\_PERID\_USART0\_TX 7

[ 22](atmel__samx7x__dma_8h.md#ab19aafb19b352c6568f5980afdbe51c1)#define DMA\_PERID\_USART0\_RX 8

[ 23](atmel__samx7x__dma_8h.md#ad0101a8a5c7bef36f742d0990f7f478a)#define DMA\_PERID\_USART1\_TX 9

[ 24](atmel__samx7x__dma_8h.md#a2d57240e7a8aa6f0fcd72272fb7d7aa5)#define DMA\_PERID\_USART1\_RX 10

[ 25](atmel__samx7x__dma_8h.md#a46f5b9b287b14852470eb6a0bfa9d290)#define DMA\_PERID\_USART2\_TX 11

[ 26](atmel__samx7x__dma_8h.md#a81598c830b204221143c2639dea45e5b)#define DMA\_PERID\_USART2\_RX 12

[ 27](atmel__samx7x__dma_8h.md#a21a595d27913d4eda1596f68746c4b0f)#define DMA\_PERID\_PWM0\_TX 13

[ 28](atmel__samx7x__dma_8h.md#a318c47d196be9c19d2ddb812c4ec3498)#define DMA\_PERID\_TWIHS0\_TX 14

[ 29](atmel__samx7x__dma_8h.md#a7b9a87a4999796fb4c400f310a269230)#define DMA\_PERID\_TWIHS0\_RX 15

[ 30](atmel__samx7x__dma_8h.md#a352930e4210499b7e54156a2d801a0ef)#define DMA\_PERID\_TWIHS1\_TX 16

[ 31](atmel__samx7x__dma_8h.md#a6f8be5d3b2e8905e1b347e1d32a8398b)#define DMA\_PERID\_TWIHS1\_RX 17

[ 32](atmel__samx7x__dma_8h.md#a9844a87e669d8262dfe2bec5849808fa)#define DMA\_PERID\_TWIHS2\_TX 18

[ 33](atmel__samx7x__dma_8h.md#a7442891a0d70641ccf2a758a43a139bf)#define DMA\_PERID\_TWIHS2\_RX 19

[ 34](atmel__samx7x__dma_8h.md#a18b3089708ac30eed659c2b5d92750d2)#define DMA\_PERID\_UART0\_TX 20

[ 35](atmel__samx7x__dma_8h.md#ab3d7a4ba7f32af80e912b4725e4dde46)#define DMA\_PERID\_UART0\_RX 21

[ 36](atmel__samx7x__dma_8h.md#a4c8e41936578a3a31d26b35a0e7aaabd)#define DMA\_PERID\_UART1\_TX 22

[ 37](atmel__samx7x__dma_8h.md#aaee887dbaed83e0a2941f49c70055d11)#define DMA\_PERID\_UART1\_RX 23

[ 38](atmel__samx7x__dma_8h.md#ad95ff1702d73c3037996e4f67a4c6fe9)#define DMA\_PERID\_UART2\_TX 24

[ 39](atmel__samx7x__dma_8h.md#a627cb308b8a264cae72de25b660e227a)#define DMA\_PERID\_UART2\_RX 25

[ 40](atmel__samx7x__dma_8h.md#a64e1c5cb19554e0503c3da0be1d3f4bd)#define DMA\_PERID\_UART3\_TX 26

[ 41](atmel__samx7x__dma_8h.md#ae1baa3ad5ea51d2ce29bb6451fe3ab44)#define DMA\_PERID\_UART3\_RX 27

[ 42](atmel__samx7x__dma_8h.md#a3cfd9eac3ca3e7f4698464d6eb415594)#define DMA\_PERID\_UART4\_TX 28

[ 43](atmel__samx7x__dma_8h.md#ad271c0d6a58e2228624b5d3ede5e4567)#define DMA\_PERID\_UART4\_RX 29

[ 44](atmel__samx7x__dma_8h.md#a82778d2873c0caa278d415ff43ec1793)#define DMA\_PERID\_DACC0\_TX 30

[ 45](atmel__samx7x__dma_8h.md#a54f9ae36524cd8c627467b86ec18d9a7)#define DMA\_PERID\_DACC1\_TX 31

[ 46](atmel__samx7x__dma_8h.md#a49b223e1003aaeb74f48d78ea0ea4eba)#define DMA\_PERID\_SSC\_TX 32

[ 47](atmel__samx7x__dma_8h.md#a4846fd126b4dddb9f8bff16235212b9d)#define DMA\_PERID\_SSC\_RX 33

[ 48](atmel__samx7x__dma_8h.md#a171d85b6ef14e6ade18095920a1dc2e6)#define DMA\_PERID\_PIOA\_RX 34

[ 49](atmel__samx7x__dma_8h.md#a6c861baaeac3fc444ad910dc164bed6d)#define DMA\_PERID\_AFEC0\_RX 35

[ 50](atmel__samx7x__dma_8h.md#abdfa1c39e23390d4e3b4cc8f96c59aa7)#define DMA\_PERID\_AFEC1\_RX 36

[ 51](atmel__samx7x__dma_8h.md#a0a1c2d866f4ff93fc2bb0ae30bdb3b68)#define DMA\_PERID\_AES\_TX 37

[ 52](atmel__samx7x__dma_8h.md#a356fac72c01bdb8e54801b9c5e823f24)#define DMA\_PERID\_AES\_RX 38

[ 53](atmel__samx7x__dma_8h.md#a398615ec6af12d0cae7a28ce994b7d8c)#define DMA\_PERID\_PWM1\_TX 39

[ 54](atmel__samx7x__dma_8h.md#a1cb3a2a18f35cb3696a290e11c0dd509)#define DMA\_PERID\_TC0\_RX 40

[ 55](atmel__samx7x__dma_8h.md#a164b686731864358c6b261de0d9d54d2)#define DMA\_PERID\_TC1\_RX 41

[ 56](atmel__samx7x__dma_8h.md#ab9f6c37c8c74e1bdaff88ddd759bd63b)#define DMA\_PERID\_TC2\_RX 42

[ 57](atmel__samx7x__dma_8h.md#a2b65b2d22441cd584e0a6050721794b4)#define DMA\_PERID\_TC3\_RX 43

[ 58](atmel__samx7x__dma_8h.md#a87bd80dfa6786745ce059d27ad092eed)#define DMA\_PERID\_I2SC0\_TX\_L 44

[ 59](atmel__samx7x__dma_8h.md#ae839fe5acfd05bb968080e6ac09f7310)#define DMA\_PERID\_I2SC0\_RX\_L 45

[ 60](atmel__samx7x__dma_8h.md#ae0c680dfe9170a6f3e1bff2ac4c2a0a2)#define DMA\_PERID\_I2SC1\_TX\_L 46

[ 61](atmel__samx7x__dma_8h.md#a750f991645276c40f01d243718cc3e91)#define DMA\_PERID\_I2SC1\_RX\_L 47

[ 62](atmel__samx7x__dma_8h.md#a3f82e5ff16160265557fb465420c3692)#define DMA\_PERID\_I2SC0\_TX\_R 48

[ 63](atmel__samx7x__dma_8h.md#a55e59763d73f4cb0007537f7878d700c)#define DMA\_PERID\_I2SC0\_RX\_R 49

[ 64](atmel__samx7x__dma_8h.md#a258877cef3fafb77e0ad645ee0ecdc26)#define DMA\_PERID\_I2SC1\_TX\_R 50

[ 65](atmel__samx7x__dma_8h.md#ae16dcc6df4f58f3c15fd502b9a6ea731)#define DMA\_PERID\_I2SC1\_RX\_R 51

66

67#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ATMEL\_SAMX7X\_DMA\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [atmel\_samx7x\_dma.h](atmel__samx7x__dma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
