---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arm_2asm__inline_8h_source.html
original_path: doxygen/html/arm_2asm__inline_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

asm\_inline.h

[Go to the documentation of this file.](arm_2asm__inline_8h.md)

1/\* ARM AArch32 inline assembler functions and macros for public functions \*/

2

3/\*

4 \* Copyright (c) 2015, Wind River Systems, Inc.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_ASM\_INLINE\_H\_

10#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_ASM\_INLINE\_H\_

11

12/\*

13 \* The file must not be included directly

14 \* Include kernel.h instead

15 \*/

16

17#if defined(\_\_GNUC\_\_) || defined(\_\_ICCARM\_\_)

18#include <[zephyr/arch/arm/asm\_inline\_gcc.h](arm_2asm__inline__gcc_8h.md)>

19#else

20#error Unknown toolchain in asm\_inline.h

21#endif

22

23#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_ASM\_INLINE\_H\_ \*/

[asm\_inline\_gcc.h](arm_2asm__inline__gcc_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [asm\_inline.h](arm_2asm__inline_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
