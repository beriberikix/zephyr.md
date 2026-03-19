---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/net/sockets/echo_async/README.html
original_path: samples/net/sockets/echo_async/README.html
---

# Asynchronous echo server using poll()

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/echo_async/README.rst/..)

## Overview

The sockets/echo-async sample application for Zephyr implements an
asynchronous IPv4/IPv6 TCP echo server using a BSD Sockets compatible API
with non-blocking sockets and a `poll()` call. This is an extension of
the [Echo server (simple)](../echo/README.md#sockets-echo "Implements a simple IPv4/IPv6 TCP echo server using BSD sockets.") sample. It’s a more involved application,
supporting both IPv4 and IPv6 with concurrent connections, limiting
maximum number of simultaneous connections, and basic error handling.

The source code for this sample application can be found at:
[samples/net/sockets/echo\_async](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/echo_async).

## Requirements

- [Networking with the host system](../../../../connectivity/networking/networking_with_host.md#networking-with-host)
- or, a board with hardware networking (including 6LoWPAN)

## Building and Running

Build the Zephyr version of the sockets/echo\_async application like this:

```shell
west build -b <board_to_use> samples/net/sockets/echo_async
```

After the sample starts, it expects connections at 192.0.2.1 (IPv4), or
2001:db8::1 (IPv6), port 4242. The easiest way to connect is:

```shell
$ telnet 192.0.2.1 4242     # use this for IPv4
$ telnet 2001:db8::1 4242   # or this for IPv6
```

After a connection is made, the application will echo back any line sent to
it. Unlike the above-mentioned [Echo server (simple)](../echo/README.md#sockets-echo "Implements a simple IPv4/IPv6 TCP echo server using BSD sockets.") sample, this application
supports multiple concurrent client connections. You can open
another terminal window and run the same telnet command as above.
The sample supports up to three connected clients, but this can be adjusted
by changing `NUM_FDS` defined in the source code.

### Wi-Fi

The IPv4 Wi-Fi support can be enabled in the sample with
[Wi-Fi snippet](../../../../snippets/wifi-ipv4/README.md#snippet-wifi-ipv4).

### Running application on POSIX Host

The same application source code can be built for a POSIX system, e.g.
Linux. (Note: if you look at the source, you will see that the code is
the same except the header files are different for Zephyr vs POSIX, and
there’s an additional option to set for Linux to make a socket IPv6-only).

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
$ telnet 127.0.0.1 4242   # use this for IPv4
$ telnet ::1 4242         # or this for IPv6
```

As can be seen, the behavior of the application is the same as the Zephyr
version.

## See also

[BSD Sockets compatible API](../../../../doxygen/html/group__bsd__sockets.md)
