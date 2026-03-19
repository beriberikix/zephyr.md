---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/select_8h_source.html
original_path: doxygen/html/select_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

9#include <[zephyr/posix/posix\_types.h](posix__types_8h.md)>

10#include <[zephyr/sys/fdtable.h](fdtable_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

[ 16](select_8h.md#a86c5dbf5a99358e288f573d6a1e0873f)#define FD\_SETSIZE ZVFS\_FD\_SETSIZE

17

[ 18](select_8h.md#ae96e561afd32b1445d8a7370f23762a2)typedef struct [zvfs\_fd\_set](structzvfs__fd__set.md) [fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2);

19

20struct [timeval](structtimeval.md);

21

[ 22](select_8h.md#a2aed0a9b18a0ac6a3b8bb3ea9c3a34ab)int [pselect](select_8h.md#a2aed0a9b18a0ac6a3b8bb3ea9c3a34ab)(int nfds, [fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2) \*readfds, [fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2) \*writefds, [fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2) \*exceptfds,

23 const struct [timespec](structtimespec.md) \*timeout, const void \*sigmask);

[ 24](select_8h.md#a7ffa34f8c9a12e7fd43f5ef65bf889fa)int [select](select_8h.md#a7ffa34f8c9a12e7fd43f5ef65bf889fa)(int nfds, [fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2) \*readfds, [fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2) \*writefds, [fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2) \*errorfds, struct [timeval](structtimeval.md) \*timeout);

[ 25](select_8h.md#a0835759308c63ca23a1760980eea21d7)void [FD\_CLR](select_8h.md#a0835759308c63ca23a1760980eea21d7)(int fd, [fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2) \*fdset);

[ 26](select_8h.md#ac38fe1ff5db5e46e778f13ad5accdf98)int [FD\_ISSET](select_8h.md#ac38fe1ff5db5e46e778f13ad5accdf98)(int fd, [fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2) \*fdset);

[ 27](select_8h.md#a8c14b5b455292781fbcc2e34a47923d6)void [FD\_SET](select_8h.md#a8c14b5b455292781fbcc2e34a47923d6)(int fd, [fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2) \*fdset);

[ 28](select_8h.md#a3f88268fa19b2068723de10d848e8a42)void [FD\_ZERO](select_8h.md#a3f88268fa19b2068723de10d848e8a42)([fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2) \*fdset);

29

30#ifdef \_\_cplusplus

31}

32#endif

33

34#endif /\* ZEPHYR\_INCLUDE\_POSIX\_SYS\_SELECT\_H\_ \*/

[fdtable.h](fdtable_8h.md)

[posix\_types.h](posix__types_8h.md)

[FD\_CLR](select_8h.md#a0835759308c63ca23a1760980eea21d7)

void FD\_CLR(int fd, fd\_set \*fdset)

[pselect](select_8h.md#a2aed0a9b18a0ac6a3b8bb3ea9c3a34ab)

int pselect(int nfds, fd\_set \*readfds, fd\_set \*writefds, fd\_set \*exceptfds, const struct timespec \*timeout, const void \*sigmask)

[FD\_ZERO](select_8h.md#a3f88268fa19b2068723de10d848e8a42)

void FD\_ZERO(fd\_set \*fdset)

[select](select_8h.md#a7ffa34f8c9a12e7fd43f5ef65bf889fa)

int select(int nfds, fd\_set \*readfds, fd\_set \*writefds, fd\_set \*errorfds, struct timeval \*timeout)

[FD\_SET](select_8h.md#a8c14b5b455292781fbcc2e34a47923d6)

void FD\_SET(int fd, fd\_set \*fdset)

[FD\_ISSET](select_8h.md#ac38fe1ff5db5e46e778f13ad5accdf98)

int FD\_ISSET(int fd, fd\_set \*fdset)

[fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2)

struct zvfs\_fd\_set fd\_set

**Definition** select.h:18

[timespec](structtimespec.md)

**Definition** \_timespec.h:22

[timeval](structtimeval.md)

**Definition** \_timeval.h:22

[zvfs\_fd\_set](structzvfs__fd__set.md)

**Definition** fdtable.h:247

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [select.h](select_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
