---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__bap__unicast__group__stream__pair__param.html
original_path: doxygen/html/structbt__bap__unicast__group__stream__pair__param.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_unicast\_group\_stream\_pair\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md) » [BAP Unicast Client APIs](group__bt__bap__unicast__client.md)

Parameter struct for the unicast group functions.
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_bap\_unicast\_group\_stream\_param](structbt__bap__unicast__group__stream__param.md) \* | [rx\_param](#ad2f1f8fb4ab3fd2cb4dca8ed08de5b8d) |
|  | Pointer to a receiving stream parameters. |
| struct [bt\_bap\_unicast\_group\_stream\_param](structbt__bap__unicast__group__stream__param.md) \* | [tx\_param](#ae73a11aab16a60806d1a941306c1822a) |
|  | Pointer to a transmitting stream parameters. |

## Detailed Description

Parameter struct for the unicast group functions.

Parameter struct for the [bt\_bap\_unicast\_group\_create()](group__bt__bap__unicast__client.md#gaafd53b5f45d998b44e94a1b58e93ba21 "Create unicast group.") and [bt\_bap\_unicast\_group\_add\_streams()](group__bt__bap__unicast__client.md#ga9cc792cd1eaaa79d56f3df0e2341cbf6 "Add streams to a unicast group as a unicast client.") functions.

## Field Documentation

## [◆ ](#ad2f1f8fb4ab3fd2cb4dca8ed08de5b8d)rx\_param

| struct [bt\_bap\_unicast\_group\_stream\_param](structbt__bap__unicast__group__stream__param.md)\* bt\_bap\_unicast\_group\_stream\_pair\_param::rx\_param |
| --- |

Pointer to a receiving stream parameters.

## [◆ ](#ae73a11aab16a60806d1a941306c1822a)tx\_param

| struct [bt\_bap\_unicast\_group\_stream\_param](structbt__bap__unicast__group__stream__param.md)\* bt\_bap\_unicast\_group\_stream\_pair\_param::tx\_param |
| --- |

Pointer to a transmitting stream parameters.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_unicast\_group\_stream\_pair\_param](structbt__bap__unicast__group__stream__pair__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
