---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/rpi__pico__dma_8h_source.html
original_path: doxygen/html/rpi__pico__dma_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rpi\_pico\_dma.h

[Go to the documentation of this file.](rpi__pico__dma_8h.md)

1/\*

2 \* Copyright (c) 2023 TOKITA Hiroshi <tokita.hiroshi@fujitsu.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RPI\_PICO\_DMA\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RPI\_PICO\_DMA\_H\_

9

10/\*

11 \* Use lower 6-bit of inverted DREQ value for `slot` cell.

12 \* Need to be able to work for memory-to-memory transfer

13 \* with zero, which is the default value.

14 \*/

[ 15](rpi__pico__dma_8h.md#af17a4ab6d1b744cb7ba78185681f464b)#define RPI\_PICO\_DMA\_SLOT\_TO\_DREQ(s) (~(s)&0x3F)

[ 16](rpi__pico__dma_8h.md#a108c9650b4eb398c9994d7c1683beaa8)#define RPI\_PICO\_DMA\_DREQ\_TO\_SLOT RPI\_PICO\_DMA\_SLOT\_TO\_DREQ

17

[ 18](rpi__pico__dma_8h.md#ab4efb501d7d6acf7c4e320a992a736c9)#define RPI\_PICO\_DMA\_SLOT\_PIO0\_TX0 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x00)

[ 19](rpi__pico__dma_8h.md#ac83bcbc6b3716d947051d785f60447c1)#define RPI\_PICO\_DMA\_SLOT\_PIO0\_TX1 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x01)

[ 20](rpi__pico__dma_8h.md#ad2452d29f952c828fc38036d3fc8f7c7)#define RPI\_PICO\_DMA\_SLOT\_PIO0\_TX2 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x02)

[ 21](rpi__pico__dma_8h.md#a3be36155cb5c9faff83951e46e1ce6eb)#define RPI\_PICO\_DMA\_SLOT\_PIO0\_TX3 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x03)

[ 22](rpi__pico__dma_8h.md#a4931c164398407d3365d600d17110f95)#define RPI\_PICO\_DMA\_SLOT\_PIO0\_RX0 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x04)

[ 23](rpi__pico__dma_8h.md#a84583ff2852ec17e709f44cfe85a21d1)#define RPI\_PICO\_DMA\_SLOT\_PIO0\_RX1 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x05)

[ 24](rpi__pico__dma_8h.md#a7a30cab865790b3ff4c873cec1ae39a4)#define RPI\_PICO\_DMA\_SLOT\_PIO0\_RX2 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x06)

[ 25](rpi__pico__dma_8h.md#a131cdd1941010a43bebcda6fffd98016)#define RPI\_PICO\_DMA\_SLOT\_PIO0\_RX3 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x07)

[ 26](rpi__pico__dma_8h.md#a17f1642461493cde7e832a1ab78d9f69)#define RPI\_PICO\_DMA\_SLOT\_PIO1\_TX0 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x08)

[ 27](rpi__pico__dma_8h.md#a7a19561e334931146de9a56ce3214680)#define RPI\_PICO\_DMA\_SLOT\_PIO1\_TX1 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x09)

[ 28](rpi__pico__dma_8h.md#ae6f04b3ecc7adfa5bb4e070f6cc29780)#define RPI\_PICO\_DMA\_SLOT\_PIO1\_TX2 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x0A)

[ 29](rpi__pico__dma_8h.md#ab39ac333962fe0debca583061ba1b6cb)#define RPI\_PICO\_DMA\_SLOT\_PIO1\_TX3 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x0B)

[ 30](rpi__pico__dma_8h.md#a7eaaa6b0e6f80021364a66fd75450c0d)#define RPI\_PICO\_DMA\_SLOT\_PIO1\_RX0 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x0C)

[ 31](rpi__pico__dma_8h.md#a9963f9b698a5ffde3e3bcf9b4b43ed22)#define RPI\_PICO\_DMA\_SLOT\_PIO1\_RX1 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x0D)

[ 32](rpi__pico__dma_8h.md#ad1a63c332b00cf4442907a3a11d155d1)#define RPI\_PICO\_DMA\_SLOT\_PIO1\_RX2 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x0E)

[ 33](rpi__pico__dma_8h.md#a07eab28aade43838cf5580e0c0ea3bde)#define RPI\_PICO\_DMA\_SLOT\_PIO1\_RX3 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x0F)

[ 34](rpi__pico__dma_8h.md#ae18eed6d9f3a59b17d98e1d327d67cf7)#define RPI\_PICO\_DMA\_SLOT\_SPI0\_TX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x10)

[ 35](rpi__pico__dma_8h.md#aa955cbbf46c4c22ad7a57471aeed4344)#define RPI\_PICO\_DMA\_SLOT\_SPI0\_RX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x11)

[ 36](rpi__pico__dma_8h.md#a0076112cb2bb0ac30b53ba51b67cde13)#define RPI\_PICO\_DMA\_SLOT\_SPI1\_TX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x12)

[ 37](rpi__pico__dma_8h.md#a11b34c896fbb7993712f2a6228f0f470)#define RPI\_PICO\_DMA\_SLOT\_SPI1\_RX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x13)

[ 38](rpi__pico__dma_8h.md#a8e4849d94891581e54c20f1ad3053e61)#define RPI\_PICO\_DMA\_SLOT\_UART0\_TX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x14)

[ 39](rpi__pico__dma_8h.md#a6c9dbf9ae4a775350dba0192d2d22ece)#define RPI\_PICO\_DMA\_SLOT\_UART0\_RX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x15)

[ 40](rpi__pico__dma_8h.md#ae3b608078bb7b0076565d6ba01b7f2db)#define RPI\_PICO\_DMA\_SLOT\_UART1\_TX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x16)

[ 41](rpi__pico__dma_8h.md#a867620802abfb1ea68f4de34bd9220c8)#define RPI\_PICO\_DMA\_SLOT\_UART1\_RX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x17)

[ 42](rpi__pico__dma_8h.md#aaf7f3a66c0e4bd1ba533c926e088bb72)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP0 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x18)

[ 43](rpi__pico__dma_8h.md#a4c4d3ebb5cb30a4af4289e72c74ac705)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP1 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x19)

[ 44](rpi__pico__dma_8h.md#a6807669224a777d8b8342d5a59b87370)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP2 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x1A)

[ 45](rpi__pico__dma_8h.md#a69039f5a94f8f30f46e488df743d8623)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP3 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x1B)

[ 46](rpi__pico__dma_8h.md#a16432ea7735d3d2b46696eb42c3a5a78)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP4 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x1C)

[ 47](rpi__pico__dma_8h.md#a262317a40c039af688969d08b734cb30)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP5 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x1D)

[ 48](rpi__pico__dma_8h.md#acc46df2f8f0ba68e155eb9dfb78d316b)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP6 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x1E)

[ 49](rpi__pico__dma_8h.md#acd268446715055b789d0b32527eaec18)#define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP7 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x1F)

[ 50](rpi__pico__dma_8h.md#aeb3507fc3e3416b7bedfaebbfe8ba980)#define RPI\_PICO\_DMA\_SLOT\_I2C0\_TX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x30)

[ 51](rpi__pico__dma_8h.md#a22bdae09d66f57f0b2f26e6bd6b36f31)#define RPI\_PICO\_DMA\_SLOT\_I2C0\_RX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x31)

[ 52](rpi__pico__dma_8h.md#afa10629c69c563ca959fe692f40bc5bb)#define RPI\_PICO\_DMA\_SLOT\_I2C1\_TX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x32)

[ 53](rpi__pico__dma_8h.md#a0f6717d3026d1c19c30e84bd4f91511b)#define RPI\_PICO\_DMA\_SLOT\_I2C1\_RX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x33)

[ 54](rpi__pico__dma_8h.md#ab9e20d2a674fa5d1947c01a5dc2fb359)#define RPI\_PICO\_DMA\_SLOT\_ADC RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x34)

[ 55](rpi__pico__dma_8h.md#a831f08fba56848125d1e8773c05ac588)#define RPI\_PICO\_DMA\_SLOT\_XIP\_STREAM RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x35)

[ 56](rpi__pico__dma_8h.md#a01f1ea52277e47bff8c3d76d6da7dab3)#define RPI\_PICO\_DMA\_SLOT\_XIP\_SSITX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x36)

[ 57](rpi__pico__dma_8h.md#abdb688be5a52ddc5c3aacf2048096987)#define RPI\_PICO\_DMA\_SLOT\_XIP\_SSIRX RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x37)

[ 58](rpi__pico__dma_8h.md#aac94fe3f6411cd4bad422974be560d92)#define RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER0 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x3B)

[ 59](rpi__pico__dma_8h.md#a864c5126bab363926d43b8d2a951a935)#define RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER1 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x3C)

[ 60](rpi__pico__dma_8h.md#a0b8c6347ccfe168d06851fdac5bfe470)#define RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER2 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x3D)

[ 61](rpi__pico__dma_8h.md#aa4cf3c65b88cf11aaadd685363695262)#define RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER3 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x3E)

[ 62](rpi__pico__dma_8h.md#a6571b7502d26dcb0011fa9c38f64f793)#define RPI\_PICO\_DMA\_SLOT\_FORCE RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x3F)

63

64#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RPI\_PICO\_DMA\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [rpi\_pico\_dma.h](rpi__pico__dma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
