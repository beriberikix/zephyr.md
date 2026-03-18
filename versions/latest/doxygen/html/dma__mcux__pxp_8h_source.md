---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/dma__mcux__pxp_8h_source.html
original_path: doxygen/html/dma__mcux__pxp_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_mcux\_pxp.h

[Go to the documentation of this file.](dma__mcux__pxp_8h.md)

1/\*

2 \* Copyright 2023 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_MCUX\_PXP\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_MCUX\_PXP\_H\_

9

[ 10](dma__mcux__pxp_8h.md#a1a447b1990a0a58a58b8f2c1b91f4596)#define DMA\_MCUX\_PXP\_CMD\_MASK 0xE0

[ 11](dma__mcux__pxp_8h.md#a98023d4702873f806316fa8076217f2b)#define DMA\_MCUX\_PXP\_CMD\_SHIFT 0x5

12

[ 13](dma__mcux__pxp_8h.md#a99a43acbabab4f6d3d16601776e64ef5)#define DMA\_MCUX\_PXP\_FMT\_MASK 0x1F

[ 14](dma__mcux__pxp_8h.md#a5ecb10ea31b3b4841d1d1e50ef182b39)#define DMA\_MCUX\_PXP\_FMT\_SHIFT 0x0

15

16/\*

17 \* In order to configure the PXP for rotation, the user should

18 \* supply a format and command as the DMA slot parameter, like so:

19 \* dma\_slot = (DMA\_MCUX\_PXP\_FTM(DMA\_MCUX\_PXP\_FMT\_RGB565) |

20 \* DMA\_MCUX\_PXP\_CMD(DMA\_MCUX\_PXP\_CMD\_ROTATE\_90))

21 \* head block source address: input buffer address

22 \* head block destination address: output buffer address

23 \* source data size: input buffer size in bytes

24 \* source burst length: height of source buffer in pixels

25 \* dest data size: output buffer size in bytes

26 \* dest burst length: height of destination buffer in pixels

27 \*/

28

[ 29](dma__mcux__pxp_8h.md#ae33fe6641b02a3af1910ba0ab30306a2)#define DMA\_MCUX\_PXP\_FMT(x) ((x << DMA\_MCUX\_PXP\_FMT\_SHIFT) & DMA\_MCUX\_PXP\_FMT\_MASK)

[ 30](dma__mcux__pxp_8h.md#a3b6888b7002f91c46c891497420a59a4)#define DMA\_MCUX\_PXP\_CMD(x) ((x << DMA\_MCUX\_PXP\_CMD\_SHIFT) & DMA\_MCUX\_PXP\_CMD\_MASK)

31

[ 32](dma__mcux__pxp_8h.md#ad0e771ececbc5a7f6257d76b7d3667d7)#define DMA\_MCUX\_PXP\_CMD\_ROTATE\_0 0

[ 33](dma__mcux__pxp_8h.md#a26e4776708c27df4c2a17437ea944092)#define DMA\_MCUX\_PXP\_CMD\_ROTATE\_90 1

[ 34](dma__mcux__pxp_8h.md#ab37674ee7555385cefe3cbc328201e31)#define DMA\_MCUX\_PXP\_CMD\_ROTATE\_180 2

[ 35](dma__mcux__pxp_8h.md#af53cad3d27fbd9d2ae8ca108201f882f)#define DMA\_MCUX\_PXP\_CMD\_ROTATE\_270 3

36

[ 37](dma__mcux__pxp_8h.md#a39a2b6f27b7dae092f9cfe491bbd078f)#define DMA\_MCUX\_PXP\_FMT\_RGB565 0

[ 38](dma__mcux__pxp_8h.md#a3667a7b1faf41211b55c22d5f22edd3b)#define DMA\_MCUX\_PXP\_FMT\_RGB888 1

39

40#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_MCUX\_PXP\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma](dir_0dbbf0f7c33b88bff3996b0543cef0a8.md)
- [dma\_mcux\_pxp.h](dma__mcux__pxp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
