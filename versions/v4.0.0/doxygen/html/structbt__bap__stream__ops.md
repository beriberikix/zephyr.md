---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__bap__stream__ops.html
original_path: doxygen/html/structbt__bap__stream__ops.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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
| void(\* | [configured](#a509a400c622d1684e6ab0d47bc6300ba) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const struct [bt\_bap\_qos\_cfg\_pref](structbt__bap__qos__cfg__pref.md) \*pref) |
|  | Stream configured callback. |
| void(\* | [qos\_set](#add541b683a0042bde13749b327b897dd) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
|  | Stream QoS set callback. |
| void(\* | [enabled](#a1c67137b439a87647994530710d9e075) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
|  | Stream enabled callback. |
| void(\* | [metadata\_updated](#a553777c6b6bdda3e0e8c03f3915404cd) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
|  | Stream metadata updated callback. |
| void(\* | [disabled](#a3fc784b8a2a7c1a5b19dece3619c130e) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
|  | Stream disabled callback. |
| void(\* | [released](#a37876562731d7dbbcd5f5613621b78ca) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
|  | Stream released callback. |
| void(\* | [started](#a7f595e37d40b94510bf09c1f82b479f3) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
|  | Stream started callback. |
| void(\* | [stopped](#ab50ea295069a2cd1ab6f4353052262f5) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
|  | Stream stopped callback. |
| void(\* | [recv](#a09f31dc30de9c880758ec4a1468e59f0) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const struct [bt\_iso\_recv\_info](structbt__iso__recv__info.md) \*info, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Stream audio HCI receive callback. |
| void(\* | [sent](#a33b07c51394dea6d632f42aec89a1510) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
|  | Stream audio HCI sent callback. |
| void(\* | [connected](#a533d5ea96aa67b9b74b19c55afd43df1) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
|  | Isochronous channel connected callback. |
| void(\* | [disconnected](#a953c7174297f1a27ceed012dced53c5a) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
|  | Isochronous channel disconnected callback. |

## Detailed Description

Stream operation.

## Field Documentation

## [◆ ](#a509a400c622d1684e6ab0d47bc6300ba)configured

| void(\* bt\_bap\_stream\_ops::configured) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const struct [bt\_bap\_qos\_cfg\_pref](structbt__bap__qos__cfg__pref.md) \*pref) |
| --- |

Stream configured callback.

Configured callback is called whenever an Audio Stream has been configured.

Parameters
:   | stream | Stream object that has been configured. |
    | --- | --- |
    | pref | Remote QoS preferences. |

## [◆ ](#a533d5ea96aa67b9b74b19c55afd43df1)connected

| void(\* bt\_bap\_stream\_ops::connected) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
| --- |

Isochronous channel connected callback.

If this callback is provided it will be called whenever the isochronous channel for the stream has been connected. This does not mean that the stream is ready to be used, which is indicated by the [bt\_bap\_stream\_ops::started](#a7f595e37d40b94510bf09c1f82b479f3) callback.

If the stream shares an isochronous channel with another stream, then this callback may still be called, without the stream going into the started state.

Parameters
:   | stream | Stream object. |
    | --- | --- |

## [◆ ](#a3fc784b8a2a7c1a5b19dece3619c130e)disabled

| void(\* bt\_bap\_stream\_ops::disabled) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
| --- |

Stream disabled callback.

Disabled callback is called whenever an Audio Stream has been disabled.

Parameters
:   | stream | Stream object that has been disabled. |
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

## [◆ ](#a1c67137b439a87647994530710d9e075)enabled

| void(\* bt\_bap\_stream\_ops::enabled) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
| --- |

Stream enabled callback.

Enabled callback is called whenever an Audio Stream has been enabled.

Parameters
:   | stream | Stream object that has been enabled. |
    | --- | --- |

## [◆ ](#a553777c6b6bdda3e0e8c03f3915404cd)metadata\_updated

| void(\* bt\_bap\_stream\_ops::metadata\_updated) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
| --- |

Stream metadata updated callback.

Metadata Updated callback is called whenever an Audio Stream's metadata has been updated.

Parameters
:   | stream | Stream object that had its metadata updated. |
    | --- | --- |

## [◆ ](#add541b683a0042bde13749b327b897dd)qos\_set

| void(\* bt\_bap\_stream\_ops::qos\_set) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
| --- |

Stream QoS set callback.

QoS set callback is called whenever an Audio Stream Quality of Service has been set or updated.

Parameters
:   | stream | Stream object that had its QoS updated. |
    | --- | --- |

## [◆ ](#a09f31dc30de9c880758ec4a1468e59f0)recv

| void(\* bt\_bap\_stream\_ops::recv) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const struct [bt\_iso\_recv\_info](structbt__iso__recv__info.md) \*info, struct [net\_buf](structnet__buf.md) \*buf) |
| --- |

Stream audio HCI receive callback.

This callback is only used if the ISO data path is HCI.

Parameters
:   | stream | Stream object. |
    | --- | --- |
    | info | Pointer to the metadata for the buffer. The lifetime of the pointer is linked to the lifetime of the [net\_buf](structnet__buf.md "Network buffer representation."). Metadata such as sequence number and timestamp can be provided by the bluetooth controller. |
    | buf | Buffer containing incoming audio data. |

## [◆ ](#a37876562731d7dbbcd5f5613621b78ca)released

| void(\* bt\_bap\_stream\_ops::released) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
| --- |

Stream released callback.

Released callback is called whenever a Audio Stream has been released and can be deallocated.

Parameters
:   | stream | Stream object that has been released. |
    | --- | --- |

## [◆ ](#a33b07c51394dea6d632f42aec89a1510)sent

| void(\* bt\_bap\_stream\_ops::sent) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
| --- |

Stream audio HCI sent callback.

This callback will be called once the controller marks the SDU as completed. When the controller does so is implementation dependent. It could be after the SDU is enqueued for transmission, or after it is sent on air or flushed.

This callback is only used if the ISO data path is HCI.

Parameters
:   | stream | Stream object. |
    | --- | --- |

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
