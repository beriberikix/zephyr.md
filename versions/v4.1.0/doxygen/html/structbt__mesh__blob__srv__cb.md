---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__mesh__blob__srv__cb.html
original_path: doxygen/html/structbt__mesh__blob__srv__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_blob\_srv\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh BLOB Transfer Server model API](group__bt__mesh__blob__srv.md)

BLOB Transfer Server model event handlers.
[More...](#details)

`#include <[blob_srv.h](blob__srv_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [start](#aad5ab6e396f049a3b8a239e9f0d1c063) )(struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer) |
|  | Transfer start callback. |
| void(\* | [end](#af7b6f557f38c15a174a2a75d1210dab3) )(struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) success) |
|  | Transfer end callback. |
| void(\* | [suspended](#a99a054d410f0a82101b15309a8f4ec33) )(struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv) |
|  | Transfer suspended callback. |
| void(\* | [resume](#ae032ff1d52f46f1716451dc5ff138d0f) )(struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv) |
|  | Transfer resume callback. |
| int(\* | [recover](#a94b56462c5fd95535a5f1e0ba2ddf99a) )(struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv, struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer, const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*\*io) |
|  | Transfer recovery callback. |

## Detailed Description

BLOB Transfer Server model event handlers.

All callbacks are optional.

## Field Documentation

## [◆ ](#af7b6f557f38c15a174a2a75d1210dab3)end

| void(\* bt\_mesh\_blob\_srv\_cb::end) (struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) success) |
| --- |

Transfer end callback.

Called when the transfer ends, either because it was cancelled, or because it finished successfully. A new transfer may be prepared.

Note
:   The transfer may end before it's started if the start parameters are invalid.

Parameters
:   | srv | BLOB Transfer Server instance. |
    | --- | --- |
    | id | BLOB ID of the cancelled transfer. |
    | success | Whether the transfer was successful. |

## [◆ ](#a94b56462c5fd95535a5f1e0ba2ddf99a)recover

| int(\* bt\_mesh\_blob\_srv\_cb::recover) (struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv, struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer, const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*\*io) |
| --- |

Transfer recovery callback.

Called when the Bluetooth Mesh subsystem is started if the device is rebooted in the middle of a transfer.

Transfers will not be resumed after a reboot if this callback is not defined.

Parameters
:   | srv | BLOB Transfer Server instance. |
    | --- | --- |
    | xfer | Transfer to resume. |
    | io | BLOB stream return parameter. Must be set to a valid BLOB stream by the callback. |

Returns
:   0 on success, or (negative) error code to abandon the transfer.

## [◆ ](#ae032ff1d52f46f1716451dc5ff138d0f)resume

| void(\* bt\_mesh\_blob\_srv\_cb::resume) (struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv) |
| --- |

Transfer resume callback.

Called if the transfer is resumed after being suspended.

Parameters
:   | srv | BLOB Transfer Server instance. |
    | --- | --- |

## [◆ ](#aad5ab6e396f049a3b8a239e9f0d1c063)start

| int(\* bt\_mesh\_blob\_srv\_cb::start) (struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer) |
| --- |

Transfer start callback.

Called when the transfer has started with the prepared BLOB ID.

Parameters
:   | srv | BLOB Transfer Server instance. |
    | --- | --- |
    | ctx | Message context for the incoming start message. The entire transfer will be sent from the same source address. |
    | xfer | Transfer parameters. |

Returns
:   0 on success, or (negative) error code to reject the transfer.

## [◆ ](#a99a054d410f0a82101b15309a8f4ec33)suspended

| void(\* bt\_mesh\_blob\_srv\_cb::suspended) (struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv) |
| --- |

Transfer suspended callback.

Called if the Server timed out while waiting for a transfer packet. A suspended transfer may resume later from the start of the current block. Any received chunks in the current block should be discarded, they will be received again if the transfer resumes.

The transfer will call `resumed` again when resuming.

Note
:   The BLOB Transfer Server does not run a timer in the suspended state, and it's up to the application to determine whether the transfer should be permanently cancelled. Without interaction, the transfer will be suspended indefinitely, and the BLOB Transfer Server will not accept any new transfers.

Parameters
:   | srv | BLOB Transfer Server instance. |
    | --- | --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[blob\_srv.h](blob__srv_8h_source.md)

- [bt\_mesh\_blob\_srv\_cb](structbt__mesh__blob__srv__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
