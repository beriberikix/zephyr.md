---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/lib_2libc_2minimal_2include_2time_8h_source.html
original_path: doxygen/html/lib_2libc_2minimal_2include_2time_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

time.h

[Go to the documentation of this file.](lib_2libc_2minimal_2include_2time_8h.md)

1/\*

2 \* Copyright (c) 2017 Intel Corporation

3 \* Copyright (c) 2019 Peter Bigot Consulting, LLC

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_TIME\_H\_

9#define ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_TIME\_H\_

10

11#include <[stdint.h](stdint_8h.md)>

12#include <[zephyr/toolchain.h](toolchain_8h.md)>

13#include <[sys/\_types.h](__types_8h.md)>

14#include <[sys/\_timespec.h](__timespec_8h.md)>

15

16/\* Minimal time.h to fulfill the requirements of certain libraries

17 \* like mbedTLS and to support time APIs.

18 \*/

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

[ 24](structtm.md)struct [tm](structtm.md) {

[ 25](structtm.md#a4d098a9a5c03a00b2ee61e10851de81e) int [tm\_sec](structtm.md#a4d098a9a5c03a00b2ee61e10851de81e);

[ 26](structtm.md#af414eb7c86cc3099595211eee4d4211b) int [tm\_min](structtm.md#af414eb7c86cc3099595211eee4d4211b);

[ 27](structtm.md#a3e7ca4e37f1abcaf56b8a916c38eb9fe) int [tm\_hour](structtm.md#a3e7ca4e37f1abcaf56b8a916c38eb9fe);

[ 28](structtm.md#ab8d8904bad43b0c8b96e61941c5b5310) int [tm\_mday](structtm.md#ab8d8904bad43b0c8b96e61941c5b5310);

[ 29](structtm.md#a112ac36fa2f593777138a417cf031e17) int [tm\_mon](structtm.md#a112ac36fa2f593777138a417cf031e17);

[ 30](structtm.md#a33adf78fd6476b2120ce3b9c4a852053) int [tm\_year](structtm.md#a33adf78fd6476b2120ce3b9c4a852053);

[ 31](structtm.md#afe81a8c46f1c693c43f259b288859f4f) int [tm\_wday](structtm.md#afe81a8c46f1c693c43f259b288859f4f);

[ 32](structtm.md#a93a0ba77cc23796df84405dcbcc57eb1) int [tm\_yday](structtm.md#a93a0ba77cc23796df84405dcbcc57eb1);

[ 33](structtm.md#a5645ca0580c8ab2c24f6c2965d9c9f9c) int [tm\_isdst](structtm.md#a5645ca0580c8ab2c24f6c2965d9c9f9c);

34};

35

36#if !defined(\_\_time\_t\_defined)

37#define \_\_time\_t\_defined

38typedef \_TIME\_T\_ [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7);

39#endif

40

41#if !defined(\_\_suseconds\_t\_defined)

42#define \_\_suseconds\_t\_defined

43typedef \_SUSECONDS\_T\_ [suseconds\_t](__timespec_8h.md#ad7acf95ceafb15a1d8d86af0c4982995);

44#endif

45

46/\*

47 \* Conversion between civil time and UNIX time. The companion

48 \* mktime() is not provided here since it

49 \* require access to time zone information.

50 \*

51 \* The localtime() & localtime\_r() simply

52 \* wraps around the gmtime() & gmtime\_r() functions, the

53 \* results are always expressed as UTC.

54 \*/

[ 55](lib_2libc_2minimal_2include_2time_8h.md#a4bc4ff58d4ac838a36ba939747e5833e)struct [tm](structtm.md) \*[gmtime](lib_2libc_2minimal_2include_2time_8h.md#a4bc4ff58d4ac838a36ba939747e5833e)(const [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*timep);

[ 56](lib_2libc_2minimal_2include_2time_8h.md#aee41f7a79e9f6ec34cdf7096fd597dbd)struct [tm](structtm.md) \*[gmtime\_r](lib_2libc_2minimal_2include_2time_8h.md#aee41f7a79e9f6ec34cdf7096fd597dbd)(const [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) timep,

57 struct [tm](structtm.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) result);

[ 58](lib_2libc_2minimal_2include_2time_8h.md#a068d11e0d50eab73920a3162d2ac9202)char \*[asctime](lib_2libc_2minimal_2include_2time_8h.md#a068d11e0d50eab73920a3162d2ac9202)(const struct [tm](structtm.md) \*timeptr);

[ 59](lib_2libc_2minimal_2include_2time_8h.md#a47dad42d50a51f3ba4033320084c833b)struct [tm](structtm.md) \*[localtime](lib_2libc_2minimal_2include_2time_8h.md#a47dad42d50a51f3ba4033320084c833b)(const [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*timer);

[ 60](lib_2libc_2minimal_2include_2time_8h.md#a185521f2c273b9697eb1e536a37912fb)char \*[ctime](lib_2libc_2minimal_2include_2time_8h.md#a185521f2c273b9697eb1e536a37912fb)(const [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*clock);

[ 61](lib_2libc_2minimal_2include_2time_8h.md#a86ed062bf74f495209b11b650631e2f2)char \*[asctime\_r](lib_2libc_2minimal_2include_2time_8h.md#a86ed062bf74f495209b11b650631e2f2)(const struct [tm](structtm.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) tp, char \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) buf);

[ 62](lib_2libc_2minimal_2include_2time_8h.md#abb5334ac0f38a87278861e6edab616db)char \*[ctime\_r](lib_2libc_2minimal_2include_2time_8h.md#abb5334ac0f38a87278861e6edab616db)(const [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*clock, char \*buf);

[ 63](lib_2libc_2minimal_2include_2time_8h.md#a3d8015c8bf5fadc92389635bd977e880)struct [tm](structtm.md) \*[localtime\_r](lib_2libc_2minimal_2include_2time_8h.md#a3d8015c8bf5fadc92389635bd977e880)(const [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) timer, struct [tm](structtm.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) result);

64

[ 65](lib_2libc_2minimal_2include_2time_8h.md#a99ef1cb2c789827dd5db3886dccf9067)[time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) [time](lib_2libc_2minimal_2include_2time_8h.md#a99ef1cb2c789827dd5db3886dccf9067)([time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*tloc);

66

67#ifdef \_\_cplusplus

68}

69#endif

70

71#endif /\* ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_STDIO\_H\_ \*/

[\_timespec.h](__timespec_8h.md)

[time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7)

\_TIME\_T\_ time\_t

**Definition** \_timespec.h:14

[suseconds\_t](__timespec_8h.md#ad7acf95ceafb15a1d8d86af0c4982995)

\_SUSECONDS\_T\_ suseconds\_t

**Definition** \_timespec.h:19

[\_types.h](__types_8h.md)

[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd)

#define ZRESTRICT

**Definition** common.h:36

[asctime](lib_2libc_2minimal_2include_2time_8h.md#a068d11e0d50eab73920a3162d2ac9202)

char \* asctime(const struct tm \*timeptr)

[ctime](lib_2libc_2minimal_2include_2time_8h.md#a185521f2c273b9697eb1e536a37912fb)

char \* ctime(const time\_t \*clock)

[localtime\_r](lib_2libc_2minimal_2include_2time_8h.md#a3d8015c8bf5fadc92389635bd977e880)

struct tm \* localtime\_r(const time\_t \*ZRESTRICT timer, struct tm \*ZRESTRICT result)

[localtime](lib_2libc_2minimal_2include_2time_8h.md#a47dad42d50a51f3ba4033320084c833b)

struct tm \* localtime(const time\_t \*timer)

[gmtime](lib_2libc_2minimal_2include_2time_8h.md#a4bc4ff58d4ac838a36ba939747e5833e)

struct tm \* gmtime(const time\_t \*timep)

[asctime\_r](lib_2libc_2minimal_2include_2time_8h.md#a86ed062bf74f495209b11b650631e2f2)

char \* asctime\_r(const struct tm \*ZRESTRICT tp, char \*ZRESTRICT buf)

[time](lib_2libc_2minimal_2include_2time_8h.md#a99ef1cb2c789827dd5db3886dccf9067)

time\_t time(time\_t \*tloc)

[ctime\_r](lib_2libc_2minimal_2include_2time_8h.md#abb5334ac0f38a87278861e6edab616db)

char \* ctime\_r(const time\_t \*clock, char \*buf)

[gmtime\_r](lib_2libc_2minimal_2include_2time_8h.md#aee41f7a79e9f6ec34cdf7096fd597dbd)

struct tm \* gmtime\_r(const time\_t \*ZRESTRICT timep, struct tm \*ZRESTRICT result)

[stdint.h](stdint_8h.md)

[tm](structtm.md)

**Definition** time.h:24

[tm::tm\_mon](structtm.md#a112ac36fa2f593777138a417cf031e17)

int tm\_mon

**Definition** time.h:29

[tm::tm\_year](structtm.md#a33adf78fd6476b2120ce3b9c4a852053)

int tm\_year

**Definition** time.h:30

[tm::tm\_hour](structtm.md#a3e7ca4e37f1abcaf56b8a916c38eb9fe)

int tm\_hour

**Definition** time.h:27

[tm::tm\_sec](structtm.md#a4d098a9a5c03a00b2ee61e10851de81e)

int tm\_sec

**Definition** time.h:25

[tm::tm\_isdst](structtm.md#a5645ca0580c8ab2c24f6c2965d9c9f9c)

int tm\_isdst

**Definition** time.h:33

[tm::tm\_yday](structtm.md#a93a0ba77cc23796df84405dcbcc57eb1)

int tm\_yday

**Definition** time.h:32

[tm::tm\_mday](structtm.md#ab8d8904bad43b0c8b96e61941c5b5310)

int tm\_mday

**Definition** time.h:28

[tm::tm\_min](structtm.md#af414eb7c86cc3099595211eee4d4211b)

int tm\_min

**Definition** time.h:26

[tm::tm\_wday](structtm.md#afe81a8c46f1c693c43f259b288859f4f)

int tm\_wday

**Definition** time.h:31

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [time.h](lib_2libc_2minimal_2include_2time_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
