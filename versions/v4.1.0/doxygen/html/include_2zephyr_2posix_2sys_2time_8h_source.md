---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/include_2zephyr_2posix_2sys_2time_8h_source.html
original_path: doxygen/html/include_2zephyr_2posix_2sys_2time_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

time.h

[Go to the documentation of this file.](include_2zephyr_2posix_2sys_2time_8h.md)

1/\*

2 \* Copyright (c) 2019 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_POSIX\_SYS\_TIME\_H\_

8#define ZEPHYR\_INCLUDE\_POSIX\_SYS\_TIME\_H\_

9

10#ifdef CONFIG\_NEWLIB\_LIBC

11/\* Kludge to support outdated newlib version as used in SDK 0.10 for Xtensa \*/

12#include <newlib.h>

13

14#ifdef \_\_NEWLIB\_\_

15#include <[sys/\_timeval.h](__timeval_8h.md)>

16#else

17#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

18struct [timeval](structtimeval.md) {

19 [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) [tv\_sec](structtimeval.md#aef6ddab1064c430758f9f913b7e4a21e);

20 [suseconds\_t](__timespec_8h.md#ad7acf95ceafb15a1d8d86af0c4982995) [tv\_usec](structtimeval.md#a810bf8fcd58e255a5c1896d19538b86a);

21};

22#endif

23

24#else

25#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

26#include <[sys/\_timeval.h](__timeval_8h.md)>

27#endif /\* CONFIG\_NEWLIB\_LIBC \*/

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

[ 33](include_2zephyr_2posix_2sys_2time_8h.md#a2f316a4ad94a242df56b01953677015d)int [gettimeofday](include_2zephyr_2posix_2sys_2time_8h.md#a2f316a4ad94a242df56b01953677015d)(struct [timeval](structtimeval.md) \*tv, void \*tz);

34

35#ifdef \_\_cplusplus

36}

37#endif

38

39#endif /\* ZEPHYR\_INCLUDE\_POSIX\_SYS\_TIME\_H\_ \*/

[time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7)

\_TIME\_T\_ time\_t

**Definition** \_timespec.h:14

[suseconds\_t](__timespec_8h.md#ad7acf95ceafb15a1d8d86af0c4982995)

\_SUSECONDS\_T\_ suseconds\_t

**Definition** \_timespec.h:19

[\_timeval.h](__timeval_8h.md)

[gettimeofday](include_2zephyr_2posix_2sys_2time_8h.md#a2f316a4ad94a242df56b01953677015d)

int gettimeofday(struct timeval \*tv, void \*tz)

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[timeval](structtimeval.md)

**Definition** \_timeval.h:22

[timeval::tv\_usec](structtimeval.md#a810bf8fcd58e255a5c1896d19538b86a)

suseconds\_t tv\_usec

**Definition** \_timeval.h:24

[timeval::tv\_sec](structtimeval.md#aef6ddab1064c430758f9f913b7e4a21e)

time\_t tv\_sec

**Definition** \_timeval.h:23

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [time.h](include_2zephyr_2posix_2sys_2time_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
