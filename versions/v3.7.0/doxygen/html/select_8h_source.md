---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/select_8h_source.html
original_path: doxygen/html/select_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

select.h

[Go to the documentation of this file.](select_8h.md)

1/\*

2 \* Copyright (c) 2019 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_SYS\_SELECT\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_SYS\_SELECT\_H\_

8

9#include <[zephyr/net/socket\_types.h](socket__types_8h.md)>

10#include <[zephyr/net/socket\_select.h](socket__select_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

[ 16](select_8h.md#a7acea921b59df1dc48b89b21ecfa446b)#define fd\_set zsock\_fd\_set

[ 17](select_8h.md#a86c5dbf5a99358e288f573d6a1e0873f)#define FD\_SETSIZE ZSOCK\_FD\_SETSIZE

[ 18](select_8h.md#aaf62b9bedda0be6bd5a878a9146883fe)#define FD\_ZERO ZSOCK\_FD\_ZERO

[ 19](select_8h.md#a279931aa1d0b7974e7a5a7cbaab4244f)#define FD\_SET ZSOCK\_FD\_SET

[ 20](select_8h.md#a3246fcda97abc25e2187633c7800df66)#define FD\_CLR ZSOCK\_FD\_CLR

[ 21](select_8h.md#ad23e70ae9e622bb3aa740c623d276d6f)#define FD\_ISSET ZSOCK\_FD\_ISSET

22

23struct [timeval](structtimeval.md);

24

[ 25](select_8h.md#aa95a19f21c5fced38c8bd3a64f362192)int [select](select_8h.md#aa95a19f21c5fced38c8bd3a64f362192)(int nfds, [fd\_set](select_8h.md#a7acea921b59df1dc48b89b21ecfa446b) \*readfds, [fd\_set](select_8h.md#a7acea921b59df1dc48b89b21ecfa446b) \*writefds, [fd\_set](select_8h.md#a7acea921b59df1dc48b89b21ecfa446b) \*exceptfds, struct [timeval](structtimeval.md) \*timeout);

26

27#ifdef \_\_cplusplus

28}

29#endif

30

31#endif /\* ZEPHYR\_INCLUDE\_POSIX\_SYS\_SELECT\_H\_ \*/

[fd\_set](select_8h.md#a7acea921b59df1dc48b89b21ecfa446b)

#define fd\_set

**Definition** select.h:16

[select](select_8h.md#aa95a19f21c5fced38c8bd3a64f362192)

int select(int nfds, zsock\_fd\_set \*readfds, zsock\_fd\_set \*writefds, zsock\_fd\_set \*exceptfds, struct timeval \*timeout)

[socket\_select.h](socket__select_8h.md)

BSD select support functions.

[socket\_types.h](socket__types_8h.md)

socket types definitionis

[timeval](structtimeval.md)

**Definition** \_timeval.h:22

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [select.h](select_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
