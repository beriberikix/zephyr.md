---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/socket__types_8h_source.html
original_path: doxygen/html/socket__types_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socket\_types.h

[Go to the documentation of this file.](socket__types_8h.md)

1/\*

2 \* Copyright (c) 2021 Nordic Semiconductor

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_NET\_SOCKET\_TYPES\_H\_

8#define ZEPHYR\_INCLUDE\_NET\_SOCKET\_TYPES\_H\_

9

16

17#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

18

19

20#ifdef CONFIG\_NEWLIB\_LIBC

21

22#include <newlib.h>

23

24#ifdef \_\_NEWLIB\_\_

25#include <[sys/\_timeval.h](__timeval_8h.md)>

26#else /\* \_\_NEWLIB\_\_ \*/

27#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

28/\* workaround for older Newlib 2.x, as it lacks sys/\_timeval.h \*/

29struct [timeval](structtimeval.md) {

30 [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) [tv\_sec](structtimeval.md#aef6ddab1064c430758f9f913b7e4a21e);

31 [suseconds\_t](__timespec_8h.md#ad7acf95ceafb15a1d8d86af0c4982995) [tv\_usec](structtimeval.md#a810bf8fcd58e255a5c1896d19538b86a);

32};

33#endif /\* \_\_NEWLIB\_\_ \*/

34

35#else /\* CONFIG\_NEWLIB\_LIBC \*/

36

37#if defined(CONFIG\_ARCH\_POSIX) && defined(CONFIG\_EXTERNAL\_LIBC)

38#include <bits/types/struct\_timeval.h>

39#else

40#include <[sys/\_timeval.h](__timeval_8h.md)>

41#endif

42

43#endif /\* CONFIG\_NEWLIB\_LIBC \*/

44

45#ifdef \_\_cplusplus

46extern "C" {

47#endif

48

[ 49](group__bsd__sockets.md#ga0fa9dd4796261813b164fed42303e4ee)#define zsock\_timeval timeval

50

51#ifdef \_\_cplusplus

52}

53#endif

54

58

59#endif /\* ZEPHYR\_INCLUDE\_NET\_SOCKET\_TYPES\_H\_ \*/

[time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7)

\_TIME\_T\_ time\_t

**Definition** \_timespec.h:14

[suseconds\_t](__timespec_8h.md#ad7acf95ceafb15a1d8d86af0c4982995)

\_SUSECONDS\_T\_ suseconds\_t

**Definition** \_timespec.h:19

[\_timeval.h](__timeval_8h.md)

[types.h](include_2zephyr_2types_8h.md)

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
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socket\_types.h](socket__types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
