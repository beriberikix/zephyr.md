---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__le__adv__param.html
original_path: doxygen/html/structbt__le__adv__param.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_adv\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

LE Advertising Parameters.
[More...](#details)

`#include <[bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [id](#af957bd92b949536af2b2db0db7b2b425) |
|  | Local identity. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sid](#a6e2f0e1b76495afe7fe661e8698d0909) |
|  | Advertising Set Identifier, valid range 0x00 - 0x0f. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [secondary\_max\_skip](#a9911e9bfc97ff0c48a6decae3f922e95) |
|  | Secondary channel maximum skip count. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [options](#a2a978c60153eb03697769bc72928f4ef) |
|  | Bit-field of advertising options. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [interval\_min](#aca8ff5a4f5d29184535162f007b2d39e) |
|  | Minimum Advertising Interval (N \* 0.625 milliseconds) Minimum Advertising Interval shall be less than or equal to the Maximum Advertising Interval. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [interval\_max](#afeba6973dca99d8ee818fdde0c22cb59) |
|  | Maximum Advertising Interval (N \* 0.625 milliseconds) Minimum Advertising Interval shall be less than or equal to the Maximum Advertising Interval. |
| const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | [peer](#a4cf31f54f067fffa3c848adc2ffd7119) |
|  | Directed advertising to peer. |

## Detailed Description

LE Advertising Parameters.

## Field Documentation

## [◆ ](#af957bd92b949536af2b2db0db7b2b425)id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_adv\_param::id |
| --- |

Local identity.

Note
:   When extended advertising `CONFIG_BT_EXT_ADV` is not enabled or not supported by the controller it is not possible to scan and advertise simultaneously using two different random addresses.

## [◆ ](#afeba6973dca99d8ee818fdde0c22cb59)interval\_max

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_le\_adv\_param::interval\_max |
| --- |

Maximum Advertising Interval (N \* 0.625 milliseconds) Minimum Advertising Interval shall be less than or equal to the Maximum Advertising Interval.

The Minimum Advertising Interval and Maximum Advertising Interval should not be the same value (as stated in Bluetooth Core Spec 5.2, section 7.8.5) Range: 0x0020 to 0x4000

## [◆ ](#aca8ff5a4f5d29184535162f007b2d39e)interval\_min

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_le\_adv\_param::interval\_min |
| --- |

Minimum Advertising Interval (N \* 0.625 milliseconds) Minimum Advertising Interval shall be less than or equal to the Maximum Advertising Interval.

The Minimum Advertising Interval and Maximum Advertising Interval should not be the same value (as stated in Bluetooth Core Spec 5.2, section 7.8.5) Range: 0x0020 to 0x4000

## [◆ ](#a2a978c60153eb03697769bc72928f4ef)options

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_le\_adv\_param::options |
| --- |

Bit-field of advertising options.

## [◆ ](#a4cf31f54f067fffa3c848adc2ffd7119)peer

| const [bt\_addr\_le\_t](structbt__addr__le__t.md)\* bt\_le\_adv\_param::peer |
| --- |

Directed advertising to peer.

When this parameter is set the advertiser will send directed advertising to the remote device.

The advertising type will either be high duty cycle, or low duty cycle if the BT\_LE\_ADV\_OPT\_DIR\_MODE\_LOW\_DUTY option is enabled. When using [BT\_LE\_ADV\_OPT\_EXT\_ADV](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab "BT_LE_ADV_OPT_EXT_ADV") then only low duty cycle is allowed.

In case of connectable high duty cycle if the connection could not be established within the timeout the connected() callback will be called with the status set to [BT\_HCI\_ERR\_ADV\_TIMEOUT](hci__types_8h.md#abfa408d8366ff3cae1cd35fffcda30c0 "BT_HCI_ERR_ADV_TIMEOUT").

## [◆ ](#a9911e9bfc97ff0c48a6decae3f922e95)secondary\_max\_skip

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_adv\_param::secondary\_max\_skip |
| --- |

Secondary channel maximum skip count.

Maximum advertising events the advertiser can skip before it must send advertising data on the secondary advertising channel.

Note
:   Requires [BT\_LE\_ADV\_OPT\_EXT\_ADV](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab "BT_LE_ADV_OPT_EXT_ADV")

## [◆ ](#a6e2f0e1b76495afe7fe661e8698d0909)sid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_adv\_param::sid |
| --- |

Advertising Set Identifier, valid range 0x00 - 0x0f.

Note
:   Requires [BT\_LE\_ADV\_OPT\_EXT\_ADV](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab "BT_LE_ADV_OPT_EXT_ADV")

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_adv\_param](structbt__le__adv__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
