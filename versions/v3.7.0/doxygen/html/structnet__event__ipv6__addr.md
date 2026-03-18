---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structnet__event__ipv6__addr.html
original_path: doxygen/html/structnet__event__ipv6__addr.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_event\_ipv6\_addr Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Management](group__net__mgmt.md)

Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_ADDR\_ADD, NET\_EVENT\_IPV6\_ADDR\_DEL, NET\_EVENT\_IPV6\_MADDR\_ADD and NET\_EVENT\_IPV6\_MADDR\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO enabled and event generator pass the information.
[More...](#details)

`#include <[net_event.h](net__event_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [in6\_addr](structin6__addr.md) | [addr](#a3cb4dd6d1e33ef2769cd64fa27c69b43) |
|  | IPv6 address related to this event. |

## Detailed Description

Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_ADDR\_ADD, NET\_EVENT\_IPV6\_ADDR\_DEL, NET\_EVENT\_IPV6\_MADDR\_ADD and NET\_EVENT\_IPV6\_MADDR\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO enabled and event generator pass the information.

## Field Documentation

## [◆ ](#a3cb4dd6d1e33ef2769cd64fa27c69b43)addr

| struct [in6\_addr](structin6__addr.md) net\_event\_ipv6\_addr::addr |
| --- |

IPv6 address related to this event.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_event.h](net__event_8h_source.md)

- [net\_event\_ipv6\_addr](structnet__event__ipv6__addr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
