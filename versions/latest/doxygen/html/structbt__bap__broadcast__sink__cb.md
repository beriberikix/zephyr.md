---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__bap__broadcast__sink__cb.html
original_path: doxygen/html/structbt__bap__broadcast__sink__cb.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_broadcast\_sink\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md) | [Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md) » [BAP Broadcast APIs](group__bt__bap__broadcast.md) » [BAP Broadcast Sink APIs](group__bt__bap__broadcast__sink.md)

Broadcast Audio Sink callback structure.
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [base\_recv](#a1adf2124ec9a16c3c68774194febd0fc) )(struct bt\_bap\_broadcast\_sink \*sink, const struct bt\_bap\_base \*base, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) base\_size) |
|  | Broadcast Audio Source Endpoint (BASE) received. |
| void(\* | [syncable](#ac2c8389a8e68e5b4afe735f623dc36ec) )(struct bt\_bap\_broadcast\_sink \*sink, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) encrypted) |
|  | Broadcast sink is syncable. |

## Detailed Description

Broadcast Audio Sink callback structure.

## Field Documentation

## [◆ ](#a1adf2124ec9a16c3c68774194febd0fc)base\_recv

| void(\* bt\_bap\_broadcast\_sink\_cb::base\_recv) (struct bt\_bap\_broadcast\_sink \*sink, const struct bt\_bap\_base \*base, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) base\_size) |
| --- |

Broadcast Audio Source Endpoint (BASE) received.

Callback for when we receive a BASE from a broadcaster after syncing to the broadcaster's periodic advertising.

Parameters
:   | sink | Pointer to the sink structure. |
    | --- | --- |
    | base | Broadcast Audio Source Endpoint (BASE). |
    | base\_size | Size of the `base` |

## [◆ ](#ac2c8389a8e68e5b4afe735f623dc36ec)syncable

| void(\* bt\_bap\_broadcast\_sink\_cb::syncable) (struct bt\_bap\_broadcast\_sink \*sink, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) encrypted) |
| --- |

Broadcast sink is syncable.

Called whenever a broadcast sink is not synchronized to audio, but the audio is synchronizable. This is inferred when a BIGInfo report is received.

Once this callback has been called, it is possible to call [bt\_bap\_broadcast\_sink\_sync()](group__bt__bap__broadcast__sink.md#ga3485ef8527928209274ae0b5351b72b3 "Sync to a broadcaster's audio.") to synchronize to the audio stream(s).

Parameters
:   | sink | Pointer to the sink structure. |
    | --- | --- |
    | encrypted | Whether or not the broadcast is encrypted |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_broadcast\_sink\_cb](structbt__bap__broadcast__sink__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
