---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structsensor__uint64__data.html
original_path: doxygen/html/structsensor__uint64__data.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor\_uint64\_data Struct Reference

Data from a sensor that produces a count like value.
[More...](#details)

`#include <[sensor_data_types.h](sensor__data__types_8h_source.md)>`

| Data Structures | |
| --- | --- |
| struct | [sensor\_uint64\_sample\_data](structsensor__uint64__data_1_1sensor__uint64__sample__data.md) |

| Data Fields | |
| --- | --- |
| struct [sensor\_data\_header](structsensor__data__header.md) | [header](#a61e2d0796ba3c0e95a0455e03ce01d76) |
| struct [sensor\_uint64\_data::sensor\_uint64\_sample\_data](structsensor__uint64__data_1_1sensor__uint64__sample__data.md) | [readings](#a86a1b96bd7a3aeb6b615e6ab0c3a96a6) [1] |

## Detailed Description

Data from a sensor that produces a count like value.

This is used by:

- :c:enum:[SENSOR\_CHAN\_GAUGE\_CYCLE\_COUNT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a8834978858c2b62b5e923d06cfcb1a46 "Cycle count (total number of charge/discharge cycles).")

## Field Documentation

## [◆ ](#a61e2d0796ba3c0e95a0455e03ce01d76)header

| struct [sensor\_data\_header](structsensor__data__header.md) sensor\_uint64\_data::header |
| --- |

## [◆ ](#a86a1b96bd7a3aeb6b615e6ab0c3a96a6)readings

| struct [sensor\_uint64\_data::sensor\_uint64\_sample\_data](structsensor__uint64__data_1_1sensor__uint64__sample__data.md) sensor\_uint64\_data::readings[1] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[sensor\_data\_types.h](sensor__data__types_8h_source.md)

- [sensor\_uint64\_data](structsensor__uint64__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
