---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__le__ext__adv__info.html
original_path: doxygen/html/structbt__le__ext__adv__info.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_ext\_adv\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

Advertising set info structure.
[More...](#details)

`#include <[bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [id](#a06aa727cd2523914bc7509713585bffd) |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [tx\_power](#a485e4a8124fddee897fe744836cbfb24) |
|  | Currently selected Transmit Power (dBM). |
| const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | [addr](#a0dd0aa8a26fe1ef5813fa07732c5c4c9) |
|  | Current local advertising address used. |

## Detailed Description

Advertising set info structure.

## Field Documentation

## [◆ ](#a0dd0aa8a26fe1ef5813fa07732c5c4c9)addr

| const [bt\_addr\_le\_t](structbt__addr__le__t.md)\* bt\_le\_ext\_adv\_info::addr |
| --- |

Current local advertising address used.

## [◆ ](#a06aa727cd2523914bc7509713585bffd)id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_ext\_adv\_info::id |
| --- |

## [◆ ](#a485e4a8124fddee897fe744836cbfb24)tx\_power

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_le\_ext\_adv\_info::tx\_power |
| --- |

Currently selected Transmit Power (dBM).

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_ext\_adv\_info](structbt__le__ext__adv__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
