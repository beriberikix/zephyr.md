---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/tool-compat_8h_source.html
original_path: doxygen/html/tool-compat_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tool-compat.h

[Go to the documentation of this file.](tool-compat_8h.md)

1/\*

2 \* Copyright (c) 2020 Synopsys.

3 \* Author: Eugeniy Paltsev <Eugeniy.Paltsev@synopsys.com>

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARC\_TOOL\_COMPAT\_H\_

9#define ZEPHYR\_INCLUDE\_ARCH\_ARC\_TOOL\_COMPAT\_H\_

10

11#ifdef \_ASMLANGUAGE

12/\*

13 \* GNU toolchain and MWDT (Metware) toolchain have different style for accessing

14 \* arguments in assembly macro. Here is the preprocessor macro to handle the

15 \* difference.

16 \* \_\_CCAC\_\_ is a pre-defined macro of metaware compiler.

17 \*/

18#if defined(\_\_CCAC\_\_)

19#define MACRO\_ARG(x) x

20#else

21#define MACRO\_ARG(x) \x

22#endif

23

24#endif /\* \_ASMLANGUAGE \*/

25#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARC\_TOOL\_COMPAT\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [tool-compat.h](tool-compat_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
