---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsensing__sensor__value__3d__q31.html
original_path: doxygen/html/structsensing__sensor__value__3d__q31.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensing\_sensor\_value\_3d\_q31 Struct Reference

[Sensing](group__sensing.md) » [Data Types](group__sensing__datatypes.md)

Sensor value data structure types based on common data types.
[More...](#details)

`#include <[sensing_datatypes.h](sensing__datatypes_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [sensing\_sensor\_value\_header](structsensing__sensor__value__header.md) | [header](#a163e62d50de3b5f61688ff9b00db0dcd) |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [shift](#af0db9faee6eaabff7f9c2f955873378b) |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [timestamp\_delta](#a1bf323a7bb69af0801acebfe03e35b7a) |  |
| union { |  |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [v](#a68eefb9ba2e8d954e8ea3c4f30893f3f) [3] |  |
| struct { |  |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [x](#ad1d2f43d1a9a4b5333ac1b8531d6c94c) |  |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [y](#a721b9cd33e360691b9fb07a90c3f4df2) |  |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [z](#abbf0f5aaae8978eba1e5f3e2ffad20d0) |  |
| } |  |
| } |  |
| } | [readings](#aea782e09d486595b5fbd7a94f3bde253) [1] |

## Detailed Description

Sensor value data structure types based on common data types.

Suitable for common sensors, such as IMU, Light sensors and orientation sensors.

Sensor value data structure for 3-axis sensors. struct [sensing\_sensor\_value\_3d\_q31](structsensing__sensor__value__3d__q31.md "Sensor value data structure types based on common data types.") can be used by 3D IMU sensors like: SENSING\_SENSOR\_TYPE\_MOTION\_ACCELEROMETER\_3D, SENSING\_SENSOR\_TYPE\_MOTION\_UNCALIB\_ACCELEROMETER\_3D, SENSING\_SENSOR\_TYPE\_MOTION\_GYROMETER\_3D, q31 version

## Field Documentation

## [◆ ](#a163e62d50de3b5f61688ff9b00db0dcd)header

| struct [sensing\_sensor\_value\_header](structsensing__sensor__value__header.md) sensing\_sensor\_value\_3d\_q31::header |
| --- |

## [◆ ](#aea782e09d486595b5fbd7a94f3bde253)[struct]

| struct { ... } sensing\_sensor\_value\_3d\_q31::readings[1] |
| --- |

## [◆ ](#af0db9faee6eaabff7f9c2f955873378b)shift

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) sensing\_sensor\_value\_3d\_q31::shift |
| --- |

## [◆ ](#a1bf323a7bb69af0801acebfe03e35b7a)timestamp\_delta

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sensing\_sensor\_value\_3d\_q31::timestamp\_delta |
| --- |

## [◆ ](#a68eefb9ba2e8d954e8ea3c4f30893f3f)v

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensing\_sensor\_value\_3d\_q31::v[3] |
| --- |

## [◆ ](#ad1d2f43d1a9a4b5333ac1b8531d6c94c)x

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensing\_sensor\_value\_3d\_q31::x |
| --- |

## [◆ ](#a721b9cd33e360691b9fb07a90c3f4df2)y

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensing\_sensor\_value\_3d\_q31::y |
| --- |

## [◆ ](#abbf0f5aaae8978eba1e5f3e2ffad20d0)z

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensing\_sensor\_value\_3d\_q31::z |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/sensing/[sensing\_datatypes.h](sensing__datatypes_8h_source.md)

- [sensing\_sensor\_value\_3d\_q31](structsensing__sensor__value__3d__q31.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
