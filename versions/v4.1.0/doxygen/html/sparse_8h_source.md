---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sparse_8h_source.html
original_path: doxygen/html/sparse_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sparse.h

[Go to the documentation of this file.](sparse_8h.md)

1/\*

2 \* Copyright (c) 2022 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DEBUG\_SPARSE\_H

8#define ZEPHYR\_INCLUDE\_DEBUG\_SPARSE\_H

9

10#if defined(\_\_CHECKER\_\_)

11#define \_\_sparse\_cache \_\_attribute\_\_((address\_space(\_\_cache)))

12#define \_\_sparse\_force \_\_attribute\_\_((force))

13#else

14#define \_\_sparse\_cache

15#define \_\_sparse\_force

16#endif

17

18#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [debug](dir_44aa0acd5660d74ea205f18be43003ca.md)
- [sparse.h](sparse_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
