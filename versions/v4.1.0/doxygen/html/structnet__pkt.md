---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__pkt.html
original_path: doxygen/html/structnet__pkt.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_pkt Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Packet Library](group__net__pkt.md)

Network packet.
[More...](#details)

`#include <[net_pkt.h](net__pkt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [intptr\_t](stdint_8h.md#a0bd5dec00e345e69027427f8621d6a6c) | [fifo](#a96e82461f6786814de708049f2bc0b22) |
|  | The fifo is used by RX/TX threads and by socket layer. |
| struct k\_mem\_slab \* | [slab](#add4540bddb5c549a5ae61b99b14b0b54) |
|  | Slab pointer from where it belongs to. |
| union { |  |
| struct [net\_buf](structnet__buf.md) \*   [frags](#a1c27e50656b8c2713704d979b902c5d6) |  |
|  | buffer fragment [More...](#a1c27e50656b8c2713704d979b902c5d6) |
| struct [net\_buf](structnet__buf.md) \*   [buffer](#ad319458430aa691b88e24776e843d30b) |  |
|  | alias to a buffer fragment [More...](#ad319458430aa691b88e24776e843d30b) |
| }; |  |
|  | buffer holding the packet |
| struct net\_pkt\_cursor | [cursor](#a52f155a86698a929fa2130b594630d06) |
|  | Internal buffer iterator used for reading/writing. |
| struct [net\_context](structnet__context.md) \* | [context](#a4b9c3f62209f4d7748070224654360cf) |
|  | Network connection context. |
| struct [net\_if](structnet__if.md) \* | [iface](#a7590eeacf06469206cb7e7949acfa7b2) |
|  | Network interface. |

## Detailed Description

Network packet.

Note that if you add new fields into [net\_pkt](structnet__pkt.md "Network packet."), remember to update [net\_pkt\_clone()](group__net__pkt.md#gaefefe50d0c68fb4997abc7b309740959 "Clone pkt and its buffer.") function.

## Field Documentation

## [◆ ](#a76f873778e8c46f508a71d6c3a93f588)[union]

| union { ... } [net\_pkt](structnet__pkt.md) |
| --- |

buffer holding the packet

## [◆ ](#ad319458430aa691b88e24776e843d30b)buffer

| struct [net\_buf](structnet__buf.md)\* net\_pkt::buffer |
| --- |

alias to a buffer fragment

## [◆ ](#a4b9c3f62209f4d7748070224654360cf)context

| struct [net\_context](structnet__context.md)\* net\_pkt::context |
| --- |

Network connection context.

## [◆ ](#a52f155a86698a929fa2130b594630d06)cursor

| struct net\_pkt\_cursor net\_pkt::cursor |
| --- |

Internal buffer iterator used for reading/writing.

## [◆ ](#a96e82461f6786814de708049f2bc0b22)fifo

| [intptr\_t](stdint_8h.md#a0bd5dec00e345e69027427f8621d6a6c) net\_pkt::fifo |
| --- |

The fifo is used by RX/TX threads and by socket layer.

The [net\_pkt](structnet__pkt.md "Network packet.") is queued via fifo to the processing thread.

## [◆ ](#a1c27e50656b8c2713704d979b902c5d6)frags

| struct [net\_buf](structnet__buf.md)\* net\_pkt::frags |
| --- |

buffer fragment

## [◆ ](#a7590eeacf06469206cb7e7949acfa7b2)iface

| struct [net\_if](structnet__if.md)\* net\_pkt::iface |
| --- |

Network interface.

## [◆ ](#add4540bddb5c549a5ae61b99b14b0b54)slab

| struct k\_mem\_slab\* net\_pkt::slab |
| --- |

Slab pointer from where it belongs to.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_pkt.h](net__pkt_8h_source.md)

- [net\_pkt](structnet__pkt.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
