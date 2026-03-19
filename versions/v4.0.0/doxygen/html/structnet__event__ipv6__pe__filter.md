---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structnet__event__ipv6__pe__filter.html
original_path: doxygen/html/structnet__event__ipv6__pe__filter.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_event\_ipv6\_pe\_filter Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Management](group__net__mgmt.md)

Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_PE\_FILTER\_ADD and NET\_EVENT\_IPV6\_PE\_FILTER\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO is enabled and event generator pass the information.
[More...](#details)

`#include <[net_event.h](net__event_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [in6\_addr](structin6__addr.md) | [prefix](#a2c0b6477f021e32bae98916f74e6affc) |
|  | IPv6 address of privacy extension filter. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [is\_deny\_list](#a07961a42f5ff8ca98615164192b8ca5a) |
|  | IPv6 filter deny or allow list. |

## Detailed Description

Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_PE\_FILTER\_ADD and NET\_EVENT\_IPV6\_PE\_FILTER\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO is enabled and event generator pass the information.

This is only available if CONFIG\_NET\_IPV6\_PE\_FILTER\_PREFIX\_COUNT is >0.

## Field Documentation

## [◆ ](#a07961a42f5ff8ca98615164192b8ca5a)is\_deny\_list

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_event\_ipv6\_pe\_filter::is\_deny\_list |
| --- |

IPv6 filter deny or allow list.

## [◆ ](#a2c0b6477f021e32bae98916f74e6affc)prefix

| struct [in6\_addr](structin6__addr.md) net\_event\_ipv6\_pe\_filter::prefix |
| --- |

IPv6 address of privacy extension filter.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_event.h](net__event_8h_source.md)

- [net\_event\_ipv6\_pe\_filter](structnet__event__ipv6__pe__filter.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
