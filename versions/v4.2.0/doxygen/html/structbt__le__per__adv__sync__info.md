---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__le__per__adv__sync__info.html
original_path: doxygen/html/structbt__le__per__adv__sync__info.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_per\_adv\_sync\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

Periodic advertising set info structure.
[More...](#details)

`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bt\_addr\_le\_t](structbt__addr__le__t.md) | [addr](#ac10fc2e2d3ec2160db8c2aac148d18a2) |
|  | Periodic Advertiser Address. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sid](#acc0ef26c38279c9a67f8992005c2e58a) |
|  | Advertising Set Identifier, valid range [BT\_GAP\_SID\_MIN](group__bt__gap__defines.md#gacf05b7660d2ae85f64e2a220abf8e57d "BT_GAP_SID_MIN") to [BT\_GAP\_SID\_MAX](group__bt__gap__defines.md#gafa6f803fe3ada07030fb1f2f725940c4 "BT_GAP_SID_MAX"). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [interval](#a365a0d8577429e4ee96e977071c9a906) |
|  | Periodic advertising interval (N \* 1.25 ms). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [phy](#a4d9520ea6a803f8fe4f41190f55c26e5) |
|  | Advertiser PHY (see [bt\_gap\_le\_phy](group__bt__gap__defines.md#ga691d9793fd21c41b2c192d65cc2bf6c4 "bt_gap_le_phy")). |

## Detailed Description

Periodic advertising set info structure.

## Field Documentation

## [◆ ](#ac10fc2e2d3ec2160db8c2aac148d18a2)addr

| [bt\_addr\_le\_t](structbt__addr__le__t.md) bt\_le\_per\_adv\_sync\_info::addr |
| --- |

Periodic Advertiser Address.

## [◆ ](#a365a0d8577429e4ee96e977071c9a906)interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_per\_adv\_sync\_info::interval |
| --- |

Periodic advertising interval (N \* 1.25 ms).

## [◆ ](#a4d9520ea6a803f8fe4f41190f55c26e5)phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_sync\_info::phy |
| --- |

Advertiser PHY (see [bt\_gap\_le\_phy](group__bt__gap__defines.md#ga691d9793fd21c41b2c192d65cc2bf6c4 "bt_gap_le_phy")).

## [◆ ](#acc0ef26c38279c9a67f8992005c2e58a)sid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_sync\_info::sid |
| --- |

Advertising Set Identifier, valid range [BT\_GAP\_SID\_MIN](group__bt__gap__defines.md#gacf05b7660d2ae85f64e2a220abf8e57d "BT_GAP_SID_MIN") to [BT\_GAP\_SID\_MAX](group__bt__gap__defines.md#gafa6f803fe3ada07030fb1f2f725940c4 "BT_GAP_SID_MAX").

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_per\_adv\_sync\_info](structbt__le__per__adv__sync__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
