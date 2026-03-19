---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structip__mreq.html
original_path: doxygen/html/structip__mreq.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ip\_mreq Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [BSD Sockets compatible API](group__bsd__sockets.md)

Struct used when setting a IPv4 multicast network interface.
[More...](#details)

`#include <[socket.h](net_2socket_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [in\_addr](structin__addr.md) | [imr\_multiaddr](#a68a7523377d80bddb61cd260ed0d8658) |
|  | IP multicast group address. |
| struct [in\_addr](structin__addr.md) | [imr\_interface](#a5a01c67398a3c25dab84996a04730a2a) |
|  | IP address of local interface. |

## Detailed Description

Struct used when setting a IPv4 multicast network interface.

## Field Documentation

## [◆ ](#a5a01c67398a3c25dab84996a04730a2a)imr\_interface

| struct [in\_addr](structin__addr.md) ip\_mreq::imr\_interface |
| --- |

IP address of local interface.

## [◆ ](#a68a7523377d80bddb61cd260ed0d8658)imr\_multiaddr

| struct [in\_addr](structin__addr.md) ip\_mreq::imr\_multiaddr |
| --- |

IP multicast group address.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[socket.h](net_2socket_8h_source.md)

- [ip\_mreq](structip__mreq.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
