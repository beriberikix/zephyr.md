---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsockaddr__nm.html
original_path: doxygen/html/structsockaddr__nm.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sockaddr\_nm Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Core Library](group__socket__net__mgmt.md)

struct [sockaddr\_nm](structsockaddr__nm.md "struct sockaddr_nm - The sockaddr structure for NET_MGMT sockets") - The sockaddr structure for NET\_MGMT sockets
[More...](#details)

`#include <[socket_net_mgmt.h](socket__net__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) | [nm\_family](#af6d556718e643c9083c790e1e797eedf) |
|  | AF\_NET\_MGMT address family. |
| int | [nm\_ifindex](#a79727f415488b6e548c48a556692a330) |
|  | Network interface related to this address. |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [nm\_pid](#ad3299cf4df378026cc40ee10f5abcba1) |
|  | Thread id or similar that is used to separate the different sockets. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [nm\_mask](#ac46ee5b5a9b3a04a53a8ae6e0f640a83) |
|  | net\_mgmt mask |

## Detailed Description

struct [sockaddr\_nm](structsockaddr__nm.md "struct sockaddr_nm - The sockaddr structure for NET_MGMT sockets") - The sockaddr structure for NET\_MGMT sockets

Similar concepts are used as in Linux AF\_NETLINK. The NETLINK name is not used in order to avoid confusion between Zephyr and Linux as the implementations are different.

The socket domain (address family) is AF\_NET\_MGMT, and the type of socket is either SOCK\_RAW or SOCK\_DGRAM, because this is a datagram-oriented service.

The protocol (protocol type) selects for which feature the socket is used.

When used with [bind()](group__bsd__sockets.md#ga0de5e0b54a93dc6462078539b0a4a0b9 "POSIX wrapper for zsock_bind."), the nm\_pid field of the [sockaddr\_nm](structsockaddr__nm.md "struct sockaddr_nm - The sockaddr structure for NET_MGMT sockets") can be filled with the calling thread' own id. The nm\_pid serves here as the local address of this net\_mgmt socket. The application is responsible for picking a unique integer value to fill in nm\_pid.

## Field Documentation

## [◆ ](#af6d556718e643c9083c790e1e797eedf)nm\_family

| [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) sockaddr\_nm::nm\_family |
| --- |

AF\_NET\_MGMT address family.

## [◆ ](#a79727f415488b6e548c48a556692a330)nm\_ifindex

| int sockaddr\_nm::nm\_ifindex |
| --- |

Network interface related to this address.

## [◆ ](#ac46ee5b5a9b3a04a53a8ae6e0f640a83)nm\_mask

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sockaddr\_nm::nm\_mask |
| --- |

net\_mgmt mask

## [◆ ](#ad3299cf4df378026cc40ee10f5abcba1)nm\_pid

| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) sockaddr\_nm::nm\_pid |
| --- |

Thread id or similar that is used to separate the different sockets.

Application can decide how the pid is constructed.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[socket\_net\_mgmt.h](socket__net__mgmt_8h_source.md)

- [sockaddr\_nm](structsockaddr__nm.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
