---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arch__inlines_8h_source.html
original_path: doxygen/html/arch__inlines_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch\_inlines.h

[Go to the documentation of this file.](arch__inlines_8h.md)

1/\*

2 \* arch\_inlines.h - automatically selects the correct arch\_inlines.h file to

3 \* include based on the selected architecture.

4 \*/

5

6/\*

7 \* Copyright (c) 2019 Stephanos Ioannidis <root@stephanos.io>

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_ARCH\_INLINES\_H\_

13#define ZEPHYR\_INCLUDE\_ARCH\_INLINES\_H\_

14

15#if defined(CONFIG\_X86) || defined(CONFIG\_X86\_64)

16#include <[zephyr/arch/x86/arch\_inlines.h](x86_2arch__inlines_8h.md)>

17#elif defined(CONFIG\_ARM)

18#include <[zephyr/arch/arm/arch\_inlines.h](arm_2arch__inlines_8h.md)>

19#elif defined(CONFIG\_ARM64)

20#include <[zephyr/arch/arm64/arch\_inlines.h](arm64_2arch__inlines_8h.md)>

21#elif defined(CONFIG\_ARC)

22#include <[zephyr/arch/arc/arch\_inlines.h](arc_2arch__inlines_8h.md)>

23#elif defined(CONFIG\_XTENSA)

24#include <[zephyr/arch/xtensa/arch\_inlines.h](xtensa_2arch__inlines_8h.md)>

25#elif defined(CONFIG\_RISCV)

26#include <[zephyr/arch/riscv/arch\_inlines.h](riscv_2arch__inlines_8h.md)>

27#elif defined(CONFIG\_NIOS2)

28#include <[zephyr/arch/nios2/arch\_inlines.h](nios2_2arch__inlines_8h.md)>

29#elif defined(CONFIG\_MIPS)

30#include <[zephyr/arch/mips/arch\_inlines.h](mips_2arch__inlines_8h.md)>

31#elif defined(CONFIG\_ARCH\_POSIX)

32#include <[zephyr/arch/posix/arch\_inlines.h](posix_2arch__inlines_8h.md)>

33#elif defined(CONFIG\_SPARC)

34#include <[zephyr/arch/sparc/arch\_inlines.h](sparc_2arch__inlines_8h.md)>

35#else

36#error "Unknown Architecture"

37#endif

38

39#endif /\* ZEPHYR\_INCLUDE\_ARCH\_INLINES\_H\_ \*/

[arch\_inlines.h](arc_2arch__inlines_8h.md)

[arch\_inlines.h](arm64_2arch__inlines_8h.md)

[arch\_inlines.h](arm_2arch__inlines_8h.md)

[arch\_inlines.h](mips_2arch__inlines_8h.md)

[arch\_inlines.h](nios2_2arch__inlines_8h.md)

[arch\_inlines.h](posix_2arch__inlines_8h.md)

[arch\_inlines.h](riscv_2arch__inlines_8h.md)

[arch\_inlines.h](sparc_2arch__inlines_8h.md)

[arch\_inlines.h](x86_2arch__inlines_8h.md)

[arch\_inlines.h](xtensa_2arch__inlines_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arch\_inlines.h](arch__inlines_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
