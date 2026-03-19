---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/net/ipv4_autoconf/README.html
original_path: samples/net/ipv4_autoconf/README.html
---

# IPv4 autoconf client

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/ipv4_autoconf/README.rst/..)

## Overview

This sample application starts a IPv4 autoconf and self-assigns
a random IPv4 address in the 169.254.0.0/16 range, it defends
the IPv4 address and resolves IPv4 conflicts if multiple
parties try to allocate an identical address.

## Requirements

- [Networking with the host system](../../../connectivity/networking/networking_with_host.md#networking-with-host)

## Building and Running

These are instructions for how to use this sample application running
on a [FRDM-K64F](../../../boards/nxp/frdm_k64f/doc/index.md#frdm_k64f) board to configure a link local IPv4 address and
connect to a Linux host.

Connect ethernet cable from a [Freedom-K64F board](../../../boards/nxp/frdm_k64f/doc/index.md#frdm_k64f) to a Linux
host machine and check for new interfaces.

### Running Avahi client in Linux Host

Assign a IPv4 link local address to the interface in the Linux system

```shell
$ avahi-autoipd --force-bind -D eth0
```

### FRDM\_K64F

Build Zephyr the `samples/net/ipv4_autoconf` application using these
steps:

```shell
west build -b frdm_k64f samples/net/ipv4_autoconf
west flash
```

Once IPv4 LL has completed probing and announcement, details are shown like this:

```shell
$ sudo screen /dev/ttyACM0 115200
```

```shell
[ipv4ll] [INF] main: Run ipv4 autoconf client
[ipv4ll] [INF] handler: Your address: 169.254.218.128
```

Note that the IP address may change at each self assignment.

To verify the Zephyr application is running and has configured an IP address
type:

```shell
$ ping -I eth1 169.254.218.128
```

### Wi-Fi

The IPv4 Wi-Fi support can be enabled in the sample with
[Wi-Fi snippet](../../../snippets/wifi-ipv4/README.md#snippet-wifi-ipv4).

## See also

[Networking](../../../doxygen/html/group__networking.md)

[Network Interface abstraction layer](../../../doxygen/html/group__net__if.md)

[Application network context](../../../doxygen/html/group__net__context.md)

[Network Management](../../../doxygen/html/group__net__mgmt.md)
