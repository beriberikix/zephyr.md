---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structcan__mcan__callbacks.html
original_path: doxygen/html/structcan__mcan__callbacks.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can\_mcan\_callbacks Struct Reference

Bosch M\_CAN driver internal Tx + Rx callbacks structure.
[More...](#details)

`#include <[can_mcan.h](can__mcan_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [can\_mcan\_tx\_callback](structcan__mcan__tx__callback.md) \* | [tx](#ad2ee7f63634cc67160f4eb75f05babd2) |
| struct [can\_mcan\_rx\_callback](structcan__mcan__rx__callback.md) \* | [std](#ae225638097e1ddb5270de06401490a7f) |
| struct [can\_mcan\_rx\_callback](structcan__mcan__rx__callback.md) \* | [ext](#ab29bb0963a78fcc68677ff5e4589f004) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_tx](#aad1b8f0b76637e7a53ef5c88118d7bd1) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_std](#a0388e27fc1852d7e7c7ac6f062cab3e1) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_ext](#a9edfccadf0ef4006ac5eb7926772ca85) |

## Detailed Description

Bosch M\_CAN driver internal Tx + Rx callbacks structure.

## Field Documentation

## [◆ ](#ab29bb0963a78fcc68677ff5e4589f004)ext

| struct [can\_mcan\_rx\_callback](structcan__mcan__rx__callback.md)\* can\_mcan\_callbacks::ext |
| --- |

## [◆ ](#a9edfccadf0ef4006ac5eb7926772ca85)num\_ext

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_mcan\_callbacks::num\_ext |
| --- |

## [◆ ](#a0388e27fc1852d7e7c7ac6f062cab3e1)num\_std

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_mcan\_callbacks::num\_std |
| --- |

## [◆ ](#aad1b8f0b76637e7a53ef5c88118d7bd1)num\_tx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_mcan\_callbacks::num\_tx |
| --- |

## [◆ ](#ae225638097e1ddb5270de06401490a7f)std

| struct [can\_mcan\_rx\_callback](structcan__mcan__rx__callback.md)\* can\_mcan\_callbacks::std |
| --- |

## [◆ ](#ad2ee7f63634cc67160f4eb75f05babd2)tx

| struct [can\_mcan\_tx\_callback](structcan__mcan__tx__callback.md)\* can\_mcan\_callbacks::tx |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_mcan.h](can__mcan_8h_source.md)

- [can\_mcan\_callbacks](structcan__mcan__callbacks.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
