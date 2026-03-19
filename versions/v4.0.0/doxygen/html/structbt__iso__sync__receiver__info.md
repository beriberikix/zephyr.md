---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__iso__sync__receiver__info.html
original_path: doxygen/html/structbt__iso__sync__receiver__info.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_iso\_sync\_receiver\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Isochronous channels (ISO)](group__bt__iso.md)

ISO Synchronized Receiver Info Structure.
[More...](#details)

`#include <[iso.h](iso_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [latency](#a24bad4231eb214a2c95b1da9ba59c284) |
|  | The transport latency in us. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pto](#a80ac6e529491156109955219569fdec6) |
|  | Pre-transmission offset (N \* 1.25 ms). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_pdu](#a40ff5a4d691a75802f211a63b1e12303) |
|  | The maximum PDU size in octets. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bn](#a8be50f8c6d76515ac290407959eaf0e1) |
|  | The burst number. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [irc](#a6185a7ac123be930650da6dc84c0c1e0) |
|  | Number of times a payload is transmitted in a BIS event. |

## Detailed Description

ISO Synchronized Receiver Info Structure.

## Field Documentation

## [◆ ](#a8be50f8c6d76515ac290407959eaf0e1)bn

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_sync\_receiver\_info::bn |
| --- |

The burst number.

## [◆ ](#a6185a7ac123be930650da6dc84c0c1e0)irc

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_sync\_receiver\_info::irc |
| --- |

Number of times a payload is transmitted in a BIS event.

## [◆ ](#a24bad4231eb214a2c95b1da9ba59c284)latency

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_iso\_sync\_receiver\_info::latency |
| --- |

The transport latency in us.

## [◆ ](#a40ff5a4d691a75802f211a63b1e12303)max\_pdu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_iso\_sync\_receiver\_info::max\_pdu |
| --- |

The maximum PDU size in octets.

## [◆ ](#a80ac6e529491156109955219569fdec6)pto

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_iso\_sync\_receiver\_info::pto |
| --- |

Pre-transmission offset (N \* 1.25 ms).

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[iso.h](iso_8h_source.md)

- [bt\_iso\_sync\_receiver\_info](structbt__iso__sync__receiver__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
