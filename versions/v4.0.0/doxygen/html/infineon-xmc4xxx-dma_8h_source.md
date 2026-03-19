---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/infineon-xmc4xxx-dma_8h_source.html
original_path: doxygen/html/infineon-xmc4xxx-dma_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

infineon-xmc4xxx-dma.h

[Go to the documentation of this file.](infineon-xmc4xxx-dma_8h.md)

1/\*

2 \* Copyright (c) 2022 Andriy Gelman <andriy.gelman@gmail.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_DMA\_INFINEON\_XMC4XXX\_DMA\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_DMA\_INFINEON\_XMC4XXX\_DMA\_H\_

9

[ 10](infineon-xmc4xxx-dma_8h.md#a3c4acabda14da40580e0a2b27ee65460)#define XMC4XXX\_DMA\_REQUEST\_SOURCE\_POS 0

[ 11](infineon-xmc4xxx-dma_8h.md#a4df66f182189c3ae0983cdbbf9ae441c)#define XMC4XXX\_DMA\_REQUEST\_SOURCE\_MASK 0xf

12

[ 13](infineon-xmc4xxx-dma_8h.md#a770a813125a4338de8e409d4c9056c16)#define XMC4XXX\_DMA\_LINE\_POS 4

[ 14](infineon-xmc4xxx-dma_8h.md#a6675bcb092ce91d47fa5b47142ca45f4)#define XMC4XXX\_DMA\_LINE\_MASK 0xf

15

[ 16](infineon-xmc4xxx-dma_8h.md#a7545b103c79e582bec92c59571c2aee5)#define XMC4XXX\_DMA\_GET\_REQUEST\_SOURCE(mx) \

17 ((mx >> XMC4XXX\_DMA\_REQUEST\_SOURCE\_POS) & XMC4XXX\_DMA\_REQUEST\_SOURCE\_MASK)

18

[ 19](infineon-xmc4xxx-dma_8h.md#a27d5d96c050301bfc22b52fe7f5483db)#define XMC4XXX\_DMA\_GET\_LINE(mx) ((mx >> XMC4XXX\_DMA\_LINE\_POS) & XMC4XXX\_DMA\_LINE\_MASK)

20

[ 21](infineon-xmc4xxx-dma_8h.md#afa54bae091f586404ae79cfa97db6d36)#define XMC4XXX\_SET\_CONFIG(line, rs) \

22 ((line) << XMC4XXX\_DMA\_LINE\_POS | (rs) << XMC4XXX\_DMA\_REQUEST\_SOURCE\_POS)

23

24#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_DMA\_INFINEON\_XMC4XXX\_DMA\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [infineon-xmc4xxx-dma.h](infineon-xmc4xxx-dma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
