---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structpinctrl__soc__pin.html
original_path: doxygen/html/structpinctrl__soc__pin.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl\_soc\_pin Struct Reference

Type for R-Car pin.
[More...](#details)

`#include <[pinctrl_rcar_common.h](pinctrl__rcar__common_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [pin](#a0a2ceae237c3321a4ce1a3dd7a031322) |
| struct [rcar\_pin\_func](structrcar__pin__func.md) | [func](#aa1e68145488d654ab03e114c3f9949a9) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#a8e7c595f1e24e227da45a2b5d5fad501) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [drive\_strength](#a0784ff8fd0192c54997ab5841153c82b) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [voltage](#a37e11e6cc80fdd3cedbbbee555e062ae) |

## Detailed Description

Type for R-Car pin.

## Field Documentation

## [◆ ](#a0784ff8fd0192c54997ab5841153c82b)drive\_strength

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pinctrl\_soc\_pin::drive\_strength |
| --- |

## [◆ ](#a8e7c595f1e24e227da45a2b5d5fad501)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pinctrl\_soc\_pin::flags |
| --- |

## [◆ ](#aa1e68145488d654ab03e114c3f9949a9)func

| struct [rcar\_pin\_func](structrcar__pin__func.md) pinctrl\_soc\_pin::func |
| --- |

## [◆ ](#a0a2ceae237c3321a4ce1a3dd7a031322)pin

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pinctrl\_soc\_pin::pin |
| --- |

## [◆ ](#a37e11e6cc80fdd3cedbbbee555e062ae)voltage

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pinctrl\_soc\_pin::voltage |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/pinctrl/[pinctrl\_rcar\_common.h](pinctrl__rcar__common_8h_source.md)

- [pinctrl\_soc\_pin](structpinctrl__soc__pin.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
