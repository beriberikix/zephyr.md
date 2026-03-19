---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/net/sockets/echo_service/README.html
original_path: samples/net/sockets/echo_service/README.html
---

# Echo server (service)

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/echo_service/README.rst/..)

## Overview

The sockets/echo\_service sample application for Zephyr implements a TCP echo
server supporting both IPv4 and IPv6 and using a BSD Sockets compatible API.

The purpose of this sample is to show how to use socket service API.
The socket service is a concept where many blocking sockets can be listened by
one thread, and which can then trigger a callback if there is activity in the set
of sockets. This saves memory as only one thread needs to be created in the
system.

The application supports IPv4 and IPv6, and both UDP and TCP are also supported.
The source code for this sample application can be found at:
[samples/net/sockets/echo\_service](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/echo_service).

## Requirements

- [Networking with the host system](../../../../connectivity/networking/networking_with_host.md#networking-with-host)
- or, a board with hardware networking

## Building and Running

Build the Zephyr version of the sockets/echo\_service application like this:

```shell
west build -b <board_to_use> samples/net/sockets/echo_service
```

After the sample starts, it expects connections at 192.0.2.1, or 2001:db8::1
and port 4242.
The easiest way to connect is:

```shell
$ telnet 192.0.2.1 4242
```

After a connection is made, the application will echo back any line sent
to it. The application implements a single-threaded server using blocking
sockets, and currently is only implemented to serve only one client connection
at time. After the current client disconnects, the next connection can proceed.

## See also

[BSD Sockets compatible API](../../../../doxygen/html/group__bsd__sockets.md)
