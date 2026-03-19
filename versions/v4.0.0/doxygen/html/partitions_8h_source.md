---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/partitions_8h_source.html
original_path: doxygen/html/partitions_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

partitions.h

[Go to the documentation of this file.](partitions_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_APP\_MEMORY\_PARTITIONS\_H

8#define ZEPHYR\_APP\_MEMORY\_PARTITIONS\_H

9

10#ifdef CONFIG\_USERSPACE

11#include <[zephyr/kernel.h](kernel_8h.md)> /\* For struct k\_mem\_partition \*/

12

13#if defined(CONFIG\_MBEDTLS)

14extern struct [k\_mem\_partition](structk__mem__partition.md) k\_mbedtls\_partition;

15#endif /\* CONFIG\_MBEDTLS \*/

16#endif /\* CONFIG\_USERSPACE \*/

17#endif /\* ZEPHYR\_APP\_MEMORY\_PARTITIONS\_H \*/

[kernel.h](kernel_8h.md)

Public kernel APIs.

[k\_mem\_partition](structk__mem__partition.md)

Memory Partition.

**Definition** mem\_domain.h:55

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [app\_memory](dir_a5c66281f93d933ad709643c33992dc2.md)
- [partitions.h](partitions_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
