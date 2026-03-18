---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/api/mesh/blob_srv.html
original_path: connectivity/bluetooth/api/mesh/blob_srv.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# BLOB Transfer Server

The Binary Large Object (BLOB) Transfer Server model implements reliable receiving of large binary
objects. It serves as the backend of the [Firmware Update Server](dfu_srv.md#bluetooth-mesh-dfu-srv), but can also be used for
receiving other binary images.

## BLOBs

As described in [BLOB Transfer models](blob.md#bluetooth-mesh-blob), the binary objects transferred by the BLOB Transfer
models are divided into blocks, which are divided into chunks. As the transfer is controlled by the
BLOB Transfer Client model, the BLOB Transfer Server must allow blocks to come in any order. The
chunks within a block may also come in any order, but all chunks in a block must be received before
the next block is started.

The BLOB Transfer Server keeps track of the received blocks and chunks, and will process each block
and chunk only once. The BLOB Transfer Server also ensures that any missing chunks are resent by the
BLOB Transfer Client.

## Usage

The BLOB Transfer Server is instantiated on an element with a set of event handler callbacks:

```c
static const struct bt_mesh_blob_srv_cb blob_cb = {
    /* Callbacks */
};

static struct bt_mesh_blob_srv blob_srv = {
    .cb = &blob_cb,
};

static const struct bt_mesh_model models[] = {
    BT_MESH_MODEL_BLOB_SRV(&blob_srv),
};
```

A BLOB Transfer Server is capable of receiving a single BLOB transfer at a time. Before the BLOB
Transfer Server can receive a transfer, it must be prepared by the user. The transfer ID must be
passed to the BLOB Transfer Server through the [`bt_mesh_blob_srv_recv()`](#c.bt_mesh_blob_srv_recv) function before the
transfer is started by the BLOB Transfer Client. The ID must be shared between the BLOB Transfer
Client and the BLOB Transfer Server through some higher level procedure, like a vendor specific
transfer management model.

Once the transfer has been set up on the BLOB Transfer Server, it’s ready for receiving the BLOB.
The application is notified of the transfer progress through the event handler callbacks, and the
BLOB data is sent to the BLOB stream.

The interaction between the BLOB Transfer Server, BLOB stream and application is shown below:

![BLOB Transfer Server model interaction](../../../../_images/blob_srv.svg)

BLOB Transfer Server model interaction

## Transfer suspension

The BLOB Transfer Server keeps a running timer during the transfer, that is reset on every received
message. If the BLOB Transfer Client does not send a message before the transfer timer expires, the
transfer is suspended by the BLOB Transfer Server.

The BLOB Transfer Server notifies the user of the suspension by calling the [`suspended`](#c.bt_mesh_blob_srv_cb.suspended) callback. If the BLOB Transfer Server is in the middle of receiving
a block, this block is discarded.

The BLOB Transfer Client may resume a suspended transfer by starting a new block transfer. The BLOB
Transfer Server notifies the user by calling the [`resume`](#c.bt_mesh_blob_srv_cb.resume)
callback.

## Transfer recovery

The state of the BLOB transfer is stored persistently. If a reboot occurs, the BLOB Transfer Server
will attempt to recover the transfer. When the Bluetooth Mesh subsystem is started (for instance by
calling [`bt_mesh_init()`](core.md#c.bt_mesh_init "bt_mesh_init")), the BLOB Transfer Server will check for aborted transfers, and call
the [`recover`](#c.bt_mesh_blob_srv_cb.recover) callback if there is any. In the recover
callback, the user must provide a BLOB stream to use for the rest of the transfer. If the recover
callback doesn’t return successfully or does not provide a BLOB stream, the transfer is abandoned.
If no recover callback is implemented, transfers are always abandoned after a reboot.

After a transfer is successfully recovered, the BLOB Transfer Server enters the suspended state. It
will stay suspended until the BLOB Transfer Client resumes the transfer, or the user cancels it.

Note

The BLOB Transfer Client sending the transfer must support transfer recovery for the transfer to
complete. If the BLOB Transfer Client has already given up the transfer, the BLOB Transfer Server
will stay suspended until the application calls [`bt_mesh_blob_srv_cancel()`](#c.bt_mesh_blob_srv_cancel).

## API reference

*group* Bluetooth Mesh BLOB Transfer Server model API
:   Defines

    BT\_MESH\_BLOB\_BLOCKS\_MAX
    :   Max number of blocks in a single transfer.

    BT\_MESH\_MODEL\_BLOB\_SRV(\_srv)
    :   BLOB Transfer Server model composition data entry.

        Parameters:
        :   - **\_srv** – Pointer to a [Bluetooth Mesh BLOB Transfer Server model API](#group__bt__mesh__blob__srv) instance.

    Functions

    int bt\_mesh\_blob\_srv\_recv(struct [bt\_mesh\_blob\_srv](#c.bt_mesh_blob_srv) \*srv, uint64\_t id, const struct [bt\_mesh\_blob\_io](blob.md#c.bt_mesh_blob_io "bt_mesh_blob_io") \*io, uint8\_t ttl, uint16\_t timeout\_base)
    :   Prepare BLOB Transfer Server for an incoming transfer.

        Before a BLOB Transfer Server can receive a transfer, the transfer must be prepared through some application level mechanism. The BLOB Transfer Server will only accept incoming transfers with a matching BLOB ID.

        Parameters:
        :   - **srv** – BLOB Transfer Server instance.
            - **id** – BLOB ID to accept.
            - **io** – BLOB stream to write the incoming BLOB to.
            - **ttl** – Time to live value to use in responses to the BLOB Transfer Client.
            - **timeout\_base** – Extra time for the Client to respond in addition to the base 10 seconds, in 10-second increments.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_blob\_srv\_cancel(struct [bt\_mesh\_blob\_srv](#c.bt_mesh_blob_srv) \*srv)
    :   Cancel the current BLOB transfer.

        Tells the BLOB Transfer Client to drop this device from the list of Targets for the current transfer. Note that the client may continue sending the transfer to other Targets.

        Parameters:
        :   - **srv** – BLOB Transfer Server instance.

        Returns:
        :   0 on success, or (negative) error code on failure.

    bool bt\_mesh\_blob\_srv\_is\_busy(const struct [bt\_mesh\_blob\_srv](#c.bt_mesh_blob_srv) \*srv)
    :   Get the current state of the BLOB Transfer Server.

        Parameters:
        :   - **srv** – BLOB Transfer Server instance.

        Returns:
        :   true if the BLOB Transfer Server is currently participating in a transfer, false otherwise.

    uint8\_t bt\_mesh\_blob\_srv\_progress(const struct [bt\_mesh\_blob\_srv](#c.bt_mesh_blob_srv) \*srv)
    :   Get the current progress of the active transfer in percent.

        Parameters:
        :   - **srv** – BLOB Transfer Server instance.

        Returns:
        :   The current transfer progress, or 0 if no transfer is active.

    struct bt\_mesh\_blob\_srv\_cb
    :   *#include <blob\_srv.h>*

        BLOB Transfer Server model event handlers.

        All callbacks are optional.

        Public Members

        int (\*start)(struct [bt\_mesh\_blob\_srv](#c.bt_mesh_blob_srv) \*srv, struct [bt\_mesh\_msg\_ctx](msg.md#c.bt_mesh_msg_ctx "bt_mesh_msg_ctx") \*ctx, struct [bt\_mesh\_blob\_xfer](blob.md#c.bt_mesh_blob_xfer "bt_mesh_blob_xfer") \*xfer)
        :   Transfer start callback.

            Called when the transfer has started with the prepared BLOB ID.

            Param srv:
            :   BLOB Transfer Server instance.

            Param ctx:
            :   Message context for the incoming start message. The entire transfer will be sent from the same source address.

            Param xfer:
            :   Transfer parameters.

            Return:
            :   0 on success, or (negative) error code to reject the transfer.

        void (\*end)(struct [bt\_mesh\_blob\_srv](#c.bt_mesh_blob_srv) \*srv, uint64\_t id, bool success)
        :   Transfer end callback.

            Called when the transfer ends, either because it was cancelled, or because it finished successfully. A new transfer may be prepared.

            Note

            The transfer may end before it’s started if the start parameters are invalid.

            Param srv:
            :   BLOB Transfer Server instance.

            Param id:
            :   BLOB ID of the cancelled transfer.

            Param success:
            :   Whether the transfer was successful.

        void (\*suspended)(struct [bt\_mesh\_blob\_srv](#c.bt_mesh_blob_srv) \*srv)
        :   Transfer suspended callback.

            Called if the Server timed out while waiting for a transfer packet. A suspended transfer may resume later from the start of the current block. Any received chunks in the current block should be discarded, they will be received again if the transfer resumes.

            The transfer will call `resumed` again when resuming.

            Note

            The BLOB Transfer Server does not run a timer in the suspended state, and it’s up to the application to determine whether the transfer should be permanently cancelled. Without interaction, the transfer will be suspended indefinitely, and the BLOB Transfer Server will not accept any new transfers.

            Param srv:
            :   BLOB Transfer Server instance.

        void (\*resume)(struct [bt\_mesh\_blob\_srv](#c.bt_mesh_blob_srv) \*srv)
        :   Transfer resume callback.

            Called if the transfer is resumed after being suspended.

            Param srv:
            :   BLOB Transfer Server instance.

        int (\*recover)(struct [bt\_mesh\_blob\_srv](#c.bt_mesh_blob_srv) \*srv, struct [bt\_mesh\_blob\_xfer](blob.md#c.bt_mesh_blob_xfer "bt_mesh_blob_xfer") \*xfer, const struct [bt\_mesh\_blob\_io](blob.md#c.bt_mesh_blob_io "bt_mesh_blob_io") \*\*io)
        :   Transfer recovery callback.

            Called when the Bluetooth Mesh subsystem is started if the device is rebooted in the middle of a transfer.

            Transfers will not be resumed after a reboot if this callback is not defined.

            Param srv:
            :   BLOB Transfer Server instance.

            Param xfer:
            :   Transfer to resume.

            Param io:
            :   BLOB stream return parameter. Must be set to a valid BLOB stream by the callback.

            Return:
            :   0 on success, or (negative) error code to abandon the transfer.

    struct bt\_mesh\_blob\_srv
    :   *#include <blob\_srv.h>*

        BLOB Transfer Server instance.

        Public Members

        const struct [bt\_mesh\_blob\_srv\_cb](#c.bt_mesh_blob_srv_cb) \*cb
        :   Event handler callbacks.

        struct bt\_mesh\_blob\_srv\_state
        :   *#include <blob\_srv.h>*
