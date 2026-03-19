---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structipv6__mreq.html
original_path: doxygen/html/structipv6__mreq.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipv6\_mreq Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [BSD Sockets compatible API](group__bsd__sockets.md)

Struct used when joining or leaving a IPv6 multicast group.
[More...](#details)

`#include <[socket.h](net_2socket_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [in6\_addr](structin6__addr.md) | [ipv6mr\_multiaddr](#a11adc73ca35eb4c46bf443ecc15d4715) |
|  | IPv6 multicast address of group. |
| int | [ipv6mr\_ifindex](#aacd3c9cbb7cd91bf914570bd9d20298f) |
|  | Network interface index of the local IPv6 address. |

## Detailed Description

Struct used when joining or leaving a IPv6 multicast group.

## Field Documentation

## [◆ ](#aacd3c9cbb7cd91bf914570bd9d20298f)ipv6mr\_ifindex

| int ipv6\_mreq::ipv6mr\_ifindex |
| --- |

Network interface index of the local IPv6 address.

## [◆ ](#a11adc73ca35eb4c46bf443ecc15d4715)ipv6mr\_multiaddr

| struct [in6\_addr](structin6__addr.md) ipv6\_mreq::ipv6mr\_multiaddr |
| --- |

IPv6 multicast address of group.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[socket.h](net_2socket_8h_source.md)

- [ipv6\_mreq](structipv6__mreq.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
