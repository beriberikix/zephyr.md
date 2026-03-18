---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structsensing__sensor__value__header.html
original_path: doxygen/html/structsensing__sensor__value__header.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensing\_sensor\_value\_header Struct Reference

[Sensing](group__sensing.md) » [Data Types](group__sensing__datatypes.md)

sensor value header
[More...](#details)

`#include <[sensing_datatypes.h](sensing__datatypes_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [base\_timestamp](#aa8efbfd682535deca1172cb192c1a86c) |
|  | Base timestamp of this data readings, unit is micro seconds. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [reading\_count](#a147989d4c36de1cbd83093a2c5d90950) |
|  | Count of this data readings. |

## Detailed Description

sensor value header

Each sensor value data structure should have this header

Here use 'base\_timestamp' ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)) and 'timestamp\_delta' ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)) to save memory usage in batching mode.

The 'base\_timestamp' is for readings[0], the 'timestamp\_delta' is relation to the previous 'readings'. So, timestamp of readings[0] is header.base\_timestamp + readings[0].timestamp\_delta. timestamp of readings[1] is timestamp of readings[0] + readings[1].timestamp\_delta.

Since timestamp unit is micro seconds, the max 'timestamp\_delta' ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)) is 4295 seconds.

If a sensor has batched data where two consecutive readings differ by more than 4295 seconds, the sensor subsystem core will split them across multiple instances of the readings structure, and send multiple events.

This concept is borrowed from CHRE: [https://cs.android.com/android/platform/superproject/+/master:](https://cs.android.com/android/platform/superproject/+/master:)\ system/chre/chre\_api/include/chre\_api/chre/sensor\_types.h

## Field Documentation

## [◆ ](#aa8efbfd682535deca1172cb192c1a86c)base\_timestamp

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sensing\_sensor\_value\_header::base\_timestamp |
| --- |

Base timestamp of this data readings, unit is micro seconds.

## [◆ ](#a147989d4c36de1cbd83093a2c5d90950)reading\_count

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sensing\_sensor\_value\_header::reading\_count |
| --- |

Count of this data readings.

---

The documentation for this struct was generated from the following file:

- zephyr/sensing/[sensing\_datatypes.h](sensing__datatypes_8h_source.md)

- [sensing\_sensor\_value\_header](structsensing__sensor__value__header.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
