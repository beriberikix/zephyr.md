---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arm_2exception_8h_source.html
original_path: doxygen/html/arm_2exception_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exception.h

[Go to the documentation of this file.](arm_2exception_8h.md)

1/\*

2 \* Copyright (c) 2013-2014 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_EXCEPTION\_H\_

16#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_EXCEPTION\_H\_

17

18#if defined(CONFIG\_CPU\_CORTEX\_M)

19#include <[zephyr/arch/arm/cortex\_m/exception.h](arm_2cortex__m_2exception_8h.md)>

20#elif defined(CONFIG\_CPU\_AARCH32\_CORTEX\_A) || defined(CONFIG\_CPU\_AARCH32\_CORTEX\_R)

21#include <[zephyr/arch/arm/cortex\_a\_r/exception.h](arm_2cortex__a__r_2exception_8h.md)>

22#else

23#error Unknown ARM architecture

24#endif /\* CONFIG\_CPU\_CORTEX\_M \*/

25

26#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_EXCEPTION\_H\_ \*/

[exception.h](arm_2cortex__a__r_2exception_8h.md)

ARM AArch32 Cortex-A and Cortex-R public exception handling.

[exception.h](arm_2cortex__m_2exception_8h.md)

ARM AArch32 Cortex-M public exception handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [exception.h](arm_2exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
