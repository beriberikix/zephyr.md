---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsensing__sensor__value__uint32.html
original_path: doxygen/html/structsensing__sensor__value__uint32.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensing\_sensor\_value\_uint32 Struct Reference

[Sensing](group__sensing.md) » [Data Types](group__sensing__datatypes.md)

Sensor value data structure for single 1-axis value.
[More...](#details)

`#include <[sensing_datatypes.h](sensing__datatypes_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [sensing\_sensor\_value\_header](structsensing__sensor__value__header.md) | [header](#adfb3431b5b5e90d29931b9861c9dcd21) |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [timestamp\_delta](#a1fd1c1d018a3793e56e4d0bfded03812) |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [v](#a10d8f7d8f36c4969552b297ed34bf592) |  |
| } | [readings](#af30e831ebd860b0dec15733220bdb9df) [1] |

## Detailed Description

Sensor value data structure for single 1-axis value.

struct [sensing\_sensor\_value\_uint32](structsensing__sensor__value__uint32.md "Sensor value data structure for single 1-axis value.") can be used by SENSING\_SENSOR\_TYPE\_LIGHT\_AMBIENTLIGHT sensor [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) version

## Field Documentation

## [◆ ](#adfb3431b5b5e90d29931b9861c9dcd21)header

| struct [sensing\_sensor\_value\_header](structsensing__sensor__value__header.md) sensing\_sensor\_value\_uint32::header |
| --- |

## [◆ ](#af30e831ebd860b0dec15733220bdb9df)[struct]

| struct { ... } sensing\_sensor\_value\_uint32::readings[1] |
| --- |

## [◆ ](#a1fd1c1d018a3793e56e4d0bfded03812)timestamp\_delta

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sensing\_sensor\_value\_uint32::timestamp\_delta |
| --- |

## [◆ ](#a10d8f7d8f36c4969552b297ed34bf592)v

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sensing\_sensor\_value\_uint32::v |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/sensing/[sensing\_datatypes.h](sensing__datatypes_8h_source.md)

- [sensing\_sensor\_value\_uint32](structsensing__sensor__value__uint32.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
