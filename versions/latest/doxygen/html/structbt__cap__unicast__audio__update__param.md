---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__cap__unicast__audio__update__param.html
original_path: doxygen/html/structbt__cap__unicast__audio__update__param.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_unicast\_audio\_update\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Parameters for the [bt\_cap\_initiator\_unicast\_audio\_update()](group__bt__cap.md#ga92e4e2c12720ec25c4050cde307cd639 "Update unicast audio streams.") function.
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) | [type](#a768029ce89b74e0bcc06bb50f1fd8dcd) |
|  | The type of the set. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [count](#ac8982f313161380af536d41ec48dcba1) |
|  | The number of parameters in `stream_params`. |
| struct [bt\_cap\_unicast\_audio\_update\_stream\_param](structbt__cap__unicast__audio__update__stream__param.md) \* | [stream\_params](#a3d8f940d8401b8524764e7ecab3cfacb) |
|  | Array of stream parameters. |

## Detailed Description

Parameters for the [bt\_cap\_initiator\_unicast\_audio\_update()](group__bt__cap.md#ga92e4e2c12720ec25c4050cde307cd639 "Update unicast audio streams.") function.

## Field Documentation

## [◆ ](#ac8982f313161380af536d41ec48dcba1)count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_cap\_unicast\_audio\_update\_param::count |
| --- |

The number of parameters in `stream_params`.

## [◆ ](#a3d8f940d8401b8524764e7ecab3cfacb)stream\_params

| struct [bt\_cap\_unicast\_audio\_update\_stream\_param](structbt__cap__unicast__audio__update__stream__param.md)\* bt\_cap\_unicast\_audio\_update\_param::stream\_params |
| --- |

Array of stream parameters.

## [◆ ](#a768029ce89b74e0bcc06bb50f1fd8dcd)type

| enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) bt\_cap\_unicast\_audio\_update\_param::type |
| --- |

The type of the set.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_unicast\_audio\_update\_param](structbt__cap__unicast__audio__update__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
