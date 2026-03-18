---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structccs811__result__type.html
original_path: doxygen/html/structccs811__result__type.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ccs811\_result\_type Struct Reference

Information collected from the sensor on each fetch.
[More...](#details)

`#include <[ccs811.h](ccs811_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [co2](#a07b71c653136f3afb9d8e0d594cf7c24) |
|  | Equivalent carbon dioxide in parts-per-million volume (ppmv). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [voc](#ad3fef69b83fa1f67f0a3cf7ab1f36f12) |
|  | Equivalent total volatile organic compounds in parts-per-billion volume. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [raw](#a5ddde08ed2992dcd24a283f781775da2) |
|  | Raw voltage and current measured by sensor. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [status](#adf50f8b7e4eb0b45b61a00fb4e2ae8f5) |
|  | Sensor status at completion of most recent fetch. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [error](#a00426f8ba17dcbf696b70a5adb6ff5a4) |
|  | Sensor error flags at completion of most recent fetch. |

## Detailed Description

Information collected from the sensor on each fetch.

## Field Documentation

## [◆ ](#a07b71c653136f3afb9d8e0d594cf7c24)co2

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ccs811\_result\_type::co2 |
| --- |

Equivalent carbon dioxide in parts-per-million volume (ppmv).

## [◆ ](#a00426f8ba17dcbf696b70a5adb6ff5a4)error

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ccs811\_result\_type::error |
| --- |

Sensor error flags at completion of most recent fetch.

Note that errors are cleared when read.

## [◆ ](#a5ddde08ed2992dcd24a283f781775da2)raw

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ccs811\_result\_type::raw |
| --- |

Raw voltage and current measured by sensor.

## [◆ ](#adf50f8b7e4eb0b45b61a00fb4e2ae8f5)status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ccs811\_result\_type::status |
| --- |

Sensor status at completion of most recent fetch.

## [◆ ](#ad3fef69b83fa1f67f0a3cf7ab1f36f12)voc

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ccs811\_result\_type::voc |
| --- |

Equivalent total volatile organic compounds in parts-per-billion volume.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/sensor/[ccs811.h](ccs811_8h_source.md)

- [ccs811\_result\_type](structccs811__result__type.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
