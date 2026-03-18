---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structcan__sja1000__rx__filter.html
original_path: doxygen/html/structcan__sja1000__rx__filter.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can\_sja1000\_rx\_filter Struct Reference

SJA1000 driver internal RX filter structure.
[More...](#details)

`#include <[can_sja1000.h](can__sja1000_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [can\_filter](structcan__filter.md) | [filter](#aee19675d5cc25ed7adec2bff84b347e5) |
| [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f) | [callback](#a7f312ad2aa06e836928da30ea012d797) |
| void \* | [user\_data](#addc5b07b6aa6a144ae0d2e792523f4df) |

## Detailed Description

SJA1000 driver internal RX filter structure.

## Field Documentation

## [◆ ](#a7f312ad2aa06e836928da30ea012d797)callback

| [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f) can\_sja1000\_rx\_filter::callback |
| --- |

## [◆ ](#aee19675d5cc25ed7adec2bff84b347e5)filter

| struct [can\_filter](structcan__filter.md) can\_sja1000\_rx\_filter::filter |
| --- |

## [◆ ](#addc5b07b6aa6a144ae0d2e792523f4df)user\_data

| void\* can\_sja1000\_rx\_filter::user\_data |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_sja1000.h](can__sja1000_8h_source.md)

- [can\_sja1000\_rx\_filter](structcan__sja1000__rx__filter.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
