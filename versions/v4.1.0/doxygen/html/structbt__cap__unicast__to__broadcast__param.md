---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__cap__unicast__to__broadcast__param.html
original_path: doxygen/html/structbt__cap__unicast__to__broadcast__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_unicast\_to\_broadcast\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Parameters for [bt\_cap\_initiator\_unicast\_to\_broadcast()](group__bt__cap.md#ga6ab41d799396175c8c14e1d8222f3558 "Hands over the data streams in a unicast group to a broadcast source.").
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct bt\_bap\_unicast\_group \* | [unicast\_group](#a249a8ae6be36346c78dddb4406ed5239) |
|  | The source unicast group with the streams. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [encrypt](#ae8ebc736ab9a00ab3ed6e997e2806262) |
|  | Whether or not to encrypt the streams. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [broadcast\_code](#ad27a5f69ce697f029887e597090120a3) [[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)] |
|  | 16-octet broadcast code. |

## Detailed Description

Parameters for [bt\_cap\_initiator\_unicast\_to\_broadcast()](group__bt__cap.md#ga6ab41d799396175c8c14e1d8222f3558 "Hands over the data streams in a unicast group to a broadcast source.").

## Field Documentation

## [◆ ](#ad27a5f69ce697f029887e597090120a3)broadcast\_code

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_cap\_unicast\_to\_broadcast\_param::broadcast\_code[[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)] |
| --- |

16-octet broadcast code.

Only valid if `encrypt` is true.

If the value is a string or a the value is less than 16 octets, the remaining octets shall be 0.

Example: The string "Broadcast Code" shall be [42 72 6F 61 64 63 61 73 74 20 43 6F 64 65 00 00]

## [◆ ](#ae8ebc736ab9a00ab3ed6e997e2806262)encrypt

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_cap\_unicast\_to\_broadcast\_param::encrypt |
| --- |

Whether or not to encrypt the streams.

If set to true, then the broadcast code in `broadcast_code` will be used to encrypt the streams.

## [◆ ](#a249a8ae6be36346c78dddb4406ed5239)unicast\_group

| struct bt\_bap\_unicast\_group\* bt\_cap\_unicast\_to\_broadcast\_param::unicast\_group |
| --- |

The source unicast group with the streams.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_unicast\_to\_broadcast\_param](structbt__cap__unicast__to__broadcast__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
