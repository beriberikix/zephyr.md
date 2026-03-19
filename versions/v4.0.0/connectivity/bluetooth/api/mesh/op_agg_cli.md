---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/bluetooth/api/mesh/op_agg_cli.html
original_path: connectivity/bluetooth/api/mesh/op_agg_cli.html
---

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

[Opcodes Aggregator Client model](../../../../doxygen/html/group__bt__mesh__op__agg__cli.md)
