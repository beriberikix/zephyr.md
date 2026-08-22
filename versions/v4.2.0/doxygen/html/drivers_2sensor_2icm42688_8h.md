---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/drivers_2sensor_2icm42688_8h.html
original_path: doxygen/html/drivers_2sensor_2icm42688_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

icm42688.h File Reference

Extended public API for ICM42688.
[More...](#details)

`#include <[zephyr/drivers/sensor.h](sensor_8h_source.md)>`

[Go to the source code of this file.](drivers_2sensor_2icm42688_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ICM42688\_PIN9\_FUNCTION\_INT2](#a3c5c9d8d18ea8c8aef23e6699149d28a)   0 |
| #define | [ICM42688\_PIN9\_FUNCTION\_FSYNC](#aae84cb7bf1ce1ceb097ed91e4a452be5)   1 |
| #define | [ICM42688\_PIN9\_FUNCTION\_CLKIN](#a68600f859f297e76e3b6b0f2c89ca089)   2 |

| Enumerations | |
| --- | --- |
| enum | [sensor\_attribute\_icm42688](#a75e9a515047a6fb3ce41dbdf50fdf944) { [SENSOR\_ATTR\_ICM42688\_PIN9\_FUNCTION](#a75e9a515047a6fb3ce41dbdf50fdf944a080aef04033d9986025bc1964c5e6af4) = SENSOR\_ATTR\_PRIV\_START } |
|  | Extended sensor attributes for ICM42688. [More...](#a75e9a515047a6fb3ce41dbdf50fdf944) |

## Detailed Description

Extended public API for ICM42688.

Pin function configuration via attributes under the current sensor driver abstraction.

## Macro Definition Documentation

## [◆ ](#a68600f859f297e76e3b6b0f2c89ca089)ICM42688\_PIN9\_FUNCTION\_CLKIN

| #define ICM42688\_PIN9\_FUNCTION\_CLKIN   2 |
| --- |

## [◆ ](#aae84cb7bf1ce1ceb097ed91e4a452be5)ICM42688\_PIN9\_FUNCTION\_FSYNC

| #define ICM42688\_PIN9\_FUNCTION\_FSYNC   1 |
| --- |

## [◆ ](#a3c5c9d8d18ea8c8aef23e6699149d28a)ICM42688\_PIN9\_FUNCTION\_INT2

| #define ICM42688\_PIN9\_FUNCTION\_INT2   0 |
| --- |

## Enumeration Type Documentation

## [◆ ](#a75e9a515047a6fb3ce41dbdf50fdf944)sensor\_attribute\_icm42688

| enum [sensor\_attribute\_icm42688](#a75e9a515047a6fb3ce41dbdf50fdf944) |
| --- |

Extended sensor attributes for ICM42688.

Attributes for setting pin function.

| Enumerator | |
| --- | --- |
| SENSOR\_ATTR\_ICM42688\_PIN9\_FUNCTION |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [icm42688.h](drivers_2sensor_2icm42688_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
