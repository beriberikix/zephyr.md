---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mips_2arch__inlines_8h_source.html
original_path: doxygen/html/mips_2arch__inlines_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch\_inlines.h

[Go to the documentation of this file.](mips_2arch__inlines_8h.md)

1/\*

2 \* Copyright (c) 2022 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_MIPS\_ARCH\_INLINES\_H

8#define ZEPHYR\_INCLUDE\_ARCH\_MIPS\_ARCH\_INLINES\_H

9

10#include <[zephyr/kernel\_structs.h](kernel__structs_8h.md)>

11

[ 12](mips_2arch__inlines_8h.md#a83c8ae933b0ec7d067569f17125c6a2c)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_num\_cpus](arc_2arch__inlines_8h.md#a83c8ae933b0ec7d067569f17125c6a2c)(void)

13{

14 return CONFIG\_MP\_MAX\_NUM\_CPUS;

15}

16

17#endif /\* ZEPHYR\_INCLUDE\_ARCH\_MIPS\_ARCH\_INLINES\_H \*/

[arch\_num\_cpus](arc_2arch__inlines_8h.md#a83c8ae933b0ec7d067569f17125c6a2c)

static ALWAYS\_INLINE unsigned int arch\_num\_cpus(void)

**Definition** arch\_inlines.h:39

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[kernel\_structs.h](kernel__structs_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [mips](dir_fc8c8ea71cc5b300c3fa15bb05243853.md)
- [arch\_inlines.h](mips_2arch__inlines_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
