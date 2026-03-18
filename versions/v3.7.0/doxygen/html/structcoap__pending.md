---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structcoap__pending.html
original_path: doxygen/html/structcoap__pending.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coap\_pending Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [COAP Library](group__coap.md)

Represents a request awaiting for an acknowledgment (ACK).
[More...](#details)

`#include <[coap.h](coap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [sockaddr](structsockaddr.md) | [addr](#adcc34b0d0201a24b15a5adca89ae0da3) |
|  | Remote address. |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [t0](#a8b95f80a6eaac759ed0895201ff089d9) |
|  | Time when the request was sent. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [timeout](#ab31339cc91df71ee6f90d5702f722fd6) |
|  | Timeout in ms. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [id](#a8b1952271bd0c733c2fbcb158b60ca99) |
|  | Message id. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [data](#a0a506507e472b3813e672f2b455e4bcc) |
|  | User allocated buffer. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [len](#a4eb95f8fadef7d42aecdf25cc5ee3b1d) |
|  | Length of the CoAP packet. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [retries](#a8aebb187845bcb6cb07dee68927f1aa6) |
|  | Number of times the request has been sent. |
| struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) | [params](#a05ca08379d13e10dfe86322f666c3d97) |
|  | Transmission parameters. |

## Detailed Description

Represents a request awaiting for an acknowledgment (ACK).

## Field Documentation

## [◆ ](#adcc34b0d0201a24b15a5adca89ae0da3)addr

| struct [sockaddr](structsockaddr.md) coap\_pending::addr |
| --- |

Remote address.

## [◆ ](#a0a506507e472b3813e672f2b455e4bcc)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* coap\_pending::data |
| --- |

User allocated buffer.

## [◆ ](#a8b1952271bd0c733c2fbcb158b60ca99)id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) coap\_pending::id |
| --- |

Message id.

## [◆ ](#a4eb95f8fadef7d42aecdf25cc5ee3b1d)len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) coap\_pending::len |
| --- |

Length of the CoAP packet.

## [◆ ](#a05ca08379d13e10dfe86322f666c3d97)params

| struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) coap\_pending::params |
| --- |

Transmission parameters.

## [◆ ](#a8aebb187845bcb6cb07dee68927f1aa6)retries

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) coap\_pending::retries |
| --- |

Number of times the request has been sent.

## [◆ ](#a8b95f80a6eaac759ed0895201ff089d9)t0

| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) coap\_pending::t0 |
| --- |

Time when the request was sent.

## [◆ ](#ab31339cc91df71ee6f90d5702f722fd6)timeout

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) coap\_pending::timeout |
| --- |

Timeout in ms.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[coap.h](coap_8h_source.md)

- [coap\_pending](structcoap__pending.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
