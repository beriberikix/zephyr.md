---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__event__ipv6__pmtu__info.html
original_path: doxygen/html/structnet__event__ipv6__pmtu__info.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_event\_ipv6\_pmtu\_info Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Management](group__net__mgmt.md)

Network Management event information structure Used to pass information on network event NET\_EVENT\_IPV6\_PMTU\_CHANGED when CONFIG\_NET\_MGMT\_EVENT\_INFO enabled and event generator pass the information.
[More...](#details)

`#include <[net_event.h](net__event_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [in6\_addr](structin6__addr.md) | [dst](#aa9398dc7f56432b7489bcba7e9a6803c) |
|  | IPv6 address. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [mtu](#a52e5078e0f39cb5e95d4e5bc42674480) |
|  | New MTU. |

## Detailed Description

Network Management event information structure Used to pass information on network event NET\_EVENT\_IPV6\_PMTU\_CHANGED when CONFIG\_NET\_MGMT\_EVENT\_INFO enabled and event generator pass the information.

## Field Documentation

## [◆ ](#aa9398dc7f56432b7489bcba7e9a6803c)dst

| struct [in6\_addr](structin6__addr.md) net\_event\_ipv6\_pmtu\_info::dst |
| --- |

IPv6 address.

## [◆ ](#a52e5078e0f39cb5e95d4e5bc42674480)mtu

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_event\_ipv6\_pmtu\_info::mtu |
| --- |

New MTU.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_event.h](net__event_8h_source.md)

- [net\_event\_ipv6\_pmtu\_info](structnet__event__ipv6__pmtu__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
