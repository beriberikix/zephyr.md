---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__conn__le__subrating__info.html
original_path: doxygen/html/structbt__conn__le__subrating__info.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_le\_subrating\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

Subrating information for LE connections.
[More...](#details)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [factor](#a23736535309f38695a2e432c5c80bbe1) |
|  | Connection subrate factor. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [continuation\_number](#a0a6d1eae73f76382f1a9415c01761c19) |
|  | Number of underlying connection events to remain active after a packet containing a Link Layer PDU with a non-zero Length field is sent or received. |

## Detailed Description

Subrating information for LE connections.

## Field Documentation

## [◆ ](#a0a6d1eae73f76382f1a9415c01761c19)continuation\_number

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_subrating\_info::continuation\_number |
| --- |

Number of underlying connection events to remain active after a packet containing a Link Layer PDU with a non-zero Length field is sent or received.

## [◆ ](#a23736535309f38695a2e432c5c80bbe1)factor

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_subrating\_info::factor |
| --- |

Connection subrate factor.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_le\_subrating\_info](structbt__conn__le__subrating__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
