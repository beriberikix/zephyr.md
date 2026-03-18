---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__cap__commander__change__microphone__mute__state__param.html
original_path: doxygen/html/structbt__cap__commander__change__microphone__mute__state__param.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_commander\_change\_microphone\_mute\_state\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Parameters for changing microphone mute state.
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) | [type](#a9cdb1eda2108fc341a6d7268fac689b0) |
|  | The type of the set. |
| union [bt\_cap\_set\_member](unionbt__cap__set__member.md) \* | [members](#a9c989fe2446ee2e055778c063a6b6de1) |
|  | Coordinated or ad-hoc set member. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [count](#a96007101444d3cd61dda067fa072580e) |
|  | The number of members in `members`. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [mute](#a1b6e22c9c41eb24b3961927b45c98af8) |
|  | The microphone mute state to set. |

## Detailed Description

Parameters for changing microphone mute state.

## Field Documentation

## [◆ ](#a96007101444d3cd61dda067fa072580e)count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_cap\_commander\_change\_microphone\_mute\_state\_param::count |
| --- |

The number of members in `members`.

## [◆ ](#a9c989fe2446ee2e055778c063a6b6de1)members

| union [bt\_cap\_set\_member](unionbt__cap__set__member.md)\* bt\_cap\_commander\_change\_microphone\_mute\_state\_param::members |
| --- |

Coordinated or ad-hoc set member.

## [◆ ](#a1b6e22c9c41eb24b3961927b45c98af8)mute

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_cap\_commander\_change\_microphone\_mute\_state\_param::mute |
| --- |

The microphone mute state to set.

true to mute, and false to unmute

## [◆ ](#a9cdb1eda2108fc341a6d7268fac689b0)type

| enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) bt\_cap\_commander\_change\_microphone\_mute\_state\_param::type |
| --- |

The type of the set.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_commander\_change\_microphone\_mute\_state\_param](structbt__cap__commander__change__microphone__mute__state__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
