---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/poweroff_8h_source.html
original_path: doxygen/html/poweroff_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

poweroff.h

[Go to the documentation of this file.](poweroff_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SYS\_POWEROFF\_H\_

8#define ZEPHYR\_INCLUDE\_SYS\_POWEROFF\_H\_

9

10#include <[zephyr/toolchain.h](toolchain_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

21

23

30FUNC\_NORETURN void z\_sys\_poweroff(void);

31

33

35

[ 46](group__sys__poweroff.md#gaf4552a8ea40b4adb94f85b0a1ff06e39)FUNC\_NORETURN void [sys\_poweroff](group__sys__poweroff.md#gaf4552a8ea40b4adb94f85b0a1ff06e39)(void);

47

49

50#ifdef \_\_cplusplus

51}

52#endif

53

54#endif /\* ZEPHYR\_INCLUDE\_SYS\_POWEROFF\_H\_ \*/

[sys\_poweroff](group__sys__poweroff.md#gaf4552a8ea40b4adb94f85b0a1ff06e39)

FUNC\_NORETURN void sys\_poweroff(void)

Perform a system power off.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [poweroff.h](poweroff_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
