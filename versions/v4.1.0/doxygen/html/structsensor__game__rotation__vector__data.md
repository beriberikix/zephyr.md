---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsensor__game__rotation__vector__data.html
original_path: doxygen/html/structsensor__game__rotation__vector__data.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor\_game\_rotation\_vector\_data Struct Reference

Data for a sensor channel which reports game rotation vector data.
[More...](#details)

`#include <[sensor_data_types.h](sensor__data__types_8h_source.md)>`

| Data Structures | |
| --- | --- |
| struct | [sensor\_game\_rotation\_vector\_sample\_data](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md) |

| Data Fields | |
| --- | --- |
| struct [sensor\_data\_header](structsensor__data__header.md) | [header](#abb709edf89ac7dc720a5f307cd1a48bb) |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [shift](#a22817d2c2b6b9e04ab574eb816df5442) |
| struct [sensor\_game\_rotation\_vector\_data::sensor\_game\_rotation\_vector\_sample\_data](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md) | [readings](#acc17463dbd99f1ce4fc6a0c42a6bf0c2) [1] |

## Detailed Description

Data for a sensor channel which reports game rotation vector data.

This is used by:

- :c:enum:[SENSOR\_CHAN\_GAME\_ROTATION\_VECTOR](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a3905467a96940ada0dbdef6ff8ee1a8a "Game Rotation Vector (unit quaternion components X/Y/Z/W).")

## Field Documentation

## [◆ ](#abb709edf89ac7dc720a5f307cd1a48bb)header

| struct [sensor\_data\_header](structsensor__data__header.md) sensor\_game\_rotation\_vector\_data::header |
| --- |

## [◆ ](#acc17463dbd99f1ce4fc6a0c42a6bf0c2)readings

| struct [sensor\_game\_rotation\_vector\_data::sensor\_game\_rotation\_vector\_sample\_data](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md) sensor\_game\_rotation\_vector\_data::readings[1] |
| --- |

## [◆ ](#a22817d2c2b6b9e04ab574eb816df5442)shift

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) sensor\_game\_rotation\_vector\_data::shift |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[sensor\_data\_types.h](sensor__data__types_8h_source.md)

- [sensor\_game\_rotation\_vector\_data](structsensor__game__rotation__vector__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
