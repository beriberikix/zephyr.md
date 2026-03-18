---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/kinetis__pcc_8h_source.html
original_path: doxygen/html/kinetis__pcc_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

kinetis\_pcc.h

[Go to the documentation of this file.](kinetis__pcc_8h.md)

1/\*

2 \* Copyright (c) 2019 Vestas Wind Systems A/S

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_KINETIS\_PCC\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_KINETIS\_PCC\_H\_

9

10/\* NXP Kinetis Peripheral Clock Controller IP sources \*/

[ 11](kinetis__pcc_8h.md#a4da823bad2458ed0443e9832b5a1d5ce)#define KINETIS\_PCC\_SRC\_NONE\_OR\_EXT 0 /\* Clock off or external clock is used \*/

[ 12](kinetis__pcc_8h.md#a04f2415d18cd0566d135ffc8bd6a93f5)#define KINETIS\_PCC\_SRC\_SOSC\_ASYNC 1 /\* System Oscillator async clock \*/

[ 13](kinetis__pcc_8h.md#abdbbf807790548a52a737eacf09d9c51)#define KINETIS\_PCC\_SRC\_SIRC\_ASYNC 2 /\* Slow IRC async clock \*/

[ 14](kinetis__pcc_8h.md#a18f811e96fa60fb0526d2f69542c2bd2)#define KINETIS\_PCC\_SRC\_FIRC\_ASYNC 3 /\* Fast IRC async clock \*/

[ 15](kinetis__pcc_8h.md#a114c98191606e3faec846ac7c5e4f2a0)#define KINETIS\_PCC\_SRC\_SPLL\_ASYNC 6 /\* System PLL async clock \*/

16

17#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_KINETIS\_PCC\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [kinetis\_pcc.h](kinetis__pcc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
