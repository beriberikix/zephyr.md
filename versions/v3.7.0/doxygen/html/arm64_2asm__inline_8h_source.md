---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arm64_2asm__inline_8h_source.html
original_path: doxygen/html/arm64_2asm__inline_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

asm\_inline.h

[Go to the documentation of this file.](arm64_2asm__inline_8h.md)

1/\*

2 \* Copyright (c) 2019 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM64\_ASM\_INLINE\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_ARM64\_ASM\_INLINE\_H\_

9

10/\*

11 \* The file must not be included directly

12 \* Include kernel.h instead

13 \*/

14

15#if defined(\_\_GNUC\_\_)

16#include <[zephyr/arch/arm64/asm\_inline\_gcc.h](arm64_2asm__inline__gcc_8h.md)>

17#else

18#include <arch/arm/asm\_inline\_other.h>

19#endif

20

21#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM64\_ASM\_INLINE\_H\_ \*/

[asm\_inline\_gcc.h](arm64_2asm__inline__gcc_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [asm\_inline.h](arm64_2asm__inline_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
