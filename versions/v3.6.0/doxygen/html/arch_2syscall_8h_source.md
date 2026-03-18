---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arch_2syscall_8h_source.html
original_path: doxygen/html/arch_2syscall_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

syscall.h

[Go to the documentation of this file.](arch_2syscall_8h.md)

1/\* syscall.h - automatically selects the correct syscall.h file to include \*/

2

3/\*

4 \* Copyright (c) 1997-2014 Wind River Systems, Inc.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_INCLUDE\_ARCH\_SYSCALL\_H\_

10#define ZEPHYR\_INCLUDE\_ARCH\_SYSCALL\_H\_

11

12#if defined(CONFIG\_X86)

13#if defined(CONFIG\_X86\_64)

14#include <[zephyr/arch/x86/intel64/syscall.h](arch_2x86_2intel64_2syscall_8h.md)>

15#else

16#include <[zephyr/arch/x86/ia32/syscall.h](arch_2x86_2ia32_2syscall_8h.md)>

17#endif

18#elif defined(CONFIG\_ARM64)

19#include <[zephyr/arch/arm64/syscall.h](arch_2arm64_2syscall_8h.md)>

20#elif defined(CONFIG\_ARM)

21#include <[zephyr/arch/arm/syscall.h](arch_2arm_2syscall_8h.md)>

22#elif defined(CONFIG\_ARC)

23#include <[zephyr/arch/arc/syscall.h](arch_2arc_2syscall_8h.md)>

24#elif defined(CONFIG\_RISCV)

25#include <[zephyr/arch/riscv/syscall.h](arch_2riscv_2syscall_8h.md)>

26#elif defined(CONFIG\_XTENSA)

27#include <[zephyr/arch/xtensa/syscall.h](arch_2xtensa_2syscall_8h.md)>

28#endif

29

30#endif /\* ZEPHYR\_INCLUDE\_ARCH\_SYSCALL\_H\_ \*/

[syscall.h](arch_2arc_2syscall_8h.md)

ARC specific syscall header.

[syscall.h](arch_2arm64_2syscall_8h.md)

ARM64 specific syscall header.

[syscall.h](arch_2arm_2syscall_8h.md)

ARM AArch32 specific syscall header.

[syscall.h](arch_2riscv_2syscall_8h.md)

RISCV specific syscall header.

[syscall.h](arch_2x86_2ia32_2syscall_8h.md)

x86 (IA32) specific syscall header

[syscall.h](arch_2x86_2intel64_2syscall_8h.md)

x86 (INTEL64) specific syscall header

[syscall.h](arch_2xtensa_2syscall_8h.md)

Xtensa specific syscall header.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [syscall.h](arch_2syscall_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
