---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/net/dhcpv4_client/README.html
original_path: samples/net/dhcpv4_client/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# DHCPv4 client

## Overview

This application starts a DHCPv4 client, gets an IPv4 address from the
DHCPv4 server, and prints address, lease time, netmask and router
information to a serial console.

## Requirements

- [Networking with the host system](../../../connectivity/networking/networking_with_host.md#networking-with-host)

## Building and Running

### Running DHCPv4 client in Linux Host

These are instructions for how to use this sample application using
QEMU on a Linux host to negotiate IP address from DHCPv4 server running
on Linux host.

To use QEMU for testing, follow the [Networking with QEMU](../../../connectivity/networking/qemu_setup.md#networking-with-qemu) guide.

Here’s a sample server configuration file ‘/etc/dhcp/dhcpd.conf’
used to configure the DHCPv4 server:

```shell
log-facility local7;
default-lease-time 600;
max-lease-time 7200;

subnet 192.0.2.0 netmask 255.255.255.0 {
  range 192.0.2.10 192.0.2.100;
}
```

Use another terminal window to start up a DHCPv4 server on the Linux host,
using this conf file:

```shell
$ sudo dhcpd -d -4 -cf /etc/dhcp/dhcpd.conf -lf /var/lib/dhcp/dhcpd.leases tap0
```

Run Zephyr samples/net/dhcpv4\_client application in QEMU:

```shell
west build -b qemu_x86 samples/net/dhcpv4_client
west build -t run
```

Once DHCPv4 client address negotiation completed with server, details
are shown like this:

```shell
[dhcpv4] [INF] main: In main
[dhcpv4] [INF] main_thread: Run dhcpv4 client
[dhcpv4] [INF] handler: Your address: 192.0.2.10
[dhcpv4] [INF] handler: Lease time: 600
[dhcpv4] [INF] handler: Subnet: 255.255.255.0
[dhcpv4] [INF] handler: Router: 0.0.0.0
```

To verify the Zephyr application client is running and has received
an ip address by typing:

```shell
$ ping -I tap0 192.0.2.10
```

### FRDM\_K64F

These are instructions for how to use this sample application running on
[NXP FRDM-K64F](../../../boards/arm/frdm_k64f/doc/index.md#frdm-k64f) board to negotiate IP address from DHCPv4 server running on
Linux host.

Connect ethernet cable from [Freedom-K64F board](../../../boards/arm/frdm_k64f/doc/index.md#frdm-k64f) to Linux host
machine and check for new interfaces:

```shell
$ ifconfig
```

Add ip address and routing information to interface:

```shell
$ sudo ip addr add 192.0.2.2 dev eth1
$ sudo ip route add 192.0.2.0/24 dev eth1
```

Here’s a sample server configuration file ‘/etc/dhcpd/dhcp.conf’
used to configure the DHCPv4 server:

```shell
log-facility local7;
default-lease-time 600;
max-lease-time 7200;

subnet 192.0.2.0 netmask 255.255.255.0 {
  range 192.0.2.10 192.0.2.100;
}
```

Use another terminal window to start up a DHCPv4 server on the Linux host,
using this conf file:

```shell
$ sudo dhcpd -d -4 -cf /etc/dhcp/dhcpd.conf -lf /var/lib/dhcp/dhcpd.leases eth1
```

Build Zephyr samples/net/dhcpv4\_client application:

```shell
west build -b frdm_k64f samples/net/dhcpv4_client
west flash
```

Once DHCPv4 client address negotiation completed with server, details
are shown like this:

```shell
$ sudo screen /dev/ttyACM0 115200
[dhcpv4] [INF] main: In main
[dhcpv4] [INF] main_thread: Run dhcpv4 client
[dhcpv4] [INF] handler: Your address: 192.0.2.10
[dhcpv4] [INF] handler: Lease time: 600
[dhcpv4] [INF] handler: Subnet: 255.255.255.0
[dhcpv4] [INF] handler: Router: 0.0.0.0
```

To verify the Zephyr application client is running and has received
an ip address by typing:

```shell
$ ping -I eth1 192.0.2.10
```

### Arm FVP

- [Arm FVP BaseR AEMv8-R](../../../boards/arm64/fvp_baser_aemv8r/doc/index.md#fvp-baser-aemv8r)
- [ARM BASE RevC AEMv8A Fixed Virtual Platforms](../../../boards/arm64/fvp_base_revc_2xaemv8a/doc/index.md#fvp-base-revc-2xaemv8a)

This sample application running on Arm FVP board can negotiate IP
address from DHCPv4 server running on Arm FVP, so there is no extra
configuration that needed to do. It can be build and run directly.

Build Zephyr samples/net/dhcpv4\_client application:

```shell
west build -b fvp_baser_aemv8r samples/net/dhcpv4_client
west build -t run
```

Once DHCPv4 client address negotiation completed with server, details
are shown like this:

```shell
uart:~$
[00:00:00.060,000] <inf> phy_mii: PHY (0) ID 16F840

[00:00:00.170,000] <inf> phy_mii: PHY (0) Link speed 10 Mb, half duplex

[00:00:00.170,000] <inf> eth_smsc91x: MAC 00:02:f7:ef:37:16
*** Booting Zephyr OS build zephyr-v3.2.0-4300-g3e6505dba29e ***
[00:00:00.170,000] <inf> net_dhcpv4_client_sample: Run dhcpv4 client
[00:00:00.180,000] <inf> net_dhcpv4_client_sample: Start on ethernet@9a000000: index=1
[00:00:07.180,000] <inf> net_dhcpv4: Received: 172.20.51.1
[00:00:07.180,000] <inf> net_dhcpv4_client_sample:    Address[1]: 172.20.51.1
[00:00:07.180,000] <inf> net_dhcpv4_client_sample:     Subnet[1]: 255.255.255.0
[00:00:07.180,000] <inf> net_dhcpv4_client_sample:     Router[1]: 172.20.51.254
[00:00:07.180,000] <inf> net_dhcpv4_client_sample: Lease time[1]: 86400 seconds
```
