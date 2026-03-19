---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/grp_8h_source.html
original_path: doxygen/html/grp_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

grp.h

[Go to the documentation of this file.](grp_8h.md)

1/\*

2 \* Copyright (c) 2024 Meta Platforms

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_GRP\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_GRP\_H\_

8

9#ifdef \_\_cplusplus

10extern "C" {

11#endif

12

13#include <[zephyr/posix/sys/stat.h](stat_8h.md)>

14

[ 18](structgroup.md)struct [group](structgroup.md) {

[ 20](structgroup.md#a828b9f3708aa76cecd8fda0a20b61e98) char \*[gr\_name](structgroup.md#a828b9f3708aa76cecd8fda0a20b61e98);

[ 22](structgroup.md#a00f124d1201a4de3cc885fe87a91431f) [gid\_t](posix__types_8h.md#a3a7834be1a79bb0c5a65d3546c2e3bd8) [gr\_gid](structgroup.md#a00f124d1201a4de3cc885fe87a91431f);

[ 24](structgroup.md#a338a8153e1e47d345a0bb578f3c2656c) char \*\*[gr\_mem](structgroup.md#a338a8153e1e47d345a0bb578f3c2656c);

25};

26

[ 27](grp_8h.md#acf054c85917adbbc3687004d51317685)int [getgrnam\_r](grp_8h.md#acf054c85917adbbc3687004d51317685)(const char \*name, struct [group](structgroup.md) \*grp, char \*buffer, size\_t bufsize,

28 struct [group](structgroup.md) \*\*result);

[ 29](grp_8h.md#a64e84dfb3f386daaa7530fc8177a6056)int [getgrgid\_r](grp_8h.md#a64e84dfb3f386daaa7530fc8177a6056)([gid\_t](posix__types_8h.md#a3a7834be1a79bb0c5a65d3546c2e3bd8) gid, struct [group](structgroup.md) \*grp, char \*buffer, size\_t bufsize, struct [group](structgroup.md) \*\*result);

30

31#ifdef \_\_cplusplus

32}

33#endif

34

35#endif /\* ZEPHYR\_INCLUDE\_POSIX\_GRP\_H\_ \*/

[getgrgid\_r](grp_8h.md#a64e84dfb3f386daaa7530fc8177a6056)

int getgrgid\_r(gid\_t gid, struct group \*grp, char \*buffer, size\_t bufsize, struct group \*\*result)

[getgrnam\_r](grp_8h.md#acf054c85917adbbc3687004d51317685)

int getgrnam\_r(const char \*name, struct group \*grp, char \*buffer, size\_t bufsize, struct group \*\*result)

[gid\_t](posix__types_8h.md#a3a7834be1a79bb0c5a65d3546c2e3bd8)

unsigned short gid\_t

**Definition** posix\_types.h:61

[stat.h](stat_8h.md)

[group](structgroup.md)

Group structure.

**Definition** grp.h:18

[group::gr\_gid](structgroup.md#a00f124d1201a4de3cc885fe87a91431f)

gid\_t gr\_gid

pointer to a null-terminated array of character pointers to member names

**Definition** grp.h:22

[group::gr\_mem](structgroup.md#a338a8153e1e47d345a0bb578f3c2656c)

char \*\* gr\_mem

**Definition** grp.h:24

[group::gr\_name](structgroup.md#a828b9f3708aa76cecd8fda0a20b61e98)

char \* gr\_name

< the name of the group

**Definition** grp.h:20

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [grp.h](grp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
