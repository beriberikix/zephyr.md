---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/net/sockets/websocket_client/README.html
original_path: samples/net/sockets/websocket_client/README.html
---

# WebSocket Client

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/websocket_client/README.rst/..)

## Overview

This sample application implements a Websocket client that will do an HTTP
or HTTPS handshake request to HTTP server, then start to send data and wait for
the responses from the Websocket server.

The source code for this sample application can be found at:
[samples/net/sockets/websocket\_client](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/websocket_client).

## Requirements

- [Networking with the host system](../../../../connectivity/networking/networking_with_host.md#networking-with-host)

## Building and Running

You can use this application on a supported board, including
running it inside QEMU as described in [Networking with QEMU](../../../../connectivity/networking/qemu_setup.md#networking-with-qemu).

Build websocket-client sample application like this:

```shell
west build -b <board to use> samples/net/sockets/websocket_client -- -DCONF_FILE=<config file to use>
```

### Enabling TLS support

Enable TLS support in the sample by building the project with the
`overlay-tls.conf` overlay file enabled using these commands:

```shell
west build -b qemu_x86 samples/net/sockets/websocket_client -- -DCONF_FILE="prj.conf overlay-tls.conf"
```

An alternative way is to specify `-DEXTRA_CONF_FILE=overlay-tls.conf` when
running `west build` or `cmake`.

The certificate and private key used by the sample can be found in the sample’s
[samples/net/sockets/websocket\_client/src/](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/websocket_client/src/) directory.

### Running websocket-server in Linux Host

You can run this `websocket-client` sample application in QEMU
and run the `zephyr-websocket-server.py` (from net-tools) on a Linux host.
Other alternative is to install [websocketd](http://websocketd.com/) and
use that.

To use QEMU for testing, follow the [Networking with QEMU](../../../../connectivity/networking/qemu_setup.md#networking-with-qemu) guide.

In a terminal window you can do either:

```shell
$ ./zephyr-websocket-server.py
```

or

```shell
$ websocketd --port=9001 cat
```

Run `websocket-client` application in QEMU:

```shell
west build -b qemu_x86 samples/net/sockets/websocket_client -- -DCONF_FILE=prj.conf
west build -t run
```

Note that `zephyr-websocket-server.py` or `websocketd` must be running in
the Linux host terminal window before you start the `websocket-client`
application in QEMU. Exit QEMU by pressing `CTRL`+`A` `x`.

Current version of `zephyr-websocket-server.py` found in
[net-tools](https://github.com/zephyrproject-rtos/net-tools) project, does
not support TLS.

## See also

[BSD Sockets compatible API](../../../../doxygen/html/group__bsd__sockets.md)

[Websocket API](../../../../doxygen/html/group__websocket.md)
