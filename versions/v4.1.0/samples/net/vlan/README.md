---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/net/vlan/README.html
original_path: samples/net/vlan/README.html
---

# Virtual LAN

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/vlan/README.rst/..)

## Overview

The VLAN sample application for Zephyr will setup two virtual LAN networks.
The application sample enables net-shell and allows users to view VLAN settings.

The source code for this sample application can be found at:
[samples/net/vlan](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/vlan).

## Requirements

- [Networking with the host system](../../../connectivity/networking/networking_with_host.md#networking-with-host)

## Building and Running

A good way to run this VLAN application is with QEMU as described in
[Networking with QEMU Ethernet](../../../connectivity/networking/qemu_eth_setup.md#networking-with-eth-qemu). You can use `zeth-vlan.conf` configuration
file when running `net-setup.sh` script in Linux like this:

```shell
./net-setup.sh -c zeth-vlan.conf
```

Note that VLAN is only supported for boards that have an ethernet port or
that support USB networking.

Follow these steps to build the VLAN sample application:

```shell
west build -b <board to use> samples/net/vlan -- -DCONF_FILE=prj.conf
```

The default configuration file [samples/net/vlan/prj.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/vlan/prj.conf) creates
two virtual LAN networks with these settings:

- VLAN tag 100: IPv4 198.51.100.1 and IPv6 2001:db8:100::1
- VLAN tag 200: IPv4 203.0.113.1 and IPv6 2001:db8:200::1

### Setting up Linux Host

The [samples/net/vlan/vlan-setup-linux.sh](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/vlan/vlan-setup-linux.sh) provides a script that
can be executed on the Linux host. It creates two VLAN interfaces `vlan.100`
and `vlan.200` on the Linux host and creates routes to Zephyr.

If everything is configured correctly, you will be able to successfully execute
the following commands on the Linux host.

```shell
ping -c 1 2001:db8:100::1
ping -c 1 198.51.100.1
ping -c 1 2001:db8:200::1
ping -c 1 203.0.113.1
```

The network packets to `2001:db8:100::1` or `198.51.100.1` will have VLAN
tag 100 set to them. The vlan tag 200 will be set to network packets to
`2001:db8:200::1` or `203.0.113.1`.

## See also

[Virtual LAN definitions and helpers](../../../doxygen/html/group__vlan__api.md)

[Network L2 Abstraction Layer](../../../doxygen/html/group__net__l2.md)

[Network Interface abstraction layer](../../../doxygen/html/group__net__if.md)
