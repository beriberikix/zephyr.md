---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/nmi_8h_source.html
original_path: doxygen/html/nmi_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nmi.h

[Go to the documentation of this file.](nmi_8h.md)

1

6

7/\*

8 \* Copyright (c) 2015 Intel Corporation

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_NMI\_H\_

14#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_NMI\_H\_

15

16#if !defined(\_ASMLANGUAGE) && defined(CONFIG\_RUNTIME\_NMI)

17extern void z\_arm\_nmi\_set\_handler(void (\*pHandler)(void));

18#endif

19

20#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_NMI\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [nmi.h](nmi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
