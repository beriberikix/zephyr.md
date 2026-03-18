---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/networking/api/net_core.html
original_path: connectivity/networking/api/net_core.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

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

Related code samples

[Telnet console](../../../samples/net/telnet/README.md#telnet-console "Access Zephyr shell over telnet.")
:   Access Zephyr shell over telnet.

[mDNS responder](../../../samples/net/mdns_responder/README.md#mdns-responder "Listen and respond to mDNS queries.")
:   Listen and respond to mDNS queries.

*group* net\_core
:   Network core library.

    Enums

    enum net\_verdict
    :   Net Verdict.

        *Values:*

        enumerator NET\_OK
        :   Packet has been taken care of.

        enumerator NET\_CONTINUE
        :   Packet has not been touched, other part should decide about its fate.

        enumerator NET\_DROP
        :   Packet must be dropped.

    Functions

    int net\_recv\_data(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, struct [net\_pkt](net_pkt.md#c.net_pkt "net_pkt") \*pkt)
    :   Called by lower network stack or network device driver when a network packet has been received.

        The function will push the packet up in the network stack for further processing.

        Parameters:
        :   - **iface** – Network interface where the packet was received.
            - **pkt** – Network packet data.

        Returns:
        :   0 if ok, <0 if error.

    int net\_send\_data(struct [net\_pkt](net_pkt.md#c.net_pkt "net_pkt") \*pkt)
    :   Send data to network.

        Send data to network. This should not be used normally by applications as it requires that the network packet is properly constructed.

        Parameters:
        :   - **pkt** – Network packet.

        Returns:
        :   0 if ok, <0 if error. If <0 is returned, then the caller needs to unref the pkt in order to avoid memory leak.
