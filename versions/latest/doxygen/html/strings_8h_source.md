---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/strings_8h_source.html
original_path: doxygen/html/strings_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

strings.h

[Go to the documentation of this file.](strings_8h.md)

1/\* strings.h \*/

2

3/\*

4 \* Copyright (c) 2014 Wind River Systems, Inc.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_STRINGS\_H\_

10#define ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_STRINGS\_H\_

11

12#include <stddef.h>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

[ 18](strings_8h.md#a674b7f779fec84cb1a3be8222b5c381a)extern int [strncasecmp](strings_8h.md#a674b7f779fec84cb1a3be8222b5c381a)(const char \*s1, const char \*s2, size\_t n);

19

20#ifdef \_\_cplusplus

21}

22#endif

23

24#endif /\* ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_STRINGS\_H\_ \*/

[strncasecmp](strings_8h.md#a674b7f779fec84cb1a3be8222b5c381a)

int strncasecmp(const char \*s1, const char \*s2, size\_t n)

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [strings.h](strings_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
