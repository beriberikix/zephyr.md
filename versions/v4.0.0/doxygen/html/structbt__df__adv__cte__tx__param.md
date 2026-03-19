---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__df__adv__cte__tx__param.html
original_path: doxygen/html/structbt__df__adv__cte__tx__param.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_df\_adv\_cte\_tx\_param Struct Reference

Constant Tone Extension parameters for connectionless transmission.
[More...](#details)

`#include <[direction.h](direction_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cte\_len](#a2ab62db4279338e05cd9e5c222c3aab2) |
|  | Length of CTE in 8us units. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cte\_type](#a4af32abbb603d1b7a533771a23d6e9ee) |
|  | CTE type. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cte\_count](#a288d635221a752b231033803acddd261) |
|  | Number of CTE to transmit in each periodic adv interval. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_ant\_ids](#ac974c5bb804912f5940b2ede5f6394a1) |
|  | Number of Antenna IDs in the switch pattern. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [ant\_ids](#ac1f251cb2205ce345dc3815b53f13918) |
|  | List of antenna IDs in the pattern. |

## Detailed Description

Constant Tone Extension parameters for connectionless transmission.

The structure holds information required to setup CTE transmission in periodic advertising.

## Field Documentation

## [◆ ](#ac1f251cb2205ce345dc3815b53f13918)ant\_ids

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_df\_adv\_cte\_tx\_param::ant\_ids |
| --- |

List of antenna IDs in the pattern.

## [◆ ](#a288d635221a752b231033803acddd261)cte\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_adv\_cte\_tx\_param::cte\_count |
| --- |

Number of CTE to transmit in each periodic adv interval.

## [◆ ](#a2ab62db4279338e05cd9e5c222c3aab2)cte\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_adv\_cte\_tx\_param::cte\_len |
| --- |

Length of CTE in 8us units.

## [◆ ](#a4af32abbb603d1b7a533771a23d6e9ee)cte\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_adv\_cte\_tx\_param::cte\_type |
| --- |

CTE type.

Allowed values are defined by [bt\_df\_cte\_type](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05 "bt_df_cte_type"), except BT\_DF\_CTE\_TYPE\_NONE and BT\_DF\_CTE\_TYPE\_ALL.

## [◆ ](#ac974c5bb804912f5940b2ede5f6394a1)num\_ant\_ids

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_adv\_cte\_tx\_param::num\_ant\_ids |
| --- |

Number of Antenna IDs in the switch pattern.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[direction.h](direction_8h_source.md)

- [bt\_df\_adv\_cte\_tx\_param](structbt__df__adv__cte__tx__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
