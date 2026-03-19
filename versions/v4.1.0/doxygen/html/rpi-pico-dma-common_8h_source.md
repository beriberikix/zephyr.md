---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/rpi-pico-dma-common_8h_source.html
original_path: doxygen/html/rpi-pico-dma-common_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rpi-pico-dma-common.h

[Go to the documentation of this file.](rpi-pico-dma-common_8h.md)

1/\*

2 \* Copyright (c) 2023 TOKITA Hiroshi <tokita.hiroshi@fujitsu.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RPI\_PICO\_DMA\_COMMON\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RPI\_PICO\_DMA\_COMMON\_H\_

9

10/\*

11 \* Use lower 6-bit of inverted DREQ value for `slot` cell.

12 \* Need to be able to work for memory-to-memory transfer

13 \* with zero, which is the default value.

14 \*/

[ 15](rpi-pico-dma-common_8h.md#af17a4ab6d1b744cb7ba78185681f464b)#define RPI\_PICO\_DMA\_SLOT\_TO\_DREQ(s) (~(s)&0x3F)

[ 16](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)#define RPI\_PICO\_DMA\_DREQ\_TO\_SLOT RPI\_PICO\_DMA\_SLOT\_TO\_DREQ

17

[ 18](rpi-pico-dma-common_8h.md#ab4efb501d7d6acf7c4e320a992a736c9)#define RPI\_PICO\_DMA\_SLOT\_PIO0\_TX0 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x00)

[ 19](rpi-pico-dma-common_8h.md#ac83bcbc6b3716d947051d785f60447c1)#define RPI\_PICO\_DMA\_SLOT\_PIO0\_TX1 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x01)

[ 20](rpi-pico-dma-common_8h.md#ad2452d29f952c828fc38036d3fc8f7c7)#define RPI\_PICO\_DMA\_SLOT\_PIO0\_TX2 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x02)

[ 21](rpi-pico-dma-common_8h.md#a3be36155cb5c9faff83951e46e1ce6eb)#define RPI\_PICO\_DMA\_SLOT\_PIO0\_TX3 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x03)

[ 22](rpi-pico-dma-common_8h.md#a4931c164398407d3365d600d17110f95)#define RPI\_PICO\_DMA\_SLOT\_PIO0\_RX0 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x04)

[ 23](rpi-pico-dma-common_8h.md#a84583ff2852ec17e709f44cfe85a21d1)#define RPI\_PICO\_DMA\_SLOT\_PIO0\_RX1 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x05)

[ 24](rpi-pico-dma-common_8h.md#a7a30cab865790b3ff4c873cec1ae39a4)#define RPI\_PICO\_DMA\_SLOT\_PIO0\_RX2 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x06)

[ 25](rpi-pico-dma-common_8h.md#a131cdd1941010a43bebcda6fffd98016)#define RPI\_PICO\_DMA\_SLOT\_PIO0\_RX3 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x07)

[ 26](rpi-pico-dma-common_8h.md#a17f1642461493cde7e832a1ab78d9f69)#define RPI\_PICO\_DMA\_SLOT\_PIO1\_TX0 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x08)

[ 27](rpi-pico-dma-common_8h.md#a7a19561e334931146de9a56ce3214680)#define RPI\_PICO\_DMA\_SLOT\_PIO1\_TX1 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x09)

[ 28](rpi-pico-dma-common_8h.md#ae6f04b3ecc7adfa5bb4e070f6cc29780)#define RPI\_PICO\_DMA\_SLOT\_PIO1\_TX2 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x0A)

[ 29](rpi-pico-dma-common_8h.md#ab39ac333962fe0debca583061ba1b6cb)#define RPI\_PICO\_DMA\_SLOT\_PIO1\_TX3 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x0B)

[ 30](rpi-pico-dma-common_8h.md#a7eaaa6b0e6f80021364a66fd75450c0d)#define RPI\_PICO\_DMA\_SLOT\_PIO1\_RX0 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x0C)

[ 31](rpi-pico-dma-common_8h.md#a9963f9b698a5ffde3e3bcf9b4b43ed22)#define RPI\_PICO\_DMA\_SLOT\_PIO1\_RX1 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x0D)

[ 32](rpi-pico-dma-common_8h.md#ad1a63c332b00cf4442907a3a11d155d1)#define RPI\_PICO\_DMA\_SLOT\_PIO1\_RX2 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x0E)

[ 33](rpi-pico-dma-common_8h.md#a07eab28aade43838cf5580e0c0ea3bde)#define RPI\_PICO\_DMA\_SLOT\_PIO1\_RX3 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x0F)

34

[ 35](rpi-pico-dma-common_8h.md#aac94fe3f6411cd4bad422974be560d92)#define RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER0 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x3B)

[ 36](rpi-pico-dma-common_8h.md#a864c5126bab363926d43b8d2a951a935)#define RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER1 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x3C)

[ 37](rpi-pico-dma-common_8h.md#a0b8c6347ccfe168d06851fdac5bfe470)#define RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER2 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x3D)

[ 38](rpi-pico-dma-common_8h.md#aa4cf3c65b88cf11aaadd685363695262)#define RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER3 RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x3E)

[ 39](rpi-pico-dma-common_8h.md#a6571b7502d26dcb0011fa9c38f64f793)#define RPI\_PICO\_DMA\_SLOT\_FORCE RPI\_PICO\_DMA\_DREQ\_TO\_SLOT(0x3F)

40

41#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RPI\_PICO\_DMA\_COMMON\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [rpi-pico-dma-common.h](rpi-pico-dma-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
