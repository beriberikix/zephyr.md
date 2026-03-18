---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/net/sockets/dumb_http_server_mt/README.html
original_path: samples/net/sockets/dumb_http_server_mt/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Dumb HTTP server (multi-threaded)

## Overview

The `sockets/dumb_http_server_mt` sample application for Zephyr implements a
skeleton HTTP server using a BSD Sockets compatible API.
This sample has similar functionality as [Dumb HTTP server](../dumb_http_server/README.md#socket-dumb-http-server "Implement a simple, portable, HTTP server using BSD sockets.")
except it has support for multiple simultaneous connections, TLS and
IPv6. Also this sample application has no compatibility with POSIX.
This HTTP server example is very minimal and does not really parse an incoming
HTTP request, just reads and discards it, and always serves a single static
page.

The source code for this sample application can be found at:
[samples/net/sockets/dumb\_http\_server\_mt](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/dumb_http_server_mt).

## Requirements

- [Networking with the host system](../../../../connectivity/networking/networking_with_host.md#networking-with-host)
- or, a board with hardware networking

## Building and Running

Build the Zephyr version of the sockets/dumb\_http\_server\_mt application like
this:

```shell
west build -b <board_to_use> samples/net/sockets/dumb_http_server_mt
```

After the sample starts, it expects connections at 192.0.2.1 or 2001:db8::1,
port 8080. The easiest way to connect is by opening a following URL in a web
browser: http://192.0.2.1:8080/ or http://[2001:db8::1]:8080/
You should see a page with a sample content about Zephyr (captured at a
particular time from Zephyr’s web site, note that it may differ from the
content on the live Zephyr site).
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
