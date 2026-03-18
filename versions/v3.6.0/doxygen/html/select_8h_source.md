---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/select_8h_source.html
original_path: doxygen/html/select_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

16#ifndef CONFIG\_NET\_SOCKETS\_POSIX\_NAMES

17

18#define fd\_set zsock\_fd\_set

19#define FD\_SETSIZE ZSOCK\_FD\_SETSIZE

20#define FD\_ZERO ZSOCK\_FD\_ZERO

21#define FD\_SET ZSOCK\_FD\_SET

22#define FD\_CLR ZSOCK\_FD\_CLR

23#define FD\_ISSET ZSOCK\_FD\_ISSET

24

25struct [timeval](structtimeval.md);

26

27static inline int [select](group__bsd__sockets.md#gaeaf2734d19e74439d9db54896b399c87)(int nfds, [fd\_set](group__bsd__sockets.md#ga7acea921b59df1dc48b89b21ecfa446b) \*readfds,

28 [fd\_set](group__bsd__sockets.md#ga7acea921b59df1dc48b89b21ecfa446b) \*writefds, [fd\_set](group__bsd__sockets.md#ga7acea921b59df1dc48b89b21ecfa446b) \*exceptfds,

29 struct [timeval](structtimeval.md) \*timeout)

30{

31 return [zsock\_select](group__bsd__sockets.md#ga265b8fc197a7a79102bdce4875bbb045)(nfds, readfds, writefds, exceptfds,

32 (struct [zsock\_timeval](group__bsd__sockets.md#ga0fa9dd4796261813b164fed42303e4ee) \*)timeout);

33}

34

35#endif /\* CONFIG\_NET\_SOCKETS\_POSIX\_NAMES \*/

36

37#ifdef \_\_cplusplus

38}

39#endif

40

41#endif /\* ZEPHYR\_INCLUDE\_POSIX\_SYS\_SELECT\_H\_ \*/

[zsock\_timeval](group__bsd__sockets.md#ga0fa9dd4796261813b164fed42303e4ee)

#define zsock\_timeval

**Definition** socket\_types.h:49

[zsock\_select](group__bsd__sockets.md#ga265b8fc197a7a79102bdce4875bbb045)

int zsock\_select(int nfds, zsock\_fd\_set \*readfds, zsock\_fd\_set \*writefds, zsock\_fd\_set \*exceptfds, struct zsock\_timeval \*timeout)

Legacy function to poll multiple sockets for events.

[fd\_set](group__bsd__sockets.md#ga7acea921b59df1dc48b89b21ecfa446b)

#define fd\_set

**Definition** socket\_select.h:111

[select](group__bsd__sockets.md#gaeaf2734d19e74439d9db54896b399c87)

static int select(int nfds, zsock\_fd\_set \*readfds, zsock\_fd\_set \*writefds, zsock\_fd\_set \*exceptfds, struct timeval \*timeout)

**Definition** socket\_select.h:114

[socket\_select.h](socket__select_8h.md)

[socket\_types.h](socket__types_8h.md)

[timeval](structtimeval.md)

**Definition** \_timeval.h:22

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [select.h](select_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
