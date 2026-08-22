---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__data.html
original_path: doxygen/html/structbt__data.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_data Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

Bluetooth data.
[More...](#details)

`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [type](#a984aecb40a4993ffa113be53942db065) |
|  | Type of scan response data or advertisement data. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data\_len](#abda19091a1b8f99d385f11772ef34d5f) |
|  | Length of scan response data or advertisement data. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [data](#ac80ec10101ad69a86f703a4e652c7826) |
|  | Pointer to Scan response or advertisement data. |

## Detailed Description

Bluetooth data.

Description of different AD Types that can be encoded into advertising data. Used to form arrays that are passed to the [bt\_le\_adv\_start](group__bt__gap.md#gad2e3caef88d52d720e8e4d21df767b02 "bt_le_adv_start") function. The [BT\_DATA](group__bt__gap.md#ga8481217e632522e1f322de87d745f8f0 "BT_DATA") define can be used as a helpter to declare the elements of an [bt\_data](structbt__data.md "bt_data") array.

## Field Documentation

## [◆ ](#ac80ec10101ad69a86f703a4e652c7826)data

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_data::data |
| --- |

Pointer to Scan response or advertisement data.

## [◆ ](#abda19091a1b8f99d385f11772ef34d5f)data\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_data::data\_len |
| --- |

Length of scan response data or advertisement data.

## [◆ ](#a984aecb40a4993ffa113be53942db065)type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_data::type |
| --- |

Type of scan response data or advertisement data.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_data](structbt__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
