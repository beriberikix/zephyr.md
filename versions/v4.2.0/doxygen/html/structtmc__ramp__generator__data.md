---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structtmc__ramp__generator__data.html
original_path: doxygen/html/structtmc__ramp__generator__data.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tmc\_ramp\_generator\_data Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Stepper Driver Interface](group__stepper__interface.md) » [Trinamic Stepper Controller Interface](group__trinamic__stepper__interface.md)

Trinamic Stepper Ramp Generator data.
[More...](#details)

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [vstart](#a6b861b90bb7e4c637b21b7809608152f) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [v1](#ae9377878720cc03760d207b750997997) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [vmax](#a54558710f19a1781bbec3dc857cb8fcf) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [a1](#aff69cc918c9ed7e067d728a936b9a5f0) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [amax](#a277403bbb0bbc8a7562bf7b6c3e22333) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [d1](#a8672451e2bff4af7f13b72f8a4bc4ed1) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [dmax](#a34bc24f327a5c1a6315fa4869c5418df) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [vstop](#a5f4a921ae3ba0fec18633e659ad42573) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [tzerowait](#ad3846d55690f835623fceca620ec3b23) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [iholdrun](#acd7d7b5170ce3ce8839272ecc4dccd52) |
| union { |  |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [vcoolthrs](#a522f3c11bcac25852a0d7088795f46bd) |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [vhigh](#a5ee17564fb78bbbfd1097c6b440bd30c) |  |
| } |  |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [tpowerdown](#a3b7d2176725aef71e12950fde1ae3ee0) |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [tpwmthrs](#a94352ae1924cbc900545065c7302379b) |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [tcoolthrs](#a871cb11fb3d1aacfd29b85f8ea42b502) |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [thigh](#a8045473482ca1272a75e99938564a700) |  |
| } |  |
| }; |  |

## Detailed Description

Trinamic Stepper Ramp Generator data.

## Field Documentation

## [◆ ](#ab28bf0fcbf81b68c0cf775f79e57856a)[union]

| union { ... } [tmc\_ramp\_generator\_data](structtmc__ramp__generator__data.md) |
| --- |

## [◆ ](#aff69cc918c9ed7e067d728a936b9a5f0)a1

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tmc\_ramp\_generator\_data::a1 |
| --- |

## [◆ ](#a277403bbb0bbc8a7562bf7b6c3e22333)amax

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tmc\_ramp\_generator\_data::amax |
| --- |

## [◆ ](#a8672451e2bff4af7f13b72f8a4bc4ed1)d1

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tmc\_ramp\_generator\_data::d1 |
| --- |

## [◆ ](#a34bc24f327a5c1a6315fa4869c5418df)dmax

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tmc\_ramp\_generator\_data::dmax |
| --- |

## [◆ ](#acd7d7b5170ce3ce8839272ecc4dccd52)iholdrun

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tmc\_ramp\_generator\_data::iholdrun |
| --- |

## [◆ ](#a871cb11fb3d1aacfd29b85f8ea42b502)tcoolthrs

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tmc\_ramp\_generator\_data::tcoolthrs |
| --- |

## [◆ ](#a8045473482ca1272a75e99938564a700)thigh

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tmc\_ramp\_generator\_data::thigh |
| --- |

## [◆ ](#a3b7d2176725aef71e12950fde1ae3ee0)tpowerdown

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tmc\_ramp\_generator\_data::tpowerdown |
| --- |

## [◆ ](#a94352ae1924cbc900545065c7302379b)tpwmthrs

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tmc\_ramp\_generator\_data::tpwmthrs |
| --- |

## [◆ ](#ad3846d55690f835623fceca620ec3b23)tzerowait

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tmc\_ramp\_generator\_data::tzerowait |
| --- |

## [◆ ](#ae9377878720cc03760d207b750997997)v1

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tmc\_ramp\_generator\_data::v1 |
| --- |

## [◆ ](#a522f3c11bcac25852a0d7088795f46bd)vcoolthrs

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tmc\_ramp\_generator\_data::vcoolthrs |
| --- |

## [◆ ](#a5ee17564fb78bbbfd1097c6b440bd30c)vhigh

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tmc\_ramp\_generator\_data::vhigh |
| --- |

## [◆ ](#a54558710f19a1781bbec3dc857cb8fcf)vmax

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tmc\_ramp\_generator\_data::vmax |
| --- |

## [◆ ](#a6b861b90bb7e4c637b21b7809608152f)vstart

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tmc\_ramp\_generator\_data::vstart |
| --- |

## [◆ ](#a5f4a921ae3ba0fec18633e659ad42573)vstop

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tmc\_ramp\_generator\_data::vstop |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/stepper/[stepper\_trinamic.h](stepper__trinamic_8h_source.md)

- [tmc\_ramp\_generator\_data](structtmc__ramp__generator__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
