---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/pwd_8h_source.html
original_path: doxygen/html/pwd_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pwd.h

[Go to the documentation of this file.](pwd_8h.md)

1/\*

2 \* Copyright (c) 2024 Meta Platforms

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_PWD\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_PWD\_H\_

8

9#ifdef \_\_cplusplus

10extern "C" {

11#endif

12

13#include <[zephyr/posix/sys/stat.h](stat_8h.md)>

14

[ 15](structpasswd.md)struct [passwd](structpasswd.md) {

16 /\* user's login name \*/

[ 17](structpasswd.md#a6de92e6d2e3dd348ee82472d2b219556) char \*[pw\_name](structpasswd.md#a6de92e6d2e3dd348ee82472d2b219556);

18 /\* numerical user ID \*/

[ 19](structpasswd.md#aa6e0e62ee3cf5152f2697a0104f627c1) [uid\_t](posix__types_8h.md#a75bb141dc55bc89a8ddc565fd374e3d9) [pw\_uid](structpasswd.md#aa6e0e62ee3cf5152f2697a0104f627c1);

20 /\* numerical group ID \*/

[ 21](structpasswd.md#aefbacfb7dc7f7f47313d08707253e4c6) [gid\_t](posix__types_8h.md#a3a7834be1a79bb0c5a65d3546c2e3bd8) [pw\_gid](structpasswd.md#aefbacfb7dc7f7f47313d08707253e4c6);

22 /\* initial working directory \*/

[ 23](structpasswd.md#afa7bb51f592e9199dc776ccc763352a7) char \*[pw\_dir](structpasswd.md#afa7bb51f592e9199dc776ccc763352a7);

24 /\* program to use as shell \*/

[ 25](structpasswd.md#aa0584dc9fdf7920c25b6326b5fdb5416) char \*[pw\_shell](structpasswd.md#aa0584dc9fdf7920c25b6326b5fdb5416);

26};

27

[ 28](pwd_8h.md#a9848a1faaee1b74dbc399b2d746ef16c)int [getpwnam\_r](pwd_8h.md#a9848a1faaee1b74dbc399b2d746ef16c)(const char \*nam, struct [passwd](structpasswd.md) \*pwd, char \*buffer, size\_t bufsize,

29 struct [passwd](structpasswd.md) \*\*result);

[ 30](pwd_8h.md#a171c52c8fac39d01f77ed0d69efbaa61)int [getpwuid\_r](pwd_8h.md#a171c52c8fac39d01f77ed0d69efbaa61)([uid\_t](posix__types_8h.md#a75bb141dc55bc89a8ddc565fd374e3d9) uid, struct [passwd](structpasswd.md) \*pwd, char \*buffer, size\_t bufsize, struct [passwd](structpasswd.md) \*\*result);

31

32#ifdef \_\_cplusplus

33}

34#endif

35

36#endif /\* ZEPHYR\_INCLUDE\_POSIX\_PWD\_H\_ \*/

[gid\_t](posix__types_8h.md#a3a7834be1a79bb0c5a65d3546c2e3bd8)

unsigned short gid\_t

**Definition** posix\_types.h:61

[uid\_t](posix__types_8h.md#a75bb141dc55bc89a8ddc565fd374e3d9)

unsigned short uid\_t

**Definition** posix\_types.h:55

[getpwuid\_r](pwd_8h.md#a171c52c8fac39d01f77ed0d69efbaa61)

int getpwuid\_r(uid\_t uid, struct passwd \*pwd, char \*buffer, size\_t bufsize, struct passwd \*\*result)

[getpwnam\_r](pwd_8h.md#a9848a1faaee1b74dbc399b2d746ef16c)

int getpwnam\_r(const char \*nam, struct passwd \*pwd, char \*buffer, size\_t bufsize, struct passwd \*\*result)

[stat.h](stat_8h.md)

[passwd](structpasswd.md)

**Definition** pwd.h:15

[passwd::pw\_name](structpasswd.md#a6de92e6d2e3dd348ee82472d2b219556)

char \* pw\_name

**Definition** pwd.h:17

[passwd::pw\_shell](structpasswd.md#aa0584dc9fdf7920c25b6326b5fdb5416)

char \* pw\_shell

**Definition** pwd.h:25

[passwd::pw\_uid](structpasswd.md#aa6e0e62ee3cf5152f2697a0104f627c1)

uid\_t pw\_uid

**Definition** pwd.h:19

[passwd::pw\_gid](structpasswd.md#aefbacfb7dc7f7f47313d08707253e4c6)

gid\_t pw\_gid

**Definition** pwd.h:21

[passwd::pw\_dir](structpasswd.md#afa7bb51f592e9199dc776ccc763352a7)

char \* pw\_dir

**Definition** pwd.h:23

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [pwd.h](pwd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
