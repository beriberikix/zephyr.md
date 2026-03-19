---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structin6__pktinfo.html
original_path: doxygen/html/structin6__pktinfo.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

in6\_pktinfo Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [BSD Sockets compatible API](group__bsd__sockets.md)

Incoming IPv6 packet information.
[More...](#details)

`#include <[socket.h](net_2socket_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [in6\_addr](structin6__addr.md) | [ipi6\_addr](#a87b026872bd4ab42bc948a1951f0922b) |
|  | Destination IPv6 address. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [ipi6\_ifindex](#a9ce9353893fc69ca3c177826305e28e7) |
|  | Receive interface index. |

## Detailed Description

Incoming IPv6 packet information.

Used as ancillary data when calling [recvmsg()](posix_2sys_2socket_8h.md#ae074d22829eb79c596fd60d0f9f9611f) and IPV6\_RECVPKTINFO socket option is set.

## Field Documentation

## [◆ ](#a87b026872bd4ab42bc948a1951f0922b)ipi6\_addr

| struct [in6\_addr](structin6__addr.md) in6\_pktinfo::ipi6\_addr |
| --- |

Destination IPv6 address.

## [◆ ](#a9ce9353893fc69ca3c177826305e28e7)ipi6\_ifindex

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int in6\_pktinfo::ipi6\_ifindex |
| --- |

Receive interface index.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[socket.h](net_2socket_8h_source.md)

- [in6\_pktinfo](structin6__pktinfo.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
