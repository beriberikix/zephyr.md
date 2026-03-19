---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/timespec_8h_source.html
original_path: doxygen/html/timespec_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

timespec.h

[Go to the documentation of this file.](timespec_8h.md)

1/\*

2 \* Copyright (c) 2019 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_SYS\_TIMESPEC\_H\_

8#define ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_SYS\_TIMESPEC\_H\_

9

10#include <[sys/\_timespec.h](__timespec_8h.md)>

11

[ 12](structitimerspec.md)struct [itimerspec](structitimerspec.md) {

[ 13](structitimerspec.md#a27cedae552e2b2fe0993c1b2c4ff1889) struct [timespec](structtimespec.md) [it\_interval](structitimerspec.md#a27cedae552e2b2fe0993c1b2c4ff1889); /\* Timer interval \*/

[ 14](structitimerspec.md#a754dda918053251c24558b07571d6e8f) struct [timespec](structtimespec.md) [it\_value](structitimerspec.md#a754dda918053251c24558b07571d6e8f); /\* Timer expiration \*/

15};

16

17#endif /\* ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_SYS\_TIMESPEC\_H\_ \*/

[\_timespec.h](__timespec_8h.md)

[itimerspec](structitimerspec.md)

**Definition** timespec.h:12

[itimerspec::it\_interval](structitimerspec.md#a27cedae552e2b2fe0993c1b2c4ff1889)

struct timespec it\_interval

**Definition** timespec.h:13

[itimerspec::it\_value](structitimerspec.md#a754dda918053251c24558b07571d6e8f)

struct timespec it\_value

**Definition** timespec.h:14

[timespec](structtimespec.md)

**Definition** \_timespec.h:22

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [sys](dir_4d70b020f8f8c9ca462b8905bdfa3f4f.md)
- [timespec.h](timespec_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
