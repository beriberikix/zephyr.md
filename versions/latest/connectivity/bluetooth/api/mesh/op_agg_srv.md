---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/mesh/op_agg_srv.html
original_path: connectivity/bluetooth/api/mesh/op_agg_srv.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Opcodes Aggregator Server

The Opcodes Aggregator Server model is a foundation model defined by the Bluetooth
mesh specification. It is an optional model, enabled with the
[`CONFIG_BT_MESH_OP_AGG_SRV`](../../../../kconfig.md#CONFIG_BT_MESH_OP_AGG_SRV "CONFIG_BT_MESH_OP_AGG_SRV") option.

The Opcodes Aggregator Server model is introduced in the Bluetooth Mesh Protocol
Specification version 1.1, and is used to support the functionality of processing
a sequence of access layer messages.

The Opcodes Aggregator Server model accepts messages encrypted with the node’s device key
or the application keys.

If present, the Opcodes Aggregator Server model must only be instantiated on the primary element.

The targeted server models should be bound to the same application key that is used
to encrypt the sequence of access layer messages sent to the Opcodes Aggregator Server.

The Opcodes Aggregator Server handles aggregated messages and dispatches them to the
respective models and their message handlers. Current implementation assumes that
responses are sent from the same execution context as the received message and
doesn’t allow to send a postponed response, for example from a work queue.

## API reference

*group* bt\_mesh\_op\_agg\_srv
:   Defines

    BT\_MESH\_MODEL\_OP\_AGG\_SRV
    :   Opcodes Aggretator Server model composition data entry.

        Note

        The Opcodes Aggregator Server handles aggregated messages and dispatches them to the respective models and their message handlers. Current implementation assumes that responses are sent from the same execution context as the received message and doesn’t allow to send a postponed response, e.g. from workqueue.
