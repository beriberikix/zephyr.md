---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__bap__scan__delegator__add__src__param.html
original_path: doxygen/html/structbt__bap__scan__delegator__add__src__param.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_scan\_delegator\_add\_src\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct bt\_le\_per\_adv\_sync \* | [pa\_sync](#a7e2ae6194fe7878e6f8d4967f005c7aa) |
|  | The periodic adverting sync. |
| enum [bt\_bap\_big\_enc\_state](group__bt__bap.md#ga5e0b0f70d247e131fa542fae16826a22) | [encrypt\_state](#a502d263982995c99559714f07d74443f) |
|  | The broadcast isochronous group encryption state. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [broadcast\_id](#a8e8eda4139e460800c6195b4c5f246e2) |
|  | The 24-bit broadcast ID. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_subgroups](#a12bed26ffdc9d4683a5fcdf512a194eb) |
|  | Number of subgroups. |
| struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) | [subgroups](#a9153dbdef5b507ef14e73a188cb00ae1) [CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS] |
|  | Subgroup specific information. |

## Field Documentation

## [◆ ](#a8e8eda4139e460800c6195b4c5f246e2)broadcast\_id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_bap\_scan\_delegator\_add\_src\_param::broadcast\_id |
| --- |

The 24-bit broadcast ID.

## [◆ ](#a502d263982995c99559714f07d74443f)encrypt\_state

| enum [bt\_bap\_big\_enc\_state](group__bt__bap.md#ga5e0b0f70d247e131fa542fae16826a22) bt\_bap\_scan\_delegator\_add\_src\_param::encrypt\_state |
| --- |

The broadcast isochronous group encryption state.

## [◆ ](#a12bed26ffdc9d4683a5fcdf512a194eb)num\_subgroups

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_scan\_delegator\_add\_src\_param::num\_subgroups |
| --- |

Number of subgroups.

## [◆ ](#a7e2ae6194fe7878e6f8d4967f005c7aa)pa\_sync

| struct bt\_le\_per\_adv\_sync\* bt\_bap\_scan\_delegator\_add\_src\_param::pa\_sync |
| --- |

The periodic adverting sync.

## [◆ ](#a9153dbdef5b507ef14e73a188cb00ae1)subgroups

| struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) bt\_bap\_scan\_delegator\_add\_src\_param::subgroups[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS] |
| --- |

Subgroup specific information.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_scan\_delegator\_add\_src\_param](structbt__bap__scan__delegator__add__src__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
