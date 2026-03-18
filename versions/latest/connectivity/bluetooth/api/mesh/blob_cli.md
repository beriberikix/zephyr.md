---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/mesh/blob_cli.html
original_path: connectivity/bluetooth/api/mesh/blob_cli.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# BLOB Transfer Client

The Binary Large Object (BLOB) Transfer Client is the sender of the BLOB transfer. It supports
sending BLOBs of any size to any number of Target nodes, in both Push BLOB Transfer Mode and Pull
BLOB Transfer Mode.

## Usage

### Initialization

The BLOB Transfer Client is instantiated on an element with a set of event handler callbacks:

```c
static const struct bt_mesh_blob_cli_cb blob_cb = {
      /* Callbacks */
};

static struct bt_mesh_blob_cli blob_cli = {
      .cb = &blob_cb,
};

static const struct bt_mesh_model models[] = {
      BT_MESH_MODEL_BLOB_CLI(&blob_cli),
};
```

### Transfer context

Both the transfer capabilities retrieval procedure and the BLOB transfer uses an instance of a
[`bt_mesh_blob_cli_inputs`](#c.bt_mesh_blob_cli_inputs) to determine how to perform the transfer. The BLOB Transfer Client
Inputs structure must at least be initialized with a list of targets, an application key and a time
to live (TTL) value before it is used in a procedure:

```c
static struct bt_mesh_blob_target targets[3] = {
        { .addr = 0x0001 },
        { .addr = 0x0002 },
        { .addr = 0x0003 },
};
static struct bt_mesh_blob_cli_inputs inputs = {
        .app_idx = MY_APP_IDX,
        .ttl = BT_MESH_TTL_DEFAULT,
};

sys_slist_init(&inputs.targets);
sys_slist_append(&inputs.targets, &targets[0].n);
sys_slist_append(&inputs.targets, &targets[1].n);
sys_slist_append(&inputs.targets, &targets[2].n);
```

Note that all BLOB Transfer Servers in the transfer must be bound to the chosen application key.

#### Group address

The application may additionally specify a group address in the context structure. If the group is
not [`BT_MESH_ADDR_UNASSIGNED`](access.md#c.BT_MESH_ADDR_UNASSIGNED "BT_MESH_ADDR_UNASSIGNED"), the messages in the transfer will be sent to the group
address, instead of being sent individually to each Target node. Mesh Manager must ensure that all
Target nodes having the BLOB Transfer Server model subscribe to this group address.

Using group addresses for transferring the BLOBs can generally increase the transfer speed, as the
BLOB Transfer Client sends each message to all Target nodes at the same time. However, sending
large, segmented messages to group addresses in Bluetooth Mesh is generally less reliable than
sending them to unicast addresses, as there is no transport layer acknowledgment mechanism for
groups. This can lead to longer recovery periods at the end of each block, and increases the risk of
losing Target nodes. Using group addresses for BLOB transfers will generally only pay off if the
list of Target nodes is extensive, and the effectiveness of each addressing strategy will vary
heavily between different deployments and the size of the chunks.

#### Transfer timeout

If a Target node fails to respond to an acknowledged message within the BLOB Transfer Client’s time
limit, the Target node is dropped from the transfer. The application can reduce the chances of this
by giving the BLOB Transfer Client extra time through the context structure. The extra time may be
set in 10-second increments, up to 182 hours, in addition to the base time of 20 seconds. The wait
time scales automatically with the transfer TTL.

Note that the BLOB Transfer Client only moves forward with the transfer in following cases:

- All Target nodes have responded.
- A node has been removed from the list of Target nodes.
- The BLOB Transfer Client times out.

Increasing the wait time will increase this delay.

### BLOB transfer capabilities retrieval

It is generally recommended to retrieve BLOB transfer capabilities before starting a transfer. The
procedure populates the transfer capabilities from all Target nodes with the most liberal set of
parameters that allows all Target nodes to participate in the transfer. Any Target nodes that fail
to respond, or respond with incompatible transfer parameters, will be dropped.

Target nodes are prioritized according to their order in the list of Target nodes. If a Target node
is found to be incompatible with any of the previous Target nodes, for instance by reporting a
non-overlapping block size range, it will be dropped. Lost Target nodes will be reported through the
[`lost_target`](#c.bt_mesh_blob_cli_cb.lost_target) callback.

The end of the procedure is signalled through the [`caps`](#c.bt_mesh_blob_cli_cb.caps)
callback, and the resulting capabilities can be used to determine the block and chunk sizes required
for the BLOB transfer.

### BLOB transfer

The BLOB transfer is started by calling [`bt_mesh_blob_cli_send()`](#c.bt_mesh_blob_cli_send) function, which (in addition
to the aforementioned transfer inputs) requires a set of transfer parameters and a BLOB stream
instance. The transfer parameters include the 64-bit BLOB ID, the BLOB size, the transfer mode, the
block size in logarithmic representation and the chunk size. The BLOB ID is application defined, but
must match the BLOB ID the BLOB Transfer Servers have been started with.

The transfer runs until it either completes successfully for at least one Target node, or it is
cancelled. The end of the transfer is communicated to the application through the [`end`](#c.bt_mesh_blob_cli_cb.end) callback. Lost Target nodes will be reported through the
[`lost_target`](#c.bt_mesh_blob_cli_cb.lost_target) callback.

## API reference

*group* bt\_mesh\_blob\_cli
:   Defines

    BT\_MESH\_MODEL\_BLOB\_CLI(\_cli)
    :   BLOB Transfer Client model Composition Data entry.

        Parameters:
        :   - **\_cli** – Pointer to a [Bluetooth Mesh BLOB Transfer Client model API](#group__bt__mesh__blob__cli) instance.

    Enums

    enum bt\_mesh\_blob\_cli\_state
    :   BLOB Transfer Client state.

        *Values:*

        enumerator BT\_MESH\_BLOB\_CLI\_STATE\_NONE
        :   No transfer is active.

        enumerator BT\_MESH\_BLOB\_CLI\_STATE\_CAPS\_GET
        :   Retrieving transfer capabilities.

        enumerator BT\_MESH\_BLOB\_CLI\_STATE\_START
        :   Sending transfer start.

        enumerator BT\_MESH\_BLOB\_CLI\_STATE\_BLOCK\_START
        :   Sending block start.

        enumerator BT\_MESH\_BLOB\_CLI\_STATE\_BLOCK\_SEND
        :   Sending block chunks.

        enumerator BT\_MESH\_BLOB\_CLI\_STATE\_BLOCK\_CHECK
        :   Checking block status.

        enumerator BT\_MESH\_BLOB\_CLI\_STATE\_XFER\_CHECK
        :   Checking transfer status.

        enumerator BT\_MESH\_BLOB\_CLI\_STATE\_CANCEL
        :   Cancelling transfer.

        enumerator BT\_MESH\_BLOB\_CLI\_STATE\_SUSPENDED
        :   Transfer is suspended.

        enumerator BT\_MESH\_BLOB\_CLI\_STATE\_XFER\_PROGRESS\_GET
        :   Checking transfer progress.

    Functions

    int bt\_mesh\_blob\_cli\_caps\_get(struct [bt\_mesh\_blob\_cli](#c.bt_mesh_blob_cli) \*cli, const struct [bt\_mesh\_blob\_cli\_inputs](#c.bt_mesh_blob_cli_inputs) \*inputs)
    :   Retrieve transfer capabilities for a list of Target nodes.

        Queries the availability and capabilities of all Target nodes, producing a cumulative set of transfer capabilities for the Target nodes, and returning it through the [bt\_mesh\_blob\_cli\_cb::caps](#structbt__mesh__blob__cli__cb_1a58e749cadeb464299495ee74456c592c) callback.

        Retrieving the capabilities may take several seconds, depending on the number of Target nodes and mesh network performance. The end of the procedure is indicated through the [bt\_mesh\_blob\_cli\_cb::caps](#structbt__mesh__blob__cli__cb_1a58e749cadeb464299495ee74456c592c) callback.

        This procedure is not required, but strongly recommended as a preparation for a transfer to maximize performance and the chances of success.

        Parameters:
        :   - **cli** – BLOB Transfer Client instance.
            - **inputs** – Statically allocated BLOB Transfer Client transfer inputs.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int bt\_mesh\_blob\_cli\_send(struct [bt\_mesh\_blob\_cli](#c.bt_mesh_blob_cli) \*cli, const struct [bt\_mesh\_blob\_cli\_inputs](#c.bt_mesh_blob_cli_inputs) \*inputs, const struct [bt\_mesh\_blob\_xfer](blob.md#c.bt_mesh_blob_xfer "bt_mesh_blob_xfer") \*xfer, const struct [bt\_mesh\_blob\_io](blob.md#c.bt_mesh_blob_io "bt_mesh_blob_io") \*io)
    :   Perform a BLOB transfer.

        Starts sending the transfer to the Target nodes. Only Target nodes with a `status` of [BT\_MESH\_BLOB\_SUCCESS](blob.md#group__bt__mesh__blob_1gga7b5e2895a6577103a8a680a94ee7776daac639c3c82cf48a394c13e3b057c9c0d) will be considered.

        The transfer will keep going either until all Target nodes have been dropped, or the full BLOB has been sent.

        The BLOB transfer may take several minutes, depending on the number of Target nodes, size of the BLOB and mesh network performance. The end of the transfer is indicated through the [bt\_mesh\_blob\_cli\_cb::end](#structbt__mesh__blob__cli__cb_1a60bc49eab376b055a8c21099f86fdde7) callback.

        A Client only supports one transfer at the time.

        Parameters:
        :   - **cli** – BLOB Transfer Client instance.
            - **inputs** – Statically allocated BLOB Transfer Client transfer inputs.
            - **xfer** – Statically allocated transfer parameters.
            - **io** – BLOB stream to read the transfer from.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int bt\_mesh\_blob\_cli\_suspend(struct [bt\_mesh\_blob\_cli](#c.bt_mesh_blob_cli) \*cli)
    :   Suspend the active transfer.

        Parameters:
        :   - **cli** – BLOB Transfer Client instance.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int bt\_mesh\_blob\_cli\_resume(struct [bt\_mesh\_blob\_cli](#c.bt_mesh_blob_cli) \*cli)
    :   Resume the suspended transfer.

        Parameters:
        :   - **cli** – BLOB Transfer Client instance.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    void bt\_mesh\_blob\_cli\_cancel(struct [bt\_mesh\_blob\_cli](#c.bt_mesh_blob_cli) \*cli)
    :   Cancel an ongoing transfer.

        Parameters:
        :   - **cli** – BLOB Transfer Client instance.

    int bt\_mesh\_blob\_cli\_xfer\_progress\_get(struct [bt\_mesh\_blob\_cli](#c.bt_mesh_blob_cli) \*cli, const struct [bt\_mesh\_blob\_cli\_inputs](#c.bt_mesh_blob_cli_inputs) \*inputs)
    :   Get the progress of BLOB transfer.

        This function can only be used if the BLOB Transfer Client is currently not performing a BLOB transfer. To get progress of the active BLOB transfer, use the [bt\_mesh\_blob\_cli\_xfer\_progress\_active\_get](#group__bt__mesh__blob__cli_1ga065196837cbf9d2626b5589ce2671441) function.

        Parameters:
        :   - **cli** – BLOB Transfer Client instance.
            - **inputs** – Statically allocated BLOB Transfer Client transfer inputs.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    uint8\_t bt\_mesh\_blob\_cli\_xfer\_progress\_active\_get(struct [bt\_mesh\_blob\_cli](#c.bt_mesh_blob_cli) \*cli)
    :   Get the current progress of the active transfer in percent.

        Parameters:
        :   - **cli** – BLOB Transfer Client instance.

        Returns:
        :   The current transfer progress, or 0 if no transfer is active.

    bool bt\_mesh\_blob\_cli\_is\_busy(struct [bt\_mesh\_blob\_cli](#c.bt_mesh_blob_cli) \*cli)
    :   Get the current state of the BLOB Transfer Client.

        Parameters:
        :   - **cli** – BLOB Transfer Client instance.

        Returns:
        :   true if the BLOB Transfer Client is currently participating in a transfer or retrieving the capabilities and false otherwise.

    struct bt\_mesh\_blob\_target\_pull
    :   *#include <blob\_cli.h>*

        Target node’s Pull mode (Pull BLOB Transfer Mode) context used while sending chunks to the Target node.

        Public Members

        int64\_t block\_report\_timestamp
        :   Timestamp when the Block Report Timeout Timer expires for this Target node.

        uint8\_t missing[[DIV\_ROUND\_UP](../../../../kernel/util/index.md#c.DIV_ROUND_UP "DIV_ROUND_UP")([CONFIG\_BT\_MESH\_BLOB\_CHUNK\_COUNT\_MAX](blob.md#c.CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX "CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX"), 8)]
        :   Missing chunks reported by this Target node.

    struct bt\_mesh\_blob\_target
    :   *#include <blob\_cli.h>*

        BLOB Transfer Client Target node.

        Public Members

        [sys\_snode\_t](../../../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") n
        :   Linked list node.

        uint16\_t addr
        :   Target node address.

        struct [bt\_mesh\_blob\_target\_pull](#c.bt_mesh_blob_target_pull) \*pull
        :   Target node’s Pull mode context.

            Needs to be initialized when sending a BLOB in Pull mode.

        uint8\_t status
        :   BLOB transfer status, see [bt\_mesh\_blob\_status](blob.md#group__bt__mesh__blob_1ga7b5e2895a6577103a8a680a94ee7776d).

    struct bt\_mesh\_blob\_xfer\_info
    :   *#include <blob\_cli.h>*

        BLOB transfer information.

        If `phase` is [BT\_MESH\_BLOB\_XFER\_PHASE\_INACTIVE](blob.md#group__bt__mesh__blob_1gga26ed2c64bae03758a8a53b28052d0f81a60d2a7f950f2763ecb38b0cd84ae9600), the fields below `phase` are not initialized. If `phase` is [BT\_MESH\_BLOB\_XFER\_PHASE\_WAITING\_FOR\_START](blob.md#group__bt__mesh__blob_1gga26ed2c64bae03758a8a53b28052d0f81a68f54acdddf2df36f31c8c7c4d7eb9b9), the fields below `id` are not initialized.

        Public Members

        enum [bt\_mesh\_blob\_status](blob.md#c.bt_mesh_blob_status "bt_mesh_blob_status") status
        :   BLOB transfer status.

        enum [bt\_mesh\_blob\_xfer\_mode](blob.md#c.bt_mesh_blob_xfer_mode "bt_mesh_blob_xfer_mode") mode
        :   BLOB transfer mode.

        enum [bt\_mesh\_blob\_xfer\_phase](blob.md#c.bt_mesh_blob_xfer_phase "bt_mesh_blob_xfer_phase") phase
        :   BLOB transfer phase.

        uint64\_t id
        :   BLOB ID.

        uint32\_t size
        :   BLOB size in octets.

        uint8\_t block\_size\_log
        :   Logarithmic representation of the block size.

        uint16\_t mtu\_size
        :   MTU size in octets.

        const uint8\_t \*missing\_blocks
        :   Bit field indicating blocks that were not received.

    struct bt\_mesh\_blob\_cli\_inputs
    :   *#include <blob\_cli.h>*

        BLOB Transfer Client transfer inputs.

        Public Members

        [sys\_slist\_t](../../../../kernel/data_structures/slist.md#c.sys_slist_t "sys_slist_t") targets
        :   Linked list of Target nodes.

            Each node should point to [bt\_mesh\_blob\_target::n](#structbt__mesh__blob__target_1aca0f3cabb5c457cfb11a4bc71c3bea85).

        uint16\_t app\_idx
        :   AppKey index to send with.

        uint16\_t group
        :   Group address destination for the BLOB transfer, or [BT\_MESH\_ADDR\_UNASSIGNED](access.md#group__bt__mesh__access_1ga6d11790af686e6d48f08c6f1cd65317c) to send every message to each Target node individually.

        uint8\_t ttl
        :   Time to live value of BLOB transfer messages.

        uint16\_t timeout\_base
        :   Additional response time for the Target nodes, in 10-second increments.

            The extra time can be used to give the Target nodes more time to respond to messages from the Client. The actual timeout will be calculated according to the following formula:

            ```text
            *  timeout = 20 seconds + (10 seconds * timeout_base) + (100 ms * TTL)
            *
            ```

            If a Target node fails to respond to a message from the Client within the configured transfer timeout, the Target node is dropped.

    struct bt\_mesh\_blob\_cli\_caps
    :   *#include <blob\_cli.h>*

        Transfer capabilities of a Target node.

        Public Members

        size\_t max\_size
        :   Max BLOB size.

        uint8\_t min\_block\_size\_log
        :   Logarithmic representation of the minimum block size.

        uint8\_t max\_block\_size\_log
        :   Logarithmic representation of the maximum block size.

        uint16\_t max\_chunks
        :   Max number of chunks per block.

        uint16\_t max\_chunk\_size
        :   Max chunk size.

        uint16\_t mtu\_size
        :   Max MTU size.

        enum [bt\_mesh\_blob\_xfer\_mode](blob.md#c.bt_mesh_blob_xfer_mode "bt_mesh_blob_xfer_mode") modes
        :   Supported transfer modes.

    struct bt\_mesh\_blob\_cli\_cb
    :   *#include <blob\_cli.h>*

        Event handler callbacks for the BLOB Transfer Client model.

        All handlers are optional.

        Public Members

        void (\*caps)(struct [bt\_mesh\_blob\_cli](#c.bt_mesh_blob_cli) \*cli, const struct [bt\_mesh\_blob\_cli\_caps](#c.bt_mesh_blob_cli_caps) \*caps)
        :   Capabilities retrieval completion callback.

            Called when the capabilities retrieval procedure completes, indicating that a common set of acceptable transfer parameters have been established for the given list of Target nodes. All compatible Target nodes have status code [BT\_MESH\_BLOB\_SUCCESS](blob.md#group__bt__mesh__blob_1gga7b5e2895a6577103a8a680a94ee7776daac639c3c82cf48a394c13e3b057c9c0d).

            Param cli:
            :   BLOB Transfer Client instance.

            Param caps:
            :   Safe transfer capabilities if the transfer capabilities of at least one Target node has satisfied the Client, or NULL otherwise.

        void (\*lost\_target)(struct [bt\_mesh\_blob\_cli](#c.bt_mesh_blob_cli) \*cli, struct [bt\_mesh\_blob\_target](#c.bt_mesh_blob_target) \*target, enum [bt\_mesh\_blob\_status](blob.md#c.bt_mesh_blob_status "bt_mesh_blob_status") reason)
        :   Target node loss callback.

            Called whenever a Target node has been lost due to some error in the transfer. Losing a Target node is not considered a fatal error for the Client until all Target nodes have been lost.

            Param cli:
            :   BLOB Transfer Client instance.

            Param target:
            :   Target node that was lost.

            Param reason:
            :   Reason for the Target node loss.

        void (\*suspended)(struct [bt\_mesh\_blob\_cli](#c.bt_mesh_blob_cli) \*cli)
        :   Transfer is suspended.

            Called when the transfer is suspended due to response timeout from all Target nodes.

            Param cli:
            :   BLOB Transfer Client instance.

        void (\*end)(struct [bt\_mesh\_blob\_cli](#c.bt_mesh_blob_cli) \*cli, const struct [bt\_mesh\_blob\_xfer](blob.md#c.bt_mesh_blob_xfer "bt_mesh_blob_xfer") \*xfer, bool success)
        :   Transfer end callback.

            Called when the transfer ends.

            Param cli:
            :   BLOB Transfer Client instance.

            Param xfer:
            :   Completed transfer.

            Param success:
            :   Status of the transfer. Is `true` if at least one Target node received the whole transfer.

        void (\*xfer\_progress)(struct [bt\_mesh\_blob\_cli](#c.bt_mesh_blob_cli) \*cli, struct [bt\_mesh\_blob\_target](#c.bt_mesh_blob_target) \*target, const struct [bt\_mesh\_blob\_xfer\_info](#c.bt_mesh_blob_xfer_info) \*info)
        :   Transfer progress callback.

            The content of `info` is invalidated upon exit from the callback. Therefore it needs to be copied if it is planned to be used later.

            Param cli:
            :   BLOB Transfer Client instance.

            Param target:
            :   Target node that responded to the request.

            Param info:
            :   BLOB transfer information.

        void (\*xfer\_progress\_complete)(struct [bt\_mesh\_blob\_cli](#c.bt_mesh_blob_cli) \*cli)
        :   End of Get Transfer Progress procedure.

            Called when all Target nodes have responded or the procedure timed-out.

            Param cli:
            :   BLOB Transfer Client instance.

    struct bt\_mesh\_blob\_cli
    :   *#include <blob\_cli.h>*

        BLOB Transfer Client model instance.

        Public Members

        const struct [bt\_mesh\_blob\_cli\_cb](#c.bt_mesh_blob_cli_cb) \*cb
        :   Event handler callbacks.
