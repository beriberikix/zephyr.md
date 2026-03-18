---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/api/mesh/blob.html
original_path: connectivity/bluetooth/api/mesh/blob.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# BLOB Transfer models

The Binary Large Object (BLOB) Transfer models implement the Bluetooth Mesh Binary Large Object
Transfer Model specification version 1.0 and provide functionality for sending large binary objects
from a single source to many Target nodes over the Bluetooth Mesh network. It is the underlying
transport method for the [Device Firmware Update (DFU)](dfu.md#bluetooth-mesh-dfu), but may be used for other object transfer
purposes. The implementation is in experimental state.

The BLOB Transfer models support transfers of continuous binary objects of up to 4 GB (2 32
bytes). The BLOB transfer protocol has built-in recovery procedures for packet losses, and sets up
checkpoints to ensure that all targets have received all the data before moving on. Data transfer
order is not guaranteed.

BLOB transfers are constrained by the transfer speed and reliability of the underlying mesh network.
Under ideal conditions, the BLOBs can be transferred at a rate of up to 1 kbps, allowing a 100 kB
BLOB to be transferred in 10-15 minutes. However, network conditions, transfer capabilities and
other limiting factors can easily degrade the data rate by several orders of magnitude. Tuning the
parameters of the transfer according to the application and network configuration, as well as
scheduling it to periods with low network traffic, will offer significant improvements on the speed
and reliability of the protocol. However, achieving transfer rates close to the ideal rate is
unlikely in actual deployments.

There are two BLOB Transfer models:

The BLOB Transfer Client is instantiated on the sender node, and the BLOB Transfer Server is
instantiated on the receiver nodes.

## Concepts

The BLOB transfer protocol introduces several new concepts to implement the BLOB transfer.

### BLOBs

BLOBs are binary objects up to 4 GB in size, that can contain any data the application would like to
transfer through the mesh network. The BLOBs are continuous data objects, divided into blocks and
chunks to make the transfers reliable and easy to process. No limitations are put on the contents or
structure of the BLOB, and applications are free to define any encoding or compression they’d like
on the data itself.

The BLOB transfer protocol does not provide any built-in integrity checks, encryption or
authentication of the BLOB data. However, the underlying encryption of the Bluetooth Mesh protocol
provides data integrity checks and protects the contents of the BLOB from third parties using
network and application level encryption.

#### Blocks

The binary objects are divided into blocks, typically from a few hundred to several thousand bytes
in size. Each block is transmitted separately, and the BLOB Transfer Client ensures that all BLOB
Transfer Servers have received the full block before moving on to the next. The block size is
determined by the transfer’s `block_size_log` parameter, and is the same for all blocks in the
transfer except the last, which may be smaller. For a BLOB stored in flash memory, the block size is
typically a multiple of the flash page size of the Target devices.

#### Chunks

Each block is divided into chunks. A chunk is the smallest data unit in the BLOB transfer, and must
fit inside a single Bluetooth Mesh access message excluding the opcode (379 bytes or less). The
mechanism for transferring chunks depends on the transfer mode.

When operating in Push BLOB Transfer Mode, the chunks are sent as unacknowledged packets from the
BLOB Transfer Client to all targeted BLOB Transfer Servers. Once all chunks in a block have been
sent, the BLOB Transfer Client asks each BLOB Transfer Server if they’re missing any chunks, and
resends them. This is repeated until all BLOB Transfer Servers have received all chunks, or the BLOB
Transfer Client gives up.

When operating in Pull BLOB Transfer Mode, the BLOB Transfer Server will request a small number of
chunks from the BLOB Transfer Client at a time, and wait for the BLOB Transfer Client to send them
before requesting more chunks. This repeats until all chunks have been transferred, or the BLOB
Transfer Server gives up.

Read more about the transfer modes in [Transfer modes](#bluetooth-mesh-blob-transfer-modes) section.

### BLOB streams

In the BLOB Transfer models’ APIs, the BLOB data handling is separated from the high-level transfer
handling. This split allows reuse of different BLOB storage and transfer strategies for different
applications. While the high level transfer is controlled directly by the application, the BLOB data
itself is accessed through a *BLOB stream*.

The BLOB stream is comparable to a standard library file stream. Through opening, closing, reading
and writing, the BLOB Transfer model gets full access to the BLOB data, whether it’s kept in flash,
RAM, or on a peripheral. The BLOB stream is opened with an access mode (read or write) before it’s
used, and the BLOB Transfer models will move around inside the BLOB’s data in blocks and chunks,
using the BLOB stream as an interface.

#### Interaction

Before the BLOB is read or written, the stream is opened by calling its
[`open`](#c.bt_mesh_blob_io.open) callback. When used with a BLOB Transfer Server, the BLOB
stream is always opened in write mode, and when used with a BLOB Transfer Client, it’s always opened
in read mode.

For each block in the BLOB, the BLOB Transfer model starts by calling
[`block_start`](#c.bt_mesh_blob_io.block_start). Then, depending on the access mode, the BLOB
stream’s [`wr`](#c.bt_mesh_blob_io.wr) or [`rd`](#c.bt_mesh_blob_io.rd) callback is
called repeatedly to move data to or from the BLOB. When the model is done processing the block, it
calls [`block_end`](#c.bt_mesh_blob_io.block_end). When the transfer is complete, the BLOB
stream is closed by calling [`close`](#c.bt_mesh_blob_io.close).

#### Implementations

The application may implement their own BLOB stream, or use the implementations provided by Zephyr:

### Transfer capabilities

Each BLOB Transfer Server may have different transfer capabilities. The transfer capabilities of
each device are controlled through the following configuration options:

- [`CONFIG_BT_MESH_BLOB_SIZE_MAX`](../../../../kconfig.md#CONFIG_BT_MESH_BLOB_SIZE_MAX "CONFIG_BT_MESH_BLOB_SIZE_MAX")
- [`CONFIG_BT_MESH_BLOB_BLOCK_SIZE_MIN`](../../../../kconfig.md#CONFIG_BT_MESH_BLOB_BLOCK_SIZE_MIN "CONFIG_BT_MESH_BLOB_BLOCK_SIZE_MIN")
- [`CONFIG_BT_MESH_BLOB_BLOCK_SIZE_MAX`](../../../../kconfig.md#CONFIG_BT_MESH_BLOB_BLOCK_SIZE_MAX "CONFIG_BT_MESH_BLOB_BLOCK_SIZE_MAX")
- [`CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX`](../../../../kconfig.md#CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX "CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX")

The [`CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX`](../../../../kconfig.md#CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX "CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX") option is also used by the BLOB Transfer
Client and affects memory consumption by the BLOB Transfer Client model structure.

To ensure that the transfer can be received by as many servers as possible, the BLOB Transfer Client
can retrieve the capabilities of each BLOB Transfer Server before starting the transfer. The client
will transfer the BLOB with the highest possible block and chunk size.

### Transfer modes

BLOBs can be transferred using two transfer modes, Push BLOB Transfer Mode and Pull BLOB Transfer
Mode. In most cases, the transfer should be conducted in Push BLOB Transfer Mode.

In Push BLOB Transfer Mode, the send rate is controlled by the BLOB Transfer Client, which will push
all the chunks of each block without any high level flow control. Push BLOB Transfer Mode supports
any number of Target nodes, and should be the default transfer mode.

In Pull BLOB Transfer Mode, the BLOB Transfer Server will “pull” the chunks from the BLOB Transfer
Client at its own rate. Pull BLOB Transfer Mode can be conducted with multiple Target nodes, and is
intended for transferring BLOBs to Target nodes acting as [Low Power Node](core.md#bluetooth-mesh-lpn). When operating
in Pull BLOB Transfer Mode, the BLOB Transfer Server will request chunks from the BLOB Transfer
Client in small batches, and wait for them all to arrive before requesting more chunks. This process
is repeated until the BLOB Transfer Server has received all chunks in a block. Then, the BLOB
Transfer Client starts the next block, and the BLOB Transfer Server requests all chunks of that
block.

### Transfer timeout

The timeout of the BLOB transfer is based on a Timeout Base value. Both client and server use the
same Timeout Base value, but they calculate timeout differently.

The BLOB Transfer Server uses the following formula to calculate the BLOB transfer timeout:

```text
10 * (Timeout Base + 1) seconds
```

For the BLOB Transfer Client, the following formula is used:

```text
(10000 * (Timeout Base + 2)) + (100 * TTL) milliseconds
```

where TTL is time to live value set in the transfer.

## API reference

This section contains types and defines common to the BLOB Transfer models.

*group* Bluetooth Mesh BLOB model API
:   Defines

    CONFIG\_BT\_MESH\_BLOB\_CHUNK\_COUNT\_MAX

    Enums

    enum bt\_mesh\_blob\_xfer\_mode
    :   BLOB transfer mode.

        *Values:*

        enumerator BT\_MESH\_BLOB\_XFER\_MODE\_NONE
        :   No valid transfer mode.

        enumerator BT\_MESH\_BLOB\_XFER\_MODE\_PUSH
        :   Push mode (Push BLOB Transfer Mode).

        enumerator BT\_MESH\_BLOB\_XFER\_MODE\_PULL
        :   Pull mode (Pull BLOB Transfer Mode).

        enumerator BT\_MESH\_BLOB\_XFER\_MODE\_ALL
        :   Both modes are valid.

    enum bt\_mesh\_blob\_xfer\_phase
    :   Transfer phase.

        *Values:*

        enumerator BT\_MESH\_BLOB\_XFER\_PHASE\_INACTIVE
        :   The BLOB Transfer Server is awaiting configuration.

        enumerator BT\_MESH\_BLOB\_XFER\_PHASE\_WAITING\_FOR\_START
        :   The BLOB Transfer Server is ready to receive a BLOB transfer.

        enumerator BT\_MESH\_BLOB\_XFER\_PHASE\_WAITING\_FOR\_BLOCK
        :   The BLOB Transfer Server is waiting for the next block of data.

        enumerator BT\_MESH\_BLOB\_XFER\_PHASE\_WAITING\_FOR\_CHUNK
        :   The BLOB Transfer Server is waiting for the next chunk of data.

        enumerator BT\_MESH\_BLOB\_XFER\_PHASE\_COMPLETE
        :   The BLOB was transferred successfully.

        enumerator BT\_MESH\_BLOB\_XFER\_PHASE\_SUSPENDED
        :   The BLOB transfer is paused.

    enum bt\_mesh\_blob\_status
    :   BLOB model status codes.

        *Values:*

        enumerator BT\_MESH\_BLOB\_SUCCESS
        :   The message was processed successfully.

        enumerator BT\_MESH\_BLOB\_ERR\_INVALID\_BLOCK\_NUM
        :   The Block Number field value is not within the range of blocks being transferred.

        enumerator BT\_MESH\_BLOB\_ERR\_INVALID\_BLOCK\_SIZE
        :   The block size is smaller than the size indicated by the Min Block Size Log state or is larger than the size indicated by the Max Block Size Log state.

        enumerator BT\_MESH\_BLOB\_ERR\_INVALID\_CHUNK\_SIZE
        :   The chunk size exceeds the size indicated by the Max Chunk Size state, or the number of chunks exceeds the number specified by the Max Total Chunks state.

        enumerator BT\_MESH\_BLOB\_ERR\_WRONG\_PHASE
        :   The operation cannot be performed while the server is in the current phase.

        enumerator BT\_MESH\_BLOB\_ERR\_INVALID\_PARAM
        :   A parameter value in the message cannot be accepted.

        enumerator BT\_MESH\_BLOB\_ERR\_WRONG\_BLOB\_ID
        :   The message contains a BLOB ID value that is not expected.

        enumerator BT\_MESH\_BLOB\_ERR\_BLOB\_TOO\_LARGE
        :   There is not enough space available in memory to receive the BLOB.

        enumerator BT\_MESH\_BLOB\_ERR\_UNSUPPORTED\_MODE
        :   The transfer mode is not supported by the BLOB Transfer Server model.

        enumerator BT\_MESH\_BLOB\_ERR\_INTERNAL
        :   An internal error occurred on the node.

        enumerator BT\_MESH\_BLOB\_ERR\_INFO\_UNAVAILABLE
        :   The requested information cannot be provided while the server is in the current phase.

    enum bt\_mesh\_blob\_io\_mode
    :   BLOB stream interaction mode.

        *Values:*

        enumerator BT\_MESH\_BLOB\_READ
        :   Read data from the stream.

        enumerator BT\_MESH\_BLOB\_WRITE
        :   Write data to the stream.

    struct bt\_mesh\_blob\_block
    :   *#include <blob.h>*

        BLOB transfer data block.

        Public Members

        size\_t size
        :   Block size in bytes.

        off\_t offset
        :   Offset in bytes from the start of the BLOB.

        uint16\_t number
        :   Block number.

        uint16\_t chunk\_count
        :   Number of chunks in block.

        uint8\_t missing[[DIV\_ROUND\_UP](../../../../kernel/util/index.md#c.DIV_ROUND_UP "DIV_ROUND_UP")(0, 8)]
        :   Bitmap of missing chunks.

    struct bt\_mesh\_blob\_chunk
    :   *#include <blob.h>*

        BLOB data chunk.

        Public Members

        off\_t offset
        :   Offset of the chunk data from the start of the block.

        size\_t size
        :   Chunk data size.

        uint8\_t \*data
        :   Chunk data.

    struct bt\_mesh\_blob\_xfer
    :   *#include <blob.h>*

        BLOB transfer.

        Public Members

        uint64\_t id
        :   BLOB ID.

        size\_t size
        :   Total BLOB size in bytes.

        enum [bt\_mesh\_blob\_xfer\_mode](#c.bt_mesh_blob_xfer_mode) mode
        :   BLOB transfer mode.

        uint16\_t chunk\_size
        :   Base chunk size.

            May be smaller for the last chunk.

    struct bt\_mesh\_blob\_io
    :   *#include <blob.h>*

        BLOB stream.

        Public Members

        int (\*open)(const struct [bt\_mesh\_blob\_io](#c.bt_mesh_blob_io) \*io, const struct [bt\_mesh\_blob\_xfer](#c.bt_mesh_blob_xfer) \*xfer, enum [bt\_mesh\_blob\_io\_mode](#c.bt_mesh_blob_io_mode) mode)
        :   Open callback.

            Called when the reader is opened for reading.

            Param io:
            :   BLOB stream.

            Param xfer:
            :   BLOB transfer.

            Param mode:
            :   Direction of the stream (read/write).

            Return:
            :   0 on success, or (negative) error code otherwise.

        void (\*close)(const struct [bt\_mesh\_blob\_io](#c.bt_mesh_blob_io) \*io, const struct [bt\_mesh\_blob\_xfer](#c.bt_mesh_blob_xfer) \*xfer)
        :   Close callback.

            Called when the reader is closed.

            Param io:
            :   BLOB stream.

            Param xfer:
            :   BLOB transfer.

        int (\*block\_start)(const struct [bt\_mesh\_blob\_io](#c.bt_mesh_blob_io) \*io, const struct [bt\_mesh\_blob\_xfer](#c.bt_mesh_blob_xfer) \*xfer, const struct [bt\_mesh\_blob\_block](#c.bt_mesh_blob_block) \*block)
        :   Block start callback.

            Called when a new block is opened for sending. Each block is only sent once, and are always sent in increasing order. The data chunks inside a single block may be requested out of order and multiple times.

            Param io:
            :   BLOB stream.

            Param xfer:
            :   BLOB transfer.

            Param block:
            :   Block that was started.

        void (\*block\_end)(const struct [bt\_mesh\_blob\_io](#c.bt_mesh_blob_io) \*io, const struct [bt\_mesh\_blob\_xfer](#c.bt_mesh_blob_xfer) \*xfer, const struct [bt\_mesh\_blob\_block](#c.bt_mesh_blob_block) \*block)
        :   Block end callback.

            Called when the current block has been transmitted in full. No data from this block will be requested again, and the application data associated with this block may be discarded.

            Param io:
            :   BLOB stream.

            Param xfer:
            :   BLOB transfer.

            Param block:
            :   Block that finished sending.

        int (\*wr)(const struct [bt\_mesh\_blob\_io](#c.bt_mesh_blob_io) \*io, const struct [bt\_mesh\_blob\_xfer](#c.bt_mesh_blob_xfer) \*xfer, const struct [bt\_mesh\_blob\_block](#c.bt_mesh_blob_block) \*block, const struct [bt\_mesh\_blob\_chunk](#c.bt_mesh_blob_chunk) \*chunk)
        :   Chunk data write callback.

            Used by the BLOB Transfer Server on incoming data.

            Each block is divided into chunks of data. This callback is called when a new chunk of data is received. Chunks may be received in any order within their block.

            If the callback returns successfully, this chunk will be marked as received, and will not be received again unless the block is restarted due to a transfer suspension. If the callback returns a non-zero value, the chunk remains unreceived, and the BLOB Transfer Client will attempt to resend it later.

            Note that the Client will only perform a limited number of attempts at delivering a chunk before dropping a Target node from the transfer. The number of retries performed by the Client is implementation specific.

            Param io:
            :   BLOB stream.

            Param xfer:
            :   BLOB transfer.

            Param block:
            :   Block the chunk is part of.

            Param chunk:
            :   Received chunk.

            Return:
            :   0 on success, or (negative) error code otherwise.

        int (\*rd)(const struct [bt\_mesh\_blob\_io](#c.bt_mesh_blob_io) \*io, const struct [bt\_mesh\_blob\_xfer](#c.bt_mesh_blob_xfer) \*xfer, const struct [bt\_mesh\_blob\_block](#c.bt_mesh_blob_block) \*block, const struct [bt\_mesh\_blob\_chunk](#c.bt_mesh_blob_chunk) \*chunk)
        :   Chunk data read callback.

            Used by the BLOB Transfer Client to fetch outgoing data.

            The Client calls the chunk data request callback to populate a chunk message going out to the Target nodes. The data request callback may be called out of order and multiple times for each offset, and cannot be used as an indication of progress.

            Returning a non-zero status code on the chunk data request callback results in termination of the transfer.

            Param io:
            :   BLOB stream.

            Param xfer:
            :   BLOB transfer.

            Param block:
            :   Block the chunk is part of.

            Param chunk:
            :   Chunk to get the data of. The buffer pointer to by the `data` member should be filled by the callback.

            Return:
            :   0 on success, or (negative) error code otherwise.
