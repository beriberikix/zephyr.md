---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/canbus/isotp.html
original_path: connectivity/canbus/isotp.html
---

# ISO-TP Transport Protocol

## [Overview](#id1)

ISO-TP is a transport protocol defined in the ISO-Standard ISO15765-2 Road
vehicles - Diagnostic communication over Controller Area Network (DoCAN).
Part2: Transport protocol and network layer services. As its name already
implies, it is originally designed, and still used in road vehicle diagnostic
over Controller Area Networks. Nevertheless, it’s not limited to applications in
road vehicles or the automotive domain.

This transport protocol extends the limited payload data size for classical
CAN (8 bytes) and CAN FD (64 bytes) to theoretically four gigabytes.
Additionally, it adds a flow control mechanism to influence the sender’s
behavior. ISO-TP segments packets into small fragments depending on the payload
size of the CAN frame. The header of those segments is called Protocol Control
Information (PCI).

Packets smaller or equal to seven bytes on Classical CAN are called
single-frames (SF). They don’t need to fragment and do not have any flow-control.

Packets larger than that are segmented into a first-frame (FF) and as many
consecutive-frames (CF) as required. The FF contains information about the length of
the entire payload data and additionally, the first few bytes of payload data.
The receiving peer sends back a flow-control-frame (FC) to either deny,
postpone, or accept the following consecutive frames.
The FC also defines the conditions of sending, namely the block-size (BS) and
the minimum separation time between frames (STmin). The block size defines how
many CF the sender is allowed to send, before he has to wait for another FC.

[![ISO-TP Sequence](../../_images/isotp_sequence.svg)
](../../_images/isotp_sequence.svg)

## [API Reference](#id2)

[CAN ISO-TP Protocol](../../doxygen/html/group__can__isotp.md)

Related code samples

- [ISO-TP library](../../samples/subsys/canbus/isotp/README.md#isotp "Use ISO-TP library to exchange messages between two boards.")Use ISO-TP library to exchange messages between two boards.
