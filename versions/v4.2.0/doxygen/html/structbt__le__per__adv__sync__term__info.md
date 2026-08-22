---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__le__per__adv__sync__term__info.html
original_path: doxygen/html/structbt__le__per__adv__sync__term__info.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_per\_adv\_sync\_term\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

Information about the termination of a periodic advertising sync.
[More...](#details)

`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | [addr](#a2b76ccd5e4c9933f2c05db2ec5b8e2fc) |
|  | Advertiser LE address and type. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sid](#a7a5f2ecccaf698bad86f10d9a7d16189) |
|  | Advertising Set Identifier, valid range [BT\_GAP\_SID\_MIN](group__bt__gap__defines.md#gacf05b7660d2ae85f64e2a220abf8e57d "BT_GAP_SID_MIN") to [BT\_GAP\_SID\_MAX](group__bt__gap__defines.md#gafa6f803fe3ada07030fb1f2f725940c4 "BT_GAP_SID_MAX"). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [reason](#a429b8b665eacbfe9db013a571b829bac) |
|  | Cause of periodic advertising termination (see the BT\_HCI\_ERR\_\* values). |

## Detailed Description

Information about the termination of a periodic advertising sync.

This struct provides information about the termination of a periodic advertising sync. It includes the advertiser’s address and SID, along with the reason for the sync termination. This information is provided in the callback when the sync is terminated, either due to a local or remote request, or due to missing data (e.g., out of range or lost sync).

Note
:   Used in [bt\_le\_per\_adv\_sync\_cb](structbt__le__per__adv__sync__cb.md "bt_le_per_adv_sync_cb") structure.

## Field Documentation

## [◆ ](#a2b76ccd5e4c9933f2c05db2ec5b8e2fc)addr

| const [bt\_addr\_le\_t](structbt__addr__le__t.md)\* bt\_le\_per\_adv\_sync\_term\_info::addr |
| --- |

Advertiser LE address and type.

## [◆ ](#a429b8b665eacbfe9db013a571b829bac)reason

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_sync\_term\_info::reason |
| --- |

Cause of periodic advertising termination (see the BT\_HCI\_ERR\_\* values).

## [◆ ](#a7a5f2ecccaf698bad86f10d9a7d16189)sid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_sync\_term\_info::sid |
| --- |

Advertising Set Identifier, valid range [BT\_GAP\_SID\_MIN](group__bt__gap__defines.md#gacf05b7660d2ae85f64e2a220abf8e57d "BT_GAP_SID_MIN") to [BT\_GAP\_SID\_MAX](group__bt__gap__defines.md#gafa6f803fe3ada07030fb1f2f725940c4 "BT_GAP_SID_MAX").

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_per\_adv\_sync\_term\_info](structbt__le__per__adv__sync__term__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
