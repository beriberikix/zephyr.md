---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__bap__broadcast__source__param.html
original_path: doxygen/html/structbt__bap__broadcast__source__param.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_broadcast\_source\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md) | [Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md) » [BAP Broadcast APIs](group__bt__bap__broadcast.md) » [BAP Broadcast Source APIs](group__bt__bap__broadcast__source.md)

Broadcast Source create parameters.
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [params\_count](#a5e155c3b92b4f9de3c9e6efa377097e3) |
|  | The number of parameters in `subgroup_params`. |
| struct [bt\_bap\_broadcast\_source\_subgroup\_param](structbt__bap__broadcast__source__subgroup__param.md) \* | [params](#a6291842b49a55f6b2767dc95c9e874f3) |
|  | Array of stream parameters. |
| struct [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md) \* | [qos](#af969b5aacd4743bae608a7f54c0556e9) |
|  | Quality of Service configuration. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packing](#a493fa57a80e21a288854b2e3e1df775a) |
|  | Broadcast Source packing mode. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [encryption](#a7552bf9a4ff5441b13669effe23abb8c) |
|  | Whether or not to encrypt the streams. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [broadcast\_code](#acc096d55aaeb419a356ab5c023928df6) [16] |
|  | Broadcast code. |

## Detailed Description

Broadcast Source create parameters.

## Field Documentation

## [◆ ](#acc096d55aaeb419a356ab5c023928df6)broadcast\_code

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_broadcast\_source\_param::broadcast\_code[16] |
| --- |

Broadcast code.

If the value is a string or a the value is less than 16 octets, the remaining octets shall be 0.

Example: The string "Broadcast Code" shall be [42 72 6F 61 64 63 61 73 74 20 43 6F 64 65 00 00]

## [◆ ](#a7552bf9a4ff5441b13669effe23abb8c)encryption

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_bap\_broadcast\_source\_param::encryption |
| --- |

Whether or not to encrypt the streams.

## [◆ ](#a493fa57a80e21a288854b2e3e1df775a)packing

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_broadcast\_source\_param::packing |
| --- |

Broadcast Source packing mode.

[BT\_ISO\_PACKING\_SEQUENTIAL](group__bt__iso.md#ga6275e8d805e2366522a78f18ca47ac19 "BT_ISO_PACKING_SEQUENTIAL") or [BT\_ISO\_PACKING\_INTERLEAVED](group__bt__iso.md#ga35b037fcce858857642b4c54bae8dd79 "BT_ISO_PACKING_INTERLEAVED").

Note
:   This is a recommendation to the controller, which the controller may ignore.

## [◆ ](#a6291842b49a55f6b2767dc95c9e874f3)params

| struct [bt\_bap\_broadcast\_source\_subgroup\_param](structbt__bap__broadcast__source__subgroup__param.md)\* bt\_bap\_broadcast\_source\_param::params |
| --- |

Array of stream parameters.

## [◆ ](#a5e155c3b92b4f9de3c9e6efa377097e3)params\_count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_bap\_broadcast\_source\_param::params\_count |
| --- |

The number of parameters in `subgroup_params`.

## [◆ ](#af969b5aacd4743bae608a7f54c0556e9)qos

| struct [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md)\* bt\_bap\_broadcast\_source\_param::qos |
| --- |

Quality of Service configuration.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_broadcast\_source\_param](structbt__bap__broadcast__source__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
