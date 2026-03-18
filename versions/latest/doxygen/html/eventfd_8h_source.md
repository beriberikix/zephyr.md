---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/eventfd_8h_source.html
original_path: doxygen/html/eventfd_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

eventfd.h

[Go to the documentation of this file.](eventfd_8h.md)

1/\*

2 \* Copyright (c) 2020 Tobias Svehagen

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_POSIX\_SYS\_EVENTFD\_H\_

8#define ZEPHYR\_INCLUDE\_POSIX\_SYS\_EVENTFD\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11

12#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

13#include <[zephyr/posix/fcntl.h](include_2zephyr_2posix_2fcntl_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

[ 19](eventfd_8h.md#abcdfb656e756cf2a492aff987df8d5f2)#define EFD\_IN\_USE 0x1 \_\_DEPRECATED\_MACRO

[ 20](eventfd_8h.md#aa1cf1f9ea4d84916ad5fdf7105d4ee1f)#define EFD\_SEMAPHORE 0x2

[ 21](eventfd_8h.md#a04677f5ad8d61c569b9c32ec35b05e7a)#define EFD\_NONBLOCK O\_NONBLOCK

[ 22](eventfd_8h.md#a0959e68b487308e9dd8586e56f072781)#define EFD\_FLAGS\_SET (EFD\_SEMAPHORE | EFD\_NONBLOCK) \_\_DEPRECATED\_MACRO

23

[ 24](eventfd_8h.md#ad6a5579f52209e68c4196c5473677db5)typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [eventfd\_t](eventfd_8h.md#ad6a5579f52209e68c4196c5473677db5);

25

[ 41](eventfd_8h.md#ab06039421a08cedb36946381608fa7f7)int [eventfd](eventfd_8h.md#ab06039421a08cedb36946381608fa7f7)(unsigned int initval, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

42

[ 53](eventfd_8h.md#a32e55549cb7aea88db8a14be9ed5d092)int [eventfd\_read](eventfd_8h.md#a32e55549cb7aea88db8a14be9ed5d092)(int fd, [eventfd\_t](eventfd_8h.md#ad6a5579f52209e68c4196c5473677db5) \*value);

54

[ 63](eventfd_8h.md#a9c7aafe8ee787e3ba362fb6aab3e5542)int [eventfd\_write](eventfd_8h.md#a9c7aafe8ee787e3ba362fb6aab3e5542)(int fd, [eventfd\_t](eventfd_8h.md#ad6a5579f52209e68c4196c5473677db5) value);

64

65#ifdef \_\_cplusplus

66}

67#endif

68

69#endif /\* ZEPHYR\_INCLUDE\_POSIX\_SYS\_EVENTFD\_H\_ \*/

[eventfd\_read](eventfd_8h.md#a32e55549cb7aea88db8a14be9ed5d092)

int eventfd\_read(int fd, eventfd\_t \*value)

Read from an eventfd.

[eventfd\_write](eventfd_8h.md#a9c7aafe8ee787e3ba362fb6aab3e5542)

int eventfd\_write(int fd, eventfd\_t value)

Write to an eventfd.

[eventfd](eventfd_8h.md#ab06039421a08cedb36946381608fa7f7)

int eventfd(unsigned int initval, int flags)

Create a file descriptor for event notification.

[eventfd\_t](eventfd_8h.md#ad6a5579f52209e68c4196c5473677db5)

uint64\_t eventfd\_t

**Definition** eventfd.h:24

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[fcntl.h](include_2zephyr_2posix_2fcntl_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[stdint.h](stdint_8h.md)

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [eventfd.h](eventfd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
