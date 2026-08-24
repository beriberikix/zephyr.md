---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__cap__unicast__group__stream__param.html
original_path: doxygen/html/structbt__cap__unicast__group__stream__param.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_unicast\_group\_stream\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Parameter struct for each stream in the unicast group.
[More...](#details)

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_cap\_stream](structbt__cap__stream.md) \* | [stream](#a16aacd43bb7b449648ab6a5a89999fba) |
|  | Pointer to a stream object. |
| struct [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md) \* | [qos\_cfg](#af55f6b576509853d39b1fe68bcec348a) |
|  | The QoS settings for the stream object. |

## Detailed Description

Parameter struct for each stream in the unicast group.

## Field Documentation

## [◆ ](#af55f6b576509853d39b1fe68bcec348a)qos\_cfg

| struct [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md)\* bt\_cap\_unicast\_group\_stream\_param::qos\_cfg |
| --- |

The QoS settings for the stream object.

## [◆ ](#a16aacd43bb7b449648ab6a5a89999fba)stream

| struct [bt\_cap\_stream](structbt__cap__stream.md)\* bt\_cap\_unicast\_group\_stream\_param::stream |
| --- |

Pointer to a stream object.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_unicast\_group\_stream\_param](structbt__cap__unicast__group__stream__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
