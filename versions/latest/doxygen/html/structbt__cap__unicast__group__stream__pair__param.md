---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__cap__unicast__group__stream__pair__param.html
original_path: doxygen/html/structbt__cap__unicast__group__stream__pair__param.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_unicast\_group\_stream\_pair\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Parameter struct for the unicast group functions.
[More...](#details)

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_cap\_unicast\_group\_stream\_param](structbt__cap__unicast__group__stream__param.md) \* | [rx\_param](#a19d49ab8c0daa7e6a4c73563952ae461) |
|  | Pointer to a receiving stream parameters. |
| struct [bt\_cap\_unicast\_group\_stream\_param](structbt__cap__unicast__group__stream__param.md) \* | [tx\_param](#a6edeca159371f3a70cc5a1f662a0e45c) |
|  | Pointer to a transmitting stream parameters. |

## Detailed Description

Parameter struct for the unicast group functions.

Parameter struct for the [bt\_cap\_unicast\_group\_create()](group__bt__cap.md#ga299ee8321aa5059e48244e1ae8080637 "Create unicast group.") and [bt\_cap\_unicast\_group\_add\_streams()](group__bt__cap.md#ga7b5d30c07e57f4db23f72836a3b12b2b "Add streams to a unicast group as a unicast client.") functions.

## Field Documentation

## [◆ ](#a19d49ab8c0daa7e6a4c73563952ae461)rx\_param

| struct [bt\_cap\_unicast\_group\_stream\_param](structbt__cap__unicast__group__stream__param.md)\* bt\_cap\_unicast\_group\_stream\_pair\_param::rx\_param |
| --- |

Pointer to a receiving stream parameters.

## [◆ ](#a6edeca159371f3a70cc5a1f662a0e45c)tx\_param

| struct [bt\_cap\_unicast\_group\_stream\_param](structbt__cap__unicast__group__stream__param.md)\* bt\_cap\_unicast\_group\_stream\_pair\_param::tx\_param |
| --- |

Pointer to a transmitting stream parameters.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_unicast\_group\_stream\_pair\_param](structbt__cap__unicast__group__stream__pair__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
