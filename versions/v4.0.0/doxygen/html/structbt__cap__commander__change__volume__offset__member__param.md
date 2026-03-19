---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__cap__commander__change__volume__offset__member__param.html
original_path: doxygen/html/structbt__cap__commander__change__volume__offset__member__param.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_commander\_change\_volume\_offset\_member\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Parameters part of [bt\_cap\_commander\_change\_volume\_offset\_param](structbt__cap__commander__change__volume__offset__param.md "bt_cap_commander_change_volume_offset_param") for [bt\_cap\_commander\_change\_volume\_offset()](group__bt__cap.md#gae2cd451b387659b0a2021a9023d74dfa "Change the volume offset on one or more Common Audio Profile Acceptors.").
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union [bt\_cap\_set\_member](unionbt__cap__set__member.md) | [member](#a8e2e4f07be565ef1067d4955ebef50d4) |
|  | Coordinated or ad-hoc set member. |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [offset](#a7d9e94cd9eb79f1f7a14c8b9bb84e5a8) |
|  | The offset to set. |

## Detailed Description

Parameters part of [bt\_cap\_commander\_change\_volume\_offset\_param](structbt__cap__commander__change__volume__offset__param.md "bt_cap_commander_change_volume_offset_param") for [bt\_cap\_commander\_change\_volume\_offset()](group__bt__cap.md#gae2cd451b387659b0a2021a9023d74dfa "Change the volume offset on one or more Common Audio Profile Acceptors.").

## Field Documentation

## [◆ ](#a8e2e4f07be565ef1067d4955ebef50d4)member

| union [bt\_cap\_set\_member](unionbt__cap__set__member.md) bt\_cap\_commander\_change\_volume\_offset\_member\_param::member |
| --- |

Coordinated or ad-hoc set member.

## [◆ ](#a7d9e94cd9eb79f1f7a14c8b9bb84e5a8)offset

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) bt\_cap\_commander\_change\_volume\_offset\_member\_param::offset |
| --- |

The offset to set.

Value shall be between [BT\_VOCS\_MIN\_OFFSET](group__bt__vocs.md#ga64d4e32f9d92a58b3229b3aa2e8fcc4d "BT_VOCS_MIN_OFFSET") and [BT\_VOCS\_MAX\_OFFSET](group__bt__vocs.md#ga800092562173fd37826b5537feaac3ae "BT_VOCS_MAX_OFFSET")

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_commander\_change\_volume\_offset\_member\_param](structbt__cap__commander__change__volume__offset__member__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
