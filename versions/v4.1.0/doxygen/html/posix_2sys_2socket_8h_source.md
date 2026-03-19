---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/posix_2sys_2socket_8h_source.html
original_path: doxygen/html/posix_2sys_2socket_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

[ 30](posix_2sys_2socket_8h.md#a66e3de379c18201b21c889035ec54864)int [accept](posix_2sys_2socket_8h.md#a66e3de379c18201b21c889035ec54864)(int sock, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

[ 31](posix_2sys_2socket_8h.md#a05b4e957a092db3e68281988ceb32df8)int [bind](posix_2sys_2socket_8h.md#a05b4e957a092db3e68281988ceb32df8)(int sock, const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

[ 32](posix_2sys_2socket_8h.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb)int [connect](posix_2sys_2socket_8h.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb)(int sock, const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

[ 33](posix_2sys_2socket_8h.md#a5580f3aa0827aae89459c24b91f80cae)int [getpeername](posix_2sys_2socket_8h.md#a5580f3aa0827aae89459c24b91f80cae)(int sock, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

[ 34](posix_2sys_2socket_8h.md#abef44fb98f476ef2adba92bbdb362a1b)int [getsockname](posix_2sys_2socket_8h.md#abef44fb98f476ef2adba92bbdb362a1b)(int sock, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

[ 35](posix_2sys_2socket_8h.md#a2d33f1c2b99a5d0df682f54c3ccb2ffa)int [getsockopt](posix_2sys_2socket_8h.md#a2d33f1c2b99a5d0df682f54c3ccb2ffa)(int sock, int level, int optname, void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*optlen);

[ 36](posix_2sys_2socket_8h.md#a7005ffbeeff92be5394ff3244da79028)int [listen](posix_2sys_2socket_8h.md#a7005ffbeeff92be5394ff3244da79028)(int sock, int backlog);

[ 37](posix_2sys_2socket_8h.md#adee01662b0cf762a014efd87ab811276)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [recv](posix_2sys_2socket_8h.md#adee01662b0cf762a014efd87ab811276)(int sock, void \*buf, size\_t max\_len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

[ 38](posix_2sys_2socket_8h.md#a1c41b0d557d19b5031e668b1997dc73a)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [recvfrom](posix_2sys_2socket_8h.md#a1c41b0d557d19b5031e668b1997dc73a)(int sock, void \*buf, size\_t max\_len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), struct [sockaddr](structsockaddr.md) \*src\_addr,

39 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

[ 40](posix_2sys_2socket_8h.md#ae074d22829eb79c596fd60d0f9f9611f)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [recvmsg](posix_2sys_2socket_8h.md#ae074d22829eb79c596fd60d0f9f9611f)(int sock, struct [msghdr](structmsghdr.md) \*msg, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

[ 41](posix_2sys_2socket_8h.md#a16485de18b1ec93572e5d74b4a04e42f)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [send](posix_2sys_2socket_8h.md#a16485de18b1ec93572e5d74b4a04e42f)(int sock, const void \*buf, size\_t len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

[ 42](posix_2sys_2socket_8h.md#a8a2ad4261d3978ba299926f45d56ed74)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [sendmsg](posix_2sys_2socket_8h.md#a8a2ad4261d3978ba299926f45d56ed74)(int sock, const struct [msghdr](structmsghdr.md) \*message, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

[ 43](posix_2sys_2socket_8h.md#ac223969ed767c313123d06547db45ff8)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [sendto](posix_2sys_2socket_8h.md#ac223969ed767c313123d06547db45ff8)(int sock, const void \*buf, size\_t len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), const struct [sockaddr](structsockaddr.md) \*dest\_addr,

44 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

[ 45](posix_2sys_2socket_8h.md#a71c8788caef89a362e35ce5855e77077)int [setsockopt](posix_2sys_2socket_8h.md#a71c8788caef89a362e35ce5855e77077)(int sock, int level, int optname, const void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) optlen);

[ 46](posix_2sys_2socket_8h.md#a8dadddc96fee56a9f8b0904aca02eab2)int [shutdown](posix_2sys_2socket_8h.md#a8dadddc96fee56a9f8b0904aca02eab2)(int sock, int how);

[ 47](posix_2sys_2socket_8h.md#afcde75d283454d9d266b2ac6ebd867fe)int [sockatmark](posix_2sys_2socket_8h.md#afcde75d283454d9d266b2ac6ebd867fe)(int [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d));

[ 48](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a)int [socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a)(int family, int type, int proto);

[ 49](posix_2sys_2socket_8h.md#a56dcc24333a632cc8cdb8265151c0e7f)int [socketpair](posix_2sys_2socket_8h.md#a56dcc24333a632cc8cdb8265151c0e7f)(int family, int type, int proto, int sv[2]);

50

51#ifdef \_\_cplusplus

52}

53#endif

54

55#endif /\* ZEPHYR\_INCLUDE\_POSIX\_SYS\_SOCKET\_H\_ \*/

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:172

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[bind](posix_2sys_2socket_8h.md#a05b4e957a092db3e68281988ceb32df8)

int bind(int sock, const struct sockaddr \*addr, socklen\_t addrlen)

[send](posix_2sys_2socket_8h.md#a16485de18b1ec93572e5d74b4a04e42f)

ssize\_t send(int sock, const void \*buf, size\_t len, int flags)

[recvfrom](posix_2sys_2socket_8h.md#a1c41b0d557d19b5031e668b1997dc73a)

ssize\_t recvfrom(int sock, void \*buf, size\_t max\_len, int flags, struct sockaddr \*src\_addr, socklen\_t \*addrlen)

[getsockopt](posix_2sys_2socket_8h.md#a2d33f1c2b99a5d0df682f54c3ccb2ffa)

int getsockopt(int sock, int level, int optname, void \*optval, socklen\_t \*optlen)

[socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a)

int socket(int family, int type, int proto)

[getpeername](posix_2sys_2socket_8h.md#a5580f3aa0827aae89459c24b91f80cae)

int getpeername(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

[socketpair](posix_2sys_2socket_8h.md#a56dcc24333a632cc8cdb8265151c0e7f)

int socketpair(int family, int type, int proto, int sv[2])

[accept](posix_2sys_2socket_8h.md#a66e3de379c18201b21c889035ec54864)

int accept(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

[listen](posix_2sys_2socket_8h.md#a7005ffbeeff92be5394ff3244da79028)

int listen(int sock, int backlog)

[setsockopt](posix_2sys_2socket_8h.md#a71c8788caef89a362e35ce5855e77077)

int setsockopt(int sock, int level, int optname, const void \*optval, socklen\_t optlen)

[sendmsg](posix_2sys_2socket_8h.md#a8a2ad4261d3978ba299926f45d56ed74)

ssize\_t sendmsg(int sock, const struct msghdr \*message, int flags)

[shutdown](posix_2sys_2socket_8h.md#a8dadddc96fee56a9f8b0904aca02eab2)

int shutdown(int sock, int how)

[connect](posix_2sys_2socket_8h.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb)

int connect(int sock, const struct sockaddr \*addr, socklen\_t addrlen)

[getsockname](posix_2sys_2socket_8h.md#abef44fb98f476ef2adba92bbdb362a1b)

int getsockname(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

[sendto](posix_2sys_2socket_8h.md#ac223969ed767c313123d06547db45ff8)

ssize\_t sendto(int sock, const void \*buf, size\_t len, int flags, const struct sockaddr \*dest\_addr, socklen\_t addrlen)

[recv](posix_2sys_2socket_8h.md#adee01662b0cf762a014efd87ab811276)

ssize\_t recv(int sock, void \*buf, size\_t max\_len, int flags)

[recvmsg](posix_2sys_2socket_8h.md#ae074d22829eb79c596fd60d0f9f9611f)

ssize\_t recvmsg(int sock, struct msghdr \*msg, int flags)

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

**Definition** net\_ip.h:257

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:408

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [socket.h](posix_2sys_2socket_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
