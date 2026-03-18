---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structsensor__three__axis__data_1_1sensor__three__axis__sample__data.html
original_path: doxygen/html/structsensor__three__axis__data_1_1sensor__three__axis__sample__data.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor\_three\_axis\_data::sensor\_three\_axis\_sample\_data Struct Reference

`#include <[sensor_data_types.h](sensor__data__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [timestamp\_delta](#a62dd4febada1d6b0b0fad600747089a2) |
| union { |  |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [values](#aa8a07324f3139a6a34f695927a1d6486) [3] |  |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [v](#aa0de6e1354c259857b2b5a89717a5f9a) [3] |  |
| struct { |  |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [x](#a60a8b323508fb4ececd4c3bdad770525) |  |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [y](#ac78d9fa7e085025f1ccc9f53bf30f3bb) |  |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [z](#a5ef91a336b07c2c3e79ed34afbbf8850) |  |
| } |  |
| }; |  |

## Field Documentation

## [◆ ](#a193b99770e283c803a08db173b457431)[union]

| union { ... } [sensor\_three\_axis\_data::sensor\_three\_axis\_sample\_data](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md) |
| --- |

## [◆ ](#a62dd4febada1d6b0b0fad600747089a2)timestamp\_delta

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sensor\_three\_axis\_data::sensor\_three\_axis\_sample\_data::timestamp\_delta |
| --- |

## [◆ ](#aa0de6e1354c259857b2b5a89717a5f9a)v

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_three\_axis\_data::sensor\_three\_axis\_sample\_data::v[3] |
| --- |

## [◆ ](#aa8a07324f3139a6a34f695927a1d6486)values

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_three\_axis\_data::sensor\_three\_axis\_sample\_data::values[3] |
| --- |

## [◆ ](#a60a8b323508fb4ececd4c3bdad770525)x

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_three\_axis\_data::sensor\_three\_axis\_sample\_data::x |
| --- |

## [◆ ](#ac78d9fa7e085025f1ccc9f53bf30f3bb)y

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_three\_axis\_data::sensor\_three\_axis\_sample\_data::y |
| --- |

## [◆ ](#a5ef91a336b07c2c3e79ed34afbbf8850)z

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_three\_axis\_data::sensor\_three\_axis\_sample\_data::z |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[sensor\_data\_types.h](sensor__data__types_8h_source.md)

- [sensor\_three\_axis\_data](structsensor__three__axis__data.md)
- [sensor\_three\_axis\_sample\_data](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
