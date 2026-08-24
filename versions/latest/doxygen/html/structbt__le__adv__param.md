---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__le__adv__param.html
original_path: doxygen/html/structbt__le__adv__param.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_adv\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

LE Advertising Parameters.
[More...](#details)

`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [id](#af957bd92b949536af2b2db0db7b2b425) |
|  | Local identity handle. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sid](#a6e2f0e1b76495afe7fe661e8698d0909) |
|  | Advertising Set Identifier, valid range is [BT\_GAP\_SID\_MIN](group__bt__gap__defines.md#gacf05b7660d2ae85f64e2a220abf8e57d "BT_GAP_SID_MIN") to [BT\_GAP\_SID\_MAX](group__bt__gap__defines.md#gafa6f803fe3ada07030fb1f2f725940c4 "BT_GAP_SID_MAX"). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [secondary\_max\_skip](#a9911e9bfc97ff0c48a6decae3f922e95) |
|  | Secondary channel maximum skip count. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [options](#a2a978c60153eb03697769bc72928f4ef) |
|  | Bit-field of advertising options, see the [bt\_le\_adv\_opt](group__bt__gap.md#gafbf81dab68b0e484d4742471c722fc28 "bt_le_adv_opt") field. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [interval\_min](#aca8ff5a4f5d29184535162f007b2d39e) |
|  | Minimum Advertising Interval (N \* 0.625 milliseconds). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [interval\_max](#afeba6973dca99d8ee818fdde0c22cb59) |
|  | Maximum Advertising Interval (N \* 0.625 milliseconds). |
| const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | [peer](#a4cf31f54f067fffa3c848adc2ffd7119) |
|  | Directed advertising to peer. |

## Detailed Description

LE Advertising Parameters.

## Field Documentation

## [◆ ](#af957bd92b949536af2b2db0db7b2b425)id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_adv\_param::id |
| --- |

Local identity handle.

The index of the identity address in the local Bluetooth controller.

Note
:   When extended advertising `CONFIG_BT_EXT_ADV` is not enabled or not supported by the controller it is not possible to scan and advertise simultaneously using two different random addresses.

## [◆ ](#afeba6973dca99d8ee818fdde0c22cb59)interval\_max

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_le\_adv\_param::interval\_max |
| --- |

Maximum Advertising Interval (N \* 0.625 milliseconds).

The Maximum Advertising Interval shall be more than or equal to the Minimum Advertising Interval. The Minimum Advertising Interval and Maximum Advertising Interval aren't recommended to be the same value to enable the Controller to determine the best advertising interval given other activities. (See Bluetooth Core Spec 6.0, Vol 4, Part E, section 7.8.5) Range: 0x0020 to 0x4000

## [◆ ](#aca8ff5a4f5d29184535162f007b2d39e)interval\_min

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_le\_adv\_param::interval\_min |
| --- |

Minimum Advertising Interval (N \* 0.625 milliseconds).

The Minimum Advertising Interval shall be less than or equal to the Maximum Advertising Interval. The Minimum Advertising Interval and Maximum Advertising Interval aren't recommended to be the same value to enable the Controller to determine the best advertising interval given other activities. (See Bluetooth Core Spec 6.0, Vol 4, Part E, section 7.8.5) Range: 0x0020 to 0x4000

## [◆ ](#a2a978c60153eb03697769bc72928f4ef)options

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_le\_adv\_param::options |
| --- |

Bit-field of advertising options, see the [bt\_le\_adv\_opt](group__bt__gap.md#gafbf81dab68b0e484d4742471c722fc28 "bt_le_adv_opt") field.

## [◆ ](#a4cf31f54f067fffa3c848adc2ffd7119)peer

| const [bt\_addr\_le\_t](structbt__addr__le__t.md)\* bt\_le\_adv\_param::peer |
| --- |

Directed advertising to peer.

When this parameter is set the advertiser will send directed advertising to the remote device.

The advertising type will either be high duty cycle, or low duty cycle if the [BT\_LE\_ADV\_OPT\_DIR\_MODE\_LOW\_DUTY](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28afd164ec5476f5e2d9aedf50032946872 "BT_LE_ADV_OPT_DIR_MODE_LOW_DUTY") option is enabled. When using [BT\_LE\_ADV\_OPT\_EXT\_ADV](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28ae33ae9d8e43cce82e47fa73999d415ab "BT_LE_ADV_OPT_EXT_ADV") then only low duty cycle is allowed.

In case of connectable high duty cycle if the connection could not be established within the timeout the connected callback will be called with the status set to [BT\_HCI\_ERR\_ADV\_TIMEOUT](hci__types_8h.md#abfa408d8366ff3cae1cd35fffcda30c0 "BT_HCI_ERR_ADV_TIMEOUT").

## [◆ ](#a9911e9bfc97ff0c48a6decae3f922e95)secondary\_max\_skip

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_adv\_param::secondary\_max\_skip |
| --- |

Secondary channel maximum skip count.

Maximum advertising events the advertiser can skip before it must send advertising data on the secondary advertising channel.

Note
:   Requires [BT\_LE\_ADV\_OPT\_EXT\_ADV](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28ae33ae9d8e43cce82e47fa73999d415ab "BT_LE_ADV_OPT_EXT_ADV") bit (see [bt\_le\_adv\_opt](group__bt__gap.md#gafbf81dab68b0e484d4742471c722fc28 "bt_le_adv_opt") field) to be set as [bt\_le\_adv\_param::options](#a2a978c60153eb03697769bc72928f4ef).

## [◆ ](#a6e2f0e1b76495afe7fe661e8698d0909)sid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_adv\_param::sid |
| --- |

Advertising Set Identifier, valid range is [BT\_GAP\_SID\_MIN](group__bt__gap__defines.md#gacf05b7660d2ae85f64e2a220abf8e57d "BT_GAP_SID_MIN") to [BT\_GAP\_SID\_MAX](group__bt__gap__defines.md#gafa6f803fe3ada07030fb1f2f725940c4 "BT_GAP_SID_MAX").

Note
:   Requires [BT\_LE\_ADV\_OPT\_EXT\_ADV](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28ae33ae9d8e43cce82e47fa73999d415ab "BT_LE_ADV_OPT_EXT_ADV") bit (see [bt\_le\_adv\_opt](group__bt__gap.md#gafbf81dab68b0e484d4742471c722fc28 "bt_le_adv_opt") field) to be set as [bt\_le\_adv\_param::options](#a2a978c60153eb03697769bc72928f4ef).

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_adv\_param](structbt__le__adv__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
