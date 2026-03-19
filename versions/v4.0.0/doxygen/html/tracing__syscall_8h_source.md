---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/tracing__syscall_8h_source.html
original_path: doxygen/html/tracing__syscall_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tracing\_syscall.h

[Go to the documentation of this file.](tracing__syscall_8h.md)

1/\*

2 \* Copyright (c) 2021 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_TRACING\_SYSCALL\_H\_

8#define ZEPHYR\_INCLUDE\_TRACING\_SYSCALL\_H\_

9

10#if defined CONFIG\_SEGGER\_SYSTEMVIEW

11#include "tracing\_sysview\_syscall.h"

12#elif defined CONFIG\_TRACING\_TEST

13#include "tracing\_test\_syscall.h"

14#else

15

22

[ 29](group__subsys__tracing__apis__syscall.md#ga5526336abc0394bd8d8c7541473ad4ef)#define sys\_port\_trace\_syscall\_enter(id, name, ...)

30

[ 38](group__subsys__tracing__apis__syscall.md#gaed9dc749bc6da68e4df2ba9cd098f863)#define sys\_port\_trace\_syscall\_exit(id, name, ...)

39 /\* end of subsys\_tracing\_syscall\_apis \*/

41

42#endif

43

44#endif /\* ZEPHYR\_INCLUDE\_TRACING\_SYSCALL\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [tracing](dir_c5f5a3ad31e756e37640fc6557a06392.md)
- [tracing\_syscall.h](tracing__syscall_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
