---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arm64_2error_8h_source.html
original_path: doxygen/html/arm64_2error_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

error.h

[Go to the documentation of this file.](arm64_2error_8h.md)

1/\*

2 \* Copyright (c) 2020 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM64\_ERROR\_H\_

15#define ZEPHYR\_INCLUDE\_ARCH\_ARM64\_ERROR\_H\_

16

17#include <[zephyr/arch/arm64/syscall.h](arch_2arm64_2syscall_8h.md)>

18#include <[zephyr/arch/arm64/exception.h](arm64_2exception_8h.md)>

19#include <[stdbool.h](stdbool_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

[ 25](arm64_2error_8h.md#a8d3604770d7735d229e7d2fef4ff590a)#define ARCH\_EXCEPT(reason\_p) \

26do { \

27 register uint64\_t x8 \_\_asm\_\_("x8") = reason\_p; \

28 \

29 \_\_asm\_\_ volatile("svc %[id]\n" \

30 : \

31 : [id] "i" (\_SVC\_CALL\_RUNTIME\_EXCEPT), \

32 "r" (x8) \

33 : "memory"); \

34} while (false)

35

36#ifdef \_\_cplusplus

37}

38#endif

39

40#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM64\_ERROR\_H\_ \*/

[syscall.h](arch_2arm64_2syscall_8h.md)

ARM64 specific syscall header.

[exception.h](arm64_2exception_8h.md)

Cortex-A public exception handling.

[stdbool.h](stdbool_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [error.h](arm64_2error_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
