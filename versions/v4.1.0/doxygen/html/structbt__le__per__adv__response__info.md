---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__le__per__adv__response__info.html
original_path: doxygen/html/structbt__le__per__adv__response__info.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_per\_adv\_response\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

`#include <[bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [subevent](#a1b87ab77f5c7d4ee0c1c612bcfb424d5) |
|  | The subevent the response was received in. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tx\_status](#ab17f33cb713d258bf6c863a64e5aba07) |
|  | Status of the subevent indication. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [tx\_power](#a7ed20f695e0d696eaab7cddc4e3c11fb) |
|  | The TX power of the response in dBm. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [rssi](#a2db58fb452a07290ab4a50892c682837) |
|  | The RSSI of the response in dBm. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cte\_type](#a52b0c612b09cfcb3eb2ea475614c34b8) |
|  | The Constant Tone Extension (CTE) of the advertisement ([bt\_df\_cte\_type](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05 "bt_df_cte_type")). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [response\_slot](#a83cc642c9f22c767421644e7d8233001) |
|  | The slot the response was received in. |

## Field Documentation

## [◆ ](#a52b0c612b09cfcb3eb2ea475614c34b8)cte\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_response\_info::cte\_type |
| --- |

The Constant Tone Extension (CTE) of the advertisement ([bt\_df\_cte\_type](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05 "bt_df_cte_type")).

## [◆ ](#a83cc642c9f22c767421644e7d8233001)response\_slot

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_response\_info::response\_slot |
| --- |

The slot the response was received in.

## [◆ ](#a2db58fb452a07290ab4a50892c682837)rssi

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_le\_per\_adv\_response\_info::rssi |
| --- |

The RSSI of the response in dBm.

## [◆ ](#a1b87ab77f5c7d4ee0c1c612bcfb424d5)subevent

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_response\_info::subevent |
| --- |

The subevent the response was received in.

## [◆ ](#a7ed20f695e0d696eaab7cddc4e3c11fb)tx\_power

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_le\_per\_adv\_response\_info::tx\_power |
| --- |

The TX power of the response in dBm.

## [◆ ](#ab17f33cb713d258bf6c863a64e5aba07)tx\_status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_response\_info::tx\_status |
| --- |

Status of the subevent indication.

0 if subevent indication was transmitted. 1 if subevent indication was not transmitted. All other values RFU.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_per\_adv\_response\_info](structbt__le__per__adv__response__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
