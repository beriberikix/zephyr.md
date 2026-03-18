---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__df__conn__cte__rx__param.html
original_path: doxygen/html/structbt__df__conn__cte__rx__param.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_df\_conn\_cte\_rx\_param Struct Reference

`#include <[direction.h](direction_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cte\_types](#a3401f31865ced48d89c2b4560bcd4512) |
|  | Bitfield with allowed CTE types. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [slot\_durations](#afe2dae75b7138b374f991c58f8143c9d) |
|  | Antenna switching slots ([bt\_df\_antenna\_switching\_slot](direction_8h.md#a546598ce9a81161ad1ba098a7b1a8df4 "bt_df_antenna_switching_slot")). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_ant\_ids](#aee2ed2d86e2740e166434ede099b1250) |
|  | Length of antenna switch pattern. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [ant\_ids](#a35c2aac4512e2ffce19346c9bf51f033) |
|  | Antenna switch pattern. |

## Field Documentation

## [◆ ](#a35c2aac4512e2ffce19346c9bf51f033)ant\_ids

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_df\_conn\_cte\_rx\_param::ant\_ids |
| --- |

Antenna switch pattern.

## [◆ ](#a3401f31865ced48d89c2b4560bcd4512)cte\_types

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_conn\_cte\_rx\_param::cte\_types |
| --- |

Bitfield with allowed CTE types.

Allowed values are defined by [bt\_df\_cte\_type](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05 "bt_df_cte_type"), except BT\_DF\_CTE\_TYPE\_NONE.

## [◆ ](#aee2ed2d86e2740e166434ede099b1250)num\_ant\_ids

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_conn\_cte\_rx\_param::num\_ant\_ids |
| --- |

Length of antenna switch pattern.

## [◆ ](#afe2dae75b7138b374f991c58f8143c9d)slot\_durations

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_conn\_cte\_rx\_param::slot\_durations |
| --- |

Antenna switching slots ([bt\_df\_antenna\_switching\_slot](direction_8h.md#a546598ce9a81161ad1ba098a7b1a8df4 "bt_df_antenna_switching_slot")).

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[direction.h](direction_8h_source.md)

- [bt\_df\_conn\_cte\_rx\_param](structbt__df__conn__cte__rx__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
