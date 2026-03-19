---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmspi__event.html
original_path: doxygen/html/structmspi__event.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mspi\_event Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MSPI Driver APIs](group__mspi__interface.md) » [MSPI callback API](group__mspi__callback__api.md)

MSPI event.
[More...](#details)

`#include <[mspi.h](mspi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [mspi\_bus\_event](group__mspi__interface.md#ga4cd05950729893e08ef0d4a12e2242d5) | [evt\_type](#a65079ed0fcdb2ca607dab070f2ed010b) |
|  | Event type. |
| struct [mspi\_event\_data](structmspi__event__data.md) | [evt\_data](#aeeb42b82bd219169e6f185ecdcc2129d) |
|  | Data associated to the event. |

## Detailed Description

MSPI event.

## Field Documentation

## [◆ ](#aeeb42b82bd219169e6f185ecdcc2129d)evt\_data

| struct [mspi\_event\_data](structmspi__event__data.md) mspi\_event::evt\_data |
| --- |

Data associated to the event.

## [◆ ](#a65079ed0fcdb2ca607dab070f2ed010b)evt\_type

| enum [mspi\_bus\_event](group__mspi__interface.md#ga4cd05950729893e08ef0d4a12e2242d5) mspi\_event::evt\_type |
| --- |

Event type.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[mspi.h](mspi_8h_source.md)

- [mspi\_event](structmspi__event.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
