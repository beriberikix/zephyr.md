---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__blob__io.html
original_path: doxygen/html/structbt__mesh__blob__io.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_blob\_io Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh BLOB model API](group__bt__mesh__blob.md)

BLOB stream.
[More...](#details)

`#include <[blob.h](blob_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [open](#a4666a3fafde0ee9fdd51d27732bec6bc) )(const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io, const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer, enum [bt\_mesh\_blob\_io\_mode](group__bt__mesh__blob.md#ga2618fb7365f180a73a7eecd11cf2f962) mode) |
|  | Open callback. |
| void(\* | [close](#aac42902d0bbbef10a5e9cc35e8a3ea64) )(const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io, const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer) |
|  | Close callback. |
| int(\* | [block\_start](#a900f049b6a778d9e0973ee66b46dc046) )(const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io, const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer, const struct [bt\_mesh\_blob\_block](structbt__mesh__blob__block.md) \*block) |
|  | Block start callback. |
| void(\* | [block\_end](#a57381249bf63924b2345ece6e12909cb) )(const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io, const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer, const struct [bt\_mesh\_blob\_block](structbt__mesh__blob__block.md) \*block) |
|  | Block end callback. |
| int(\* | [wr](#ae0b27ea814e5c939d708ae20d452ca09) )(const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io, const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer, const struct [bt\_mesh\_blob\_block](structbt__mesh__blob__block.md) \*block, const struct [bt\_mesh\_blob\_chunk](structbt__mesh__blob__chunk.md) \*chunk) |
|  | Chunk data write callback. |
| int(\* | [rd](#a330ec5dcc8d18b84e7fdab9ef6d75f49) )(const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io, const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer, const struct [bt\_mesh\_blob\_block](structbt__mesh__blob__block.md) \*block, const struct [bt\_mesh\_blob\_chunk](structbt__mesh__blob__chunk.md) \*chunk) |
|  | Chunk data read callback. |

## Detailed Description

BLOB stream.

## Field Documentation

## [◆ ](#a57381249bf63924b2345ece6e12909cb)block\_end

| void(\* bt\_mesh\_blob\_io::block\_end) (const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io, const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer, const struct [bt\_mesh\_blob\_block](structbt__mesh__blob__block.md) \*block) |
| --- |

Block end callback.

Called when the current block has been transmitted in full. No data from this block will be requested again, and the application data associated with this block may be discarded.

Parameters
:   | io | BLOB stream. |
    | --- | --- |
    | xfer | BLOB transfer. |
    | block | Block that finished sending. |

## [◆ ](#a900f049b6a778d9e0973ee66b46dc046)block\_start

| int(\* bt\_mesh\_blob\_io::block\_start) (const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io, const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer, const struct [bt\_mesh\_blob\_block](structbt__mesh__blob__block.md) \*block) |
| --- |

Block start callback.

Called when a new block is opened for sending. Each block is only sent once, and are always sent in increasing order. The data chunks inside a single block may be requested out of order and multiple times.

Parameters
:   | io | BLOB stream. |
    | --- | --- |
    | xfer | BLOB transfer. |
    | block | Block that was started. |

## [◆ ](#aac42902d0bbbef10a5e9cc35e8a3ea64)close

| void(\* bt\_mesh\_blob\_io::close) (const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io, const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer) |
| --- |

Close callback.

Called when the reader is closed.

Parameters
:   | io | BLOB stream. |
    | --- | --- |
    | xfer | BLOB transfer. |

## [◆ ](#a4666a3fafde0ee9fdd51d27732bec6bc)open

| int(\* bt\_mesh\_blob\_io::open) (const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io, const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer, enum [bt\_mesh\_blob\_io\_mode](group__bt__mesh__blob.md#ga2618fb7365f180a73a7eecd11cf2f962) mode) |
| --- |

Open callback.

Called when the reader is opened for reading.

Parameters
:   | io | BLOB stream. |
    | --- | --- |
    | xfer | BLOB transfer. |
    | mode | Direction of the stream (read/write). |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#a330ec5dcc8d18b84e7fdab9ef6d75f49)rd

| int(\* bt\_mesh\_blob\_io::rd) (const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io, const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer, const struct [bt\_mesh\_blob\_block](structbt__mesh__blob__block.md) \*block, const struct [bt\_mesh\_blob\_chunk](structbt__mesh__blob__chunk.md) \*chunk) |
| --- |

Chunk data read callback.

Used by the BLOB Transfer Client to fetch outgoing data.

The Client calls the chunk data request callback to populate a chunk message going out to the Target nodes. The data request callback may be called out of order and multiple times for each offset, and cannot be used as an indication of progress.

Returning a non-zero status code on the chunk data request callback results in termination of the transfer.

Parameters
:   | io | BLOB stream. |
    | --- | --- |
    | xfer | BLOB transfer. |
    | block | Block the chunk is part of. |
    | chunk | Chunk to get the data of. The buffer pointer to by the `data` member should be filled by the callback. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ae0b27ea814e5c939d708ae20d452ca09)wr

| int(\* bt\_mesh\_blob\_io::wr) (const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io, const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer, const struct [bt\_mesh\_blob\_block](structbt__mesh__blob__block.md) \*block, const struct [bt\_mesh\_blob\_chunk](structbt__mesh__blob__chunk.md) \*chunk) |
| --- |

Chunk data write callback.

Used by the BLOB Transfer Server on incoming data.

Each block is divided into chunks of data. This callback is called when a new chunk of data is received. Chunks may be received in any order within their block.

If the callback returns successfully, this chunk will be marked as received, and will not be received again unless the block is restarted due to a transfer suspension. If the callback returns a non-zero value, the chunk remains unreceived, and the BLOB Transfer Client will attempt to resend it later.

Note that the Client will only perform a limited number of attempts at delivering a chunk before dropping a Target node from the transfer. The number of retries performed by the Client is implementation specific.

Parameters
:   | io | BLOB stream. |
    | --- | --- |
    | xfer | BLOB transfer. |
    | block | Block the chunk is part of. |
    | chunk | Received chunk. |

Returns
:   0 on success, or (negative) error code otherwise.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[blob.h](blob_8h_source.md)

- [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
