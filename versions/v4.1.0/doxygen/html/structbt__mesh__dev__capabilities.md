---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__mesh__dev__capabilities.html
original_path: doxygen/html/structbt__mesh__dev__capabilities.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_dev\_capabilities Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Provisioning](group__bt__mesh__prov.md)

Device Capabilities.
[More...](#details)

`#include <[main.h](main_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [elem\_count](#acfef4ecf5ca9324ddc584b9cb910bfe0) |
|  | Number of elements supported by the device. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [algorithms](#a762786d98c070d0ae79e09f22bad4b33) |
|  | Supported algorithms and other capabilities. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pub\_key\_type](#a7f549f5b3923c0b4249e1b21368ee857) |
|  | Supported public key types. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [oob\_type](#a744703091988432baa14a84347309bcf) |
|  | Supported OOB Types. |
| [bt\_mesh\_output\_action\_t](group__bt__mesh__prov.md#ga5512b81ef7eeb45b0a12ef62234c8795) | [output\_actions](#a359caeaf64f45783b0c576ef8ef14975) |
|  | Supported Output OOB Actions. |
| [bt\_mesh\_input\_action\_t](group__bt__mesh__prov.md#gaf71f3dbdef6b8c085e9a4f068e1f60c5) | [input\_actions](#a6132c85094980f839cf9dca57d7969ea) |
|  | Supported Input OOB Actions. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [output\_size](#a59c959cbd8b1a2aa4e548e7f990cf1f4) |
|  | Maximum size of Output OOB supported. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [input\_size](#ac9097c4d634683120509f4c1ac732928) |
|  | Maximum size in octets of Input OOB supported. |

## Detailed Description

Device Capabilities.

## Field Documentation

## [◆ ](#a762786d98c070d0ae79e09f22bad4b33)algorithms

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_dev\_capabilities::algorithms |
| --- |

Supported algorithms and other capabilities.

## [◆ ](#acfef4ecf5ca9324ddc584b9cb910bfe0)elem\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dev\_capabilities::elem\_count |
| --- |

Number of elements supported by the device.

## [◆ ](#a6132c85094980f839cf9dca57d7969ea)input\_actions

| [bt\_mesh\_input\_action\_t](group__bt__mesh__prov.md#gaf71f3dbdef6b8c085e9a4f068e1f60c5) bt\_mesh\_dev\_capabilities::input\_actions |
| --- |

Supported Input OOB Actions.

## [◆ ](#ac9097c4d634683120509f4c1ac732928)input\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dev\_capabilities::input\_size |
| --- |

Maximum size in octets of Input OOB supported.

## [◆ ](#a744703091988432baa14a84347309bcf)oob\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dev\_capabilities::oob\_type |
| --- |

Supported OOB Types.

## [◆ ](#a359caeaf64f45783b0c576ef8ef14975)output\_actions

| [bt\_mesh\_output\_action\_t](group__bt__mesh__prov.md#ga5512b81ef7eeb45b0a12ef62234c8795) bt\_mesh\_dev\_capabilities::output\_actions |
| --- |

Supported Output OOB Actions.

## [◆ ](#a59c959cbd8b1a2aa4e548e7f990cf1f4)output\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dev\_capabilities::output\_size |
| --- |

Maximum size of Output OOB supported.

## [◆ ](#a7f549f5b3923c0b4249e1b21368ee857)pub\_key\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dev\_capabilities::pub\_key\_type |
| --- |

Supported public key types.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[main.h](main_8h_source.md)

- [bt\_mesh\_dev\_capabilities](structbt__mesh__dev__capabilities.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
