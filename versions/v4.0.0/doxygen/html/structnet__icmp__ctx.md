---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structnet__icmp__ctx.html
original_path: doxygen/html/structnet__icmp__ctx.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_icmp\_ctx Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Send and receive IPv4 or IPv6 ICMP Echo Request messages.](group__icmp.md)

ICMP context structure.
[More...](#details)

`#include <[icmp.h](icmp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a792d11b7dc74b0c064e5471f385028e5) |
|  | List node. |
| [net\_icmp\_handler\_t](group__icmp.md#ga0c3bd8147e4664ca0557ef0f118117ff) | [handler](#a9da78845a12a69a359087607e11f7e72) |
|  | ICMP response handler. |
| struct [net\_if](structnet__if.md) \* | [iface](#a88e1f3dc6118366f37ff5a110fff4b08) |
|  | Network interface where the ICMP request was sent. |
| void \* | [user\_data](#a2a718521d0b8c6de45c39fc8b45e47cf) |
|  | Opaque user supplied data. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [type](#ae7ccf9c7bbcc89d656d20e9486cf7df5) |
|  | ICMP type of the response we are waiting. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [code](#a8eaa061d7ade479523cfdbcb465f76b2) |
|  | ICMP code of the response type we are waiting. |

## Detailed Description

ICMP context structure.

## Field Documentation

## [◆ ](#a8eaa061d7ade479523cfdbcb465f76b2)code

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_icmp\_ctx::code |
| --- |

ICMP code of the response type we are waiting.

## [◆ ](#a9da78845a12a69a359087607e11f7e72)handler

| [net\_icmp\_handler\_t](group__icmp.md#ga0c3bd8147e4664ca0557ef0f118117ff) net\_icmp\_ctx::handler |
| --- |

ICMP response handler.

## [◆ ](#a88e1f3dc6118366f37ff5a110fff4b08)iface

| struct [net\_if](structnet__if.md)\* net\_icmp\_ctx::iface |
| --- |

Network interface where the ICMP request was sent.

## [◆ ](#a792d11b7dc74b0c064e5471f385028e5)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) net\_icmp\_ctx::node |
| --- |

List node.

## [◆ ](#ae7ccf9c7bbcc89d656d20e9486cf7df5)type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_icmp\_ctx::type |
| --- |

ICMP type of the response we are waiting.

## [◆ ](#a2a718521d0b8c6de45c39fc8b45e47cf)user\_data

| void\* net\_icmp\_ctx::user\_data |
| --- |

Opaque user supplied data.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[icmp.h](icmp_8h_source.md)

- [net\_icmp\_ctx](structnet__icmp__ctx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
