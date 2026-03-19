---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__cap__commander__broadcast__reception__start__member__param.html
original_path: doxygen/html/structbt__cap__commander__broadcast__reception__start__member__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_commander\_broadcast\_reception\_start\_member\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Parameters part of [bt\_cap\_commander\_broadcast\_reception\_start\_param](structbt__cap__commander__broadcast__reception__start__param.md "bt_cap_commander_broadcast_reception_start_param") for [bt\_cap\_commander\_broadcast\_reception\_start()](group__bt__cap.md#ga25be83bb53c8e2ab76f311eaf4f615b9 "Starts the reception of broadcast audio on one or more remote Common Audio Profile Acceptors.").
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union [bt\_cap\_set\_member](unionbt__cap__set__member.md) | [member](#abf47aafab0b076da675182308d89bff7) |
|  | Coordinated or ad-hoc set member. |
| [bt\_addr\_le\_t](structbt__addr__le__t.md) | [addr](#a93d6b4c76e730f282d24b2086c10aa3e) |
|  | Address of the advertiser. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [adv\_sid](#acc52738756124db042ea884c82163362) |
|  | SID of the advertising set. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [pa\_interval](#a1ba6b20f822f38dd4a0ce1f8b2f2671c) |
|  | Periodic advertising interval in milliseconds. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [broadcast\_id](#a8e6d5d1004d13069739229a7eec3abc0) |
|  | 24-bit broadcast ID |
| struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) | [subgroups](#a2222f8ae46afed4760db56079779532d) [[BT\_BAP\_BASS\_MAX\_SUBGROUPS](group__bt__bap.md#ga443c212a736852305715452e7f165a9e)] |
|  | Pointer to array of subgroups. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [num\_subgroups](#a184f2623ab759832a3ec9770b14c9c63) |
|  | Number of subgroups. |

## Detailed Description

Parameters part of [bt\_cap\_commander\_broadcast\_reception\_start\_param](structbt__cap__commander__broadcast__reception__start__param.md "bt_cap_commander_broadcast_reception_start_param") for [bt\_cap\_commander\_broadcast\_reception\_start()](group__bt__cap.md#ga25be83bb53c8e2ab76f311eaf4f615b9 "Starts the reception of broadcast audio on one or more remote Common Audio Profile Acceptors.").

## Field Documentation

## [◆ ](#a93d6b4c76e730f282d24b2086c10aa3e)addr

| [bt\_addr\_le\_t](structbt__addr__le__t.md) bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::addr |
| --- |

Address of the advertiser.

## [◆ ](#acc52738756124db042ea884c82163362)adv\_sid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::adv\_sid |
| --- |

SID of the advertising set.

## [◆ ](#a8e6d5d1004d13069739229a7eec3abc0)broadcast\_id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::broadcast\_id |
| --- |

24-bit broadcast ID

## [◆ ](#abf47aafab0b076da675182308d89bff7)member

| union [bt\_cap\_set\_member](unionbt__cap__set__member.md) bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::member |
| --- |

Coordinated or ad-hoc set member.

## [◆ ](#a184f2623ab759832a3ec9770b14c9c63)num\_subgroups

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::num\_subgroups |
| --- |

Number of subgroups.

## [◆ ](#a1ba6b20f822f38dd4a0ce1f8b2f2671c)pa\_interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::pa\_interval |
| --- |

Periodic advertising interval in milliseconds.

BT\_BAP\_PA\_INTERVAL\_UNKNOWN if unknown.

## [◆ ](#a2222f8ae46afed4760db56079779532d)subgroups

| struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::subgroups[[BT\_BAP\_BASS\_MAX\_SUBGROUPS](group__bt__bap.md#ga443c212a736852305715452e7f165a9e)] |
| --- |

Pointer to array of subgroups.

At least one bit in one of the subgroups bis\_sync parameters shall be set.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_commander\_broadcast\_reception\_start\_member\_param](structbt__cap__commander__broadcast__reception__start__member__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
