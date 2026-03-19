---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__bap__broadcast__assistant__add__src__param.html
original_path: doxygen/html/structbt__bap__broadcast__assistant__add__src__param.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_broadcast\_assistant\_add\_src\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md)

Parameters for adding a source to a Broadcast Audio Scan Service server.
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bt\_addr\_le\_t](structbt__addr__le__t.md) | [addr](#a2b04d75ca9a740a7d819eae1bcc5cba7) |
|  | Address of the advertiser. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [adv\_sid](#a390cd8d887cd256ee74b39b9b516cac4) |
|  | SID of the advertising set. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pa\_sync](#ad9af814e8a232230d4ee97c459f47747) |
|  | Whether to sync to periodic advertisements. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [broadcast\_id](#ae50b6b5a3f2c92f01e7070c605b37dde) |
|  | 24-bit broadcast ID |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [pa\_interval](#acaecbbf7b3c96fe5ca53f90e92fa1e5e) |
|  | Periodic advertising interval in milliseconds. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_subgroups](#a17b67d65b6840c3d4480027b7deb31a5) |
|  | Number of subgroups. |
| struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) \* | [subgroups](#ab8423e5cce4a6c9ac142221d2e816763) |
|  | Pointer to array of subgroups. |

## Detailed Description

Parameters for adding a source to a Broadcast Audio Scan Service server.

## Field Documentation

## [◆ ](#a2b04d75ca9a740a7d819eae1bcc5cba7)addr

| [bt\_addr\_le\_t](structbt__addr__le__t.md) bt\_bap\_broadcast\_assistant\_add\_src\_param::addr |
| --- |

Address of the advertiser.

## [◆ ](#a390cd8d887cd256ee74b39b9b516cac4)adv\_sid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_broadcast\_assistant\_add\_src\_param::adv\_sid |
| --- |

SID of the advertising set.

## [◆ ](#ae50b6b5a3f2c92f01e7070c605b37dde)broadcast\_id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_bap\_broadcast\_assistant\_add\_src\_param::broadcast\_id |
| --- |

24-bit broadcast ID

## [◆ ](#a17b67d65b6840c3d4480027b7deb31a5)num\_subgroups

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_broadcast\_assistant\_add\_src\_param::num\_subgroups |
| --- |

Number of subgroups.

## [◆ ](#acaecbbf7b3c96fe5ca53f90e92fa1e5e)pa\_interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_bap\_broadcast\_assistant\_add\_src\_param::pa\_interval |
| --- |

Periodic advertising interval in milliseconds.

BT\_BAP\_PA\_INTERVAL\_UNKNOWN if unknown.

## [◆ ](#ad9af814e8a232230d4ee97c459f47747)pa\_sync

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_bap\_broadcast\_assistant\_add\_src\_param::pa\_sync |
| --- |

Whether to sync to periodic advertisements.

## [◆ ](#ab8423e5cce4a6c9ac142221d2e816763)subgroups

| struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md)\* bt\_bap\_broadcast\_assistant\_add\_src\_param::subgroups |
| --- |

Pointer to array of subgroups.

The [bt\_bap\_bass\_subgroup::bis\_sync](structbt__bap__bass__subgroup.md#ac8061995eb73ba30e335e37714396ff5 "bt_bap_bass_subgroup::bis_sync") value can be set to BT\_BAP\_BIS\_SYNC\_NO\_PREF to let the broadcast sink decide which BIS to synchronize to.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_broadcast\_assistant\_add\_src\_param](structbt__bap__broadcast__assistant__add__src__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
