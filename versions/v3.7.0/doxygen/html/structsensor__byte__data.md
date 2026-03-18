---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structsensor__byte__data.html
original_path: doxygen/html/structsensor__byte__data.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor\_byte\_data Struct Reference

Data from a sensor that produces a byte of data.
[More...](#details)

`#include <[sensor_data_types.h](sensor__data__types_8h_source.md)>`

| Data Structures | |
| --- | --- |
| struct | [sensor\_byte\_sample\_data](structsensor__byte__data_1_1sensor__byte__sample__data.md) |

| Data Fields | |
| --- | --- |
| struct [sensor\_data\_header](structsensor__data__header.md) | [header](#ab18ad72251bae040fc4752bc125be3ba) |
| struct [sensor\_byte\_data::sensor\_byte\_sample\_data](structsensor__byte__data_1_1sensor__byte__sample__data.md) | [readings](#ad4ac07ed10938265e89a43133c41af24) [1] |

## Detailed Description

Data from a sensor that produces a byte of data.

This is used by:

- :c:enum:[SENSOR\_CHAN\_PROX](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934abaec2c1347ef0035221dd4d9c34a4774 "Proximity.")

## Field Documentation

## [◆ ](#ab18ad72251bae040fc4752bc125be3ba)header

| struct [sensor\_data\_header](structsensor__data__header.md) sensor\_byte\_data::header |
| --- |

## [◆ ](#ad4ac07ed10938265e89a43133c41af24)readings

| struct [sensor\_byte\_data::sensor\_byte\_sample\_data](structsensor__byte__data_1_1sensor__byte__sample__data.md) sensor\_byte\_data::readings[1] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[sensor\_data\_types.h](sensor__data__types_8h_source.md)

- [sensor\_byte\_data](structsensor__byte__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
