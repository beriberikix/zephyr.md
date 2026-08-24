---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ch32v00x-clocks_8h_source.html
original_path: doxygen/html/ch32v00x-clocks_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ch32v00x-clocks.h

[Go to the documentation of this file.](ch32v00x-clocks_8h.md)

1/\*

2 \* Copyright (c) 2024 Michael Hope

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_CH32V00X\_CLOCKS\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_CH32V00X\_CLOCKS\_H\_

9

[ 10](ch32v00x-clocks_8h.md#ae23b04c6f7dc288edd55ca371b0ac6ac)#define CH32V00X\_HB\_PCENR\_OFFSET 0

[ 11](ch32v00x-clocks_8h.md#ac16a6b94e0d36222243acfe99bd576b1)#define CH32V00X\_PB2\_PCENR\_OFFSET 1

[ 12](ch32v00x-clocks_8h.md#a4de5424f7b84a7be9525d3baaf95b372)#define CH32V00X\_PB1\_PCENR\_OFFSET 2

13

[ 14](ch32v00x-clocks_8h.md#ab39a50912925831fd0f53da79caa1f3e)#define CH32V00X\_CLOCK\_CONFIG(bus, bit) (((CH32V00X\_##bus##\_PCENR\_OFFSET) << 5) | (bit))

15

[ 16](ch32v00x-clocks_8h.md#a673a85e0807d525d0d896968e72476d7)#define CH32V00X\_CLOCK\_DMA1 CH32V00X\_CLOCK\_CONFIG(HB, 0)

[ 17](ch32v00x-clocks_8h.md#aea9e25b32bec97ba5c4d341a31523586)#define CH32V00X\_CLOCK\_SRAM CH32V00X\_CLOCK\_CONFIG(HB, 2)

18

[ 19](ch32v00x-clocks_8h.md#adba8b05c326b5c50a5f46a4235347cd2)#define CH32V00X\_CLOCK\_AFIO CH32V00X\_CLOCK\_CONFIG(PB2, 0)

[ 20](ch32v00x-clocks_8h.md#a6937d869f977cb90e519b2b92f98c120)#define CH32V00X\_CLOCK\_IOPA CH32V00X\_CLOCK\_CONFIG(PB2, 2)

[ 21](ch32v00x-clocks_8h.md#a58487531bac2d11010fa719cc9b8bc5b)#define CH32V00X\_CLOCK\_IOPB CH32V00X\_CLOCK\_CONFIG(PB2, 3)

[ 22](ch32v00x-clocks_8h.md#af66030ec198edaa564110cc3b0a6b889)#define CH32V00X\_CLOCK\_IOPC CH32V00X\_CLOCK\_CONFIG(PB2, 4)

[ 23](ch32v00x-clocks_8h.md#aa2c9b9bc83471c7c0701685025ad45b9)#define CH32V00X\_CLOCK\_IOPD CH32V00X\_CLOCK\_CONFIG(PB2, 5)

[ 24](ch32v00x-clocks_8h.md#a4ddfcf15d13a740f3917034aa6aee075)#define CH32V00X\_CLOCK\_ADC1 CH32V00X\_CLOCK\_CONFIG(PB2, 9)

[ 25](ch32v00x-clocks_8h.md#a35b5af6bc5e72b9360c923916cd2e0f1)#define CH32V00X\_CLOCK\_TIM1 CH32V00X\_CLOCK\_CONFIG(PB2, 11)

[ 26](ch32v00x-clocks_8h.md#a9ee9b0e633a4a50809c2d2d1d437dd2b)#define CH32V00X\_CLOCK\_SPI1 CH32V00X\_CLOCK\_CONFIG(PB2, 12)

[ 27](ch32v00x-clocks_8h.md#a7d61b5360a6d66ee4ca2210f3e1d32f2)#define CH32V00X\_CLOCK\_USART2 CH32V00X\_CLOCK\_CONFIG(PB2, 13)

[ 28](ch32v00x-clocks_8h.md#af46cda54f5d666db759746a11909b148)#define CH32V00X\_CLOCK\_USART1 CH32V00X\_CLOCK\_CONFIG(PB2, 14)

29

[ 30](ch32v00x-clocks_8h.md#a22cff65ee5b38ca47089ffa0916c8fda)#define CH32V00X\_CLOCK\_TIM2 CH32V00X\_CLOCK\_CONFIG(PB1, 0)

[ 31](ch32v00x-clocks_8h.md#a69c30a9fb4e812dff7c5d2b9834a012b)#define CH32V00X\_CLOCK\_TIM3 CH32V00X\_CLOCK\_CONFIG(PB1, 2)

[ 32](ch32v00x-clocks_8h.md#aa1b25307b070e0131c8d2883cc6daac2)#define CH32V00X\_CLOCK\_WWDG CH32V00X\_CLOCK\_CONFIG(PB1, 11)

[ 33](ch32v00x-clocks_8h.md#a44898d60cab2a44b6f11f44dcc910faf)#define CH32V00X\_CLOCK\_I2C1 CH32V00X\_CLOCK\_CONFIG(PB1, 21)

[ 34](ch32v00x-clocks_8h.md#ae70e92186311daf444e9b2a9c4891dcf)#define CH32V00X\_CLOCK\_PWR CH32V00X\_CLOCK\_CONFIG(PB1, 28)

35

36#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_CH32V00X\_CLOCKS\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [ch32v00x-clocks.h](ch32v00x-clocks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
