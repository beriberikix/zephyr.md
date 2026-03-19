---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dirent_8h_source.html
original_path: doxygen/html/dirent_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dirent.h

[Go to the documentation of this file.](dirent_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \* Copyright (c) 2024 Tenstorrent AI ULC

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_POSIX\_DIRENT\_H\_

9#define ZEPHYR\_INCLUDE\_POSIX\_DIRENT\_H\_

10

11#include <[zephyr/posix/sys/dirent.h](sys_2dirent_8h.md)>

12#include <[zephyr/toolchain.h](toolchain_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

18#if (\_POSIX\_C\_SOURCE >= 200809L) || (\_XOPEN\_SOURCE >= 700)

19int alphasort(const struct [dirent](structdirent.md) \*\*d1, const struct [dirent](structdirent.md) \*\*d2);

20#endif

[ 21](dirent_8h.md#aaeac2b41e8c2c3a5f91c9bd511a8c0a6)int [closedir](dirent_8h.md#aaeac2b41e8c2c3a5f91c9bd511a8c0a6)([DIR](sys_2dirent_8h.md#a6808d95339147c6e29523463181854cc) \*dirp);

22#if (\_POSIX\_C\_SOURCE >= 200809L) || (\_XOPEN\_SOURCE >= 700)

23int dirfd([DIR](sys_2dirent_8h.md#a6808d95339147c6e29523463181854cc) \*dirp);

24#endif

[ 25](dirent_8h.md#a58be90fffc0b5713ea34e39eb26d59f3)[DIR](sys_2dirent_8h.md#a6808d95339147c6e29523463181854cc) \*[fdopendir](dirent_8h.md#a58be90fffc0b5713ea34e39eb26d59f3)(int fd);

[ 26](dirent_8h.md#ae27c7f260a652b74c43296993d14ef0b)[DIR](sys_2dirent_8h.md#a6808d95339147c6e29523463181854cc) \*[opendir](dirent_8h.md#ae27c7f260a652b74c43296993d14ef0b)(const char \*dirname);

[ 27](dirent_8h.md#a824e3b8c5995631b373ddb65cb674318)struct [dirent](structdirent.md) \*[readdir](dirent_8h.md#a824e3b8c5995631b373ddb65cb674318)([DIR](sys_2dirent_8h.md#a6808d95339147c6e29523463181854cc) \*dirp);

28#if (\_POSIX\_C\_SOURCE >= 199506L) || (\_XOPEN\_SOURCE >= 500)

29int readdir\_r([DIR](sys_2dirent_8h.md#a6808d95339147c6e29523463181854cc) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) dirp, struct [dirent](structdirent.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) entry,

30 struct [dirent](structdirent.md) \*\*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) result);

31#endif

[ 32](dirent_8h.md#ad4fcb58b9194b1a3c1699654de963719)void [rewinddir](dirent_8h.md#ad4fcb58b9194b1a3c1699654de963719)([DIR](sys_2dirent_8h.md#a6808d95339147c6e29523463181854cc) \*dirp);

33#if (\_POSIX\_C\_SOURCE >= 200809L) || (\_XOPEN\_SOURCE >= 700)

34int scandir(const char \*dir, struct [dirent](structdirent.md) \*\*\*namelist, int (\*sel)(const struct [dirent](structdirent.md) \*),

35 int (\*compar)(const struct [dirent](structdirent.md) \*\*, const struct [dirent](structdirent.md) \*\*));

36#endif

37#if defined(\_XOPEN\_SOURCE)

38void seekdir([DIR](sys_2dirent_8h.md#a6808d95339147c6e29523463181854cc) \*dirp, long loc);

39long telldir([DIR](sys_2dirent_8h.md#a6808d95339147c6e29523463181854cc) \*dirp);

40#endif

41

42#ifdef \_\_cplusplus

43}

44#endif

45

46#endif /\* ZEPHYR\_INCLUDE\_POSIX\_DIRENT\_H\_ \*/

[fdopendir](dirent_8h.md#a58be90fffc0b5713ea34e39eb26d59f3)

DIR \* fdopendir(int fd)

[readdir](dirent_8h.md#a824e3b8c5995631b373ddb65cb674318)

struct dirent \* readdir(DIR \*dirp)

[closedir](dirent_8h.md#aaeac2b41e8c2c3a5f91c9bd511a8c0a6)

int closedir(DIR \*dirp)

[rewinddir](dirent_8h.md#ad4fcb58b9194b1a3c1699654de963719)

void rewinddir(DIR \*dirp)

[opendir](dirent_8h.md#ae27c7f260a652b74c43296993d14ef0b)

DIR \* opendir(const char \*dirname)

[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd)

#define ZRESTRICT

**Definition** common.h:36

[dirent](structdirent.md)

**Definition** dirent.h:28

[dirent.h](sys_2dirent_8h.md)

[DIR](sys_2dirent_8h.md#a6808d95339147c6e29523463181854cc)

void DIR

**Definition** dirent.h:26

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [dirent.h](dirent_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
