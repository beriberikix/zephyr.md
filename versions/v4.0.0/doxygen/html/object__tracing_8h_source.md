---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/object__tracing_8h_source.html
original_path: doxygen/html/object__tracing_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

object\_tracing.h

[Go to the documentation of this file.](object__tracing_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_THREAD\_MONITOR\_H\_

8#define ZEPHYR\_INCLUDE\_THREAD\_MONITOR\_H\_

9

10#include <[zephyr/kernel.h](kernel_8h.md)>

11#include <[zephyr/kernel\_structs.h](kernel__structs_8h.md)>

12

[ 19](object__tracing_8h.md#aba3e9abb310c42fef67ce63cb2845046)#define SYS\_THREAD\_MONITOR\_HEAD ((struct k\_thread \*)(\_kernel.threads))

20

[ 29](object__tracing_8h.md#aefa138ca1b427f994b994ebe1224764e)#define SYS\_THREAD\_MONITOR\_NEXT(obj) (((struct k\_thread \*)obj)->next\_thread)

30

31#endif /\* ZEPHYR\_INCLUDE\_THREAD\_MONITOR\_H\_ \*/

[kernel.h](kernel_8h.md)

Public kernel APIs.

[kernel\_structs.h](kernel__structs_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [debug](dir_44aa0acd5660d74ea205f18be43003ca.md)
- [object\_tracing.h](object__tracing_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
