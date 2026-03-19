---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/net/sockets/dumb_http_server/README.html
original_path: samples/net/sockets/dumb_http_server/README.html
---

# Dumb HTTP server

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/dumb_http_server/README.rst/..)

## Overview

The sockets/dumb\_http\_server sample application for Zephyr implements a
skeleton HTTP server using a BSD Sockets compatible API. The purpose of
this sample is to show how it’s possible to develop a sockets application
portable to both POSIX and Zephyr. As such, this HTTP server example is
kept very minimal and does not really parse an incoming HTTP request,
just reads and discards it, and always serve a single static page. Even
with such simplification, it is useful as an example of a socket
application which can be accessed via a conventional web browser, or to
perform performance/regression testing using existing HTTP diagnostic
tools.

The source code for this sample application can be found at:
[samples/net/sockets/dumb\_http\_server](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/dumb_http_server).

## Requirements

- [Networking with the host system](../../../../connectivity/networking/networking_with_host.md#networking-with-host)
- or, a board with hardware networking

## Building and Running

Build the Zephyr version of the sockets/echo application like this:

```shell
west build -b <board_to_use> samples/net/sockets/dumb_http_server
```

After the sample starts, it expects connections at 192.0.2.1, port 8080.
The easiest way to connect is by opening a following URL in a web
browser: [http://192.0.2.1:8080/](http://192.0.2.1:8080/) . You should see a page with a sample
content about Zephyr (captured at a particular time from Zephyr’s web
site, note that it may differ from the content on the live Zephyr site).
Alternatively, a tool like `curl` can be used:

```shell
$ curl http://192.0.2.1:8080/
```

Finally, you can run an HTTP profiling/load tool like Apache Bench
(`ab`) against the server:

```text
$ ab -n10 http://192.0.2.1:8080/
```

`-n` parameter specifies the number of HTTP requests to issue against
a server.

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
$ ./socket_dumb_http
```

To test, connect to [http://127.0.0.1:8080/](http://127.0.0.1:8080/) , and follow the steps in the
previous section.

As can be seen, the behavior of the application is the same as the Zephyr
version.

## See also

[BSD Sockets compatible API](../../../../doxygen/html/group__bsd__sockets.md)

[Network Packet Library](../../../../doxygen/html/group__net__pkt.md)
