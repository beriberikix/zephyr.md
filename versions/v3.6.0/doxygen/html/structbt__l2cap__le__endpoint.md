---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__l2cap__le__endpoint.html
original_path: doxygen/html/structbt__l2cap__le__endpoint.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_l2cap\_le\_endpoint Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [L2CAP](group__bt__l2cap.md)

LE L2CAP Endpoint structure.
[More...](#details)

`#include <[l2cap.h](l2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [cid](#aeee85135541b17bede098891b820c63f) |
|  | Endpoint Channel Identifier (CID). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [mtu](#a598f0c7f0ad4cc029013358d35ce9dc2) |
|  | Endpoint Maximum Transmission Unit. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [mps](#aa9e4f21e48eda61a3d0b777ee13c2599) |
|  | Endpoint Maximum PDU payload Size. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [init\_credits](#a834561b4a8857253bdfc3d0d2c1033f5) |
|  | Endpoint initial credits. |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [credits](#ab3f475c383791731c595845c80c27edf) |
|  | Endpoint credits. |

## Detailed Description

LE L2CAP Endpoint structure.

## Field Documentation

## [◆ ](#aeee85135541b17bede098891b820c63f)cid

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_le\_endpoint::cid |
| --- |

Endpoint Channel Identifier (CID).

## [◆ ](#ab3f475c383791731c595845c80c27edf)credits

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) bt\_l2cap\_le\_endpoint::credits |
| --- |

Endpoint credits.

## [◆ ](#a834561b4a8857253bdfc3d0d2c1033f5)init\_credits

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_le\_endpoint::init\_credits |
| --- |

Endpoint initial credits.

## [◆ ](#aa9e4f21e48eda61a3d0b777ee13c2599)mps

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_le\_endpoint::mps |
| --- |

Endpoint Maximum PDU payload Size.

## [◆ ](#a598f0c7f0ad4cc029013358d35ce9dc2)mtu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_le\_endpoint::mtu |
| --- |

Endpoint Maximum Transmission Unit.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[l2cap.h](l2cap_8h_source.md)

- [bt\_l2cap\_le\_endpoint](structbt__l2cap__le__endpoint.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
