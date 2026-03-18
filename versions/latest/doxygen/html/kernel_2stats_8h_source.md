---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/kernel_2stats_8h_source.html
original_path: doxygen/html/kernel_2stats_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stats.h

[Go to the documentation of this file.](kernel_2stats_8h.md)

1/\*

2 \* Copyright (c) 2021,2023, Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_KERNEL\_STATS\_H\_

8#define ZEPHYR\_INCLUDE\_KERNEL\_STATS\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11#include <[stdbool.h](stdbool_8h.md)>

12

17

[ 18](structk__cycle__stats.md)struct [k\_cycle\_stats](structk__cycle__stats.md) {

[ 19](structk__cycle__stats.md#a1d49158db605872cd8d31225c0ae8ab5) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [total](structk__cycle__stats.md#a1d49158db605872cd8d31225c0ae8ab5);

20#if defined(CONFIG\_SCHED\_THREAD\_USAGE\_ANALYSIS) || defined(\_\_DOXYGEN\_\_)

[ 25](structk__cycle__stats.md#a9c12b140936bcc4a8630c68680a245b4) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [current](structk__cycle__stats.md#a9c12b140936bcc4a8630c68680a245b4);

[ 26](structk__cycle__stats.md#a161c8d21c7d4a3d21c7cce87237c8334) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [longest](structk__cycle__stats.md#a161c8d21c7d4a3d21c7cce87237c8334);

[ 27](structk__cycle__stats.md#acdb6a6b005384535607aaf1bc5dd3feb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [num\_windows](structk__cycle__stats.md#acdb6a6b005384535607aaf1bc5dd3feb);

29#endif

[ 30](structk__cycle__stats.md#a8a955f987ddc88ff587edab8cb71dd6f) bool [track\_usage](structk__cycle__stats.md#a8a955f987ddc88ff587edab8cb71dd6f);

31};

32

33#endif

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[k\_cycle\_stats](structk__cycle__stats.md)

Structure used to track internal statistics about both thread and CPU usage.

**Definition** stats.h:18

[k\_cycle\_stats::longest](structk__cycle__stats.md#a161c8d21c7d4a3d21c7cce87237c8334)

uint64\_t longest

# of cycles in longest usage window

**Definition** stats.h:26

[k\_cycle\_stats::total](structk__cycle__stats.md#a1d49158db605872cd8d31225c0ae8ab5)

uint64\_t total

total usage in cycles

**Definition** stats.h:19

[k\_cycle\_stats::track\_usage](structk__cycle__stats.md#a8a955f987ddc88ff587edab8cb71dd6f)

bool track\_usage

true if gathering usage stats

**Definition** stats.h:30

[k\_cycle\_stats::current](structk__cycle__stats.md#a9c12b140936bcc4a8630c68680a245b4)

uint64\_t current

# of cycles in current usage window

**Definition** stats.h:25

[k\_cycle\_stats::num\_windows](structk__cycle__stats.md#acdb6a6b005384535607aaf1bc5dd3feb)

uint32\_t num\_windows

# of usage windows

**Definition** stats.h:27

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel](dir_87084789f4f879979d9b1b0acd11eedc.md)
- [stats.h](kernel_2stats_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
