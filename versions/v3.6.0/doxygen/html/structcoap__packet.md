---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structcoap__packet.html
original_path: doxygen/html/structcoap__packet.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coap\_packet Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [COAP Library](group__coap.md)

Representation of a CoAP Packet.
[More...](#details)

`#include <[coap.h](coap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [data](#a8116711bcdff1fa6b0cf5c4fa9ab88d1) |
|  | User allocated buffer. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [offset](#a46c0842c785b8de5eb8564950a786c02) |
|  | CoAP lib maintains offset while adding data. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_len](#a48c216a7da37e85942d271c85a79bcb6) |
|  | Max CoAP packet data length. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [hdr\_len](#ab302c002da88f6d3a44c3a2215082be4) |
|  | CoAP header length. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [opt\_len](#acc5542ba2a69db8957155b90e75fd563) |
|  | Total options length (delta + len + value). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [delta](#a95dd8c6fb08ac61a1571c84258579475) |
|  | Used for delta calculation in CoAP packet. |

## Detailed Description

Representation of a CoAP Packet.

## Field Documentation

## [◆ ](#a8116711bcdff1fa6b0cf5c4fa9ab88d1)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* coap\_packet::data |
| --- |

User allocated buffer.

## [◆ ](#a95dd8c6fb08ac61a1571c84258579475)delta

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) coap\_packet::delta |
| --- |

Used for delta calculation in CoAP packet.

## [◆ ](#ab302c002da88f6d3a44c3a2215082be4)hdr\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) coap\_packet::hdr\_len |
| --- |

CoAP header length.

## [◆ ](#a48c216a7da37e85942d271c85a79bcb6)max\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) coap\_packet::max\_len |
| --- |

Max CoAP packet data length.

## [◆ ](#a46c0842c785b8de5eb8564950a786c02)offset

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) coap\_packet::offset |
| --- |

CoAP lib maintains offset while adding data.

## [◆ ](#acc5542ba2a69db8957155b90e75fd563)opt\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) coap\_packet::opt\_len |
| --- |

Total options length (delta + len + value).

---

The documentation for this struct was generated from the following file:

- zephyr/net/[coap.h](coap_8h_source.md)

- [coap\_packet](structcoap__packet.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
