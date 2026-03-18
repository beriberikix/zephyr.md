---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/kernel_2smp_8h_source.html
original_path: doxygen/html/kernel_2smp_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smp.h

[Go to the documentation of this file.](kernel_2smp_8h.md)

1/\*

2 \* Copyright (c) 2023 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_KERNEL\_SMP\_H\_

8#define ZEPHYR\_INCLUDE\_KERNEL\_SMP\_H\_

9

10#include <[stdbool.h](stdbool_8h.md)>

11

[ 12](kernel_2smp_8h.md#abc49de5bf9e70f48e39f41c413f7cc74)typedef void (\*[smp\_init\_fn](kernel_2smp_8h.md#abc49de5bf9e70f48e39f41c413f7cc74))(void \*arg);

13

[ 40](kernel_2smp_8h.md#a33eb24503679583d853db1c4dc7e3812)void [k\_smp\_cpu\_start](kernel_2smp_8h.md#a33eb24503679583d853db1c4dc7e3812)(int id, [smp\_init\_fn](kernel_2smp_8h.md#abc49de5bf9e70f48e39f41c413f7cc74) fn, void \*arg);

41

[ 68](kernel_2smp_8h.md#a39b4f48857baef688ee646bac36c882d)void [k\_smp\_cpu\_resume](kernel_2smp_8h.md#a39b4f48857baef688ee646bac36c882d)(int id, [smp\_init\_fn](kernel_2smp_8h.md#abc49de5bf9e70f48e39f41c413f7cc74) fn, void \*arg,

69 bool reinit\_timer, bool invoke\_sched);

70

71#endif /\* ZEPHYR\_INCLUDE\_KERNEL\_SMP\_H\_ \*/

[k\_smp\_cpu\_start](kernel_2smp_8h.md#a33eb24503679583d853db1c4dc7e3812)

void k\_smp\_cpu\_start(int id, smp\_init\_fn fn, void \*arg)

Start a CPU.

[k\_smp\_cpu\_resume](kernel_2smp_8h.md#a39b4f48857baef688ee646bac36c882d)

void k\_smp\_cpu\_resume(int id, smp\_init\_fn fn, void \*arg, bool reinit\_timer, bool invoke\_sched)

Resume a previously suspended CPU.

[smp\_init\_fn](kernel_2smp_8h.md#abc49de5bf9e70f48e39f41c413f7cc74)

void(\* smp\_init\_fn)(void \*arg)

**Definition** smp.h:12

[stdbool.h](stdbool_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel](dir_87084789f4f879979d9b1b0acd11eedc.md)
- [smp.h](kernel_2smp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
