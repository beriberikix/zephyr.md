---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/panel_8h_source.html
original_path: doxygen/html/panel_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

panel.h

[Go to the documentation of this file.](panel_8h.md)

1/\*

2 \* Copyright 2023 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_DISPLAY\_PANEL\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_DISPLAY\_PANEL\_H\_

8

15

25

[ 26](group__lcd__interface.md#ga4775abe39fd68a2d64b4edb649790915)#define PANEL\_PIXEL\_FORMAT\_RGB\_888 (0x1 << 0)

[ 27](group__lcd__interface.md#ga6712b7424ad89a33e04f66e76d3678ce)#define PANEL\_PIXEL\_FORMAT\_MONO01 (0x1 << 1) /\* 0=Black 1=White \*/

[ 28](group__lcd__interface.md#ga6311ee67721bd6e7209bbdc1b6788eb6)#define PANEL\_PIXEL\_FORMAT\_MONO10 (0x1 << 2) /\* 1=Black 0=White \*/

[ 29](group__lcd__interface.md#gac86c839997816ecfe501b14d240a6f2a)#define PANEL\_PIXEL\_FORMAT\_ARGB\_8888 (0x1 << 3)

[ 30](group__lcd__interface.md#gad8d20eb4c243e11080d31df41026475b)#define PANEL\_PIXEL\_FORMAT\_RGB\_565 (0x1 << 4)

[ 31](group__lcd__interface.md#gabb5f7e341cdd0155e4b7476b81d45d8e)#define PANEL\_PIXEL\_FORMAT\_BGR\_565 (0x1 << 5)

32

36

37#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_DISPLAY\_PANEL\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [display](dir_91baf1483b4b8962ae5c4d52a6474304.md)
- [panel.h](panel_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
