---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/addr__types_8h_source.html
original_path: doxygen/html/addr__types_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

addr\_types.h

[Go to the documentation of this file.](addr__types_8h.md)

1/\* x86 address types (virtual, physical, etc) definitions \*/

2

3/\*

4 \* Copyright (c) 2015 Wind River Systems, Inc.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_ADDR\_TYPES\_H\_

10#define ZEPHYR\_INCLUDE\_ARCH\_X86\_ADDR\_TYPES\_H\_

11

12#ifndef \_ASMLANGUAGE

[ 13](addr__types_8h.md#a59897e9d2af1ab86597c1f4cfa994365)typedef [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [paddr\_t](addr__types_8h.md#a59897e9d2af1ab86597c1f4cfa994365);

[ 14](addr__types_8h.md#a96329c9b2410bdd79046e2529238a30f)typedef void \*[vaddr\_t](addr__types_8h.md#a96329c9b2410bdd79046e2529238a30f);

15#endif

16

17#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_ADDR\_TYPES\_H\_ \*/

[paddr\_t](addr__types_8h.md#a59897e9d2af1ab86597c1f4cfa994365)

uintptr\_t paddr\_t

**Definition** addr\_types.h:13

[vaddr\_t](addr__types_8h.md#a96329c9b2410bdd79046e2529238a30f)

void \* vaddr\_t

**Definition** addr\_types.h:14

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [common](dir_7cbd25c8850fe30be392200e83a608be.md)
- [addr\_types.h](addr__types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
