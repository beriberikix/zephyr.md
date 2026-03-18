---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__iso__broadcaster__info.html
original_path: doxygen/html/structbt__iso__broadcaster__info.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_iso\_broadcaster\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Isochronous channels (ISO)](group__bt__iso.md)

ISO Broadcaster Info Structure.
[More...](#details)

`#include <[iso.h](iso_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sync\_delay](#a577370ab24ebd4d80db4d8ffdb918483) |
|  | The maximum time in us for all PDUs of all BIS in a BIG event. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [latency](#a71388f9b64510ab91c3147f05f775aeb) |
|  | The transport latency in us. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pto](#a9f93161fb7f81d5eb3a55f955be1b85d) |
|  | Pre-transmission offset (N \* 1.25 ms). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_pdu](#aa57b6e08cf4d3d154762c8c43de0f2cf) |
|  | The maximum PDU size in octets. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [phy](#a3d4e44a1da54e5ca0f2002ca3f6e7a13) |
|  | The transport PHY. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bn](#ab3cb80e6b362e093e6924ab11b8737e9) |
|  | The burst number. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [irc](#ac1feade59bbad1e08418e1808619f775) |
|  | Number of times a payload is transmitted in a BIS event. |

## Detailed Description

ISO Broadcaster Info Structure.

## Field Documentation

## [◆ ](#ab3cb80e6b362e093e6924ab11b8737e9)bn

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_broadcaster\_info::bn |
| --- |

The burst number.

## [◆ ](#ac1feade59bbad1e08418e1808619f775)irc

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_broadcaster\_info::irc |
| --- |

Number of times a payload is transmitted in a BIS event.

## [◆ ](#a71388f9b64510ab91c3147f05f775aeb)latency

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_iso\_broadcaster\_info::latency |
| --- |

The transport latency in us.

## [◆ ](#aa57b6e08cf4d3d154762c8c43de0f2cf)max\_pdu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_iso\_broadcaster\_info::max\_pdu |
| --- |

The maximum PDU size in octets.

## [◆ ](#a3d4e44a1da54e5ca0f2002ca3f6e7a13)phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_broadcaster\_info::phy |
| --- |

The transport PHY.

## [◆ ](#a9f93161fb7f81d5eb3a55f955be1b85d)pto

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_iso\_broadcaster\_info::pto |
| --- |

Pre-transmission offset (N \* 1.25 ms).

## [◆ ](#a577370ab24ebd4d80db4d8ffdb918483)sync\_delay

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_iso\_broadcaster\_info::sync\_delay |
| --- |

The maximum time in us for all PDUs of all BIS in a BIG event.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[iso.h](iso_8h_source.md)

- [bt\_iso\_broadcaster\_info](structbt__iso__broadcaster__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
