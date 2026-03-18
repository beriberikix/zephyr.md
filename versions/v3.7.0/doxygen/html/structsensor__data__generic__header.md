---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structsensor__data__generic__header.html
original_path: doxygen/html/structsensor__data__generic__header.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor\_data\_generic\_header Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Sensor Interface](group__sensor__interface.md)

`#include <[sensor.h](sensor_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [timestamp\_ns](#a429e22b3191df271ccfe321b796e1ac9) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [num\_channels](#a7edbe674f28c95f3aa40b1df84ca61fe) |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [shift](#a68067521c1058b6802176e1d48fed788) |
| struct [sensor\_chan\_spec](structsensor__chan__spec.md) | [channels](#ac09f23959c66ff75b0854a95e8d4504b) [0] |

## Field Documentation

## [◆ ](#ac09f23959c66ff75b0854a95e8d4504b)channels

| struct [sensor\_chan\_spec](structsensor__chan__spec.md) sensor\_data\_generic\_header::channels[0] |
| --- |

## [◆ ](#a7edbe674f28c95f3aa40b1df84ca61fe)num\_channels

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sensor\_data\_generic\_header::num\_channels |
| --- |

## [◆ ](#a68067521c1058b6802176e1d48fed788)shift

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) sensor\_data\_generic\_header::shift |
| --- |

## [◆ ](#a429e22b3191df271ccfe321b796e1ac9)timestamp\_ns

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sensor\_data\_generic\_header::timestamp\_ns |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[sensor.h](sensor_8h_source.md)

- [sensor\_data\_generic\_header](structsensor__data__generic__header.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
