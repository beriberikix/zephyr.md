---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structtisci__version__info.html
original_path: doxygen/html/structtisci__version__info.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tisci\_version\_info Struct Reference

version information structure
[More...](#details)

`#include <[zephyr/drivers/firmware/tisci/tisci.h](tisci_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [abi\_major](#a7371d69f5f0993dfd1e582c165d2ddc5) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [abi\_minor](#a8547f04843609b8a324ea4ecb91c17a7) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [firmware\_revision](#a711c9ca4b063958fcb46ad0e298caa27) |
| char | [firmware\_description](#a62cb5c8e86a94dbf53430d73c9f241a9) [32] |

## Detailed Description

version information structure

Parameters
:   | [abi\_major](#a7371d69f5f0993dfd1e582c165d2ddc5) | Major ABI version. Change here implies risk of backward compatibility break. |
    | --- | --- |
    | [abi\_minor](#a8547f04843609b8a324ea4ecb91c17a7) | Minor ABI version. Change here implies new feature addition, or compatible change in ABI. |
    | [firmware\_revision](#a711c9ca4b063958fcb46ad0e298caa27) | Firmware revision (not usually used). |
    | [firmware\_description](#a62cb5c8e86a94dbf53430d73c9f241a9) | Firmware description (not usually used). |

## Field Documentation

## [◆ ](#a7371d69f5f0993dfd1e582c165d2ddc5)abi\_major

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_version\_info::abi\_major |
| --- |

## [◆ ](#a8547f04843609b8a324ea4ecb91c17a7)abi\_minor

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_version\_info::abi\_minor |
| --- |

## [◆ ](#a62cb5c8e86a94dbf53430d73c9f241a9)firmware\_description

| char tisci\_version\_info::firmware\_description[32] |
| --- |

## [◆ ](#a711c9ca4b063958fcb46ad0e298caa27)firmware\_revision

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_version\_info::firmware\_revision |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/firmware/tisci/[tisci.h](tisci_8h_source.md)

- [tisci\_version\_info](structtisci__version__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
