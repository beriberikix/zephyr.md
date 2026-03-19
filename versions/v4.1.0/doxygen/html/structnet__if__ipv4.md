---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__if__ipv4.html
original_path: doxygen/html/structnet__if__ipv4.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_if\_ipv4 Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Interface abstraction layer](group__net__if.md)

IPv4 configuration.
[More...](#details)

`#include <[net_if.h](net__if_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [net\_if\_addr\_ipv4](structnet__if__addr__ipv4.md) | [unicast](#a806cf92123452ed3aa93540803b0a8d3) [NET\_IF\_MAX\_IPV4\_ADDR] |
|  | Unicast IP addresses. |
| struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) | [mcast](#adfaf5b50255bd35297195a7218729ae7) [NET\_IF\_MAX\_IPV4\_MADDR] |
|  | Multicast IP addresses. |
| struct [in\_addr](structin__addr.md) | [gw](#aa24772c7202bf465ee3da94a172b7bcb) |
|  | Gateway. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ttl](#acdc6d5d6eb5362f4f6d2c027cc40e684) |
|  | IPv4 time-to-live. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mcast\_ttl](#a7e9bf16d51989cfcfe564f4f0a43b480) |
|  | IPv4 time-to-live for multicast packets. |

## Detailed Description

IPv4 configuration.

## Field Documentation

## [◆ ](#aa24772c7202bf465ee3da94a172b7bcb)gw

| struct [in\_addr](structin__addr.md) net\_if\_ipv4::gw |
| --- |

Gateway.

## [◆ ](#adfaf5b50255bd35297195a7218729ae7)mcast

| struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) net\_if\_ipv4::mcast[NET\_IF\_MAX\_IPV4\_MADDR] |
| --- |

Multicast IP addresses.

## [◆ ](#a7e9bf16d51989cfcfe564f4f0a43b480)mcast\_ttl

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_if\_ipv4::mcast\_ttl |
| --- |

IPv4 time-to-live for multicast packets.

## [◆ ](#acdc6d5d6eb5362f4f6d2c027cc40e684)ttl

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_if\_ipv4::ttl |
| --- |

IPv4 time-to-live.

## [◆ ](#a806cf92123452ed3aa93540803b0a8d3)unicast

| struct [net\_if\_addr\_ipv4](structnet__if__addr__ipv4.md) net\_if\_ipv4::unicast[NET\_IF\_MAX\_IPV4\_ADDR] |
| --- |

Unicast IP addresses.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_if.h](net__if_8h_source.md)

- [net\_if\_ipv4](structnet__if__ipv4.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
