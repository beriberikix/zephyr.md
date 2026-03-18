---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnet__event__ipv6__route.html
original_path: doxygen/html/structnet__event__ipv6__route.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_event\_ipv6\_route Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Management](group__net__mgmt.md)

Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_ROUTE\_ADD and NET\_EVENT\_IPV6\_ROUTE\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO enabled and event generator pass the information.
[More...](#details)

`#include <[net_event.h](net__event_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [in6\_addr](structin6__addr.md) | [nexthop](#ad8772d7949fa8b7e7217324acbda6829) |
| struct [in6\_addr](structin6__addr.md) | [addr](#a42bb70c6b92841e5a77c80a3a193178c) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [prefix\_len](#aa1f21f6963befb3f94183d02c6d2d23f) |

## Detailed Description

Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_ROUTE\_ADD and NET\_EVENT\_IPV6\_ROUTE\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO enabled and event generator pass the information.

## Field Documentation

## [◆ ](#a42bb70c6b92841e5a77c80a3a193178c)addr

| struct [in6\_addr](structin6__addr.md) net\_event\_ipv6\_route::addr |
| --- |

## [◆ ](#ad8772d7949fa8b7e7217324acbda6829)nexthop

| struct [in6\_addr](structin6__addr.md) net\_event\_ipv6\_route::nexthop |
| --- |

## [◆ ](#aa1f21f6963befb3f94183d02c6d2d23f)prefix\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_event\_ipv6\_route::prefix\_len |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_event.h](net__event_8h_source.md)

- [net\_event\_ipv6\_route](structnet__event__ipv6__route.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
