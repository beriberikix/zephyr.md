---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/posix_2sched_8h_source.html
original_path: doxygen/html/posix_2sched_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

9#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

10

11#include "[posix\_types.h](posix__types_8h.md)"

12

13#include <[time.h](include_2zephyr_2posix_2time_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

19/\*

20 \* Other mandatory scheduling policy. Must be numerically distinct. May

21 \* execute identically to SCHED\_RR or SCHED\_FIFO. For Zephyr this is a

22 \* pseudonym for SCHED\_RR.

23 \*/

[ 24](posix_2sched_8h.md#a44c9baaf6f3c286f76783265b4938881)#define SCHED\_OTHER 0

25

26/\* Cooperative scheduling policy \*/

[ 27](posix_2sched_8h.md#ab998332c6538a029b4eed398b7a423da)#define SCHED\_FIFO 1

28

29/\* Priority based preemptive scheduling policy \*/

[ 30](posix_2sched_8h.md#a2a29482379f591144ace39cbd659a257)#define SCHED\_RR 2

31

32#if defined(CONFIG\_MINIMAL\_LIBC) || defined(CONFIG\_PICOLIBC) || defined(CONFIG\_ARMCLANG\_STD\_LIBC) \

33 || defined(CONFIG\_ARCMWDT\_LIBC)

34struct sched\_param {

35 int sched\_priority;

36};

37#endif

38

[ 44](posix_2sched_8h.md#aa1124f0d208ff28b7d9cf563ff183e8d)static inline int [sched\_yield](posix_2sched_8h.md#aa1124f0d208ff28b7d9cf563ff183e8d)(void)

45{

46 [k\_yield](group__thread__apis.md#ga08a3484c33444ecedc2d71d78495a295)();

47 return 0;

48}

49

[ 50](posix_2sched_8h.md#af1f370fc36ea6b22ed42b5ee3cf82a81)int [sched\_get\_priority\_min](posix_2sched_8h.md#af1f370fc36ea6b22ed42b5ee3cf82a81)(int policy);

[ 51](posix_2sched_8h.md#afaebd1698caeb9b9b9e614ad84edd609)int [sched\_get\_priority\_max](posix_2sched_8h.md#afaebd1698caeb9b9b9e614ad84edd609)(int policy);

52

[ 53](posix_2sched_8h.md#a563c7ac53bac2c1b51379147e66c44ec)int [sched\_getparam](posix_2sched_8h.md#a563c7ac53bac2c1b51379147e66c44ec)([pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) pid, struct sched\_param \*param);

[ 54](posix_2sched_8h.md#a99fcb2532b1482d236dc04495a3f194d)int [sched\_getscheduler](posix_2sched_8h.md#a99fcb2532b1482d236dc04495a3f194d)([pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) pid);

55

[ 56](posix_2sched_8h.md#a06b497c4ea6bbabd2b62ba1a8a848a1b)int [sched\_setparam](posix_2sched_8h.md#a06b497c4ea6bbabd2b62ba1a8a848a1b)([pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) pid, const struct sched\_param \*param);

[ 57](posix_2sched_8h.md#a84ad29a6f2ad27370df09c664ac65eac)int [sched\_setscheduler](posix_2sched_8h.md#a84ad29a6f2ad27370df09c664ac65eac)([pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) pid, int policy, const struct sched\_param \*param);

[ 58](posix_2sched_8h.md#a484f0eb93529d29a66e24485725c4c7b)int [sched\_rr\_get\_interval](posix_2sched_8h.md#a484f0eb93529d29a66e24485725c4c7b)([pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) pid, struct [timespec](structtimespec.md) \*interval);

59

60#ifdef \_\_cplusplus

61}

62#endif

63

64#endif /\* ZEPHYR\_INCLUDE\_POSIX\_SCHED\_H\_ \*/

[k\_yield](group__thread__apis.md#ga08a3484c33444ecedc2d71d78495a295)

void k\_yield(void)

Yield the current thread.

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[time.h](include_2zephyr_2posix_2time_8h.md)

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

**Definition** sched.h:44

[sched\_get\_priority\_min](posix_2sched_8h.md#af1f370fc36ea6b22ed42b5ee3cf82a81)

int sched\_get\_priority\_min(int policy)

[sched\_get\_priority\_max](posix_2sched_8h.md#afaebd1698caeb9b9b9e614ad84edd609)

int sched\_get\_priority\_max(int policy)

[posix\_types.h](posix__types_8h.md)

[pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df)

int pid\_t

**Definition** posix\_types.h:24

[timespec](structtimespec.md)

**Definition** \_timespec.h:22

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sched.h](posix_2sched_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
