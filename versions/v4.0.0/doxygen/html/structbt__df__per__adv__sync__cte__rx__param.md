---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__df__per__adv__sync__cte__rx__param.html
original_path: doxygen/html/structbt__df__per__adv__sync__cte__rx__param.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_df\_per\_adv\_sync\_cte\_rx\_param Struct Reference

Constant Tone Extension parameters for connectionless reception.
[More...](#details)

`#include <[direction.h](direction_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cte\_types](#a1740d3f41dddd755fc1e04216c8070e5) |
|  | Bitfield with allowed CTE types. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [slot\_durations](#abff68c9f2e42e3fe6e8b155f5390f219) |
|  | Antenna switching slots ([bt\_df\_antenna\_switching\_slot](direction_8h.md#a546598ce9a81161ad1ba098a7b1a8df4 "bt_df_antenna_switching_slot")). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [max\_cte\_count](#ac64232b5e9b2c6acfadfca1c95fd1021) |
|  | Max number of CTEs to receive. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_ant\_ids](#ae358cbd7b1dd59a7d0a931c8a5fbd94d) |
|  | Length of antenna switch pattern. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [ant\_ids](#ac83de1a86fef076d6c8fc6bccbe49a64) |
|  | Antenna switch pattern. |

## Detailed Description

Constant Tone Extension parameters for connectionless reception.

Note
:   cte\_type is a bit field that provides information about type of CTE an application expects ([bt\_df\_cte\_type](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05 "bt_df_cte_type")). In case cte\_type bit BT\_DF\_CTE\_TYPE\_AOA is not set, members: slot\_durations, num\_ant\_ids and ant\_ids are not required and their values will be not verified for correctness.

## Field Documentation

## [◆ ](#ac83de1a86fef076d6c8fc6bccbe49a64)ant\_ids

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_df\_per\_adv\_sync\_cte\_rx\_param::ant\_ids |
| --- |

Antenna switch pattern.

## [◆ ](#a1740d3f41dddd755fc1e04216c8070e5)cte\_types

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_per\_adv\_sync\_cte\_rx\_param::cte\_types |
| --- |

Bitfield with allowed CTE types.

Allowed values are defined by [bt\_df\_cte\_type](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05 "bt_df_cte_type"), except BT\_DF\_CTE\_TYPE\_NONE.

## [◆ ](#ac64232b5e9b2c6acfadfca1c95fd1021)max\_cte\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_per\_adv\_sync\_cte\_rx\_param::max\_cte\_count |
| --- |

Max number of CTEs to receive.

Min is 1, max is 10, 0 means receive continuously.

## [◆ ](#ae358cbd7b1dd59a7d0a931c8a5fbd94d)num\_ant\_ids

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_per\_adv\_sync\_cte\_rx\_param::num\_ant\_ids |
| --- |

Length of antenna switch pattern.

## [◆ ](#abff68c9f2e42e3fe6e8b155f5390f219)slot\_durations

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_per\_adv\_sync\_cte\_rx\_param::slot\_durations |
| --- |

Antenna switching slots ([bt\_df\_antenna\_switching\_slot](direction_8h.md#a546598ce9a81161ad1ba098a7b1a8df4 "bt_df_antenna_switching_slot")).

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[direction.h](direction_8h_source.md)

- [bt\_df\_per\_adv\_sync\_cte\_rx\_param](structbt__df__per__adv__sync__cte__rx__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
