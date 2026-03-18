---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/net/sockets/packet/README.html
original_path: samples/net/sockets/packet/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Packet socket

## Overview

This sample is a simple packet socket application showing usage
of packet sockets over Ethernet. The sample prints every packet
received, and sends a dummy packet every 5 seconds.
The Zephyr network subsystem does not touch any of the headers
(L2, L3, etc.).

## Building and Running

When the application is run, it opens a packet socket and prints
the length of the packet it receives. After that it sends a dummy
packet every 5 seconds. You can use Wireshark to observe these
sent and received packets.

See the [net-tools](https://github.com/zephyrproject-rtos/net-tools) project for more details.

This sample can be built and executed on QEMU or native\_sim board as
described in [Networking with the host system](../../../../connectivity/networking/networking_with_host.md#networking-with-host).
