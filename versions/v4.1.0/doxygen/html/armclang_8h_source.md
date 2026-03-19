---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/armclang_8h_source.html
original_path: doxygen/html/armclang_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

armclang.h

[Go to the documentation of this file.](armclang_8h.md)

1/\*

2 \* Copyright (c) 2021 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_TOOLCHAIN\_ARMCLANG\_H\_

8#define ZEPHYR\_INCLUDE\_TOOLCHAIN\_ARMCLANG\_H\_

9

10#ifndef ZEPHYR\_INCLUDE\_TOOLCHAIN\_H\_

11#error Please do not include toolchain-specific headers directly, use <zephyr/toolchain.h> instead

12#endif

13

14#include <[zephyr/toolchain/llvm.h](llvm_8h.md)>

15

16/\*

17 \* To reuse as much as possible from the llvm.h header we only redefine the

18 \* \_\_GENERIC\_SECTION and Z\_GENERIC\_SECTION macros here to include the `used` keyword.

19 \*/

20#undef \_\_GENERIC\_SECTION

21#undef Z\_GENERIC\_SECTION

22

23#define \_\_GENERIC\_SECTION(segment) \_\_attribute\_\_((section(STRINGIFY(segment)), used))

24#define Z\_GENERIC\_SECTION(segment) \_\_GENERIC\_SECTION(segment)

25

26#endif /\* ZEPHYR\_INCLUDE\_TOOLCHAIN\_ARMCLANG\_H\_ \*/

[llvm.h](llvm_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [armclang.h](armclang_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
