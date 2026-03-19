---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/networking/api/net_core.html
original_path: connectivity/networking/api/net_core.html
---

# Network Core Helpers

## [Overview](#id1)

The network subsystem contains two functions for sending and receiving
data from the network. The `net_recv_data()` is typically used by network
device driver when the received network data needs to be pushed up in the
network stack for further processing. All the data is received via a network
interface which is typically created by the device driver.

For sending, the `net_send_data()` can be used. Typically applications do not
call this function directly as there is the [BSD Sockets](sockets.md#bsd-sockets-interface) API
for sending and receiving network data.

## [API Reference](#id2)

[Network Core Library](../../../doxygen/html/group__net__core.md)

Related code samples

- [mDNS responder](../../../samples/net/mdns_responder/README.md#mdns-responder "Listen and respond to mDNS queries.")Listen and respond to mDNS queries.
- [Telnet console](../../../samples/net/telnet/README.md#telnet-console "Access Zephyr shell over telnet.")Access Zephyr shell over telnet.
