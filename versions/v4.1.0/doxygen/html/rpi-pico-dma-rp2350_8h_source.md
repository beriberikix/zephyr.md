---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/rpi-pico-dma-rp2350_8h_source.html
original_path: doxygen/html/rpi-pico-dma-rp2350_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rpi-pico-dma-rp2350.h

[Go to the documentation of this file.](rpi-pico-dma-rp2350_8h.md)

1/\*

2 \* Copyright (c) 2024 Manuel Aebischer <manuel.aebischer@belden.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RPI\_PICO\_DMA\_RP2350\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RPI\_PICO\_DMA\_RP2350\_H\_

9

10#include "[rpi-pico-dma-common.h](rpi-pico-dma-common_8h.md)"

11

[ 12](rpi-pico-dma-rp2350_8h.md#a69ec0b9fa3b672e9820e413ab0386d83)#define RPI\_PICO\_DMA\_SLOT\_PIO2\_TX0 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x10)

[ 13](rpi-pico-dma-rp2350_8h.md#aa7a1cfc1210a846845ae8e60bb26fa3b)#define RPI\_PICO\_DMA\_SLOT\_PIO2\_TX1 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x11)

[ 14](rpi-pico-dma-rp2350_8h.md#a238f716e6a07cb637f2827f9d4563648)#define RPI\_PICO\_DMA\_SLOT\_PIO2\_TX2 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x12)

[ 15](rpi-pico-dma-rp2350_8h.md#a3c48bf2318bed841ab3a0f820294ad17)#define RPI\_PICO\_DMA\_SLOT\_PIO2\_TX3 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x13)

[ 16](rpi-pico-dma-rp2350_8h.md#a9eecd7e6ad0c93017392469185c7e2cf)#define RPI\_PICO\_DMA\_SLOT\_PIO2\_RX0 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x14)

[ 17](rpi-pico-dma-rp2350_8h.md#adf9059e13851b00b6fb39e8b2223e9cc)#define RPI\_PICO\_DMA\_SLOT\_PIO2\_RX1 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x15)

[ 18](rpi-pico-dma-rp2350_8h.md#ac1a9787d5fdbfa252a9db11571367f76)#define RPI\_PICO\_DMA\_SLOT\_PIO2\_RX2 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x16)

[ 19](rpi-pico-dma-rp2350_8h.md#a5009bef8c4d185efcfda599f9ce36101)#define RPI\_PICO\_DMA\_SLOT\_PIO2\_RX3 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x17)

[ 20](rpi-pico-dma-rp2350_8h.md#ae18eed6d9f3a59b17d98e1d327d67cf7)#define RPI\_PICO\_DMA\_SLOT\_SPI0\_TX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x18)

[ 21](rpi-pico-dma-rp2350_8h.md#aa955cbbf46c4c22ad7a57471aeed4344)#define RPI\_PICO\_DMA\_SLOT\_SPI0\_RX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x19)

[ 22](rpi-pico-dma-rp2350_8h.md#a0076112cb2bb0ac30b53ba51b67cde13)#define RPI\_PICO\_DMA\_SLOT\_SPI1\_TX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x1A)

[ 23](rpi-pico-dma-rp2350_8h.md#a11b34c896fbb7993712f2a6228f0f470)#define RPI\_PICO\_DMA\_SLOT\_SPI1\_RX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x1B)

[ 24](rpi-pico-dma-rp2350_8h.md#a8e4849d94891581e54c20f1ad3053e61)#define RPI\_PICO\_DMA\_SLOT\_UART0\_TX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x1C)

[ 25](rpi-pico-dma-rp2350_8h.md#a6c9dbf9ae4a775350dba0192d2d22ece)#define RPI\_PICO\_DMA\_SLOT\_UART0\_RX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x1D)

[ 26](rpi-pico-dma-rp2350_8h.md#ae3b608078bb7b0076565d6ba01b7f2db)#define RPI\_PICO\_DMA\_SLOT\_UART1\_TX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x1E)

[ 27](rpi-pico-dma-rp2350_8h.md#a867620802abfb1ea68f4de34bd9220c8)#define RPI\_PICO\_DMA\_SLOT\_UART1\_RX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x1F)

[ 28](rpi-pico-dma-rp2350_8h.md#aaf7f3a66c0e4bd1ba533c926e088bb72)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP0 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x20)

[ 29](rpi-pico-dma-rp2350_8h.md#a4c4d3ebb5cb30a4af4289e72c74ac705)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP1 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x21)

[ 30](rpi-pico-dma-rp2350_8h.md#a6807669224a777d8b8342d5a59b87370)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP2 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x22)

[ 31](rpi-pico-dma-rp2350_8h.md#a69039f5a94f8f30f46e488df743d8623)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP3 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x23)

[ 32](rpi-pico-dma-rp2350_8h.md#a16432ea7735d3d2b46696eb42c3a5a78)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP4 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x24)

[ 33](rpi-pico-dma-rp2350_8h.md#a262317a40c039af688969d08b734cb30)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP5 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x25)

[ 34](rpi-pico-dma-rp2350_8h.md#acc46df2f8f0ba68e155eb9dfb78d316b)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP6 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x26)

[ 35](rpi-pico-dma-rp2350_8h.md#acd268446715055b789d0b32527eaec18)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP7 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x27)

[ 36](rpi-pico-dma-rp2350_8h.md#a1d3bf23bd024945572ab68dc46ffec61)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP8 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x28)

[ 37](rpi-pico-dma-rp2350_8h.md#afcb9ae0553626bc49bacd088be038606)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP9 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x29)

[ 38](rpi-pico-dma-rp2350_8h.md#a5ee10d7e719551ee3b87d09ca2d28cf9)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP10 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x2A)

[ 39](rpi-pico-dma-rp2350_8h.md#a9646f5712c2f1e33b4f73e75da31b70b)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP11 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x2B)

[ 40](rpi-pico-dma-rp2350_8h.md#aeb3507fc3e3416b7bedfaebbfe8ba980)#define RPI\_PICO\_DMA\_SLOT\_I2C0\_TX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x2C)

[ 41](rpi-pico-dma-rp2350_8h.md#a22bdae09d66f57f0b2f26e6bd6b36f31)#define RPI\_PICO\_DMA\_SLOT\_I2C0\_RX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x2D)

[ 42](rpi-pico-dma-rp2350_8h.md#afa10629c69c563ca959fe692f40bc5bb)#define RPI\_PICO\_DMA\_SLOT\_I2C1\_TX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x2E)

[ 43](rpi-pico-dma-rp2350_8h.md#a0f6717d3026d1c19c30e84bd4f91511b)#define RPI\_PICO\_DMA\_SLOT\_I2C1\_RX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x2F)

[ 44](rpi-pico-dma-rp2350_8h.md#ab9e20d2a674fa5d1947c01a5dc2fb359)#define RPI\_PICO\_DMA\_SLOT\_ADC RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x30)

[ 45](rpi-pico-dma-rp2350_8h.md#a831f08fba56848125d1e8773c05ac588)#define RPI\_PICO\_DMA\_SLOT\_XIP\_STREAM RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x31)

[ 46](rpi-pico-dma-rp2350_8h.md#ab6a325be6e26d5b2dbd97fb426da5b25)#define RPI\_PICO\_DMA\_SLOT\_XIP\_QMITX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x32)

[ 47](rpi-pico-dma-rp2350_8h.md#ac9b29d9f6c4923fb16f8e02b2901e7ec)#define RPI\_PICO\_DMA\_SLOT\_XIP\_QMIRX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x33)

[ 48](rpi-pico-dma-rp2350_8h.md#a5ae6d61fc1edc6a2c1f00d8a88f78e3f)#define RPI\_PICO\_DMA\_SLOT\_HSTX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x34)

[ 49](rpi-pico-dma-rp2350_8h.md#ab95e32efed232a4fb5a2e6b9e6352ce2)#define RPI\_PICO\_DMA\_SLOT\_CORESIGHT RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x35)

[ 50](rpi-pico-dma-rp2350_8h.md#a43a7b803f57744f3da8aa0d07d2cd8ec)#define RPI\_PICO\_DMA\_SLOT\_SHA256 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x36)

51

52#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RPI\_PICO\_DMA\_RP2350\_H\_ \*/

[rpi-pico-dma-common.h](rpi-pico-dma-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [rpi-pico-dma-rp2350.h](rpi-pico-dma-rp2350_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
