---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__cts__time__format.html
original_path: doxygen/html/structbt__cts__time__format.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cts\_time\_format Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Current Time Service (CTS)](group__bt__cts.md)

Current Time service data format, Please refer to specifications for more details.
[More...](#details)

`#include <[cts.h](cts_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [year](#ad5ab55fcb3e1dbaa73ba4ecb78d6b47e) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mon](#a079a1c49698b6e9cb84291acdd1cf687) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mday](#a408a2b777d10b536dbdfeca1b8335e6b) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [hours](#ab592c89e81e5cb43724affd3ce2b5768) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [min](#a299d6432d9b44b0de0be9c130733eb69) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sec](#ae0ccd07b2a280888f3881f0d2fc2add6) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [wday](#ae696cbbd3a785c1df6d54ce771f1d7a2) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [fractions256](#af601779a164440fe95c0dcbd7a3d7e60) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [reason](#a3482e00650e9e9a63816709c82a1aa07) |

## Detailed Description

Current Time service data format, Please refer to specifications for more details.

## Field Documentation

## [◆ ](#af601779a164440fe95c0dcbd7a3d7e60)fractions256

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_cts\_time\_format::fractions256 |
| --- |

## [◆ ](#ab592c89e81e5cb43724affd3ce2b5768)hours

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_cts\_time\_format::hours |
| --- |

## [◆ ](#a408a2b777d10b536dbdfeca1b8335e6b)mday

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_cts\_time\_format::mday |
| --- |

## [◆ ](#a299d6432d9b44b0de0be9c130733eb69)min

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_cts\_time\_format::min |
| --- |

## [◆ ](#a079a1c49698b6e9cb84291acdd1cf687)mon

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_cts\_time\_format::mon |
| --- |

## [◆ ](#a3482e00650e9e9a63816709c82a1aa07)reason

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_cts\_time\_format::reason |
| --- |

## [◆ ](#ae0ccd07b2a280888f3881f0d2fc2add6)sec

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_cts\_time\_format::sec |
| --- |

## [◆ ](#ae696cbbd3a785c1df6d54ce771f1d7a2)wday

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_cts\_time\_format::wday |
| --- |

## [◆ ](#ad5ab55fcb3e1dbaa73ba4ecb78d6b47e)year

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_cts\_time\_format::year |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/services/[cts.h](cts_8h_source.md)

- [bt\_cts\_time\_format](structbt__cts__time__format.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
