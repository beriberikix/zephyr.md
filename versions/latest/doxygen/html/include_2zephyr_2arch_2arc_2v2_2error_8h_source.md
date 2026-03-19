---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/include_2zephyr_2arch_2arc_2v2_2error_8h_source.html
original_path: doxygen/html/include_2zephyr_2arch_2arc_2v2_2error_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

error.h

[Go to the documentation of this file.](include_2zephyr_2arch_2arc_2v2_2error_8h.md)

1/\*

2 \* Copyright (c) 2014 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_ERROR\_H\_

15#define ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_ERROR\_H\_

16

17#include <[zephyr/arch/arc/syscall.h](arch_2arc_2syscall_8h.md)>

18#include <[zephyr/arch/arc/v2/exception.h](arc_2v2_2exception_8h.md)>

19#include <[stdbool.h](stdbool_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

25/\*

26 \* use trap\_s to raise a SW exception

27 \*/

[ 28](include_2zephyr_2arch_2arc_2v2_2error_8h.md#a8d3604770d7735d229e7d2fef4ff590a)#define ARCH\_EXCEPT(reason\_p) do { \

29 \_\_asm\_\_ volatile ( \

30 "mov %%r0, %[reason]\n\t" \

31 "trap\_s %[id]\n\t" \

32 : \

33 : [reason] "i" (reason\_p), \

34 [id] "i" (\_TRAP\_S\_CALL\_RUNTIME\_EXCEPT) \

35 : "memory"); \

36 CODE\_UNREACHABLE; /\* LCOV\_EXCL\_LINE \*/ \

37 } while (false)

38

39#ifdef \_\_cplusplus

40}

41#endif

42

43

44#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_ERROR\_H\_ \*/

[exception.h](arc_2v2_2exception_8h.md)

ARCv2 public exception handling.

[syscall.h](arch_2arc_2syscall_8h.md)

ARC specific syscall header.

[stdbool.h](stdbool_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [error.h](include_2zephyr_2arch_2arc_2v2_2error_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
