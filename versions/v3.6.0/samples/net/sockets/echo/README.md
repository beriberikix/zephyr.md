---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/net/sockets/echo/README.html
original_path: samples/net/sockets/echo/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Echo server (simple)

## Overview

The sockets/echo sample application for Zephyr implements a TCP echo
server supporting both IPv4 and IPv6 and using a BSD Sockets compatible API.
The purpose of this sample is to show how it’s possible to develop a sockets
application portable to both POSIX and Zephyr. As such, it is kept minimal
and supports only IPv4, IPv6 and TCP.

The source code for this sample application can be found at:
[samples/net/sockets/echo](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/echo).

## Requirements

- [Networking with the host system](../../../../connectivity/networking/networking_with_host.md#networking-with-host)
- or, a board with hardware networking

## Building and Running

Build the Zephyr version of the sockets/echo application like this:

```shell
west build -b <board_to_use> samples/net/sockets/echo
```

After the sample starts, it expects connections at 192.0.2.1, port 4242.
The easiest way to connect is:

```shell
$ telnet 192.0.2.1 4242
```

After a connection is made, the application will echo back any line sent
to it. The application implements a single-threaded server using blocking
sockets, and thus can serve only one client connection at time. After the
current client disconnects, the next connection can proceed.

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
$ ./socket_echo
```

To test:

```shell
$ telnet 127.0.0.1 4242
```

As can be seen, the behavior of the application is the same as the Zephyr
version.

### Running on cc3220sf\_launchxl

See the note on Provisioning and Fast Connect in [CC3220SF LaunchXL](../../../../boards/arm/cc3220sf_launchxl/doc/index.md#cc3220sf-launchxl).

After having connected to an Access Point using the sample Wi-Fi shell,
the IP address will be printed to the console upon running this echo
application.

Proceed to test as above.
