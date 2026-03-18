---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/net_offload.html
original_path: connectivity/networking/api/net_offload.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Network Traffic Offloading

## [Network Offloading](#id2)

### [Overview](#id3)

The network offloading API provides hooks that a device vendor can use
to provide an alternate implementation for an IP stack. This means that the
actual network connection creation, data transfer, etc., is done in the vendor
HAL instead of the Zephyr network stack.

### [API Reference](#id4)

*group* Network Offloading Interface
:   Network offloading interface.

## [Socket Offloading](#id5)

### [Overview](#id6)

In addition to the network offloading API, Zephyr allows offloading of networking
functionality at the socket API level. With this approach, vendors who provide an
alternate implementation of the networking stack, exposing socket API for their
networking devices, can easily integrate it with Zephyr.

See [drivers/wifi/simplelink/simplelink\_sockets.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/simplelink/simplelink_sockets.c) for a sample
implementation on how to integrate network offloading at socket level.
