---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/posix_2sys_2socket_8h_source.html
original_path: doxygen/html/posix_2sys_2socket_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socket.h

[Go to the documentation of this file.](posix_2sys_2socket_8h.md)

1/\*

2 \* Copyright (c) 2019 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_SYS\_SOCKET\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_SYS\_SOCKET\_H\_

8

9#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

10#include <[zephyr/net/socket.h](net_2socket_8h.md)>

11

[ 12](posix_2sys_2socket_8h.md#af1c8cf84ac37451afaef3bde9976b6e1)#define SHUT\_RD ZSOCK\_SHUT\_RD

[ 13](posix_2sys_2socket_8h.md#addb0a758e6fafdd89f5b7120f84738eb)#define SHUT\_WR ZSOCK\_SHUT\_WR

[ 14](posix_2sys_2socket_8h.md#a80c54d1399557c97a0c81a319d08e9db)#define SHUT\_RDWR ZSOCK\_SHUT\_RDWR

15

[ 16](posix_2sys_2socket_8h.md#a60c35b1016d0d87fe1066ea817acad98)#define MSG\_PEEK ZSOCK\_MSG\_PEEK

[ 17](posix_2sys_2socket_8h.md#a6a90f17f258e36353f09375263324f41)#define MSG\_TRUNC ZSOCK\_MSG\_TRUNC

[ 18](posix_2sys_2socket_8h.md#ab18d3d439e4a9c8d0f73e7166e8eb376)#define MSG\_DONTWAIT ZSOCK\_MSG\_DONTWAIT

[ 19](posix_2sys_2socket_8h.md#a0c0fac4635e91ca9d839e20a09d3989e)#define MSG\_WAITALL ZSOCK\_MSG\_WAITALL

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

[ 25](structlinger.md)struct [linger](structlinger.md) {

[ 26](structlinger.md#aa917aeadf061af6ed64aad87df3255fc) int [l\_onoff](structlinger.md#aa917aeadf061af6ed64aad87df3255fc);

[ 27](structlinger.md#a2b7d01c9a43f95d2ba6f6cf0ec68b412) int [l\_linger](structlinger.md#a2b7d01c9a43f95d2ba6f6cf0ec68b412);

28};

29

[ 30](posix_2sys_2socket_8h.md#a66e3de379c18201b21c889035ec54864)int [accept](group__bsd__sockets.md#ga33e6ea428ff537ed7a4763ce91b7d9bb)(int sock, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

[ 31](posix_2sys_2socket_8h.md#a05b4e957a092db3e68281988ceb32df8)int [bind](group__bsd__sockets.md#ga0de5e0b54a93dc6462078539b0a4a0b9)(int sock, const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

[ 32](posix_2sys_2socket_8h.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb)int [connect](group__bsd__sockets.md#gadfa930dd3c38f6c287d64e1680dbf386)(int sock, const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

[ 33](posix_2sys_2socket_8h.md#a5580f3aa0827aae89459c24b91f80cae)int [getpeername](group__bsd__sockets.md#ga03d89b6e64b4e734d892bcd498583682)(int sock, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

[ 34](posix_2sys_2socket_8h.md#abef44fb98f476ef2adba92bbdb362a1b)int [getsockname](group__bsd__sockets.md#gaa64d4aea83941c69d5405bd2f2de7a72)(int sock, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

[ 35](posix_2sys_2socket_8h.md#a2d33f1c2b99a5d0df682f54c3ccb2ffa)int [getsockopt](group__bsd__sockets.md#ga2ea64db46a2b23badc726616b2fb6c84)(int sock, int level, int optname, void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*optlen);

[ 36](posix_2sys_2socket_8h.md#a7005ffbeeff92be5394ff3244da79028)int [listen](group__bsd__sockets.md#ga36f501240a9428fe2ae63a9540c97adb)(int sock, int backlog);

[ 37](posix_2sys_2socket_8h.md#adee01662b0cf762a014efd87ab811276)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)(int sock, void \*buf, size\_t max\_len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

[ 38](posix_2sys_2socket_8h.md#a1c41b0d557d19b5031e668b1997dc73a)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [recvfrom](group__bsd__sockets.md#ga2aa207302b058bbb5b88533c752218a2)(int sock, void \*buf, size\_t max\_len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), struct [sockaddr](structsockaddr.md) \*src\_addr,

39 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

[ 40](posix_2sys_2socket_8h.md#ae074d22829eb79c596fd60d0f9f9611f)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [recvmsg](group__bsd__sockets.md#ga6145592f431b7ba7b4ae1869b22cb359)(int sock, struct [msghdr](structmsghdr.md) \*msg, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

[ 41](posix_2sys_2socket_8h.md#a16485de18b1ec93572e5d74b4a04e42f)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d)(int sock, const void \*buf, size\_t len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

[ 42](posix_2sys_2socket_8h.md#a8a2ad4261d3978ba299926f45d56ed74)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [sendmsg](group__bsd__sockets.md#ga1d7ee25c28352b2e7af55f75d721c4b8)(int sock, const struct [msghdr](structmsghdr.md) \*message, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

[ 43](posix_2sys_2socket_8h.md#ac223969ed767c313123d06547db45ff8)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [sendto](group__bsd__sockets.md#gacdc42cdbe2f9480ed58a2bdc2af57035)(int sock, const void \*buf, size\_t len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), const struct [sockaddr](structsockaddr.md) \*dest\_addr,

44 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

[ 45](posix_2sys_2socket_8h.md#a71c8788caef89a362e35ce5855e77077)int [setsockopt](group__bsd__sockets.md#ga9e476c4da1bb69b721e4aaa384114328)(int sock, int level, int optname, const void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) optlen);

[ 46](posix_2sys_2socket_8h.md#a8dadddc96fee56a9f8b0904aca02eab2)int [shutdown](group__bsd__sockets.md#gafe31a414f8777d15266fe84df7b66cbf)(int sock, int how);

[ 47](posix_2sys_2socket_8h.md#afcde75d283454d9d266b2ac6ebd867fe)int [sockatmark](posix_2sys_2socket_8h.md#afcde75d283454d9d266b2ac6ebd867fe)(int [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d));

[ 48](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a)int [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)(int family, int type, int proto);

[ 49](posix_2sys_2socket_8h.md#a56dcc24333a632cc8cdb8265151c0e7f)int [socketpair](group__bsd__sockets.md#gad8e31e081924ef65e482f355604009cb)(int family, int type, int proto, int sv[2]);

50

51#ifdef \_\_cplusplus

52}

53#endif

54

55#endif /\* ZEPHYR\_INCLUDE\_POSIX\_SYS\_SOCKET\_H\_ \*/

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)

static int socket(int family, int type, int proto)

POSIX wrapper for zsock\_socket.

**Definition** socket.h:867

[getpeername](group__bsd__sockets.md#ga03d89b6e64b4e734d892bcd498583682)

static int getpeername(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

POSIX wrapper for zsock\_getpeername.

**Definition** socket.h:976

[bind](group__bsd__sockets.md#ga0de5e0b54a93dc6462078539b0a4a0b9)

static int bind(int sock, const struct sockaddr \*addr, socklen\_t addrlen)

POSIX wrapper for zsock\_bind.

**Definition** socket.h:891

[sendmsg](group__bsd__sockets.md#ga1d7ee25c28352b2e7af55f75d721c4b8)

static ssize\_t sendmsg(int sock, const struct msghdr \*message, int flags)

POSIX wrapper for zsock\_sendmsg.

**Definition** socket.h:936

[recvfrom](group__bsd__sockets.md#ga2aa207302b058bbb5b88533c752218a2)

static ssize\_t recvfrom(int sock, void \*buf, size\_t max\_len, int flags, struct sockaddr \*src\_addr, socklen\_t \*addrlen)

POSIX wrapper for zsock\_recvfrom.

**Definition** socket.h:943

[getsockopt](group__bsd__sockets.md#ga2ea64db46a2b23badc726616b2fb6c84)

static int getsockopt(int sock, int level, int optname, void \*optval, socklen\_t \*optlen)

POSIX wrapper for zsock\_getsockopt.

**Definition** socket.h:962

[accept](group__bsd__sockets.md#ga33e6ea428ff537ed7a4763ce91b7d9bb)

static int accept(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

POSIX wrapper for zsock\_accept.

**Definition** socket.h:910

[listen](group__bsd__sockets.md#ga36f501240a9428fe2ae63a9540c97adb)

static int listen(int sock, int backlog)

POSIX wrapper for zsock\_listen.

**Definition** socket.h:904

[recvmsg](group__bsd__sockets.md#ga6145592f431b7ba7b4ae1869b22cb359)

static ssize\_t recvmsg(int sock, struct msghdr \*msg, int flags)

POSIX wrapper for zsock\_recvmsg.

**Definition** socket.h:950

[setsockopt](group__bsd__sockets.md#ga9e476c4da1bb69b721e4aaa384114328)

static int setsockopt(int sock, int level, int optname, const void \*optval, socklen\_t optlen)

POSIX wrapper for zsock\_setsockopt.

**Definition** socket.h:969

[getsockname](group__bsd__sockets.md#gaa64d4aea83941c69d5405bd2f2de7a72)

static int getsockname(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

POSIX wrapper for zsock\_getsockname.

**Definition** socket.h:983

[sendto](group__bsd__sockets.md#gacdc42cdbe2f9480ed58a2bdc2af57035)

static ssize\_t sendto(int sock, const void \*buf, size\_t len, int flags, const struct sockaddr \*dest\_addr, socklen\_t addrlen)

POSIX wrapper for zsock\_sendto.

**Definition** socket.h:928

[send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d)

static ssize\_t send(int sock, const void \*buf, size\_t len, int flags)

POSIX wrapper for zsock\_send.

**Definition** socket.h:916

[socketpair](group__bsd__sockets.md#gad8e31e081924ef65e482f355604009cb)

static int socketpair(int family, int type, int proto, int sv[2])

POSIX wrapper for zsock\_socketpair.

**Definition** socket.h:873

[connect](group__bsd__sockets.md#gadfa930dd3c38f6c287d64e1680dbf386)

static int connect(int sock, const struct sockaddr \*addr, socklen\_t addrlen)

POSIX wrapper for zsock\_connect.

**Definition** socket.h:897

[recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)

static ssize\_t recv(int sock, void \*buf, size\_t max\_len, int flags)

POSIX wrapper for zsock\_recv.

**Definition** socket.h:922

[shutdown](group__bsd__sockets.md#gafe31a414f8777d15266fe84df7b66cbf)

static int shutdown(int sock, int how)

POSIX wrapper for zsock\_shutdown.

**Definition** socket.h:885

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:168

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[sockatmark](posix_2sys_2socket_8h.md#afcde75d283454d9d266b2ac6ebd867fe)

int sockatmark(int s)

[linger](structlinger.md)

**Definition** socket.h:25

[linger::l\_linger](structlinger.md#a2b7d01c9a43f95d2ba6f6cf0ec68b412)

int l\_linger

**Definition** socket.h:27

[linger::l\_onoff](structlinger.md#aa917aeadf061af6ed64aad87df3255fc)

int l\_onoff

**Definition** socket.h:26

[msghdr](structmsghdr.md)

Message struct.

**Definition** net\_ip.h:247

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:385

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [socket.h](posix_2sys_2socket_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
