---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsensor__chan__spec.html
original_path: doxygen/html/structsensor__chan__spec.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor\_chan\_spec Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Sensor Interface](group__sensor__interface.md)

Sensor Channel Specification.
[More...](#details)

`#include <[sensor.h](sensor_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [chan\_type](#a1b2f0ecdc23e0d235536eb5fcdeeb63c) |
|  | A sensor channel type. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [chan\_idx](#a00d4a927cfeae33b2beea8cdc415dda1) |
|  | A sensor channel index. |

## Detailed Description

Sensor Channel Specification.

A sensor channel specification is a unique identifier per sensor device describing a measurement channel.

Note
:   Typically passed by value as the size of a [sensor\_chan\_spec](structsensor__chan__spec.md "Sensor Channel Specification.") is a single word.

## Field Documentation

## [◆ ](#a00d4a927cfeae33b2beea8cdc415dda1)chan\_idx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sensor\_chan\_spec::chan\_idx |
| --- |

A sensor channel index.

## [◆ ](#a1b2f0ecdc23e0d235536eb5fcdeeb63c)chan\_type

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sensor\_chan\_spec::chan\_type |
| --- |

A sensor channel type.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[sensor.h](sensor_8h_source.md)

- [sensor\_chan\_spec](structsensor__chan__spec.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
