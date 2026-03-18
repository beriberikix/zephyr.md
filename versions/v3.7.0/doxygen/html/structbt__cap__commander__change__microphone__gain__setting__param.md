---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__cap__commander__change__microphone__gain__setting__param.html
original_path: doxygen/html/structbt__cap__commander__change__microphone__gain__setting__param.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_commander\_change\_microphone\_gain\_setting\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Parameters for changing microphone mute state.
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) | [type](#abac0f4da7b8b05067636539b2e9f9673) |
|  | The type of the set. |
| struct [bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param](structbt__cap__commander__change__microphone__gain__setting__member__param.md) \* | [param](#ade5a93aee8bcff628228664c4a8428a8) |
|  | The set of devices for this procedure. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [count](#ae78e5d4761df00c8c8e2cfcb3e727349) |
|  | The number of parameters in `param`. |

## Detailed Description

Parameters for changing microphone mute state.

## Field Documentation

## [◆ ](#ae78e5d4761df00c8c8e2cfcb3e727349)count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_cap\_commander\_change\_microphone\_gain\_setting\_param::count |
| --- |

The number of parameters in `param`.

## [◆ ](#ade5a93aee8bcff628228664c4a8428a8)param

| struct [bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param](structbt__cap__commander__change__microphone__gain__setting__member__param.md)\* bt\_cap\_commander\_change\_microphone\_gain\_setting\_param::param |
| --- |

The set of devices for this procedure.

## [◆ ](#abac0f4da7b8b05067636539b2e9f9673)type

| enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) bt\_cap\_commander\_change\_microphone\_gain\_setting\_param::type |
| --- |

The type of the set.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_commander\_change\_microphone\_gain\_setting\_param](structbt__cap__commander__change__microphone__gain__setting__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
