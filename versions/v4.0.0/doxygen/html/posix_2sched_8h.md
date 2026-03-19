---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/posix_2sched_8h.html
original_path: doxygen/html/posix_2sched_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sched.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/posix/posix_types.h](posix__types_8h_source.md)>`  
`#include <[time.h](include_2zephyr_2posix_2time_8h_source.md)>`

[Go to the source code of this file.](posix_2sched_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SCHED\_OTHER](#a44c9baaf6f3c286f76783265b4938881)   0 |
| #define | [SCHED\_FIFO](#ab998332c6538a029b4eed398b7a423da)   1 |
| #define | [SCHED\_RR](#a2a29482379f591144ace39cbd659a257)   2 |

| Functions | |
| --- | --- |
| static int | [sched\_yield](#aa1124f0d208ff28b7d9cf563ff183e8d) (void) |
|  | Yield the processor. |
| int | [sched\_get\_priority\_min](#af1f370fc36ea6b22ed42b5ee3cf82a81) (int policy) |
| int | [sched\_get\_priority\_max](#afaebd1698caeb9b9b9e614ad84edd609) (int policy) |
| int | [sched\_getparam](#a563c7ac53bac2c1b51379147e66c44ec) ([pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) pid, struct sched\_param \*param) |
| int | [sched\_getscheduler](#a99fcb2532b1482d236dc04495a3f194d) ([pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) pid) |
| int | [sched\_setparam](#a06b497c4ea6bbabd2b62ba1a8a848a1b) ([pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) pid, const struct sched\_param \*param) |
| int | [sched\_setscheduler](#a84ad29a6f2ad27370df09c664ac65eac) ([pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) pid, int policy, const struct sched\_param \*param) |
| int | [sched\_rr\_get\_interval](#a484f0eb93529d29a66e24485725c4c7b) ([pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) pid, struct [timespec](structtimespec.md) \*interval) |

## Macro Definition Documentation

## [◆ ](#ab998332c6538a029b4eed398b7a423da)SCHED\_FIFO

| #define SCHED\_FIFO   1 |
| --- |

## [◆ ](#a44c9baaf6f3c286f76783265b4938881)SCHED\_OTHER

| #define SCHED\_OTHER   0 |
| --- |

## [◆ ](#a2a29482379f591144ace39cbd659a257)SCHED\_RR

| #define SCHED\_RR   2 |
| --- |

## Function Documentation

## [◆ ](#afaebd1698caeb9b9b9e614ad84edd609)sched\_get\_priority\_max()

| int sched\_get\_priority\_max | ( | int | *policy* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#af1f370fc36ea6b22ed42b5ee3cf82a81)sched\_get\_priority\_min()

| int sched\_get\_priority\_min | ( | int | *policy* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a563c7ac53bac2c1b51379147e66c44ec)sched\_getparam()

| int sched\_getparam | ( | [pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) | *pid*, |
| --- | --- | --- | --- |
|  |  | struct sched\_param \* | *param* ) |

## [◆ ](#a99fcb2532b1482d236dc04495a3f194d)sched\_getscheduler()

| int sched\_getscheduler | ( | [pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) | *pid* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a484f0eb93529d29a66e24485725c4c7b)sched\_rr\_get\_interval()

| int sched\_rr\_get\_interval | ( | [pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) | *pid*, |
| --- | --- | --- | --- |
|  |  | struct [timespec](structtimespec.md) \* | *interval* ) |

## [◆ ](#a06b497c4ea6bbabd2b62ba1a8a848a1b)sched\_setparam()

| int sched\_setparam | ( | [pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) | *pid*, |
| --- | --- | --- | --- |
|  |  | const struct sched\_param \* | *param* ) |

## [◆ ](#a84ad29a6f2ad27370df09c664ac65eac)sched\_setscheduler()

| int sched\_setscheduler | ( | [pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) | *pid*, |
| --- | --- | --- | --- |
|  |  | int | *policy*, |
|  |  | const struct sched\_param \* | *param* ) |

## [◆ ](#aa1124f0d208ff28b7d9cf563ff183e8d)sched\_yield()

| | int sched\_yield | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Yield the processor.

See IEEE 1003.1

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sched.h](posix_2sched_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
