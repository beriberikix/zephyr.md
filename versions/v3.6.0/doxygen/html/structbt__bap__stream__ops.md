---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__bap__stream__ops.html
original_path: doxygen/html/structbt__bap__stream__ops.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_stream\_ops Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md)

Stream operation.
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [started](#a7f595e37d40b94510bf09c1f82b479f3) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
|  | Stream started callback. |
| void(\* | [stopped](#ab50ea295069a2cd1ab6f4353052262f5) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
|  | Stream stopped callback. |
| void(\* | [connected](#a533d5ea96aa67b9b74b19c55afd43df1) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
|  | Isochronous channel connected callback. |
| void(\* | [disconnected](#a953c7174297f1a27ceed012dced53c5a) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
|  | Isochronous channel disconnected callback. |

## Detailed Description

Stream operation.

## Field Documentation

## [◆ ](#a533d5ea96aa67b9b74b19c55afd43df1)connected

| void(\* bt\_bap\_stream\_ops::connected) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
| --- |

Isochronous channel connected callback.

If this callback is provided it will be called whenever the isochronous channel for the stream has been connected. This does not mean that the stream is ready to be used, which is indicated by the [bt\_bap\_stream\_ops::started](#a7f595e37d40b94510bf09c1f82b479f3) callback.

If the stream shares an isochronous channel with another stream, then this callback may still be called, without the stream going into the started state.

Parameters
:   | stream | Stream object. |
    | --- | --- |

## [◆ ](#a953c7174297f1a27ceed012dced53c5a)disconnected

| void(\* bt\_bap\_stream\_ops::disconnected) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
| --- |

Isochronous channel disconnected callback.

If this callback is provided it will be called whenever the isochronous channel is disconnected, including when a connection gets rejected.

If the stream shares an isochronous channel with another stream, then this callback may not be called, even if the stream is leaving the streaming state.

Parameters
:   | stream | Stream object. |
    | --- | --- |
    | reason | BT\_HCI\_ERR\_\* reason for the disconnection. |

## [◆ ](#a7f595e37d40b94510bf09c1f82b479f3)started

| void(\* bt\_bap\_stream\_ops::started) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
| --- |

Stream started callback.

Started callback is called whenever an Audio Stream has been started and will be usable for streaming.

Parameters
:   | stream | Stream object that has been started. |
    | --- | --- |

## [◆ ](#ab50ea295069a2cd1ab6f4353052262f5)stopped

| void(\* bt\_bap\_stream\_ops::stopped) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
| --- |

Stream stopped callback.

Stopped callback is called whenever an Audio Stream has been stopped.

Parameters
:   | stream | Stream object that has been stopped. |
    | --- | --- |
    | reason | BT\_HCI\_ERR\_\* reason for the disconnection. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
