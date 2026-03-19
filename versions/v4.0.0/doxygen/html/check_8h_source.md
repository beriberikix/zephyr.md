---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/check_8h_source.html
original_path: doxygen/html/check_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

check.h

[Go to the documentation of this file.](check_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7

8#ifndef ZEPHYR\_INCLUDE\_SYS\_CHECK\_H\_

9#define ZEPHYR\_INCLUDE\_SYS\_CHECK\_H\_

10

11#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

12

13#if defined(CONFIG\_ASSERT\_ON\_ERRORS)

14#define CHECKIF(expr) \

15 \_\_ASSERT\_NO\_MSG(!(expr)); \

16 if (0)

17#elif defined(CONFIG\_NO\_RUNTIME\_CHECKS)

18#define CHECKIF(...) \

19 if (0)

20#else

[ 21](check_8h.md#ac53803cb41bff9492f98fe0ac7ea1bc4)#define CHECKIF(expr) \

22 if (expr)

23#endif

24

25

26#endif /\* ZEPHYR\_INCLUDE\_SYS\_CHECK\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [check.h](check_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
