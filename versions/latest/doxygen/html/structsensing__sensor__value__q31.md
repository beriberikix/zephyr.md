---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsensing__sensor__value__q31.html
original_path: doxygen/html/structsensing__sensor__value__q31.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensing\_sensor\_value\_q31 Struct Reference

[Sensing](group__sensing.md) » [Data Types](group__sensing__datatypes.md)

Sensor value data structure for single 1-axis value.
[More...](#details)

`#include <[sensing_datatypes.h](sensing__datatypes_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [sensing\_sensor\_value\_header](structsensing__sensor__value__header.md) | [header](#af3dbde41e764de34d1b2b38800909da9) |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [shift](#a555e1bec3fe6f781fd12c13a097d4f16) |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [timestamp\_delta](#aff3865d5645e7cb53718b4f09b20b162) |  |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [v](#ad3ed83faec34ebce96e57e23aab36101) |  |
| } | [readings](#a94e301bf8a27dfdb0e5e6c2d6540b83b) [1] |

## Detailed Description

Sensor value data structure for single 1-axis value.

struct [sensing\_sensor\_value\_q31](structsensing__sensor__value__q31.md "Sensor value data structure for single 1-axis value.") can be used by SENSING\_SENSOR\_TYPE\_MOTION\_HINGE\_ANGLE sensor q31 version

## Field Documentation

## [◆ ](#af3dbde41e764de34d1b2b38800909da9)header

| struct [sensing\_sensor\_value\_header](structsensing__sensor__value__header.md) sensing\_sensor\_value\_q31::header |
| --- |

## [◆ ](#a94e301bf8a27dfdb0e5e6c2d6540b83b)[struct]

| struct { ... } sensing\_sensor\_value\_q31::readings[1] |
| --- |

## [◆ ](#a555e1bec3fe6f781fd12c13a097d4f16)shift

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) sensing\_sensor\_value\_q31::shift |
| --- |

## [◆ ](#aff3865d5645e7cb53718b4f09b20b162)timestamp\_delta

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sensing\_sensor\_value\_q31::timestamp\_delta |
| --- |

## [◆ ](#ad3ed83faec34ebce96e57e23aab36101)v

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensing\_sensor\_value\_q31::v |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/sensing/[sensing\_datatypes.h](sensing__datatypes_8h_source.md)

- [sensing\_sensor\_value\_q31](structsensing__sensor__value__q31.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
