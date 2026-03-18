---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structsensor__occurrence__data.html
original_path: doxygen/html/structsensor__occurrence__data.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor\_occurrence\_data Struct Reference

Data from a sensor where we only care about an event occurring.
[More...](#details)

`#include <[sensor_data_types.h](sensor__data__types_8h_source.md)>`

| Data Structures | |
| --- | --- |
| struct | [sensor\_occurrence\_sample\_data](structsensor__occurrence__data_1_1sensor__occurrence__sample__data.md) |

| Data Fields | |
| --- | --- |
| struct [sensor\_data\_header](structsensor__data__header.md) | [header](#a06e7c6b24166e1c85d05286d44f60768) |
| struct [sensor\_occurrence\_data::sensor\_occurrence\_sample\_data](structsensor__occurrence__data_1_1sensor__occurrence__sample__data.md) | [readings](#a181279d03759db87e3855d46d30c5aaf) [1] |

## Detailed Description

Data from a sensor where we only care about an event occurring.

This is used to report triggers.

## Field Documentation

## [◆ ](#a06e7c6b24166e1c85d05286d44f60768)header

| struct [sensor\_data\_header](structsensor__data__header.md) sensor\_occurrence\_data::header |
| --- |

## [◆ ](#a181279d03759db87e3855d46d30c5aaf)readings

| struct [sensor\_occurrence\_data::sensor\_occurrence\_sample\_data](structsensor__occurrence__data_1_1sensor__occurrence__sample__data.md) sensor\_occurrence\_data::readings[1] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[sensor\_data\_types.h](sensor__data__types_8h_source.md)

- [sensor\_occurrence\_data](structsensor__occurrence__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
