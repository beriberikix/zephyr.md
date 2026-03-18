---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__cap__unicast__audio__update__stream__param.html
original_path: doxygen/html/structbt__cap__unicast__audio__update__stream__param.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_unicast\_audio\_update\_stream\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Stream specific parameters for the [bt\_cap\_initiator\_unicast\_audio\_update()](group__bt__cap.md#ga92e4e2c12720ec25c4050cde307cd639 "Update unicast audio streams.") function.
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_cap\_stream](structbt__cap__stream.md) \* | [stream](#a7a2042834b79ca37e3b3df9fc2f8a7a1) |
|  | Stream to update. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [meta\_len](#a07c1ab3158377ce51d94084ad7dc3e9c) |
|  | The length of `meta`. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [meta](#a87833f9e91b47513a27db0aa7692d8c0) |
|  | The new metadata. |

## Detailed Description

Stream specific parameters for the [bt\_cap\_initiator\_unicast\_audio\_update()](group__bt__cap.md#ga92e4e2c12720ec25c4050cde307cd639 "Update unicast audio streams.") function.

## Field Documentation

## [◆ ](#a87833f9e91b47513a27db0aa7692d8c0)meta

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_cap\_unicast\_audio\_update\_stream\_param::meta |
| --- |

The new metadata.

The metadata shall a list of CCIDs as well as a non-0 context bitfield.

## [◆ ](#a07c1ab3158377ce51d94084ad7dc3e9c)meta\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_cap\_unicast\_audio\_update\_stream\_param::meta\_len |
| --- |

The length of `meta`.

## [◆ ](#a7a2042834b79ca37e3b3df9fc2f8a7a1)stream

| struct [bt\_cap\_stream](structbt__cap__stream.md)\* bt\_cap\_unicast\_audio\_update\_stream\_param::stream |
| --- |

Stream to update.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_unicast\_audio\_update\_stream\_param](structbt__cap__unicast__audio__update__stream__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
