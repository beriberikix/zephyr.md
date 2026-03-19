---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/bluetooth/api/mesh/sar_cfg.html
original_path: connectivity/bluetooth/api/mesh/sar_cfg.html
---

# Segmentation and reassembly (SAR)

Segmentation and reassembly (SAR) provides a way of handling larger upper transport layer messages
in a mesh network, with a purpose of enhancing the Bluetooth Mesh throughput. The segmentation and
reassembly mechanism is used by the lower transport layer.

The lower transport layer defines how the upper transport layer PDUs are segmented and reassembled
into multiple Lower Transport PDUs, and sends them to the lower transport layer on a peer device.
If the Upper Transport PDU fits, it is sent in a single Lower Transport PDU. For longer packets,
which do not fit into a single Lower Transport PDU, the lower transport layer performs segmentation,
splitting the Upper Transport
PDU into multiple segments.

The lower transport layer on the receiving device reassembles the segments into a single Upper
Transport PDU before passing it up the stack. Delivery of a segmented message is acknowledged by the
lower transport layer of the receiving node, while an unsegmented message delivery is not
acknowledged. However, an Upper Transport PDU that fits into one Lower Transport PDU can also be
sent as a single-segment segmented message when acknowledgment by the lower transport layer is
required. Set the `send rel` flag (see [`bt_mesh_msg_ctx`](../../../../doxygen/html/structbt__mesh__msg__ctx.md)) to use the reliable message
transmission and acknowledge single-segment segmented messages.

The transport layer is able to transport up to 32 segments with its SAR mechanism, with a maximum
message (PDU) size of 384 octets. To configure message size for the Bluetooth Mesh stack, use the
following Kconfig options:

- [`CONFIG_BT_MESH_RX_SEG_MAX`](../../../../kconfig.md#CONFIG_BT_MESH_RX_SEG_MAX "CONFIG_BT_MESH_RX_SEG_MAX") to set the maximum number of segments in an incoming message.
- [`CONFIG_BT_MESH_TX_SEG_MAX`](../../../../kconfig.md#CONFIG_BT_MESH_TX_SEG_MAX "CONFIG_BT_MESH_TX_SEG_MAX") to set the maximum number of segments in an outgoing message.

The Kconfig options [`CONFIG_BT_MESH_TX_SEG_MSG_COUNT`](../../../../kconfig.md#CONFIG_BT_MESH_TX_SEG_MSG_COUNT "CONFIG_BT_MESH_TX_SEG_MSG_COUNT") and
[`CONFIG_BT_MESH_RX_SEG_MSG_COUNT`](../../../../kconfig.md#CONFIG_BT_MESH_RX_SEG_MSG_COUNT "CONFIG_BT_MESH_RX_SEG_MSG_COUNT") define how many outgoing and incoming segmented
messages can be processed simultaneously. When more than one segmented message is sent to the same
destination, the messages are queued and sent one at a time.

Incoming and outgoing segmented messages share the same pool for allocation of their segments. This
pool size is configured through the [`CONFIG_BT_MESH_SEG_BUFS`](../../../../kconfig.md#CONFIG_BT_MESH_SEG_BUFS "CONFIG_BT_MESH_SEG_BUFS") Kconfig option.
Both incoming and outgoing messages allocate segments at the start of the transaction. The outgoing
segmented message releases its segments one by one as soon as they are acknowledged by the receiver,
while the incoming message releases the segments first after the message is fully received.
Keep this in mind when defining the size of the buffers.

SAR does not impose extra overhead on the access layer payload per segment.

## Segmentation and reassembly (SAR) Configuration models

With Bluetooth Mesh Protocol Specification version 1.1, it became possible to configure SAR
behavior, such as intervals, timers and retransmission counters, over a mesh network using SAR
Configuration models:

- [SAR Configuration Client](sar_cfg_cli.md#bluetooth-mesh-sar-cfg-cli)
- [SAR Configuration Server](sar_cfg_srv.md#bluetooth-mesh-sar-cfg-srv)

The following SAR behavior applies regardless of the presence of a SAR Configuration Server on a
node.

Transmission of segments is separated by a segment transmission interval (see the
[SAR Segment Interval Step](#sar-segment-interval-step) state). Other configurable time intervals and delays available for the
segmentation and reassembly are:

- Interval between unicast retransmissions (see the states [SAR Unicast Retransmissions Interval Step](#sar-unicast-retransmissions-interval-step) and [SAR Unicast Retransmissions Interval Increment](#sar-unicast-retransmissions-interval-increment)).
- Interval between multicast retransmissions (see the [SAR Multicast Retransmissions Interval Step](#sar-multicast-retransmissions-interval-step) state).
- Segment reception interval (see the [SAR Receiver Segment Interval Step](#sar-receiver-segment-interval-step) state).
- Acknowledgment delay increment (see the [SAR Acknowledgment Delay Increment](#sar-acknowledgment-delay-increment) state).

When the last segment marked as unacknowledged is transmitted, the lower transport layer starts a
retransmissions timer. The initial value of the SAR Unicast Retransmissions timer depends on the
value of the TTL field of the message. If the TTL field value is greater than `0`, the initial
value for the timer is set according to the following formula:

\[unicast~retransmissions~interval~step + unicast~retransmissions~interval~increment \times (TTL - 1)\]

If the TTL field value is `0`, the initial value of the timer is set to the unicast
retransmissions interval step.

The initial value of the SAR Multicast Retransmissions timer is set to the multicast retransmissions
interval.

When the lower transport layer receives a message segment, it starts a SAR Discard timer. The
discard timer tells how long the lower transport layer waits before discarding the segmented message
the segment belongs to. The initial value of the SAR Discard timer is the discard timeout value
indicated by the [SAR Discard Timeout](#sar-discard-timeout) state.

SAR Acknowledgment timer holds the time before a Segment Acknowledgment message is sent for a
received segment. The initial value of the SAR Acknowledgment timer is calculated using the
following formula:

\[min(SegN + 0.5 , acknowledgment~delay~increment) \times segment~reception~interval\]

The `SegN` field value identifies the total number of segments the Upper Transport PDU is
segmented into.

Four counters are related to SAR behavior:

- Two unicast retransmissions counts (see [SAR Unicast Retransmissions Count](#sar-unicast-retransmissions-count) state and [SAR Unicast Retransmissions Without Progress Count](#sar-unicast-retransmissions-without-progress-count) state)
- Multicast retransmissions count (see [SAR Multicast Retransmissions Count](#sar-multicast-retransmissions-count) state)
- Acknowledgment retransmissions count (see [SAR Acknowledgment Retransmissions Count](#sar-acknowledgment-retransmissions-count) state)

If the number of segments in the transmission is higher than the value of the
[SAR Segments Threshold](#sar-segments-threshold) state, Segment Acknowledgment messages are retransmitted using the value
of the [SAR Acknowledgment Retransmissions Count](#sar-acknowledgment-retransmissions-count) state.

## SAR states

There are two states defined related to segmentation and reassembly:

- SAR Transmitter state
- SAR Receiver state

The SAR Transmitter state is a composite state that controls the number and timing of transmissions
of segmented messages. It includes the following states:

- SAR Segment Interval Step
- SAR Unicast Retransmissions Count
- SAR Unicast Retransmissions Without Progress Count
- SAR Unicast Retransmissions Interval Step
- SAR Unicast Retransmissions Interval Increment
- SAR Multicast Retransmissions Count
- SAR Multicast Retransmissions Interval Step

The SAR Receiver state is a composite state that controls the number and timing of Segment
Acknowledgment transmissions and the discarding of reassembly of a segmented message. It includes
the following states:

- SAR Segments Threshold
- SAR Discard Timeout
- SAR Acknowledgment Delay Increment
- SAR Acknowledgment Retransmissions Count
- SAR Receiver Segment Interval Step

### SAR Segment Interval Step

SAR Segment Interval Step state holds a value that controls the interval between transmissions of
segments of a segmented message. The interval is measured in milliseconds.

Use the [`CONFIG_BT_MESH_SAR_TX_SEG_INT_STEP`](../../../../kconfig.md#CONFIG_BT_MESH_SAR_TX_SEG_INT_STEP "CONFIG_BT_MESH_SAR_TX_SEG_INT_STEP") Kconfig option to set the default
value. Segment transmission interval is then calculated using the following formula:

\[(\mathtt{CONFIG\\_BT\\_MESH\\_SAR\\_TX\\_SEG\\_INT\\_STEP} + 1) \times 10~\text{ms}\]

### SAR Unicast Retransmissions Count

SAR Unicast Retransmissions Count holds a value that defines the maximum number of retransmissions
of a segmented message to a unicast destination. Use the
[`CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_COUNT`](../../../../kconfig.md#CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_COUNT "CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_COUNT") Kconfig option to set the default
value for this state.

### SAR Unicast Retransmissions Without Progress Count

This state holds a value that defines the maximum number of retransmissions of a segmented message
to a unicast address that will be sent if no acknowledgment was received during the timeout, or if
an acknowledgment with already confirmed segments was received. Use the Kconfig option
[`CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_WITHOUT_PROG_COUNT`](../../../../kconfig.md#CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_WITHOUT_PROG_COUNT "CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_WITHOUT_PROG_COUNT") to set the maximum number
of retransmissions.

### SAR Unicast Retransmissions Interval Step

The value of this state controls the interval step used for delaying the retransmissions of
unacknowledged segments of a segmented message to a unicast address. The interval step is measured
in milliseconds.

Use the [`CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_INT_STEP`](../../../../kconfig.md#CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_INT_STEP "CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_INT_STEP") Kconfig option to set the
default value. This value is then used to calculate the interval step using the following formula:

\[(\mathtt{CONFIG\\_BT\\_MESH\\_SAR\\_TX\\_UNICAST\\_RETRANS\\_INT\\_STEP} + 1) \times 25~\text{ms}\]

### SAR Unicast Retransmissions Interval Increment

SAR Unicast Retransmissions Interval Increment holds a value that controls the interval increment
used for delaying the retransmissions of unacknowledged segments of a segmented message to a unicast
address. The increment is measured in milliseconds.

Use the Kconfig option [`CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_INT_INC`](../../../../kconfig.md#CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_INT_INC "CONFIG_BT_MESH_SAR_TX_UNICAST_RETRANS_INT_INC") to set the
default value. The Kconfig option value is used to calculate the increment using the following
formula:

\[(\mathtt{CONFIG\\_BT\\_MESH\\_SAR\\_TX\\_UNICAST\\_RETRANS\\_INT\\_INC} + 1) \times 25~\text{ms}\]

### SAR Multicast Retransmissions Count

The state holds a value that controls the total number of retransmissions of a segmented message to
a multicast address. Use the Kconfig option
[`CONFIG_BT_MESH_SAR_TX_MULTICAST_RETRANS_COUNT`](../../../../kconfig.md#CONFIG_BT_MESH_SAR_TX_MULTICAST_RETRANS_COUNT "CONFIG_BT_MESH_SAR_TX_MULTICAST_RETRANS_COUNT") to set the total number of
retransmissions.

### SAR Multicast Retransmissions Interval Step

This state holds a value that controls the interval between retransmissions of all segments in a
segmented message to a multicast address. The interval is measured in milliseconds.

Use the Kconfig option [`CONFIG_BT_MESH_SAR_TX_MULTICAST_RETRANS_INT`](../../../../kconfig.md#CONFIG_BT_MESH_SAR_TX_MULTICAST_RETRANS_INT "CONFIG_BT_MESH_SAR_TX_MULTICAST_RETRANS_INT") to set the
default value that is used to calculate the interval using the following formula:

\[(\mathtt{CONFIG\\_BT\\_MESH\\_SAR\\_TX\\_MULTICAST\\_RETRANS\\_INT} + 1) \times 25~\text{ms}\]

### SAR Discard Timeout

The value of this state defines the time in seconds that the lower transport layer waits after
receiving segments of a segmented message before discarding that segmented message. Use the Kconfig
option [`CONFIG_BT_MESH_SAR_RX_DISCARD_TIMEOUT`](../../../../kconfig.md#CONFIG_BT_MESH_SAR_RX_DISCARD_TIMEOUT "CONFIG_BT_MESH_SAR_RX_DISCARD_TIMEOUT") to set the default value. The discard
timeout will be calculated using the following formula:

\[(\mathtt{CONFIG\\_BT\\_MESH\\_SAR\\_RX\\_DISCARD\\_TIMEOUT} + 1) \times 5~\text{seconds}\]

### SAR Acknowledgment Delay Increment

This state holds a value that controls the delay increment of an interval used for delaying the
transmission of an acknowledgment message after receiving a new segment. The increment is measured
in segments.

Use the Kconfig option [`CONFIG_BT_MESH_SAR_RX_ACK_DELAY_INC`](../../../../kconfig.md#CONFIG_BT_MESH_SAR_RX_ACK_DELAY_INC "CONFIG_BT_MESH_SAR_RX_ACK_DELAY_INC") to set the default
value. The increment value is calculated to be
\(\verb|CONFIG\_BT\_MESH\_SAR\_RX\_ACK\_DELAY\_INC| + 1.5\).

### SAR Segments Threshold

SAR Segments Threshold state holds a value that defines a threshold in number of segments of a
segmented message for acknowledgment retransmissions. Use the Kconfig option
[`CONFIG_BT_MESH_SAR_RX_SEG_THRESHOLD`](../../../../kconfig.md#CONFIG_BT_MESH_SAR_RX_SEG_THRESHOLD "CONFIG_BT_MESH_SAR_RX_SEG_THRESHOLD") to set the threshold.

When the number of segments of a segmented message is above this threshold, the stack will
additionally retransmit every acknowledgment message the number of times given by the value of
[`CONFIG_BT_MESH_SAR_RX_ACK_RETRANS_COUNT`](../../../../kconfig.md#CONFIG_BT_MESH_SAR_RX_ACK_RETRANS_COUNT "CONFIG_BT_MESH_SAR_RX_ACK_RETRANS_COUNT").

### SAR Acknowledgment Retransmissions Count

The SAR Acknowledgment Retransmissions Count state controls the number of retransmissions of Segment
Acknowledgment messages sent by the lower transport layer. It gives the total number of
retranmissions of an acknowledgment message that the stack will additionally send when the size of
segments in a segmented message is above the [`CONFIG_BT_MESH_SAR_RX_SEG_THRESHOLD`](../../../../kconfig.md#CONFIG_BT_MESH_SAR_RX_SEG_THRESHOLD "CONFIG_BT_MESH_SAR_RX_SEG_THRESHOLD")
value.

Use the Kconfig option [`CONFIG_BT_MESH_SAR_RX_ACK_RETRANS_COUNT`](../../../../kconfig.md#CONFIG_BT_MESH_SAR_RX_ACK_RETRANS_COUNT "CONFIG_BT_MESH_SAR_RX_ACK_RETRANS_COUNT") to set the default
value for this state. The maximum number of transmissions of a Segment Acknowledgment message is
\(\verb|CONFIG\_BT\_MESH\_SAR\_RX\_ACK\_RETRANS\_COUNT| + 1\).

### SAR Receiver Segment Interval Step

The SAR Receiver Segment Interval Step defines the segments reception interval step used for
delaying the transmission of an acknowledgment message after receiving a new segment. The interval
is measured in milliseconds.

Use the Kconfig option [`CONFIG_BT_MESH_SAR_RX_SEG_INT_STEP`](../../../../kconfig.md#CONFIG_BT_MESH_SAR_RX_SEG_INT_STEP "CONFIG_BT_MESH_SAR_RX_SEG_INT_STEP") to set the default value
and calculate the interval using the following formula:

\[(\mathtt{CONFIG\\_BT\\_MESH\\_SAR\\_RX\\_SEG\\_INT\\_STEP} + 1) \times 10~\text{ms}\]
