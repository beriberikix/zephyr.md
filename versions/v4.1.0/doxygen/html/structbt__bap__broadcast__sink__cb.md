---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__bap__broadcast__sink__cb.html
original_path: doxygen/html/structbt__bap__broadcast__sink__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| void(\* | [syncable](#a23390a63acbcf831a177a550d1012047) )(struct bt\_bap\_broadcast\_sink \*sink, const struct [bt\_iso\_biginfo](structbt__iso__biginfo.md) \*biginfo) |
|  | Broadcast sink is syncable. |
| void(\* | [started](#a6af7aa849cebad26cdf382a1c97a681f) )(struct bt\_bap\_broadcast\_sink \*sink) |
|  | The Broadcast Sink has started and audio data may be received from all of the streams. |
| void(\* | [stopped](#a1dd64d7c764ddd6c531bdd5b1890694f) )(struct bt\_bap\_broadcast\_sink \*sink, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
|  | The Broadcast Sink has stopped and none of the streams will receive audio data. |

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

## [◆ ](#a6af7aa849cebad26cdf382a1c97a681f)started

| void(\* bt\_bap\_broadcast\_sink\_cb::started) (struct bt\_bap\_broadcast\_sink \*sink) |
| --- |

The Broadcast Sink has started and audio data may be received from all of the streams.

Parameters
:   | sink | The started Broadcast Sink |
    | --- | --- |

## [◆ ](#a1dd64d7c764ddd6c531bdd5b1890694f)stopped

| void(\* bt\_bap\_broadcast\_sink\_cb::stopped) (struct bt\_bap\_broadcast\_sink \*sink, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
| --- |

The Broadcast Sink has stopped and none of the streams will receive audio data.

Parameters
:   | sink | The stopped Broadcast Sink |
    | --- | --- |
    | reason | The reason why the Broadcast Sink stopped (see the BT\_HCI\_ERR\_\* values) |

## [◆ ](#a23390a63acbcf831a177a550d1012047)syncable

| void(\* bt\_bap\_broadcast\_sink\_cb::syncable) (struct bt\_bap\_broadcast\_sink \*sink, const struct [bt\_iso\_biginfo](structbt__iso__biginfo.md) \*biginfo) |
| --- |

Broadcast sink is syncable.

Called whenever a broadcast sink is not synchronized to audio, but the audio is synchronizable. This is inferred when a BIGInfo report is received.

Once this callback has been called, it is possible to call [bt\_bap\_broadcast\_sink\_sync()](group__bt__bap__broadcast__sink.md#gacadebb5ce8aab5f5b8f1ff7e0fa57805 "Sync to a broadcaster's audio.") to synchronize to the audio stream(s).

Parameters
:   | sink | Pointer to the sink structure. |
    | --- | --- |
    | biginfo | The BIGInfo report. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_broadcast\_sink\_cb](structbt__bap__broadcast__sink__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
