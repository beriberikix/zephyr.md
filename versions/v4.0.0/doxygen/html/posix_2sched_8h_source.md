---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/posix_2sched_8h_source.html
original_path: doxygen/html/posix_2sched_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sched.h

[Go to the documentation of this file.](posix_2sched_8h.md)

1/\*

2 \* Copyright (c) 2018-2023 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_SCHED\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_SCHED\_H\_

8

9#include <[zephyr/kernel.h](kernel_8h.md)>

10#include <[zephyr/posix/posix\_types.h](posix__types_8h.md)>

11

12#include <[time.h](include_2zephyr_2posix_2time_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

18/\*

19 \* Other mandatory scheduling policy. Must be numerically distinct. May

20 \* execute identically to SCHED\_RR or SCHED\_FIFO. For Zephyr this is a

21 \* pseudonym for SCHED\_RR.

22 \*/

[ 23](posix_2sched_8h.md#a44c9baaf6f3c286f76783265b4938881)#define SCHED\_OTHER 0

24

25/\* Cooperative scheduling policy \*/

[ 26](posix_2sched_8h.md#ab998332c6538a029b4eed398b7a423da)#define SCHED\_FIFO 1

27

28/\* Priority based preemptive scheduling policy \*/

[ 29](posix_2sched_8h.md#a2a29482379f591144ace39cbd659a257)#define SCHED\_RR 2

30

31#if defined(CONFIG\_MINIMAL\_LIBC) || defined(CONFIG\_PICOLIBC) || defined(CONFIG\_ARMCLANG\_STD\_LIBC) \

32 || defined(CONFIG\_ARCMWDT\_LIBC)

33struct sched\_param {

34 int sched\_priority;

35};

36#endif

37

[ 43](posix_2sched_8h.md#aa1124f0d208ff28b7d9cf563ff183e8d)static inline int [sched\_yield](posix_2sched_8h.md#aa1124f0d208ff28b7d9cf563ff183e8d)(void)

44{

45 [k\_yield](group__thread__apis.md#ga08a3484c33444ecedc2d71d78495a295)();

46 return 0;

47}

48

[ 49](posix_2sched_8h.md#af1f370fc36ea6b22ed42b5ee3cf82a81)int [sched\_get\_priority\_min](posix_2sched_8h.md#af1f370fc36ea6b22ed42b5ee3cf82a81)(int policy);

[ 50](posix_2sched_8h.md#afaebd1698caeb9b9b9e614ad84edd609)int [sched\_get\_priority\_max](posix_2sched_8h.md#afaebd1698caeb9b9b9e614ad84edd609)(int policy);

51

[ 52](posix_2sched_8h.md#a563c7ac53bac2c1b51379147e66c44ec)int [sched\_getparam](posix_2sched_8h.md#a563c7ac53bac2c1b51379147e66c44ec)([pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) pid, struct sched\_param \*param);

[ 53](posix_2sched_8h.md#a99fcb2532b1482d236dc04495a3f194d)int [sched\_getscheduler](posix_2sched_8h.md#a99fcb2532b1482d236dc04495a3f194d)([pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) pid);

54

[ 55](posix_2sched_8h.md#a06b497c4ea6bbabd2b62ba1a8a848a1b)int [sched\_setparam](posix_2sched_8h.md#a06b497c4ea6bbabd2b62ba1a8a848a1b)([pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) pid, const struct sched\_param \*param);

[ 56](posix_2sched_8h.md#a84ad29a6f2ad27370df09c664ac65eac)int [sched\_setscheduler](posix_2sched_8h.md#a84ad29a6f2ad27370df09c664ac65eac)([pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) pid, int policy, const struct sched\_param \*param);

[ 57](posix_2sched_8h.md#a484f0eb93529d29a66e24485725c4c7b)int [sched\_rr\_get\_interval](posix_2sched_8h.md#a484f0eb93529d29a66e24485725c4c7b)([pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) pid, struct [timespec](structtimespec.md) \*interval);

58

59#ifdef \_\_cplusplus

60}

61#endif

62

63#endif /\* ZEPHYR\_INCLUDE\_POSIX\_SCHED\_H\_ \*/

[k\_yield](group__thread__apis.md#ga08a3484c33444ecedc2d71d78495a295)

void k\_yield(void)

Yield the current thread.

[time.h](include_2zephyr_2posix_2time_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[sched\_setparam](posix_2sched_8h.md#a06b497c4ea6bbabd2b62ba1a8a848a1b)

int sched\_setparam(pid\_t pid, const struct sched\_param \*param)

[sched\_rr\_get\_interval](posix_2sched_8h.md#a484f0eb93529d29a66e24485725c4c7b)

int sched\_rr\_get\_interval(pid\_t pid, struct timespec \*interval)

[sched\_getparam](posix_2sched_8h.md#a563c7ac53bac2c1b51379147e66c44ec)

int sched\_getparam(pid\_t pid, struct sched\_param \*param)

[sched\_setscheduler](posix_2sched_8h.md#a84ad29a6f2ad27370df09c664ac65eac)

int sched\_setscheduler(pid\_t pid, int policy, const struct sched\_param \*param)

[sched\_getscheduler](posix_2sched_8h.md#a99fcb2532b1482d236dc04495a3f194d)

int sched\_getscheduler(pid\_t pid)

[sched\_yield](posix_2sched_8h.md#aa1124f0d208ff28b7d9cf563ff183e8d)

static int sched\_yield(void)

Yield the processor.

**Definition** sched.h:43

[sched\_get\_priority\_min](posix_2sched_8h.md#af1f370fc36ea6b22ed42b5ee3cf82a81)

int sched\_get\_priority\_min(int policy)

[sched\_get\_priority\_max](posix_2sched_8h.md#afaebd1698caeb9b9b9e614ad84edd609)

int sched\_get\_priority\_max(int policy)

[posix\_types.h](posix__types_8h.md)

[pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df)

int pid\_t

**Definition** posix\_types.h:79

[timespec](structtimespec.md)

**Definition** \_timespec.h:22

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sched.h](posix_2sched_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
