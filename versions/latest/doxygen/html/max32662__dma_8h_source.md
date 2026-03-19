---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/max32662__dma_8h_source.html
original_path: doxygen/html/max32662__dma_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

max32662\_dma.h

[Go to the documentation of this file.](max32662__dma_8h.md)

1/\*

2 \* Copyright (c) 2024 Analog Devices, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_DMA\_MAX32662\_DMA\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_DMA\_MAX32662\_DMA\_H\_

9

[ 10](max32662__dma_8h.md#a6e1ea6d5650545947928c83c71776c04)#define MAX32\_DMA\_SLOT\_MEMTOMEM 0x00U

[ 11](max32662__dma_8h.md#ac505ee888a8cb52b03ac733a9b650097)#define MAX32\_DMA\_SLOT\_SPI0\_RX 0x01U

[ 12](max32662__dma_8h.md#a0df8d71978ba7b5c5b6766c1cf28d00c)#define MAX32\_DMA\_SLOT\_SPI1\_RX 0x02U

[ 13](max32662__dma_8h.md#ac823471b99eda7df54c2fce6eb923e96)#define MAX32\_DMA\_SLOT\_UART0\_RX 0x04U

[ 14](max32662__dma_8h.md#ab7e79c3fa976243daa7ef5880f20fade)#define MAX32\_DMA\_SLOT\_UART1\_RX 0x05U

[ 15](max32662__dma_8h.md#a575aa21e202d58585069733331d52d56)#define MAX32\_DMA\_SLOT\_CAN\_RX 0x06U

[ 16](max32662__dma_8h.md#a207563fbc9fb4110d78f92b1d2d4c423)#define MAX32\_DMA\_SLOT\_I2C0\_RX 0x07U

[ 17](max32662__dma_8h.md#ad589918d7435fc9c74021d5ae1e5d5ca)#define MAX32\_DMA\_SLOT\_I2C1\_RX 0x08U

[ 18](max32662__dma_8h.md#adf6d862b295bc34de7b3c8334b6ad306)#define MAX32\_DMA\_SLOT\_ADC 0x09U

[ 19](max32662__dma_8h.md#a56646e3053fc8a76ef214adbd0ba5921)#define MAX32\_DMA\_SLOT\_I2S\_RX 0x1EU

[ 20](max32662__dma_8h.md#a26f06363fd4639eaee5668450adaa1c3)#define MAX32\_DMA\_SLOT\_SPI0\_TX 0x21U

[ 21](max32662__dma_8h.md#aa85105348eeb191fd2799d645aacc575)#define MAX32\_DMA\_SLOT\_SPI1\_TX 0x22U

[ 22](max32662__dma_8h.md#a009a7e71c5fed2afa3d8907411c454e3)#define MAX32\_DMA\_SLOT\_UART0\_TX 0x24U

[ 23](max32662__dma_8h.md#a5f8ba237de646a46c5584fe28fd05afa)#define MAX32\_DMA\_SLOT\_UART1\_TX 0x25U

[ 24](max32662__dma_8h.md#a57149d49c6a445849a8395ac76128ccc)#define MAX32\_DMA\_SLOT\_CAN\_TX 0x26U

[ 25](max32662__dma_8h.md#aee43cae318d6b70f9f2a7e6bd77e02dd)#define MAX32\_DMA\_SLOT\_I2C0\_TX 0x27U

[ 26](max32662__dma_8h.md#a7a8535c65c0e3d286c0d26824ed37b0c)#define MAX32\_DMA\_SLOT\_I2C1\_TX 0x28U

[ 27](max32662__dma_8h.md#a6ac25728509e7319f256fd02bb53f208)#define MAX32\_DMA\_SLOT\_I2S\_TX 0x3EU

28

29#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_DMA\_MAX32662\_DMA\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [max32662\_dma.h](max32662__dma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
