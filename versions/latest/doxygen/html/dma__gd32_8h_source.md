---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/dma__gd32_8h_source.html
original_path: doxygen/html/dma__gd32_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_gd32.h

[Go to the documentation of this file.](dma__gd32_8h.md)

1/\*

2 \* Copyright (c) 2022 TOKITA Hiroshi <tokita.hiroshi@gmail.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_GD32\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_GD32\_H\_

9

[ 10](dma__gd32_8h.md#a0bfc50da9b666c382ca00e53612c08e8)#define GD32\_DMA\_CONFIG\_DIRECTION(config) ((config >> 6) & 0x3)

[ 11](dma__gd32_8h.md#a12c9387cd798e45a97a025d892fee048)#define GD32\_DMA\_CONFIG\_PERIPH\_ADDR\_INC(config) ((config >> 9) & 0x1)

[ 12](dma__gd32_8h.md#a6048bfaf2929f8ace82bfdf910a85224)#define GD32\_DMA\_CONFIG\_MEMORY\_ADDR\_INC(config) ((config >> 10) & 0x1)

[ 13](dma__gd32_8h.md#ae09b2bd2a0abf46f92afbc93c8f0b1f2)#define GD32\_DMA\_CONFIG\_PERIPH\_WIDTH(config) ((config >> 11) & 0x3)

[ 14](dma__gd32_8h.md#af6d346ff11af7445ef216ff86943de58)#define GD32\_DMA\_CONFIG\_MEMORY\_WIDTH(config) ((config >> 13) & 0x3)

[ 15](dma__gd32_8h.md#a3c35875713e5534e753068e77c4a8796)#define GD32\_DMA\_CONFIG\_PERIPHERAL\_INC\_FIXED(config) ((config >> 15) & 0x1)

[ 16](dma__gd32_8h.md#acfb3e4c8ef6bed1484348f72be5a2fb9)#define GD32\_DMA\_CONFIG\_PRIORITY(config) ((config >> 16) & 0x3)

17

[ 18](dma__gd32_8h.md#af41c61ae669ce510d514ccb9ff6204f9)#define GD32\_DMA\_FEATURES\_FIFO\_THRESHOLD(threshold) (threshold & 0x3)

19

20#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_GD32\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma](dir_0dbbf0f7c33b88bff3996b0543cef0a8.md)
- [dma\_gd32.h](dma__gd32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
