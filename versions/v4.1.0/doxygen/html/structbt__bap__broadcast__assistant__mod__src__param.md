---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__bap__broadcast__assistant__mod__src__param.html
original_path: doxygen/html/structbt__bap__broadcast__assistant__mod__src__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_broadcast\_assistant\_mod\_src\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md)

Parameters for modifying a source.
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [src\_id](#a5bc7c0a491872d655296bbb979402a62) |
|  | Source ID of the receive state. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pa\_sync](#a794bb68c8a73edfe3d44dbe9a0bf2830) |
|  | Whether to sync to periodic advertisements. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [pa\_interval](#aebaa104384dcbec7bb952a27f3acc24d) |
|  | Periodic advertising interval. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_subgroups](#a42b12c6d9f5c622433c9c1f0c72726c1) |
|  | Number of subgroups. |
| struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) \* | [subgroups](#a2383ec98b14054e0bc66bb4a0ae7b8b6) |
|  | Pointer to array of subgroups. |

## Detailed Description

Parameters for modifying a source.

## Field Documentation

## [◆ ](#a42b12c6d9f5c622433c9c1f0c72726c1)num\_subgroups

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_broadcast\_assistant\_mod\_src\_param::num\_subgroups |
| --- |

Number of subgroups.

## [◆ ](#aebaa104384dcbec7bb952a27f3acc24d)pa\_interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_bap\_broadcast\_assistant\_mod\_src\_param::pa\_interval |
| --- |

Periodic advertising interval.

BT\_BAP\_PA\_INTERVAL\_UNKNOWN if unknown.

## [◆ ](#a794bb68c8a73edfe3d44dbe9a0bf2830)pa\_sync

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_bap\_broadcast\_assistant\_mod\_src\_param::pa\_sync |
| --- |

Whether to sync to periodic advertisements.

## [◆ ](#a5bc7c0a491872d655296bbb979402a62)src\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_broadcast\_assistant\_mod\_src\_param::src\_id |
| --- |

Source ID of the receive state.

## [◆ ](#a2383ec98b14054e0bc66bb4a0ae7b8b6)subgroups

| struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md)\* bt\_bap\_broadcast\_assistant\_mod\_src\_param::subgroups |
| --- |

Pointer to array of subgroups.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_broadcast\_assistant\_mod\_src\_param](structbt__bap__broadcast__assistant__mod__src__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
