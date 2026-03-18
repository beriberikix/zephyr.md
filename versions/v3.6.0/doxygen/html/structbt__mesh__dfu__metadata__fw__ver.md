---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__mesh__dfu__metadata__fw__ver.html
original_path: doxygen/html/structbt__mesh__dfu__metadata__fw__ver.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_dfu\_metadata\_fw\_ver Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh Device Firmware Update](group__bt__mesh__dfu.md) » [Bluetooth Mesh Device Firmware Update (DFU) metadata](group__bt__mesh__dfu__metadata.md)

Firmware version.
[More...](#details)

`#include <[dfu_metadata.h](dfu__metadata_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [major](#ad4bcde436cbf014cf24fa84888408cc1) |
|  | Firmware major version. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [minor](#a3386d56c363d631e4b4e77ea49bd9e8d) |
|  | Firmware minor version. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [revision](#aadeed181c571412b42fbad8111f0d53d) |
|  | Firmware revision. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [build\_num](#a7c21ae9b7340a1f13d107bf31aeeca90) |
|  | Firmware build number. |

## Detailed Description

Firmware version.

## Field Documentation

## [◆ ](#a7c21ae9b7340a1f13d107bf31aeeca90)build\_num

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_dfu\_metadata\_fw\_ver::build\_num |
| --- |

Firmware build number.

## [◆ ](#ad4bcde436cbf014cf24fa84888408cc1)major

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dfu\_metadata\_fw\_ver::major |
| --- |

Firmware major version.

## [◆ ](#a3386d56c363d631e4b4e77ea49bd9e8d)minor

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dfu\_metadata\_fw\_ver::minor |
| --- |

Firmware minor version.

## [◆ ](#aadeed181c571412b42fbad8111f0d53d)revision

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_dfu\_metadata\_fw\_ver::revision |
| --- |

Firmware revision.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[dfu\_metadata.h](dfu__metadata_8h_source.md)

- [bt\_mesh\_dfu\_metadata\_fw\_ver](structbt__mesh__dfu__metadata__fw__ver.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
