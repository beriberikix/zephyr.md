---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/poll_8h_source.html
original_path: doxygen/html/poll_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

15#ifndef CONFIG\_NET\_SOCKETS\_POSIX\_NAMES

16

17#define pollfd zsock\_pollfd

18

19#define POLLIN ZSOCK\_POLLIN

20#define POLLOUT ZSOCK\_POLLOUT

21#define POLLERR ZSOCK\_POLLERR

22#define POLLHUP ZSOCK\_POLLHUP

23#define POLLNVAL ZSOCK\_POLLNVAL

24

25static inline int [poll](group__bsd__sockets.md#gae2d9b8390c125624595e2b400a08ea29)(struct [pollfd](group__bsd__sockets.md#gaf78a57e8ee17b7ecfe4510253d858afd) \*fds, int nfds, int timeout)

26{

27 return [zsock\_poll](group__bsd__sockets.md#gaa946975d9892a0ad730b6bf7090267cf)(fds, nfds, timeout);

28}

29

30#endif /\* CONFIG\_NET\_SOCKETS\_POSIX\_NAMES \*/

31

32#ifdef \_\_cplusplus

33}

34#endif

35

36#endif /\* ZEPHYR\_INCLUDE\_POSIX\_POLL\_H\_ \*/

[zsock\_poll](group__bsd__sockets.md#gaa946975d9892a0ad730b6bf7090267cf)

int zsock\_poll(struct zsock\_pollfd \*fds, int nfds, int timeout)

Efficiently poll multiple sockets for events.

[poll](group__bsd__sockets.md#gae2d9b8390c125624595e2b400a08ea29)

static int poll(struct zsock\_pollfd \*fds, int nfds, int timeout)

POSIX wrapper for zsock\_poll.

**Definition** socket.h:954

[pollfd](group__bsd__sockets.md#gaf78a57e8ee17b7ecfe4510253d858afd)

#define pollfd

POSIX wrapper for zsock\_pollfd.

**Definition** socket.h:830

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [poll.h](poll_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
