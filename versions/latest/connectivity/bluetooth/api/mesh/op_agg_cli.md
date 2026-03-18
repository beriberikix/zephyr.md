---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/mesh/op_agg_cli.html
original_path: connectivity/bluetooth/api/mesh/op_agg_cli.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Opcodes Aggregator Client

The Opcodes Aggregator Client model is a foundation model defined by the Bluetooth Mesh
specification. It is an optional model, enabled with the [`CONFIG_BT_MESH_OP_AGG_CLI`](../../../../kconfig.md#CONFIG_BT_MESH_OP_AGG_CLI "CONFIG_BT_MESH_OP_AGG_CLI")
option.

The Opcodes Aggregator Client model is introduced in the Bluetooth Mesh Protocol Specification
version 1.1, and is used to support the functionality of dispatching a sequence of access layer
messages to nodes supporting the [Opcodes Aggregator Server](op_agg_srv.md#bluetooth-mesh-models-op-agg-srv) model.

The Opcodes Aggregator Client model communicates with an Opcodes Aggregator Server model using the
device key of the target node or the application keys configured by the Configuration Client.

If present, the Opcodes Aggregator Client model must only be instantiated on the primary element.

The Opcodes Aggregator Client model is implicitly bound to the device key on initialization. It
should be bound to the same application keys as the client models that are used to produce the
sequence of messages.

To be able to aggregate a message from a client model, it should support an asynchronous API, for
example through callbacks.

## API reference

*group* bt\_mesh\_op\_agg\_cli
:   Defines

    BT\_MESH\_MODEL\_OP\_AGG\_CLI
    :   Opcodes Aggregator Client model composition data entry.

    Functions

    int bt\_mesh\_op\_agg\_cli\_seq\_start(uint16\_t net\_idx, uint16\_t app\_idx, uint16\_t dst, uint16\_t elem\_addr)
    :   Configure Opcodes Aggregator context.

        Parameters:
        :   - **net\_idx** – NetKey index to encrypt with.
            - **app\_idx** – AppKey index to encrypt with.
            - **dst** – Target Opcodes Aggregator Server address.
            - **elem\_addr** – Target node element address for the sequence message.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_op\_agg\_cli\_seq\_send(void)
    :   Opcodes Aggregator message send.

        Uses previously configured context and sends aggregated message to target node.

        Returns:
        :   0 on success, or (negative) error code on failure.

    void bt\_mesh\_op\_agg\_cli\_seq\_abort(void)
    :   Abort Opcodes Aggregator context.

    bool bt\_mesh\_op\_agg\_cli\_seq\_is\_started(void)
    :   Check if Opcodes Aggregator Sequence context is started.

        Returns:
        :   true if it is started, otherwise false.

    size\_t bt\_mesh\_op\_agg\_cli\_seq\_tailroom(void)
    :   Get Opcodes Aggregator context tailroom.

        Returns:
        :   Remaning tailroom of Opcodes Aggregator SDU.

    int32\_t bt\_mesh\_op\_agg\_cli\_timeout\_get(void)
    :   Get the current transmission timeout value.

        Returns:
        :   The configured transmission timeout in milliseconds.

    void bt\_mesh\_op\_agg\_cli\_timeout\_set(int32\_t timeout)
    :   Set the transmission timeout value.

        Parameters:
        :   - **timeout** – The new transmission timeout.
