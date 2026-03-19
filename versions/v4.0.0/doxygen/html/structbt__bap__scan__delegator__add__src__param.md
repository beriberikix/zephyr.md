---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__bap__scan__delegator__add__src__param.html
original_path: doxygen/html/structbt__bap__scan__delegator__add__src__param.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_scan\_delegator\_add\_src\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md)

Parameters for [bt\_bap\_scan\_delegator\_add\_src()](group__bt__bap.md#ga6eb2a782d761da12d112356cfe723ff0 "Add a receive state source locally.").
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bt\_addr\_le\_t](structbt__addr__le__t.md) | [addr](#a751106648b8f040747b5ffb804932798) |
|  | Periodic Advertiser Address. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sid](#a80817dd3bc046d76baabd62e470ad797) |
|  | Advertiser SID. |
| enum [bt\_bap\_big\_enc\_state](group__bt__bap.md#ga5e0b0f70d247e131fa542fae16826a22) | [encrypt\_state](#a502d263982995c99559714f07d74443f) |
|  | The broadcast isochronous group encryption state. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [broadcast\_id](#a8e8eda4139e460800c6195b4c5f246e2) |
|  | The 24-bit broadcast ID. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_subgroups](#a12bed26ffdc9d4683a5fcdf512a194eb) |
|  | Number of subgroups. |
| struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) | [subgroups](#a9153dbdef5b507ef14e73a188cb00ae1) [CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS] |
|  | Subgroup specific information. |

## Detailed Description

Parameters for [bt\_bap\_scan\_delegator\_add\_src()](group__bt__bap.md#ga6eb2a782d761da12d112356cfe723ff0 "Add a receive state source locally.").

## Field Documentation

## [◆ ](#a751106648b8f040747b5ffb804932798)addr

| [bt\_addr\_le\_t](structbt__addr__le__t.md) bt\_bap\_scan\_delegator\_add\_src\_param::addr |
| --- |

Periodic Advertiser Address.

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

## [◆ ](#a80817dd3bc046d76baabd62e470ad797)sid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_scan\_delegator\_add\_src\_param::sid |
| --- |

Advertiser SID.

## [◆ ](#a9153dbdef5b507ef14e73a188cb00ae1)subgroups

| struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) bt\_bap\_scan\_delegator\_add\_src\_param::subgroups[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS] |
| --- |

Subgroup specific information.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_scan\_delegator\_add\_src\_param](structbt__bap__scan__delegator__add__src__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
