---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__bap__scan__delegator__mod__src__param.html
original_path: doxygen/html/structbt__bap__scan__delegator__mod__src__param.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_scan\_delegator\_mod\_src\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md)

Parameters for [bt\_bap\_scan\_delegator\_mod\_src()](group__bt__bap.md#gac022f38269742f16ff6887840ef5ba9a "Add a receive state source locally.").
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [src\_id](#ae387a2c0613545ae3acd372780f738bb) |
|  | The periodic adverting sync. |
| enum [bt\_bap\_big\_enc\_state](group__bt__bap.md#ga5e0b0f70d247e131fa542fae16826a22) | [encrypt\_state](#aecc8b74632dcb2b17b9a358e00c75d31) |
|  | The broadcast isochronous group encryption state. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [broadcast\_id](#a11b4c6d787bd2c828e565282daf5cf2f) |
|  | The 24-bit broadcast ID. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_subgroups](#aa8dcd7983005ffd23779db6b6ccfb752) |
|  | Number of subgroups. |
| struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) | [subgroups](#a14ffee52751dd152b1a8cc0822d1702f) [CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS] |
|  | Subgroup specific information. |

## Detailed Description

Parameters for [bt\_bap\_scan\_delegator\_mod\_src()](group__bt__bap.md#gac022f38269742f16ff6887840ef5ba9a "Add a receive state source locally.").

## Field Documentation

## [◆ ](#a11b4c6d787bd2c828e565282daf5cf2f)broadcast\_id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_bap\_scan\_delegator\_mod\_src\_param::broadcast\_id |
| --- |

The 24-bit broadcast ID.

## [◆ ](#aecc8b74632dcb2b17b9a358e00c75d31)encrypt\_state

| enum [bt\_bap\_big\_enc\_state](group__bt__bap.md#ga5e0b0f70d247e131fa542fae16826a22) bt\_bap\_scan\_delegator\_mod\_src\_param::encrypt\_state |
| --- |

The broadcast isochronous group encryption state.

## [◆ ](#aa8dcd7983005ffd23779db6b6ccfb752)num\_subgroups

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_scan\_delegator\_mod\_src\_param::num\_subgroups |
| --- |

Number of subgroups.

## [◆ ](#ae387a2c0613545ae3acd372780f738bb)src\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_scan\_delegator\_mod\_src\_param::src\_id |
| --- |

The periodic adverting sync.

## [◆ ](#a14ffee52751dd152b1a8cc0822d1702f)subgroups

| struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) bt\_bap\_scan\_delegator\_mod\_src\_param::subgroups[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS] |
| --- |

Subgroup specific information.

If a subgroup's metadata\_len is set to 0, the existing metadata for the subgroup will remain unchanged

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_scan\_delegator\_mod\_src\_param](structbt__bap__scan__delegator__mod__src__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
