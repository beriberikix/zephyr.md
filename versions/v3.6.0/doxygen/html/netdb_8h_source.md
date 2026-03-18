---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/netdb_8h_source.html
original_path: doxygen/html/netdb_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

netdb.h

[Go to the documentation of this file.](netdb_8h.md)

1/\*

2 \* Copyright (c) 2019 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_NETDB\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_NETDB\_H\_

8

9#include <[zephyr/net/socket.h](net_2socket_8h.md)>

10

11#ifndef NI\_MAXSERV

[ 13](netdb_8h.md#aefdeadf85356cc2fa0870d86a6055eb1)#define NI\_MAXSERV 32

14#endif

15

[ 16](netdb_8h.md#a3f3b38f2ac6688612a0fd20f3e6210be)#define EAI\_BADFLAGS DNS\_EAI\_BADFLAGS

[ 17](netdb_8h.md#a0bb00f48d6ba1e8c55b7d85c8e3a19a7)#define EAI\_NONAME DNS\_EAI\_NONAME

[ 18](netdb_8h.md#a7a0f2f10f8778fe201a68932d18434e5)#define EAI\_AGAIN DNS\_EAI\_AGAIN

[ 19](netdb_8h.md#acfc712115bf29357d33472da2209dc15)#define EAI\_FAIL DNS\_EAI\_FAIL

[ 20](netdb_8h.md#aae1a32f26ffbb7461251d7c4a7c3a0a2)#define EAI\_NODATA DNS\_EAI\_NODATA

[ 21](netdb_8h.md#a33d8eb0c89167f95dcdaf23386631174)#define EAI\_MEMORY DNS\_EAI\_MEMORY

[ 22](netdb_8h.md#a8e864fa95f26341c27127deb6237c88c)#define EAI\_SYSTEM DNS\_EAI\_SYSTEM

[ 23](netdb_8h.md#ac7f08e3ee3c38f7c869beb5a44c9f651)#define EAI\_SERVICE DNS\_EAI\_SERVICE

[ 24](netdb_8h.md#a110777c2c99dab32101324b3b1dd1df5)#define EAI\_SOCKTYPE DNS\_EAI\_SOCKTYPE

[ 25](netdb_8h.md#a1d195add54c14a8903441848fb2f7da6)#define EAI\_FAMILY DNS\_EAI\_FAMILY

[ 26](netdb_8h.md#a01d6798d308152b919a0b9f998bbd336)#define EAI\_OVERFLOW DNS\_EAI\_OVERFLOW

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

32#ifndef CONFIG\_NET\_SOCKETS\_POSIX\_NAMES

33

34#define addrinfo zsock\_addrinfo

35

36static inline int [getaddrinfo](group__bsd__sockets.md#ga08be4218900930dcc3add7e03173a83c)(const char \*host, const char \*service,

37 const struct [zsock\_addrinfo](structzsock__addrinfo.md) \*hints,

38 struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\*res)

39{

40 return [zsock\_getaddrinfo](group__bsd__sockets.md#gaf59c97c9bd07f188e3f06b2372ac1856)(host, service, hints, res);

41}

42

43static inline void [freeaddrinfo](group__bsd__sockets.md#gaf70cde067b55e04adff98d672fa41c94)(struct [zsock\_addrinfo](structzsock__addrinfo.md) \*ai)

44{

45 [zsock\_freeaddrinfo](group__bsd__sockets.md#ga7953da2e52bcfad51b877de6d7fd6cc9)(ai);

46}

47

48static inline const char \*[gai\_strerror](group__bsd__sockets.md#gab388347be08b4e7d1d9f3ea6f956cd41)(int errcode)

49{

50 return [zsock\_gai\_strerror](group__bsd__sockets.md#gaa9d9e97c347b3854dc73d7ba33d8ca4b)(errcode);

51}

52

53static inline int [getnameinfo](group__bsd__sockets.md#ga6c9b3f03fde427c355b26ad9d6054250)(const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

54 char \*host, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) hostlen,

55 char \*serv, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) servlen, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

56{

57 return [zsock\_getnameinfo](group__bsd__sockets.md#gae9375bc6a1e945e5486f40c0198e3505)(addr, addrlen, host, hostlen,

58 serv, servlen, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

59}

60

61#endif /\* CONFIG\_NET\_SOCKETS\_POSIX\_NAMES \*/

62

63#ifdef \_\_cplusplus

64}

65#endif

66

67#endif /\* ZEPHYR\_INCLUDE\_POSIX\_NETDB\_H\_ \*/

[getaddrinfo](group__bsd__sockets.md#ga08be4218900930dcc3add7e03173a83c)

static int getaddrinfo(const char \*host, const char \*service, const struct zsock\_addrinfo \*hints, struct zsock\_addrinfo \*\*res)

POSIX wrapper for zsock\_getaddrinfo.

**Definition** socket.h:988

[getnameinfo](group__bsd__sockets.md#ga6c9b3f03fde427c355b26ad9d6054250)

static int getnameinfo(const struct sockaddr \*addr, socklen\_t addrlen, char \*host, socklen\_t hostlen, char \*serv, socklen\_t servlen, int flags)

POSIX wrapper for zsock\_getnameinfo.

**Definition** socket.h:1008

[zsock\_freeaddrinfo](group__bsd__sockets.md#ga7953da2e52bcfad51b877de6d7fd6cc9)

void zsock\_freeaddrinfo(struct zsock\_addrinfo \*ai)

Free results returned by zsock\_getaddrinfo().

[zsock\_gai\_strerror](group__bsd__sockets.md#gaa9d9e97c347b3854dc73d7ba33d8ca4b)

const char \* zsock\_gai\_strerror(int errcode)

Convert zsock\_getaddrinfo() error code to textual message.

[gai\_strerror](group__bsd__sockets.md#gab388347be08b4e7d1d9f3ea6f956cd41)

static const char \* gai\_strerror(int errcode)

POSIX wrapper for zsock\_gai\_strerror.

**Definition** socket.h:1002

[zsock\_getnameinfo](group__bsd__sockets.md#gae9375bc6a1e945e5486f40c0198e3505)

int zsock\_getnameinfo(const struct sockaddr \*addr, socklen\_t addrlen, char \*host, socklen\_t hostlen, char \*serv, socklen\_t servlen, int flags)

Resolve a network address to a domain name or ASCII address.

[zsock\_getaddrinfo](group__bsd__sockets.md#gaf59c97c9bd07f188e3f06b2372ac1856)

int zsock\_getaddrinfo(const char \*host, const char \*service, const struct zsock\_addrinfo \*hints, struct zsock\_addrinfo \*\*res)

Resolve a domain name to one or more network addresses.

[freeaddrinfo](group__bsd__sockets.md#gaf70cde067b55e04adff98d672fa41c94)

static void freeaddrinfo(struct zsock\_addrinfo \*ai)

POSIX wrapper for zsock\_freeaddrinfo.

**Definition** socket.h:996

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:168

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:347

[zsock\_addrinfo](structzsock__addrinfo.md)

Definition used when querying address information.

**Definition** socket.h:280

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [netdb.h](netdb_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
