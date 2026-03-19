---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/rpi-pico-dma-rp2040_8h_source.html
original_path: doxygen/html/rpi-pico-dma-rp2040_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rpi-pico-dma-rp2040.h

[Go to the documentation of this file.](rpi-pico-dma-rp2040_8h.md)

1/\*

2 \* Copyright (c) 2023 TOKITA Hiroshi <tokita.hiroshi@fujitsu.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RPI\_PICO\_DMA\_RP2040\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RPI\_PICO\_DMA\_RP2040\_H\_

9

10#include "[rpi-pico-dma-common.h](rpi-pico-dma-common_8h.md)"

11

[ 12](rpi-pico-dma-rp2040_8h.md#ae18eed6d9f3a59b17d98e1d327d67cf7)#define RPI\_PICO\_DMA\_SLOT\_SPI0\_TX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x10)

[ 13](rpi-pico-dma-rp2040_8h.md#aa955cbbf46c4c22ad7a57471aeed4344)#define RPI\_PICO\_DMA\_SLOT\_SPI0\_RX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x11)

[ 14](rpi-pico-dma-rp2040_8h.md#a0076112cb2bb0ac30b53ba51b67cde13)#define RPI\_PICO\_DMA\_SLOT\_SPI1\_TX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x12)

[ 15](rpi-pico-dma-rp2040_8h.md#a11b34c896fbb7993712f2a6228f0f470)#define RPI\_PICO\_DMA\_SLOT\_SPI1\_RX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x13)

[ 16](rpi-pico-dma-rp2040_8h.md#a8e4849d94891581e54c20f1ad3053e61)#define RPI\_PICO\_DMA\_SLOT\_UART0\_TX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x14)

[ 17](rpi-pico-dma-rp2040_8h.md#a6c9dbf9ae4a775350dba0192d2d22ece)#define RPI\_PICO\_DMA\_SLOT\_UART0\_RX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x15)

[ 18](rpi-pico-dma-rp2040_8h.md#ae3b608078bb7b0076565d6ba01b7f2db)#define RPI\_PICO\_DMA\_SLOT\_UART1\_TX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x16)

[ 19](rpi-pico-dma-rp2040_8h.md#a867620802abfb1ea68f4de34bd9220c8)#define RPI\_PICO\_DMA\_SLOT\_UART1\_RX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x17)

[ 20](rpi-pico-dma-rp2040_8h.md#aaf7f3a66c0e4bd1ba533c926e088bb72)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP0 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x18)

[ 21](rpi-pico-dma-rp2040_8h.md#a4c4d3ebb5cb30a4af4289e72c74ac705)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP1 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x19)

[ 22](rpi-pico-dma-rp2040_8h.md#a6807669224a777d8b8342d5a59b87370)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP2 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x1A)

[ 23](rpi-pico-dma-rp2040_8h.md#a69039f5a94f8f30f46e488df743d8623)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP3 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x1B)

[ 24](rpi-pico-dma-rp2040_8h.md#a16432ea7735d3d2b46696eb42c3a5a78)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP4 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x1C)

[ 25](rpi-pico-dma-rp2040_8h.md#a262317a40c039af688969d08b734cb30)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP5 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x1D)

[ 26](rpi-pico-dma-rp2040_8h.md#acc46df2f8f0ba68e155eb9dfb78d316b)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP6 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x1E)

[ 27](rpi-pico-dma-rp2040_8h.md#acd268446715055b789d0b32527eaec18)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP7 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x1F)

[ 28](rpi-pico-dma-rp2040_8h.md#aeb3507fc3e3416b7bedfaebbfe8ba980)#define RPI\_PICO\_DMA\_SLOT\_I2C0\_TX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x30)

[ 29](rpi-pico-dma-rp2040_8h.md#a22bdae09d66f57f0b2f26e6bd6b36f31)#define RPI\_PICO\_DMA\_SLOT\_I2C0\_RX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x31)

[ 30](rpi-pico-dma-rp2040_8h.md#afa10629c69c563ca959fe692f40bc5bb)#define RPI\_PICO\_DMA\_SLOT\_I2C1\_TX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x32)

[ 31](rpi-pico-dma-rp2040_8h.md#a0f6717d3026d1c19c30e84bd4f91511b)#define RPI\_PICO\_DMA\_SLOT\_I2C1\_RX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x33)

[ 32](rpi-pico-dma-rp2040_8h.md#ab9e20d2a674fa5d1947c01a5dc2fb359)#define RPI\_PICO\_DMA\_SLOT\_ADC RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x34)

[ 33](rpi-pico-dma-rp2040_8h.md#a831f08fba56848125d1e8773c05ac588)#define RPI\_PICO\_DMA\_SLOT\_XIP\_STREAM RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x35)

[ 34](rpi-pico-dma-rp2040_8h.md#a01f1ea52277e47bff8c3d76d6da7dab3)#define RPI\_PICO\_DMA\_SLOT\_XIP\_SSITX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x36)

[ 35](rpi-pico-dma-rp2040_8h.md#abdb688be5a52ddc5c3aacf2048096987)#define RPI\_PICO\_DMA\_SLOT\_XIP\_SSIRX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x37)

36

37#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RPI\_PICO\_DMA\_RP2040\_H\_ \*/

[rpi-pico-dma-common.h](rpi-pico-dma-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [rpi-pico-dma-rp2040.h](rpi-pico-dma-rp2040_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
