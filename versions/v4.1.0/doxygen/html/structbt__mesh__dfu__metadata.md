---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__mesh__dfu__metadata.html
original_path: doxygen/html/structbt__mesh__dfu__metadata.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_dfu\_metadata Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh Device Firmware Update](group__bt__mesh__dfu.md) » [Bluetooth Mesh Device Firmware Update (DFU) metadata](group__bt__mesh__dfu__metadata.md)

Firmware metadata.
[More...](#details)

`#include <[dfu_metadata.h](dfu__metadata_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_mesh\_dfu\_metadata\_fw\_ver](structbt__mesh__dfu__metadata__fw__ver.md) | [fw\_ver](#a48a680b1c3a802e15d4212865fa1d0df) |
|  | New firmware version. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [fw\_size](#a624e2e30f31d2d2f2554eb22c6950ebc) |
|  | New firmware size. |
| enum [bt\_mesh\_dfu\_metadata\_fw\_core\_type](group__bt__mesh__dfu__metadata.md#gaec5fa6e61a6ae88ac7a14f1ec09585b8) | [fw\_core\_type](#a82719aefc21e1fac5a6e8813af23e131) |
|  | New firmware core type. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [comp\_hash](#af4d02eeccb2537b81738ffd186c7d9ed) |
|  | Hash of incoming Composition Data. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [elems](#ac487e125632b55b8477f648759dbbba0) |
|  | New number of node elements. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [user\_data](#ac3e6dd2b069785ae359d49162d33e104) |
|  | Application-specific data for new firmware. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [user\_data\_len](#ae4853b55fda6ec8c4c8609d5648890ab) |
|  | Length of the application-specific field. |

## Detailed Description

Firmware metadata.

## Field Documentation

## [◆ ](#af4d02eeccb2537b81738ffd186c7d9ed)comp\_hash

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_dfu\_metadata::comp\_hash |
| --- |

Hash of incoming Composition Data.

## [◆ ](#ac487e125632b55b8477f648759dbbba0)elems

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_dfu\_metadata::elems |
| --- |

New number of node elements.

## [◆ ](#a82719aefc21e1fac5a6e8813af23e131)fw\_core\_type

| enum [bt\_mesh\_dfu\_metadata\_fw\_core\_type](group__bt__mesh__dfu__metadata.md#gaec5fa6e61a6ae88ac7a14f1ec09585b8) bt\_mesh\_dfu\_metadata::fw\_core\_type |
| --- |

New firmware core type.

## [◆ ](#a624e2e30f31d2d2f2554eb22c6950ebc)fw\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_dfu\_metadata::fw\_size |
| --- |

New firmware size.

## [◆ ](#a48a680b1c3a802e15d4212865fa1d0df)fw\_ver

| struct [bt\_mesh\_dfu\_metadata\_fw\_ver](structbt__mesh__dfu__metadata__fw__ver.md) bt\_mesh\_dfu\_metadata::fw\_ver |
| --- |

New firmware version.

## [◆ ](#ac3e6dd2b069785ae359d49162d33e104)user\_data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_mesh\_dfu\_metadata::user\_data |
| --- |

Application-specific data for new firmware.

This field is optional.

## [◆ ](#ae4853b55fda6ec8c4c8609d5648890ab)user\_data\_len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_dfu\_metadata::user\_data\_len |
| --- |

Length of the application-specific field.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[dfu\_metadata.h](dfu__metadata_8h_source.md)

- [bt\_mesh\_dfu\_metadata](structbt__mesh__dfu__metadata.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
