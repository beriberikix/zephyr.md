---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structsensor__three__axis__data.html
original_path: doxygen/html/structsensor__three__axis__data.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor\_three\_axis\_data Struct Reference

Data for a sensor channel which reports on three axes.
[More...](#details)

`#include <[sensor_data_types.h](sensor__data__types_8h_source.md)>`

| Data Structures | |
| --- | --- |
| struct | [sensor\_three\_axis\_sample\_data](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md) |

| Data Fields | |
| --- | --- |
| struct [sensor\_data\_header](structsensor__data__header.md) | [header](#a6017fc7964204235e2222c4950f3650a) |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [shift](#ade10fa0bd60d4b31eebed92e564539c5) |
| struct [sensor\_three\_axis\_data::sensor\_three\_axis\_sample\_data](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md) | [readings](#ad1a498b1cc31b18b17e69300749bbbc0) [1] |

## Detailed Description

Data for a sensor channel which reports on three axes.

This is used by:

- :c:enum:[SENSOR\_CHAN\_ACCEL\_X](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934afa9238082f000350530ca77b2f513d4c "Acceleration on the X axis, in m/s^2.")
- :c:enum:[SENSOR\_CHAN\_ACCEL\_Y](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a61c145468f01916c1a547fb38a1be9a8 "Acceleration on the Y axis, in m/s^2.")
- :c:enum:[SENSOR\_CHAN\_ACCEL\_Z](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a78e06bb48cfe06e42829816ad4cb5a0f "Acceleration on the Z axis, in m/s^2.")
- :c:enum:[SENSOR\_CHAN\_ACCEL\_XYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9 "Acceleration on the X, Y and Z axes.")
- :c:enum:[SENSOR\_CHAN\_GYRO\_X](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac5709b77f0eb69972ccc055f927e5015 "Angular velocity around the X axis, in radians/s.")
- :c:enum:[SENSOR\_CHAN\_GYRO\_Y](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4a9533172105fd2e55d96e0122a48847 "Angular velocity around the Y axis, in radians/s.")
- :c:enum:[SENSOR\_CHAN\_GYRO\_Z](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a9b6b9d13cd8d82449823d65779a87a39 "Angular velocity around the Z axis, in radians/s.")
- :c:enum:[SENSOR\_CHAN\_GYRO\_XYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a1d36b89ab3761e9bc86effc839f8db0e "Angular velocity around the X, Y and Z axes.")
- :c:enum:[SENSOR\_CHAN\_MAGN\_X](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a171f37ba152d34f75ff745cb848b3240 "Magnetic field on the X axis, in Gauss.")
- :c:enum:[SENSOR\_CHAN\_MAGN\_Y](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2b4f1764f47428c528447347d7730942 "Magnetic field on the Y axis, in Gauss.")
- :c:enum:[SENSOR\_CHAN\_MAGN\_Z](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2a2115051ded019a57ece5a00f86ea61 "Magnetic field on the Z axis, in Gauss.")
- :c:enum:[SENSOR\_CHAN\_MAGN\_XYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5d1f48466f6f600503af18427fa3da32 "Magnetic field on the X, Y and Z axes.")
- :c:enum:[SENSOR\_CHAN\_POS\_DX](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa00b7a857e33c925c910661a91389517 "Position change on the X axis, in points.")
- :c:enum:[SENSOR\_CHAN\_POS\_DY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a974327ca88ea6d22731cd03afeacef76 "Position change on the Y axis, in points.")
- :c:enum:[SENSOR\_CHAN\_POS\_DZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aeaf49aa075947a160f21ae19cf8c39b9 "Position change on the Z axis, in points.")
- :c:enum:[SENSOR\_CHAN\_POS\_DXYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a81fe5eca365c048c5a112071b7aca740 "Position change on the X, Y and Z axis, in points.")

## Field Documentation

## [◆ ](#a6017fc7964204235e2222c4950f3650a)header

| struct [sensor\_data\_header](structsensor__data__header.md) sensor\_three\_axis\_data::header |
| --- |

## [◆ ](#ad1a498b1cc31b18b17e69300749bbbc0)readings

| struct [sensor\_three\_axis\_data::sensor\_three\_axis\_sample\_data](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md) sensor\_three\_axis\_data::readings[1] |
| --- |

## [◆ ](#ade10fa0bd60d4b31eebed92e564539c5)shift

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) sensor\_three\_axis\_data::shift |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[sensor\_data\_types.h](sensor__data__types_8h_source.md)

- [sensor\_three\_axis\_data](structsensor__three__axis__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
