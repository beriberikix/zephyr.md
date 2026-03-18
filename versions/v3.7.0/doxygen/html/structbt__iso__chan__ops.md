---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__iso__chan__ops.html
original_path: doxygen/html/structbt__iso__chan__ops.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_iso\_chan\_ops Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Isochronous channels (ISO)](group__bt__iso.md)

ISO Channel operations structure.
[More...](#details)

`#include <[iso.h](iso_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [connected](#a6b0e51770158da7b728e1084a8e44504) )(struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan) |
|  | Channel connected callback. |
| void(\* | [disconnected](#a2069849352019362e5dc7d68f835f359) )(struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
|  | Channel disconnected callback. |
| struct [net\_buf](structnet__buf.md) \*(\* | [alloc\_buf](#a7bf9fe04f42bacd59f623aa28a3b0665) )(struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan) |
|  | Channel alloc\_buf callback. |
| void(\* | [recv](#a6d5d9423fff83f8f337f97b3fc018f39) )(struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan, const struct [bt\_iso\_recv\_info](structbt__iso__recv__info.md) \*info, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Channel recv callback. |
| void(\* | [sent](#a048954070628229b8aacd373de1fb236) )(struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan) |
|  | Channel sent callback. |

## Detailed Description

ISO Channel operations structure.

## Field Documentation

## [◆ ](#a7bf9fe04f42bacd59f623aa28a3b0665)alloc\_buf

| struct [net\_buf](structnet__buf.md) \*(\* bt\_iso\_chan\_ops::alloc\_buf) (struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan) |
| --- |

Channel alloc\_buf callback.

If this callback is provided the channel will use it to allocate buffers to store incoming data.

Parameters
:   | chan | The channel requesting a buffer. |
    | --- | --- |

Returns
:   Allocated buffer.

## [◆ ](#a6b0e51770158da7b728e1084a8e44504)connected

| void(\* bt\_iso\_chan\_ops::connected) (struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan) |
| --- |

Channel connected callback.

If this callback is provided it will be called whenever the connection completes.

For a peripheral, the QoS values (see [bt\_iso\_chan\_io\_qos](structbt__iso__chan__io__qos.md "bt_iso_chan_io_qos")) are set when this is called. The peripheral does not have any information about the RTN though.

Parameters
:   | chan | The channel that has been connected |
    | --- | --- |

## [◆ ](#a2069849352019362e5dc7d68f835f359)disconnected

| void(\* bt\_iso\_chan\_ops::disconnected) (struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
| --- |

Channel disconnected callback.

If this callback is provided it will be called whenever the channel is disconnected, including when a connection gets rejected or when setting security fails.

Parameters
:   | chan | The channel that has been Disconnected |
    | --- | --- |
    | reason | BT\_HCI\_ERR\_\* reason for the disconnection. |

## [◆ ](#a6d5d9423fff83f8f337f97b3fc018f39)recv

| void(\* bt\_iso\_chan\_ops::recv) (struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan, const struct [bt\_iso\_recv\_info](structbt__iso__recv__info.md) \*info, struct [net\_buf](structnet__buf.md) \*buf) |
| --- |

Channel recv callback.

Parameters
:   | chan | The channel receiving data. |
    | --- | --- |
    | buf | Buffer containing incoming data. |
    | info | Pointer to the metadata for the buffer. The lifetime of the pointer is linked to the lifetime of the [net\_buf](structnet__buf.md "Network buffer representation."). Metadata such as sequence number and timestamp can be provided by the bluetooth controller. |

## [◆ ](#a048954070628229b8aacd373de1fb236)sent

| void(\* bt\_iso\_chan\_ops::sent) (struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan) |
| --- |

Channel sent callback.

This callback will be called once the controller marks the SDU as completed. When the controller does so is implementation dependent. It could be after the SDU is enqueued for transmission, or after it is sent on air or flushed.

Parameters
:   | chan | The channel which has sent data. |
    | --- | --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[iso.h](iso_8h_source.md)

- [bt\_iso\_chan\_ops](structbt__iso__chan__ops.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
