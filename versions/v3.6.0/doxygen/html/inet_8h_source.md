---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/inet_8h_source.html
original_path: doxygen/html/inet_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

inet.h

[Go to the documentation of this file.](inet_8h.md)

1/\*

2 \* Copyright (c) 2019 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_ARPA\_INET\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_ARPA\_INET\_H\_

8

9#include <stddef.h>

10

11#include <[zephyr/posix/netinet/in.h](in_8h.md)>

12#include <[zephyr/posix/sys/socket.h](posix_2sys_2socket_8h.md)>

13

14#include <[zephyr/net/socket.h](net_2socket_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

20#ifndef CONFIG\_NET\_SOCKETS\_POSIX\_NAMES

21

22static inline char \*[inet\_ntop](group__bsd__sockets.md#gaebd26cfb6d976e64c3ce5594f1d4237b)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const void \*src, char \*dst,

23 size\_t size)

24{

25 return [zsock\_inet\_ntop](group__bsd__sockets.md#gae3092504b98d3b5f28675081a1e5b1ab)(family, src, dst, size);

26}

27

28static inline int [inet\_pton](group__bsd__sockets.md#ga2947410d1e58486907c3ddb8f280fab2)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const char \*src, void \*dst)

29{

30 return [zsock\_inet\_pton](group__bsd__sockets.md#gae4cf68b3752057b4b0818394487a2dbb)(family, src, dst);

31}

32

33#endif /\* CONFIG\_NET\_SOCKETS\_POSIX\_NAMES \*/

34

35#ifdef \_\_cplusplus

36}

37#endif

38

39#endif /\* ZEPHYR\_INCLUDE\_POSIX\_ARPA\_INET\_H\_ \*/

[inet\_pton](group__bsd__sockets.md#ga2947410d1e58486907c3ddb8f280fab2)

static int inet\_pton(sa\_family\_t family, const char \*src, void \*dst)

POSIX wrapper for zsock\_inet\_pton.

**Definition** socket.h:1026

[zsock\_inet\_ntop](group__bsd__sockets.md#gae3092504b98d3b5f28675081a1e5b1ab)

static char \* zsock\_inet\_ntop(sa\_family\_t family, const void \*src, char \*dst, size\_t size)

Convert network address from internal to numeric ASCII form.

**Definition** socket.h:690

[zsock\_inet\_pton](group__bsd__sockets.md#gae4cf68b3752057b4b0818394487a2dbb)

int zsock\_inet\_pton(sa\_family\_t family, const char \*src, void \*dst)

Convert network address from numeric ASCII form to internal representation.

[inet\_ntop](group__bsd__sockets.md#gaebd26cfb6d976e64c3ce5594f1d4237b)

static char \* inet\_ntop(sa\_family\_t family, const void \*src, char \*dst, size\_t size)

POSIX wrapper for zsock\_inet\_ntop.

**Definition** socket.h:1032

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:164

[in.h](in_8h.md)

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[socket.h](posix_2sys_2socket_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [arpa](dir_600f14fff2b86b8fd0090e7f273e0e80.md)
- [inet.h](inet_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
