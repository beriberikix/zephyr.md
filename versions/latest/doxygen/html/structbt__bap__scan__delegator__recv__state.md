---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__bap__scan__delegator__recv__state.html
original_path: doxygen/html/structbt__bap__scan__delegator__recv__state.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_scan\_delegator\_recv\_state Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md)

Represents the Broadcast Audio Scan Service receive state.
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [src\_id](#a1755a6332c86aeaf624d3c540037772a) |
|  | The source ID. |
| [bt\_addr\_le\_t](structbt__addr__le__t.md) | [addr](#a6153ea6bbfe7057c39f6b652a4e6e34e) |
|  | The Bluetooth address. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [adv\_sid](#aa03e02a1832950e4a53ff2fe803c14a6) |
|  | The advertising set ID. |
| enum [bt\_bap\_pa\_state](group__bt__bap.md#gac551e9b0d53fd50f3a9e9c08447f0296) | [pa\_sync\_state](#a30fbad06780fd7bca9aacdf14ecaf4a0) |
|  | The periodic adverting sync state. |
| enum [bt\_bap\_big\_enc\_state](group__bt__bap.md#ga5e0b0f70d247e131fa542fae16826a22) | [encrypt\_state](#ac770a5ad001f73d3acaf2b36827f9343) |
|  | The broadcast isochronous group encryption state. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [broadcast\_id](#abaa80f30cf2e84ee873d18eaedd4159d) |
|  | The 24-bit broadcast ID. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bad\_code](#a3fb5ae9266643182798ef056d1569821) [16] |
|  | The bad broadcast code. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_subgroups](#aa97765bdbaa43a280645eb62c0035b82) |
|  | Number of subgroups. |
| struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) | [subgroups](#ae674ccfdc1905f230b0f7a58cc553274) [CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS] |
|  | Subgroup specific information. |

## Detailed Description

Represents the Broadcast Audio Scan Service receive state.

## Field Documentation

## [◆ ](#a6153ea6bbfe7057c39f6b652a4e6e34e)addr

| [bt\_addr\_le\_t](structbt__addr__le__t.md) bt\_bap\_scan\_delegator\_recv\_state::addr |
| --- |

The Bluetooth address.

## [◆ ](#aa03e02a1832950e4a53ff2fe803c14a6)adv\_sid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_scan\_delegator\_recv\_state::adv\_sid |
| --- |

The advertising set ID.

## [◆ ](#a3fb5ae9266643182798ef056d1569821)bad\_code

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_scan\_delegator\_recv\_state::bad\_code[16] |
| --- |

The bad broadcast code.

Only valid if encrypt\_state is [BT\_BAP\_BIG\_ENC\_STATE\_BCODE\_REQ](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22a27fa0c62c91f8be8f4097a0e89d219d2 "BT_BAP_BIG_ENC_STATE_BCODE_REQ")

## [◆ ](#abaa80f30cf2e84ee873d18eaedd4159d)broadcast\_id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_bap\_scan\_delegator\_recv\_state::broadcast\_id |
| --- |

The 24-bit broadcast ID.

## [◆ ](#ac770a5ad001f73d3acaf2b36827f9343)encrypt\_state

| enum [bt\_bap\_big\_enc\_state](group__bt__bap.md#ga5e0b0f70d247e131fa542fae16826a22) bt\_bap\_scan\_delegator\_recv\_state::encrypt\_state |
| --- |

The broadcast isochronous group encryption state.

## [◆ ](#aa97765bdbaa43a280645eb62c0035b82)num\_subgroups

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_scan\_delegator\_recv\_state::num\_subgroups |
| --- |

Number of subgroups.

## [◆ ](#a30fbad06780fd7bca9aacdf14ecaf4a0)pa\_sync\_state

| enum [bt\_bap\_pa\_state](group__bt__bap.md#gac551e9b0d53fd50f3a9e9c08447f0296) bt\_bap\_scan\_delegator\_recv\_state::pa\_sync\_state |
| --- |

The periodic adverting sync state.

## [◆ ](#a1755a6332c86aeaf624d3c540037772a)src\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_scan\_delegator\_recv\_state::src\_id |
| --- |

The source ID.

## [◆ ](#ae674ccfdc1905f230b0f7a58cc553274)subgroups

| struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) bt\_bap\_scan\_delegator\_recv\_state::subgroups[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS] |
| --- |

Subgroup specific information.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
