---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structw1__slave__config.html
original_path: doxygen/html/structw1__slave__config.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

w1\_slave\_config Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [1-Wire Interface](group__w1__interface.md) » [1-Wire network layer](group__w1__network.md)

Node specific 1-wire configuration struct.
[More...](#details)

`#include <[w1.h](w1_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [w1\_rom](structw1__rom.md) | [rom](#a9f42fd1257483f308115ae02e6ef8596) |
|  | Unique 1-Wire ROM. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [overdrive](#ab8a2d4522505416863fed561df22d058): 1 |
|  | overdrive speed is used if set to 1. |

## Detailed Description

Node specific 1-wire configuration struct.

This struct is passed to network functions, such that they can configure the bus to address the specific slave using the selected speed.

## Field Documentation

## [◆ ](#ab8a2d4522505416863fed561df22d058)overdrive

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) w1\_slave\_config::overdrive |
| --- |

overdrive speed is used if set to 1.

## [◆ ](#a9f42fd1257483f308115ae02e6ef8596)rom

| struct [w1\_rom](structw1__rom.md) w1\_slave\_config::rom |
| --- |

Unique 1-Wire ROM.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[w1.h](w1_8h_source.md)

- [w1\_slave\_config](structw1__slave__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
