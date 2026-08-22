---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/max32650__dma_8h_source.html
original_path: doxygen/html/max32650__dma_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

max32650\_dma.h

[Go to the documentation of this file.](max32650__dma_8h.md)

1/\*

2 \* Copyright (c) 2025 Analog Devices, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_DMA\_MAX32650\_DMA\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_DMA\_MAX32650\_DMA\_H\_

8

[ 9](max32650__dma_8h.md#a6e1ea6d5650545947928c83c71776c04)#define MAX32\_DMA\_SLOT\_MEMTOMEM 0x00U

[ 10](max32650__dma_8h.md#ac505ee888a8cb52b03ac733a9b650097)#define MAX32\_DMA\_SLOT\_SPI0\_RX 0x01U

[ 11](max32650__dma_8h.md#a0df8d71978ba7b5c5b6766c1cf28d00c)#define MAX32\_DMA\_SLOT\_SPI1\_RX 0x02U

[ 12](max32650__dma_8h.md#afedfa23ede3c9817b4952311c3458ba0)#define MAX32\_DMA\_SLOT\_SPI2\_RX 0x03U

[ 13](max32650__dma_8h.md#ac823471b99eda7df54c2fce6eb923e96)#define MAX32\_DMA\_SLOT\_UART0\_RX 0x04U

[ 14](max32650__dma_8h.md#ab7e79c3fa976243daa7ef5880f20fade)#define MAX32\_DMA\_SLOT\_UART1\_RX 0x05U

[ 15](max32650__dma_8h.md#a207563fbc9fb4110d78f92b1d2d4c423)#define MAX32\_DMA\_SLOT\_I2C0\_RX 0x07U

[ 16](max32650__dma_8h.md#ad589918d7435fc9c74021d5ae1e5d5ca)#define MAX32\_DMA\_SLOT\_I2C1\_RX 0x08U

[ 17](max32650__dma_8h.md#adf6d862b295bc34de7b3c8334b6ad306)#define MAX32\_DMA\_SLOT\_ADC 0x09U

[ 18](max32650__dma_8h.md#ac82aa4f9ad49e656963580bf297dcd26)#define MAX32\_DMA\_SLOT\_UART2\_RX 0x0EU

[ 19](max32650__dma_8h.md#a5314a7ed922831a39b6a025b4392ad06)#define MAX32\_DMA\_SLOT\_SPI3\_RX 0x0FU

[ 20](max32650__dma_8h.md#a85a173b66c3ebc2768b5a8ad3514a83a)#define MAX32\_DMA\_SLOT\_SPI\_MSS\_RX 0x10U

[ 21](max32650__dma_8h.md#a0b75476dc07fbc9ec8ffb2e1e3a81981)#define MAX32\_DMA\_SLOT\_USB\_RX1 0x11U

[ 22](max32650__dma_8h.md#a740ff452ee6d87e8294c20202e5a5eff)#define MAX32\_DMA\_SLOT\_USB\_RX2 0x12U

[ 23](max32650__dma_8h.md#adce27b072546e820614976131f6e107a)#define MAX32\_DMA\_SLOT\_USB\_RX3 0x13U

[ 24](max32650__dma_8h.md#a406cf4dd9f03849ae40057de5e7e1f01)#define MAX32\_DMA\_SLOT\_USB\_RX4 0x14U

[ 25](max32650__dma_8h.md#a034c7228b0e23ef8d8df08f084b960ce)#define MAX32\_DMA\_SLOT\_USB\_RX5 0x15U

[ 26](max32650__dma_8h.md#a2d38a4656f34282ab3d2766ee1a28429)#define MAX32\_DMA\_SLOT\_USB\_RX6 0x16U

[ 27](max32650__dma_8h.md#a2f2e9d3c91ec5dda76f66099ff536725)#define MAX32\_DMA\_SLOT\_USB\_RX7 0x17U

[ 28](max32650__dma_8h.md#a44c9abf42bedbf7a2459493a9a555b12)#define MAX32\_DMA\_SLOT\_USB\_RX8 0x18U

[ 29](max32650__dma_8h.md#a41536d9831888832f4952fdf422864fa)#define MAX32\_DMA\_SLOT\_USB\_RX9 0x19U

[ 30](max32650__dma_8h.md#a0c7485b0d883b3dab77565daa0bb4a74)#define MAX32\_DMA\_SLOT\_USB\_RX10 0x1AU

[ 31](max32650__dma_8h.md#a1cd31446fe267673688df59af1f6f07d)#define MAX32\_DMA\_SLOT\_USB\_RX11 0x1BU

[ 32](max32650__dma_8h.md#a26f06363fd4639eaee5668450adaa1c3)#define MAX32\_DMA\_SLOT\_SPI0\_TX 0x21U

[ 33](max32650__dma_8h.md#aa85105348eeb191fd2799d645aacc575)#define MAX32\_DMA\_SLOT\_SPI1\_TX 0x22U

[ 34](max32650__dma_8h.md#a88067802f3a790268fcca78597551d80)#define MAX32\_DMA\_SLOT\_SPI2\_TX 0x23U

[ 35](max32650__dma_8h.md#a009a7e71c5fed2afa3d8907411c454e3)#define MAX32\_DMA\_SLOT\_UART0\_TX 0x24U

[ 36](max32650__dma_8h.md#a5f8ba237de646a46c5584fe28fd05afa)#define MAX32\_DMA\_SLOT\_UART1\_TX 0x25U

[ 37](max32650__dma_8h.md#aee43cae318d6b70f9f2a7e6bd77e02dd)#define MAX32\_DMA\_SLOT\_I2C0\_TX 0x27U

[ 38](max32650__dma_8h.md#a7a8535c65c0e3d286c0d26824ed37b0c)#define MAX32\_DMA\_SLOT\_I2C1\_TX 0x28U

[ 39](max32650__dma_8h.md#af2c822f39971c7bc6b8d58df6d139433)#define MAX32\_DMA\_SLOT\_UART2\_TX 0x2EU

[ 40](max32650__dma_8h.md#a051094c0cb0cfc3bd513cea484046601)#define MAX32\_DMA\_SLOT\_SPI3\_TX 0x2FU

[ 41](max32650__dma_8h.md#ade3c6853ef7a5690d886903978b414f1)#define MAX32\_DMA\_SLOT\_SPI\_MSS\_TX 0x30U

[ 42](max32650__dma_8h.md#a0a3828eb499d5fa83acec4b4d0bb3f01)#define MAX32\_DMA\_SLOT\_USB\_TX1 0x31U

[ 43](max32650__dma_8h.md#a7c7e6605fecf725fd9ba2fe6145a6038)#define MAX32\_DMA\_SLOT\_USB\_TX2 0x32U

[ 44](max32650__dma_8h.md#a1d3020098dad909bc83ec30b25a6dcee)#define MAX32\_DMA\_SLOT\_USB\_TX3 0x33U

[ 45](max32650__dma_8h.md#a11f32857847be0b0c4c71b8bd98f0227)#define MAX32\_DMA\_SLOT\_USB\_TX4 0x34U

[ 46](max32650__dma_8h.md#ab6ff1b56cffd6c8f210db5fa2c67e862)#define MAX32\_DMA\_SLOT\_USB\_TX5 0x35U

[ 47](max32650__dma_8h.md#aeb107c1e11d72e3cccc403c214ec1714)#define MAX32\_DMA\_SLOT\_USB\_TX6 0x36U

[ 48](max32650__dma_8h.md#a21a7cec8333267f2bae73054500b2453)#define MAX32\_DMA\_SLOT\_USB\_TX7 0x37U

[ 49](max32650__dma_8h.md#a273d7a9da9f57c5d8f3bdfbea2fd17e7)#define MAX32\_DMA\_SLOT\_USB\_TX8 0x38U

[ 50](max32650__dma_8h.md#a7c323924a5cf297987b54211c2591283)#define MAX32\_DMA\_SLOT\_USB\_TX9 0x39U

[ 51](max32650__dma_8h.md#ac64dc00771e5d66fe9946648958208dc)#define MAX32\_DMA\_SLOT\_USB\_TX10 0x3AU

[ 52](max32650__dma_8h.md#a4643edd680c15f931e8185b7a216c1e4)#define MAX32\_DMA\_SLOT\_USB\_TX11 0x3BU

53

54#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_DMA\_MAX32650\_DMA\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [max32650\_dma.h](max32650__dma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
