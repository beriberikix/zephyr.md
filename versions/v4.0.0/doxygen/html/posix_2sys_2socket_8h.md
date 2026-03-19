---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/posix_2sys_2socket_8h.html
original_path: doxygen/html/posix_2sys_2socket_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socket.h File Reference

`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/net/socket.h](net_2socket_8h_source.md)>`

[Go to the source code of this file.](posix_2sys_2socket_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [linger](structlinger.md) |

| Macros | |
| --- | --- |
| #define | [SHUT\_RD](#af1c8cf84ac37451afaef3bde9976b6e1)   [ZSOCK\_SHUT\_RD](group__bsd__sockets.md#ga2a58cbc62db1e559898ea979454d74d4) |
| #define | [SHUT\_WR](#addb0a758e6fafdd89f5b7120f84738eb)   [ZSOCK\_SHUT\_WR](group__bsd__sockets.md#ga87630f1abe81c4e33a24cb1f1ebb3571) |
| #define | [SHUT\_RDWR](#a80c54d1399557c97a0c81a319d08e9db)   [ZSOCK\_SHUT\_RDWR](group__bsd__sockets.md#ga788dcff81663a9fb01e32b53bca13e2d) |
| #define | [MSG\_PEEK](#a60c35b1016d0d87fe1066ea817acad98)   [ZSOCK\_MSG\_PEEK](group__bsd__sockets.md#gae7da123a40584192b65af77e918080b9) |
| #define | [MSG\_TRUNC](#a6a90f17f258e36353f09375263324f41)   [ZSOCK\_MSG\_TRUNC](group__bsd__sockets.md#gae594c5e74cd473df8e3328a4cd935ce1) |
| #define | [MSG\_DONTWAIT](#ab18d3d439e4a9c8d0f73e7166e8eb376)   [ZSOCK\_MSG\_DONTWAIT](group__bsd__sockets.md#ga92cf4460e23f376bf130d885ea64ed6b) |
| #define | [MSG\_WAITALL](#a0c0fac4635e91ca9d839e20a09d3989e)   [ZSOCK\_MSG\_WAITALL](group__bsd__sockets.md#ga00b950f50302d97c27111da49f5289fb) |

| Functions | |
| --- | --- |
| int | [accept](#a66e3de379c18201b21c889035ec54864) (int sock, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen) |
| int | [bind](#a05b4e957a092db3e68281988ceb32df8) (int sock, const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen) |
| int | [connect](#a90f0aa598d0f4ab4ea99ecf289a6a7fb) (int sock, const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen) |
| int | [getpeername](#a5580f3aa0827aae89459c24b91f80cae) (int sock, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen) |
| int | [getsockname](#abef44fb98f476ef2adba92bbdb362a1b) (int sock, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen) |
| int | [getsockopt](#a2d33f1c2b99a5d0df682f54c3ccb2ffa) (int sock, int level, int optname, void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*optlen) |
| int | [listen](#a7005ffbeeff92be5394ff3244da79028) (int sock, int backlog) |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [recv](#adee01662b0cf762a014efd87ab811276) (int sock, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) max\_len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [recvfrom](#a1c41b0d557d19b5031e668b1997dc73a) (int sock, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) max\_len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), struct [sockaddr](structsockaddr.md) \*src\_addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen) |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [recvmsg](#ae074d22829eb79c596fd60d0f9f9611f) (int sock, struct [msghdr](structmsghdr.md) \*msg, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [send](#a16485de18b1ec93572e5d74b4a04e42f) (int sock, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [sendmsg](#a8a2ad4261d3978ba299926f45d56ed74) (int sock, const struct [msghdr](structmsghdr.md) \*message, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [sendto](#ac223969ed767c313123d06547db45ff8) (int sock, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), const struct [sockaddr](structsockaddr.md) \*dest\_addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen) |
| int | [setsockopt](#a71c8788caef89a362e35ce5855e77077) (int sock, int level, int optname, const void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) optlen) |
| int | [shutdown](#a8dadddc96fee56a9f8b0904aca02eab2) (int sock, int how) |
| int | [sockatmark](#afcde75d283454d9d266b2ac6ebd867fe) (int [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
| int | [socket](#a4dcc080bfb18d95d173bc205084f8b0a) (int family, int type, int proto) |
| int | [socketpair](#a56dcc24333a632cc8cdb8265151c0e7f) (int family, int type, int proto, int sv[2]) |

## Macro Definition Documentation

## [◆ ](#ab18d3d439e4a9c8d0f73e7166e8eb376)MSG\_DONTWAIT

| #define MSG\_DONTWAIT   [ZSOCK\_MSG\_DONTWAIT](group__bsd__sockets.md#ga92cf4460e23f376bf130d885ea64ed6b) |
| --- |

## [◆ ](#a60c35b1016d0d87fe1066ea817acad98)MSG\_PEEK

| #define MSG\_PEEK   [ZSOCK\_MSG\_PEEK](group__bsd__sockets.md#gae7da123a40584192b65af77e918080b9) |
| --- |

## [◆ ](#a6a90f17f258e36353f09375263324f41)MSG\_TRUNC

| #define MSG\_TRUNC   [ZSOCK\_MSG\_TRUNC](group__bsd__sockets.md#gae594c5e74cd473df8e3328a4cd935ce1) |
| --- |

## [◆ ](#a0c0fac4635e91ca9d839e20a09d3989e)MSG\_WAITALL

| #define MSG\_WAITALL   [ZSOCK\_MSG\_WAITALL](group__bsd__sockets.md#ga00b950f50302d97c27111da49f5289fb) |
| --- |

## [◆ ](#af1c8cf84ac37451afaef3bde9976b6e1)SHUT\_RD

| #define SHUT\_RD   [ZSOCK\_SHUT\_RD](group__bsd__sockets.md#ga2a58cbc62db1e559898ea979454d74d4) |
| --- |

## [◆ ](#a80c54d1399557c97a0c81a319d08e9db)SHUT\_RDWR

| #define SHUT\_RDWR   [ZSOCK\_SHUT\_RDWR](group__bsd__sockets.md#ga788dcff81663a9fb01e32b53bca13e2d) |
| --- |

## [◆ ](#addb0a758e6fafdd89f5b7120f84738eb)SHUT\_WR

| #define SHUT\_WR   [ZSOCK\_SHUT\_WR](group__bsd__sockets.md#ga87630f1abe81c4e33a24cb1f1ebb3571) |
| --- |

## Function Documentation

## [◆ ](#a66e3de379c18201b21c889035ec54864)accept()

| int accept | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \* | *addrlen* ) |

## [◆ ](#a05b4e957a092db3e68281988ceb32df8)bind()

| int bind | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *addrlen* ) |

## [◆ ](#a90f0aa598d0f4ab4ea99ecf289a6a7fb)connect()

| int connect | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *addrlen* ) |

## [◆ ](#a5580f3aa0827aae89459c24b91f80cae)getpeername()

| int getpeername | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \* | *addrlen* ) |

## [◆ ](#abef44fb98f476ef2adba92bbdb362a1b)getsockname()

| int getsockname | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \* | *addrlen* ) |

## [◆ ](#a2d33f1c2b99a5d0df682f54c3ccb2ffa)getsockopt()

| int getsockopt | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | int | *level*, |
|  |  | int | *optname*, |
|  |  | void \* | *optval*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \* | *optlen* ) |

## [◆ ](#a7005ffbeeff92be5394ff3244da79028)listen()

| int listen | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | int | *backlog* ) |

## [◆ ](#adee01662b0cf762a014efd87ab811276)recv()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) recv | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *max\_len*, |
|  |  | int | *flags* ) |

## [◆ ](#a1c41b0d557d19b5031e668b1997dc73a)recvfrom()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) recvfrom | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *max\_len*, |
|  |  | int | *flags*, |
|  |  | struct [sockaddr](structsockaddr.md) \* | *src\_addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \* | *addrlen* ) |

## [◆ ](#ae074d22829eb79c596fd60d0f9f9611f)recvmsg()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) recvmsg | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | struct [msghdr](structmsghdr.md) \* | *msg*, |
|  |  | int | *flags* ) |

## [◆ ](#a16485de18b1ec93572e5d74b4a04e42f)send()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) send | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | const void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | int | *flags* ) |

## [◆ ](#a8a2ad4261d3978ba299926f45d56ed74)sendmsg()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) sendmsg | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | const struct [msghdr](structmsghdr.md) \* | *message*, |
|  |  | int | *flags* ) |

## [◆ ](#ac223969ed767c313123d06547db45ff8)sendto()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) sendto | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | const void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | int | *flags*, |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *dest\_addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *addrlen* ) |

## [◆ ](#a71c8788caef89a362e35ce5855e77077)setsockopt()

| int setsockopt | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | int | *level*, |
|  |  | int | *optname*, |
|  |  | const void \* | *optval*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *optlen* ) |

## [◆ ](#a8dadddc96fee56a9f8b0904aca02eab2)shutdown()

| int shutdown | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | int | *how* ) |

## [◆ ](#afcde75d283454d9d266b2ac6ebd867fe)sockatmark()

| int sockatmark | ( | int | *s* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a4dcc080bfb18d95d173bc205084f8b0a)socket()

| int socket | ( | int | *family*, |
| --- | --- | --- | --- |
|  |  | int | *type*, |
|  |  | int | *proto* ) |

## [◆ ](#a56dcc24333a632cc8cdb8265151c0e7f)socketpair()

| int socketpair | ( | int | *family*, |
| --- | --- | --- | --- |
|  |  | int | *type*, |
|  |  | int | *proto*, |
|  |  | int | *sv*[2] ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [socket.h](posix_2sys_2socket_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
