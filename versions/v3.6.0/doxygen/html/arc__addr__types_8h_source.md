---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arc__addr__types_8h_source.html
original_path: doxygen/html/arc__addr__types_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arc\_addr\_types.h

[Go to the documentation of this file.](arc__addr__types_8h.md)

1/\*

2 \* Copyright (c) 2021 Synopsys.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARC\_ADDR\_TYPES\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_ARC\_ADDR\_TYPES\_H\_

9#ifndef \_ASMLANGUAGE

10

11/\*

12 \* MWDT provides paddr\_t type and it conflicts with Zephyr definition:

13 \* - Zephyr defines paddr\_t as a uintptr\_t

14 \* - MWDT defines paddr\_t as a unsigned long

15 \* This causes extra warnings. However we can safely define

16 \* paddr\_t as a unsigned long for the case when MWDT toolchain is used as

17 \* they are both unsigned, have same size and aligning.

18 \*/

19#ifdef \_\_CCAC\_\_

20typedef unsigned long [paddr\_t](addr__types_8h.md#a59897e9d2af1ab86597c1f4cfa994365);

21typedef void \*[vaddr\_t](addr__types_8h.md#a96329c9b2410bdd79046e2529238a30f);

22#else

23#include <[zephyr/arch/common/addr\_types.h](addr__types_8h.md)>

24#endif

25

26#endif /\* \_ASMLANGUAGE \*/

27#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARC\_ADDR\_TYPES\_H\_ \*/

[addr\_types.h](addr__types_8h.md)

[paddr\_t](addr__types_8h.md#a59897e9d2af1ab86597c1f4cfa994365)

uintptr\_t paddr\_t

**Definition** addr\_types.h:13

[vaddr\_t](addr__types_8h.md#a96329c9b2410bdd79046e2529238a30f)

void \* vaddr\_t

**Definition** addr\_types.h:14

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [arc\_addr\_types.h](arc__addr__types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
