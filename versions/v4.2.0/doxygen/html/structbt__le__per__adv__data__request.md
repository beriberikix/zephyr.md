---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__le__per__adv__data__request.html
original_path: doxygen/html/structbt__le__per__adv__data__request.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_per\_adv\_data\_request Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

Info of the PAwR subevents.
[More...](#details)

`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [start](#a779ed161919c3117f6ce165deb0a9b0a) |
|  | The first subevent data can be set for. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [count](#a766991899bc3e689adec36bf1f12e802) |
|  | The number of subevents data can be set for. |

## Detailed Description

Info of the PAwR subevents.

When the Controller indicates it is ready to transmit one or more PAwR subevents, [bt\_le\_per\_adv\_data\_request](structbt__le__per__adv__data__request.md "bt_le_per_adv_data_request") holds the information about the first subevent data and the number of subevents data can be set for.

Note
:   Used in [bt\_le\_ext\_adv\_cb](structbt__le__ext__adv__cb.md "bt_le_ext_adv_cb").

## Field Documentation

## [◆ ](#a766991899bc3e689adec36bf1f12e802)count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_data\_request::count |
| --- |

The number of subevents data can be set for.

## [◆ ](#a779ed161919c3117f6ce165deb0a9b0a)start

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_data\_request::start |
| --- |

The first subevent data can be set for.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_per\_adv\_data\_request](structbt__le__per__adv__data__request.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
