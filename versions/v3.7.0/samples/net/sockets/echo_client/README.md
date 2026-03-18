---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/net/sockets/echo_client/README.html
original_path: samples/net/sockets/echo_client/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Echo client (advanced)

## Overview

The echo-client sample application for Zephyr implements a UDP/TCP client
that will send IPv4 or IPv6 packets, wait for the data to be sent back,
and then verify it matches the data that was sent.

The source code for this sample application can be found at:
[samples/net/sockets/echo\_client](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/echo_client).

## Requirements

- [Networking with the host system](../../../../connectivity/networking/networking_with_host.md#networking-with-host)

## Building and Running

There are multiple ways to use this application. One of the most common
usage scenario is to run echo-client application inside QEMU. This is
described in [Networking with QEMU](../../../../connectivity/networking/qemu_setup.md#networking-with-qemu).

There are configuration files for different boards and setups in the
echo-client directory:

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

Build echo-client sample application like this:

```shell
west build -b <board to use> samples/net/sockets/echo_client -- -DCONF_FILE=<config file to use>
```

Example building for the nrf52840dk/nrf52840 with OpenThread support:

```shell
west build -b nrf52840dk/nrf52840 samples/net/sockets/echo_client -- -DCONF_FILE="prj.conf overlay-ot.conf"
west build -t run
```

Example building for the IEEE 802.15.4 RF2XX transceiver:

```shell
west build -b [samr21_xpro | sam4s_xplained | sam_v71_xult/samv71q21] samples/net/sockets/echo_client -- -DEXTRA_CONF_FILE=overlay-802154.conf
west flash
```

In a terminal window you can check if communication is happen:

```shell
$ minicom -D /dev/ttyACM1
```

### Enabling TLS support

Enable TLS support in the sample by building the project with the
`overlay-tls.conf` overlay file enabled, for example, using these commands:

```shell
west build -b qemu_x86 samples/net/sockets/echo_client -- -DCONF_FILE="prj.conf overlay-tls.conf"
```

An alternative way is to specify `-DEXTRA_CONF_FILE=overlay-tls.conf` when
running `west build` or `cmake`.

The certificate and private key used by the sample can be found in the sample’s
`src` directory. The default certificates used by Socket Echo Client and
[Echo server (advanced)](../echo_server/README.md#sockets-echo-server "Implement a UDP/TCP server that sends received packets back to the sender.") enable establishing a secure connection
between the samples.

### SOCKS5 proxy support

It is also possible to connect to the echo-server through a SOCKS5 proxy.
To enable it, use `-DEXTRA_CONF_FILE=overlay-socks5.conf` when running `west
build` or `cmake`.

By default, to make the testing easier, the proxy is expected to run on the
same host as the echo-server in Linux host.

To start a proxy server, for example a builtin SOCKS server support in ssh
can be used (-D option). Use the following command to run it on your host
with the default port:

For IPv4 proxy server:

```shell
$ ssh -N -D 0.0.0.0:1080 localhost
```

For IPv6 proxy server:

```shell
$ ssh -N -D [::]:1080 localhost
```

Run both commands if you are testing IPv4 and IPv6.

To connect to a proxy server that is not running under the same IP as the
echo-server or uses a different port number, modify the following values
in echo\_client/src/tcp.c.

```c
#define SOCKS5_PROXY_V4_ADDR IPV4_ADDR
#define SOCKS5_PROXY_V6_ADDR IPV6_ADDR
#define SOCKS5_PROXY_PORT    1080
```

### Running echo-server in Linux Host

There is one useful testing scenario that can be used with Linux host.
Here echo-client is run in QEMU and echo-server is run in Linux host.

To use QEMU for testing, follow the [Networking with QEMU](../../../../connectivity/networking/qemu_setup.md#networking-with-qemu) guide.

In a terminal window:

```shell
$ sudo ./echo-server -i tap0
```

Run echo-client application in QEMU:

```shell
west build -b qemu_x86 samples/net/sockets/echo_client -- -DCONF_FILE="prj.conf overlay-linux.conf"
west build -t run
```

Note that echo-server must be running in the Linux host terminal window
before you start the echo-client application in QEMU.
Exit QEMU by pressing `CTRL+A` `x`.

You can verify TLS communication with a Linux host as well. See
[https://github.com/zephyrproject-rtos/net-tools](https://github.com/zephyrproject-rtos/net-tools) documentation for information
on how to test TLS with Linux host samples.

See the [Echo server (advanced)](../echo_server/README.md#sockets-echo-server "Implement a UDP/TCP server that sends received packets back to the sender.") documentation for an alternate
way of running, with the echo-client on the Linux host and the echo-server
in QEMU.
