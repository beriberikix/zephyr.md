---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/capture.html
original_path: connectivity/networking/api/capture.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Network Packet Capture

## [Overview](#id1)

The `net_capture` API allows user to monitor the network
traffic in one of the Zephyr network interfaces and send that traffic to
external system for analysis. The monitoring can be setup either manually
using `net-shell` or automatically by using the `net_capture` API.

## [Cooked Mode Capture](#id2)

If capturing is enabled and configured, the system will automatically capture
network traffic for a given network interface. If you would like to capture
network data when there is no network interface involved, then you need to use
the cooked mode capture API.

In cooked mode capture, arbitrary network packets can be captured and there
does not need to be network interface involved. For example low level HDLC
packets in PPP can be captured, as the HDLC L2 layer data is stripped away when
using the normal network interface based capture. Also CANBUS or Bluetooth
network data could be captured although currently there is no support in the
network stack to capture those.

The cooked mode capture works like this:

- An `any` network interface is created. It acts as a sink where the cooked
  mode captured packets are written by the cooked mode capture API.
- A `cooked` virtual network interface is attached on top of this `any`
  interface.
- The `cooked` interface must be configured to capture certain L2 packet types
  using the network interface configuration API.
- When cooked mode capture API is used, the caller must specify what is the
  layer 2 protocol type of the captured data. The cooked mode capture API is then
  able to determine what to capture when receiving such a L2 packet.
- The network packet capturing infrastructure is then setup so that the `cooked`
  interface is marked as captured network interface.
  The packets received by the `cooked` interface via the `any` interface are
  then automatically placed to the capture IP tunnel and sent to remote host
  for analysis.

For example, in the sample capture application, these network interfaces
are created:

```c
Interface any (0x808ab3c) (Dummy) [1]
================================
Virtual interfaces attached to this : 2
Device    : NET_ANY (0x80849a4)

Interface cooked (0x808ac94) (Virtual) [2]
==================================
Virtual name : Cooked mode capture
Attached  : 1 (Dummy / 0x808ab3c)
Device    : NET_COOKED (0x808497c)

Interface eth0 (0x808adec) (Ethernet) [3]
===================================
Virtual interfaces attached to this : 4
Device    : zeth0 (0x80849b8)
IPv6 unicast addresses (max 4):
     fe80::5eff:fe00:53e6 autoconf preferred infinite
     2001:db8::1 manual preferred infinite
IPv4 unicast addresses (max 2):
     192.0.2.1/255.255.255.0 overridable preferred infinite

Interface net0 (0x808af44) (Virtual) [4]
==================================
Virtual name : Capture tunnel
Attached  : 3 (Ethernet / 0x808adec)
Device    : IP_TUNNEL0 (0x8084990)
IPv6 unicast addresses (max 4):
     2001:db8:200::1 manual preferred infinite
     fe80::efed:6dff:fef2:b1df autoconf preferred infinite
     fe80::56da:1eff:fe5e:bc02 autoconf preferred infinite
```

In this example, the `192.0.2.2` is the address of the outer end point of the
host that terminates the tunnel. Zephyr uses this address to select the
internal interface to use for the tunnel. In this example it is interface 3.

The interface 2 is a virtual interface that runs on top of interface 1. The
cooked capture packets are written by the capture API to sink interface 1.
The packets propagate to interface 2 because it is linked to the first interface.
The `net capture enable 2` net-shell command will cause the packets sent to
interface 2 to be written to capture interface 4, which in turn then capsulates
the packets and tunnels them to peer via the Ethernet interface 3.

The above IP addresses might change if you change the addresses in the
sample [samples/net/capture/overlay-tunnel.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/capture/overlay-tunnel.conf) file.

## [Sample usage](#id3)

See [Network packet capture](../../../samples/net/capture/README.md#net-capture "Capture network packets and send them to a remote host via IPIP tunnel.") sample application and
[Monitor Network Traffic](../network_monitoring.md#network-monitoring) for details.

## [API Reference](#id4)

Related code samples

[Network packet capture](../../../samples/net/capture/README.md#net-capture "Capture network packets and send them to a remote host via IPIP tunnel.")
:   Capture network packets and send them to a remote host via IPIP tunnel.

*group* Network packet capture
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
        :   - **dev** – Network capture device. If set to NULL, then the default capture device is used.

        Returns:
        :   True if enabled, False if network capture is disabled.

    static inline int net\_capture\_disable(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Disable network packet capturing support.

        Parameters:
        :   - **dev** – Network capture device

        Returns:
        :   0 if ok, <0 if network packet capture disable failed
