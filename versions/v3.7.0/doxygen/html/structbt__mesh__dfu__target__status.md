---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__dfu__target__status.html
original_path: doxygen/html/structbt__mesh__dfu__target__status.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_dfu\_target\_status Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh Device Firmware Update](group__bt__mesh__dfu.md) » [Firmware Uppdate Client model](group__bt__mesh__dfu__cli.md)

DFU Target node status parameters.
[More...](#details)

`#include <[dfu_cli.h](dfu__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [bt\_mesh\_dfu\_status](group__bt__mesh__dfu.md#ga9e627a3c15de782faa11ef6c4ec5e05d) | [status](#a25b2198ad4970d50707ff7994c9d1415) |
|  | Status of the previous operation. |
| enum [bt\_mesh\_dfu\_phase](group__bt__mesh__dfu.md#ga99919dcee1e41bc74bd59e33bec2ded2) | [phase](#aedbbfc07a68e60236901a3c79377fe65) |
|  | Phase of the current DFU transfer. |
| enum [bt\_mesh\_dfu\_effect](group__bt__mesh__dfu.md#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8) | [effect](#aef5cbadbdd7b4b006dc304cd94c1bca4) |
|  | The effect the update will have on the Target device's state. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [blob\_id](#a2848ad866fbd437164b73a7504b75518) |
|  | BLOB ID used in the transfer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [img\_idx](#aedbd5c0a04460656d0a78eb49fd047b2) |
|  | Image index to transfer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ttl](#ab2e77b63918bb9a735a4ab20a4ca9333) |
|  | TTL used in the transfer. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [timeout\_base](#a13505201dbafeff54c0b35b445fd4f85) |
|  | Additional response time for the Target nodes, in 10-second increments. |

## Detailed Description

DFU Target node status parameters.

## Field Documentation

## [◆ ](#a2848ad866fbd437164b73a7504b75518)blob\_id

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) bt\_mesh\_dfu\_target\_status::blob\_id |
| --- |

BLOB ID used in the transfer.

## [◆ ](#aef5cbadbdd7b4b006dc304cd94c1bca4)effect

| enum [bt\_mesh\_dfu\_effect](group__bt__mesh__dfu.md#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8) bt\_mesh\_dfu\_target\_status::effect |
| --- |

The effect the update will have on the Target device's state.

## [◆ ](#aedbd5c0a04460656d0a78eb49fd047b2)img\_idx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dfu\_target\_status::img\_idx |
| --- |

Image index to transfer.

## [◆ ](#aedbbfc07a68e60236901a3c79377fe65)phase

| enum [bt\_mesh\_dfu\_phase](group__bt__mesh__dfu.md#ga99919dcee1e41bc74bd59e33bec2ded2) bt\_mesh\_dfu\_target\_status::phase |
| --- |

Phase of the current DFU transfer.

## [◆ ](#a25b2198ad4970d50707ff7994c9d1415)status

| enum [bt\_mesh\_dfu\_status](group__bt__mesh__dfu.md#ga9e627a3c15de782faa11ef6c4ec5e05d) bt\_mesh\_dfu\_target\_status::status |
| --- |

Status of the previous operation.

## [◆ ](#a13505201dbafeff54c0b35b445fd4f85)timeout\_base

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_dfu\_target\_status::timeout\_base |
| --- |

Additional response time for the Target nodes, in 10-second increments.

The extra time can be used to give the Target nodes more time to respond to messages from the Client. The actual timeout will be calculated according to the following formula:

```
*  timeout = 20 seconds + (10 seconds * timeout_base) + (100 ms * TTL)
*
```

If a Target node fails to respond to a message from the Client within the configured transfer timeout, the Target node is dropped.

## [◆ ](#ab2e77b63918bb9a735a4ab20a4ca9333)ttl

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dfu\_target\_status::ttl |
| --- |

TTL used in the transfer.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[dfu\_cli.h](dfu__cli_8h_source.md)

- [bt\_mesh\_dfu\_target\_status](structbt__mesh__dfu__target__status.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
