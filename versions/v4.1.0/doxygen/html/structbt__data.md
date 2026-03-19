---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__data.html
original_path: doxygen/html/structbt__data.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_data Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

Bluetooth data.
[More...](#details)

`#include <[bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [type](#a984aecb40a4993ffa113be53942db065) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data\_len](#abda19091a1b8f99d385f11772ef34d5f) |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [data](#ac80ec10101ad69a86f703a4e652c7826) |

## Detailed Description

Bluetooth data.

Description of different data types that can be encoded into advertising data. Used to form arrays that are passed to the [bt\_le\_adv\_start()](group__bt__gap.md#gad2e3caef88d52d720e8e4d21df767b02 "Start advertising.") function.

## Field Documentation

## [◆ ](#ac80ec10101ad69a86f703a4e652c7826)data

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_data::data |
| --- |

## [◆ ](#abda19091a1b8f99d385f11772ef34d5f)data\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_data::data\_len |
| --- |

## [◆ ](#a984aecb40a4993ffa113be53942db065)type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_data::type |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_data](structbt__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
