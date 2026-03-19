---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/networking/network_tracing.html
original_path: connectivity/networking/network_tracing.html
---

# Network Tracing

User can enable network core stack and socket API calls tracing.

The [`CONFIG_TRACING_NET_CORE`](../../kconfig.md#CONFIG_TRACING_NET_CORE "CONFIG_TRACING_NET_CORE") option controls the core network
stack tracing. This option is enabled by default if tracing and networking
are enabled. The system will start to collect the receiving and sending call
verdicts i.e., whether the network packet was successfully sent or received.
It will also collect packet sending or receiving timings i.e., how long
it took to deliver the network packet, and the network interface, priority
and traffic class used.

The [`CONFIG_TRACING_NET_SOCKETS`](../../kconfig.md#CONFIG_TRACING_NET_SOCKETS "CONFIG_TRACING_NET_SOCKETS") option can be used to track
BSD socket call usage in the system. It is enabled if tracing and BSD socket
API support are enabled. The system will start to collect what BSD socket
API calls are made and what parameters the API calls are using and returning.

See the [tracing documentation](../../services/tracing/index.md#tracing) for how to use the tracing
service.
