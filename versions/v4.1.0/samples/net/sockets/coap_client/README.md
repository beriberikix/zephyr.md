---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/net/sockets/coap_client/README.html
original_path: samples/net/sockets/coap_client/README.html
---

# CoAP client

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/coap_client/README.rst/..)

## Overview

This sample is a simple CoAP client showing how to retrieve information
from a resource.

This demo assumes that the platform of choice has networking support,
some adjustments to the configuration may be needed.

This sample will make a GET request with path ‘test’ to the IPv6
multicast address reserved for CoAP nodes, so the URI can be
represented as:

```text
coap://[ff02::fd]:5683/test
```

## Building and Running

This project will print all the octets of the response received, more context can
be obtained by using a tool such as tcpdump or wireshark.

See the [net-tools](https://github.com/zephyrproject-rtos/net-tools) project for more details.

This sample can be built and executed on QEMU or native\_sim board as described
in [Networking with the host system](../../../../connectivity/networking/networking_with_host.md#networking-with-host).

### Sample output

```shell
reply: 60 00 00 00 00 24 11 40 fe 80 00 00 00 00 00 00 5c 25 e2 ff fe
15 01 01 fe 80 00 00 00 00 00 00 5c 25 e2 ff fe 15 01 01 16 33 16 33
00 24 3d 86 60 40 00 01 ff 54 79 70 65 3a 20 30 0a 43 6f 64 65 3a 20
31 0a 4d 49 44 3a 20 31 0a (76 bytes)
```

## See also

[COAP Library](../../../../doxygen/html/group__coap.md)
