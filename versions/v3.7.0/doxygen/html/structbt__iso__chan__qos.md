---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__iso__chan__qos.html
original_path: doxygen/html/structbt__iso__chan__qos.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_iso\_chan\_qos Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Isochronous channels (ISO)](group__bt__iso.md)

ISO Channel QoS structure.
[More...](#details)

`#include <[iso.h](iso_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_iso\_chan\_io\_qos](structbt__iso__chan__io__qos.md) \* | [rx](#ac231434d1798f431c4fbac5a759784a5) |
|  | Channel Receiving QoS. |
| struct [bt\_iso\_chan\_io\_qos](structbt__iso__chan__io__qos.md) \* | [tx](#a47a99a6ccfa5f1e0c9fb859e66d2e9e3) |
|  | Channel Transmission QoS. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_subevents](#a4c6bfa577f8cbd724ed2561850fd6255) |
|  | Number of subevents. |

## Detailed Description

ISO Channel QoS structure.

## Field Documentation

## [◆ ](#a4c6bfa577f8cbd724ed2561850fd6255)num\_subevents

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_chan\_qos::num\_subevents |
| --- |

Number of subevents.

Maximum number of subevents in each CIS or BIS event.

Value range [BT\_ISO\_NSE\_MIN](group__bt__iso.md#ga3eba4c20b4203b0323b14178522e6159 "BT_ISO_NSE_MIN") to [BT\_ISO\_NSE\_MAX](group__bt__iso.md#gab7637d96bde7a41123b34f487eec3436 "BT_ISO_NSE_MAX").

## [◆ ](#ac231434d1798f431c4fbac5a759784a5)rx

| struct [bt\_iso\_chan\_io\_qos](structbt__iso__chan__io__qos.md)\* bt\_iso\_chan\_qos::rx |
| --- |

Channel Receiving QoS.

Setting NULL disables data path [BT\_HCI\_DATAPATH\_DIR\_CTLR\_TO\_HOST](hci__types_8h.md#af8d89c712a3d27f9b6f92a31bea2a8c3 "BT_HCI_DATAPATH_DIR_CTLR_TO_HOST").

Can only be set for a connected isochronous channel, or a broadcast isochronous receiver.

## [◆ ](#a47a99a6ccfa5f1e0c9fb859e66d2e9e3)tx

| struct [bt\_iso\_chan\_io\_qos](structbt__iso__chan__io__qos.md)\* bt\_iso\_chan\_qos::tx |
| --- |

Channel Transmission QoS.

Setting NULL disables data path [BT\_HCI\_DATAPATH\_DIR\_HOST\_TO\_CTLR](hci__types_8h.md#a0f74c19fabbcb3088e1a819d33a05a1c "BT_HCI_DATAPATH_DIR_HOST_TO_CTLR").

Can only be set for a connected isochronous channel, or a broadcast isochronous transmitter.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[iso.h](iso_8h_source.md)

- [bt\_iso\_chan\_qos](structbt__iso__chan__qos.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
