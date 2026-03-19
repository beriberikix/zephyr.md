---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__cap__commander__change__volume__mute__state__param.html
original_path: doxygen/html/structbt__cap__commander__change__volume__mute__state__param.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_commander\_change\_volume\_mute\_state\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Parameters for changing volume mute state.
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) | [type](#ae4b664c4b8da062a83dfcc32ebd28775) |
|  | The type of the set. |
| union [bt\_cap\_set\_member](unionbt__cap__set__member.md) \* | [members](#af54b6898bfcd42188cf45d65c72217d1) |
|  | Coordinated or ad-hoc set member. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [count](#a784542a30164a62d44fcd3f801bc29f8) |
|  | The number of members in `members`. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [mute](#ad4cc775dc74540a2b40126dba96776cd) |
|  | The volume mute state to set. |

## Detailed Description

Parameters for changing volume mute state.

## Field Documentation

## [◆ ](#a784542a30164a62d44fcd3f801bc29f8)count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_cap\_commander\_change\_volume\_mute\_state\_param::count |
| --- |

The number of members in `members`.

## [◆ ](#af54b6898bfcd42188cf45d65c72217d1)members

| union [bt\_cap\_set\_member](unionbt__cap__set__member.md)\* bt\_cap\_commander\_change\_volume\_mute\_state\_param::members |
| --- |

Coordinated or ad-hoc set member.

## [◆ ](#ad4cc775dc74540a2b40126dba96776cd)mute

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_cap\_commander\_change\_volume\_mute\_state\_param::mute |
| --- |

The volume mute state to set.

true to mute, and false to unmute

## [◆ ](#ae4b664c4b8da062a83dfcc32ebd28775)type

| enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) bt\_cap\_commander\_change\_volume\_mute\_state\_param::type |
| --- |

The type of the set.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_commander\_change\_volume\_mute\_state\_param](structbt__cap__commander__change__volume__mute__state__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
