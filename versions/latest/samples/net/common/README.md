---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/samples/net/common/README.html
original_path: samples/net/common/README.html
---

# Overview

Various network samples can utilize common code to enable generic
features like VLAN support.

The source code for the common sample can be found at:
[samples/net/common](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/common).

# VLAN

If you want to enable VLAN support to network sample application,
then add `overlay-vlan.conf` to your sample application compilation
like in this example for echo-server sample application:

```shell
west build -b native_sim samples/net/sockets/echo_server -- -DCONF_FILE="prj.conf overlay-vlan.conf"
west build -t run
```

You host setup for the VLAN can be done like this:

```shell
$ cd tools/net-setup
$ ./net-setup.sh -c zeth-vlan.conf
```

The example configuration will create this kind of configuration:

- In host side:

  - Normal `zeth` interface is created. It has `192.0.2.2/24`
    address. All the network traffic to Zephyr will go through this
    interface.
  - VLAN interface `vlan.100` is used for VLAN tag 100 network traffic.
    It has `198.51.100.2` IPv4 and `2001:db8:100::2` IPv6 addresses.
  - VLAN interface `vlan.200` is used for VLAN tag 200 network traffic.
    It has `203.0.113.2` IPv4 and `2001:db8:200::2` IPv6 addresses.
- The network interfaces and addresses in Zephyr side:

  - The `eth0` is the main interface, it has `192.0.2.1/24`
    address and it has connection to the host.
  - The `VLAN-100` is a virtual interface for VLAN tag 100 traffic.
    It has `198.51.100.1/24` IPv4 and `2001:db8:100::1/64` addresses.
  - The `VLAN-200` is a virtual interface for VLAN tag 200 traffic.
    It has `203.0.113.1/24` IPv4 and `2001:db8:200::1/64` addresses.

Warning

The IPv4 and IPv6 addresses used in the samples are not to be used
in any live network and are only meant for these network samples.
These IPv4 and IPv6 addresses are meant for documentation use only and
are not routable.
