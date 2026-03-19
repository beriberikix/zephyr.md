---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsensor__byte__data_1_1sensor__byte__sample__data.html
original_path: doxygen/html/structsensor__byte__data_1_1sensor__byte__sample__data.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor\_byte\_data::sensor\_byte\_sample\_data Struct Reference

`#include <[sensor_data_types.h](sensor__data__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [timestamp\_delta](#ab29a911990794b35bde3114e813d2c9a) |
| union { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [value](#a3ad640ff448fe87d2eda7c5118404b7a) |  |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [is\_near](#acd42cfa0dc446378cebf998c1b795963): 1 |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [padding](#ab07c2a7ce6e47c61249606a88aeda2bd): 7 |  |
| } |  |
| }; |  |

## Field Documentation

## [◆ ](#a50af39162773fe8e4a725acbba8d90d4)[union]

| union { ... } [sensor\_byte\_data::sensor\_byte\_sample\_data](structsensor__byte__data_1_1sensor__byte__sample__data.md) |
| --- |

## [◆ ](#acd42cfa0dc446378cebf998c1b795963)is\_near

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sensor\_byte\_data::sensor\_byte\_sample\_data::is\_near |
| --- |

## [◆ ](#ab07c2a7ce6e47c61249606a88aeda2bd)padding

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sensor\_byte\_data::sensor\_byte\_sample\_data::padding |
| --- |

## [◆ ](#ab29a911990794b35bde3114e813d2c9a)timestamp\_delta

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sensor\_byte\_data::sensor\_byte\_sample\_data::timestamp\_delta |
| --- |

## [◆ ](#a3ad640ff448fe87d2eda7c5118404b7a)value

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sensor\_byte\_data::sensor\_byte\_sample\_data::value |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[sensor\_data\_types.h](sensor__data__types_8h_source.md)

- [sensor\_byte\_data](structsensor__byte__data.md)
- [sensor\_byte\_sample\_data](structsensor__byte__data_1_1sensor__byte__sample__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
