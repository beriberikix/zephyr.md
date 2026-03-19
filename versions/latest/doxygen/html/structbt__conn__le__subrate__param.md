---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__conn__le__subrate__param.html
original_path: doxygen/html/structbt__conn__le__subrate__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_le\_subrate\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

Connection subrating parameters for LE connections.
[More...](#details)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [subrate\_min](#aef75fec8ba8c9987d55e81aa2539b96e) |
|  | Minimum subrate factor. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [subrate\_max](#a59d2d244e3568b8f97ce936121d41b1a) |
|  | Maximum subrate factor. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_latency](#a15d05324708ddeea8d2f3515eea396bb) |
|  | Maximum Peripheral latency in units of subrated connection intervals. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [continuation\_number](#a978cef5f2f14a5a7fe7ded09c6fdf2d9) |
|  | Minimum number of underlying connection events to remain active after a packet containing a Link Layer PDU with a non-zero Length field is sent or received. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [supervision\_timeout](#aca0897d00a1dd1735dbbaf5bfde711ed) |
|  | Connection Supervision timeout (N \* 10 ms). |

## Detailed Description

Connection subrating parameters for LE connections.

## Field Documentation

## [◆ ](#a978cef5f2f14a5a7fe7ded09c6fdf2d9)continuation\_number

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_subrate\_param::continuation\_number |
| --- |

Minimum number of underlying connection events to remain active after a packet containing a Link Layer PDU with a non-zero Length field is sent or received.

## [◆ ](#a15d05324708ddeea8d2f3515eea396bb)max\_latency

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_subrate\_param::max\_latency |
| --- |

Maximum Peripheral latency in units of subrated connection intervals.

## [◆ ](#a59d2d244e3568b8f97ce936121d41b1a)subrate\_max

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_subrate\_param::subrate\_max |
| --- |

Maximum subrate factor.

## [◆ ](#aef75fec8ba8c9987d55e81aa2539b96e)subrate\_min

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_subrate\_param::subrate\_min |
| --- |

Minimum subrate factor.

## [◆ ](#aca0897d00a1dd1735dbbaf5bfde711ed)supervision\_timeout

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_subrate\_param::supervision\_timeout |
| --- |

Connection Supervision timeout (N \* 10 ms).

If using [bt\_conn\_le\_subrate\_set\_defaults](group__bt__conn.md#gac7bb456c530c7e08b4fa9f4d478fdaf9 "bt_conn_le_subrate_set_defaults"), this is the maximum supervision timeout allowed in requests by a peripheral.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_le\_subrate\_param](structbt__conn__le__subrate__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
