---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__bap__broadcast__source__cb.html
original_path: doxygen/html/structbt__bap__broadcast__source__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_broadcast\_source\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md) | [Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md) » [BAP Broadcast APIs](group__bt__bap__broadcast.md) » [BAP Broadcast Source APIs](group__bt__bap__broadcast__source.md)

Struct to hold the Broadcast Source callbacks.
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [started](#a1108c983823ee3331d8343db4ec9c0c5) )(struct bt\_bap\_broadcast\_source \*source) |
|  | The Broadcast Source has started and all of the streams are ready for audio data. |
| void(\* | [stopped](#a66b62e90c1cdfa2c2963bafe99670f92) )(struct bt\_bap\_broadcast\_source \*source, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
|  | The Broadcast Source has stopped and none of the streams are ready for audio data. |

## Detailed Description

Struct to hold the Broadcast Source callbacks.

These can be registered for usage with [bt\_bap\_broadcast\_source\_register\_cb()](group__bt__bap__broadcast__source.md#gac75ad00b8f9a1cd7048677a33b17acda "Registers callbacks for Broadcast Sources.").

## Field Documentation

## [◆ ](#a1108c983823ee3331d8343db4ec9c0c5)started

| void(\* bt\_bap\_broadcast\_source\_cb::started) (struct bt\_bap\_broadcast\_source \*source) |
| --- |

The Broadcast Source has started and all of the streams are ready for audio data.

Parameters
:   | source | The started Broadcast Source |
    | --- | --- |

## [◆ ](#a66b62e90c1cdfa2c2963bafe99670f92)stopped

| void(\* bt\_bap\_broadcast\_source\_cb::stopped) (struct bt\_bap\_broadcast\_source \*source, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
| --- |

The Broadcast Source has stopped and none of the streams are ready for audio data.

Parameters
:   | source | The stopped Broadcast Source |
    | --- | --- |
    | reason | The reason why the Broadcast Source stopped (see the BT\_HCI\_ERR\_\* values) |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_broadcast\_source\_cb](structbt__bap__broadcast__source__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
