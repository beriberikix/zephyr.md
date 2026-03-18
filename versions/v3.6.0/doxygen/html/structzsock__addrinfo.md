---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structzsock__addrinfo.html
original_path: doxygen/html/structzsock__addrinfo.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

zsock\_addrinfo Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [BSD Sockets compatible API](group__bsd__sockets.md)

Definition used when querying address information.
[More...](#details)

`#include <[socket.h](net_2socket_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [zsock\_addrinfo](structzsock__addrinfo.md) \* | [ai\_next](#a7fdc7a266b2f96766f8c4e79649bfa65) |
|  | Pointer to next address entry. |
| int | [ai\_flags](#a971514adde66f5c1a04efc7f42f244d1) |
|  | Additional options. |
| int | [ai\_family](#a83ef78e3347e69564e2663a769356d87) |
|  | Address family of the returned addresses. |
| int | [ai\_socktype](#adcb8a732921a11a35f89241cfe413b78) |
|  | Socket type, for example SOCK\_STREAM or SOCK\_DGRAM. |
| int | [ai\_protocol](#aae090dcd0c1e73497560cbcc333a452d) |
|  | Protocol for addresses, 0 means any protocol. |
| [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | [ai\_addrlen](#afeb3c893f19642352f79404dbe5443b2) |
|  | Length of the socket address. |
| struct [sockaddr](structsockaddr.md) \* | [ai\_addr](#acd0173c9e99bb72b444c18f4237bf17b) |
|  | Pointer to the address. |
| char \* | [ai\_canonname](#aa9a96f1d5d49833beea05558879867cf) |
|  | Optional official name of the host. |

## Detailed Description

Definition used when querying address information.

A linked list of these descriptors is returned by [getaddrinfo()](group__bsd__sockets.md#ga08be4218900930dcc3add7e03173a83c "POSIX wrapper for zsock_getaddrinfo."). The struct is also passed as hints when calling the [getaddrinfo()](group__bsd__sockets.md#ga08be4218900930dcc3add7e03173a83c "POSIX wrapper for zsock_getaddrinfo.") function.

## Field Documentation

## [◆ ](#acd0173c9e99bb72b444c18f4237bf17b)ai\_addr

| struct [sockaddr](structsockaddr.md)\* zsock\_addrinfo::ai\_addr |
| --- |

Pointer to the address.

## [◆ ](#afeb3c893f19642352f79404dbe5443b2)ai\_addrlen

| [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) zsock\_addrinfo::ai\_addrlen |
| --- |

Length of the socket address.

## [◆ ](#aa9a96f1d5d49833beea05558879867cf)ai\_canonname

| char\* zsock\_addrinfo::ai\_canonname |
| --- |

Optional official name of the host.

## [◆ ](#a83ef78e3347e69564e2663a769356d87)ai\_family

| int zsock\_addrinfo::ai\_family |
| --- |

Address family of the returned addresses.

## [◆ ](#a971514adde66f5c1a04efc7f42f244d1)ai\_flags

| int zsock\_addrinfo::ai\_flags |
| --- |

Additional options.

## [◆ ](#a7fdc7a266b2f96766f8c4e79649bfa65)ai\_next

| struct [zsock\_addrinfo](structzsock__addrinfo.md)\* zsock\_addrinfo::ai\_next |
| --- |

Pointer to next address entry.

## [◆ ](#aae090dcd0c1e73497560cbcc333a452d)ai\_protocol

| int zsock\_addrinfo::ai\_protocol |
| --- |

Protocol for addresses, 0 means any protocol.

## [◆ ](#adcb8a732921a11a35f89241cfe413b78)ai\_socktype

| int zsock\_addrinfo::ai\_socktype |
| --- |

Socket type, for example SOCK\_STREAM or SOCK\_DGRAM.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[socket.h](net_2socket_8h_source.md)

- [zsock\_addrinfo](structzsock__addrinfo.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
