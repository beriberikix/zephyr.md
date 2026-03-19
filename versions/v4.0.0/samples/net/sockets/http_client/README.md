---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/net/sockets/http_client/README.html
original_path: samples/net/sockets/http_client/README.html
---

# HTTP Client

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/http_client/README.rst/..)

## Overview

This sample application implements an HTTP(S) client that will do an HTTP
or HTTPS request and wait for the response from the HTTP server.

The source code for this sample application can be found at:
[samples/net/sockets/http\_client](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_client).

## Requirements

- [Networking with the host system](../../../../connectivity/networking/networking_with_host.md#networking-with-host)

## Building and Running

You can use this application on a supported board, including
running it inside QEMU as described in [Networking with QEMU](../../../../connectivity/networking/qemu_setup.md#networking-with-qemu).

Build the http-client sample application like this:

```shell
west build -b <board to use> samples/net/sockets/http_client -- -DCONF_FILE=<config file to use>
```

### Enabling TLS support

Enable TLS support in the sample by building the project with the
`overlay-tls.conf` overlay file enabled using these commands:

```shell
west build -b qemu_x86 samples/net/sockets/http_client -- -DCONF_FILE="prj.conf overlay-tls.conf"
```

An alternative way is to specify `-DEXTRA_CONF_FILE=overlay-tls.conf` when
running `west build` or `cmake`.

The certificate and private key used by the sample can be found in the sample’s
[samples/net/sockets/http\_client/src/](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_client/src/) directory.
The default certificates used by Socket HTTP Client and `https-server.py`
program found in the [net-tools](https://github.com/zephyrproject-rtos/net-tools) project, enable establishing a secure
connection between the samples.

### Running http-server in Linux Host

You can run this `http-client` sample application in QEMU
and run the `http-server.py` (from net-tools) on a Linux host.

To use QEMU for testing, follow the [Networking with QEMU](../../../../connectivity/networking/qemu_setup.md#networking-with-qemu) guide.

In a terminal window:

```shell
$ ./http-server.py
```

Run `http-client` application in QEMU:

```shell
west build -b qemu_x86 samples/net/sockets/http_client -- -DCONF_FILE=prj.conf
west build -t run
```

Note that `http-server.py` must be running in the Linux host terminal window
before you start the http-client application in QEMU.
Exit QEMU by pressing `CTRL`+`A` `x`.

You can verify TLS communication with a Linux host as well. Just use the
`https-server.py` program in net-tools project.

## See also

[BSD Sockets compatible API](../../../../doxygen/html/group__bsd__sockets.md)

[HTTP client API](../../../../doxygen/html/group__http__client.md)

[TLS credentials management](../../../../doxygen/html/group__tls__credentials.md)

[Socket options for TLS](../../../../doxygen/html/group__secure__sockets__options.md)
