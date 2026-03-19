---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/xg29-dma_8h.html
original_path: doxygen/html/xg29-dma_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xg29-dma.h File Reference

`#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h_source.md)>`  
`#include "[common-dma.h](common-dma_8h_source.md)"`

[Go to the source code of this file.](xg29-dma_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DMA\_REQSEL\_NONE](#a3b04d98c82d29396f8e688db8d5c5de9)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
|  | Definition of Silabs LDMA request signal. |
| #define | [DMA\_REQSEL\_LDMAXBARPRSREQ0](#ac27c323faa6e0db8d8e6439fdd277181)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| #define | [DMA\_REQSEL\_LDMAXBARPRSREQ1](#ac20515cf65e2ca19ee0ad5f92403c6f1)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| #define | [DMA\_REQSEL\_TIMER0CC0](#a6fc80a2f87eb37f53c77fff13ba28c85)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 2) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| #define | [DMA\_REQSEL\_TIMER0CC1](#a310cc4350ec3f721a3ce4055ad8a1110)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 2) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| #define | [DMA\_REQSEL\_TIMER0CC2](#a2d02b538557c468e47cad0aef76952ef)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 2) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 2)) |
| #define | [DMA\_REQSEL\_TIMER0UFOF](#a1862b04a508e5c89a565040f2b20ad0b)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 2) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 3)) |
| #define | [DMA\_REQSEL\_TIMER1CC0](#ab6c754dbaa545bda3ebe376825958008)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 3) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| #define | [DMA\_REQSEL\_TIMER1CC1](#a909e0705fd68b7e79f6d07e5c9e7d9e9)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 3) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| #define | [DMA\_REQSEL\_TIMER1CC2](#a7299498af9580ac0236dfd776394e4f1)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 3) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 2)) |
| #define | [DMA\_REQSEL\_TIMER1UFOF](#a13f9bb1b7de6061b0eebca52e4349c71)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 3) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 3)) |
| #define | [DMA\_REQSEL\_USART0RXDATAV](#a4d8e451527281f0292c491fd1f40f709)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 4) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| #define | [DMA\_REQSEL\_USART0RXDATAVRIGHT](#a17598696e9a520ac6adea3920eff6900)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 4) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| #define | [DMA\_REQSEL\_USART0TXBL](#ae691ddb9858cbd5205c2d62ea54a2797)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 4) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 2)) |
| #define | [DMA\_REQSEL\_USART0TXBLRIGHT](#adf8abf7448fea14cbc7dcd946a1dfd91)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 4) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 3)) |
| #define | [DMA\_REQSEL\_USART0TXEMPTY](#a180469c6cace2af0e91336b25d18ece1)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 4) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 4)) |
| #define | [DMA\_REQSEL\_USART1RXDATAV](#af3a58d9f0d3770d966077a57a4943c9d)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 5) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| #define | [DMA\_REQSEL\_USART1RXDATAVRIGHT](#a00a5c899f86f2df43b1d0d118a87eabf)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 5) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| #define | [DMA\_REQSEL\_USART1TXBL](#a40c0cf3975a32bd1ccede07dd7fad334)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 5) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 2)) |
| #define | [DMA\_REQSEL\_USART1TXBLRIGHT](#a590b79286b632dc9fc12cf402d746d17)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 5) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 3)) |
| #define | [DMA\_REQSEL\_USART1TXEMPTY](#ab94d4e0857f9400f93a51ee1201f6bb7)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 5) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 4)) |
| #define | [DMA\_REQSEL\_I2C0RXDATAV](#a27f66bf3557d8f7f3b34251f03334926)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 6) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| #define | [DMA\_REQSEL\_I2C0TXBL](#a724a2e12ee165d026039df6a016d043e)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 6) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| #define | [DMA\_REQSEL\_I2C1RXDATAV](#a02e993bfd9d57d946257bc34d6538347)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 7) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| #define | [DMA\_REQSEL\_I2C1TXBL](#af2f468e4d0dc9fce4cc54810e739f11d)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 7) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| #define | [DMA\_REQSEL\_IADC0IADC\_SCAN](#a8940bc48310aad0e3c9cab0e5eb95742)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 11) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| #define | [DMA\_REQSEL\_IADC0IADC\_SINGLE](#ae8a09e6ec4fd8da57e5b568380afee64)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 11) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| #define | [DMA\_REQSEL\_MSCWDATA](#a296a10558a0bb7c76d3fd9eab80fff91)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 12) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| #define | [DMA\_REQSEL\_TIMER2CC0](#a8503415586264bbbc2c17560dfa36325)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 13) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| #define | [DMA\_REQSEL\_TIMER2CC1](#aed70ea120b2a199163c46f028aec4538)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 13) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| #define | [DMA\_REQSEL\_TIMER2CC2](#aff76df3b43b1ce7ff7cf36dad62914b5)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 13) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 2)) |
| #define | [DMA\_REQSEL\_TIMER2UFOF](#a359eec69c4e20a62fda0382318777ca2)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 13) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 3)) |
| #define | [DMA\_REQSEL\_TIMER3CC0](#acd2b7ad92fa2c7fe11b0410760e431d0)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 14) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| #define | [DMA\_REQSEL\_TIMER3CC1](#ac875ac8e9ee74e79df2e9a7e7f7d47bc)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 14) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| #define | [DMA\_REQSEL\_TIMER3CC2](#a84068b2390c9db03e234e8ebf7dd844e)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 14) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 2)) |
| #define | [DMA\_REQSEL\_TIMER3UFOF](#a0b099b82ec5b12e2da5d9fcafeb6feb4)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 14) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 3)) |
| #define | [DMA\_REQSEL\_PDMRXDATAV](#aa108050ebd2efcd502a1d057cab87cb0)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 15) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| #define | [DMA\_REQSEL\_TIMER4CC0](#a91a9946b6909ffb54bd69df41c5d9907)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 16) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| #define | [DMA\_REQSEL\_TIMER4CC1](#a3a12807722a1716c6bb6e58143441870)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 16) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| #define | [DMA\_REQSEL\_TIMER4CC2](#a3af0824dce9be11286d8521bb051554c)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 16) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 2)) |
| #define | [DMA\_REQSEL\_TIMER4UFOF](#a48480c7b2b8319598e5d609acc6852cd)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 16) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 3)) |
| #define | [DMA\_REQSEL\_EUSART0RXFL](#a1e7d7594318c137d147918cb045ac5e9)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 17) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| #define | [DMA\_REQSEL\_EUSART0TXFL](#a5ba224acfec4569865731d9af8a4ea26)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 17) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| #define | [DMA\_REQSEL\_EUSART1RXFL](#ae7962cdc63fac178d0e43dd85a5ec4c4)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 18) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| #define | [DMA\_REQSEL\_EUSART1TXFL](#a13d651b0c01c1370cb0b9806d5ce59cd)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 18) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |

## Macro Definition Documentation

## [◆ ](#a1e7d7594318c137d147918cb045ac5e9)DMA\_REQSEL\_EUSART0RXFL

| #define DMA\_REQSEL\_EUSART0RXFL   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 17) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| --- |

## [◆ ](#a5ba224acfec4569865731d9af8a4ea26)DMA\_REQSEL\_EUSART0TXFL

| #define DMA\_REQSEL\_EUSART0TXFL   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 17) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| --- |

## [◆ ](#ae7962cdc63fac178d0e43dd85a5ec4c4)DMA\_REQSEL\_EUSART1RXFL

| #define DMA\_REQSEL\_EUSART1RXFL   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 18) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| --- |

## [◆ ](#a13d651b0c01c1370cb0b9806d5ce59cd)DMA\_REQSEL\_EUSART1TXFL

| #define DMA\_REQSEL\_EUSART1TXFL   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 18) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| --- |

## [◆ ](#a27f66bf3557d8f7f3b34251f03334926)DMA\_REQSEL\_I2C0RXDATAV

| #define DMA\_REQSEL\_I2C0RXDATAV   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 6) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| --- |

## [◆ ](#a724a2e12ee165d026039df6a016d043e)DMA\_REQSEL\_I2C0TXBL

| #define DMA\_REQSEL\_I2C0TXBL   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 6) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| --- |

## [◆ ](#a02e993bfd9d57d946257bc34d6538347)DMA\_REQSEL\_I2C1RXDATAV

| #define DMA\_REQSEL\_I2C1RXDATAV   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 7) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| --- |

## [◆ ](#af2f468e4d0dc9fce4cc54810e739f11d)DMA\_REQSEL\_I2C1TXBL

| #define DMA\_REQSEL\_I2C1TXBL   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 7) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| --- |

## [◆ ](#a8940bc48310aad0e3c9cab0e5eb95742)DMA\_REQSEL\_IADC0IADC\_SCAN

| #define DMA\_REQSEL\_IADC0IADC\_SCAN   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 11) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| --- |

## [◆ ](#ae8a09e6ec4fd8da57e5b568380afee64)DMA\_REQSEL\_IADC0IADC\_SINGLE

| #define DMA\_REQSEL\_IADC0IADC\_SINGLE   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 11) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| --- |

## [◆ ](#ac27c323faa6e0db8d8e6439fdd277181)DMA\_REQSEL\_LDMAXBARPRSREQ0

| #define DMA\_REQSEL\_LDMAXBARPRSREQ0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| --- |

## [◆ ](#ac20515cf65e2ca19ee0ad5f92403c6f1)DMA\_REQSEL\_LDMAXBARPRSREQ1

| #define DMA\_REQSEL\_LDMAXBARPRSREQ1   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| --- |

## [◆ ](#a296a10558a0bb7c76d3fd9eab80fff91)DMA\_REQSEL\_MSCWDATA

| #define DMA\_REQSEL\_MSCWDATA   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 12) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| --- |

## [◆ ](#a3b04d98c82d29396f8e688db8d5c5de9)DMA\_REQSEL\_NONE

| #define DMA\_REQSEL\_NONE   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| --- |

Definition of Silabs LDMA request signal.

## [◆ ](#aa108050ebd2efcd502a1d057cab87cb0)DMA\_REQSEL\_PDMRXDATAV

| #define DMA\_REQSEL\_PDMRXDATAV   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 15) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| --- |

## [◆ ](#a6fc80a2f87eb37f53c77fff13ba28c85)DMA\_REQSEL\_TIMER0CC0

| #define DMA\_REQSEL\_TIMER0CC0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 2) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| --- |

## [◆ ](#a310cc4350ec3f721a3ce4055ad8a1110)DMA\_REQSEL\_TIMER0CC1

| #define DMA\_REQSEL\_TIMER0CC1   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 2) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| --- |

## [◆ ](#a2d02b538557c468e47cad0aef76952ef)DMA\_REQSEL\_TIMER0CC2

| #define DMA\_REQSEL\_TIMER0CC2   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 2) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 2)) |
| --- |

## [◆ ](#a1862b04a508e5c89a565040f2b20ad0b)DMA\_REQSEL\_TIMER0UFOF

| #define DMA\_REQSEL\_TIMER0UFOF   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 2) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 3)) |
| --- |

## [◆ ](#ab6c754dbaa545bda3ebe376825958008)DMA\_REQSEL\_TIMER1CC0

| #define DMA\_REQSEL\_TIMER1CC0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 3) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| --- |

## [◆ ](#a909e0705fd68b7e79f6d07e5c9e7d9e9)DMA\_REQSEL\_TIMER1CC1

| #define DMA\_REQSEL\_TIMER1CC1   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 3) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| --- |

## [◆ ](#a7299498af9580ac0236dfd776394e4f1)DMA\_REQSEL\_TIMER1CC2

| #define DMA\_REQSEL\_TIMER1CC2   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 3) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 2)) |
| --- |

## [◆ ](#a13f9bb1b7de6061b0eebca52e4349c71)DMA\_REQSEL\_TIMER1UFOF

| #define DMA\_REQSEL\_TIMER1UFOF   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 3) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 3)) |
| --- |

## [◆ ](#a8503415586264bbbc2c17560dfa36325)DMA\_REQSEL\_TIMER2CC0

| #define DMA\_REQSEL\_TIMER2CC0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 13) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| --- |

## [◆ ](#aed70ea120b2a199163c46f028aec4538)DMA\_REQSEL\_TIMER2CC1

| #define DMA\_REQSEL\_TIMER2CC1   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 13) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| --- |

## [◆ ](#aff76df3b43b1ce7ff7cf36dad62914b5)DMA\_REQSEL\_TIMER2CC2

| #define DMA\_REQSEL\_TIMER2CC2   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 13) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 2)) |
| --- |

## [◆ ](#a359eec69c4e20a62fda0382318777ca2)DMA\_REQSEL\_TIMER2UFOF

| #define DMA\_REQSEL\_TIMER2UFOF   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 13) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 3)) |
| --- |

## [◆ ](#acd2b7ad92fa2c7fe11b0410760e431d0)DMA\_REQSEL\_TIMER3CC0

| #define DMA\_REQSEL\_TIMER3CC0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 14) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| --- |

## [◆ ](#ac875ac8e9ee74e79df2e9a7e7f7d47bc)DMA\_REQSEL\_TIMER3CC1

| #define DMA\_REQSEL\_TIMER3CC1   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 14) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| --- |

## [◆ ](#a84068b2390c9db03e234e8ebf7dd844e)DMA\_REQSEL\_TIMER3CC2

| #define DMA\_REQSEL\_TIMER3CC2   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 14) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 2)) |
| --- |

## [◆ ](#a0b099b82ec5b12e2da5d9fcafeb6feb4)DMA\_REQSEL\_TIMER3UFOF

| #define DMA\_REQSEL\_TIMER3UFOF   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 14) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 3)) |
| --- |

## [◆ ](#a91a9946b6909ffb54bd69df41c5d9907)DMA\_REQSEL\_TIMER4CC0

| #define DMA\_REQSEL\_TIMER4CC0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 16) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| --- |

## [◆ ](#a3a12807722a1716c6bb6e58143441870)DMA\_REQSEL\_TIMER4CC1

| #define DMA\_REQSEL\_TIMER4CC1   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 16) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| --- |

## [◆ ](#a3af0824dce9be11286d8521bb051554c)DMA\_REQSEL\_TIMER4CC2

| #define DMA\_REQSEL\_TIMER4CC2   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 16) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 2)) |
| --- |

## [◆ ](#a48480c7b2b8319598e5d609acc6852cd)DMA\_REQSEL\_TIMER4UFOF

| #define DMA\_REQSEL\_TIMER4UFOF   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 16) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 3)) |
| --- |

## [◆ ](#a4d8e451527281f0292c491fd1f40f709)DMA\_REQSEL\_USART0RXDATAV

| #define DMA\_REQSEL\_USART0RXDATAV   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 4) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| --- |

## [◆ ](#a17598696e9a520ac6adea3920eff6900)DMA\_REQSEL\_USART0RXDATAVRIGHT

| #define DMA\_REQSEL\_USART0RXDATAVRIGHT   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 4) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| --- |

## [◆ ](#ae691ddb9858cbd5205c2d62ea54a2797)DMA\_REQSEL\_USART0TXBL

| #define DMA\_REQSEL\_USART0TXBL   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 4) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 2)) |
| --- |

## [◆ ](#adf8abf7448fea14cbc7dcd946a1dfd91)DMA\_REQSEL\_USART0TXBLRIGHT

| #define DMA\_REQSEL\_USART0TXBLRIGHT   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 4) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 3)) |
| --- |

## [◆ ](#a180469c6cace2af0e91336b25d18ece1)DMA\_REQSEL\_USART0TXEMPTY

| #define DMA\_REQSEL\_USART0TXEMPTY   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 4) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 4)) |
| --- |

## [◆ ](#af3a58d9f0d3770d966077a57a4943c9d)DMA\_REQSEL\_USART1RXDATAV

| #define DMA\_REQSEL\_USART1RXDATAV   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 5) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 0)) |
| --- |

## [◆ ](#a00a5c899f86f2df43b1d0d118a87eabf)DMA\_REQSEL\_USART1RXDATAVRIGHT

| #define DMA\_REQSEL\_USART1RXDATAVRIGHT   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 5) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 1)) |
| --- |

## [◆ ](#a40c0cf3975a32bd1ccede07dd7fad334)DMA\_REQSEL\_USART1TXBL

| #define DMA\_REQSEL\_USART1TXBL   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 5) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 2)) |
| --- |

## [◆ ](#a590b79286b632dc9fc12cf402d746d17)DMA\_REQSEL\_USART1TXBLRIGHT

| #define DMA\_REQSEL\_USART1TXBLRIGHT   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 5) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 3)) |
| --- |

## [◆ ](#ab94d4e0857f9400f93a51ee1201f6bb7)DMA\_REQSEL\_USART1TXEMPTY

| #define DMA\_REQSEL\_USART1TXEMPTY   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SRC\_MASK](common-dma_8h.md#a0e9e5febc44f1450a524ec73c9649d20), 5) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([DMA\_SIG\_MASK](common-dma_8h.md#afe1c8630fc69f691df9bdcfb8f4ebb67), 4)) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [silabs](dir_457bcdd23b8c5c7a64b19c2fab5b10fc.md)
- [xg29-dma.h](xg29-dma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
