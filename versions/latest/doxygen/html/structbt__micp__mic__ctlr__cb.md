---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__micp__mic__ctlr__cb.html
original_path: doxygen/html/structbt__micp__mic__ctlr__cb.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_micp\_mic\_ctlr\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Microphone Control Profile (MICP)](group__bt__gatt__micp.md)

`#include <[micp.h](micp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [mute](#a21786359322dbd6f814929293a69482f) )(struct bt\_micp\_mic\_ctlr \*mic\_ctlr, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mute) |
|  | Callback function for Microphone Control Profile mute. |
| void(\* | [discover](#a2359b88344bf36c3a491b0126dac006b) )(struct bt\_micp\_mic\_ctlr \*mic\_ctlr, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) aics\_count) |
|  | Callback function for [bt\_micp\_mic\_ctlr\_discover()](group__bt__gatt__micp.md#ga26187007ebf35ba2a5c57a076a3a7212 "Discover Microphone Control Service."). |
| void(\* | [mute\_written](#ae15fb539599feab59041e30a121021f0) )(struct bt\_micp\_mic\_ctlr \*mic\_ctlr, int err) |
|  | Callback function for Microphone Control Profile mute/unmute. |
| void(\* | [unmute\_written](#a03afd3a79838c15be9262f441a3d338b) )(struct bt\_micp\_mic\_ctlr \*mic\_ctlr, int err) |
|  | Callback function for Microphone Control Profile mute/unmute. |

## Field Documentation

## [◆ ](#a2359b88344bf36c3a491b0126dac006b)discover

| void(\* bt\_micp\_mic\_ctlr\_cb::discover) (struct bt\_micp\_mic\_ctlr \*mic\_ctlr, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) aics\_count) |
| --- |

Callback function for [bt\_micp\_mic\_ctlr\_discover()](group__bt__gatt__micp.md#ga26187007ebf35ba2a5c57a076a3a7212 "Discover Microphone Control Service.").

Parameters
:   | mic\_ctlr | Microphone Controller instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail. |
    | aics\_count | Number of Audio Input Control Service instances on peer device. |

## [◆ ](#a21786359322dbd6f814929293a69482f)mute

| void(\* bt\_micp\_mic\_ctlr\_cb::mute) (struct bt\_micp\_mic\_ctlr \*mic\_ctlr, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mute) |
| --- |

Callback function for Microphone Control Profile mute.

Called when the value is read, or if the value is changed by either the Microphone Device or a Microphone Controller.

Parameters
:   | mic\_ctlr | Microphone Controller instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail. For notifications, this will always be 0. |
    | [mute](#a21786359322dbd6f814929293a69482f) | The mute setting of the Microphone Control Service. |

## [◆ ](#ae15fb539599feab59041e30a121021f0)mute\_written

| void(\* bt\_micp\_mic\_ctlr\_cb::mute\_written) (struct bt\_micp\_mic\_ctlr \*mic\_ctlr, int err) |
| --- |

Callback function for Microphone Control Profile mute/unmute.

Parameters
:   | mic\_ctlr | Microphone Controller instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail. |

## [◆ ](#a03afd3a79838c15be9262f441a3d338b)unmute\_written

| void(\* bt\_micp\_mic\_ctlr\_cb::unmute\_written) (struct bt\_micp\_mic\_ctlr \*mic\_ctlr, int err) |
| --- |

Callback function for Microphone Control Profile mute/unmute.

Parameters
:   | mic\_ctlr | Microphone Controller instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[micp.h](micp_8h_source.md)

- [bt\_micp\_mic\_ctlr\_cb](structbt__micp__mic__ctlr__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
