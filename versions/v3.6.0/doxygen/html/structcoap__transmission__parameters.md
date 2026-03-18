---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structcoap__transmission__parameters.html
original_path: doxygen/html/structcoap__transmission__parameters.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coap\_transmission\_parameters Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [COAP Library](group__coap.md)

CoAP transmission parameters.
[More...](#details)

`#include <[coap.h](coap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ack\_timeout](#aca76954d785d04312fb834dc524f102c) |
|  | Initial ACK timeout. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [coap\_backoff\_percent](#a74c91235bf64fab5e7abc0c9f581e44c) |
|  | Set CoAP retry backoff factor. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [max\_retransmission](#a3a9b8bf0f2e00fc0981acdd86d404190) |
|  | Maximum number of retransmissions. |

## Detailed Description

CoAP transmission parameters.

## Field Documentation

## [◆ ](#aca76954d785d04312fb834dc524f102c)ack\_timeout

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) coap\_transmission\_parameters::ack\_timeout |
| --- |

Initial ACK timeout.

Value is used as a base value to retry pending CoAP packets.

## [◆ ](#a74c91235bf64fab5e7abc0c9f581e44c)coap\_backoff\_percent

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) coap\_transmission\_parameters::coap\_backoff\_percent |
| --- |

Set CoAP retry backoff factor.

A value of 200 means a factor of 2.0.

## [◆ ](#a3a9b8bf0f2e00fc0981acdd86d404190)max\_retransmission

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) coap\_transmission\_parameters::max\_retransmission |
| --- |

Maximum number of retransmissions.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[coap.h](coap_8h_source.md)

- [coap\_transmission\_parameters](structcoap__transmission__parameters.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
