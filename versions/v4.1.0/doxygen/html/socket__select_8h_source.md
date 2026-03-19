---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/socket__select_8h_source.html
original_path: doxygen/html/socket__select_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socket\_select.h

[Go to the documentation of this file.](socket__select_8h.md)

1/\*

2 \* Copyright (c) 2019 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_SOCKET\_SELECT\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_SOCKET\_SELECT\_H\_

14

21

22#include <time.h>

23

24#include <[zephyr/toolchain.h](toolchain_8h.md)>

25#include <[zephyr/net/socket\_types.h](socket__types_8h.md)>

26#include <[zephyr/sys/fdtable.h](fdtable_8h.md)>

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

[ 33](group__bsd__sockets.md#ga1cdeeddce9000b9fd29b638c422f48f8)typedef struct [zvfs\_fd\_set](structzvfs__fd__set.md) [zsock\_fd\_set](group__bsd__sockets.md#ga1cdeeddce9000b9fd29b638c422f48f8);

34

[ 49](group__bsd__sockets.md#ga1a065da89061bcb10b10663a9ffbdd10)static inline int [zsock\_select](group__bsd__sockets.md#ga1a065da89061bcb10b10663a9ffbdd10)(int nfds, [zsock\_fd\_set](group__bsd__sockets.md#ga1cdeeddce9000b9fd29b638c422f48f8) \*readfds, [zsock\_fd\_set](group__bsd__sockets.md#ga1cdeeddce9000b9fd29b638c422f48f8) \*writefds,

50 [zsock\_fd\_set](group__bsd__sockets.md#ga1cdeeddce9000b9fd29b638c422f48f8) \*exceptfds, struct zsock\_timeval \*timeout)

51{

52 struct [timespec](structtimespec.md) to = {

53 .tv\_sec = (timeout == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) ? 0 : timeout->tv\_sec,

54 .tv\_nsec = (long)((timeout == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) ? 0 : timeout->tv\_usec \* [NSEC\_PER\_USEC](group__clock__apis.md#ga2180f263d149841a7c1fde663edb84c5))};

55

56 return [zvfs\_select](fdtable_8h.md#a8ced1fc0adbdf35b71ec486a8ec68665)(nfds, readfds, writefds, exceptfds, (timeout == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) ? [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) : &to,

57 [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

58}

59

[ 61](group__bsd__sockets.md#ga5c88da69b8d9401d3ae02495056f7e23)#define ZSOCK\_FD\_SETSIZE ZVFS\_FD\_SETSIZE

62

[ 73](group__bsd__sockets.md#gaa4855f07c1329a150f371044e4384490)static inline void [ZSOCK\_FD\_ZERO](group__bsd__sockets.md#gaa4855f07c1329a150f371044e4384490)([zsock\_fd\_set](group__bsd__sockets.md#ga1cdeeddce9000b9fd29b638c422f48f8) \*set)

74{

75 [ZVFS\_FD\_ZERO](fdtable_8h.md#a46ae4a3ac3d192de02fb1b6c4a4e95ac)(set);

76}

77

[ 88](group__bsd__sockets.md#gab92b08adccc22a85e7a1c06bf11a88bc)static inline int [ZSOCK\_FD\_ISSET](group__bsd__sockets.md#gab92b08adccc22a85e7a1c06bf11a88bc)(int fd, [zsock\_fd\_set](group__bsd__sockets.md#ga1cdeeddce9000b9fd29b638c422f48f8) \*set)

89{

90 return [ZVFS\_FD\_ISSET](fdtable_8h.md#a84f63f19ea89e5711725f4d753b5484c)(fd, set);

91}

92

[ 103](group__bsd__sockets.md#ga7023ec00d24af41a7cbf5f376fb44487)static inline void [ZSOCK\_FD\_CLR](group__bsd__sockets.md#ga7023ec00d24af41a7cbf5f376fb44487)(int fd, [zsock\_fd\_set](group__bsd__sockets.md#ga1cdeeddce9000b9fd29b638c422f48f8) \*set)

104{

105 [ZVFS\_FD\_CLR](fdtable_8h.md#a029809dfde96846d9e7871e252d74546)(fd, set);

106}

107

[ 118](group__bsd__sockets.md#ga5d07f52910f6d881295ec659716767f1)static inline void [ZSOCK\_FD\_SET](group__bsd__sockets.md#ga5d07f52910f6d881295ec659716767f1)(int fd, [zsock\_fd\_set](group__bsd__sockets.md#ga1cdeeddce9000b9fd29b638c422f48f8) \*set)

119{

120 [ZVFS\_FD\_SET](fdtable_8h.md#afa48d92e5f545412139f567a19e01f71)(fd, set);

121}

122

123#ifdef \_\_cplusplus

124}

125#endif

126

130

131#endif /\* ZEPHYR\_INCLUDE\_NET\_SOCKET\_SELECT\_H\_ \*/

[fdtable.h](fdtable_8h.md)

[ZVFS\_FD\_CLR](fdtable_8h.md#a029809dfde96846d9e7871e252d74546)

void ZVFS\_FD\_CLR(int fd, struct zvfs\_fd\_set \*fdset)

[ZVFS\_FD\_ZERO](fdtable_8h.md#a46ae4a3ac3d192de02fb1b6c4a4e95ac)

void ZVFS\_FD\_ZERO(struct zvfs\_fd\_set \*fdset)

[ZVFS\_FD\_ISSET](fdtable_8h.md#a84f63f19ea89e5711725f4d753b5484c)

int ZVFS\_FD\_ISSET(int fd, struct zvfs\_fd\_set \*fdset)

[zvfs\_select](fdtable_8h.md#a8ced1fc0adbdf35b71ec486a8ec68665)

int zvfs\_select(int nfds, struct zvfs\_fd\_set \*ZRESTRICT readfds, struct zvfs\_fd\_set \*ZRESTRICT writefds, struct zvfs\_fd\_set \*ZRESTRICT errorfds, const struct timespec \*ZRESTRICT timeout, const void \*ZRESTRICT sigmask)

[ZVFS\_FD\_SET](fdtable_8h.md#afa48d92e5f545412139f567a19e01f71)

void ZVFS\_FD\_SET(int fd, struct zvfs\_fd\_set \*fdset)

[zsock\_select](group__bsd__sockets.md#ga1a065da89061bcb10b10663a9ffbdd10)

static int zsock\_select(int nfds, zsock\_fd\_set \*readfds, zsock\_fd\_set \*writefds, zsock\_fd\_set \*exceptfds, struct zsock\_timeval \*timeout)

Legacy function to poll multiple sockets for events.

**Definition** socket\_select.h:49

[zsock\_fd\_set](group__bsd__sockets.md#ga1cdeeddce9000b9fd29b638c422f48f8)

struct zvfs\_fd\_set zsock\_fd\_set

Socket file descriptor set.

**Definition** socket\_select.h:33

[ZSOCK\_FD\_SET](group__bsd__sockets.md#ga5d07f52910f6d881295ec659716767f1)

static void ZSOCK\_FD\_SET(int fd, zsock\_fd\_set \*set)

Add socket to fd\_set.

**Definition** socket\_select.h:118

[ZSOCK\_FD\_CLR](group__bsd__sockets.md#ga7023ec00d24af41a7cbf5f376fb44487)

static void ZSOCK\_FD\_CLR(int fd, zsock\_fd\_set \*set)

Remove socket from fd\_set.

**Definition** socket\_select.h:103

[ZSOCK\_FD\_ZERO](group__bsd__sockets.md#gaa4855f07c1329a150f371044e4384490)

static void ZSOCK\_FD\_ZERO(zsock\_fd\_set \*set)

Initialize (clear) fd\_set.

**Definition** socket\_select.h:73

[ZSOCK\_FD\_ISSET](group__bsd__sockets.md#gab92b08adccc22a85e7a1c06bf11a88bc)

static int ZSOCK\_FD\_ISSET(int fd, zsock\_fd\_set \*set)

Check whether socket is a member of fd\_set.

**Definition** socket\_select.h:88

[NSEC\_PER\_USEC](group__clock__apis.md#ga2180f263d149841a7c1fde663edb84c5)

#define NSEC\_PER\_USEC

number of nanoseconds per microsecond

**Definition** sys\_clock.h:83

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[socket\_types.h](socket__types_8h.md)

socket types definitionis

[timespec](structtimespec.md)

**Definition** \_timespec.h:22

[zvfs\_fd\_set](structzvfs__fd__set.md)

**Definition** fdtable.h:247

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socket\_select.h](socket__select_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
