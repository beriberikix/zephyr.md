---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/net/ipv4_autoconf/README.html
original_path: samples/net/ipv4_autoconf/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# IPv4 autoconf client

## Overview

This sample application starts a IPv4 autoconf and self-assigns
a random IPv4 address in the 169.254.0.0/16 range, it defends
the IPv4 address and resolves IPv4 conflicts if multiple
parties try to allocate an identical address.

## Requirements

- [Networking with the host system](../../../connectivity/networking/networking_with_host.md#networking-with-host)

## Building and Running

These are instructions for how to use this sample application running
on a [NXP FRDM-K64F](../../../boards/arm/frdm_k64f/doc/index.md#frdm-k64f) board to configure a link local IPv4 address and
connect to a Linux host.

Connect ethernet cable from a [Freedom-K64F board](../../../boards/arm/frdm_k64f/doc/index.md#frdm-k64f) to a Linux
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
