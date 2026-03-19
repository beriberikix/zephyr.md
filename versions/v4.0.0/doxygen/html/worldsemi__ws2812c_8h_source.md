---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/worldsemi__ws2812c_8h_source.html
original_path: doxygen/html/worldsemi__ws2812c_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

worldsemi\_ws2812c.h

[Go to the documentation of this file.](worldsemi__ws2812c_8h.md)

1/\*

2 \* Copyright (c) 2023 Martin Kiepfer <mrmarteng@teleschirm.org>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_DT\_LED\_WS2812C\_H\_

8#define ZEPHYR\_DT\_LED\_WS2812C\_H\_

9

10/\*

11 \* At 7 MHz: 1 bit in 142.86 ns

12 \* 1090 ns -> 7.6 bits

13 \* 300 ns -> 2.1 bits

14 \* 790 ns -> 5.5 bits

15 \*/

[ 16](worldsemi__ws2812c_8h.md#a3117817f316cb3354e521ff2cfbb48a4)#define WS2812C\_SPI\_FREQ (7000000U)

[ 17](worldsemi__ws2812c_8h.md#a758113b33aa67798165279aca78dfe9d)#define WS2812C\_ZERO\_FRAME (0xC0U)

[ 18](worldsemi__ws2812c_8h.md#a677a8464e33c3eec0db85eadd78206f3)#define WS2812C\_ONE\_FRAME (0xFCU)

19

20#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [led](dir_43259d1800ff16a5cdd32a96a4c7d34d.md)
- [worldsemi\_ws2812c.h](worldsemi__ws2812c_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
