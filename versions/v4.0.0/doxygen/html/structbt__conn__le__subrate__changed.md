---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__conn__le__subrate__changed.html
original_path: doxygen/html/structbt__conn__le__subrate__changed.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_le\_subrate\_changed Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

Updated subrating connection parameters for LE connections.
[More...](#details)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [status](#afc5a577dadf41819e89bc3af016ce258) |
|  | HCI Status from LE Subrate Changed event. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [factor](#a0c3e3dc41ca4dec92740c920e959060b) |
|  | Connection subrate factor. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [continuation\_number](#a2420a0a3145471c6a1a618bea8d1d7c6) |
|  | Number of underlying connection events to remain active after a packet containing a Link Layer PDU with a non-zero Length field is sent or received. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [peripheral\_latency](#aa0bab070bc43972dfb3a5259934b4931) |
|  | Peripheral latency in units of subrated connection intervals. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [supervision\_timeout](#aab0cb08a7549401684bcab3c291dc192) |
|  | Connection Supervision timeout (N \* 10 ms). |

## Detailed Description

Updated subrating connection parameters for LE connections.

## Field Documentation

## [◆ ](#a2420a0a3145471c6a1a618bea8d1d7c6)continuation\_number

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_subrate\_changed::continuation\_number |
| --- |

Number of underlying connection events to remain active after a packet containing a Link Layer PDU with a non-zero Length field is sent or received.

## [◆ ](#a0c3e3dc41ca4dec92740c920e959060b)factor

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_subrate\_changed::factor |
| --- |

Connection subrate factor.

## [◆ ](#aa0bab070bc43972dfb3a5259934b4931)peripheral\_latency

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_subrate\_changed::peripheral\_latency |
| --- |

Peripheral latency in units of subrated connection intervals.

## [◆ ](#afc5a577dadf41819e89bc3af016ce258)status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_subrate\_changed::status |
| --- |

HCI Status from LE Subrate Changed event.

The remaining parameters will be unchanged if status is not BT\_HCI\_ERR\_SUCCESS.

## [◆ ](#aab0cb08a7549401684bcab3c291dc192)supervision\_timeout

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_subrate\_changed::supervision\_timeout |
| --- |

Connection Supervision timeout (N \* 10 ms).

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_le\_subrate\_changed](structbt__conn__le__subrate__changed.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
