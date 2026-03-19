---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/reg_8h_source.html
original_path: doxygen/html/reg_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

reg.h

[Go to the documentation of this file.](reg_8h.md)

1/\*

2 \* Copyright (c) 2024 Meta Platforms

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ZEPHYR\_ARCH\_RISCV\_REG\_H\_

8#define ZEPHYR\_INCLUDE\_ZEPHYR\_ARCH\_RISCV\_REG\_H\_

9

10#include <[zephyr/sys/util.h](sys_2util_8h.md)>

11

[ 12](reg_8h.md#aa57645f8a20e83b1ae1037cc3a81e1d1)#define reg\_read(reg) \

13 ({ \

14 register unsigned long \_\_rv; \

15 \_\_asm\_\_ volatile("mv %0, " STRINGIFY(reg) : "=r"(\_\_rv)); \

16 \_\_rv; \

17 })

18

[ 19](reg_8h.md#ab38fcaa2c682800f1bef4159e1949f47)#define reg\_write(reg, val) ({ \_\_asm\_\_("mv " STRINGIFY(reg) ", %0" : : "r"(val)); })

20

21#endif /\* ZEPHYR\_INCLUDE\_ZEPHYR\_ARCH\_RISCV\_REG\_H\_ \*/

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [reg.h](reg_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
