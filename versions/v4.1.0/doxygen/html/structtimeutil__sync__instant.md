---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structtimeutil__sync__instant.html
original_path: doxygen/html/structtimeutil__sync__instant.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

timeutil\_sync\_instant Struct Reference

[Utilities](group__utilities.md) » [Time Utility APIs](group__timeutil__apis.md) » [Time Synchronization APIs](group__timeutil__sync__apis.md)

Representation of an instant in two time scales.
[More...](#details)

`#include <[timeutil.h](timeutil_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [ref](#a192ad09026e7b511d0961218e34ea201) |
|  | An instant in the reference time scale. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [local](#a7ebc45287a8ae8d546dc249499f91337) |
|  | The corresponding instance in the local time scale. |

## Detailed Description

Representation of an instant in two time scales.

Capturing the same instant in two time scales provides a registration point that can be used to convert between those time scales.

## Field Documentation

## [◆ ](#a7ebc45287a8ae8d546dc249499f91337)local

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) timeutil\_sync\_instant::local |
| --- |

The corresponding instance in the local time scale.

This may be zero in a valid [timeutil\_sync\_instant](structtimeutil__sync__instant.md "Representation of an instant in two time scales.") object.

## [◆ ](#a192ad09026e7b511d0961218e34ea201)ref

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) timeutil\_sync\_instant::ref |
| --- |

An instant in the reference time scale.

This must never be zero in an initialized [timeutil\_sync\_instant](structtimeutil__sync__instant.md "Representation of an instant in two time scales.") object.

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[timeutil.h](timeutil_8h_source.md)

- [timeutil\_sync\_instant](structtimeutil__sync__instant.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
