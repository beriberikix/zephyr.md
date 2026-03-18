---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/networking/api/capture.html
original_path: connectivity/networking/api/capture.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Network Packet Capture

## [Overview](#id1)

The `net_capture` API allows user to monitor the network
traffic in one of the Zephyr network interfaces and send that traffic to
external system for analysis. The monitoring can be setup either manually
using `net-shell` or automatically by using the `net_capture` API.

## [Sample usage](#id2)

See [Network packet capture](../../../samples/net/capture/README.md#net-capture "Capture network packets and send them to a remote host via IPIP tunnel.") sample application and
[Monitor Network Traffic](../network_monitoring.md#network-monitoring) for details.

## [API Reference](#id3)

Related code samples

[Network packet capture](../../../samples/net/capture/README.md#net-capture "Capture network packets and send them to a remote host via IPIP tunnel.")
:   Capture network packets and send them to a remote host via IPIP tunnel.

*group* net\_capture
:   Network packet capture support functions.

    Functions

    int net\_capture\_setup(const char \*remote\_addr, const char \*my\_local\_addr, const char \*peer\_addr, const struct [device](../../../kernel/drivers/index.md#c.device "device") \*\*dev)
    :   Setup network packet capturing support.

        Parameters:
        :   - **remote\_addr** – The value tells the tunnel remote/outer endpoint IP address. The IP address can be either IPv4 or IPv6 address. This address is used to select the network interface where the tunnel is created.
            - **my\_local\_addr** – The local/inner IP address of the tunnel. Can contain also port number which is used as UDP source port.
            - **peer\_addr** – The peer/inner IP address of the tunnel. Can contain also port number which is used as UDP destination port.
            - **dev** – Network capture device. This is returned to the caller.

        Returns:
        :   0 if ok, <0 if network packet capture setup failed

    static inline int net\_capture\_cleanup(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Cleanup network packet capturing support.

        This should be called after the capturing is done and resources can be released.

        Parameters:
        :   - **dev** – Network capture device. User must allocate using the [net\_capture\_setup()](#group__net__capture_1gab280c0c6cc607bdb07211a9450eae262) function.

        Returns:
        :   0 if ok, <0 if network packet capture cleanup failed

    static inline int net\_capture\_enable(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [net\_if](net_if.md#c.net_if "net_if") \*iface)
    :   Enable network packet capturing support.

        This creates tunnel network interface where all the captured packets are pushed. The captured network packets are placed in UDP packets that are sent to tunnel peer.

        Parameters:
        :   - **dev** – Network capture device
            - **iface** – Network interface we are starting to capture packets.

        Returns:
        :   0 if ok, <0 if network packet capture enable failed

    static inline bool net\_capture\_is\_enabled(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Is network packet capture enabled or disabled.

        Parameters:
        :   - **dev** – Network capture device

        Returns:
        :   True if enabled, False if network capture is disabled.

    static inline int net\_capture\_disable(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Disable network packet capturing support.

        Parameters:
        :   - **dev** – Network capture device

        Returns:
        :   0 if ok, <0 if network packet capture disable failed
