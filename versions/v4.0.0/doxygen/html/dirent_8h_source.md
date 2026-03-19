---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/dirent_8h_source.html
original_path: doxygen/html/dirent_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dirent.h

[Go to the documentation of this file.](dirent_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_DIRENT\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_DIRENT\_H\_

8

9#include <[limits.h](limits_8h.md)>

10

11#include <[zephyr/posix/posix\_types.h](posix__types_8h.md)>

12

13#ifdef CONFIG\_POSIX\_FILE\_SYSTEM

14#include <[zephyr/fs/fs.h](fs_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

20typedef void DIR;

21

22struct dirent {

23 unsigned int d\_ino;

24 char d\_name[[PATH\_MAX](limits_8h.md#ae688d728e1acdfe5988c7db45d6f0166) + 1];

25};

26

27/\* Directory related operations \*/

28DIR \*opendir(const char \*dirname);

29int closedir(DIR \*dirp);

30struct dirent \*readdir(DIR \*dirp);

31int readdir\_r(DIR \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) dirp, struct dirent \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) entry,

32 struct dirent \*\*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) result);

33

34#ifdef \_\_cplusplus

35}

36#endif

37

38#endif /\* CONFIG\_POSIX\_FILE\_SYSTEM \*/

39

40#endif /\* ZEPHYR\_INCLUDE\_POSIX\_DIRENT\_H\_ \*/

[fs.h](fs_8h.md)

[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd)

#define ZRESTRICT

**Definition** common.h:36

[limits.h](limits_8h.md)

[PATH\_MAX](limits_8h.md#ae688d728e1acdfe5988c7db45d6f0166)

#define PATH\_MAX

**Definition** limits.h:83

[posix\_types.h](posix__types_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [dirent.h](dirent_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
