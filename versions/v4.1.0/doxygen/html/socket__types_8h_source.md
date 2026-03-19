---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/socket__types_8h_source.html
original_path: doxygen/html/socket__types_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_SOCKET\_TYPES\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_SOCKET\_TYPES\_H\_

14

21

22#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

23

25

26#ifdef CONFIG\_NEWLIB\_LIBC

27

28#include <newlib.h>

29

30#ifdef \_\_NEWLIB\_\_

31#include <[sys/\_timeval.h](__timeval_8h.md)>

32#else /\* \_\_NEWLIB\_\_ \*/

33#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

34/\* workaround for older Newlib 2.x, as it lacks sys/\_timeval.h \*/

35struct [timeval](structtimeval.md) {

36 [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) [tv\_sec](structtimeval.md#aef6ddab1064c430758f9f913b7e4a21e);

37 [suseconds\_t](__timespec_8h.md#ad7acf95ceafb15a1d8d86af0c4982995) [tv\_usec](structtimeval.md#a810bf8fcd58e255a5c1896d19538b86a);

38};

39#endif /\* \_\_NEWLIB\_\_ \*/

40

41#else /\* CONFIG\_NEWLIB\_LIBC \*/

42

43#if defined(CONFIG\_ARCH\_POSIX) && defined(CONFIG\_EXTERNAL\_LIBC)

44#include <bits/types/struct\_timeval.h>

45#else

46#include <[sys/\_timeval.h](__timeval_8h.md)>

47#endif

48

49#endif /\* CONFIG\_NEWLIB\_LIBC \*/

50

51#ifdef \_\_cplusplus

52extern "C" {

53#endif

54

55#define zsock\_timeval timeval

56

57#ifdef \_\_cplusplus

58}

59#endif

60

62

66

67#endif /\* ZEPHYR\_INCLUDE\_NET\_SOCKET\_TYPES\_H\_ \*/

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
