---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__iso__accept__info.html
original_path: doxygen/html/structbt__iso__accept__info.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_iso\_accept\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Isochronous channels (ISO)](group__bt__iso.md)

ISO Accept Info Structure.
[More...](#details)

`#include <[iso.h](iso_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct bt\_conn \* | [acl](#a4225ccc90f1e17e26ce61fe398f506d1) |
|  | The ACL connection that is requesting authorization. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cig\_id](#a88002043a67c89c8d518ebdf92cf8847) |
|  | The ID of the connected isochronous group (CIG) on the central. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cis\_id](#a688809132997c37a6fe2529498a4ee0e) |
|  | The ID of the connected isochronous stream (CIS) on the central. |

## Detailed Description

ISO Accept Info Structure.

## Field Documentation

## [◆ ](#a4225ccc90f1e17e26ce61fe398f506d1)acl

| struct bt\_conn\* bt\_iso\_accept\_info::acl |
| --- |

The ACL connection that is requesting authorization.

## [◆ ](#a88002043a67c89c8d518ebdf92cf8847)cig\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_accept\_info::cig\_id |
| --- |

The ID of the connected isochronous group (CIG) on the central.

The ID is unique per ACL

## [◆ ](#a688809132997c37a6fe2529498a4ee0e)cis\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_accept\_info::cis\_id |
| --- |

The ID of the connected isochronous stream (CIS) on the central.

This ID is unique within a CIG

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[iso.h](iso_8h_source.md)

- [bt\_iso\_accept\_info](structbt__iso__accept__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
