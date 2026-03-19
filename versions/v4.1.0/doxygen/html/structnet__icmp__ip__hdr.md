---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__icmp__ip__hdr.html
original_path: doxygen/html/structnet__icmp__ip__hdr.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_icmp\_ip\_hdr Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Send and receive IPv4 or IPv6 ICMP Echo Request messages.](group__icmp.md)

Struct presents either IPv4 or IPv6 header in ICMP response message.
[More...](#details)

`#include <[icmp.h](icmp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| struct net\_ipv4\_hdr \*   [ipv4](#a3d0d8b7442611c74a71a72ab1d1c7a90) |  |
|  | IPv4 header in response message. [More...](#a3d0d8b7442611c74a71a72ab1d1c7a90) |
| struct net\_ipv6\_hdr \*   [ipv6](#ac993b71afdd637dba048ba5038d489c8) |  |
|  | IPv6 header in response message. [More...](#ac993b71afdd637dba048ba5038d489c8) |
| }; |  |
| [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) | [family](#a4e0f7c9694ed1c7bfafc0d73d7447b26) |
|  | Is the header IPv4 or IPv6 one. |

## Detailed Description

Struct presents either IPv4 or IPv6 header in ICMP response message.

## Field Documentation

## [◆ ](#a2db6f9a29bd3cc97b662f00d2d886e85)[union]

| union { ... } [net\_icmp\_ip\_hdr](structnet__icmp__ip__hdr.md) |
| --- |

## [◆ ](#a4e0f7c9694ed1c7bfafc0d73d7447b26)family

| [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) net\_icmp\_ip\_hdr::family |
| --- |

Is the header IPv4 or IPv6 one.

Value of either AF\_INET or AF\_INET6

## [◆ ](#a3d0d8b7442611c74a71a72ab1d1c7a90)ipv4

| struct net\_ipv4\_hdr\* net\_icmp\_ip\_hdr::ipv4 |
| --- |

IPv4 header in response message.

## [◆ ](#ac993b71afdd637dba048ba5038d489c8)ipv6

| struct net\_ipv6\_hdr\* net\_icmp\_ip\_hdr::ipv6 |
| --- |

IPv6 header in response message.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[icmp.h](icmp_8h_source.md)

- [net\_icmp\_ip\_hdr](structnet__icmp__ip__hdr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
