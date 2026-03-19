---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__icmp__offload.html
original_path: doxygen/html/structnet__icmp__offload.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_icmp\_offload Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Send and receive IPv4 or IPv6 ICMP Echo Request messages.](group__icmp.md)

ICMP offload context structure.
[More...](#details)

`#include <[icmp.h](icmp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#ae31036c45fac89b321fe2c62c06be0b3) |
|  | List node. |
| [net\_icmp\_handler\_t](group__icmp.md#ga0c3bd8147e4664ca0557ef0f118117ff) | [handler](#aad5c9913e8bf68a7453bc773c5784772) |
|  | ICMP response handler. |
| [net\_icmp\_offload\_ping\_handler\_t](group__icmp.md#ga2923024c2ab217eb6b0fb1371a597dde) | [ping\_handler](#ae28f8f6a0e15271b1f00b10abecdfc3e) |
|  | ICMP offloaded ping handler. |
| struct [net\_if](structnet__if.md) \* | [iface](#aeffe11b4701e58532e44b4cff37be680) |
|  | Offloaded network interface. |

## Detailed Description

ICMP offload context structure.

## Field Documentation

## [◆ ](#aad5c9913e8bf68a7453bc773c5784772)handler

| [net\_icmp\_handler\_t](group__icmp.md#ga0c3bd8147e4664ca0557ef0f118117ff) net\_icmp\_offload::handler |
| --- |

ICMP response handler.

Currently there is only one handler. This means that one offloaded ping request/response can be going on at the same time.

## [◆ ](#aeffe11b4701e58532e44b4cff37be680)iface

| struct [net\_if](structnet__if.md)\* net\_icmp\_offload::iface |
| --- |

Offloaded network interface.

## [◆ ](#ae31036c45fac89b321fe2c62c06be0b3)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) net\_icmp\_offload::node |
| --- |

List node.

## [◆ ](#ae28f8f6a0e15271b1f00b10abecdfc3e)ping\_handler

| [net\_icmp\_offload\_ping\_handler\_t](group__icmp.md#ga2923024c2ab217eb6b0fb1371a597dde) net\_icmp\_offload::ping\_handler |
| --- |

ICMP offloaded ping handler.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[icmp.h](icmp_8h_source.md)

- [net\_icmp\_offload](structnet__icmp__offload.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
