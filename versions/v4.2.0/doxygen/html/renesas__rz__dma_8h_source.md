---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/renesas__rz__dma_8h_source.html
original_path: doxygen/html/renesas__rz__dma_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas\_rz\_dma.h

[Go to the documentation of this file.](renesas__rz__dma_8h.md)

1/\*

2 \* Copyright (c) 2024 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_DMA\_RENESAS\_RZ\_DMA\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_DMA\_RENESAS\_RZ\_DMA\_H\_

8

9/\* mode: bit 0 (0: Normal, 1: Block) \*/

10/\* source data size: bit 1, 2, 3 (0b000 -> 0b111) \*/

11/\* dest data size: bit 4, 5, 6 (0b000 -> 0b111) \*/

12/\* source addr mode: bit 7 (0: incremented, 1: fixed) \*/

13/\* dest addr mode: bit 8 (0: incremented, 1: fixed) \*/

14

[ 15](renesas__rz__dma_8h.md#a2b81e575b015aab7551dd910d5c8204d)#define RZ\_DMA\_MODE\_NORMAL (0U)

[ 16](renesas__rz__dma_8h.md#a3dc76a9c51aa176eecf2fb0a7c58ce05)#define RZ\_DMA\_MODE\_BLOCK (1U)

17

18/\* DMA source data size config on bits 1, 2, 3 \*/

[ 19](renesas__rz__dma_8h.md#a5a925aec5cb8d0e787c00e3bf28adabb)#define RZ\_DMA\_CFG\_SRC\_DATA\_SIZE(val) ((val & 0x7) << 1)

[ 20](renesas__rz__dma_8h.md#ad2630f88edccd524379229c6d08c3d6f)#define RZ\_DMA\_SRC\_1\_BYTE RZ\_DMA\_CFG\_SRC\_DATA\_SIZE(0)

[ 21](renesas__rz__dma_8h.md#a06c39443f03c6bf1f4a10a46492a4fcf)#define RZ\_DMA\_SRC\_2\_BYTE RZ\_DMA\_CFG\_SRC\_DATA\_SIZE(1)

[ 22](renesas__rz__dma_8h.md#a4bd983230d98d2a4bd98942f3b433765)#define RZ\_DMA\_SRC\_4\_BYTE RZ\_DMA\_CFG\_SRC\_DATA\_SIZE(2)

[ 23](renesas__rz__dma_8h.md#aadd165c44a5d9ec2d221f4de0fff99da)#define RZ\_DMA\_SRC\_8\_BYTE RZ\_DMA\_CFG\_SRC\_DATA\_SIZE(3)

[ 24](renesas__rz__dma_8h.md#a491d97dc4a9005cbf668fed70fe61292)#define RZ\_DMA\_SRC\_16\_BYTE RZ\_DMA\_CFG\_SRC\_DATA\_SIZE(4)

[ 25](renesas__rz__dma_8h.md#a05c3af12ddbc5abc07a635ee3dc184d8)#define RZ\_DMA\_SRC\_32\_BYTE RZ\_DMA\_CFG\_SRC\_DATA\_SIZE(5)

[ 26](renesas__rz__dma_8h.md#a47c957c6ddbf73e702d3cc406396d598)#define RZ\_DMA\_SRC\_64\_BYTE RZ\_DMA\_CFG\_SRC\_DATA\_SIZE(6)

[ 27](renesas__rz__dma_8h.md#afbebd4bc7e8faafa874532416b9f5977)#define RZ\_DMA\_SRC\_128\_BYTE RZ\_DMA\_CFG\_SRC\_DATA\_SIZE(7)

28

29/\* DMA destination data size config on bits 4, 5, 6 \*/

[ 30](renesas__rz__dma_8h.md#aee9e5ee0e341869584ffcd22bec9d684)#define RZ\_DMA\_CFG\_DEST\_DATA\_SIZE(val) ((val & 0x7) << 4)

[ 31](renesas__rz__dma_8h.md#a34bf5afed49353a0ecdff99cff12bd95)#define RZ\_DMA\_DEST\_1\_BYTE RZ\_DMA\_CFG\_DEST\_DATA\_SIZE(0)

[ 32](renesas__rz__dma_8h.md#a16018c672b1ff17d2065617e1145ce85)#define RZ\_DMA\_DEST\_2\_BYTE RZ\_DMA\_CFG\_DEST\_DATA\_SIZE(1)

[ 33](renesas__rz__dma_8h.md#ad5063a15c1612bbba264227a40b91d87)#define RZ\_DMA\_DEST\_4\_BYTE RZ\_DMA\_CFG\_DEST\_DATA\_SIZE(2)

[ 34](renesas__rz__dma_8h.md#a8a02c00f90f4532b44a2c2ff7f1be3ab)#define RZ\_DMA\_DEST\_8\_BYTE RZ\_DMA\_CFG\_DEST\_DATA\_SIZE(3)

[ 35](renesas__rz__dma_8h.md#acd01a438d73deaf6fe76b06c44593394)#define RZ\_DMA\_DEST\_16\_BYTE RZ\_DMA\_CFG\_DEST\_DATA\_SIZE(4)

[ 36](renesas__rz__dma_8h.md#a47929d19f83967834a22b2a5bef7dde1)#define RZ\_DMA\_DEST\_32\_BYTE RZ\_DMA\_CFG\_DEST\_DATA\_SIZE(5)

[ 37](renesas__rz__dma_8h.md#a1a95a59ace78fbfadbfdb113975ee361)#define RZ\_DMA\_DEST\_64\_BYTE RZ\_DMA\_CFG\_DEST\_DATA\_SIZE(6)

[ 38](renesas__rz__dma_8h.md#aa415a830c4e71f1c59869f1d1935a752)#define RZ\_DMA\_DEST\_128\_BYTE RZ\_DMA\_CFG\_DEST\_DATA\_SIZE(7)

39

40/\* DMA source address mode config on bit 7 \*/

[ 41](renesas__rz__dma_8h.md#a41b9387b512f2d26315db92a55b331bc)#define RZ\_DMA\_CFG\_SRC\_ADDR\_MODE(val) ((val & 0x1) << 7)

[ 42](renesas__rz__dma_8h.md#a272bea303fa2484c83a197831b17ea75)#define RZ\_DMA\_SRC\_INCREMENTED RZ\_DMA\_CFG\_SRC\_ADDR\_MODE(0)

[ 43](renesas__rz__dma_8h.md#a0e47b6a3c30b6157d99d397641c672c1)#define RZ\_DMA\_SRC\_FIXED RZ\_DMA\_CFG\_SRC\_ADDR\_MODE(1)

44

45/\* DMA source address mode config on bit 8 \*/

[ 46](renesas__rz__dma_8h.md#a35c2cf645fd17892b06760e79e7799e0)#define RZ\_DMA\_CFG\_DEST\_ADDR\_MODE(val) ((val & 0x1) << 8)

[ 47](renesas__rz__dma_8h.md#a4d3de22701e71b2bb3dabcf63f04c35f)#define RZ\_DMA\_DEST\_INCREMENTED RZ\_DMA\_CFG\_DEST\_ADDR\_MODE(0)

[ 48](renesas__rz__dma_8h.md#a5cb1d2cbda322e0524c3317fe830dd2e)#define RZ\_DMA\_DEST\_FIXED RZ\_DMA\_CFG\_DEST\_ADDR\_MODE(1)

49

50/\* DMA usual combination for peripheral transfer \*/

[ 51](renesas__rz__dma_8h.md#a752b0f622d69a7eb8bffae025208f684)#define RZ\_DMA\_MEM\_TO\_PERIPH \

52 (RZ\_DMA\_MODE\_NORMAL | RZ\_DMA\_SRC\_INCREMENTED | RZ\_DMA\_DEST\_FIXED | RZ\_DMA\_SRC\_1\_BYTE | \

53 RZ\_DMA\_DEST\_1\_BYTE)

[ 54](renesas__rz__dma_8h.md#a11c53b4c6de9c71d7b443ef02c2b9384)#define RZ\_DMA\_PERIPH\_TO\_MEM \

55 (RZ\_DMA\_MODE\_NORMAL | RZ\_DMA\_SRC\_FIXED | RZ\_DMA\_DEST\_INCREMENTED | RZ\_DMA\_SRC\_1\_BYTE | \

56 RZ\_DMA\_DEST\_1\_BYTE)

57

58#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_DMA\_RENESAS\_RZ\_DMA\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [renesas\_rz\_dma.h](renesas__rz__dma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
