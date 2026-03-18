---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/semaphore_8h_source.html
original_path: doxygen/html/semaphore_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

semaphore.h

[Go to the documentation of this file.](semaphore_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_SEMAPHORE\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_SEMAPHORE\_H\_

8

9#include <[zephyr/posix/time.h](include_2zephyr_2posix_2time_8h.md)>

10#include "[posix\_types.h](posix__types_8h.md)"

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

[ 16](semaphore_8h.md#a2ef55dcb46a51cb0f879f4c1724bdded)#define SEM\_FAILED ((sem\_t \*) 0)

17

[ 18](semaphore_8h.md#a42cc945f89772ca24e87a569a5f2dbd7)int [sem\_destroy](semaphore_8h.md#a42cc945f89772ca24e87a569a5f2dbd7)([sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \*semaphore);

[ 19](semaphore_8h.md#af4d15a2fd215951eb7ea2424ffdd335e)int [sem\_getvalue](semaphore_8h.md#af4d15a2fd215951eb7ea2424ffdd335e)([sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) semaphore, int \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) value);

[ 20](semaphore_8h.md#a1fee59859601fb325fafb32ee41b5691)int [sem\_init](semaphore_8h.md#a1fee59859601fb325fafb32ee41b5691)([sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \*semaphore, int pshared, unsigned int value);

[ 21](semaphore_8h.md#a2bee748f81a960f80dfccf675f38e3d8)int [sem\_post](semaphore_8h.md#a2bee748f81a960f80dfccf675f38e3d8)([sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \*semaphore);

[ 22](semaphore_8h.md#a91a6510735a16f94defc52ecbb7971ac)int [sem\_timedwait](semaphore_8h.md#a91a6510735a16f94defc52ecbb7971ac)([sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) semaphore, struct [timespec](structtimespec.md) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) abstime);

[ 23](semaphore_8h.md#a0f2fd32f79e2815f52f2afd2f5069960)int [sem\_trywait](semaphore_8h.md#a0f2fd32f79e2815f52f2afd2f5069960)([sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \*semaphore);

[ 24](semaphore_8h.md#a355d892eec64a2dc95143635469c6524)int [sem\_wait](semaphore_8h.md#a355d892eec64a2dc95143635469c6524)([sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \*semaphore);

[ 25](semaphore_8h.md#a0ed06fc3db017281dc6f1eefff97053a)[sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \*[sem\_open](semaphore_8h.md#a0ed06fc3db017281dc6f1eefff97053a)(const char \*name, int oflags, ...);

[ 26](semaphore_8h.md#a776256d1a473906f8b7490689bfcb75c)int [sem\_unlink](semaphore_8h.md#a776256d1a473906f8b7490689bfcb75c)(const char \*name);

[ 27](semaphore_8h.md#a4e398fea1080fd7919e5c72ee94e2fc5)int [sem\_close](semaphore_8h.md#a4e398fea1080fd7919e5c72ee94e2fc5)([sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \*sem);

28

29#ifdef \_\_cplusplus

30}

31#endif

32

33#endif /\* ZEPHYR\_INCLUDE\_POSIX\_SEMAPHORE\_H\_ \*/

[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd)

#define ZRESTRICT

**Definition** common.h:36

[time.h](include_2zephyr_2posix_2time_8h.md)

[posix\_types.h](posix__types_8h.md)

[sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e)

struct k\_sem sem\_t

**Definition** posix\_types.h:57

[sem\_open](semaphore_8h.md#a0ed06fc3db017281dc6f1eefff97053a)

sem\_t \* sem\_open(const char \*name, int oflags,...)

[sem\_trywait](semaphore_8h.md#a0f2fd32f79e2815f52f2afd2f5069960)

int sem\_trywait(sem\_t \*semaphore)

[sem\_init](semaphore_8h.md#a1fee59859601fb325fafb32ee41b5691)

int sem\_init(sem\_t \*semaphore, int pshared, unsigned int value)

[sem\_post](semaphore_8h.md#a2bee748f81a960f80dfccf675f38e3d8)

int sem\_post(sem\_t \*semaphore)

[sem\_wait](semaphore_8h.md#a355d892eec64a2dc95143635469c6524)

int sem\_wait(sem\_t \*semaphore)

[sem\_destroy](semaphore_8h.md#a42cc945f89772ca24e87a569a5f2dbd7)

int sem\_destroy(sem\_t \*semaphore)

[sem\_close](semaphore_8h.md#a4e398fea1080fd7919e5c72ee94e2fc5)

int sem\_close(sem\_t \*sem)

[sem\_unlink](semaphore_8h.md#a776256d1a473906f8b7490689bfcb75c)

int sem\_unlink(const char \*name)

[sem\_timedwait](semaphore_8h.md#a91a6510735a16f94defc52ecbb7971ac)

int sem\_timedwait(sem\_t \*ZRESTRICT semaphore, struct timespec \*ZRESTRICT abstime)

[sem\_getvalue](semaphore_8h.md#af4d15a2fd215951eb7ea2424ffdd335e)

int sem\_getvalue(sem\_t \*ZRESTRICT semaphore, int \*ZRESTRICT value)

[timespec](structtimespec.md)

**Definition** \_timespec.h:22

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [semaphore.h](semaphore_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
