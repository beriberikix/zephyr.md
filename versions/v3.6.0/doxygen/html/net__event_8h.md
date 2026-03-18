---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/net__event_8h.html
original_path: doxygen/html/net__event_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_event.h File Reference

Network Events code public header.
[More...](#details)

`#include <[zephyr/net/net_ip.h](net__ip_8h_source.md)>`  
`#include <[zephyr/net/hostname.h](hostname_8h_source.md)>`

[Go to the source code of this file.](net__event_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [net\_event\_ipv6\_addr](structnet__event__ipv6__addr.md) |
|  | Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_ADDR\_ADD, NET\_EVENT\_IPV6\_ADDR\_DEL, NET\_EVENT\_IPV6\_MADDR\_ADD and NET\_EVENT\_IPV6\_MADDR\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO enabled and event generator pass the information. [More...](structnet__event__ipv6__addr.md#details) |
| struct | [net\_event\_ipv6\_nbr](structnet__event__ipv6__nbr.md) |
|  | Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_NBR\_ADD and NET\_EVENT\_IPV6\_NBR\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO enabled and event generator pass the information. [More...](structnet__event__ipv6__nbr.md#details) |
| struct | [net\_event\_ipv6\_route](structnet__event__ipv6__route.md) |
|  | Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_ROUTE\_ADD and NET\_EVENT\_IPV6\_ROUTE\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO enabled and event generator pass the information. [More...](structnet__event__ipv6__route.md#details) |
| struct | [net\_event\_ipv6\_prefix](structnet__event__ipv6__prefix.md) |
|  | Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_PREFIX\_ADD and NET\_EVENT\_IPV6\_PREFIX\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO is enabled and event generator pass the information. [More...](structnet__event__ipv6__prefix.md#details) |
| struct | [net\_event\_l4\_hostname](structnet__event__l4__hostname.md) |
|  | Network Management event information structure Used to pass information on NET\_EVENT\_HOSTNAME\_CHANGED event when CONFIG\_NET\_MGMT\_EVENT\_INFO is enabled and event generator pass the information. [More...](structnet__event__l4__hostname.md#details) |

## Detailed Description

Network Events code public header.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_event.h](net__event_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
