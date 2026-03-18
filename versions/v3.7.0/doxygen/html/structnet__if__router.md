---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structnet__if__router.html
original_path: doxygen/html/structnet__if__router.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_if\_router Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Interface abstraction layer](group__net__if.md)

Information about routers in the system.
[More...](#details)

`#include <[net_if.h](net__if_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#aabbac0cd0a59ca0eafdcfc0eaf5d909a) |
|  | Slist lifetime timer node. |
| struct net\_addr | [address](#a86a2ca1b95e348acbde8ce90986b83db) |
|  | IP address. |
| struct [net\_if](structnet__if.md) \* | [iface](#a03789aa0a40f7686b76616de0ca0401a) |
|  | Network interface the router is connected to. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [life\_start](#adf4f4c722917b3c30f8c73bc2519957f) |
|  | Router life timer start. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [lifetime](#a4b0d2ad8f225ab61022c10dfce3db199) |
|  | Router lifetime. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [is\_used](#a7196e6d2bc2c958d98dfe29143a62048): 1 |
|  | Is this router used or not. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [is\_default](#a34745207edcad2745d6ce311e2bf1894): 1 |
|  | Is default router. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [is\_infinite](#a4cb47f30241ae3d410f56f1487254ed0): 1 |
|  | Is the router valid forever. |

## Detailed Description

Information about routers in the system.

Stores the router information.

## Field Documentation

## [◆ ](#a86a2ca1b95e348acbde8ce90986b83db)address

| struct net\_addr net\_if\_router::address |
| --- |

IP address.

## [◆ ](#a03789aa0a40f7686b76616de0ca0401a)iface

| struct [net\_if](structnet__if.md)\* net\_if\_router::iface |
| --- |

Network interface the router is connected to.

## [◆ ](#a34745207edcad2745d6ce311e2bf1894)is\_default

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_if\_router::is\_default |
| --- |

Is default router.

## [◆ ](#a4cb47f30241ae3d410f56f1487254ed0)is\_infinite

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_if\_router::is\_infinite |
| --- |

Is the router valid forever.

## [◆ ](#a7196e6d2bc2c958d98dfe29143a62048)is\_used

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_if\_router::is\_used |
| --- |

Is this router used or not.

## [◆ ](#adf4f4c722917b3c30f8c73bc2519957f)life\_start

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_if\_router::life\_start |
| --- |

Router life timer start.

## [◆ ](#a4b0d2ad8f225ab61022c10dfce3db199)lifetime

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_if\_router::lifetime |
| --- |

Router lifetime.

## [◆ ](#aabbac0cd0a59ca0eafdcfc0eaf5d909a)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) net\_if\_router::node |
| --- |

Slist lifetime timer node.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_if.h](net__if_8h_source.md)

- [net\_if\_router](structnet__if__router.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
