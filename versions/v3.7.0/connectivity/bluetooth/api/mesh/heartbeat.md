---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/api/mesh/heartbeat.html
original_path: connectivity/bluetooth/api/mesh/heartbeat.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

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

- [`BT_MESH_FEAT_RELAY`](core.md#c.BT_MESH_FEAT_RELAY "BT_MESH_FEAT_RELAY")
- [`BT_MESH_FEAT_PROXY`](core.md#c.BT_MESH_FEAT_PROXY "BT_MESH_FEAT_PROXY")
- [`BT_MESH_FEAT_FRIEND`](core.md#c.BT_MESH_FEAT_FRIEND "BT_MESH_FEAT_FRIEND")
- [`BT_MESH_FEAT_LOW_POWER`](core.md#c.BT_MESH_FEAT_LOW_POWER "BT_MESH_FEAT_LOW_POWER")

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

*group* Heartbeat
:   Heartbeat.

    Defines

    BT\_MESH\_HB\_CB\_DEFINE(\_name)
    :   Register a callback structure for Heartbeat events.

        Registers a callback structure that will be called whenever Heartbeat events occur

        Parameters:
        :   - **\_name** – Name of callback structure.

    Functions

    void bt\_mesh\_hb\_pub\_get(struct [bt\_mesh\_hb\_pub](#c.bt_mesh_hb_pub) \*get)
    :   Get the current Heartbeat publication parameters.

        Parameters:
        :   - **get** – Heartbeat publication parameters return buffer.

    void bt\_mesh\_hb\_sub\_get(struct [bt\_mesh\_hb\_sub](#c.bt_mesh_hb_sub) \*get)
    :   Get the current Heartbeat subscription parameters.

        Parameters:
        :   - **get** – Heartbeat subscription parameters return buffer.

    struct bt\_mesh\_hb\_pub
    :   *#include <heartbeat.h>*

        Heartbeat Publication parameters.

        Public Members

        uint16\_t dst
        :   Destination address.

        uint16\_t count
        :   Remaining publish count.

        uint8\_t ttl
        :   Time To Live value.

        uint16\_t feat
        :   Bitmap of features that trigger a Heartbeat publication if they change.

            Legal values are [BT\_MESH\_FEAT\_RELAY](core.md#group__bt__mesh_1gac588eefe83db94784a420ce063f02b55), [BT\_MESH\_FEAT\_PROXY](core.md#group__bt__mesh_1gaee648ce202316c56d4d588cb0ad5aeb4), [BT\_MESH\_FEAT\_FRIEND](core.md#group__bt__mesh_1ga8f27086b3bc3c4a6e14621836f9f8e80) and [BT\_MESH\_FEAT\_LOW\_POWER](core.md#group__bt__mesh_1gaad71a36c82b4e4d3fa334ecff5cc0171).

        uint16\_t net\_idx
        :   Network index used for publishing.

        uint32\_t period
        :   Publication period in seconds.

    struct bt\_mesh\_hb\_sub
    :   *#include <heartbeat.h>*

        Heartbeat Subscription parameters.

        Public Members

        uint32\_t period
        :   Subscription period in seconds.

        uint32\_t remaining
        :   Remaining subscription time in seconds.

        uint16\_t src
        :   Source address to receive Heartbeats from.

        uint16\_t dst
        :   Destination address to received Heartbeats on.

        uint16\_t count
        :   The number of received Heartbeat messages so far.

        uint8\_t min\_hops
        :   Minimum hops in received messages, ie the shortest registered path from the publishing node to the subscribing node.

            A Heartbeat received from an immediate neighbor has hop count = 1.

        uint8\_t max\_hops
        :   Maximum hops in received messages, ie the longest registered path from the publishing node to the subscribing node.

            A Heartbeat received from an immediate neighbor has hop count = 1.

    struct bt\_mesh\_hb\_cb
    :   *#include <heartbeat.h>*

        Heartbeat callback structure.

        Public Members

        void (\*recv)(const struct [bt\_mesh\_hb\_sub](#c.bt_mesh_hb_sub) \*sub, uint8\_t hops, uint16\_t feat)
        :   Receive callback for heartbeats.

            Gets called on every received Heartbeat that matches the current Heartbeat subscription parameters.

            Param sub:
            :   Current Heartbeat subscription parameters.

            Param hops:
            :   The number of hops the Heartbeat was received with.

            Param feat:
            :   The feature set of the publishing node. The value is a bitmap of [BT\_MESH\_FEAT\_RELAY](core.md#group__bt__mesh_1gac588eefe83db94784a420ce063f02b55), [BT\_MESH\_FEAT\_PROXY](core.md#group__bt__mesh_1gaee648ce202316c56d4d588cb0ad5aeb4), [BT\_MESH\_FEAT\_FRIEND](core.md#group__bt__mesh_1ga8f27086b3bc3c4a6e14621836f9f8e80) and [BT\_MESH\_FEAT\_LOW\_POWER](core.md#group__bt__mesh_1gaad71a36c82b4e4d3fa334ecff5cc0171).

        void (\*sub\_end)(const struct [bt\_mesh\_hb\_sub](#c.bt_mesh_hb_sub) \*sub)
        :   Subscription end callback for heartbeats.

            Gets called when the subscription period ends, providing a summary of the received heartbeat messages.

            Param sub:
            :   Current Heartbeat subscription parameters.

        void (\*pub\_sent)(const struct [bt\_mesh\_hb\_pub](#c.bt_mesh_hb_pub) \*pub)
        :   Publication sent callback for heartbeats.

            Gets called when the heartbeat is successfully published.

            Param pub:
            :   Current Heartbeat publication parameters.
