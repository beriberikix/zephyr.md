---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/__timespec_8h_source.html
original_path: doxygen/html/__timespec_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

\_timespec.h

[Go to the documentation of this file.](__timespec_8h.md)

1/\*

2 \* Copyright (c) 2019 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_SYS\_\_TIMESPEC\_H\_

8#define ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_SYS\_\_TIMESPEC\_H\_

9

10#include <[sys/\_types.h](__types_8h.md)>

11

12#if !defined(\_\_time\_t\_defined)

13#define \_\_time\_t\_defined

[ 14](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7)typedef \_TIME\_T\_ [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7);

15#endif

16

17#if !defined(\_\_suseconds\_t\_defined)

18#define \_\_suseconds\_t\_defined

[ 19](__timespec_8h.md#ad7acf95ceafb15a1d8d86af0c4982995)typedef \_SUSECONDS\_T\_ [suseconds\_t](__timespec_8h.md#ad7acf95ceafb15a1d8d86af0c4982995);

20#endif

21

[ 22](structtimespec.md)struct [timespec](structtimespec.md) {

[ 23](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) [tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955);

[ 24](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) long [tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683);

25};

26

27#endif /\* ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_SYS\_\_TIMESPEC\_H\_ \*/

[time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7)

\_TIME\_T\_ time\_t

**Definition** \_timespec.h:14

[suseconds\_t](__timespec_8h.md#ad7acf95ceafb15a1d8d86af0c4982995)

\_SUSECONDS\_T\_ suseconds\_t

**Definition** \_timespec.h:19

[\_types.h](__types_8h.md)

[timespec](structtimespec.md)

**Definition** \_timespec.h:22

[timespec::tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683)

long tv\_nsec

**Definition** \_timespec.h:24

[timespec::tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955)

time\_t tv\_sec

**Definition** \_timespec.h:23

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [sys](dir_4d70b020f8f8c9ca462b8905bdfa3f4f.md)
- [\_timespec.h](__timespec_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
