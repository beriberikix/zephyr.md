---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/bluetooth/api/l2cap.html
original_path: connectivity/bluetooth/api/l2cap.html
---

# Logical Link Control and Adaptation Protocol (L2CAP)

L2CAP layer enables connection-oriented channels which can be enable with the
configuration option: [`CONFIG_BT_L2CAP_DYNAMIC_CHANNEL`](../../../kconfig.md#CONFIG_BT_L2CAP_DYNAMIC_CHANNEL "CONFIG_BT_L2CAP_DYNAMIC_CHANNEL"). This channels
support segmentation and reassembly transparently, they also support credit
based flow control making it suitable for data streams.

Channels instances are represented by the [`bt_l2cap_chan`](../../../doxygen/html/structbt__l2cap__chan.md) struct which
contains the callbacks in the [`bt_l2cap_chan_ops`](../../../doxygen/html/structbt__l2cap__chan__ops.md) struct to inform
when the channel has been connected, disconnected or when the encryption has
changed.
In addition to that it also contains the `recv` callback which is called
whenever an incoming data has been received. Data received this way can be
marked as processed by returning 0 or using
[`bt_l2cap_chan_recv_complete()`](../../../doxygen/html/group__bt__l2cap.md#gad53f5fc31314121ff84e740879eae3cf) API if processing is asynchronous.

Note

The `recv` callback is called directly from RX Thread thus it is not
recommended to block for long periods of time.

For sending data the [`bt_l2cap_chan_send()`](../../../doxygen/html/group__bt__l2cap.md#ga97b7909749667f910f83e6fcb54495c3) API can be used noting that
it may block if no credits are available, and resuming as soon as more credits
are available.

Servers can be registered using [`bt_l2cap_server_register()`](../../../doxygen/html/group__bt__l2cap.md#ga1a5e8c81c086872d7fb8da5329f982c6) API passing
the [`bt_l2cap_server`](../../../doxygen/html/structbt__l2cap__server.md) struct which informs what `psm` it should
listen to, the required security level `sec_level`, and the callback
`accept` which is called to authorize incoming connection requests and
allocate channel instances.

Client channels can be initiated with use of [`bt_l2cap_chan_connect()`](../../../doxygen/html/group__bt__l2cap.md#ga3c3cfb4b151c808c0a3d2562a5c26a20)
API and can be disconnected with the [`bt_l2cap_chan_disconnect()`](../../../doxygen/html/group__bt__l2cap.md#ga7165f82a05e3a19d6b2baf0ba292a3fe) API.
Note that the later can also disconnect channel instances created by servers.

## API Reference

[L2CAP](../../../doxygen/html/group__bt__l2cap.md)
