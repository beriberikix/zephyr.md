---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/aio_8h_source.html
original_path: doxygen/html/aio_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

aio.h

[Go to the documentation of this file.](aio_8h.md)

1/\*

2 \* Copyright 2024 Tenstorrent AI ULC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ZEPHYR\_POSIX\_AIO\_H\_

8#define ZEPHYR\_INCLUDE\_ZEPHYR\_POSIX\_AIO\_H\_

9

10#include <[signal.h](include_2zephyr_2posix_2signal_8h.md)>

11#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

12#include <[time.h](include_2zephyr_2posix_2time_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

[ 18](structaiocb.md)struct [aiocb](structaiocb.md) {

[ 19](structaiocb.md#ad6b6e95e6e4a79487f7e6edaae26003f) int [aio\_fildes](structaiocb.md#ad6b6e95e6e4a79487f7e6edaae26003f);

[ 20](structaiocb.md#a1e74b350a9ca189fa7c25b61c5cede6c) [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [aio\_offset](structaiocb.md#a1e74b350a9ca189fa7c25b61c5cede6c);

[ 21](structaiocb.md#a60a966202034e1abde4ca3ea0965fa30) volatile void \*[aio\_buf](structaiocb.md#a60a966202034e1abde4ca3ea0965fa30);

[ 22](structaiocb.md#a6b4f8a1d05ed5444784389734d71cda7) size\_t [aio\_nbytes](structaiocb.md#a6b4f8a1d05ed5444784389734d71cda7);

[ 23](structaiocb.md#a7a8f63c080c8602ebcacbb86e9f5547e) int [aio\_reqprio](structaiocb.md#a7a8f63c080c8602ebcacbb86e9f5547e);

[ 24](structaiocb.md#a7065f3086beb9cdffc525c1d09949268) struct [sigevent](structsigevent.md) [aio\_sigevent](structaiocb.md#a7065f3086beb9cdffc525c1d09949268);

[ 25](structaiocb.md#a8a23597de7bfc422b58ec9816ced7d47) int [aio\_lio\_opcode](structaiocb.md#a8a23597de7bfc422b58ec9816ced7d47);

26};

27

28#if \_POSIX\_C\_SOURCE >= 200112L

29

30int aio\_cancel(int fildes, struct [aiocb](structaiocb.md) \*aiocbp);

31int aio\_error(const struct [aiocb](structaiocb.md) \*aiocbp);

32int aio\_fsync(int filedes, struct [aiocb](structaiocb.md) \*aiocbp);

33int aio\_read(struct [aiocb](structaiocb.md) \*aiocbp);

34[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) aio\_return(struct [aiocb](structaiocb.md) \*aiocbp);

35int aio\_suspend(const struct [aiocb](structaiocb.md) \*const list[], int nent, const struct [timespec](structtimespec.md) \*timeout);

36int aio\_write(struct [aiocb](structaiocb.md) \*aiocbp);

37int lio\_listio(int mode, struct [aiocb](structaiocb.md) \*const [ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) list[], int nent,

38 struct [sigevent](structsigevent.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) sig);

39

40#endif /\* \_POSIX\_C\_SOURCE >= 200112L \*/

41

42#ifdef \_\_cplusplus

43}

44#endif

45

46#endif /\* ZEPHYR\_INCLUDE\_ZEPHYR\_POSIX\_AIO\_H\_ \*/

[signal.h](include_2zephyr_2posix_2signal_8h.md)

[time.h](include_2zephyr_2posix_2time_8h.md)

[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd)

#define ZRESTRICT

**Definition** common.h:36

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[aiocb](structaiocb.md)

**Definition** aio.h:18

[aiocb::aio\_offset](structaiocb.md#a1e74b350a9ca189fa7c25b61c5cede6c)

off\_t aio\_offset

**Definition** aio.h:20

[aiocb::aio\_buf](structaiocb.md#a60a966202034e1abde4ca3ea0965fa30)

volatile void \* aio\_buf

**Definition** aio.h:21

[aiocb::aio\_nbytes](structaiocb.md#a6b4f8a1d05ed5444784389734d71cda7)

size\_t aio\_nbytes

**Definition** aio.h:22

[aiocb::aio\_sigevent](structaiocb.md#a7065f3086beb9cdffc525c1d09949268)

struct sigevent aio\_sigevent

**Definition** aio.h:24

[aiocb::aio\_reqprio](structaiocb.md#a7a8f63c080c8602ebcacbb86e9f5547e)

int aio\_reqprio

**Definition** aio.h:23

[aiocb::aio\_lio\_opcode](structaiocb.md#a8a23597de7bfc422b58ec9816ced7d47)

int aio\_lio\_opcode

**Definition** aio.h:25

[aiocb::aio\_fildes](structaiocb.md#ad6b6e95e6e4a79487f7e6edaae26003f)

int aio\_fildes

**Definition** aio.h:19

[sigevent](structsigevent.md)

**Definition** signal.h:98

[timespec](structtimespec.md)

**Definition** \_timespec.h:22

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [aio.h](aio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
