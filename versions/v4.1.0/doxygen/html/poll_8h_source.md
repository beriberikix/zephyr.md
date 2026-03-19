---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/poll_8h_source.html
original_path: doxygen/html/poll_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

poll.h

[Go to the documentation of this file.](poll_8h.md)

1/\*

2 \* Copyright (c) 2019 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_POLL\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_POLL\_H\_

8

9#include <[zephyr/net/socket.h](net_2socket_8h.md)>

10

11#ifdef \_\_cplusplus

12extern "C" {

13#endif

14

[ 15](poll_8h.md#aa49b6bf041fda66eda01c0170243c271)typedef unsigned int [nfds\_t](poll_8h.md#aa49b6bf041fda66eda01c0170243c271);

16

[ 17](poll_8h.md#af78a57e8ee17b7ecfe4510253d858afd)#define pollfd zsock\_pollfd

18

[ 19](poll_8h.md#a52ac479a805051f59643588b096024ff)#define POLLIN ZSOCK\_POLLIN

[ 20](poll_8h.md#ab6f53b89c7a4cc5e8349f7c778d85168)#define POLLPRI ZSOCK\_POLLPRI

[ 21](poll_8h.md#a91b3c67129ac7675062f316b840a0d58)#define POLLOUT ZSOCK\_POLLOUT

[ 22](poll_8h.md#ab1c532446408c98559d4aaaeeeb99820)#define POLLERR ZSOCK\_POLLERR

[ 23](poll_8h.md#a262754fe6bdf27c2cd3da43284ec8536)#define POLLHUP ZSOCK\_POLLHUP

[ 24](poll_8h.md#ae8bffe35c61e12fb7b408b89721896df)#define POLLNVAL ZSOCK\_POLLNVAL

25

[ 26](poll_8h.md#afa7e83ddea0ab5b08fcf614b89ac48ba)int [poll](poll_8h.md#afa7e83ddea0ab5b08fcf614b89ac48ba)(struct [pollfd](poll_8h.md#af78a57e8ee17b7ecfe4510253d858afd) \*fds, int nfds, int timeout);

27

28#ifdef \_\_cplusplus

29}

30#endif

31

32#endif /\* ZEPHYR\_INCLUDE\_POSIX\_POLL\_H\_ \*/

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[nfds\_t](poll_8h.md#aa49b6bf041fda66eda01c0170243c271)

unsigned int nfds\_t

**Definition** poll.h:15

[pollfd](poll_8h.md#af78a57e8ee17b7ecfe4510253d858afd)

#define pollfd

**Definition** poll.h:17

[poll](poll_8h.md#afa7e83ddea0ab5b08fcf614b89ac48ba)

int poll(struct zsock\_pollfd \*fds, int nfds, int timeout)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [poll.h](poll_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
