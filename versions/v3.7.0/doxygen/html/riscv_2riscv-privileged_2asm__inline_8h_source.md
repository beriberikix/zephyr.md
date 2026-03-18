---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/riscv_2riscv-privileged_2asm__inline_8h_source.html
original_path: doxygen/html/riscv_2riscv-privileged_2asm__inline_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

asm\_inline.h

[Go to the documentation of this file.](riscv_2riscv-privileged_2asm__inline_8h.md)

1/\*

2 \* Copyright (c) 2017 Jean-Paul Etienne <fractalclone@gmail.com>

3 \* Contributors: 2018 Antmicro <www.antmicro.com>

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_ARCH\_RISCV\_RISCV\_PRIVILEGED\_ASM\_INLINE\_H\_

9#define ZEPHYR\_INCLUDE\_ARCH\_RISCV\_RISCV\_PRIVILEGED\_ASM\_INLINE\_H\_

10

11/\*

12 \* The file must not be included directly

13 \* Include arch/cpu.h instead

14 \*/

15

16#if defined(\_\_GNUC\_\_)

17#include <[zephyr/arch/riscv/riscv-privileged/asm\_inline\_gcc.h](riscv_2riscv-privileged_2asm__inline__gcc_8h.md)>

18#else

19#error "Supports only GNU C compiler"

20#endif

21

22#endif /\* ZEPHYR\_INCLUDE\_ARCH\_RISCV\_RISCV\_PRIVILEGED\_ASM\_INLINE\_H\_ \*/

[asm\_inline\_gcc.h](riscv_2riscv-privileged_2asm__inline__gcc_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [riscv-privileged](dir_ed8add11e8adf9177aa6eb94d599d40b.md)
- [asm\_inline.h](riscv_2riscv-privileged_2asm__inline_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
