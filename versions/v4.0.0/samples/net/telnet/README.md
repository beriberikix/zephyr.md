---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/net/telnet/README.html
original_path: samples/net/telnet/README.html
---

# Telnet console

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/telnet/README.rst/..)

## Overview

This application will setup IPv4/IPv6 addresses on the default
network interface. The telnet console service is started transparently
by the kernel, along with the shell and two shell modules: net and kernel.
Once up and running, you can connect to the target over the network,
using a telnet client.

## Requirements

- [Networking with QEMU](../../../connectivity/networking/qemu_setup.md#networking-with-qemu)

## Building and Running

### QEMU x86

These are instructions for how to use this sample application using
QEMU on a Linux host connected to a network with DHCP service.

To use QEMU for testing, follow the [Networking with QEMU](../../../connectivity/networking/qemu_setup.md#networking-with-qemu) guide.

Run Zephyr samples/net/telnet application in QEMU:

```shell
west build -b qemu_x86 samples/net/telnet
west build -t run
```

Once started, you should see you IP address details for example:

```shell
[Setup] [INF] main: Starting Telnet sample
[Setup] [INF] setup_ipv4: IPv4 address: 192.0.2.1
[Setup] [INF] setup_ipv6: IPv6 address: 2001:db8::1
```

At this point, your QEMU guest is up and running. Connect to the telnet
console from your linux host this way:

```shell
$ telnet 192.0.2.1
Telnet escape character is '^]'.
Trying 192.0.2.1...
Connected to 192.0.2.1.
Escape character is '^]'.
```

Now type enter, the shell prompt will appear and you can enter commands,
for example `help`.

### Freedom-K64F Board

These are instructions for how to use this sample application running on a
Freedom-K64F board. Unlike running it on QEMU, [Freedom-K64F board](../../../boards/nxp/frdm_k64f/doc/index.md#frdm_k64f) network configuration for IPv4 will rely on DHCPv4. You cad modify
the `prj_frdm_k64f.conf` to set static IPv4 addresses if it is really needed.

For detailed instructions about building, flashing and using the serial console
logs, follow the [Freedom-K64F board](../../../boards/nxp/frdm_k64f/doc/index.md#frdm_k64f) documentation section.

Connect ethernet cable from [Freedom-K64F](../../../boards/nxp/frdm_k64f/doc/index.md#frdm_k64f) board to a
local network providing IPv4 address configuration via DHCPv4. Creating your own
DHCP server on a local network is not in the scope of this README.

Build Zephyr samples/net/telnet application:

```shell
west build -b frdm_k64f samples/net/telnet
```

Flash the resulting Zephyr binary following the [Freedom-K64F](../../../boards/nxp/frdm_k64f/doc/index.md#frdm_k64f)
board documentation noted above.

From your host computer, open a serial console to your board:

```shell
$ sudo screen /dev/ttyACM0 115200
```

Plug the Ethernet cable to the [Freedom-K64F](../../../boards/nxp/frdm_k64f/doc/index.md#frdm_k64f) board.
Reset the board, you should see first on the console:

```shell
[dev/eth_mcux] [INF] eth_0_init: Enabled 100M full-duplex mode.
[dev/eth_mcux] [DBG] eth_0_init: MAC 00:04:9f:69:c7:36
shell> [Setup] [INF] main: Starting Telnet sample
[Setup] [INF] setup_dhcpv4: Running dhcpv4 client...
[Setup] [INF] setup_ipv6: IPv6 address: 2001:db8::1
```

And if the DHCPv4 client succeeds, you will soon see something like:

```shell
[Setup] [INF] ipv4_addr_add_handler: IPv4 address: 192.168.0.21
[Setup] [INF] ipv4_addr_add_handler: Lease time: 86400 seconds
[Setup] [INF] ipv4_addr_add_handler: Subnet: 255.255.255.0
[Setup] [INF] ipv4_addr_add_handler: Router: 192.168.0.1
```

The above result depends on your local network.
At this point you should be able to connect via telnet over the network.
On your linux host:

```shell
$ telnet 192.168.0.21
Telnet escape character is '^]'.
Trying 192.168.0.21...
Connected to 192.168.0.1.
Escape character is '^]'.
```

You are now connected, and as for the UART console, you can type in
your commands and get the output through your telnet client.

### Wi-Fi

The IPv4 Wi-Fi support can be enabled in the sample with
[Wi-Fi snippet](../../../snippets/wifi-ipv4/README.md#snippet-wifi-ipv4).

## See also

[Shell API](../../../doxygen/html/group__shell__api.md)

[Network Core Library](../../../doxygen/html/group__net__core.md)

[Network Interface abstraction layer](../../../doxygen/html/group__net__if.md)

[Network Management](../../../doxygen/html/group__net__mgmt.md)
