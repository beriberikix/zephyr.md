---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__sdp__data__elem.html
original_path: doxygen/html/structbt__sdp__data__elem.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_sdp\_data\_elem Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Service Discovery Protocol (SDP)](group__bt__sdp.md)

SDP Generic Data Element Value.
[More...](#details)

`#include <[sdp.h](sdp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [type](#ac6d5cbc71d1133f30bc20919ffd2d263) |
|  | Type of the data element. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [data\_size](#a88b38121f91d55ca796dedb99b1e18d6) |
|  | Size of the data element. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [total\_size](#a8b7f4943ad968953edb7a3a6f541369b) |
|  | Total size of the data element. |
| const void \* | [data](#a0572a0c34ddf3ba340ee63d28c330dd1) |

## Detailed Description

SDP Generic Data Element Value.

## Field Documentation

## [◆ ](#a0572a0c34ddf3ba340ee63d28c330dd1)data

| const void\* bt\_sdp\_data\_elem::data |
| --- |

## [◆ ](#a88b38121f91d55ca796dedb99b1e18d6)data\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_sdp\_data\_elem::data\_size |
| --- |

Size of the data element.

## [◆ ](#a8b7f4943ad968953edb7a3a6f541369b)total\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_sdp\_data\_elem::total\_size |
| --- |

Total size of the data element.

## [◆ ](#ac6d5cbc71d1133f30bc20919ffd2d263)type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_sdp\_data\_elem::type |
| --- |

Type of the data element.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[sdp.h](sdp_8h_source.md)

- [bt\_sdp\_data\_elem](structbt__sdp__data__elem.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
