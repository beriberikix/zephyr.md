---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/__timeval_8h_source.html
original_path: doxygen/html/__timeval_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

\_timeval.h

[Go to the documentation of this file.](__timeval_8h.md)

1/\*

2 \* Copyright (c) 2019 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_SYS\_\_TIMEVAL\_H\_

8#define ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_SYS\_\_TIMEVAL\_H\_

9

10#include <[sys/\_types.h](__types_8h.md)>

11

12#if !defined(\_\_time\_t\_defined)

13#define \_\_time\_t\_defined

14typedef \_TIME\_T\_ [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7);

15#endif

16

17#if !defined(\_\_suseconds\_t\_defined)

18#define \_\_suseconds\_t\_defined

19typedef \_SUSECONDS\_T\_ [suseconds\_t](__timespec_8h.md#ad7acf95ceafb15a1d8d86af0c4982995);

20#endif

21

[ 22](structtimeval.md)struct [timeval](structtimeval.md) {

[ 23](structtimeval.md#aef6ddab1064c430758f9f913b7e4a21e) [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) [tv\_sec](structtimeval.md#aef6ddab1064c430758f9f913b7e4a21e);

[ 24](structtimeval.md#a810bf8fcd58e255a5c1896d19538b86a) [suseconds\_t](__timespec_8h.md#ad7acf95ceafb15a1d8d86af0c4982995) [tv\_usec](structtimeval.md#a810bf8fcd58e255a5c1896d19538b86a);

25};

26

27#endif /\* ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_SYS\_\_TIMEVAL\_H\_ \*/

[time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7)

\_TIME\_T\_ time\_t

**Definition** \_timespec.h:14

[suseconds\_t](__timespec_8h.md#ad7acf95ceafb15a1d8d86af0c4982995)

\_SUSECONDS\_T\_ suseconds\_t

**Definition** \_timespec.h:19

[\_types.h](__types_8h.md)

[timeval](structtimeval.md)

**Definition** \_timeval.h:22

[timeval::tv\_usec](structtimeval.md#a810bf8fcd58e255a5c1896d19538b86a)

suseconds\_t tv\_usec

**Definition** \_timeval.h:24

[timeval::tv\_sec](structtimeval.md#aef6ddab1064c430758f9f913b7e4a21e)

time\_t tv\_sec

**Definition** \_timeval.h:23

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [sys](dir_4d70b020f8f8c9ca462b8905bdfa3f4f.md)
- [\_timeval.h](__timeval_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
