---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/mesh/dfu_cli.html
original_path: connectivity/bluetooth/api/mesh/dfu_cli.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Firmware Update Client

The Firmware Update Client is responsible for distributing firmware updates through the mesh
network. The Firmware Update Client uses the [BLOB Transfer Client](blob_cli.md#bluetooth-mesh-blob-cli) as a transport for its
transfers.

## API reference

*group* bt\_mesh\_dfu\_cli
:   API for the Bluetooth Mesh Firmware Update Client model.

    Defines

    BT\_MESH\_DFU\_CLI\_INIT(\_handlers)
    :   Initialization parameters for the [Firmware Uppdate Client model](#group__bt__mesh__dfu__cli).

        See also

        [bt\_mesh\_dfu\_cli\_cb](#structbt__mesh__dfu__cli__cb).

        Parameters:
        :   - **\_handlers** – Handler callback structure.

    BT\_MESH\_MODEL\_DFU\_CLI(\_cli)
    :   Firmware Update Client model Composition Data entry.

        Parameters:
        :   - **\_cli** – Pointer to a [Firmware Uppdate Client model](#group__bt__mesh__dfu__cli) instance.

    Typedefs

    typedef enum [bt\_mesh\_dfu\_iter](dfu.md#c.bt_mesh_dfu_iter "bt_mesh_dfu_iter") (\*bt\_mesh\_dfu\_img\_cb\_t)(struct [bt\_mesh\_dfu\_cli](#c.bt_mesh_dfu_cli) \*cli, struct [bt\_mesh\_msg\_ctx](msg.md#c.bt_mesh_msg_ctx "bt_mesh_msg_ctx") \*ctx, uint8\_t idx, uint8\_t total, const struct [bt\_mesh\_dfu\_img](dfu.md#c.bt_mesh_dfu_img "bt_mesh_dfu_img") \*img, void \*cb\_data)
    :   DFU image callback.

        The image callback is called for every DFU image on the Target node when calling [bt\_mesh\_dfu\_cli\_imgs\_get](#group__bt__mesh__dfu__cli_1ga4c33f9457d4f367760a51a771dfd2671).

        Param cli:
        :   Firmware Update Client model instance.

        Param ctx:
        :   Message context of the received message.

        Param idx:
        :   Image index.

        Param total:
        :   Total number of images on the Target node.

        Param img:
        :   Image information for the given image index.

        Param cb\_data:
        :   Callback data.

        Retval BT\_MESH\_DFU\_ITER\_STOP:
        :   Stop iterating through the image list and return from [bt\_mesh\_dfu\_cli\_imgs\_get](#group__bt__mesh__dfu__cli_1ga4c33f9457d4f367760a51a771dfd2671).

        Retval BT\_MESH\_DFU\_ITER\_CONTINUE:
        :   Continue iterating through the image list if any images remain.

    Functions

    int bt\_mesh\_dfu\_cli\_send(struct [bt\_mesh\_dfu\_cli](#c.bt_mesh_dfu_cli) \*cli, const struct [bt\_mesh\_blob\_cli\_inputs](blob_cli.md#c.bt_mesh_blob_cli_inputs "bt_mesh_blob_cli_inputs") \*inputs, const struct [bt\_mesh\_blob\_io](blob.md#c.bt_mesh_blob_io "bt_mesh_blob_io") \*io, const struct [bt\_mesh\_dfu\_cli\_xfer](#c.bt_mesh_dfu_cli_xfer) \*xfer)
    :   Start distributing a DFU.

        Starts distribution of the firmware in the given slot to the list of DFU Target nodes in `ctx`. The transfer runs in the background, and its end is signalled through the [bt\_mesh\_dfu\_cli\_cb::ended](#structbt__mesh__dfu__cli__cb_1aa3c8985490a6b2bd6fcd81dff0132060) callback.

        Note

        The BLOB Transfer Client transfer inputs `targets` list must point to a list of [bt\_mesh\_dfu\_target](#structbt__mesh__dfu__target) nodes.

        Parameters:
        :   - **cli** – Firmware Update Client model instance.
            - **inputs** – BLOB Transfer Client transfer inputs.
            - **io** – BLOB stream to read BLOB from.
            - **xfer** – Firmware Update Client transfer parameters.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int bt\_mesh\_dfu\_cli\_suspend(struct [bt\_mesh\_dfu\_cli](#c.bt_mesh_dfu_cli) \*cli)
    :   Suspend a DFU transfer.

        Parameters:
        :   - **cli** – Firmware Update Client instance.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int bt\_mesh\_dfu\_cli\_resume(struct [bt\_mesh\_dfu\_cli](#c.bt_mesh_dfu_cli) \*cli)
    :   Resume the suspended transfer.

        Parameters:
        :   - **cli** – Firmware Update Client instance.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int bt\_mesh\_dfu\_cli\_cancel(struct [bt\_mesh\_dfu\_cli](#c.bt_mesh_dfu_cli) \*cli, struct [bt\_mesh\_msg\_ctx](msg.md#c.bt_mesh_msg_ctx "bt_mesh_msg_ctx") \*ctx)
    :   Cancel a DFU transfer.

        Will cancel the ongoing DFU transfer, or the transfer on a specific Target node if `ctx` is valid.

        Parameters:
        :   - **cli** – Firmware Update Client model instance.
            - **ctx** – Message context, or NULL to cancel the ongoing DFU transfer.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int bt\_mesh\_dfu\_cli\_apply(struct [bt\_mesh\_dfu\_cli](#c.bt_mesh_dfu_cli) \*cli)
    :   Apply the completed DFU transfer.

        A transfer can only be applied after it has ended successfully. The Firmware Update Client’s `applied` callback is called at the end of the apply procedure.

        Parameters:
        :   - **cli** – Firmware Update Client model instance.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int bt\_mesh\_dfu\_cli\_confirm(struct [bt\_mesh\_dfu\_cli](#c.bt_mesh_dfu_cli) \*cli)
    :   Confirm that the active transfer has been applied on the Target nodes.

        A transfer can only be confirmed after it has been applied. The Firmware Update Client’s `confirmed` callback is called at the end of the confirm procedure.

        Target nodes that have reported the effect as [BT\_MESH\_DFU\_EFFECT\_UNPROV](dfu.md#group__bt__mesh__dfu_1ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a11e843036db6bcae565c07ace00c9211) are expected to not respond to the query, and will fail if they do.

        Parameters:
        :   - **cli** – Firmware Update Client model instance.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    uint8\_t bt\_mesh\_dfu\_cli\_progress(struct [bt\_mesh\_dfu\_cli](#c.bt_mesh_dfu_cli) \*cli)
    :   Get progress as a percentage of completion.

        Parameters:
        :   - **cli** – Firmware Update Client model instance.

        Returns:
        :   The progress of the current transfer in percent, or 0 if no transfer is active.

    bool bt\_mesh\_dfu\_cli\_is\_busy(struct [bt\_mesh\_dfu\_cli](#c.bt_mesh_dfu_cli) \*cli)
    :   Check whether a DFU transfer is in progress.

        Parameters:
        :   - **cli** – Firmware Update Client model instance.

        Returns:
        :   true if the BLOB Transfer Client is currently participating in a transfer, false otherwise.

    int bt\_mesh\_dfu\_cli\_imgs\_get(struct [bt\_mesh\_dfu\_cli](#c.bt_mesh_dfu_cli) \*cli, struct [bt\_mesh\_msg\_ctx](msg.md#c.bt_mesh_msg_ctx "bt_mesh_msg_ctx") \*ctx, [bt\_mesh\_dfu\_img\_cb\_t](#c.bt_mesh_dfu_img_cb_t) cb, void \*cb\_data, uint8\_t max\_count)
    :   Perform a DFU image list request.

        Requests the full list of DFU images on a Target node, and iterates through them, calling the `cb` for every image.

        The DFU image list request can be used to determine which image index the Target node holds its different firmwares in.

        Waits for a response until the procedure timeout expires.

        Parameters:
        :   - **cli** – Firmware Update Client model instance.
            - **ctx** – Message context.
            - **cb** – Callback to call for each image index.
            - **cb\_data** – Callback data to pass to `cb`.
            - **max\_count** – Max number of images to return.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int bt\_mesh\_dfu\_cli\_metadata\_check(struct [bt\_mesh\_dfu\_cli](#c.bt_mesh_dfu_cli) \*cli, struct [bt\_mesh\_msg\_ctx](msg.md#c.bt_mesh_msg_ctx "bt_mesh_msg_ctx") \*ctx, uint8\_t img\_idx, const struct [bt\_mesh\_dfu\_slot](dfu.md#c.bt_mesh_dfu_slot "bt_mesh_dfu_slot") \*slot, struct [bt\_mesh\_dfu\_metadata\_status](#c.bt_mesh_dfu_metadata_status) \*rsp)
    :   Perform a metadata check for the given DFU image slot.

        The metadata check procedure allows the Firmware Update Client to check if a Target node will accept a transfer of this DFU image slot, and what the effect would be.

        Waits for a response until the procedure timeout expires.

        Parameters:
        :   - **cli** – Firmware Update Client model instance.
            - **ctx** – Message context.
            - **img\_idx** – Target node’s image index to check.
            - **slot** – DFU image slot to check for.
            - **rsp** – Metadata status response buffer.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int bt\_mesh\_dfu\_cli\_status\_get(struct [bt\_mesh\_dfu\_cli](#c.bt_mesh_dfu_cli) \*cli, struct [bt\_mesh\_msg\_ctx](msg.md#c.bt_mesh_msg_ctx "bt_mesh_msg_ctx") \*ctx, struct [bt\_mesh\_dfu\_target\_status](#c.bt_mesh_dfu_target_status) \*rsp)
    :   Get the status of a Target node.

        Parameters:
        :   - **cli** – Firmware Update Client model instance.
            - **ctx** – Message context.
            - **rsp** – Response data buffer.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int32\_t bt\_mesh\_dfu\_cli\_timeout\_get(void)
    :   Get the current procedure timeout value.

        Returns:
        :   The configured procedure timeout.

    void bt\_mesh\_dfu\_cli\_timeout\_set(int32\_t timeout)
    :   Set the procedure timeout value.

        Parameters:
        :   - **timeout** – The new procedure timeout.

    struct bt\_mesh\_dfu\_target
    :   *#include <dfu\_cli.h>*

        DFU Target node.

        Public Members

        struct [bt\_mesh\_blob\_target](blob_cli.md#c.bt_mesh_blob_target "bt_mesh_blob_target") blob
        :   BLOB Target node.

        uint8\_t img\_idx
        :   Image index on the Target node.

        uint8\_t effect
        :   Expected DFU effect, see [bt\_mesh\_dfu\_effect](dfu.md#group__bt__mesh__dfu_1gae7d7ef4ed1e65e5f8e1641a9c00bb7e8).

        uint8\_t status
        :   Current DFU status, see [bt\_mesh\_dfu\_status](dfu.md#group__bt__mesh__dfu_1ga9e627a3c15de782faa11ef6c4ec5e05d).

        uint8\_t phase
        :   Current DFU phase, see [bt\_mesh\_dfu\_phase](dfu.md#group__bt__mesh__dfu_1ga99919dcee1e41bc74bd59e33bec2ded2).

    struct bt\_mesh\_dfu\_metadata\_status
    :   *#include <dfu\_cli.h>*

        Metadata status response.

        Public Members

        uint8\_t idx
        :   Image index.

        enum [bt\_mesh\_dfu\_status](dfu.md#c.bt_mesh_dfu_status "bt_mesh_dfu_status") status
        :   Status code.

        enum [bt\_mesh\_dfu\_effect](dfu.md#c.bt_mesh_dfu_effect "bt_mesh_dfu_effect") effect
        :   Effect of transfer.

    struct bt\_mesh\_dfu\_target\_status
    :   *#include <dfu\_cli.h>*

        DFU Target node status parameters.

        Public Members

        enum [bt\_mesh\_dfu\_status](dfu.md#c.bt_mesh_dfu_status "bt_mesh_dfu_status") status
        :   Status of the previous operation.

        enum [bt\_mesh\_dfu\_phase](dfu.md#c.bt_mesh_dfu_phase "bt_mesh_dfu_phase") phase
        :   Phase of the current DFU transfer.

        enum [bt\_mesh\_dfu\_effect](dfu.md#c.bt_mesh_dfu_effect "bt_mesh_dfu_effect") effect
        :   The effect the update will have on the Target device’s state.

        uint64\_t blob\_id
        :   BLOB ID used in the transfer.

        uint8\_t img\_idx
        :   Image index to transfer.

        uint8\_t ttl
        :   TTL used in the transfer.

        uint16\_t timeout\_base
        :   Additional response time for the Target nodes, in 10-second increments.

            The extra time can be used to give the Target nodes more time to respond to messages from the Client. The actual timeout will be calculated according to the following formula:

            ```text
            *  timeout = 20 seconds + (10 seconds * timeout_base) + (100 ms * TTL)
            *
            ```

            If a Target node fails to respond to a message from the Client within the configured transfer timeout, the Target node is dropped.

    struct bt\_mesh\_dfu\_cli\_cb
    :   *#include <dfu\_cli.h>*

        Firmware Update Client event callbacks.

        Public Members

        void (\*suspended)(struct [bt\_mesh\_dfu\_cli](#c.bt_mesh_dfu_cli) \*cli)
        :   BLOB transfer is suspended.

            Called when the BLOB transfer is suspended due to response timeout from all Target nodes.

            Param cli:
            :   Firmware Update Client model instance.

        void (\*ended)(struct [bt\_mesh\_dfu\_cli](#c.bt_mesh_dfu_cli) \*cli, enum [bt\_mesh\_dfu\_status](dfu.md#c.bt_mesh_dfu_status "bt_mesh_dfu_status") reason)
        :   DFU ended.

            Called when the DFU transfer ends, either because all Target nodes were lost or because the transfer was completed successfully.

            Param cli:
            :   Firmware Update Client model instance.

            Param reason:
            :   Reason for ending.

        void (\*applied)(struct [bt\_mesh\_dfu\_cli](#c.bt_mesh_dfu_cli) \*cli)
        :   DFU transfer applied on all active Target nodes.

            Called at the end of the apply procedure started by [bt\_mesh\_dfu\_cli\_apply](#group__bt__mesh__dfu__cli_1ga2904ba992a00ee9fba6704c1efc8f074).

            Param cli:
            :   Firmware Update Client model instance.

        void (\*confirmed)(struct [bt\_mesh\_dfu\_cli](#c.bt_mesh_dfu_cli) \*cli)
        :   DFU transfer confirmed on all active Target nodes.

            Called at the end of the apply procedure started by [bt\_mesh\_dfu\_cli\_confirm](#group__bt__mesh__dfu__cli_1gaf76f0cdb5c6b0df12ddb495c718c3c93).

            Param cli:
            :   Firmware Update Client model instance.

        void (\*lost\_target)(struct [bt\_mesh\_dfu\_cli](#c.bt_mesh_dfu_cli) \*cli, struct [bt\_mesh\_dfu\_target](#c.bt_mesh_dfu_target) \*target)
        :   DFU Target node was lost.

            A DFU Target node was dropped from the receivers list. The Target node’s `status` is set to reflect the reason for the failure.

            Param cli:
            :   Firmware Update Client model instance.

            Param target:
            :   DFU Target node that was lost.

    struct bt\_mesh\_dfu\_cli
    :   *#include <dfu\_cli.h>*

        Firmware Update Client model instance.

        Should be initialized with [BT\_MESH\_DFU\_CLI\_INIT](#group__bt__mesh__dfu__cli_1ga0b10a95f9b7c806bfd8649280f535c96).

        Public Members

        const struct [bt\_mesh\_dfu\_cli\_cb](#c.bt_mesh_dfu_cli_cb) \*cb
        :   Callback structure.

        struct [bt\_mesh\_blob\_cli](blob_cli.md#c.bt_mesh_blob_cli "bt_mesh_blob_cli") blob
        :   Underlying BLOB Transfer Client.

    struct bt\_mesh\_dfu\_cli\_xfer\_blob\_params
    :   *#include <dfu\_cli.h>*

        BLOB parameters for Firmware Update Client transfer:

        Public Members

        uint16\_t chunk\_size
        :   Base chunk size.

            May be smaller for the last chunk.

    struct bt\_mesh\_dfu\_cli\_xfer
    :   *#include <dfu\_cli.h>*

        Firmware Update Client transfer parameters:

        Public Members

        uint64\_t blob\_id
        :   BLOB ID to use for this transfer, or 0 to set it randomly.

        const struct [bt\_mesh\_dfu\_slot](dfu.md#c.bt_mesh_dfu_slot "bt_mesh_dfu_slot") \*slot
        :   DFU image slot to transfer.

        enum [bt\_mesh\_blob\_xfer\_mode](blob.md#c.bt_mesh_blob_xfer_mode "bt_mesh_blob_xfer_mode") mode
        :   Transfer mode (Push (Push BLOB Transfer Mode) or Pull (Pull BLOB Transfer Mode)).

        const struct [bt\_mesh\_dfu\_cli\_xfer\_blob\_params](#c.bt_mesh_dfu_cli_xfer_blob_params) \*blob\_params
        :   BLOB parameters to be used for the transfer, or NULL to retrieve Target nodes’ capabilities before sending a firmware.
