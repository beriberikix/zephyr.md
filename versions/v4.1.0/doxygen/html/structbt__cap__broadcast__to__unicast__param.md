---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__cap__broadcast__to__unicast__param.html
original_path: doxygen/html/structbt__cap__broadcast__to__unicast__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_broadcast\_to\_unicast\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Parameters for [bt\_cap\_initiator\_broadcast\_to\_unicast()](group__bt__cap.md#ga372e555208da722f0a89470d3b7e3e8b "Hands over the data streams in a broadcast source to a unicast group.").
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct bt\_cap\_broadcast\_source \* | [broadcast\_source](#aeb6b9c09c50b5b1f7556b1ca0f2b49c9) |
|  | The source broadcast source with the streams. |
| enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) | [type](#a7686cb6ef199865d94616b6aae670cdf) |
|  | The type of the set. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [count](#aaa5aa4c7540f75f391cf212308a7a9ce) |
|  | The number of set members in `members`. |
| union [bt\_cap\_set\_member](unionbt__cap__set__member.md) \*\* | [members](#a0914773df714195549d48d96672e63ed) |
|  | Coordinated or ad-hoc set members. |

## Detailed Description

Parameters for [bt\_cap\_initiator\_broadcast\_to\_unicast()](group__bt__cap.md#ga372e555208da722f0a89470d3b7e3e8b "Hands over the data streams in a broadcast source to a unicast group.").

## Field Documentation

## [◆ ](#aeb6b9c09c50b5b1f7556b1ca0f2b49c9)broadcast\_source

| struct bt\_cap\_broadcast\_source\* bt\_cap\_broadcast\_to\_unicast\_param::broadcast\_source |
| --- |

The source broadcast source with the streams.

The broadcast source will be stopped and deleted.

## [◆ ](#aaa5aa4c7540f75f391cf212308a7a9ce)count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_cap\_broadcast\_to\_unicast\_param::count |
| --- |

The number of set members in `members`.

This value shall match the number of streams in the `broadcast_source`.

## [◆ ](#a0914773df714195549d48d96672e63ed)members

| union [bt\_cap\_set\_member](unionbt__cap__set__member.md)\*\* bt\_cap\_broadcast\_to\_unicast\_param::members |
| --- |

Coordinated or ad-hoc set members.

## [◆ ](#a7686cb6ef199865d94616b6aae670cdf)type

| enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) bt\_cap\_broadcast\_to\_unicast\_param::type |
| --- |

The type of the set.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_broadcast\_to\_unicast\_param](structbt__cap__broadcast__to__unicast__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
