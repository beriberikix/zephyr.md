---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/max32690__dma_8h_source.html
original_path: doxygen/html/max32690__dma_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

max32690\_dma.h

[Go to the documentation of this file.](max32690__dma_8h.md)

1/\*

2 \* Copyright (c) 2023 Analog Devices, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_DMA\_MAX32690\_DMA\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_DMA\_MAX32690\_DMA\_H\_

9

[ 10](max32690__dma_8h.md#a6e1ea6d5650545947928c83c71776c04)#define MAX32\_DMA\_SLOT\_MEMTOMEM 0x00U

[ 11](max32690__dma_8h.md#ac505ee888a8cb52b03ac733a9b650097)#define MAX32\_DMA\_SLOT\_SPI0\_RX 0x01U

[ 12](max32690__dma_8h.md#a0df8d71978ba7b5c5b6766c1cf28d00c)#define MAX32\_DMA\_SLOT\_SPI1\_RX 0x02U

[ 13](max32690__dma_8h.md#afedfa23ede3c9817b4952311c3458ba0)#define MAX32\_DMA\_SLOT\_SPI2\_RX 0x03U

[ 14](max32690__dma_8h.md#ac823471b99eda7df54c2fce6eb923e96)#define MAX32\_DMA\_SLOT\_UART0\_RX 0x04U

[ 15](max32690__dma_8h.md#ab7e79c3fa976243daa7ef5880f20fade)#define MAX32\_DMA\_SLOT\_UART1\_RX 0x05U

[ 16](max32690__dma_8h.md#a05fffce0b3b48f9170223932559b8d41)#define MAX32\_DMA\_SLOT\_CAN0\_RX 0x06U

[ 17](max32690__dma_8h.md#a207563fbc9fb4110d78f92b1d2d4c423)#define MAX32\_DMA\_SLOT\_I2C0\_RX 0x07U

[ 18](max32690__dma_8h.md#ad589918d7435fc9c74021d5ae1e5d5ca)#define MAX32\_DMA\_SLOT\_I2C1\_RX 0x08U

[ 19](max32690__dma_8h.md#adf6d862b295bc34de7b3c8334b6ad306)#define MAX32\_DMA\_SLOT\_ADC 0x09U

[ 20](max32690__dma_8h.md#a640bd0651d35157bdd822b11e8b23274)#define MAX32\_DMA\_SLOT\_I2C2\_RX 0x0AU

[ 21](max32690__dma_8h.md#ac82aa4f9ad49e656963580bf297dcd26)#define MAX32\_DMA\_SLOT\_UART2\_RX 0x0EU

[ 22](max32690__dma_8h.md#a5314a7ed922831a39b6a025b4392ad06)#define MAX32\_DMA\_SLOT\_SPI3\_RX 0x0FU

[ 23](max32690__dma_8h.md#a891ca72eda14d6331e78015f120dbb6a)#define MAX32\_DMA\_SLOT\_SPI4\_RX 0x10U

[ 24](max32690__dma_8h.md#a03f1f3ae4ed1f1338fd04fa067ad75e8)#define MAX32\_DMA\_SLOT\_USB1\_IN 0x11U

[ 25](max32690__dma_8h.md#a64ae56f1a1e74e8b5215392833d5b32f)#define MAX32\_DMA\_SLOT\_USB2\_IN 0x12U

[ 26](max32690__dma_8h.md#af408853da19bdfc6348ebfca9f868e35)#define MAX32\_DMA\_SLOT\_USB3\_IN 0x13U

[ 27](max32690__dma_8h.md#a47f54cb1d33b89ee58e4bf11ed48a099)#define MAX32\_DMA\_SLOT\_USB4\_IN 0x14U

[ 28](max32690__dma_8h.md#a7e2ae2470bd7133deba81786fa3f8112)#define MAX32\_DMA\_SLOT\_USB5\_IN 0x15U

[ 29](max32690__dma_8h.md#a4c558e41238658fa93a7a1b94812ffe3)#define MAX32\_DMA\_SLOT\_USB6\_IN 0x16U

[ 30](max32690__dma_8h.md#a856fece9c57666f58065ed62a8a4d895)#define MAX32\_DMA\_SLOT\_USB7\_IN 0x17U

[ 31](max32690__dma_8h.md#a1539f829df18cf805b6e0dd904f67cba)#define MAX32\_DMA\_SLOT\_USB8\_IN 0x18U

[ 32](max32690__dma_8h.md#a0f6099d8756b2752fd1b61f3367328be)#define MAX32\_DMA\_SLOT\_USB9\_IN 0x19U

[ 33](max32690__dma_8h.md#ae4b1142f08cd54821757bca8c049ea52)#define MAX32\_DMA\_SLOT\_USB10\_IN 0x1AU

[ 34](max32690__dma_8h.md#a9228600145736a5a2e6c68212207f70a)#define MAX32\_DMA\_SLOT\_USB11\_IN 0x1BU

[ 35](max32690__dma_8h.md#a836e5ca3823f71e408ec8807c5bf1156)#define MAX32\_DMA\_SLOT\_UART3\_RX 0x1CU

[ 36](max32690__dma_8h.md#a56646e3053fc8a76ef214adbd0ba5921)#define MAX32\_DMA\_SLOT\_I2S\_RX 0x1EU

[ 37](max32690__dma_8h.md#a8e50669ec54878ab00ad6eb848506d55)#define MAX32\_DMA\_SLOT\_CAN1\_RX 0x1FU

[ 38](max32690__dma_8h.md#a26f06363fd4639eaee5668450adaa1c3)#define MAX32\_DMA\_SLOT\_SPI0\_TX 0x21U

[ 39](max32690__dma_8h.md#aa85105348eeb191fd2799d645aacc575)#define MAX32\_DMA\_SLOT\_SPI1\_TX 0x22U

[ 40](max32690__dma_8h.md#a88067802f3a790268fcca78597551d80)#define MAX32\_DMA\_SLOT\_SPI2\_TX 0x23U

[ 41](max32690__dma_8h.md#a009a7e71c5fed2afa3d8907411c454e3)#define MAX32\_DMA\_SLOT\_UART0\_TX 0x24U

[ 42](max32690__dma_8h.md#a5f8ba237de646a46c5584fe28fd05afa)#define MAX32\_DMA\_SLOT\_UART1\_TX 0x25U

[ 43](max32690__dma_8h.md#ab6e6d113ddcf94477524929baec50efe)#define MAX32\_DMA\_SLOT\_CAN0\_TX 0x26U

[ 44](max32690__dma_8h.md#aee43cae318d6b70f9f2a7e6bd77e02dd)#define MAX32\_DMA\_SLOT\_I2C0\_TX 0x27U

[ 45](max32690__dma_8h.md#a7a8535c65c0e3d286c0d26824ed37b0c)#define MAX32\_DMA\_SLOT\_I2C1\_TX 0x28U

[ 46](max32690__dma_8h.md#a8ae2d2fe05f0b1caea4b5c127fac3e11)#define MAX32\_DMA\_SLOT\_I2C2\_TX 0x2AU

[ 47](max32690__dma_8h.md#af2c822f39971c7bc6b8d58df6d139433)#define MAX32\_DMA\_SLOT\_UART2\_TX 0x2EU

[ 48](max32690__dma_8h.md#a051094c0cb0cfc3bd513cea484046601)#define MAX32\_DMA\_SLOT\_SPI3\_TX 0x2FU

[ 49](max32690__dma_8h.md#a814c56475fe8b6ce2a6b6817032f2a87)#define MAX32\_DMA\_SLOT\_SPI4\_TX 0x30U

[ 50](max32690__dma_8h.md#ab82dc978e78da71129ec21b08dc4c62f)#define MAX32\_DMA\_SLOT\_USB1\_OUT 0x31U

[ 51](max32690__dma_8h.md#ad3f08940af7b9908c4376e87f73a4646)#define MAX32\_DMA\_SLOT\_USB2\_OUT 0x32U

[ 52](max32690__dma_8h.md#affcdb959a2ce310a5745d623443ecf39)#define MAX32\_DMA\_SLOT\_USB3\_OUT 0x33U

[ 53](max32690__dma_8h.md#aa10e5db19758fa2983c8e5c8dec1728e)#define MAX32\_DMA\_SLOT\_USB4\_OUT 0x34U

[ 54](max32690__dma_8h.md#a3fdbec2e3910715b0505443a761d0199)#define MAX32\_DMA\_SLOT\_USB5\_OUT 0x35U

[ 55](max32690__dma_8h.md#aaafe5f2dd2de43fd0df91383fef80888)#define MAX32\_DMA\_SLOT\_USB6\_OUT 0x36U

[ 56](max32690__dma_8h.md#a7f83f6b1831f8d611d89bba5b85e3078)#define MAX32\_DMA\_SLOT\_USB7\_OUT 0x37U

[ 57](max32690__dma_8h.md#a2c6fc053f7550264605e8e49a07ff4ee)#define MAX32\_DMA\_SLOT\_USB8\_OUT 0x38U

[ 58](max32690__dma_8h.md#a85621d1cac930edf18367e3230514174)#define MAX32\_DMA\_SLOT\_USB9\_OUT 0x39U

[ 59](max32690__dma_8h.md#a00aaf2c238cb9fa36b9ebb684fb0f4e9)#define MAX32\_DMA\_SLOT\_USB10\_OUT 0x3AU

[ 60](max32690__dma_8h.md#abf6ee8392db788088caec873d6fe6ac7)#define MAX32\_DMA\_SLOT\_USB11\_OUT 0x3BU

[ 61](max32690__dma_8h.md#a7dbddaa644cdf31bc19cbcf638bec5a3)#define MAX32\_DMA\_SLOT\_UART3\_TX 0x3CU

[ 62](max32690__dma_8h.md#a6ac25728509e7319f256fd02bb53f208)#define MAX32\_DMA\_SLOT\_I2S\_TX 0x3EU

[ 63](max32690__dma_8h.md#a39e447dd29c09caef38a8b516a432e9e)#define MAX32\_DMA\_SLOT\_CAN1\_TX 0x3FU

64

65#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_DMA\_MAX32690\_DMA\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [max32690\_dma.h](max32690__dma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
