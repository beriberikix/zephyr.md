---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/posix_2exception_8h_source.html
original_path: doxygen/html/posix_2exception_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exception.h

[Go to the documentation of this file.](posix_2exception_8h.md)

1/\*

2 \* Copyright (c) 2010-2014 Wind River Systems, Inc.

3 \* Copyright (c) 2017 Oticon A/S

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_ARCH\_POSIX\_EXCEPTION\_H\_

9#define ZEPHYR\_INCLUDE\_ARCH\_POSIX\_EXCEPTION\_H\_

10

11#ifndef \_ASMLANGUAGE

12#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

18struct [arch\_esf](structarch__esf.md) {

[ 19](structarch__esf.md#ae44a189aed30d7bd9cbb860f7c177d4d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dummy](structarch__esf.md#ae44a189aed30d7bd9cbb860f7c177d4d); /\*maybe we will want to add something someday\*/

20};

21

22#ifdef \_\_cplusplus

23}

24#endif

25

26#endif /\* \_ASMLANGUAGE \*/

27

28#endif /\* ZEPHYR\_INCLUDE\_ARCH\_POSIX\_EXCEPTION\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[arch\_esf](structarch__esf.md)

Exception Stack Frame.

**Definition** exception.h:60

[arch\_esf::dummy](structarch__esf.md#ae44a189aed30d7bd9cbb860f7c177d4d)

uint32\_t dummy

**Definition** exception.h:19

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [posix](dir_2eaa0886f2679378503a1f6e740c4205.md)
- [exception.h](posix_2exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
