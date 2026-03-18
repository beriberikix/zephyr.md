---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/promiscuous.html
original_path: connectivity/networking/api/promiscuous.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Promiscuous Mode

## [Overview](#id1)

Promiscuous mode is a mode for a network interface controller that
causes it to pass all traffic it receives to the application rather than
passing only the frames that the controller is specifically programmed
to receive. This mode is normally used for packet sniffing as used
to diagnose network connectivity issues by showing an application
all the data being transferred over the network. (See the
[Wikipedia article on promiscuous mode](https://en.wikipedia.org/wiki/Promiscuous_mode) for more information.)

The network promiscuous APIs are used to enable and disable this mode,
and to wait for and receive a network data to arrive. Not all network
technologies or network device drivers support promiscuous mode.

## [Sample usage](#id2)

First the promiscuous mode needs to be turned ON by the application like this:

```c
ret = net_promisc_mode_on(iface);
if (ret < 0) {
        if (ret == -EALREADY) {
                printf("Promiscuous mode already enabled\n");
        } else {
                printf("Cannot enable promiscuous mode for "
                       "interface %p (%d)\n", iface, ret);
        }
}
```

If there is no error, then the application can start to wait for network data:

```c
while (true) {
        pkt = net_promisc_mode_wait_data(K_FOREVER);
        if (pkt) {
                print_info(pkt);
        }

        net_pkt_unref(pkt);
}
```

Finally the promiscuous mode can be turned OFF by the application like this:

```c
ret = net_promisc_mode_off(iface);
if (ret < 0) {
        if (ret == -EALREADY) {
                printf("Promiscuous mode already disabled\n");
        } else {
                printf("Cannot disable promiscuous mode for "
                       "interface %p (%d)\n", iface, ret);
        }
}
```

See [Promiscuous mode](../../../samples/net/promiscuous_mode/README.md#net-promiscuous-mode "Enable promiscuous mode on all interfaces and print information about incoming packets.") for a more comprehensive example.

## [API Reference](#id3)

Related code samples

[Promiscuous mode](../../../samples/net/promiscuous_mode/README.md#net-promiscuous-mode "Enable promiscuous mode on all interfaces and print information about incoming packets.")
:   Enable promiscuous mode on all interfaces and print information about incoming packets.

*group* Promiscuous mode
:   Promiscuous mode support.

    Functions

    static inline struct [net\_pkt](net_pkt.md#c.net_pkt "net_pkt") \*net\_promisc\_mode\_wait\_data([k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Start to wait received network packets.

        Parameters:
        :   - **timeout** – How long to wait before returning.

        Returns:
        :   Received [net\_pkt](net_pkt.md#structnet__pkt), NULL if not received any packet.

    static inline int net\_promisc\_mode\_on(struct [net\_if](net_if.md#c.net_if "net_if") \*iface)
    :   Enable promiscuous mode for a given network interface.

        Parameters:
        :   - **iface** – Network interface

        Returns:
        :   0 if ok, <0 if error

    static inline int net\_promisc\_mode\_off(struct [net\_if](net_if.md#c.net_if "net_if") \*iface)
    :   Disable promiscuous mode for a given network interface.

        Parameters:
        :   - **iface** – Network interface

        Returns:
        :   0 if ok, <0 if error
