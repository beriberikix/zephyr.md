---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arc_2v2_2asm__inline_8h_source.html
original_path: doxygen/html/arc_2v2_2asm__inline_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

asm\_inline.h

[Go to the documentation of this file.](arc_2v2_2asm__inline_8h.md)

1/\* asm\_inline.h - ARC inline assembler and macros for public functions \*/

2

3/\*

4 \* Copyright (c) 2015 Intel Corporation.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_ASM\_INLINE\_H\_

10#define ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_ASM\_INLINE\_H\_

11

12/\*

13 \* The file must not be included directly

14 \* Include kernel.h instead

15 \*/

16

17#if defined(\_\_GNUC\_\_)

18#include <[zephyr/arch/arc/v2/asm\_inline\_gcc.h](arc_2v2_2asm__inline__gcc_8h.md)>

19#else

20#erro "you need to provide an asm\_inline.h for your compiler"

21#endif

22

23#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_ASM\_INLINE\_H\_ \*/

[asm\_inline\_gcc.h](arc_2v2_2asm__inline__gcc_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [asm\_inline.h](arc_2v2_2asm__inline_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
