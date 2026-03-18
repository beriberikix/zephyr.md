---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/mem__stats_8h_source.html
original_path: doxygen/html/mem__stats_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mem\_stats.h

[Go to the documentation of this file.](mem__stats_8h.md)

1/\*

2 \* Copyright (c) 2022 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef ZEPHYR\_INCLUDE\_SYS\_MEM\_STATS\_H\_

14#define ZEPHYR\_INCLUDE\_SYS\_MEM\_STATS\_H\_

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

20#include <stddef.h>

21

22/\* A common structure used to report runtime memory usage statistics \*/

23

[ 24](structsys__memory__stats.md)struct [sys\_memory\_stats](structsys__memory__stats.md) {

[ 25](structsys__memory__stats.md#aeb79d9aad2232b3451737b8fdb335132) size\_t [free\_bytes](structsys__memory__stats.md#aeb79d9aad2232b3451737b8fdb335132);

[ 26](structsys__memory__stats.md#a5592af7e45f38f79447fd8b81cfa1285) size\_t [allocated\_bytes](structsys__memory__stats.md#a5592af7e45f38f79447fd8b81cfa1285);

[ 27](structsys__memory__stats.md#a0d89b378e4e3974c4ca778040eb34697) size\_t [max\_allocated\_bytes](structsys__memory__stats.md#a0d89b378e4e3974c4ca778040eb34697);

28};

29

30#ifdef \_\_cplusplus

31}

32#endif

33

34#endif /\* ZEPHYR\_INCLUDE\_SYS\_MEM\_STATS\_H\_ \*/

[sys\_memory\_stats](structsys__memory__stats.md)

**Definition** mem\_stats.h:24

[sys\_memory\_stats::max\_allocated\_bytes](structsys__memory__stats.md#a0d89b378e4e3974c4ca778040eb34697)

size\_t max\_allocated\_bytes

**Definition** mem\_stats.h:27

[sys\_memory\_stats::allocated\_bytes](structsys__memory__stats.md#a5592af7e45f38f79447fd8b81cfa1285)

size\_t allocated\_bytes

**Definition** mem\_stats.h:26

[sys\_memory\_stats::free\_bytes](structsys__memory__stats.md#aeb79d9aad2232b3451737b8fdb335132)

size\_t free\_bytes

**Definition** mem\_stats.h:25

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [mem\_stats.h](mem__stats_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
