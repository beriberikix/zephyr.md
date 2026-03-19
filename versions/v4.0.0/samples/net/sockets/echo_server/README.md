---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/net/sockets/echo_server/README.html
original_path: samples/net/sockets/echo_server/README.html
---

# Echo server (advanced)

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/echo_server/README.rst/..)

## Overview

The echo-server sample application for Zephyr implements a UDP/TCP server
that complements the echo-client sample application: the echo-server listens
for incoming IPv4 or IPv6 packets (sent by the echo client) and simply sends
them back.

The source code for this sample application can be found at:
[samples/net/sockets/echo\_server](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/echo_server).

## Requirements

- [Networking with the host system](../../../../connectivity/networking/networking_with_host.md#networking-with-host)

## Building and Running

There are multiple ways to use this application. One of the most common
usage scenario is to run echo-server application inside QEMU. This is
described in [Networking with QEMU](../../../../connectivity/networking/qemu_setup.md#networking-with-qemu).

There are configuration files for different boards and setups in the
echo-server directory:

- `prj.conf`
  Generic config file, normally you should use this.
- `overlay-ot.conf`
  This overlay config enables support for OpenThread.
- `overlay-802154.conf`
  This overlay config enables support for native IEEE 802.15.4 connectivity.
  Note, that by default IEEE 802.15.4 L2 uses unacknowledged communication. To
  improve connection reliability, acknowledgments can be enabled with shell
  command: `ieee802154 ack set`.
- `overlay-qemu_802154.conf`
  This overlay config enables support for two QEMU’s when simulating
  IEEE 802.15.4 network that are connected together.
- `overlay-tls.conf`
  This overlay config enables support for TLS.
- `overlay-tunnel.conf`
  This overlay config enables support for IP tunneling.

Build echo-server sample application like this:

```shell
west build -b <board to use> samples/net/sockets/echo_server -- -DCONF_FILE=<config file to use>
```

Example building for the nrf52840dk/nrf52840 with OpenThread support:

```shell
west build -b nrf52840dk/nrf52840 samples/net/sockets/echo_server -- -DCONF_FILE="prj.conf overlay-ot.conf"
west build -t run
```

Example building for the samr21\_xpro with RF2XX driver support:

```shell
west build -b [samr21_xpro | sam4e_xpro | sam_v71_xult/samv71q21] samples/net/sockets/echo_server -- -DEXTRA_CONF_FILE=overlay-802154.conf
west flash
```

In a terminal window you can check if communication is happen:

```shell
$ minicom -D /dev/ttyACM0
```

### Enabling TLS support

Enable TLS support in the sample by building the project with the
`overlay-tls.conf` overlay file enabled, for example, using these commands:

```shell
west build -b qemu_x86 samples/net/sockets/echo_server -- -DCONF_FILE="prj.conf overlay-tls.conf"
```

An alternative way is to specify `-DEXTRA_CONF_FILE=overlay-tls.conf` when
running `west build` or `cmake`.

The certificate used by the sample can be found in the sample’s `src`
directory. The default certificates used by Socket Echo Server and
[Echo client (advanced)](../echo_client/README.md#sockets-echo-client "Implement a client that sends IP packets, waits for data to be sent back, and verifies it.") enable establishing a secure connection
between the samples.

### Running echo-client in Linux Host

There is one useful testing scenario that can be used with Linux host.
Here echo-server is run in QEMU and echo-client is run in Linux host.

To use QEMU for testing, follow the [Networking with QEMU](../../../../connectivity/networking/qemu_setup.md#networking-with-qemu) guide.

Run echo-server application in QEMU:

```shell
west build -b qemu_x86 samples/net/sockets/echo_server
west build -t run
```

In a terminal window:

```shell
$ sudo ./echo-client -i tap0 2001:db8::1
```

Note that echo-server must be running in QEMU before you start the
echo-client application in host terminal window.

You can verify TLS communication with a Linux host as well. See
[https://github.com/zephyrproject-rtos/net-tools](https://github.com/zephyrproject-rtos/net-tools) documentation for information
on how to test TLS with Linux host samples.

See the [Echo client (advanced)](../echo_client/README.md#sockets-echo-client "Implement a client that sends IP packets, waits for data to be sent back, and verifies it.") sample documentation for an alternate
way of running, with the echo-server on the Linux host and the echo-client
in QEMU.

## See also

[BSD Sockets compatible API](../../../../doxygen/html/group__bsd__sockets.md)

[TLS credentials management](../../../../doxygen/html/group__tls__credentials.md)
