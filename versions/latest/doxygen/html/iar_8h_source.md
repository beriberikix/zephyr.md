---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/iar_8h_source.html
original_path: doxygen/html/iar_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

iar.h

[Go to the documentation of this file.](iar_8h.md)

1/\*

2 \* Copyright (c) 2025 IAR Systems AB

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_TOOLCHAIN\_IAR\_H\_

8#define ZEPHYR\_INCLUDE\_TOOLCHAIN\_IAR\_H\_

9

10#ifdef TOOLCHAIN\_PRAGMA

11#define \_TOOLCHAIN\_DISABLE\_WARNING(warning) TOOLCHAIN\_PRAGMA(diag\_suppress = warning)

12#define \_TOOLCHAIN\_ENABLE\_WARNING(warning) TOOLCHAIN\_PRAGMA(diag\_default = warning)

13

14#define TOOLCHAIN\_DISABLE\_WARNING(warning) \_TOOLCHAIN\_DISABLE\_WARNING(warning)

15#define TOOLCHAIN\_ENABLE\_WARNING(warning) \_TOOLCHAIN\_ENABLE\_WARNING(warning)

16#endif

17

18#ifdef \_\_ICCARM\_\_

19#include "[iar/iccarm.h](iccarm_8h.md)"

20#endif

21#ifdef \_\_ICCRISCV\_\_

22#include "iar/iccriscv.h"

23#endif

24

25#endif /\* ZEPHYR\_INCLUDE\_TOOLCHAIN\_ICCARM\_H\_ \*/

[iccarm.h](iccarm_8h.md)

ICCARM toolchain abstraction.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [iar.h](iar_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
