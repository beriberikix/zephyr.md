---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/xg21-dma_8h_source.html
original_path: doxygen/html/xg21-dma_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xg21-dma.h

[Go to the documentation of this file.](xg21-dma_8h.md)

1/\*

2 \* Copyright (c) 2025 Silicon Laboratories Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_XG21\_DMA\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_XG21\_DMA\_H\_

8

9#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

10#include "[common-dma.h](common-dma_8h.md)"

11

[ 15](xg21-dma_8h.md#a3b04d98c82d29396f8e688db8d5c5de9)#define DMA\_REQSEL\_NONE (FIELD\_PREP(DMA\_SRC\_MASK, 0) | FIELD\_PREP(DMA\_SIG\_MASK, 0))

[ 16](xg21-dma_8h.md#ac27c323faa6e0db8d8e6439fdd277181)#define DMA\_REQSEL\_LDMAXBARPRSREQ0 (FIELD\_PREP(DMA\_SRC\_MASK, 1) | FIELD\_PREP(DMA\_SIG\_MASK, 0))

[ 17](xg21-dma_8h.md#ac20515cf65e2ca19ee0ad5f92403c6f1)#define DMA\_REQSEL\_LDMAXBARPRSREQ1 (FIELD\_PREP(DMA\_SRC\_MASK, 1) | FIELD\_PREP(DMA\_SIG\_MASK, 1))

[ 18](xg21-dma_8h.md#a6fc80a2f87eb37f53c77fff13ba28c85)#define DMA\_REQSEL\_TIMER0CC0 (FIELD\_PREP(DMA\_SRC\_MASK, 2) | FIELD\_PREP(DMA\_SIG\_MASK, 0))

[ 19](xg21-dma_8h.md#a310cc4350ec3f721a3ce4055ad8a1110)#define DMA\_REQSEL\_TIMER0CC1 (FIELD\_PREP(DMA\_SRC\_MASK, 2) | FIELD\_PREP(DMA\_SIG\_MASK, 1))

[ 20](xg21-dma_8h.md#a2d02b538557c468e47cad0aef76952ef)#define DMA\_REQSEL\_TIMER0CC2 (FIELD\_PREP(DMA\_SRC\_MASK, 2) | FIELD\_PREP(DMA\_SIG\_MASK, 2))

[ 21](xg21-dma_8h.md#a1862b04a508e5c89a565040f2b20ad0b)#define DMA\_REQSEL\_TIMER0UFOF (FIELD\_PREP(DMA\_SRC\_MASK, 2) | FIELD\_PREP(DMA\_SIG\_MASK, 3))

[ 22](xg21-dma_8h.md#ab6c754dbaa545bda3ebe376825958008)#define DMA\_REQSEL\_TIMER1CC0 (FIELD\_PREP(DMA\_SRC\_MASK, 3) | FIELD\_PREP(DMA\_SIG\_MASK, 0))

[ 23](xg21-dma_8h.md#a909e0705fd68b7e79f6d07e5c9e7d9e9)#define DMA\_REQSEL\_TIMER1CC1 (FIELD\_PREP(DMA\_SRC\_MASK, 3) | FIELD\_PREP(DMA\_SIG\_MASK, 1))

[ 24](xg21-dma_8h.md#a7299498af9580ac0236dfd776394e4f1)#define DMA\_REQSEL\_TIMER1CC2 (FIELD\_PREP(DMA\_SRC\_MASK, 3) | FIELD\_PREP(DMA\_SIG\_MASK, 2))

[ 25](xg21-dma_8h.md#a13f9bb1b7de6061b0eebca52e4349c71)#define DMA\_REQSEL\_TIMER1UFOF (FIELD\_PREP(DMA\_SRC\_MASK, 3) | FIELD\_PREP(DMA\_SIG\_MASK, 3))

[ 26](xg21-dma_8h.md#a4d8e451527281f0292c491fd1f40f709)#define DMA\_REQSEL\_USART0RXDATAV (FIELD\_PREP(DMA\_SRC\_MASK, 4) | FIELD\_PREP(DMA\_SIG\_MASK, 0))

[ 27](xg21-dma_8h.md#a17598696e9a520ac6adea3920eff6900)#define DMA\_REQSEL\_USART0RXDATAVRIGHT (FIELD\_PREP(DMA\_SRC\_MASK, 4) | FIELD\_PREP(DMA\_SIG\_MASK, 1))

[ 28](xg21-dma_8h.md#ae691ddb9858cbd5205c2d62ea54a2797)#define DMA\_REQSEL\_USART0TXBL (FIELD\_PREP(DMA\_SRC\_MASK, 4) | FIELD\_PREP(DMA\_SIG\_MASK, 2))

[ 29](xg21-dma_8h.md#adf8abf7448fea14cbc7dcd946a1dfd91)#define DMA\_REQSEL\_USART0TXBLRIGHT (FIELD\_PREP(DMA\_SRC\_MASK, 4) | FIELD\_PREP(DMA\_SIG\_MASK, 3))

[ 30](xg21-dma_8h.md#a180469c6cace2af0e91336b25d18ece1)#define DMA\_REQSEL\_USART0TXEMPTY (FIELD\_PREP(DMA\_SRC\_MASK, 4) | FIELD\_PREP(DMA\_SIG\_MASK, 4))

[ 31](xg21-dma_8h.md#af3a58d9f0d3770d966077a57a4943c9d)#define DMA\_REQSEL\_USART1RXDATAV (FIELD\_PREP(DMA\_SRC\_MASK, 5) | FIELD\_PREP(DMA\_SIG\_MASK, 0))

[ 32](xg21-dma_8h.md#a00a5c899f86f2df43b1d0d118a87eabf)#define DMA\_REQSEL\_USART1RXDATAVRIGHT (FIELD\_PREP(DMA\_SRC\_MASK, 5) | FIELD\_PREP(DMA\_SIG\_MASK, 1))

[ 33](xg21-dma_8h.md#a40c0cf3975a32bd1ccede07dd7fad334)#define DMA\_REQSEL\_USART1TXBL (FIELD\_PREP(DMA\_SRC\_MASK, 5) | FIELD\_PREP(DMA\_SIG\_MASK, 2))

[ 34](xg21-dma_8h.md#a590b79286b632dc9fc12cf402d746d17)#define DMA\_REQSEL\_USART1TXBLRIGHT (FIELD\_PREP(DMA\_SRC\_MASK, 5) | FIELD\_PREP(DMA\_SIG\_MASK, 3))

[ 35](xg21-dma_8h.md#ab94d4e0857f9400f93a51ee1201f6bb7)#define DMA\_REQSEL\_USART1TXEMPTY (FIELD\_PREP(DMA\_SRC\_MASK, 5) | FIELD\_PREP(DMA\_SIG\_MASK, 4))

[ 36](xg21-dma_8h.md#a9a6b856f36ea434d7fb1c771bf9e5b68)#define DMA\_REQSEL\_USART2RXDATAV (FIELD\_PREP(DMA\_SRC\_MASK, 6) | FIELD\_PREP(DMA\_SIG\_MASK, 0))

[ 37](xg21-dma_8h.md#a6ca7c10d705d1313b79c228df8a720f6)#define DMA\_REQSEL\_USART2RXDATAVRIGHT (FIELD\_PREP(DMA\_SRC\_MASK, 6) | FIELD\_PREP(DMA\_SIG\_MASK, 1))

[ 38](xg21-dma_8h.md#a1e0a363ff93f370d2731a116b5a53148)#define DMA\_REQSEL\_USART2TXBL (FIELD\_PREP(DMA\_SRC\_MASK, 6) | FIELD\_PREP(DMA\_SIG\_MASK, 2))

[ 39](xg21-dma_8h.md#a552d14b03c3974a9ec7edc2962c50119)#define DMA\_REQSEL\_USART2TXBLRIGHT (FIELD\_PREP(DMA\_SRC\_MASK, 6) | FIELD\_PREP(DMA\_SIG\_MASK, 3))

[ 40](xg21-dma_8h.md#a315f45b4138fe8f09fff2772acbef060)#define DMA\_REQSEL\_USART2TXEMPTY (FIELD\_PREP(DMA\_SRC\_MASK, 6) | FIELD\_PREP(DMA\_SIG\_MASK, 4))

[ 41](xg21-dma_8h.md#a27f66bf3557d8f7f3b34251f03334926)#define DMA\_REQSEL\_I2C0RXDATAV (FIELD\_PREP(DMA\_SRC\_MASK, 7) | FIELD\_PREP(DMA\_SIG\_MASK, 0))

[ 42](xg21-dma_8h.md#a724a2e12ee165d026039df6a016d043e)#define DMA\_REQSEL\_I2C0TXBL (FIELD\_PREP(DMA\_SRC\_MASK, 7) | FIELD\_PREP(DMA\_SIG\_MASK, 1))

[ 43](xg21-dma_8h.md#a02e993bfd9d57d946257bc34d6538347)#define DMA\_REQSEL\_I2C1RXDATAV (FIELD\_PREP(DMA\_SRC\_MASK, 8) | FIELD\_PREP(DMA\_SIG\_MASK, 0))

[ 44](xg21-dma_8h.md#af2f468e4d0dc9fce4cc54810e739f11d)#define DMA\_REQSEL\_I2C1TXBL (FIELD\_PREP(DMA\_SRC\_MASK, 8) | FIELD\_PREP(DMA\_SIG\_MASK, 1))

[ 45](xg21-dma_8h.md#a8940bc48310aad0e3c9cab0e5eb95742)#define DMA\_REQSEL\_IADC0IADC\_SCAN (FIELD\_PREP(DMA\_SRC\_MASK, 12) | FIELD\_PREP(DMA\_SIG\_MASK, 0))

[ 46](xg21-dma_8h.md#ae8a09e6ec4fd8da57e5b568380afee64)#define DMA\_REQSEL\_IADC0IADC\_SINGLE (FIELD\_PREP(DMA\_SRC\_MASK, 12) | FIELD\_PREP(DMA\_SIG\_MASK, 1))

[ 47](xg21-dma_8h.md#a296a10558a0bb7c76d3fd9eab80fff91)#define DMA\_REQSEL\_MSCWDATA (FIELD\_PREP(DMA\_SRC\_MASK, 13) | FIELD\_PREP(DMA\_SIG\_MASK, 0))

[ 48](xg21-dma_8h.md#a8503415586264bbbc2c17560dfa36325)#define DMA\_REQSEL\_TIMER2CC0 (FIELD\_PREP(DMA\_SRC\_MASK, 14) | FIELD\_PREP(DMA\_SIG\_MASK, 0))

[ 49](xg21-dma_8h.md#aed70ea120b2a199163c46f028aec4538)#define DMA\_REQSEL\_TIMER2CC1 (FIELD\_PREP(DMA\_SRC\_MASK, 14) | FIELD\_PREP(DMA\_SIG\_MASK, 1))

[ 50](xg21-dma_8h.md#aff76df3b43b1ce7ff7cf36dad62914b5)#define DMA\_REQSEL\_TIMER2CC2 (FIELD\_PREP(DMA\_SRC\_MASK, 14) | FIELD\_PREP(DMA\_SIG\_MASK, 2))

[ 51](xg21-dma_8h.md#a359eec69c4e20a62fda0382318777ca2)#define DMA\_REQSEL\_TIMER2UFOF (FIELD\_PREP(DMA\_SRC\_MASK, 14) | FIELD\_PREP(DMA\_SIG\_MASK, 3))

[ 52](xg21-dma_8h.md#acd2b7ad92fa2c7fe11b0410760e431d0)#define DMA\_REQSEL\_TIMER3CC0 (FIELD\_PREP(DMA\_SRC\_MASK, 15) | FIELD\_PREP(DMA\_SIG\_MASK, 0))

[ 53](xg21-dma_8h.md#ac875ac8e9ee74e79df2e9a7e7f7d47bc)#define DMA\_REQSEL\_TIMER3CC1 (FIELD\_PREP(DMA\_SRC\_MASK, 15) | FIELD\_PREP(DMA\_SIG\_MASK, 1))

[ 54](xg21-dma_8h.md#a84068b2390c9db03e234e8ebf7dd844e)#define DMA\_REQSEL\_TIMER3CC2 (FIELD\_PREP(DMA\_SRC\_MASK, 15) | FIELD\_PREP(DMA\_SIG\_MASK, 2))

[ 55](xg21-dma_8h.md#a0b099b82ec5b12e2da5d9fcafeb6feb4)#define DMA\_REQSEL\_TIMER3UFOF (FIELD\_PREP(DMA\_SRC\_MASK, 15) | FIELD\_PREP(DMA\_SIG\_MASK, 3))

56

57#endif ZEPHYR\_INCLUDE\_DT\_BINDINGS\_XG21\_DMA\_H\_

[common-dma.h](common-dma_8h.md)

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [silabs](dir_457bcdd23b8c5c7a64b19c2fab5b10fc.md)
- [xg21-dma.h](xg21-dma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
