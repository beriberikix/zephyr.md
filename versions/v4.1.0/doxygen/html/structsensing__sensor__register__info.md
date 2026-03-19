---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsensing__sensor__register__info.html
original_path: doxygen/html/structsensing__sensor__register__info.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensing\_sensor\_register\_info Struct Reference

[Sensing](group__sensing.md) » [Sensing Sensor API](group__sensing__sensor.md)

Sensor registration information.
[More...](#details)

`#include <[sensing_sensor.h](sensing__sensor_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [flags](#a6300055172c8692b8313adcef5507d41) |
|  | Sensor flags. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sample\_size](#a133621dcf1da9c9ffd111eeec007f220) |
|  | Sample size in bytes for a single sample of the registered sensor. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sensitivity\_count](#aab10e29faf4e3a6bcc33d99119bb8bc9) |
|  | The number of sensor sensitivities. |
| struct [sensing\_sensor\_version](structsensing__sensor__version.md) | [version](#af87ee2748229a7f43049d058da930ce1) |
|  | Sensor version. |

## Detailed Description

Sensor registration information.

## Field Documentation

## [◆ ](#a6300055172c8692b8313adcef5507d41)flags

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sensing\_sensor\_register\_info::flags |
| --- |

Sensor flags.

## [◆ ](#a133621dcf1da9c9ffd111eeec007f220)sample\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sensing\_sensor\_register\_info::sample\_size |
| --- |

Sample size in bytes for a single sample of the registered sensor.

sensing runtime need this information for internal buffer allocation.

## [◆ ](#aab10e29faf4e3a6bcc33d99119bb8bc9)sensitivity\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sensing\_sensor\_register\_info::sensitivity\_count |
| --- |

The number of sensor sensitivities.

## [◆ ](#af87ee2748229a7f43049d058da930ce1)version

| struct [sensing\_sensor\_version](structsensing__sensor__version.md) sensing\_sensor\_register\_info::version |
| --- |

Sensor version.

Version can be used to identify different versions of sensor implementation.

---

The documentation for this struct was generated from the following file:

- zephyr/sensing/[sensing\_sensor.h](sensing__sensor_8h_source.md)

- [sensing\_sensor\_register\_info](structsensing__sensor__register__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
