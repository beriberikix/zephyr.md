---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__le__per__adv__sync__synced__info.html
original_path: doxygen/html/structbt__le__per__adv__sync__synced__info.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_per\_adv\_sync\_synced\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

Information about the successful synchronization with periodic advertising.
[More...](#details)

`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | [addr](#a7ca99b0596b08d153d3ba5310adab125) |
|  | Advertiser LE address and type. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sid](#a5489c3038f7fff596316a456fc8d580b) |
|  | Advertising Set Identifier, valid range [BT\_GAP\_SID\_MIN](group__bt__gap__defines.md#gacf05b7660d2ae85f64e2a220abf8e57d "BT_GAP_SID_MIN") to [BT\_GAP\_SID\_MAX](group__bt__gap__defines.md#gafa6f803fe3ada07030fb1f2f725940c4 "BT_GAP_SID_MAX"). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [interval](#a5304e1826face35c506f3b8f6cad7df2) |
|  | Periodic advertising interval (N \* 1.25 ms). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [phy](#a8b7709011541e95ceaeac379cc3143bb) |
|  | Advertiser PHY (see [bt\_gap\_le\_phy](group__bt__gap__defines.md#ga691d9793fd21c41b2c192d65cc2bf6c4 "bt_gap_le_phy")). |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [recv\_enabled](#a0dd4b7646da0fadc48e94ff3dc91ef83) |
|  | True if receiving periodic advertisements, false otherwise. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [service\_data](#adee2bdafa86a0c3c1dfb4660e85396a3) |
|  | Service Data provided by the peer when sync is transferred. |
| struct bt\_conn \* | [conn](#ada4cda53aa87f29d54f6cd88134efe14) |
|  | Peer that transferred the periodic advertising sync. |

## Detailed Description

Information about the successful synchronization with periodic advertising.

This struct provides information about the periodic advertising sync once it has been successfully established. It includes the advertiser's address, SID, the advertising interval, PHY, and the synchronization state. It also contains details about the sync, such as service data and the peer device that transferred the sync. When using periodic advertising response (configured via `CONFIG_BT_PER_ADV_SYNC_RSP`), additional details such as subevent information and response timings are provided.

Note
:   Used in [bt\_le\_per\_adv\_sync\_cb](structbt__le__per__adv__sync__cb.md "bt_le_per_adv_sync_cb") structure.

## Field Documentation

## [◆ ](#a7ca99b0596b08d153d3ba5310adab125)addr

| const [bt\_addr\_le\_t](structbt__addr__le__t.md)\* bt\_le\_per\_adv\_sync\_synced\_info::addr |
| --- |

Advertiser LE address and type.

## [◆ ](#ada4cda53aa87f29d54f6cd88134efe14)conn

| struct bt\_conn\* bt\_le\_per\_adv\_sync\_synced\_info::conn |
| --- |

Peer that transferred the periodic advertising sync.

Will always be NULL when the sync is locally created.

## [◆ ](#a5304e1826face35c506f3b8f6cad7df2)interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_per\_adv\_sync\_synced\_info::interval |
| --- |

Periodic advertising interval (N \* 1.25 ms).

## [◆ ](#a8b7709011541e95ceaeac379cc3143bb)phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_sync\_synced\_info::phy |
| --- |

Advertiser PHY (see [bt\_gap\_le\_phy](group__bt__gap__defines.md#ga691d9793fd21c41b2c192d65cc2bf6c4 "bt_gap_le_phy")).

## [◆ ](#a0dd4b7646da0fadc48e94ff3dc91ef83)recv\_enabled

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_le\_per\_adv\_sync\_synced\_info::recv\_enabled |
| --- |

True if receiving periodic advertisements, false otherwise.

## [◆ ](#adee2bdafa86a0c3c1dfb4660e85396a3)service\_data

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_per\_adv\_sync\_synced\_info::service\_data |
| --- |

Service Data provided by the peer when sync is transferred.

Will always be 0 when the sync is locally created.

## [◆ ](#a5489c3038f7fff596316a456fc8d580b)sid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_sync\_synced\_info::sid |
| --- |

Advertising Set Identifier, valid range [BT\_GAP\_SID\_MIN](group__bt__gap__defines.md#gacf05b7660d2ae85f64e2a220abf8e57d "BT_GAP_SID_MIN") to [BT\_GAP\_SID\_MAX](group__bt__gap__defines.md#gafa6f803fe3ada07030fb1f2f725940c4 "BT_GAP_SID_MAX").

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_per\_adv\_sync\_synced\_info](structbt__le__per__adv__sync__synced__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
