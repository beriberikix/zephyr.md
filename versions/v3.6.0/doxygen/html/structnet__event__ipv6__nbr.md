---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnet__event__ipv6__nbr.html
original_path: doxygen/html/structnet__event__ipv6__nbr.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_event\_ipv6\_nbr Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Management](group__net__mgmt.md)

Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_NBR\_ADD and NET\_EVENT\_IPV6\_NBR\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO enabled and event generator pass the information.
[More...](#details)

`#include <[net_event.h](net__event_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [in6\_addr](structin6__addr.md) | [addr](#a75653facd98b568c300395c45191b289) |
| int | [idx](#adeb139ad70e794d1a805315ffd1fcbee) |

## Detailed Description

Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_NBR\_ADD and NET\_EVENT\_IPV6\_NBR\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO enabled and event generator pass the information.

Note
:   : idx will be '-1' in case of NET\_EVENT\_IPV6\_NBR\_DEL event.

## Field Documentation

## [◆ ](#a75653facd98b568c300395c45191b289)addr

| struct [in6\_addr](structin6__addr.md) net\_event\_ipv6\_nbr::addr |
| --- |

## [◆ ](#adeb139ad70e794d1a805315ffd1fcbee)idx

| int net\_event\_ipv6\_nbr::idx |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_event.h](net__event_8h_source.md)

- [net\_event\_ipv6\_nbr](structnet__event__ipv6__nbr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
