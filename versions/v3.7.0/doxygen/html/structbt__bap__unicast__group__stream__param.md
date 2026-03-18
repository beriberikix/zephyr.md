---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__bap__unicast__group__stream__param.html
original_path: doxygen/html/structbt__bap__unicast__group__stream__param.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_unicast\_group\_stream\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md) » [BAP Unicast Client APIs](group__bt__bap__unicast__client.md)

Parameter struct for each stream in the unicast group.
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_bap\_stream](structbt__bap__stream.md) \* | [stream](#acfa192fed73b27fb194881f0021fcb35) |
|  | Pointer to a stream object. |
| struct [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md) \* | [qos](#a570776d2b689a76884331a0bc00e50ec) |
|  | The QoS settings for the stream object. |

## Detailed Description

Parameter struct for each stream in the unicast group.

## Field Documentation

## [◆ ](#a570776d2b689a76884331a0bc00e50ec)qos

| struct [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md)\* bt\_bap\_unicast\_group\_stream\_param::qos |
| --- |

The QoS settings for the stream object.

## [◆ ](#acfa192fed73b27fb194881f0021fcb35)stream

| struct [bt\_bap\_stream](structbt__bap__stream.md)\* bt\_bap\_unicast\_group\_stream\_param::stream |
| --- |

Pointer to a stream object.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_unicast\_group\_stream\_param](structbt__bap__unicast__group__stream__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
