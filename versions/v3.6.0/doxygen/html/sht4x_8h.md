---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/sht4x_8h.html
original_path: doxygen/html/sht4x_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sht4x.h File Reference

Extended public API for Sensirion's SHT4X T/RH sensors.
[More...](#details)

`#include <[zephyr/drivers/sensor.h](sensor_8h_source.md)>`

[Go to the source code of this file.](sht4x_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SHT4X\_HEATER\_MAX\_TEMP](#af10d0155ec46d5b5152251d02f7578ee)   65 |

| Enumerations | |
| --- | --- |
| enum | [sensor\_attribute\_sht4x](#a4191e02c97b8130a1c96d47c0939d535) { [SENSOR\_ATTR\_SHT4X\_HEATER\_POWER](#a4191e02c97b8130a1c96d47c0939d535ad18746a0cddc2713d63b0b6ce70f5052) = SENSOR\_ATTR\_PRIV\_START , [SENSOR\_ATTR\_SHT4X\_HEATER\_DURATION](#a4191e02c97b8130a1c96d47c0939d535a1812fd253d281025c8d4155f58e9cbd6) } |

| Functions | |
| --- | --- |
| int | [sht4x\_fetch\_with\_heater](#af2539064f44eb3981cb40a3c2f7a0eb8) (const struct [device](structdevice.md) \*dev) |
|  | Fetches data using the on-chip heater. |

## Detailed Description

Extended public API for Sensirion's SHT4X T/RH sensors.

This exposes an API to the on-chip heater which is specific to the application/environment and cannot be expressed within the sensor driver abstraction.

## Macro Definition Documentation

## [◆ ](#af10d0155ec46d5b5152251d02f7578ee)SHT4X\_HEATER\_MAX\_TEMP

| #define SHT4X\_HEATER\_MAX\_TEMP   65 |
| --- |

## Enumeration Type Documentation

## [◆ ](#a4191e02c97b8130a1c96d47c0939d535)sensor\_attribute\_sht4x

| enum [sensor\_attribute\_sht4x](#a4191e02c97b8130a1c96d47c0939d535) |
| --- |

| Enumerator | |
| --- | --- |
| SENSOR\_ATTR\_SHT4X\_HEATER\_POWER |  |
| SENSOR\_ATTR\_SHT4X\_HEATER\_DURATION |  |

## Function Documentation

## [◆ ](#af2539064f44eb3981cb40a3c2f7a0eb8)sht4x\_fetch\_with\_heater()

| int sht4x\_fetch\_with\_heater | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Fetches data using the on-chip heater.

Measurement is always done with "high" repeatability.

Parameters
:   | dev | Pointer to the sensor device |
    | --- | --- |

Returns
:   0 if successful, negative errno code if failure.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [sht4x.h](sht4x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
