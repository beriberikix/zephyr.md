---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dirent_8h_source.html
original_path: doxygen/html/dirent_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

10#include "[posix\_types.h](posix__types_8h.md)"

11

12#ifdef CONFIG\_POSIX\_FILE\_SYSTEM

13#include <[zephyr/fs/fs.h](fs_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

19typedef void DIR;

20

21struct dirent {

22 unsigned int d\_ino;

23 char d\_name[[PATH\_MAX](limits_8h.md#ae688d728e1acdfe5988c7db45d6f0166) + 1];

24};

25

26/\* Directory related operations \*/

27DIR \*opendir(const char \*dirname);

28int closedir(DIR \*dirp);

29struct dirent \*readdir(DIR \*dirp);

30

31#ifdef \_\_cplusplus

32}

33#endif

34

35#endif /\* CONFIG\_POSIX\_FILE\_SYSTEM \*/

36

37#endif /\* ZEPHYR\_INCLUDE\_POSIX\_DIRENT\_H\_ \*/

[fs.h](fs_8h.md)

[limits.h](limits_8h.md)

[PATH\_MAX](limits_8h.md#ae688d728e1acdfe5988c7db45d6f0166)

#define PATH\_MAX

**Definition** limits.h:83

[posix\_types.h](posix__types_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [dirent.h](dirent_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
