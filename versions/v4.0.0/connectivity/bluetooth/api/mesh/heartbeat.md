---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/bluetooth/api/mesh/heartbeat.html
original_path: connectivity/bluetooth/api/mesh/heartbeat.html
---

# Heartbeat

The Heartbeat feature provides functionality for monitoring Bluetooth Mesh nodes
and determining the distance between nodes.

The Heartbeat feature is configured through the [Configuration Server](cfg_srv.md#bluetooth-mesh-models-cfg-srv) model.

## Heartbeat messages

Heartbeat messages are sent as transport control packets through the network,
and are only encrypted with a network key. Heartbeat messages contain the
original Time To Live (TTL) value used to send the message and a bitfield of
the active features on the node. Through this, a receiving node can determine
how many relays the message had to go through to arrive at the receiver, and
what features the node supports.

Available Heartbeat feature flags:

- [`BT_MESH_FEAT_RELAY`](../../../../doxygen/html/group__bt__mesh.md#gac588eefe83db94784a420ce063f02b55)
- [`BT_MESH_FEAT_PROXY`](../../../../doxygen/html/group__bt__mesh.md#gaee648ce202316c56d4d588cb0ad5aeb4)
- [`BT_MESH_FEAT_FRIEND`](../../../../doxygen/html/group__bt__mesh.md#ga8f27086b3bc3c4a6e14621836f9f8e80)
- [`BT_MESH_FEAT_LOW_POWER`](../../../../doxygen/html/group__bt__mesh.md#gaad71a36c82b4e4d3fa334ecff5cc0171)

## Heartbeat publication

Heartbeat publication is controlled through the Configuration models, and can
be triggered in two ways:

Periodic publication
:   The node publishes a new Heartbeat message at regular intervals. The
    publication can be configured to stop after a certain number of messages, or
    continue indefinitely.

Triggered publication
:   The node publishes a new Heartbeat message every time a feature changes. The
    set of features that can trigger the publication is configurable.

The two publication types can be combined.

## Heartbeat subscription

A node can be configured to subscribe to Heartbeat messages from one node at
the time. To receive a Heartbeat message, both the source and destination must
match the configured subscription parameters.

Heartbeat subscription is always time limited, and throughout the subscription
period, the node keeps track of the number of received Heartbeats as well as
the minimum and maximum received hop count.

All Heartbeats received with the configured subscription parameters are passed
to the `bt_mesh_hb_cb::recv` event handler.

When the Heartbeat subscription period ends, the
`bt_mesh_hb_cb::sub_end` callback gets called.

## API reference

[Heartbeat](../../../../doxygen/html/group__bt__mesh__heartbeat.md)
