---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/posix_2asm__inline__gcc_8h_source.html
original_path: doxygen/html/posix_2asm__inline__gcc_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

asm\_inline\_gcc.h

[Go to the documentation of this file.](posix_2asm__inline__gcc_8h.md)

1/\*

2 \* Copyright (c) 2015, Wind River Systems, Inc.

3 \* Copyright (c) 2017, Oticon A/S

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8/\*

9 \* POSIX ARCH specific public inline "assembler" functions and macros

10 \*/

11

12/\* Either public functions or macros or invoked by public functions \*/

13

14#ifndef ZEPHYR\_INCLUDE\_ARCH\_POSIX\_ASM\_INLINE\_GCC\_H\_

15#define ZEPHYR\_INCLUDE\_ARCH\_POSIX\_ASM\_INLINE\_GCC\_H\_

16

17/\*

18 \* The file must not be included directly

19 \* Include kernel.h instead

20 \*/

21

22#ifndef \_ASMLANGUAGE

23

24#include <[zephyr/toolchain/common.h](include_2zephyr_2toolchain_2common_8h.md)>

25#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

26#include <[zephyr/arch/common/sys\_bitops.h](sys__bitops_8h.md)>

27#include <[zephyr/arch/common/sys\_io.h](arch_2common_2sys__io_8h.md)>

28#include <[zephyr/arch/common/ffs.h](ffs_8h.md)>

29#include <[zephyr/arch/posix/posix\_soc\_if.h](posix__soc__if_8h.md)>

30

31#endif /\* \_ASMLANGUAGE \*/

32

33#endif /\* ZEPHYR\_INCLUDE\_ARCH\_POSIX\_ASM\_INLINE\_GCC\_H\_ \*/

[sys\_io.h](arch_2common_2sys__io_8h.md)

[ffs.h](ffs_8h.md)

[common.h](include_2zephyr_2toolchain_2common_8h.md)

Common toolchain abstraction.

[types.h](include_2zephyr_2types_8h.md)

[posix\_soc\_if.h](posix__soc__if_8h.md)

[sys\_bitops.h](sys__bitops_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [posix](dir_2eaa0886f2679378503a1f6e740c4205.md)
- [asm\_inline\_gcc.h](posix_2asm__inline__gcc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
