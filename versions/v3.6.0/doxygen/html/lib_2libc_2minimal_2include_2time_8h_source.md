---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/lib_2libc_2minimal_2include_2time_8h_source.html
original_path: doxygen/html/lib_2libc_2minimal_2include_2time_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

48 \* localtime() and inverse mktime() are not provided here since they

49 \* require access to time zone information.

50 \*/

[ 51](lib_2libc_2minimal_2include_2time_8h.md#a4bc4ff58d4ac838a36ba939747e5833e)struct [tm](structtm.md) \*[gmtime](lib_2libc_2minimal_2include_2time_8h.md#a4bc4ff58d4ac838a36ba939747e5833e)(const [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*timep);

[ 52](lib_2libc_2minimal_2include_2time_8h.md#aee41f7a79e9f6ec34cdf7096fd597dbd)struct [tm](structtm.md) \*[gmtime\_r](lib_2libc_2minimal_2include_2time_8h.md#aee41f7a79e9f6ec34cdf7096fd597dbd)(const [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) timep,

53 struct [tm](structtm.md) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) result);

54

[ 55](lib_2libc_2minimal_2include_2time_8h.md#a99ef1cb2c789827dd5db3886dccf9067)[time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) [time](lib_2libc_2minimal_2include_2time_8h.md#a99ef1cb2c789827dd5db3886dccf9067)([time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*tloc);

56

57#ifdef \_\_cplusplus

58}

59#endif

60

61#endif /\* ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_STDIO\_H\_ \*/

[\_timespec.h](__timespec_8h.md)

[time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7)

\_TIME\_T\_ time\_t

**Definition** \_timespec.h:14

[suseconds\_t](__timespec_8h.md#ad7acf95ceafb15a1d8d86af0c4982995)

\_SUSECONDS\_T\_ suseconds\_t

**Definition** \_timespec.h:19

[\_types.h](__types_8h.md)

[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd)

#define ZRESTRICT

**Definition** common.h:36

[gmtime](lib_2libc_2minimal_2include_2time_8h.md#a4bc4ff58d4ac838a36ba939747e5833e)

struct tm \* gmtime(const time\_t \*timep)

[time](lib_2libc_2minimal_2include_2time_8h.md#a99ef1cb2c789827dd5db3886dccf9067)

time\_t time(time\_t \*tloc)

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
