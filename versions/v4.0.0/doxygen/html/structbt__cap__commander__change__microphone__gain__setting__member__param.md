---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__cap__commander__change__microphone__gain__setting__member__param.html
original_path: doxygen/html/structbt__cap__commander__change__microphone__gain__setting__member__param.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Parameters part of [bt\_cap\_commander\_change\_microphone\_gain\_setting\_param](structbt__cap__commander__change__microphone__gain__setting__param.md "bt_cap_commander_change_microphone_gain_setting_param") for [bt\_cap\_commander\_change\_microphone\_gain\_setting()](group__bt__cap.md#ga958cd5925699624d23479ad2ace6b55b "Change the microphone gain setting on one or more Common Audio Profile Acceptors.").
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union [bt\_cap\_set\_member](unionbt__cap__set__member.md) | [member](#a5cc34236153e6a737f71cbc77f5f840e) |
|  | Coordinated or ad-hoc set member. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [gain](#a8fdcc5ec143b5a73c369d6e15d276196) |
|  | The microphone gain setting to set. |

## Detailed Description

Parameters part of [bt\_cap\_commander\_change\_microphone\_gain\_setting\_param](structbt__cap__commander__change__microphone__gain__setting__param.md "bt_cap_commander_change_microphone_gain_setting_param") for [bt\_cap\_commander\_change\_microphone\_gain\_setting()](group__bt__cap.md#ga958cd5925699624d23479ad2ace6b55b "Change the microphone gain setting on one or more Common Audio Profile Acceptors.").

## Field Documentation

## [◆ ](#a8fdcc5ec143b5a73c369d6e15d276196)gain

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param::gain |
| --- |

The microphone gain setting to set.

## [◆ ](#a5cc34236153e6a737f71cbc77f5f840e)member

| union [bt\_cap\_set\_member](unionbt__cap__set__member.md) bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param::member |
| --- |

Coordinated or ad-hoc set member.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param](structbt__cap__commander__change__microphone__gain__setting__member__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
