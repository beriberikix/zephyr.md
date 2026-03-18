---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mqueue_8h_source.html
original_path: doxygen/html/mqueue_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqueue.h

[Go to the documentation of this file.](mqueue_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_POSIX\_MESSAGE\_PASSING\_H\_

8#define ZEPHYR\_INCLUDE\_POSIX\_MESSAGE\_PASSING\_H\_

9

10#include <[zephyr/kernel.h](kernel_8h.md)>

11#include <[zephyr/posix/time.h](include_2zephyr_2posix_2time_8h.md)>

12#include <[zephyr/posix/fcntl.h](fcntl_8h.md)>

13#include <[zephyr/posix/signal.h](include_2zephyr_2posix_2signal_8h.md)>

14#include <[zephyr/posix/sys/stat.h](stat_8h.md)>

15#include "[posix\_types.h](posix__types_8h.md)"

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

[ 21](mqueue_8h.md#aa03ac56b19aba70879b7e2934da6a507)typedef void \*[mqd\_t](mqueue_8h.md#aa03ac56b19aba70879b7e2934da6a507);

22

[ 23](structmq__attr.md)struct [mq\_attr](structmq__attr.md) {

[ 24](structmq__attr.md#a19c05fa88c6d1126120d800647ddb0dd) long [mq\_flags](structmq__attr.md#a19c05fa88c6d1126120d800647ddb0dd);

[ 25](structmq__attr.md#aa535e1fa6c07c1d189e720ba15f9af08) long [mq\_maxmsg](structmq__attr.md#aa535e1fa6c07c1d189e720ba15f9af08);

[ 26](structmq__attr.md#ae975d1d907081c1e53b079c981c32209) long [mq\_msgsize](structmq__attr.md#ae975d1d907081c1e53b079c981c32209);

[ 27](structmq__attr.md#a08cfd508cef817ba351c1af8d9af50f5) long [mq\_curmsgs](structmq__attr.md#a08cfd508cef817ba351c1af8d9af50f5); /\* Number of messages currently queued. \*/

28};

29

[ 30](mqueue_8h.md#a6e6c4881ac0fd3ad18d733b96d088b8b)[mqd\_t](mqueue_8h.md#aa03ac56b19aba70879b7e2934da6a507) [mq\_open](mqueue_8h.md#a6e6c4881ac0fd3ad18d733b96d088b8b)(const char \*name, int oflags, ...);

[ 31](mqueue_8h.md#a3fbd3906296be63451c64d69be2bc371)int [mq\_close](mqueue_8h.md#a3fbd3906296be63451c64d69be2bc371)([mqd\_t](mqueue_8h.md#aa03ac56b19aba70879b7e2934da6a507) mqdes);

[ 32](mqueue_8h.md#accd8c5ee36e60d990963e1d544ef4140)int [mq\_unlink](mqueue_8h.md#accd8c5ee36e60d990963e1d544ef4140)(const char \*name);

[ 33](mqueue_8h.md#a5a55ce03d8466a53a36601aaca9ee328)int [mq\_getattr](mqueue_8h.md#a5a55ce03d8466a53a36601aaca9ee328)([mqd\_t](mqueue_8h.md#aa03ac56b19aba70879b7e2934da6a507) mqdes, struct [mq\_attr](structmq__attr.md) \*mqstat);

[ 34](mqueue_8h.md#ae0ff0175064ab31858eff0669b7e745b)int [mq\_receive](mqueue_8h.md#ae0ff0175064ab31858eff0669b7e745b)([mqd\_t](mqueue_8h.md#aa03ac56b19aba70879b7e2934da6a507) mqdes, char \*msg\_ptr, size\_t msg\_len,

35 unsigned int \*msg\_prio);

[ 36](mqueue_8h.md#af13b6f0b3b15e14624b0c50050d062a4)int [mq\_send](mqueue_8h.md#af13b6f0b3b15e14624b0c50050d062a4)([mqd\_t](mqueue_8h.md#aa03ac56b19aba70879b7e2934da6a507) mqdes, const char \*msg\_ptr, size\_t msg\_len,

37 unsigned int msg\_prio);

[ 38](mqueue_8h.md#a83b7aa93cb6f1f5a4fd938baea5579a6)int [mq\_setattr](mqueue_8h.md#a83b7aa93cb6f1f5a4fd938baea5579a6)([mqd\_t](mqueue_8h.md#aa03ac56b19aba70879b7e2934da6a507) mqdes, const struct [mq\_attr](structmq__attr.md) \*mqstat,

39 struct [mq\_attr](structmq__attr.md) \*omqstat);

[ 40](mqueue_8h.md#aaf2e88ac75eac32eb5a3672fd56759b7)int [mq\_timedreceive](mqueue_8h.md#aaf2e88ac75eac32eb5a3672fd56759b7)([mqd\_t](mqueue_8h.md#aa03ac56b19aba70879b7e2934da6a507) mqdes, char \*msg\_ptr, size\_t msg\_len,

41 unsigned int \*msg\_prio, const struct [timespec](structtimespec.md) \*abstime);

[ 42](mqueue_8h.md#ac19939c8157d7ef9033a5be97a7ca6a1)int [mq\_timedsend](mqueue_8h.md#ac19939c8157d7ef9033a5be97a7ca6a1)([mqd\_t](mqueue_8h.md#aa03ac56b19aba70879b7e2934da6a507) mqdes, const char \*msg\_ptr, size\_t msg\_len,

43 unsigned int msg\_prio, const struct [timespec](structtimespec.md) \*abstime);

[ 44](mqueue_8h.md#a5eadbb82e0b9702d77f384a27827b334)int [mq\_notify](mqueue_8h.md#a5eadbb82e0b9702d77f384a27827b334)([mqd\_t](mqueue_8h.md#aa03ac56b19aba70879b7e2934da6a507) mqdes, const struct [sigevent](structsigevent.md) \*notification);

45

46#ifdef \_\_cplusplus

47}

48#endif

49

50#endif /\* ZEPHYR\_INCLUDE\_POSIX\_MESSAGE\_PASSING\_H\_ \*/

[fcntl.h](fcntl_8h.md)

[signal.h](include_2zephyr_2posix_2signal_8h.md)

[time.h](include_2zephyr_2posix_2time_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[mq\_close](mqueue_8h.md#a3fbd3906296be63451c64d69be2bc371)

int mq\_close(mqd\_t mqdes)

[mq\_getattr](mqueue_8h.md#a5a55ce03d8466a53a36601aaca9ee328)

int mq\_getattr(mqd\_t mqdes, struct mq\_attr \*mqstat)

[mq\_notify](mqueue_8h.md#a5eadbb82e0b9702d77f384a27827b334)

int mq\_notify(mqd\_t mqdes, const struct sigevent \*notification)

[mq\_open](mqueue_8h.md#a6e6c4881ac0fd3ad18d733b96d088b8b)

mqd\_t mq\_open(const char \*name, int oflags,...)

[mq\_setattr](mqueue_8h.md#a83b7aa93cb6f1f5a4fd938baea5579a6)

int mq\_setattr(mqd\_t mqdes, const struct mq\_attr \*mqstat, struct mq\_attr \*omqstat)

[mqd\_t](mqueue_8h.md#aa03ac56b19aba70879b7e2934da6a507)

void \* mqd\_t

**Definition** mqueue.h:21

[mq\_timedreceive](mqueue_8h.md#aaf2e88ac75eac32eb5a3672fd56759b7)

int mq\_timedreceive(mqd\_t mqdes, char \*msg\_ptr, size\_t msg\_len, unsigned int \*msg\_prio, const struct timespec \*abstime)

[mq\_timedsend](mqueue_8h.md#ac19939c8157d7ef9033a5be97a7ca6a1)

int mq\_timedsend(mqd\_t mqdes, const char \*msg\_ptr, size\_t msg\_len, unsigned int msg\_prio, const struct timespec \*abstime)

[mq\_unlink](mqueue_8h.md#accd8c5ee36e60d990963e1d544ef4140)

int mq\_unlink(const char \*name)

[mq\_receive](mqueue_8h.md#ae0ff0175064ab31858eff0669b7e745b)

int mq\_receive(mqd\_t mqdes, char \*msg\_ptr, size\_t msg\_len, unsigned int \*msg\_prio)

[mq\_send](mqueue_8h.md#af13b6f0b3b15e14624b0c50050d062a4)

int mq\_send(mqd\_t mqdes, const char \*msg\_ptr, size\_t msg\_len, unsigned int msg\_prio)

[posix\_types.h](posix__types_8h.md)

[stat.h](stat_8h.md)

[mq\_attr](structmq__attr.md)

**Definition** mqueue.h:23

[mq\_attr::mq\_curmsgs](structmq__attr.md#a08cfd508cef817ba351c1af8d9af50f5)

long mq\_curmsgs

**Definition** mqueue.h:27

[mq\_attr::mq\_flags](structmq__attr.md#a19c05fa88c6d1126120d800647ddb0dd)

long mq\_flags

**Definition** mqueue.h:24

[mq\_attr::mq\_maxmsg](structmq__attr.md#aa535e1fa6c07c1d189e720ba15f9af08)

long mq\_maxmsg

**Definition** mqueue.h:25

[mq\_attr::mq\_msgsize](structmq__attr.md#ae975d1d907081c1e53b079c981c32209)

long mq\_msgsize

**Definition** mqueue.h:26

[sigevent](structsigevent.md)

**Definition** signal.h:87

[timespec](structtimespec.md)

**Definition** \_timespec.h:22

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [mqueue.h](mqueue_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
