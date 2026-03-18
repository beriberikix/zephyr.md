---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/posix__arch__console_8h_source.html
original_path: doxygen/html/posix__arch__console_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

posix\_arch\_console.h

[Go to the documentation of this file.](posix__arch__console_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CONSOLE\_POSIX\_ARCH\_CONSOLE\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_CONSOLE\_POSIX\_ARCH\_CONSOLE\_H\_

9

10#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

[ 16](posix__arch__console_8h.md#a45e2c1fe69373f03c2ade38ced717328)void [posix\_flush\_stdout](posix__arch__console_8h.md#a45e2c1fe69373f03c2ade38ced717328)(void);

17

18#ifdef \_\_cplusplus

19}

20#endif

21

22#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CONSOLE\_POSIX\_ARCH\_CONSOLE\_H\_ \*/

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[posix\_flush\_stdout](posix__arch__console_8h.md#a45e2c1fe69373f03c2ade38ced717328)

void posix\_flush\_stdout(void)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [console](dir_5678202c8994e72aafde82bf91697a82.md)
- [posix\_arch\_console.h](posix__arch__console_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
