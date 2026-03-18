---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arc_2v2_2asm__inline__gcc_8h_source.html
original_path: doxygen/html/arc_2v2_2asm__inline__gcc_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

asm\_inline\_gcc.h

[Go to the documentation of this file.](arc_2v2_2asm__inline__gcc_8h.md)

1/\* asm\_inline\_gcc.h - ARC inline assembler and macros for public functions \*/

2

3/\*

4 \* Copyright (c) 2015 Intel Corporation.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_ASM\_INLINE\_GCC\_H\_

10#define ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_ASM\_INLINE\_GCC\_H\_

11

12#ifndef \_ASMLANGUAGE

13

14#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

15#include <stddef.h>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

21

25extern [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) z\_tsc\_read(void);

26

27#ifdef \_\_cplusplus

28}

29#endif

30

31#endif /\* \_ASMLANGUAGE \*/

32

33#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_ASM\_INLINE\_GCC\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [asm\_inline\_gcc.h](arc_2v2_2asm__inline__gcc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
