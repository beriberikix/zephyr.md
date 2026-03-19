---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/exception_8h_source.html
original_path: doxygen/html/exception_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exception.h

[Go to the documentation of this file.](exception_8h.md)

1/\* exception.h - automatically selects the correct exception.h file to include \*/

2

3/\*

4 \* Copyright (c) 2024 Meta Platforms

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_ARCH\_EXCEPTION\_H\_

9#define ZEPHYR\_INCLUDE\_ARCH\_EXCEPTION\_H\_

10

11#if defined(CONFIG\_X86\_64)

12#include <[zephyr/arch/x86/intel64/exception.h](x86_2intel64_2exception_8h.md)>

13#elif defined(CONFIG\_X86)

14#include <[zephyr/arch/x86/ia32/exception.h](x86_2ia32_2exception_8h.md)>

15#elif defined(CONFIG\_ARM64)

16#include <[zephyr/arch/arm64/exception.h](arm64_2exception_8h.md)>

17#elif defined(CONFIG\_ARM)

18#include <[zephyr/arch/arm/exception.h](arm_2exception_8h.md)>

19#elif defined(CONFIG\_ARC)

20#include <[zephyr/arch/arc/v2/exception.h](arc_2v2_2exception_8h.md)>

21#elif defined(CONFIG\_NIOS2)

22#include <[zephyr/arch/nios2/exception.h](nios2_2exception_8h.md)>

23#elif defined(CONFIG\_RISCV)

24#include <[zephyr/arch/riscv/exception.h](riscv_2exception_8h.md)>

25#elif defined(CONFIG\_XTENSA)

26#include <[zephyr/arch/xtensa/exception.h](xtensa_2exception_8h.md)>

27#elif defined(CONFIG\_MIPS)

28#include <[zephyr/arch/mips/exception.h](mips_2exception_8h.md)>

29#elif defined(CONFIG\_ARCH\_POSIX)

30#include <[zephyr/arch/posix/exception.h](posix_2exception_8h.md)>

31#elif defined(CONFIG\_SPARC)

32#include <[zephyr/arch/sparc/exception.h](sparc_2exception_8h.md)>

33#endif

34

35#endif /\* ZEPHYR\_INCLUDE\_ARCH\_EXCEPTION\_H\_ \*/

[exception.h](arc_2v2_2exception_8h.md)

ARCv2 public exception handling.

[exception.h](arm64_2exception_8h.md)

Cortex-A public exception handling.

[exception.h](arm_2exception_8h.md)

ARM AArch32 public exception handling.

[exception.h](mips_2exception_8h.md)

[exception.h](nios2_2exception_8h.md)

[exception.h](posix_2exception_8h.md)

[exception.h](riscv_2exception_8h.md)

RISCV public exception handling.

[exception.h](sparc_2exception_8h.md)

[exception.h](x86_2ia32_2exception_8h.md)

[exception.h](x86_2intel64_2exception_8h.md)

[exception.h](xtensa_2exception_8h.md)

Xtensa public exception handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [exception.h](exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
