---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/posix_2sys_2eventfd_8h_source.html
original_path: doxygen/html/posix_2sys_2eventfd_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

eventfd.h

[Go to the documentation of this file.](posix_2sys_2eventfd_8h.md)

1/\*

2 \* Copyright (c) 2020 Tobias Svehagen

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_POSIX\_SYS\_EVENTFD\_H\_

8#define ZEPHYR\_INCLUDE\_POSIX\_SYS\_EVENTFD\_H\_

9

10#include <[zephyr/zvfs/eventfd.h](zvfs_2eventfd_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

[ 16](posix_2sys_2eventfd_8h.md#aa1cf1f9ea4d84916ad5fdf7105d4ee1f)#define EFD\_SEMAPHORE ZVFS\_EFD\_SEMAPHORE

[ 17](posix_2sys_2eventfd_8h.md#a04677f5ad8d61c569b9c32ec35b05e7a)#define EFD\_NONBLOCK ZVFS\_EFD\_NONBLOCK

18

[ 19](posix_2sys_2eventfd_8h.md#ac8eb3d8ee0d064d293a5433c2c1f6165)typedef [zvfs\_eventfd\_t](zvfs_2eventfd_8h.md#a2f8a313f0a8175844c91c78d5b9340ad) [eventfd\_t](posix_2sys_2eventfd_8h.md#ac8eb3d8ee0d064d293a5433c2c1f6165);

20

[ 36](posix_2sys_2eventfd_8h.md#ab06039421a08cedb36946381608fa7f7)int [eventfd](posix_2sys_2eventfd_8h.md#ab06039421a08cedb36946381608fa7f7)(unsigned int initval, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

37

[ 48](posix_2sys_2eventfd_8h.md#a32e55549cb7aea88db8a14be9ed5d092)int [eventfd\_read](posix_2sys_2eventfd_8h.md#a32e55549cb7aea88db8a14be9ed5d092)(int fd, [eventfd\_t](posix_2sys_2eventfd_8h.md#ac8eb3d8ee0d064d293a5433c2c1f6165) \*value);

49

[ 58](posix_2sys_2eventfd_8h.md#a9c7aafe8ee787e3ba362fb6aab3e5542)int [eventfd\_write](posix_2sys_2eventfd_8h.md#a9c7aafe8ee787e3ba362fb6aab3e5542)(int fd, [eventfd\_t](posix_2sys_2eventfd_8h.md#ac8eb3d8ee0d064d293a5433c2c1f6165) value);

59

60#ifdef \_\_cplusplus

61}

62#endif

63

64#endif /\* ZEPHYR\_INCLUDE\_POSIX\_SYS\_EVENTFD\_H\_ \*/

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[eventfd\_read](posix_2sys_2eventfd_8h.md#a32e55549cb7aea88db8a14be9ed5d092)

int eventfd\_read(int fd, eventfd\_t \*value)

Read from an eventfd.

[eventfd\_write](posix_2sys_2eventfd_8h.md#a9c7aafe8ee787e3ba362fb6aab3e5542)

int eventfd\_write(int fd, eventfd\_t value)

Write to an eventfd.

[eventfd](posix_2sys_2eventfd_8h.md#ab06039421a08cedb36946381608fa7f7)

int eventfd(unsigned int initval, int flags)

Create a file descriptor for event notification.

[eventfd\_t](posix_2sys_2eventfd_8h.md#ac8eb3d8ee0d064d293a5433c2c1f6165)

zvfs\_eventfd\_t eventfd\_t

**Definition** eventfd.h:19

[eventfd.h](zvfs_2eventfd_8h.md)

[zvfs\_eventfd\_t](zvfs_2eventfd_8h.md#a2f8a313f0a8175844c91c78d5b9340ad)

uint64\_t zvfs\_eventfd\_t

**Definition** eventfd.h:21

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [eventfd.h](posix_2sys_2eventfd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
