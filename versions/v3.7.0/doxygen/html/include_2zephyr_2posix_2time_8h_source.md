---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/include_2zephyr_2posix_2time_8h_source.html
original_path: doxygen/html/include_2zephyr_2posix_2time_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

time.h

[Go to the documentation of this file.](include_2zephyr_2posix_2time_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_TIME\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_TIME\_H\_

8

9/\* Read standard header. This may find <posix/time.h> since they

10 \* refer to the same file when include/posix is in the search path.

11 \*/

12#include <[time.h](include_2zephyr_2posix_2time_8h.md)>

13

14#ifdef CONFIG\_NEWLIB\_LIBC

15/\* Kludge to support outdated newlib version as used in SDK 0.10 for Xtensa \*/

16#include <newlib.h>

17

18#ifdef \_\_NEWLIB\_\_

19/\* Newever Newlib 3.x+ \*/

20#include <[sys/timespec.h](timespec_8h.md)>

21#else /\* \_\_NEWLIB\_\_ \*/

22/\* Workaround for older Newlib 2.x, as used by Xtensa. It lacks sys/\_timeval.h,

23 \* so mimic it here.

24 \*/

25#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

26#ifndef \_\_timespec\_defined

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

32struct [timespec](structtimespec.md) {

33 [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) [tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955);

34 long [tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683);

35};

36

37struct [itimerspec](structitimerspec.md) {

38 struct timespec [it\_interval](structitimerspec.md#a27cedae552e2b2fe0993c1b2c4ff1889); /\* Timer interval \*/

39 struct timespec [it\_value](structitimerspec.md#a754dda918053251c24558b07571d6e8f); /\* Timer expiration \*/

40};

41

42#ifdef \_\_cplusplus

43}

44#endif

45

46#endif /\* \_\_timespec\_defined \*/

47#endif /\* \_\_NEWLIB\_\_ \*/

48

49#else /\* CONFIG\_NEWLIB\_LIBC \*/

50/\* Not Newlib \*/

51# if defined(CONFIG\_ARCH\_POSIX) && defined(CONFIG\_EXTERNAL\_LIBC)

52# include <bits/types/struct\_timespec.h>

53# include <bits/types/struct\_itimerspec.h>

54# else

55# include <[sys/timespec.h](timespec_8h.md)>

56# endif

57#endif /\* CONFIG\_NEWLIB\_LIBC \*/

58

59#include <[zephyr/kernel.h](kernel_8h.md)>

60#include <[errno.h](errno_8h.md)>

61#include "[posix\_types.h](posix__types_8h.md)"

62#include <[zephyr/posix/signal.h](include_2zephyr_2posix_2signal_8h.md)>

63

64#ifdef \_\_cplusplus

65extern "C" {

66#endif

67

68#ifndef CLOCK\_REALTIME

[ 69](include_2zephyr_2posix_2time_8h.md#a922ce1ae64374c9410c8a999e25e82af)#define CLOCK\_REALTIME 1

70#endif

71

72#ifndef CLOCK\_PROCESS\_CPUTIME\_ID

[ 73](include_2zephyr_2posix_2time_8h.md#ae1c3939a1e7b7cd1e5a4a7fa601cc4e9)#define CLOCK\_PROCESS\_CPUTIME\_ID 2

74#endif

75

76#ifndef CLOCK\_THREAD\_CPUTIME\_ID

[ 77](include_2zephyr_2posix_2time_8h.md#a30114e19c18f57f83727bcaba2458f1e)#define CLOCK\_THREAD\_CPUTIME\_ID 3

78#endif

79

80#ifndef CLOCK\_MONOTONIC

[ 81](include_2zephyr_2posix_2time_8h.md#a6fb83f5e91e704391ff796553d5e0f46)#define CLOCK\_MONOTONIC 4

82#endif

83

84#ifndef TIMER\_ABSTIME

[ 85](include_2zephyr_2posix_2time_8h.md#adde83d9ea51f12d4149f016eededde54)#define TIMER\_ABSTIME 4

86#endif

87

88static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \_ts\_to\_ms(const struct [timespec](structtimespec.md) \*to)

89{

90 return ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))(to->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) \* [MSEC\_PER\_SEC](group__clock__apis.md#ga222f9dff749accf8de62bc4b52c7bdcd)) + ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))(to->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) / [NSEC\_PER\_MSEC](group__clock__apis.md#gad16e9029e202d2dfb4cfae8f09131f8f));

91}

92

[ 93](include_2zephyr_2posix_2time_8h.md#a21188eaca1b3e48ac3f7715398a1fc06)int [clock\_gettime](include_2zephyr_2posix_2time_8h.md#a21188eaca1b3e48ac3f7715398a1fc06)([clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) clock\_id, struct [timespec](structtimespec.md) \*ts);

[ 94](include_2zephyr_2posix_2time_8h.md#a3e1d049d0ed1519b99570efc4d8a1ae3)int [clock\_getres](include_2zephyr_2posix_2time_8h.md#a3e1d049d0ed1519b99570efc4d8a1ae3)([clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) clock\_id, struct [timespec](structtimespec.md) \*ts);

[ 95](include_2zephyr_2posix_2time_8h.md#adab8a7307d547eb2b882dd1cda3a7655)int [clock\_settime](include_2zephyr_2posix_2time_8h.md#adab8a7307d547eb2b882dd1cda3a7655)([clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) clock\_id, const struct [timespec](structtimespec.md) \*ts);

[ 96](include_2zephyr_2posix_2time_8h.md#ab2cd29aa41b2b485b571f05ac22d9f7f)int [clock\_getcpuclockid](include_2zephyr_2posix_2time_8h.md#ab2cd29aa41b2b485b571f05ac22d9f7f)([pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) pid, [clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) \*clock\_id);

97/\* Timer APIs \*/

[ 98](include_2zephyr_2posix_2time_8h.md#ab36f0d44be3c22bae387064f49ab934c)int [timer\_create](include_2zephyr_2posix_2time_8h.md#ab36f0d44be3c22bae387064f49ab934c)([clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) clockId, struct [sigevent](structsigevent.md) \*evp, [timer\_t](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d) \*timerid);

[ 99](include_2zephyr_2posix_2time_8h.md#ad114bb350d7d5d12cff3fd19bf533303)int [timer\_delete](include_2zephyr_2posix_2time_8h.md#ad114bb350d7d5d12cff3fd19bf533303)([timer\_t](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d) timerid);

[ 100](include_2zephyr_2posix_2time_8h.md#a06dda57adfdeb4a9b346f69c95cba96a)int [timer\_gettime](include_2zephyr_2posix_2time_8h.md#a06dda57adfdeb4a9b346f69c95cba96a)([timer\_t](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d) timerid, struct [itimerspec](structitimerspec.md) \*its);

[ 101](include_2zephyr_2posix_2time_8h.md#a32207b51f2effa8441f4c728fd8519c0)int [timer\_settime](include_2zephyr_2posix_2time_8h.md#a32207b51f2effa8441f4c728fd8519c0)([timer\_t](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d) timerid, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), const struct [itimerspec](structitimerspec.md) \*value,

102 struct [itimerspec](structitimerspec.md) \*ovalue);

[ 103](include_2zephyr_2posix_2time_8h.md#ad779f0bc22f64bd3bd977221b0ce1b8f)int [timer\_getoverrun](include_2zephyr_2posix_2time_8h.md#ad779f0bc22f64bd3bd977221b0ce1b8f)([timer\_t](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d) timerid);

[ 104](include_2zephyr_2posix_2time_8h.md#a9ce6a1ed91a601dee133c8b6cf8b721a)int [nanosleep](include_2zephyr_2posix_2time_8h.md#a9ce6a1ed91a601dee133c8b6cf8b721a)(const struct [timespec](structtimespec.md) \*rqtp, struct [timespec](structtimespec.md) \*rmtp);

[ 105](include_2zephyr_2posix_2time_8h.md#a924d51d78cdcd9d7dee2613fb3a33cd1)int [clock\_nanosleep](include_2zephyr_2posix_2time_8h.md#a924d51d78cdcd9d7dee2613fb3a33cd1)([clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) clock\_id, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

106 const struct [timespec](structtimespec.md) \*rqtp, struct [timespec](structtimespec.md) \*rmtp);

107

108#ifdef \_\_cplusplus

109}

110#endif

111

112#else /\* ZEPHYR\_INCLUDE\_POSIX\_TIME\_H\_ \*/

113/\* Read the toolchain header when <posix/time.h> finds itself on the

114 \* first attempt.

115 \*/

116#include\_next <time.h>

117#endif /\* ZEPHYR\_INCLUDE\_POSIX\_TIME\_H\_ \*/

[time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7)

\_TIME\_T\_ time\_t

**Definition** \_timespec.h:14

[errno.h](errno_8h.md)

System error numbers.

[MSEC\_PER\_SEC](group__clock__apis.md#ga222f9dff749accf8de62bc4b52c7bdcd)

#define MSEC\_PER\_SEC

number of milliseconds per second

**Definition** sys\_clock.h:92

[NSEC\_PER\_MSEC](group__clock__apis.md#gad16e9029e202d2dfb4cfae8f09131f8f)

#define NSEC\_PER\_MSEC

number of nanoseconds per millisecond

**Definition** sys\_clock.h:86

[signal.h](include_2zephyr_2posix_2signal_8h.md)

[time.h](include_2zephyr_2posix_2time_8h.md)

[timer\_gettime](include_2zephyr_2posix_2time_8h.md#a06dda57adfdeb4a9b346f69c95cba96a)

int timer\_gettime(timer\_t timerid, struct itimerspec \*its)

[clock\_gettime](include_2zephyr_2posix_2time_8h.md#a21188eaca1b3e48ac3f7715398a1fc06)

int clock\_gettime(clockid\_t clock\_id, struct timespec \*ts)

[timer\_settime](include_2zephyr_2posix_2time_8h.md#a32207b51f2effa8441f4c728fd8519c0)

int timer\_settime(timer\_t timerid, int flags, const struct itimerspec \*value, struct itimerspec \*ovalue)

[clock\_getres](include_2zephyr_2posix_2time_8h.md#a3e1d049d0ed1519b99570efc4d8a1ae3)

int clock\_getres(clockid\_t clock\_id, struct timespec \*ts)

[clock\_nanosleep](include_2zephyr_2posix_2time_8h.md#a924d51d78cdcd9d7dee2613fb3a33cd1)

int clock\_nanosleep(clockid\_t clock\_id, int flags, const struct timespec \*rqtp, struct timespec \*rmtp)

[nanosleep](include_2zephyr_2posix_2time_8h.md#a9ce6a1ed91a601dee133c8b6cf8b721a)

int nanosleep(const struct timespec \*rqtp, struct timespec \*rmtp)

[clock\_getcpuclockid](include_2zephyr_2posix_2time_8h.md#ab2cd29aa41b2b485b571f05ac22d9f7f)

int clock\_getcpuclockid(pid\_t pid, clockid\_t \*clock\_id)

[timer\_create](include_2zephyr_2posix_2time_8h.md#ab36f0d44be3c22bae387064f49ab934c)

int timer\_create(clockid\_t clockId, struct sigevent \*evp, timer\_t \*timerid)

[timer\_delete](include_2zephyr_2posix_2time_8h.md#ad114bb350d7d5d12cff3fd19bf533303)

int timer\_delete(timer\_t timerid)

[timer\_getoverrun](include_2zephyr_2posix_2time_8h.md#ad779f0bc22f64bd3bd977221b0ce1b8f)

int timer\_getoverrun(timer\_t timerid)

[clock\_settime](include_2zephyr_2posix_2time_8h.md#adab8a7307d547eb2b882dd1cda3a7655)

int clock\_settime(clockid\_t clock\_id, const struct timespec \*ts)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[posix\_types.h](posix__types_8h.md)

[pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df)

int pid\_t

**Definition** posix\_types.h:25

[timer\_t](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d)

unsigned long timer\_t

**Definition** posix\_types.h:39

[clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea)

uint32\_t clockid\_t

**Definition** posix\_types.h:35

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[itimerspec](structitimerspec.md)

**Definition** timespec.h:12

[itimerspec::it\_interval](structitimerspec.md#a27cedae552e2b2fe0993c1b2c4ff1889)

struct timespec it\_interval

**Definition** timespec.h:13

[itimerspec::it\_value](structitimerspec.md#a754dda918053251c24558b07571d6e8f)

struct timespec it\_value

**Definition** timespec.h:14

[sigevent](structsigevent.md)

**Definition** signal.h:87

[timespec](structtimespec.md)

**Definition** \_timespec.h:22

[timespec::tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683)

long tv\_nsec

**Definition** \_timespec.h:24

[timespec::tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955)

time\_t tv\_sec

**Definition** \_timespec.h:23

[timespec.h](timespec_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [time.h](include_2zephyr_2posix_2time_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
