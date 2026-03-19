---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structpcie__ctrl__driver__api.html
original_path: doxygen/html/structpcie__ctrl__driver__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pcie\_ctrl\_driver\_api Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [PCI Express Controller Interface](group__pcie__controller__interface.md)

Structure providing callbacks to be implemented for devices that supports the PCI Express Controller API.
[More...](#details)

`#include <[controller.h](drivers_2pcie_2controller_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [pcie\_ctrl\_conf\_read\_t](group__pcie__controller__interface.md#gac3d0f7e90bcc30996ce23324d2d7356a) | [conf\_read](#a20c1faf02c71e88da165c889550a76ae) |
| [pcie\_ctrl\_conf\_write\_t](group__pcie__controller__interface.md#ga3241acc7de4af2b73cf3f47a25349109) | [conf\_write](#a46fa0fd3a759fe2dc960546b49c53979) |
| [pcie\_ctrl\_region\_allocate\_t](group__pcie__controller__interface.md#ga62ce18e7495256c148168b773eabd37d) | [region\_allocate](#a46191bf9aad7ab7ac1319918873b8b29) |
| [pcie\_ctrl\_region\_get\_allocate\_base\_t](group__pcie__controller__interface.md#gaa9d5bd27c841e36f65e65dec0b057e9a) | [region\_get\_allocate\_base](#a5d7687cd738bd86a785fc281781d2759) |
| [pcie\_ctrl\_region\_translate\_t](group__pcie__controller__interface.md#gab144356b1c3ec3754aae0008634f2d2f) | [region\_translate](#a71a4d13492bb3098bdb2c0e0ff7b94cf) |

## Detailed Description

Structure providing callbacks to be implemented for devices that supports the PCI Express Controller API.

## Field Documentation

## [◆ ](#a20c1faf02c71e88da165c889550a76ae)conf\_read

| [pcie\_ctrl\_conf\_read\_t](group__pcie__controller__interface.md#gac3d0f7e90bcc30996ce23324d2d7356a) pcie\_ctrl\_driver\_api::conf\_read |
| --- |

## [◆ ](#a46fa0fd3a759fe2dc960546b49c53979)conf\_write

| [pcie\_ctrl\_conf\_write\_t](group__pcie__controller__interface.md#ga3241acc7de4af2b73cf3f47a25349109) pcie\_ctrl\_driver\_api::conf\_write |
| --- |

## [◆ ](#a46191bf9aad7ab7ac1319918873b8b29)region\_allocate

| [pcie\_ctrl\_region\_allocate\_t](group__pcie__controller__interface.md#ga62ce18e7495256c148168b773eabd37d) pcie\_ctrl\_driver\_api::region\_allocate |
| --- |

## [◆ ](#a5d7687cd738bd86a785fc281781d2759)region\_get\_allocate\_base

| [pcie\_ctrl\_region\_get\_allocate\_base\_t](group__pcie__controller__interface.md#gaa9d5bd27c841e36f65e65dec0b057e9a) pcie\_ctrl\_driver\_api::region\_get\_allocate\_base |
| --- |

## [◆ ](#a71a4d13492bb3098bdb2c0e0ff7b94cf)region\_translate

| [pcie\_ctrl\_region\_translate\_t](group__pcie__controller__interface.md#gab144356b1c3ec3754aae0008634f2d2f) pcie\_ctrl\_driver\_api::region\_translate |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/pcie/[controller.h](drivers_2pcie_2controller_8h_source.md)

- [pcie\_ctrl\_driver\_api](structpcie__ctrl__driver__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
