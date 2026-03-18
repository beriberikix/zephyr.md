---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/networking_with_multiple_instances.html
original_path: connectivity/networking/networking_with_multiple_instances.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Networking with multiple Zephyr instances

This page describes how to set up a virtual network between multiple
Zephyr instances. The Zephyr instances could be running inside QEMU
or could be native\_sim board processes. The Linux host can be used
to route network traffic between these systems.

## [Prerequisites](#id1)

On the Linux Host, fetch the Zephyr `net-tools` project, which is located
in a separate Git repository:

```shell
git clone https://github.com/zephyrproject-rtos/net-tools
```

## [Basic Setup](#id2)

For the steps below, you will need five terminal windows:

- Terminal #1 and #2 are terminal windows with net-tools being the current
  directory (`cd net-tools`)
- Terminal #3, where you setup bridging in Linux host
- Terminal #4 and #5 are your usual Zephyr development terminal,
  with the Zephyr environment initialized.

As there are multiple ways to setup the Zephyr network, the example below uses
`qemu_x86` board with `e1000` Ethernet controller and native\_sim board
to simplify the setup instructions. You can use other QEMU boards and drivers
if needed, see [Networking with QEMU Ethernet](qemu_eth_setup.md#networking-with-eth-qemu) for details. You can also use
two or more native\_sim board Zephyr instances and connect them together.

### [Step 1 - Create configuration files](#id3)

Before starting QEMU with network connectivity, a network interfaces for each
Zephyr instance should be created in the host system. The default setup for
creating network interface cannot be used here as that is for connecting one
Zephyr instance to Linux host.

For Zephyr instance #1, create file called `zephyr1.conf` to `net-tools`
project, or to some other suitable directory.

```shell
# Configuration file for setting IP addresses for a network interface.
INTERFACE="$1"
HWADDR="00:00:5e:00:53:11"
IPV6_ADDR_1="2001:db8:100::2"
IPV6_ROUTE_1="2001:db8:100::/64"
IPV4_ADDR_1="198.51.100.2/24"
IPV4_ROUTE_1="198.51.100.0/24"
ip link set dev $INTERFACE up
ip link set dev $INTERFACE address $HWADDR
ip -6 address add $IPV6_ADDR_1 dev $INTERFACE nodad
ip -6 route add $IPV6_ROUTE_1 dev $INTERFACE
ip address add $IPV4_ADDR_1 dev $INTERFACE
ip route add $IPV4_ROUTE_1 dev $INTERFACE > /dev/null 2>&1
```

For Zephyr instance #2, create file called `zephyr2.conf` to `net-tools`
project, or to some other suitable directory.

```shell
# Configuration file for setting IP addresses for a network interface.
INTERFACE="$1"
HWADDR="00:00:5e:00:53:22"
IPV6_ADDR_1="2001:db8:200::2"
IPV6_ROUTE_1="2001:db8:200::/64"
IPV4_ADDR_1="203.0.113.2/24"
IPV4_ROUTE_1="203.0.113.0/24"
ip link set dev $INTERFACE up
ip link set dev $INTERFACE address $HWADDR
ip -6 address add $IPV6_ADDR_1 dev $INTERFACE nodad
ip -6 route add $IPV6_ROUTE_1 dev $INTERFACE
ip address add $IPV4_ADDR_1 dev $INTERFACE
ip route add $IPV4_ROUTE_1 dev $INTERFACE > /dev/null 2>&1
```

### [Step 2 - Create Ethernet interfaces](#id4)

The following `net-setup.sh` commands should be typed in net-tools
directory (`cd net-tools`).

In terminal #1, type:

```shell
./net-setup.sh -c zephyr1.conf -i zeth.1
```

In terminal #2, type:

```shell
./net-setup.sh -c zephyr2.conf -i zeth.2
```

### [Step 3 - Setup network bridging](#id5)

In terminal #3, type:

```shell
sudo brctl addbr zeth-br
sudo brctl addif zeth-br zeth.1
sudo brctl addif zeth-br zeth.2
sudo ifconfig zeth-br up
```

### [Step 4 - Start Zephyr instances](#id6)

In this example we start [Echo server (advanced)](../../samples/net/sockets/echo_server/README.md#sockets-echo-server "Implement a UDP/TCP server that sends received packets back to the sender.") and
[Echo client (advanced)](../../samples/net/sockets/echo_client/README.md#sockets-echo-client "Implement a client that sends IP packets, waits for data to be sent back, and verifies it.") sample applications. You can use other applications
too as needed.

In terminal #4, if you are using QEMU, type this:

```shell
west build -d build/server -b qemu_x86 -t run \
   samples/net/sockets/echo_server -- \
   -DEXTRA_CONF_FILE=overlay-e1000.conf \
   -DCONFIG_NET_CONFIG_MY_IPV4_ADDR=\"198.51.100.1\" \
   -DCONFIG_NET_CONFIG_PEER_IPV4_ADDR=\"203.0.113.1\" \
   -DCONFIG_NET_CONFIG_MY_IPV6_ADDR=\"2001:db8:100::1\" \
   -DCONFIG_NET_CONFIG_PEER_IPV6_ADDR=\"2001:db8:200::1\" \
   -DCONFIG_NET_CONFIG_MY_IPV4_GW=\"203.0.113.1\" \
   -DCONFIG_ETH_QEMU_IFACE_NAME=\"zeth.1\" \
   -DCONFIG_ETH_QEMU_EXTRA_ARGS=\"mac=00:00:5e:00:53:01\"
```

or if you want to use native\_sim board, type this:

```shell
west build -d build/server -b native_sim -t run \
   samples/net/sockets/echo_server -- \
   -DCONFIG_NET_CONFIG_MY_IPV4_ADDR=\"198.51.100.1\" \
   -DCONFIG_NET_CONFIG_PEER_IPV4_ADDR=\"203.0.113.1\" \
   -DCONFIG_NET_CONFIG_MY_IPV6_ADDR=\"2001:db8:100::1\" \
   -DCONFIG_NET_CONFIG_PEER_IPV6_ADDR=\"2001:db8:200::1\" \
   -DCONFIG_NET_CONFIG_MY_IPV4_GW=\"203.0.113.1\" \
   -DCONFIG_ETH_NATIVE_POSIX_DRV_NAME=\"zeth.1\" \
   -DCONFIG_ETH_NATIVE_POSIX_MAC_ADDR=\"00:00:5e:00:53:01\" \
   -DCONFIG_ETH_NATIVE_POSIX_RANDOM_MAC=n
```

In terminal #5, if you are using QEMU, type this:

```shell
west build -d build/client -b qemu_x86 -t run \
   samples/net/sockets/echo_client -- \
   -DEXTRA_CONF_FILE=overlay-e1000.conf \
   -DCONFIG_NET_CONFIG_MY_IPV4_ADDR=\"203.0.113.1\" \
   -DCONFIG_NET_CONFIG_PEER_IPV4_ADDR=\"198.51.100.1\" \
   -DCONFIG_NET_CONFIG_MY_IPV6_ADDR=\"2001:db8:200::1\" \
   -DCONFIG_NET_CONFIG_PEER_IPV6_ADDR=\"2001:db8:100::1\" \
   -DCONFIG_NET_CONFIG_MY_IPV4_GW=\"198.51.100.1\" \
   -DCONFIG_ETH_QEMU_IFACE_NAME=\"zeth.2\" \
   -DCONFIG_ETH_QEMU_EXTRA_ARGS=\"mac=00:00:5e:00:53:02\"
```

or if you want to use native\_sim board, type this:

```shell
west build -d build/client -b native_sim -t run \
   samples/net/sockets/echo_client -- \
   -DCONFIG_NET_CONFIG_MY_IPV4_ADDR=\"203.0.113.1\" \
   -DCONFIG_NET_CONFIG_PEER_IPV4_ADDR=\"198.51.100.1\" \
   -DCONFIG_NET_CONFIG_MY_IPV6_ADDR=\"2001:db8:200::1\" \
   -DCONFIG_NET_CONFIG_PEER_IPV6_ADDR=\"2001:db8:100::1\" \
   -DCONFIG_NET_CONFIG_MY_IPV4_GW=\"198.51.100.1\" \
   -DCONFIG_ETH_NATIVE_POSIX_DRV_NAME=\"zeth.2\" \
   -DCONFIG_ETH_NATIVE_POSIX_MAC_ADDR=\"00:00:5e:00:53:02\" \
   -DCONFIG_ETH_NATIVE_POSIX_RANDOM_MAC=n
```

Also if you have firewall enabled in your host, you need to allow traffic
between `zeth.1`, `zeth.2` and `zeth-br` interfaces.
