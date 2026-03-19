---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__comp2__record.html
original_path: doxygen/html/structbt__mesh__comp2__record.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_comp2\_record Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Access layer](group__bt__mesh__access.md)

Composition data page 2 record.
[More...](#details)

`#include <[access.h](access_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [id](#a19ce94025c1c8079ca2789bbcd09b00e) |
|  | Mesh profile ID. |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [x](#a5f25c33170c77375f6492ad3cc0feaac) |  |
|  | Major version. [More...](#a5f25c33170c77375f6492ad3cc0feaac) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [y](#a4970a0757c34ab97697c69728b564df6) |  |
|  | Minor version. [More...](#a4970a0757c34ab97697c69728b564df6) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [z](#ac3cabce01490191f145234f386b9b119) |  |
|  | Z version. [More...](#ac3cabce01490191f145234f386b9b119) |
| } | [version](#a26370a5dc68af03424c0f2f4fecd0181) |
|  | Mesh Profile Version. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [elem\_offset\_cnt](#ad13066e9d6d32e8e2eab64881249eb7e) |
|  | Element offset count. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [elem\_offset](#a6f81d99a62252cd26d87ca4fb289bdf9) |
|  | Element offset list. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [data\_len](#abdc488e846233fa05f0fc48f4081576e) |
|  | Length of additional data. |
| const void \* | [data](#acd5f5770a6606ad00fa0815e4866ec4e) |
|  | Additional data. |

## Detailed Description

Composition data page 2 record.

## Field Documentation

## [◆ ](#acd5f5770a6606ad00fa0815e4866ec4e)data

| const void\* bt\_mesh\_comp2\_record::data |
| --- |

Additional data.

## [◆ ](#abdc488e846233fa05f0fc48f4081576e)data\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_comp2\_record::data\_len |
| --- |

Length of additional data.

## [◆ ](#a6f81d99a62252cd26d87ca4fb289bdf9)elem\_offset

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_mesh\_comp2\_record::elem\_offset |
| --- |

Element offset list.

## [◆ ](#ad13066e9d6d32e8e2eab64881249eb7e)elem\_offset\_cnt

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_comp2\_record::elem\_offset\_cnt |
| --- |

Element offset count.

## [◆ ](#a19ce94025c1c8079ca2789bbcd09b00e)id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_comp2\_record::id |
| --- |

Mesh profile ID.

## [◆ ](#a26370a5dc68af03424c0f2f4fecd0181)[struct]

| struct { ... } bt\_mesh\_comp2\_record::version |
| --- |

Mesh Profile Version.

## [◆ ](#a5f25c33170c77375f6492ad3cc0feaac)x

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_comp2\_record::x |
| --- |

Major version.

## [◆ ](#a4970a0757c34ab97697c69728b564df6)y

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_comp2\_record::y |
| --- |

Minor version.

## [◆ ](#ac3cabce01490191f145234f386b9b119)z

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_comp2\_record::z |
| --- |

Z version.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[access.h](access_8h_source.md)

- [bt\_mesh\_comp2\_record](structbt__mesh__comp2__record.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
