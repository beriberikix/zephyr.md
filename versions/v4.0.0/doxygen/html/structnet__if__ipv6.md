---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structnet__if__ipv6.html
original_path: doxygen/html/structnet__if__ipv6.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_if\_ipv6 Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Interface abstraction layer](group__net__if.md)

IPv6 configuration.
[More...](#details)

`#include <[net_if.h](net__if_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [net\_if\_addr](structnet__if__addr.md) | [unicast](#adb6431d336cc3f46972e13d2255452c8) [NET\_IF\_MAX\_IPV6\_ADDR] |
|  | Unicast IP addresses. |
| struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) | [mcast](#a727d2773e0dee3be687dda5b2dd55682) [NET\_IF\_MAX\_IPV6\_MADDR] |
|  | Multicast IP addresses. |
| struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) | [prefix](#a2dccdc984f08527302d8d910a2658f72) [NET\_IF\_MAX\_IPV6\_PREFIX] |
|  | Prefixes. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [base\_reachable\_time](#a500a78fe23ee2ebc63f3d3b53b5b92ea) |
|  | Default reachable time (RFC 4861, page 52). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [reachable\_time](#af57b7dca189167f8cc757c4ed6b08f2f) |
|  | Reachable time (RFC 4861, page 20). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [retrans\_timer](#ac5ee47ff9d3e429ecbb8623e5d713246) |
|  | Retransmit timer (RFC 4861, page 52). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [hop\_limit](#a71775a082984274fbc7c009ead18e751) |
|  | IPv6 hop limit. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mcast\_hop\_limit](#ae94906c28578f2e1ea2506b0e2972d4c) |
|  | IPv6 multicast hop limit. |

## Detailed Description

IPv6 configuration.

## Field Documentation

## [◆ ](#a500a78fe23ee2ebc63f3d3b53b5b92ea)base\_reachable\_time

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_if\_ipv6::base\_reachable\_time |
| --- |

Default reachable time (RFC 4861, page 52).

## [◆ ](#a71775a082984274fbc7c009ead18e751)hop\_limit

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_if\_ipv6::hop\_limit |
| --- |

IPv6 hop limit.

## [◆ ](#a727d2773e0dee3be687dda5b2dd55682)mcast

| struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) net\_if\_ipv6::mcast[NET\_IF\_MAX\_IPV6\_MADDR] |
| --- |

Multicast IP addresses.

## [◆ ](#ae94906c28578f2e1ea2506b0e2972d4c)mcast\_hop\_limit

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_if\_ipv6::mcast\_hop\_limit |
| --- |

IPv6 multicast hop limit.

## [◆ ](#a2dccdc984f08527302d8d910a2658f72)prefix

| struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) net\_if\_ipv6::prefix[NET\_IF\_MAX\_IPV6\_PREFIX] |
| --- |

Prefixes.

## [◆ ](#af57b7dca189167f8cc757c4ed6b08f2f)reachable\_time

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_if\_ipv6::reachable\_time |
| --- |

Reachable time (RFC 4861, page 20).

## [◆ ](#ac5ee47ff9d3e429ecbb8623e5d713246)retrans\_timer

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_if\_ipv6::retrans\_timer |
| --- |

Retransmit timer (RFC 4861, page 52).

## [◆ ](#adb6431d336cc3f46972e13d2255452c8)unicast

| struct [net\_if\_addr](structnet__if__addr.md) net\_if\_ipv6::unicast[NET\_IF\_MAX\_IPV6\_ADDR] |
| --- |

Unicast IP addresses.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_if.h](net__if_8h_source.md)

- [net\_if\_ipv6](structnet__if__ipv6.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
