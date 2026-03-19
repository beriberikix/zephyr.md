---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__cap__initiator__broadcast__subgroup__param.html
original_path: doxygen/html/structbt__cap__initiator__broadcast__subgroup__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_initiator\_broadcast\_subgroup\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Parameters part of `[bt_cap_initiator_broadcast_create_param](structbt__cap__initiator__broadcast__create__param.md "Parameters for * bt_cap_initiator_broadcast_audio_create().")` for [bt\_cap\_initiator\_broadcast\_audio\_create()](group__bt__cap.md#ga78697225c6b1291dfc016e20fd605fc4 "Create a Common Audio Profile broadcast source.").
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [stream\_count](#a577a27836a02c7a6219182f1cb0bd769) |
|  | The number of parameters in `stream_params`. |
| struct [bt\_cap\_initiator\_broadcast\_stream\_param](structbt__cap__initiator__broadcast__stream__param.md) \* | [stream\_params](#a32e99898ee97a56105497c3ae480692a) |
|  | Array of stream parameters. |
| struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | [codec\_cfg](#a62d3a6a13a10f3bd594f064e761dba47) |
|  | Subgroup Codec configuration. |

## Detailed Description

Parameters part of `[bt_cap_initiator_broadcast_create_param](structbt__cap__initiator__broadcast__create__param.md "Parameters for * bt_cap_initiator_broadcast_audio_create().")` for [bt\_cap\_initiator\_broadcast\_audio\_create()](group__bt__cap.md#ga78697225c6b1291dfc016e20fd605fc4 "Create a Common Audio Profile broadcast source.").

## Field Documentation

## [◆ ](#a62d3a6a13a10f3bd594f064e761dba47)codec\_cfg

| struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md)\* bt\_cap\_initiator\_broadcast\_subgroup\_param::codec\_cfg |
| --- |

Subgroup Codec configuration.

## [◆ ](#a577a27836a02c7a6219182f1cb0bd769)stream\_count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_cap\_initiator\_broadcast\_subgroup\_param::stream\_count |
| --- |

The number of parameters in `stream_params`.

## [◆ ](#a32e99898ee97a56105497c3ae480692a)stream\_params

| struct [bt\_cap\_initiator\_broadcast\_stream\_param](structbt__cap__initiator__broadcast__stream__param.md)\* bt\_cap\_initiator\_broadcast\_subgroup\_param::stream\_params |
| --- |

Array of stream parameters.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_initiator\_broadcast\_subgroup\_param](structbt__cap__initiator__broadcast__subgroup__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
