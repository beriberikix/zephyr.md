---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/lib_2libc_2minimal_2include_2sys_2stat_8h_source.html
original_path: doxygen/html/lib_2libc_2minimal_2include_2sys_2stat_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stat.h

[Go to the documentation of this file.](lib_2libc_2minimal_2include_2sys_2stat_8h.md)

1/\*

2 \* Copyright (c) 2022 Meta

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_SYS\_STAT\_H\_

8#define ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_SYS\_STAT\_H\_

9

10#ifndef CONFIG\_POSIX\_API

11#pragma message("#include <sys/stat.h> without CONFIG\_POSIX\_API is deprecated. " \

12 "Please use CONFIG\_POSIX\_API or #include <zephyr/posix/sys/stat.h>")

13#endif

14#include <[zephyr/posix/sys/stat.h](include_2zephyr_2posix_2sys_2stat_8h.md)>

15

16#endif /\* ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_SYS\_STAT\_H\_ \*/

[stat.h](include_2zephyr_2posix_2sys_2stat_8h.md)

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [sys](dir_4d70b020f8f8c9ca462b8905bdfa3f4f.md)
- [stat.h](lib_2libc_2minimal_2include_2sys_2stat_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
