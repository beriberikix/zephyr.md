---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__bap__broadcast__source__stream__param.html
original_path: doxygen/html/structbt__bap__broadcast__source__stream__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_broadcast\_source\_stream\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md) | [Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md) » [BAP Broadcast APIs](group__bt__bap__broadcast.md) » [BAP Broadcast Source APIs](group__bt__bap__broadcast__source.md)

Broadcast Source stream parameters.
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_bap\_stream](structbt__bap__stream.md) \* | [stream](#a9c92fb50b62d963e01b1506b790fb5e1) |
|  | Audio stream. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [data\_len](#ac79a76ad748673ca4bd52c597cd073df) |
|  | The number of elements in the `data` array. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [data](#a5604297eafad95ae4e6a6c33a91b7e33) |
|  | BIS Codec Specific Configuration. |

## Detailed Description

Broadcast Source stream parameters.

## Field Documentation

## [◆ ](#a5604297eafad95ae4e6a6c33a91b7e33)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_bap\_broadcast\_source\_stream\_param::data |
| --- |

BIS Codec Specific Configuration.

## [◆ ](#ac79a76ad748673ca4bd52c597cd073df)data\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_bap\_broadcast\_source\_stream\_param::data\_len |
| --- |

The number of elements in the `data` array.

The BIS specific data may be omitted and this set to 0.

## [◆ ](#a9c92fb50b62d963e01b1506b790fb5e1)stream

| struct [bt\_bap\_stream](structbt__bap__stream.md)\* bt\_bap\_broadcast\_source\_stream\_param::stream |
| --- |

Audio stream.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_broadcast\_source\_stream\_param](structbt__bap__broadcast__source__stream__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
