---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__cap__initiator__broadcast__create__param.html
original_path: doxygen/html/structbt__cap__initiator__broadcast__create__param.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_initiator\_broadcast\_create\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [subgroup\_count](#aee3e0244b59503311bc445f36977a85b) |
|  | The number of parameters in `subgroup_params`. |
| struct [bt\_cap\_initiator\_broadcast\_subgroup\_param](structbt__cap__initiator__broadcast__subgroup__param.md) \* | [subgroup\_params](#a2eafc157450237cf311d6144e7431839) |
|  | Array of stream parameters. |
| struct [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md) \* | [qos](#af7533744fc262dac4d71bc98d33bbee2) |
|  | Quality of Service configuration. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packing](#ae81ee3dada58a3354c70401380916cbc) |
|  | Broadcast Source packing mode. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [encryption](#a4432bee0e365c189996b9f70c7226542) |
|  | Whether or not to encrypt the streams. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [broadcast\_code](#a9053fbfd5b847db896b3d832338f6b92) [[BT\_AUDIO\_BROADCAST\_CODE\_SIZE](group__bt__audio.md#ga6eedc1f97491b38fe20b91688c62ffc0)] |
|  | 16-octet broadcast code. |

## Field Documentation

## [◆ ](#a9053fbfd5b847db896b3d832338f6b92)broadcast\_code

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_cap\_initiator\_broadcast\_create\_param::broadcast\_code[[BT\_AUDIO\_BROADCAST\_CODE\_SIZE](group__bt__audio.md#ga6eedc1f97491b38fe20b91688c62ffc0)] |
| --- |

16-octet broadcast code.

Only valid if `encrypt` is true.

If the value is a string or a the value is less than 16 octets, the remaining octets shall be 0.

Example: The string "Broadcast Code" shall be [42 72 6F 61 64 63 61 73 74 20 43 6F 64 65 00 00]

## [◆ ](#a4432bee0e365c189996b9f70c7226542)encryption

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_cap\_initiator\_broadcast\_create\_param::encryption |
| --- |

Whether or not to encrypt the streams.

## [◆ ](#ae81ee3dada58a3354c70401380916cbc)packing

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_cap\_initiator\_broadcast\_create\_param::packing |
| --- |

Broadcast Source packing mode.

[BT\_ISO\_PACKING\_SEQUENTIAL](group__bt__iso.md#ga6275e8d805e2366522a78f18ca47ac19 "BT_ISO_PACKING_SEQUENTIAL") or [BT\_ISO\_PACKING\_INTERLEAVED](group__bt__iso.md#ga35b037fcce858857642b4c54bae8dd79 "BT_ISO_PACKING_INTERLEAVED").

Note
:   This is a recommendation to the controller, which the controller may ignore.

## [◆ ](#af7533744fc262dac4d71bc98d33bbee2)qos

| struct [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md)\* bt\_cap\_initiator\_broadcast\_create\_param::qos |
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
