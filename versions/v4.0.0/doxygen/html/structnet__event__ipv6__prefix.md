---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structnet__event__ipv6__prefix.html
original_path: doxygen/html/structnet__event__ipv6__prefix.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_event\_ipv6\_prefix Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Management](group__net__mgmt.md)

Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_PREFIX\_ADD and NET\_EVENT\_IPV6\_PREFIX\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO is enabled and event generator pass the information.
[More...](#details)

`#include <[net_event.h](net__event_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [in6\_addr](structin6__addr.md) | [addr](#a5ccae593ce7678fcdd91a4d0eaf142fb) |
|  | IPv6 prefix. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [len](#a3d70216e13fc0f78e08eb27f34fe8ace) |
|  | IPv6 prefix length. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [lifetime](#a6d7b0323896e43a04931ece4daaa09c4) |
|  | IPv6 prefix lifetime in seconds. |

## Detailed Description

Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_PREFIX\_ADD and NET\_EVENT\_IPV6\_PREFIX\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO is enabled and event generator pass the information.

## Field Documentation

## [◆ ](#a5ccae593ce7678fcdd91a4d0eaf142fb)addr

| struct [in6\_addr](structin6__addr.md) net\_event\_ipv6\_prefix::addr |
| --- |

IPv6 prefix.

## [◆ ](#a3d70216e13fc0f78e08eb27f34fe8ace)len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_event\_ipv6\_prefix::len |
| --- |

IPv6 prefix length.

## [◆ ](#a6d7b0323896e43a04931ece4daaa09c4)lifetime

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_event\_ipv6\_prefix::lifetime |
| --- |

IPv6 prefix lifetime in seconds.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_event.h](net__event_8h_source.md)

- [net\_event\_ipv6\_prefix](structnet__event__ipv6__prefix.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
