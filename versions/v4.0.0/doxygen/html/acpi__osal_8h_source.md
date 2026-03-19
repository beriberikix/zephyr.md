---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/acpi__osal_8h_source.html
original_path: doxygen/html/acpi__osal_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

acpi\_osal.h

[Go to the documentation of this file.](acpi__osal_8h.md)

1/\*

2 \* Copyright (c) 2023 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_ARCH\_X86\_INCLUDE\_ACPI\_OSAL\_H\_

8#define ZEPHYR\_ARCH\_X86\_INCLUDE\_ACPI\_OSAL\_H\_

9

10#if defined(CONFIG\_X86 || CONFIG\_X86\_64)

11#include <zephyr/acpi/x86\_acpi\_osal.h>

12#else

13#error "Currently only x86 Architecture support ACPI !!"

14#endif

15

16#endif /\* ZEPHYR\_ARCH\_X86\_INCLUDE\_ACPI\_OSAL\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [acpi](dir_45b4545ed375318b7880b8f15b111e07.md)
- [acpi\_osal.h](acpi__osal_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
