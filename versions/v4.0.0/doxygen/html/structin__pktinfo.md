---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structin__pktinfo.html
original_path: doxygen/html/structin__pktinfo.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

in\_pktinfo Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [BSD Sockets compatible API](group__bsd__sockets.md)

Incoming IPv4 packet information.
[More...](#details)

`#include <[socket.h](net_2socket_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [ipi\_ifindex](#a0688c86ded281fd5c2fe93a03f7f6c7d) |
|  | Network interface index. |
| struct [in\_addr](structin__addr.md) | [ipi\_spec\_dst](#a3ed6e057196d3d34d043631453df83c1) |
|  | Local address. |
| struct [in\_addr](structin__addr.md) | [ipi\_addr](#a51f86ad8ba1e3c209fb6c8d9572b08c6) |
|  | Header Destination address. |

## Detailed Description

Incoming IPv4 packet information.

Used as ancillary data when calling [recvmsg()](group__bsd__sockets.md#ga6145592f431b7ba7b4ae1869b22cb359 "POSIX wrapper for zsock_recvmsg.") and IP\_PKTINFO socket option is set.

## Field Documentation

## [◆ ](#a51f86ad8ba1e3c209fb6c8d9572b08c6)ipi\_addr

| struct [in\_addr](structin__addr.md) in\_pktinfo::ipi\_addr |
| --- |

Header Destination address.

## [◆ ](#a0688c86ded281fd5c2fe93a03f7f6c7d)ipi\_ifindex

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int in\_pktinfo::ipi\_ifindex |
| --- |

Network interface index.

## [◆ ](#a3ed6e057196d3d34d043631453df83c1)ipi\_spec\_dst

| struct [in\_addr](structin__addr.md) in\_pktinfo::ipi\_spec\_dst |
| --- |

Local address.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[socket.h](net_2socket_8h_source.md)

- [in\_pktinfo](structin__pktinfo.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
