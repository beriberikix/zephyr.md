---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__bap__broadcast__source__param.html
original_path: doxygen/html/structbt__bap__broadcast__source__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| struct [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md) \* | [qos](#ad62b77786a6996990d03d313331f2eb5) |
|  | Quality of Service configuration. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packing](#a493fa57a80e21a288854b2e3e1df775a) |
|  | Broadcast Source packing mode. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [encryption](#a7552bf9a4ff5441b13669effe23abb8c) |
|  | Whether or not to encrypt the streams. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [broadcast\_code](#a6a05b6448f55cf5f52f90e44d83146dc) [[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)] |
|  | Broadcast code. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [irc](#aab1799ab671500b02c1ab0e023ac43f7) |
|  | Immediate Repetition Count. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pto](#a50c29b5a2bcae162c0bbda32102a30cc) |
|  | Pre-transmission offset. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [iso\_interval](#a11b03e3d63ca2e116e743d9efde920be) |
|  | ISO interval. |

## Detailed Description

Broadcast Source create parameters.

## Field Documentation

## [◆ ](#a6a05b6448f55cf5f52f90e44d83146dc)broadcast\_code

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_broadcast\_source\_param::broadcast\_code[[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)] |
| --- |

Broadcast code.

If the value is a string or a the value is less than 16 octets, the remaining octets shall be 0.

Example: The string "Broadcast Code" shall be [42 72 6F 61 64 63 61 73 74 20 43 6F 64 65 00 00]

## [◆ ](#a7552bf9a4ff5441b13669effe23abb8c)encryption

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_bap\_broadcast\_source\_param::encryption |
| --- |

Whether or not to encrypt the streams.

## [◆ ](#aab1799ab671500b02c1ab0e023ac43f7)irc

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_broadcast\_source\_param::irc |
| --- |

Immediate Repetition Count.

The number of times the scheduled payloads are transmitted in a given event.

Value range from [BT\_ISO\_IRC\_MIN](group__bt__iso.md#ga52df7bd114b77872c084e28ca86e0b2e "BT_ISO_IRC_MIN") to [BT\_ISO\_IRC\_MAX](group__bt__iso.md#ga0f412f1593bcdcfa2b323b285bd508a4 "BT_ISO_IRC_MAX").

## [◆ ](#a11b03e3d63ca2e116e743d9efde920be)iso\_interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_bap\_broadcast\_source\_param::iso\_interval |
| --- |

ISO interval.

Time between consecutive BIS anchor points.

Value range from [BT\_ISO\_ISO\_INTERVAL\_MIN](group__bt__iso.md#ga5cc5e9fd5e7af83eeaab8fe2fd16b9de "BT_ISO_ISO_INTERVAL_MIN") to [BT\_ISO\_ISO\_INTERVAL\_MAX](group__bt__iso.md#gabc381a7f565061ec91d23b7783521da3 "BT_ISO_ISO_INTERVAL_MAX").

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

## [◆ ](#a50c29b5a2bcae162c0bbda32102a30cc)pto

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_broadcast\_source\_param::pto |
| --- |

Pre-transmission offset.

Offset used for pre-transmissions.

Value range from [BT\_ISO\_PTO\_MIN](group__bt__iso.md#ga3f19aaa432290d67fdf4911d1d044dd8 "BT_ISO_PTO_MIN") to [BT\_ISO\_PTO\_MAX](group__bt__iso.md#ga27e812e35a1f12329310851eb9c056f2 "BT_ISO_PTO_MAX").

## [◆ ](#ad62b77786a6996990d03d313331f2eb5)qos

| struct [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md)\* bt\_bap\_broadcast\_source\_param::qos |
| --- |

Quality of Service configuration.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_broadcast\_source\_param](structbt__bap__broadcast__source__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
