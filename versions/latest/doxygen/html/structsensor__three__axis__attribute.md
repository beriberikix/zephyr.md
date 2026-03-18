---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsensor__three__axis__attribute.html
original_path: doxygen/html/structsensor__three__axis__attribute.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor\_three\_axis\_attribute Struct Reference

Used by the following channel/attribute pairs:
[More...](#details)

`#include <[sensor_attribute_types.h](sensor__attribute__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [shift](#a230f8021356406c3225868d43e39be18) |
| union { |  |
| struct { |  |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [x](#a82ee018216949a3132fcdf165e63d2be) |  |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [y](#a5c1bd40fb615aa6515c10ff249bae0c2) |  |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [z](#afee1c9c4fc2b18fb5ae7f6a69af6e2e9) |  |
| } |  |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [values](#a88cb3f5259b9dde34c5b26daae4ed270) [3] |  |
| }; |  |

## Detailed Description

Used by the following channel/attribute pairs:

- SENSOR\_CHAN\_ACCEL\_XYZ
  - SENSOR\_ATTR\_OFFSET
- SENSOR\_CHAN\_GYRO\_XYZ
  - SENSOR\_ATTR\_OFFSET
- SENSOR\_CHAN\_MAGN\_XYZ
  - SENSOR\_ATTR\_OFFSET

## Field Documentation

## [◆ ](#abf2ad5c8026b94c5632bdaab099362c6)[union]

| union { ... } [sensor\_three\_axis\_attribute](structsensor__three__axis__attribute.md) |
| --- |

## [◆ ](#a230f8021356406c3225868d43e39be18)shift

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) sensor\_three\_axis\_attribute::shift |
| --- |

## [◆ ](#a88cb3f5259b9dde34c5b26daae4ed270)values

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_three\_axis\_attribute::values[3] |
| --- |

## [◆ ](#a82ee018216949a3132fcdf165e63d2be)x

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_three\_axis\_attribute::x |
| --- |

## [◆ ](#a5c1bd40fb615aa6515c10ff249bae0c2)y

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_three\_axis\_attribute::y |
| --- |

## [◆ ](#afee1c9c4fc2b18fb5ae7f6a69af6e2e9)z

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_three\_axis\_attribute::z |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[sensor\_attribute\_types.h](sensor__attribute__types_8h_source.md)

- [sensor\_three\_axis\_attribute](structsensor__three__axis__attribute.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
