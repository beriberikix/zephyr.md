---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/cpu_8h_source.html
original_path: doxygen/html/cpu_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cpu.h

[Go to the documentation of this file.](cpu_8h.md)

1/\* cpu.h - automatically selects the correct arch.h file to include \*/

2

3/\*

4 \* Copyright (c) 1997-2014 Wind River Systems, Inc.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_INCLUDE\_ARCH\_CPU\_H\_

10#define ZEPHYR\_INCLUDE\_ARCH\_CPU\_H\_

11

12#include <[zephyr/arch/arch\_interface.h](arch__interface_8h.md)>

13

14#if defined(CONFIG\_X86)

15#include <[zephyr/arch/x86/arch.h](x86_2arch_8h.md)>

16#elif defined(CONFIG\_ARM64)

17#include <[zephyr/arch/arm64/arch.h](arm64_2arch_8h.md)>

18#elif defined(CONFIG\_ARM)

19#include <[zephyr/arch/arm/arch.h](arm_2arch_8h.md)>

20#elif defined(CONFIG\_ARC)

21#include <[zephyr/arch/arc/arch.h](arc_2arch_8h.md)>

22#elif defined(CONFIG\_NIOS2)

23#include <[zephyr/arch/nios2/arch.h](nios2_2arch_8h.md)>

24#elif defined(CONFIG\_RISCV)

25#include <[zephyr/arch/riscv/arch.h](riscv_2arch_8h.md)>

26#elif defined(CONFIG\_XTENSA)

27#include <[zephyr/arch/xtensa/arch.h](xtensa_2arch_8h.md)>

28#elif defined(CONFIG\_MIPS)

29#include <[zephyr/arch/mips/arch.h](mips_2arch_8h.md)>

30#elif defined(CONFIG\_ARCH\_POSIX)

31#include <[zephyr/arch/posix/arch.h](posix_2arch_8h.md)>

32#elif defined(CONFIG\_SPARC)

33#include <[zephyr/arch/sparc/arch.h](sparc_2arch_8h.md)>

34#endif

35

36#endif /\* ZEPHYR\_INCLUDE\_ARCH\_CPU\_H\_ \*/

[arch.h](arc_2arch_8h.md)

ARC specific kernel interface header.

[arch\_interface.h](arch__interface_8h.md)

[arch.h](arm64_2arch_8h.md)

ARM64 specific kernel interface header.

[arch.h](arm_2arch_8h.md)

ARM AArch32 specific kernel interface header.

[arch.h](mips_2arch_8h.md)

[arch.h](nios2_2arch_8h.md)

Nios II specific kernel interface header This header contains the Nios II specific kernel interface.

[arch.h](posix_2arch_8h.md)

POSIX arch specific kernel interface header This header contains the POSIX arch specific kernel inter...

[arch.h](riscv_2arch_8h.md)

RISCV specific kernel interface header This header contains the RISCV specific kernel interface.

[arch.h](sparc_2arch_8h.md)

SPARC specific kernel interface header This header contains the SPARC specific kernel interface.

[arch.h](x86_2arch_8h.md)

[arch.h](xtensa_2arch_8h.md)

Xtensa specific kernel interface header This header contains the Xtensa specific kernel interface.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [cpu.h](cpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
