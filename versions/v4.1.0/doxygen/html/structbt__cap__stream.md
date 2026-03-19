---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__cap__stream.html
original_path: doxygen/html/structbt__cap__stream.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_stream Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Common Audio Profile stream structure.
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_bap\_stream](structbt__bap__stream.md) | [bap\_stream](#ad9d974d18ec42079b81107485b43bc18) |
|  | The underlying BAP audio stream. |
| struct [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md) \* | [ops](#aa58c47ace3f844533ab545906ede52ba) |
|  | Audio stream operations. |

## Detailed Description

Common Audio Profile stream structure.

Streams represents a Basic Audio Profile (BAP) stream and operation callbacks. See [bt\_bap\_stream](structbt__bap__stream.md "bt_bap_stream") for additional information.

## Field Documentation

## [◆ ](#ad9d974d18ec42079b81107485b43bc18)bap\_stream

| struct [bt\_bap\_stream](structbt__bap__stream.md) bt\_cap\_stream::bap\_stream |
| --- |

The underlying BAP audio stream.

## [◆ ](#aa58c47ace3f844533ab545906ede52ba)ops

| struct [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md)\* bt\_cap\_stream::ops |
| --- |

Audio stream operations.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_stream](structbt__cap__stream.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
