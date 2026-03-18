---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/gcov_8h_source.html
original_path: doxygen/html/gcov_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gcov.h

[Go to the documentation of this file.](gcov_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DEBUG\_GCOV\_H\_

8#define ZEPHYR\_INCLUDE\_DEBUG\_GCOV\_H\_

9

10#ifdef CONFIG\_COVERAGE\_GCOV

11void [gcov\_coverage\_dump](gcov_8h.md#afb216a4858e24e8db6d37a4c578e86c5)(void);

12void [gcov\_static\_init](gcov_8h.md#a4f6365ac097d037c6e41852e34e5bbfb)(void);

13#else

[ 14](gcov_8h.md#afb216a4858e24e8db6d37a4c578e86c5)static inline void [gcov\_coverage\_dump](gcov_8h.md#afb216a4858e24e8db6d37a4c578e86c5)(void) { }

[ 15](gcov_8h.md#a4f6365ac097d037c6e41852e34e5bbfb)static inline void [gcov\_static\_init](gcov_8h.md#a4f6365ac097d037c6e41852e34e5bbfb)(void) { }

16

17#endif /\* CONFIG\_COVERAGE\_GCOV \*/

18

19#endif /\* ZEPHYR\_INCLUDE\_DEBUG\_GCOV\_H\_ \*/

[gcov\_static\_init](gcov_8h.md#a4f6365ac097d037c6e41852e34e5bbfb)

static void gcov\_static\_init(void)

**Definition** gcov.h:15

[gcov\_coverage\_dump](gcov_8h.md#afb216a4858e24e8db6d37a4c578e86c5)

static void gcov\_coverage\_dump(void)

**Definition** gcov.h:14

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [debug](dir_44aa0acd5660d74ea205f18be43003ca.md)
- [gcov.h](gcov_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
