---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__df__conn__cte__req__params.html
original_path: doxygen/html/structbt__df__conn__cte__req__params.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_df\_conn\_cte\_req\_params Struct Reference

`#include <[direction.h](direction_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [interval](#ab8148905943e0d87a37740ab891b9ef7) |
|  | Requested interval for initiating the CTE Request procedure. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cte\_length](#a71340a450e573612a271467c51110166) |
|  | Requested length of the CTE in 8 us units. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cte\_type](#ae8232614ec9201e4572675d793b2292a) |
|  | Requested type of the CTE. |

## Field Documentation

## [◆ ](#a71340a450e573612a271467c51110166)cte\_length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_conn\_cte\_req\_params::cte\_length |
| --- |

Requested length of the CTE in 8 us units.

## [◆ ](#ae8232614ec9201e4572675d793b2292a)cte\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_conn\_cte\_req\_params::cte\_type |
| --- |

Requested type of the CTE.

Allowed values are defined by [bt\_df\_cte\_type](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05 "bt_df_cte_type"), except BT\_DF\_CTE\_TYPE\_NONE and BT\_DF\_CTE\_TYPE\_ALL.

## [◆ ](#ab8148905943e0d87a37740ab891b9ef7)interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_df\_conn\_cte\_req\_params::interval |
| --- |

Requested interval for initiating the CTE Request procedure.

Value 0x0 means, run the procedure once. Other values are intervals in number of connection events, to run the command periodically.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[direction.h](direction_8h_source.md)

- [bt\_df\_conn\_cte\_req\_params](structbt__df__conn__cte__req__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
