---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/networking/network_monitoring.html
original_path: connectivity/networking/network_monitoring.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Monitor Network Traffic

It is useful to be able to monitor the network traffic especially when
debugging a connectivity issues or when developing new protocol support in
Zephyr. This page describes how to set up a way to capture network traffic so
that user is able to use Wireshark or similar tool in remote host to see the
network packets sent or received by a Zephyr device.

See also the [Network packet capture](../../samples/net/capture/README.md#net-capture "Capture network packets and send them to a remote host via IPIP tunnel.") sample application from the Zephyr
source distribution for configuration options that need to be enabled.

## [Host Configuration](#id1)

The instructions here describe how to setup a Linux host to capture Zephyr
network RX and TX traffic. Similar instructions should work also in other
operating systems.
On the Linux Host, fetch the Zephyr `net-tools` project, which is located
in a separate Git repository:

```shell
git clone https://github.com/zephyrproject-rtos/net-tools
```

The `net-tools` project provides a configure file to setup IP-to-IP tunnel
interface so that we can transfer monitoring data from Zephyr to host.

In terminal #1, type:

```shell
./net-setup.sh -c zeth-tunnel.conf
```

This script will create following IPIP tunnel interfaces:

| Interface name | Description |
| --- | --- |
| `zeth-ip6ip` | IPv6-over-IPv4 tunnel |
| `zeth-ipip` | IPv4-over-IPv4 tunnel |
| `zeth-ipip6` | IPv4-over-IPv6 tunnel |
| `zeth-ip6ip6` | IPv6-over-IPv6 tunnel |

Zephyr will send captured network packets to one of these interfaces.
The actual interface will depend on how the capturing is configured.
You can then use Wireshark to monitor the proper network interface.

After the tunneling interfaces have been created, you can use for example
`net-capture.py` script from `net-tools` project to print or save the
captured network packets. The `net-capture.py` provides an UDP listener,
it can print the captured data to screen and optionally can also save the
data to a pcap file.

```shell
$ ./net-capture.py -i zeth-ip6ip -w capture.pcap
[20210408Z14:33:08.959589] Ether / IP / ICMP 192.0.2.1 > 192.0.2.2 echo-request 0 / Raw
[20210408Z14:33:08.976178] Ether / IP / ICMP 192.0.2.2 > 192.0.2.1 echo-reply 0 / Raw
[20210408Z14:33:16.176303] Ether / IPv6 / ICMPv6 Echo Request (id: 0x9feb seq: 0x0)
[20210408Z14:33:16.195326] Ether / IPv6 / ICMPv6 Echo Reply (id: 0x9feb seq: 0x0)
[20210408Z14:33:21.194979] Ether / IPv6 / ICMPv6ND_NS / ICMPv6 Neighbor Discovery Option - Source Link-Layer Address 02:00:5e:00:53:3b
[20210408Z14:33:21.217528] Ether / IPv6 / ICMPv6ND_NA / ICMPv6 Neighbor Discovery Option - Destination Link-Layer Address 00:00:5e:00:53:ff
[20210408Z14:34:10.245408] Ether / IPv6 / UDP 2001:db8::2:47319 > 2001:db8::1:4242 / Raw
[20210408Z14:34:10.266542] Ether / IPv6 / UDP 2001:db8::1:4242 > 2001:db8::2:47319 / Raw
```

The `net-capture.py` has following command line options:

```shell
Listen captured network data from Zephyr and save it optionally to pcap file.
./net-capture.py \
     -i | --interface <network interface>
             Listen this interface for the data
     [-p | --port <UDP port>]
             UDP port (default is 4242) where the capture data is received
     [-q | --quiet]
             Do not print packet information
     [-t | --type <L2 type of the data>]
             Scapy L2 type name of the UDP payload, default is Ether
     [-w | --write <pcap file name>]
             Write the received data to file in PCAP format
```

Instead of the `net-capture.py` script, you can for example use `netcat`
to provide an UDP listener so that the host will not send port unreachable
message to Zephyr:

```shell
nc -l -u 2001:db8:200::2 4242 > /dev/null
```

The IP address above is the inner tunnel endpoint, and can be changed and
it depends on how the Zephyr is configured. Zephyr will send UDP packets
containing the captured network packets to the configured IP tunnel, so we
need to terminate the network connection like this.

## [Zephyr Configuration](#id2)

In this example, we use the `native_sim` board. You can also use any other board
that supports networking.

In terminal #3, type:

```shell
west build -b native_sim samples/net/capture -- -DCONFIG_NATIVE_UART_AUTOATTACH_DEFAULT_CMD=\""gnome-terminal -- screen %s"\"
```

To see the Zephyr console and shell, start Zephyr instance like this:

```shell
build/zephyr/zephyr.exe -attach_uart
```

Any other application can be used too, just make sure that suitable
configuration options are enabled (see `samples/net/capture/prj.conf` file
for examples).

The network capture can be configured automatically if needed, but
currently the `capture` sample application does not do that. User has to use
`net-shell` to setup and enable the monitoring.

The network packet monitoring needs to be setup first. The `net-shell` has
`net capture setup` command for doing that. The command syntax is

```shell
net capture setup <remote-ip-addr> <local-ip-addr> <peer-ip-addr>
     <remote> is the (outer) endpoint IP address
     <local> is the (inner) local IP address
     <peer> is the (inner) peer IP address
     Local and Peer IP addresses can have UDP port number in them (optional)
     like 198.0.51.2:9000 or [2001:db8:100::2]:4242
```

In Zephyr console, type:

```shell
net capture setup 192.0.2.2 2001:db8:200::1 2001:db8:200::2
```

This command will create the tunneling interface. The `192.0.2.2` is the
remote host where the tunnel is terminated. The address is used to select
the local network interface where the tunneling interface is attached to.
The `2001:db8:200::1` tells the local IP address for the tunnel,
the `2001:db8:200::2` is the peer IP address where the captured network
packets are sent. The port numbers for UDP packet can be given in the
setup command like this for IPv6-over-IPv4 tunnel

```shell
net capture setup 192.0.2.2 [2001:db8:200::1]:9999 [2001:db8:200::2]:9998
```

and like this for IPv4-over-IPv4 tunnel

```shell
net capture setup 192.0.2.2 198.51.100.1:9999 198.51.100.2:9998
```

If the port number is omitted, then `4242` UDP port is used as a default.

The current monitoring configuration can be checked like this:

```shell
uart:~$ net capture
Network packet capture disabled
                Capture  Tunnel
Device          iface    iface   Local                  Peer
NET_CAPTURE0    -        1      [2001:db8:200::1]:4242  [2001:db8:200::2]:4242
```

which will print the current configuration. As we have not yet enabled
monitoring, the `Capture iface` is not set.

Then we need to enable the network packet monitoring like this:

```shell
net capture enable 2
```

The `2` tells the network interface which traffic we want to capture. In
this example, the `2` is the `native_sim` board Ethernet interface.
Note that we send the network traffic to the same interface that we are
monitoring in this example. The monitoring system avoids to capture already
captured network traffic as that would lead to recursion.
You can use `net iface` command to see what network interfaces are available.
Note that you cannot capture traffic from the tunnel interface as that would
cause recursion loop.
The captured network traffic can be sent to some other network interface
if configured so. Just set the `<remote-ip-addr>` option properly in
`net capture setup` so that the IP tunnel is attached to desired network
interface.
The capture status can be checked again like this:

```shell
uart:~$ net capture
Network packet capture enabled
                Capture  Tunnel
Device          iface    iface   Local                  Peer
NET_CAPTURE0    2        1      [2001:db8:200::1]:4242  [2001:db8:200::2]:4242
```

After enabling the monitoring, the system will send captured (either received
or sent) network packets to the tunnel interface for further processing.

The monitoring can be disabled like this:

```shell
net capture disable
```

which will turn currently running monitoring off. The monitoring setup can
be cleared like this:

```shell
net capture cleanup
```

It is not necessary to use `net-shell` for configuring the monitoring.
The [network capture API](api/capture.md#net-capture-interface) functions can be called
by the application if needed.

## [Wireshark Configuration](#id3)

The [Wireshark](https://www.wireshark.org/) tool can be used to monitor the
captured network traffic in a useful way.

You can monitor either the tunnel interfaces or the `zeth` interface.
In order to see the actual captured data inside an UDP packet,
see [Wireshark decapsulate UDP](https://osqa-ask.wireshark.org/questions/28138/decoding-ethernet-encapsulated-in-tcp-or-udp/) document for instructions.
