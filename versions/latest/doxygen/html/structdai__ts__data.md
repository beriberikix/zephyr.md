---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structdai__ts__data.html
original_path: doxygen/html/structdai__ts__data.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dai\_ts\_data Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [DAI Interface](group__dai__interface.md)

DAI timestamp data.
[More...](#details)

`#include <[dai.h](dai_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [walclk](#a11133d72485786e75a9d94f218fe699b) |
|  | Wall clock. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [sample](#a933cbc19cc837683581db806702fba36) |
|  | Sample count. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [walclk\_rate](#ace2686aa6ff5aed346705cbb0d198d36) |
|  | Rate in Hz, e.g. |

## Detailed Description

DAI timestamp data.

## Field Documentation

## [◆ ](#a933cbc19cc837683581db806702fba36)sample

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) dai\_ts\_data::sample |
| --- |

Sample count.

## [◆ ](#a11133d72485786e75a9d94f218fe699b)walclk

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) dai\_ts\_data::walclk |
| --- |

Wall clock.

## [◆ ](#ace2686aa6ff5aed346705cbb0d198d36)walclk\_rate

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dai\_ts\_data::walclk\_rate |
| --- |

Rate in Hz, e.g.

19200000

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[dai.h](dai_8h_source.md)

- [dai\_ts\_data](structdai__ts__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
