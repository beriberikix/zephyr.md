---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/gd32__dma_8h_source.html
original_path: doxygen/html/gd32__dma_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gd32\_dma.h

[Go to the documentation of this file.](gd32__dma_8h.md)

1/\*

2 \* Copyright (c) 2022 TOKITA Hiroshi <tokita.hiroshi@gmail.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GD32\_DMA\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GD32\_DMA\_H\_

9

10/\* macros for channel-cfg \*/

11

12/\* direction defined on bits 6-7 \*/

[ 13](gd32__dma_8h.md#ae2a0d7ee983ce7229d00424fc9bd561a)#define GD32\_DMA\_CH\_CFG\_DIRECTION(val) ((val & 0x3) << 6)

[ 14](gd32__dma_8h.md#ac66caaa6fd58e811ca1173afffb6eee0)#define GD32\_DMA\_MEMORY\_TO\_MEMORY GD32\_DMA\_CH\_CFG\_DIRECTION(0)

[ 15](gd32__dma_8h.md#a133ee2eba1696a8a88e553899b42215d)#define GD32\_DMA\_MEMORY\_TO\_PERIPH GD32\_DMA\_CH\_CFG\_DIRECTION(1)

[ 16](gd32__dma_8h.md#a6db732bda87b175e5594e47120b50fc4)#define GD32\_DMA\_PERIPH\_TO\_MEMORY GD32\_DMA\_CH\_CFG\_DIRECTION(2)

17

18/\* periph increase defined on bit 9 as true/false \*/

[ 19](gd32__dma_8h.md#ad0abcd3eb77751438884eb14376a4249)#define GD32\_DMA\_CH\_CFG\_PERIPH\_ADDR\_INC(val) ((val & 0x1) << 9)

[ 20](gd32__dma_8h.md#a3190a823bcefea6dea75b22751437469)#define GD32\_DMA\_NO\_PERIPH\_ADDR\_INC GD32\_DMA\_CH\_CFG\_PERIPH\_ADDR\_INC(0)

[ 21](gd32__dma_8h.md#a886f483d28ecb076d76cab9807dbd9ae)#define GD32\_DMA\_PERIPH\_ADDR\_INC GD32\_DMA\_CH\_CFG\_PERIPH\_ADDR\_INC(1)

22

23/\* memory increase defined on bit 10 as true/false \*/

[ 24](gd32__dma_8h.md#ae55d797279e2483a9de15ddb250d9c01)#define GD32\_DMA\_CH\_CFG\_MEMORY\_ADDR\_INC(val) ((val & 0x1) << 10)

[ 25](gd32__dma_8h.md#a45eb42e1d19daa3d40831c93ad0ba0a0)#define GD32\_DMA\_NO\_MEMORY\_ADDR\_INC GD32\_DMA\_CH\_CFG\_MEMORY\_ADDR\_INC(0)

[ 26](gd32__dma_8h.md#a1dfa4abe03789cb06229e071479a68d3)#define GD32\_DMA\_MEMORY\_ADDR\_INC GD32\_DMA\_CH\_CFG\_MEMORY\_ADDR\_INC(1)

27

28/\* periph data size defined on bits 11-12 \*/

[ 29](gd32__dma_8h.md#a7ee975a1a1338f3fcbf9779a4f66ec7c)#define GD32\_DMA\_CH\_CFG\_PERIPH\_WIDTH(val) ((val & 0x3) << 11)

[ 30](gd32__dma_8h.md#a43f8444f017382621385497e88bc28eb)#define GD32\_DMA\_PERIPH\_WIDTH\_8BIT GD32\_DMA\_CH\_CFG\_PERIPH\_WIDTH(0)

[ 31](gd32__dma_8h.md#acd17760bf971b4efae57cbb7413c7993)#define GD32\_DMA\_PERIPH\_WIDTH\_16BIT GD32\_DMA\_CH\_CFG\_PERIPH\_WIDTH(1)

[ 32](gd32__dma_8h.md#ac8071edf3e9c36beb96f8a2f41f9b297)#define GD32\_DMA\_PERIPH\_WIDTH\_32BIT GD32\_DMA\_CH\_CFG\_PERIPH\_WIDTH(2)

33

34/\* memory data size defined on bits 13-14 \*/

[ 35](gd32__dma_8h.md#a7e46c2dd560ad05b3ef2d49e8e934634)#define GD32\_DMA\_CH\_CFG\_MEMORY\_WIDTH(val) ((val & 0x3) << 13)

[ 36](gd32__dma_8h.md#aa02a7efc2fca50aa800f39e94b3759b4)#define GD32\_DMA\_MEMORY\_WIDTH\_8BIT GD32\_DMA\_CH\_CFG\_PERIPH\_WIDTH(0)

[ 37](gd32__dma_8h.md#a0787852dc6f450f4eff8eea7be3a6b89)#define GD32\_DMA\_MEMORY\_WIDTH\_16BIT GD32\_DMA\_CH\_CFG\_PERIPH\_WIDTH(1)

[ 38](gd32__dma_8h.md#a2d77c7ecc44a7c91dfecbf94044ec5a0)#define GD32\_DMA\_MEMORY\_WIDTH\_32BIT GD32\_DMA\_CH\_CFG\_PERIPH\_WIDTH(2)

39

40/\* priority increment offset defined on bit 15 \*/

[ 41](gd32__dma_8h.md#a0eecb55bada0630383167b56d82c4892)#define GD32\_DMA\_CH\_CFG\_PERIPH\_INC\_FIXED(val) ((val & 0x1) << 15)

42

43/\* priority defined on bits 16-17 as 0, 1, 2, 3 \*/

[ 44](gd32__dma_8h.md#a7a95cc521b5445314d9d64528d885724)#define GD32\_DMA\_CH\_CFG\_PRIORITY(val) ((val & 0x3) << 16)

[ 45](gd32__dma_8h.md#ae68917539c8744ddcfbad918e69db56e)#define GD32\_DMA\_PRIORITY\_LOW GD32\_DMA\_CH\_CFG\_PRIORITY(0)

[ 46](gd32__dma_8h.md#a548fac07f1b1c5cdd61670178c7ecc8b)#define GD32\_DMA\_PRIORITY\_MEDIUM GD32\_DMA\_CH\_CFG\_PRIORITY(1)

[ 47](gd32__dma_8h.md#a17a02cccc8980fd5a273f251b4e02ea6)#define GD32\_DMA\_PRIORITY\_HIGH GD32\_DMA\_CH\_CFG\_PRIORITY(2)

[ 48](gd32__dma_8h.md#ad6e846a9a5b52f0838c1b214ba39b6b3)#define GD32\_DMA\_PRIORITY\_VERY\_HIGH GD32\_DMA\_CH\_CFG\_PRIORITY(3)

49

50#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GD32\_DMA\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [gd32\_dma.h](gd32__dma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
