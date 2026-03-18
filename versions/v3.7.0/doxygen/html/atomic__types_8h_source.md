---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/atomic__types_8h_source.html
original_path: doxygen/html/atomic__types_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

atomic\_types.h

[Go to the documentation of this file.](atomic__types_8h.md)

1/\* Copyright (c) 1997-2015, Wind River Systems, Inc.

2 \* Copyright (c) 2021 Intel Corporation

3 \* Copyright (c) 2023 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_SYS\_ATOMIC\_TYPES\_H\_

9#define ZEPHYR\_INCLUDE\_SYS\_ATOMIC\_TYPES\_H\_

10

11#ifdef \_\_cplusplus

12extern "C" {

13#endif

14

[ 15](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)typedef long [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8);

[ 16](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1)typedef [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1);

[ 17](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7)typedef void \*[atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7);

[ 18](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4)typedef [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4);

19

20#ifdef \_\_cplusplus

21}

22#endif

23

24#endif /\* ZEPHYR\_INCLUDE\_SYS\_ATOMIC\_TYPES\_H\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1)

atomic\_t atomic\_val\_t

**Definition** atomic\_types.h:16

[atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4)

atomic\_ptr\_t atomic\_ptr\_val\_t

**Definition** atomic\_types.h:18

[atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7)

void \* atomic\_ptr\_t

**Definition** atomic\_types.h:17

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [atomic\_types.h](atomic__types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
