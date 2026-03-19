---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/net/virtual/README.html
original_path: samples/net/virtual/README.html
---

# Virtual network interface

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/virtual/README.rst/..)

## Overview

This sample application creates a sample virtual network interface for
demonstrative purposes, it does not do anything useful here.
There are total 4 network interfaces.

Ethernet network interface is providing the real network interface and
all the virtual interfaces are running on top of it.

On top of Ethernet interface there are two virtual network interfaces,
one provides only IPv6 tunnel, and the other only IPv4. These two tunnels
are provided by IPIP tunnel.

The sample provides tunnel interface which runs on top of the IPv6 tunnel.

The source code for this sample application can be found at:
[samples/net/virtual](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/virtual).

## Requirements

- [Networking with the host system](../../../connectivity/networking/networking_with_host.md#networking-with-host)

## Building and Running

The [net-tools](https://github.com/zephyrproject-rtos/net-tools) project provides a configuration that can be used
to create a sample tunnels in host side.

```shell
net-setup.sh -c zeth-tunnel.conf
```

Note that the sample application expects that the board provides
an Ethernet network interface. Build the sample application like this:

```shell
west build -b <board to use> samples/net/virtual
```

## See also

[Virtual Network Interface Support Functions](../../../doxygen/html/group__virtual.md)

[Virtual Interface Library](../../../doxygen/html/group__virtual__mgmt.md)
