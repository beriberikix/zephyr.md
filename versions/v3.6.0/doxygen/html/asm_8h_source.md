---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/asm_8h_source.html
original_path: doxygen/html/asm_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

asm.h

[Go to the documentation of this file.](asm_8h.md)

1/\* asm.h - x86 tool dependent headers \*/

2

3/\*

4 \* Copyright (c) 2007-2014 Wind River Systems, Inc.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_ASM\_H\_

10#define ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_ASM\_H\_

11

12#include <[zephyr/toolchain.h](toolchain_8h.md)>

13#include <[zephyr/linker/sections.h](sections_8h.md)>

14

15#if defined(\_ASMLANGUAGE)

16

17#ifdef CONFIG\_X86\_KPTI

18GTEXT(z\_x86\_trampoline\_to\_user)

19GTEXT(z\_x86\_trampoline\_to\_kernel)

20

21#define KPTI\_IRET jmp z\_x86\_trampoline\_to\_user

22#define KPTI\_IRET\_USER jmp z\_x86\_trampoline\_to\_user\_always

23#else

24#define KPTI\_IRET iret

25#define KPTI\_IRET\_USER iret

26#endif /\* CONFIG\_X86\_KPTI \*/

27

28#endif /\* \_ASMLANGUAGE \*/

29

30#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_ASM\_H\_ \*/

[sections.h](sections_8h.md)

Definitions of various linker Sections.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [ia32](dir_b429dacf948f53b894465a48d17dcb95.md)
- [asm.h](asm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
