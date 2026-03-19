---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__event__ipv4__pmtu__info.html
original_path: doxygen/html/structnet__event__ipv4__pmtu__info.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_event\_ipv4\_pmtu\_info Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Management](group__net__mgmt.md)

Network Management event information structure Used to pass information on network event NET\_EVENT\_IPV4\_PMTU\_CHANGED when CONFIG\_NET\_MGMT\_EVENT\_INFO enabled and event generator pass the information.
[More...](#details)

`#include <[net_event.h](net__event_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [in\_addr](structin__addr.md) | [dst](#a9779ec9487b5dde4d5df1d0aeef82ebf) |
|  | IPv4 address. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [mtu](#ae4f6951aed4253428a7ac4273b8b43fe) |
|  | New MTU. |

## Detailed Description

Network Management event information structure Used to pass information on network event NET\_EVENT\_IPV4\_PMTU\_CHANGED when CONFIG\_NET\_MGMT\_EVENT\_INFO enabled and event generator pass the information.

## Field Documentation

## [◆ ](#a9779ec9487b5dde4d5df1d0aeef82ebf)dst

| struct [in\_addr](structin__addr.md) net\_event\_ipv4\_pmtu\_info::dst |
| --- |

IPv4 address.

## [◆ ](#ae4f6951aed4253428a7ac4273b8b43fe)mtu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_event\_ipv4\_pmtu\_info::mtu |
| --- |

New MTU.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_event.h](net__event_8h_source.md)

- [net\_event\_ipv4\_pmtu\_info](structnet__event__ipv4__pmtu__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
