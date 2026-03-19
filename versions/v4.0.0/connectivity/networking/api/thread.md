---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/networking/api/thread.html
original_path: connectivity/networking/api/thread.html
---

# Thread protocol

## [Overview](#id1)

Thread is a low-power mesh networking technology, designed specifically for home
automation applications. It is an IPv6-based standard, which uses 6LoWPAN
technology over IEEE 802.15.4 protocol. IP connectivity lets you easily connect
a Thread mesh network to the internet with a Thread Border Router.

The Thread specification provides a high level of network security. Mesh networks
built with Thread are secure - only authenticated devices can join the network
and all communications within the mesh are encrypted. More information about
Thread protocol can be found at
[Thread Group website](https://www.threadgroup.org).

Zephyr integrates an open source Thread protocol implementation called OpenThread,
documented on the [OpenThread website](https://openthread.io/).

## [Internet connectivity](#id2)

A Thread Border Router is required to connect mesh network to the internet.
An open source implementation of Thread Border Router is provided by the OpenThread
community. See
[OpenThread Border Router guide](https://openthread.io/guides/border-router)
for instructions on how to set up a Border Router.

## [Sample usage](#id3)

You can try using OpenThread with the Zephyr Echo server and Echo client samples,
which provide out-of-the-box configuration for OpenThread. To enable OpenThread
support in these samples, build them with `overlay-ot.conf` overlay config file.
See [Echo server (advanced)](../../../samples/net/sockets/echo_server/README.md#sockets-echo-server "Implement a UDP/TCP server that sends received packets back to the sender.") and [Echo client (advanced)](../../../samples/net/sockets/echo_client/README.md#sockets-echo-client "Implement a client that sends IP packets, waits for data to be sent back, and verifies it.")
samples for details.

## [Thread related APIs](#id4)

### [OpenThread Driver API](#id5)

OpenThread L2 uses Zephyr’s protocol agnostic IEEE 802.15.4 driver API
internally. This API is of interest to **driver developers** that want to
support OpenThread.

The driver API is part of the [IEEE 802.15.4 Driver API](ieee802154.md#ieee802154-driver-api) subsystem and
documented there.

### [OpenThread L2 Adaptation Layer API](#id6)

Zephyr’s OpenThread L2 platform adaptation layer glues the external OpenThread
stack together with Zephyr’s IEEE 802.15.4 protocol agnostic driver API. This
API is of interest to OpenThread L2 **subsystem contributors** only.

[OpenThread L2 abstraction layer](../../../doxygen/html/group__openthread.md)

Related code samples

- [OpenThread co-processor](../../../samples/net/openthread/coprocessor/README.md#coprocessor "Build a Thread border-router using OpenThread's co-processor designs.")Build a Thread border-router using OpenThread's co-processor designs.
