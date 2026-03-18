---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/include_2zephyr_2posix_2time_8h.html
original_path: doxygen/html/include_2zephyr_2posix_2time_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

time.h File Reference

`#include <[time.h](include_2zephyr_2posix_2time_8h_source.md)>`  
`#include <[sys/timespec.h](timespec_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[errno.h](errno_8h_source.md)>`  
`#include "[posix_types.h](posix__types_8h_source.md)"`  
`#include <[zephyr/posix/signal.h](include_2zephyr_2posix_2signal_8h_source.md)>`

[Go to the source code of this file.](include_2zephyr_2posix_2time_8h_source.md)

| Macros | |
| --- | --- |
| #define | [CLOCK\_REALTIME](#a922ce1ae64374c9410c8a999e25e82af)   1 |
| #define | [CLOCK\_PROCESS\_CPUTIME\_ID](#ae1c3939a1e7b7cd1e5a4a7fa601cc4e9)   2 |
| #define | [CLOCK\_THREAD\_CPUTIME\_ID](#a30114e19c18f57f83727bcaba2458f1e)   3 |
| #define | [CLOCK\_MONOTONIC](#a6fb83f5e91e704391ff796553d5e0f46)   4 |
| #define | [TIMER\_ABSTIME](#adde83d9ea51f12d4149f016eededde54)   4 |

| Functions | |
| --- | --- |
| int | [clock\_gettime](#a21188eaca1b3e48ac3f7715398a1fc06) ([clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) clock\_id, struct [timespec](structtimespec.md) \*ts) |
| int | [clock\_getres](#a3e1d049d0ed1519b99570efc4d8a1ae3) ([clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) clock\_id, struct [timespec](structtimespec.md) \*ts) |
| int | [clock\_settime](#adab8a7307d547eb2b882dd1cda3a7655) ([clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) clock\_id, const struct [timespec](structtimespec.md) \*ts) |
| int | [clock\_getcpuclockid](#ab2cd29aa41b2b485b571f05ac22d9f7f) ([pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) pid, [clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) \*clock\_id) |
| int | [timer\_create](#ab36f0d44be3c22bae387064f49ab934c) ([clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) clockId, struct [sigevent](structsigevent.md) \*evp, [timer\_t](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d) \*timerid) |
| int | [timer\_delete](#ad114bb350d7d5d12cff3fd19bf533303) ([timer\_t](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d) timerid) |
| int | [timer\_gettime](#a06dda57adfdeb4a9b346f69c95cba96a) ([timer\_t](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d) timerid, struct [itimerspec](structitimerspec.md) \*its) |
| int | [timer\_settime](#a32207b51f2effa8441f4c728fd8519c0) ([timer\_t](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d) timerid, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), const struct [itimerspec](structitimerspec.md) \*value, struct [itimerspec](structitimerspec.md) \*ovalue) |
| int | [timer\_getoverrun](#ad779f0bc22f64bd3bd977221b0ce1b8f) ([timer\_t](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d) timerid) |
| int | [nanosleep](#a9ce6a1ed91a601dee133c8b6cf8b721a) (const struct [timespec](structtimespec.md) \*rqtp, struct [timespec](structtimespec.md) \*rmtp) |
| int | [clock\_nanosleep](#a924d51d78cdcd9d7dee2613fb3a33cd1) ([clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) clock\_id, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), const struct [timespec](structtimespec.md) \*rqtp, struct [timespec](structtimespec.md) \*rmtp) |

## Macro Definition Documentation

## [◆ ](#a6fb83f5e91e704391ff796553d5e0f46)CLOCK\_MONOTONIC

| #define CLOCK\_MONOTONIC   4 |
| --- |

## [◆ ](#ae1c3939a1e7b7cd1e5a4a7fa601cc4e9)CLOCK\_PROCESS\_CPUTIME\_ID

| #define CLOCK\_PROCESS\_CPUTIME\_ID   2 |
| --- |

## [◆ ](#a922ce1ae64374c9410c8a999e25e82af)CLOCK\_REALTIME

| #define CLOCK\_REALTIME   1 |
| --- |

## [◆ ](#a30114e19c18f57f83727bcaba2458f1e)CLOCK\_THREAD\_CPUTIME\_ID

| #define CLOCK\_THREAD\_CPUTIME\_ID   3 |
| --- |

## [◆ ](#adde83d9ea51f12d4149f016eededde54)TIMER\_ABSTIME

| #define TIMER\_ABSTIME   4 |
| --- |

## Function Documentation

## [◆ ](#ab2cd29aa41b2b485b571f05ac22d9f7f)clock\_getcpuclockid()

| int clock\_getcpuclockid | ( | [pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) | *pid*, |
| --- | --- | --- | --- |
|  |  | [clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) \* | *clock\_id* ) |

## [◆ ](#a3e1d049d0ed1519b99570efc4d8a1ae3)clock\_getres()

| int clock\_getres | ( | [clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) | *clock\_id*, |
| --- | --- | --- | --- |
|  |  | struct [timespec](structtimespec.md) \* | *ts* ) |

## [◆ ](#a21188eaca1b3e48ac3f7715398a1fc06)clock\_gettime()

| int clock\_gettime | ( | [clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) | *clock\_id*, |
| --- | --- | --- | --- |
|  |  | struct [timespec](structtimespec.md) \* | *ts* ) |

## [◆ ](#a924d51d78cdcd9d7dee2613fb3a33cd1)clock\_nanosleep()

| int clock\_nanosleep | ( | [clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) | *clock\_id*, |
| --- | --- | --- | --- |
|  |  | int | *flags*, |
|  |  | const struct [timespec](structtimespec.md) \* | *rqtp*, |
|  |  | struct [timespec](structtimespec.md) \* | *rmtp* ) |

## [◆ ](#adab8a7307d547eb2b882dd1cda3a7655)clock\_settime()

| int clock\_settime | ( | [clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) | *clock\_id*, |
| --- | --- | --- | --- |
|  |  | const struct [timespec](structtimespec.md) \* | *ts* ) |

## [◆ ](#a9ce6a1ed91a601dee133c8b6cf8b721a)nanosleep()

| int nanosleep | ( | const struct [timespec](structtimespec.md) \* | *rqtp*, |
| --- | --- | --- | --- |
|  |  | struct [timespec](structtimespec.md) \* | *rmtp* ) |

## [◆ ](#ab36f0d44be3c22bae387064f49ab934c)timer\_create()

| int timer\_create | ( | [clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) | *clockId*, |
| --- | --- | --- | --- |
|  |  | struct [sigevent](structsigevent.md) \* | *evp*, |
|  |  | [timer\_t](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d) \* | *timerid* ) |

## [◆ ](#ad114bb350d7d5d12cff3fd19bf533303)timer\_delete()

| int timer\_delete | ( | [timer\_t](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d) | *timerid* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ad779f0bc22f64bd3bd977221b0ce1b8f)timer\_getoverrun()

| int timer\_getoverrun | ( | [timer\_t](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d) | *timerid* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a06dda57adfdeb4a9b346f69c95cba96a)timer\_gettime()

| int timer\_gettime | ( | [timer\_t](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d) | *timerid*, |
| --- | --- | --- | --- |
|  |  | struct [itimerspec](structitimerspec.md) \* | *its* ) |

## [◆ ](#a32207b51f2effa8441f4c728fd8519c0)timer\_settime()

| int timer\_settime | ( | [timer\_t](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d) | *timerid*, |
| --- | --- | --- | --- |
|  |  | int | *flags*, |
|  |  | const struct [itimerspec](structitimerspec.md) \* | *value*, |
|  |  | struct [itimerspec](structitimerspec.md) \* | *ovalue* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [time.h](include_2zephyr_2posix_2time_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
