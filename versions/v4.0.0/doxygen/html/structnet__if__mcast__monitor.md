---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structnet__if__mcast__monitor.html
original_path: doxygen/html/structnet__if__mcast__monitor.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_if\_mcast\_monitor Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Interface abstraction layer](group__net__if.md)

Multicast monitor handler struct.
[More...](#details)

`#include <[net_if.h](net__if_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a570b7d8a8a5fabca83982a5f7d1d896a) |
|  | Node information for the slist. |
| struct [net\_if](structnet__if.md) \* | [iface](#af4d0e937b2b9161918a13a0d6723c60a) |
|  | Network interface. |
| [net\_if\_mcast\_callback\_t](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5) | [cb](#aec441b858a5f6792ac9cdbc625f6babe) |
|  | Multicast callback. |

## Detailed Description

Multicast monitor handler struct.

Stores the multicast callback information. Caller must make sure that the variable pointed by this is valid during the lifetime of registration. Typically this means that the variable cannot be allocated from stack.

## Field Documentation

## [◆ ](#aec441b858a5f6792ac9cdbc625f6babe)cb

| [net\_if\_mcast\_callback\_t](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5) net\_if\_mcast\_monitor::cb |
| --- |

Multicast callback.

## [◆ ](#af4d0e937b2b9161918a13a0d6723c60a)iface

| struct [net\_if](structnet__if.md)\* net\_if\_mcast\_monitor::iface |
| --- |

Network interface.

## [◆ ](#a570b7d8a8a5fabca83982a5f7d1d896a)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) net\_if\_mcast\_monitor::node |
| --- |

Node information for the slist.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_if.h](net__if_8h_source.md)

- [net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
