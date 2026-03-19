---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structi3c__ccc__deftgts__active__controller.html
original_path: doxygen/html/structi3c__ccc__deftgts__active__controller.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_ccc\_deftgts\_active\_controller Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C Common Command Codes](group__i3c__ccc.md)

The active controller part of payload for DEFTGTS CCC.
[More...](#details)

`#include <[ccc.h](ccc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [addr](#a4d7671db542bb70ef623be26804c154a) |
|  | Dynamic Address of Active Controller. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [dcr](#a7acd12fad49f565a6b8a71993b6ad5d4) |
|  | Device Characteristic Register of Active Controller. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bcr](#aeb56808d9b998c51d5b30307e0212328) |
|  | Bus Characteristic Register of Active Controller. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [static\_addr](#ae2fb1ebc28ef1f69c6114af0b25875d3) |
|  | Static Address of Active Controller. |

## Detailed Description

The active controller part of payload for DEFTGTS CCC.

This is used by DEFTGTS (Define List of Targets) CCC to describe the active controller on the I3C bus.

## Field Documentation

## [◆ ](#a4d7671db542bb70ef623be26804c154a)addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_deftgts\_active\_controller::addr |
| --- |

Dynamic Address of Active Controller.

## [◆ ](#aeb56808d9b998c51d5b30307e0212328)bcr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_deftgts\_active\_controller::bcr |
| --- |

Bus Characteristic Register of Active Controller.

## [◆ ](#a7acd12fad49f565a6b8a71993b6ad5d4)dcr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_deftgts\_active\_controller::dcr |
| --- |

Device Characteristic Register of Active Controller.

## [◆ ](#ae2fb1ebc28ef1f69c6114af0b25875d3)static\_addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_deftgts\_active\_controller::static\_addr |
| --- |

Static Address of Active Controller.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/i3c/[ccc.h](ccc_8h_source.md)

- [i3c\_ccc\_deftgts\_active\_controller](structi3c__ccc__deftgts__active__controller.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
