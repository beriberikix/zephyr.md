---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/net/sockets/http_get/README.html
original_path: samples/net/sockets/http_get/README.html
---

# HTTP GET using plain sockets

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/http_get/README.rst/..)

## Overview

The sockets/http\_get sample application for Zephyr implements a simple
HTTP GET client using a BSD Sockets compatible API. The purpose of this
sample is to show how it’s possible to develop a sockets application
portable to both POSIX and Zephyr. As such, it is kept minimal and
supports only IPv4.

The source code for this sample application can be found at:
[samples/net/sockets/http\_get](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_get).

## Requirements

- [Networking with the host system](../../../../connectivity/networking/networking_with_host.md#networking-with-host)
- or, a board with hardware networking
- NAT/routing should be set up to allow connections to the Internet
- DNS server should be available on the host to resolve domain names

## Building and Running

Build the Zephyr version of the application like this:

```shell
west build -b <board_to_use> samples/net/sockets/http_get
```

After the sample starts, it issues HTTP GET request to “google.com:80”
and dumps the response. You can edit the source code to issue a request
to any other site on the Internet (or on the local network, in which
case no NAT/routing setup is needed).
Exit QEMU by pressing `CTRL`+`A` `x`.

### Enabling TLS support

Enable TLS support in the sample by building the project with the
`overlay-tls.conf` overlay file enabled, for example, using these commands:

```shell
west build -b qemu_x86 samples/net/sockets/http_get -- -DCONF_FILE="prj.conf overlay-tls.conf"
```

An alternative way is to specify `-DEXTRA_CONF_FILE=overlay-tls.conf` when
running `west build` or `cmake`.

For boards that support TLS offloading (e.g. TI’s cc3220sf\_launchxl), use
`overlay-tls-offload.conf` instead of `overlay-tls.conf`.

The certificate used by the sample can be found in the sample’s `src`
directory. The certificate was selected to enable access to the default website
configured in the sample ([https://google.com](https://google.com)). To access a different web page
over TLS, provide an appropriate certificate to authenticate to that web server.

Note, that TLS support in the sample depends on non-posix, TLS socket
functionality. Therefore, it is only possible to run TLS in this sample
on Zephyr.

### Wi-Fi

The IPv4 Wi-Fi support can be enabled in the sample with
[Wi-Fi snippet](../../../../snippets/wifi-ipv4/README.md#snippet-wifi-ipv4).

### Running application on POSIX Host

The same application source code can be built for a POSIX system, e.g.
Linux. (Note: if you look at the source, you will see that the code is
the same except the header files are different for Zephyr vs POSIX.)

To build:

```shell
$ make -f Makefile.host
```

To run:

```shell
$ ./http_get
```

As can be seen, the behavior of the application is the same as the Zephyr
version.

## See also

[BSD Sockets compatible API](../../../../doxygen/html/group__bsd__sockets.md)

[TLS credentials management](../../../../doxygen/html/group__tls__credentials.md)

[Socket options for TLS](../../../../doxygen/html/group__secure__sockets__options.md)
