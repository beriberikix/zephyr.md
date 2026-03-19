---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__cap__initiator__broadcast__stream__param.html
original_path: doxygen/html/structbt__cap__initiator__broadcast__stream__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_initiator\_broadcast\_stream\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Parameters part of `[bt_cap_initiator_broadcast_subgroup_param](structbt__cap__initiator__broadcast__subgroup__param.md "Parameters part of bt_cap_initiator_broadcast_create_param for bt_cap_initiator_broadcast_audio_creat...")` for [bt\_cap\_initiator\_broadcast\_audio\_create()](group__bt__cap.md#ga78697225c6b1291dfc016e20fd605fc4 "Create a Common Audio Profile broadcast source.").
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_cap\_stream](structbt__cap__stream.md) \* | [stream](#a7e5ddb85024b58d6ecbb6d7f70ef5c6a) |
|  | Audio stream. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [data\_len](#aa4677e278d6d4823551ccfd9c27c68a4) |
|  | The length of the p data array. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [data](#a72720e8423dbeb0341041cc24a9e0869) |
|  | BIS Codec Specific Configuration. |

## Detailed Description

Parameters part of `[bt_cap_initiator_broadcast_subgroup_param](structbt__cap__initiator__broadcast__subgroup__param.md "Parameters part of bt_cap_initiator_broadcast_create_param for bt_cap_initiator_broadcast_audio_creat...")` for [bt\_cap\_initiator\_broadcast\_audio\_create()](group__bt__cap.md#ga78697225c6b1291dfc016e20fd605fc4 "Create a Common Audio Profile broadcast source.").

## Field Documentation

## [◆ ](#a72720e8423dbeb0341041cc24a9e0869)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_cap\_initiator\_broadcast\_stream\_param::data |
| --- |

BIS Codec Specific Configuration.

## [◆ ](#aa4677e278d6d4823551ccfd9c27c68a4)data\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_cap\_initiator\_broadcast\_stream\_param::data\_len |
| --- |

The length of the p data array.

The BIS specific data may be omitted and this set to 0.

## [◆ ](#a7e5ddb85024b58d6ecbb6d7f70ef5c6a)stream

| struct [bt\_cap\_stream](structbt__cap__stream.md)\* bt\_cap\_initiator\_broadcast\_stream\_param::stream |
| --- |

Audio stream.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_initiator\_broadcast\_stream\_param](structbt__cap__initiator__broadcast__stream__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
