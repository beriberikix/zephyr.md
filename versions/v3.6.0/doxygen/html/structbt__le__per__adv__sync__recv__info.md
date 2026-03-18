---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__le__per__adv__sync__recv__info.html
original_path: doxygen/html/structbt__le__per__adv__sync__recv__info.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_per\_adv\_sync\_recv\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

`#include <[bluetooth.h](bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | [addr](#a5817bd4fba2c93adebcebe007650b6eb) |
|  | Advertiser LE address and type. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sid](#a21b0ca87e46c6897282ebd877e45114e) |
|  | Advertiser SID. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [tx\_power](#a65f1a2adb7c3d740cb8262ae7f5a7c3e) |
|  | The TX power of the advertisement. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [rssi](#aa17c9d917469f121448ed4e1db485700) |
|  | The RSSI of the advertisement excluding any CTE. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cte\_type](#a1591907e3cb1f4565b9d26c18bccc7d2) |
|  | The Constant Tone Extension (CTE) of the advertisement ([bt\_df\_cte\_type](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05 "bt_df_cte_type")). |

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

Advertiser SID.

## [◆ ](#a65f1a2adb7c3d740cb8262ae7f5a7c3e)tx\_power

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_le\_per\_adv\_sync\_recv\_info::tx\_power |
| --- |

The TX power of the advertisement.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_8h_source.md)

- [bt\_le\_per\_adv\_sync\_recv\_info](structbt__le__per__adv__sync__recv__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
