---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__le__per__adv__sync__recv__info.html
original_path: doxygen/html/structbt__le__per__adv__sync__recv__info.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_per\_adv\_sync\_recv\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

Information about a received periodic advertising report.
[More...](#details)

`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | [addr](#a5817bd4fba2c93adebcebe007650b6eb) |
|  | Advertiser LE address and type. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sid](#a21b0ca87e46c6897282ebd877e45114e) |
|  | Advertising Set Identifier, valid range [BT\_GAP\_SID\_MIN](group__bt__gap__defines.md#gacf05b7660d2ae85f64e2a220abf8e57d "BT_GAP_SID_MIN") to [BT\_GAP\_SID\_MAX](group__bt__gap__defines.md#gafa6f803fe3ada07030fb1f2f725940c4 "BT_GAP_SID_MAX"). |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [tx\_power](#a65f1a2adb7c3d740cb8262ae7f5a7c3e) |
|  | The TX power of the advertisement. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [rssi](#aa17c9d917469f121448ed4e1db485700) |
|  | The RSSI of the advertisement excluding any CTE. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cte\_type](#a1591907e3cb1f4565b9d26c18bccc7d2) |
|  | The Constant Tone Extension (CTE) of the advertisement ([bt\_df\_cte\_type](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05 "bt_df_cte_type")). |

## Detailed Description

Information about a received periodic advertising report.

This struct holds information about a periodic advertising event that has been received. It contains details such as the advertiser’s address, SID, transmit power, RSSI, CTE type, and additional information depending on the configuration (e.g., event counter and subevent in case of a subevent indication). This information is provided in the callback when periodic advertising data is received.

Note
:   Used in [bt\_le\_per\_adv\_sync\_cb](structbt__le__per__adv__sync__cb.md "bt_le_per_adv_sync_cb") structure.

## Field Documentation

## [◆ ](#a5817bd4fba2c93adebcebe007650b6eb)addr

| const [bt\_addr\_le\_t](structbt__addr__le__t.md)\* bt\_le\_per\_adv\_sync\_recv\_info::addr |
| --- |

Advertiser LE address and type.

## [◆ ](#a1591907e3cb1f4565b9d26c18bccc7d2)cte\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_sync\_recv\_info::cte\_type |
| --- |

The Constant Tone Extension (CTE) of the advertisement ([bt\_df\_cte\_type](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05 "bt_df_cte_type")).

## [◆ ](#aa17c9d917469f121448ed4e1db485700)rssi

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_le\_per\_adv\_sync\_recv\_info::rssi |
| --- |

The RSSI of the advertisement excluding any CTE.

## [◆ ](#a21b0ca87e46c6897282ebd877e45114e)sid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_sync\_recv\_info::sid |
| --- |

Advertising Set Identifier, valid range [BT\_GAP\_SID\_MIN](group__bt__gap__defines.md#gacf05b7660d2ae85f64e2a220abf8e57d "BT_GAP_SID_MIN") to [BT\_GAP\_SID\_MAX](group__bt__gap__defines.md#gafa6f803fe3ada07030fb1f2f725940c4 "BT_GAP_SID_MAX").

## [◆ ](#a65f1a2adb7c3d740cb8262ae7f5a7c3e)tx\_power

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_le\_per\_adv\_sync\_recv\_info::tx\_power |
| --- |

The TX power of the advertisement.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_per\_adv\_sync\_recv\_info](structbt__le__per__adv__sync__recv__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
