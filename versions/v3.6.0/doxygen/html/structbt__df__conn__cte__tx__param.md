---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__df__conn__cte__tx__param.html
original_path: doxygen/html/structbt__df__conn__cte__tx__param.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_df\_conn\_cte\_tx\_param Struct Reference

Constant Tone Extension parameters for CTE transmission in connected mode.
[More...](#details)

`#include <[direction.h](direction_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cte\_types](#af78df8115d2fac5b8f6132b48a56bc1c) |
|  | Bitfield with allowed CTE types ([bt\_df\_cte\_type](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05 "bt_df_cte_type"). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_ant\_ids](#ad49bc64170e8ee4741aa01393284e7de) |
|  | Number of antenna switch pattern. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [ant\_ids](#a9df1dac6180e77a4c7abc80890346c4a) |
|  | Antenna switch pattern. |

## Detailed Description

Constant Tone Extension parameters for CTE transmission in connected mode.

## Field Documentation

## [◆ ](#a9df1dac6180e77a4c7abc80890346c4a)ant\_ids

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_df\_conn\_cte\_tx\_param::ant\_ids |
| --- |

Antenna switch pattern.

## [◆ ](#af78df8115d2fac5b8f6132b48a56bc1c)cte\_types

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_conn\_cte\_tx\_param::cte\_types |
| --- |

Bitfield with allowed CTE types ([bt\_df\_cte\_type](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05 "bt_df_cte_type").

All enum members may be used except BT\_DF\_CTE\_TYPE\_NONE).

## [◆ ](#ad49bc64170e8ee4741aa01393284e7de)num\_ant\_ids

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_conn\_cte\_tx\_param::num\_ant\_ids |
| --- |

Number of antenna switch pattern.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[direction.h](direction_8h_source.md)

- [bt\_df\_conn\_cte\_tx\_param](structbt__df__conn__cte__tx__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
