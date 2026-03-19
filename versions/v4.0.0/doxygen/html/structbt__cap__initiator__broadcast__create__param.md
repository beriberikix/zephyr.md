---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__cap__initiator__broadcast__create__param.html
original_path: doxygen/html/structbt__cap__initiator__broadcast__create__param.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_initiator\_broadcast\_create\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Parameters for \* [bt\_cap\_initiator\_broadcast\_audio\_create()](group__bt__cap.md#ga78697225c6b1291dfc016e20fd605fc4 "Create a Common Audio Profile broadcast source.").
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [subgroup\_count](#aee3e0244b59503311bc445f36977a85b) |
|  | The number of parameters in `subgroup_params`. |
| struct [bt\_cap\_initiator\_broadcast\_subgroup\_param](structbt__cap__initiator__broadcast__subgroup__param.md) \* | [subgroup\_params](#a2eafc157450237cf311d6144e7431839) |
|  | Array of stream parameters. |
| struct [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md) \* | [qos](#a142125e620776aed464d90f280ef1a4c) |
|  | Quality of Service configuration. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packing](#ae81ee3dada58a3354c70401380916cbc) |
|  | Broadcast Source packing mode. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [encryption](#a4432bee0e365c189996b9f70c7226542) |
|  | Whether or not to encrypt the streams. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [broadcast\_code](#aa4d6fbd5bd13963004e381b987bbeb4d) [[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)] |
|  | 16-octet broadcast code. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [irc](#a6f562b7a696472b7784ca2e1ced4997a) |
|  | Immediate Repetition Count. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pto](#a01d6ffb369caaf808d4b55b3b1748890) |
|  | Pre-transmission offset. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [iso\_interval](#a8eedd8f9a896931f75642576ca37c7d5) |
|  | ISO interval. |

## Detailed Description

Parameters for \* [bt\_cap\_initiator\_broadcast\_audio\_create()](group__bt__cap.md#ga78697225c6b1291dfc016e20fd605fc4 "Create a Common Audio Profile broadcast source.").

## Field Documentation

## [◆ ](#aa4d6fbd5bd13963004e381b987bbeb4d)broadcast\_code

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_cap\_initiator\_broadcast\_create\_param::broadcast\_code[[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)] |
| --- |

16-octet broadcast code.

Only valid if `encrypt` is true.

If the value is a string or a the value is less than 16 octets, the remaining octets shall be 0.

Example: The string "Broadcast Code" shall be [42 72 6F 61 64 63 61 73 74 20 43 6F 64 65 00 00]

## [◆ ](#a4432bee0e365c189996b9f70c7226542)encryption

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_cap\_initiator\_broadcast\_create\_param::encryption |
| --- |

Whether or not to encrypt the streams.

## [◆ ](#a6f562b7a696472b7784ca2e1ced4997a)irc

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_cap\_initiator\_broadcast\_create\_param::irc |
| --- |

Immediate Repetition Count.

The number of times the scheduled payloads are transmitted in a given event.

Value range from [BT\_ISO\_IRC\_MIN](group__bt__iso.md#ga52df7bd114b77872c084e28ca86e0b2e "BT_ISO_IRC_MIN") to [BT\_ISO\_IRC\_MAX](group__bt__iso.md#ga0f412f1593bcdcfa2b323b285bd508a4 "BT_ISO_IRC_MAX").

## [◆ ](#a8eedd8f9a896931f75642576ca37c7d5)iso\_interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_cap\_initiator\_broadcast\_create\_param::iso\_interval |
| --- |

ISO interval.

Time between consecutive BIS anchor points.

Value range from [BT\_ISO\_ISO\_INTERVAL\_MIN](group__bt__iso.md#ga5cc5e9fd5e7af83eeaab8fe2fd16b9de "BT_ISO_ISO_INTERVAL_MIN") to [BT\_ISO\_ISO\_INTERVAL\_MAX](group__bt__iso.md#gabc381a7f565061ec91d23b7783521da3 "BT_ISO_ISO_INTERVAL_MAX").

## [◆ ](#ae81ee3dada58a3354c70401380916cbc)packing

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_cap\_initiator\_broadcast\_create\_param::packing |
| --- |

Broadcast Source packing mode.

[BT\_ISO\_PACKING\_SEQUENTIAL](group__bt__iso.md#ga6275e8d805e2366522a78f18ca47ac19 "BT_ISO_PACKING_SEQUENTIAL") or [BT\_ISO\_PACKING\_INTERLEAVED](group__bt__iso.md#ga35b037fcce858857642b4c54bae8dd79 "BT_ISO_PACKING_INTERLEAVED").

Note
:   This is a recommendation to the controller, which the controller may ignore.

## [◆ ](#a01d6ffb369caaf808d4b55b3b1748890)pto

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_cap\_initiator\_broadcast\_create\_param::pto |
| --- |

Pre-transmission offset.

Offset used for pre-transmissions.

Value range from [BT\_ISO\_PTO\_MIN](group__bt__iso.md#ga3f19aaa432290d67fdf4911d1d044dd8 "BT_ISO_PTO_MIN") to [BT\_ISO\_PTO\_MAX](group__bt__iso.md#ga27e812e35a1f12329310851eb9c056f2 "BT_ISO_PTO_MAX").

## [◆ ](#a142125e620776aed464d90f280ef1a4c)qos

| struct [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md)\* bt\_cap\_initiator\_broadcast\_create\_param::qos |
| --- |

Quality of Service configuration.

## [◆ ](#aee3e0244b59503311bc445f36977a85b)subgroup\_count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_cap\_initiator\_broadcast\_create\_param::subgroup\_count |
| --- |

The number of parameters in `subgroup_params`.

## [◆ ](#a2eafc157450237cf311d6144e7431839)subgroup\_params

| struct [bt\_cap\_initiator\_broadcast\_subgroup\_param](structbt__cap__initiator__broadcast__subgroup__param.md)\* bt\_cap\_initiator\_broadcast\_create\_param::subgroup\_params |
| --- |

Array of stream parameters.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_initiator\_broadcast\_create\_param](structbt__cap__initiator__broadcast__create__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
