---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__vcp__vol__rend__register__param.html
original_path: doxygen/html/structbt__vcp__vol__rend__register__param.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_vcp\_vol\_rend\_register\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Volume Control Profile (VCP)](group__bt__gatt__vcp.md)

Register structure for Volume Control Service.
[More...](#details)

`#include <[vcp.h](vcp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [step](#a098e6c6921813b3f0dc7512cd483c829) |
|  | Initial step size (1-255). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mute](#a93f2b246ac4241db468a46a64909866e) |
|  | Initial mute state (0-1). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [volume](#a6cf1343a2b3033c3f4676d66017cfda7) |
|  | Initial volume level (0-255). |
| struct [bt\_vocs\_register\_param](structbt__vocs__register__param.md) | [vocs\_param](#a45eb75a4590d278cec0cf4cf6d94dda3) [0] |
|  | Register parameters for Volume Offset Control Services. |
| struct [bt\_aics\_register\_param](structbt__aics__register__param.md) | [aics\_param](#a1e3a4744de697d92d0fc8b9e27593417) [0] |
|  | Register parameters for Audio Input Control Services. |
| struct [bt\_vcp\_vol\_rend\_cb](structbt__vcp__vol__rend__cb.md) \* | [cb](#af9a09c453394fd4a28d6415e2775c3f5) |
|  | Volume Control Service callback structure. |

## Detailed Description

Register structure for Volume Control Service.

## Field Documentation

## [◆ ](#a1e3a4744de697d92d0fc8b9e27593417)aics\_param

| struct [bt\_aics\_register\_param](structbt__aics__register__param.md) bt\_vcp\_vol\_rend\_register\_param::aics\_param[0] |
| --- |

Register parameters for Audio Input Control Services.

## [◆ ](#af9a09c453394fd4a28d6415e2775c3f5)cb

| struct [bt\_vcp\_vol\_rend\_cb](structbt__vcp__vol__rend__cb.md)\* bt\_vcp\_vol\_rend\_register\_param::cb |
| --- |

Volume Control Service callback structure.

## [◆ ](#a93f2b246ac4241db468a46a64909866e)mute

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_vcp\_vol\_rend\_register\_param::mute |
| --- |

Initial mute state (0-1).

## [◆ ](#a098e6c6921813b3f0dc7512cd483c829)step

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_vcp\_vol\_rend\_register\_param::step |
| --- |

Initial step size (1-255).

## [◆ ](#a45eb75a4590d278cec0cf4cf6d94dda3)vocs\_param

| struct [bt\_vocs\_register\_param](structbt__vocs__register__param.md) bt\_vcp\_vol\_rend\_register\_param::vocs\_param[0] |
| --- |

Register parameters for Volume Offset Control Services.

## [◆ ](#a6cf1343a2b3033c3f4676d66017cfda7)volume

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_vcp\_vol\_rend\_register\_param::volume |
| --- |

Initial volume level (0-255).

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[vcp.h](vcp_8h_source.md)

- [bt\_vcp\_vol\_rend\_register\_param](structbt__vcp__vol__rend__register__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
