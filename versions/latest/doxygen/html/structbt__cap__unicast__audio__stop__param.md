---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__cap__unicast__audio__stop__param.html
original_path: doxygen/html/structbt__cap__unicast__audio__stop__param.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_unicast\_audio\_stop\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Parameters for the [bt\_cap\_initiator\_unicast\_audio\_stop()](group__bt__cap.md#gafdf6f1656249ab3ae6296272dc36b66f "Stop unicast audio streams.") function.
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) | [type](#a773eedda9ae8969e8749d56ffa3d1afa) |
|  | The type of the set. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [count](#a11b5ac19301ce8ebd2c35df45c60bfe2) |
|  | The number of streams in `streams`. |
| struct [bt\_cap\_stream](structbt__cap__stream.md) \*\* | [streams](#a94707060a6ef15dd8d3e48eae526aa82) |
|  | Array of streams to stop. |

## Detailed Description

Parameters for the [bt\_cap\_initiator\_unicast\_audio\_stop()](group__bt__cap.md#gafdf6f1656249ab3ae6296272dc36b66f "Stop unicast audio streams.") function.

## Field Documentation

## [◆ ](#a11b5ac19301ce8ebd2c35df45c60bfe2)count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_cap\_unicast\_audio\_stop\_param::count |
| --- |

The number of streams in `streams`.

## [◆ ](#a94707060a6ef15dd8d3e48eae526aa82)streams

| struct [bt\_cap\_stream](structbt__cap__stream.md)\*\* bt\_cap\_unicast\_audio\_stop\_param::streams |
| --- |

Array of streams to stop.

## [◆ ](#a773eedda9ae8969e8749d56ffa3d1afa)type

| enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) bt\_cap\_unicast\_audio\_stop\_param::type |
| --- |

The type of the set.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_unicast\_audio\_stop\_param](structbt__cap__unicast__audio__stop__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
