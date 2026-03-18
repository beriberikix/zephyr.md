---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__conn__le__tx__power.html
original_path: doxygen/html/structbt__conn__le__tx__power.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_le\_tx\_power Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

LE Transmit Power Level Structure.
[More...](#details)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [phy](#a8702c4ff5082b8f90decdfabfb8253fe) |
|  | Input: 1M, 2M, Coded S2 or Coded S8. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [current\_level](#a6d2e5a5215fa5d60630e74928a67fc04) |
|  | Output: current transmit power level. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [max\_level](#a1674247c511906fa6f0193653ed0b71a) |
|  | Output: maximum transmit power level. |

## Detailed Description

LE Transmit Power Level Structure.

## Field Documentation

## [◆ ](#a6d2e5a5215fa5d60630e74928a67fc04)current\_level

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_conn\_le\_tx\_power::current\_level |
| --- |

Output: current transmit power level.

## [◆ ](#a1674247c511906fa6f0193653ed0b71a)max\_level

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_conn\_le\_tx\_power::max\_level |
| --- |

Output: maximum transmit power level.

## [◆ ](#a8702c4ff5082b8f90decdfabfb8253fe)phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_tx\_power::phy |
| --- |

Input: 1M, 2M, Coded S2 or Coded S8.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_le\_tx\_power](structbt__conn__le__tx__power.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
