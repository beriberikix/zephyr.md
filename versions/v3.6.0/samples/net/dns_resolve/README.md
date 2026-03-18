---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/net/dns_resolve/README.html
original_path: samples/net/dns_resolve/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# DNS resolve

## Overview

This application will setup IP address for the device, and then
try to resolve various hostnames according to how the user has
configured the system.

- If IPv4 is enabled, then A record for `www.zephyrproject.org` is
  resolved.
- If IPv6 is enabled, then AAAA record for `www.zephyrproject.org` is
  resolved.
- If mDNS is enabled, then `zephyr.local` name is resolved.

## Requirements

- [Networking with the host system](../../../connectivity/networking/networking_with_host.md#networking-with-host)
- screen terminal emulator or equivalent.
- For most boards without ethernet, the ENC28J60 Ethernet module is required.
- dnsmasq application. The dnsmasq version used in this sample is:

```shell
dnsmasq -v
Dnsmasq version 2.76  Copyright (c) 2000-2016 Simon Kelley
```

## Building and Running

### Network Configuration

Open the project configuration file for your platform, for example:
`prj_frdm_k64f.conf` is the configuration file for the
[NXP FRDM-K64F](../../../boards/arm/frdm_k64f/doc/index.md#frdm-k64f) board.

In this sample application, both static or DHCPv4 IP addresses are supported.
Static IP addresses are specified in the project configuration file,
for example:

```shell
CONFIG_NET_CONFIG_MY_IPV6_ADDR="2001:db8::1"
CONFIG_NET_CONFIG_PEER_IPV6_ADDR="2001:db8::2"
```

are the IPv6 addresses for the DNS client running Zephyr and the DNS server,
respectively.

### DNS server

The dnsmasq tool may be used for testing purposes. Sample dnsmasq start
script can be downloaded from the zephyrproject-rtos/net-tools project area:
[https://github.com/zephyrproject-rtos/net-tools](https://github.com/zephyrproject-rtos/net-tools)

Open a terminal window and type:

```shell
$ cd net-tools
$ sudo ./dnsmasq.sh
```

The default project configurations settings for this sample uses the public
Google DNS servers. In order to use the local dnsmasq server, please edit
the appropriate ‘prj.conf’ file and update the DNS server addresses. For
instance, if using the usual IP addresses assigned to testing, update them
to the following values:

```shell
CONFIG_DNS_SERVER1="192.0.2.2:5353"
CONFIG_DNS_SERVER2="[2001:db8::2]:5353"
```

Note

DNS uses port 53 by default, but the dnsmasq.conf file provided by
net-tools uses port 5353 to allow executing the daemon without
superuser privileges.

If dnsmasq fails to start with an error like this:

```shell
dnsmasq: failed to create listening socket for port 5353: Address already in use
```

Open a terminal window and type:

```shell
$ killall -s KILL dnsmasq
```

Try to launch the dnsmasq application again.

For testing mDNS, use Avahi script in net-tools project:

```shell
$ cd net-tools
$ ./avahi-daemon.sh
```

### LLMNR Responder

If you want Zephyr to respond to a LLMNR DNS request that Windows host is
sending, then following config options could be set:

```shell
CONFIG_NET_HOSTNAME_ENABLE=y
CONFIG_NET_HOSTNAME="zephyr-device"
CONFIG_DNS_RESOLVER=y
CONFIG_LLMNR_RESPONDER=y
```

A Zephyr host needs a hostname assigned to it so that it can respond to a DNS
query. Note that the hostname should not have any dots in it.

### QEMU x86

To use QEMU for testing, follow the [Networking with QEMU](../../../connectivity/networking/qemu_setup.md#networking-with-qemu) guide.

### FRDM K64F

Open a terminal window and type:

```shell
west build -b frdm_k64f samples/net/dns_resolve
west flash
```

See [Freedom-K64F board documentation](../../../boards/arm/frdm_k64f/doc/index.md#frdm-k64f) for more information
about this board.

Open a terminal window and type:

```shell
$ screen /dev/ttyACM0 115200
```

Use ‘dmesg’ to find the right USB device.

Once the binary is loaded into the FRDM board, press the RESET button.
