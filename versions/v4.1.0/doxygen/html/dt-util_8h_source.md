---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dt-util_8h_source.html
original_path: doxygen/html/dt-util_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dt-util.h

[Go to the documentation of this file.](dt-util_8h.md)

1/\*

2 \* Copyright (c) 2020 Gerson Fernando Budke <nandojve@gmail.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_DT\_UTIL\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_DT\_UTIL\_H\_

9

10/\*

11 \* This file exists to keep in-tree DTS clean. This means, only

12 \* #include <zephyr/dt-bindings/foo.h> form should be included. The

13 \* <zephyr/dt-bindings/dt-util.h> wraps <zephyr/sys/util\_macro.h> file exposing

14 \* all macro base definitions to DTS preprocessor. It provides

15 \* necessary background to elaborate complex constructions like

16 \* variable length macros with zero or more elements.

17 \*/

18

19#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

20

21#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_DT\_UTIL\_H\_ \*/

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dt-util.h](dt-util_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
