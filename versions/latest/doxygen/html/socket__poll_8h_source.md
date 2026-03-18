---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/socket__poll_8h_source.html
original_path: doxygen/html/socket__poll_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socket\_poll.h

[Go to the documentation of this file.](socket__poll_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_NET\_SOCKET\_POLL\_H\_

8#define ZEPHYR\_INCLUDE\_NET\_SOCKET\_POLL\_H\_

9

10/\* Setting for pollfd to avoid circular inclusion \*/

11

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

[ 28](structzsock__pollfd.md)struct [zsock\_pollfd](structzsock__pollfd.md) {

[ 29](structzsock__pollfd.md#a58fcd3f9af542bb15a936319aaf9c32e) int [fd](structzsock__pollfd.md#a58fcd3f9af542bb15a936319aaf9c32e);

[ 30](structzsock__pollfd.md#a31929c24c64b58c6f7e443645352f67d) short [events](structzsock__pollfd.md#a31929c24c64b58c6f7e443645352f67d);

[ 31](structzsock__pollfd.md#a98838f19b29e759a4b53db9b15349917) short [revents](structzsock__pollfd.md#a98838f19b29e759a4b53db9b15349917);

32};

33

34#ifdef \_\_cplusplus

35}

36#endif

37

41

42#endif /\* ZEPHYR\_INCLUDE\_NET\_SOCKET\_POLL\_H\_ \*/

[zsock\_pollfd](structzsock__pollfd.md)

Definition of the monitored socket/file descriptor.

**Definition** socket\_poll.h:28

[zsock\_pollfd::events](structzsock__pollfd.md#a31929c24c64b58c6f7e443645352f67d)

short events

Requested events.

**Definition** socket\_poll.h:30

[zsock\_pollfd::fd](structzsock__pollfd.md#a58fcd3f9af542bb15a936319aaf9c32e)

int fd

Socket descriptor.

**Definition** socket\_poll.h:29

[zsock\_pollfd::revents](structzsock__pollfd.md#a98838f19b29e759a4b53db9b15349917)

short revents

Returned events.

**Definition** socket\_poll.h:31

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socket\_poll.h](socket__poll_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
