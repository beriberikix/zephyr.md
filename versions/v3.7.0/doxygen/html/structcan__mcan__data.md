---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structcan__mcan__data.html
original_path: doxygen/html/structcan__mcan__data.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can\_mcan\_data Struct Reference

Bosch M\_CAN driver internal data structure.
[More...](#details)

`#include <[can_mcan.h](can__mcan_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct can\_driver\_data | [common](#a486500387e6351f68d741f089d57f913) |
| struct [k\_mutex](structk__mutex.md) | [lock](#a27048362bd5d4288e3ea9018ccc210f6) |
| struct k\_sem | [tx\_sem](#a5e0239c7ff45045d4f4ca5c83a41c4dd) |
| struct [k\_mutex](structk__mutex.md) | [tx\_mtx](#a535ad3150d0c64f11b4dd4e3010d4718) |
| void \* | [custom](#a4211c8dce9704c43790ac354d124c3ab) |

## Detailed Description

Bosch M\_CAN driver internal data structure.

## Field Documentation

## [◆ ](#a486500387e6351f68d741f089d57f913)common

| struct can\_driver\_data can\_mcan\_data::common |
| --- |

## [◆ ](#a4211c8dce9704c43790ac354d124c3ab)custom

| void\* can\_mcan\_data::custom |
| --- |

## [◆ ](#a27048362bd5d4288e3ea9018ccc210f6)lock

| struct [k\_mutex](structk__mutex.md) can\_mcan\_data::lock |
| --- |

## [◆ ](#a535ad3150d0c64f11b4dd4e3010d4718)tx\_mtx

| struct [k\_mutex](structk__mutex.md) can\_mcan\_data::tx\_mtx |
| --- |

## [◆ ](#a5e0239c7ff45045d4f4ca5c83a41c4dd)tx\_sem

| struct k\_sem can\_mcan\_data::tx\_sem |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_mcan.h](can__mcan_8h_source.md)

- [can\_mcan\_data](structcan__mcan__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
