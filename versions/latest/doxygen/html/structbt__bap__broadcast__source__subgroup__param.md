---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__bap__broadcast__source__subgroup__param.html
original_path: doxygen/html/structbt__bap__broadcast__source__subgroup__param.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_broadcast\_source\_subgroup\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md) | [Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md) » [BAP Broadcast APIs](group__bt__bap__broadcast.md) » [BAP Broadcast Source APIs](group__bt__bap__broadcast__source.md)

Broadcast Source subgroup parameters.
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [params\_count](#a701d9480ffae2351149de6b962095d32) |
|  | The number of parameters in `stream_params`. |
| struct [bt\_bap\_broadcast\_source\_stream\_param](structbt__bap__broadcast__source__stream__param.md) \* | [params](#a9719e89d8979f9502023e0032814c477) |
|  | Array of stream parameters. |
| struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | [codec\_cfg](#a1986239ea2ed5204d8f46a6500d5900d) |
|  | Subgroup Codec configuration. |

## Detailed Description

Broadcast Source subgroup parameters.

## Field Documentation

## [◆ ](#a1986239ea2ed5204d8f46a6500d5900d)codec\_cfg

| struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md)\* bt\_bap\_broadcast\_source\_subgroup\_param::codec\_cfg |
| --- |

Subgroup Codec configuration.

## [◆ ](#a9719e89d8979f9502023e0032814c477)params

| struct [bt\_bap\_broadcast\_source\_stream\_param](structbt__bap__broadcast__source__stream__param.md)\* bt\_bap\_broadcast\_source\_subgroup\_param::params |
| --- |

Array of stream parameters.

## [◆ ](#a701d9480ffae2351149de6b962095d32)params\_count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_bap\_broadcast\_source\_subgroup\_param::params\_count |
| --- |

The number of parameters in `stream_params`.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_broadcast\_source\_subgroup\_param](structbt__bap__broadcast__source__subgroup__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
