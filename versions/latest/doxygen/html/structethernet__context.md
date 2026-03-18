---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structethernet__context.html
original_path: doxygen/html/structethernet__context.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ethernet\_context Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Ethernet Support Functions](group__ethernet.md)

Ethernet L2 context that is needed for VLAN.
[More...](#details)

`#include <[ethernet.h](ethernet_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [flags](#a800f7b276341771addd3f1f1ffb5329b) |
|  | Flags representing ethernet state, which are accessed from multiple threads. |
| struct [k\_work](structk__work.md) | [carrier\_work](#a4c152bdc054a3e86a5baedcf4e8eed1d) |
|  | Carrier ON/OFF handler worker. |
| struct [net\_if](structnet__if.md) \* | [iface](#a2358d48d02192220f2621dd96e353f37) |
|  | Network interface. |
| enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) | [ethernet\_l2\_flags](#a49f0358828531ab6e3cc398ebaf6f6f9) |
|  | This tells what L2 features does ethernet support. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [is\_net\_carrier\_up](#a483abbb2e14fea59b01d6ee74466c702): 1 |
|  | Is network carrier up. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [is\_init](#ab7ea3afc9bd0ac19893d4a7edf2be057): 1 |
|  | Is this context already initialized. |
| enum [ethernet\_if\_types](group__ethernet.md#ga139cc696837611a522b289f2ea7bf6fc) | [eth\_if\_type](#a81e35df9b1648c1e2dc6234bb2eb2d76) |
|  | Types of Ethernet network interfaces. |

## Detailed Description

Ethernet L2 context that is needed for VLAN.

## Field Documentation

## [◆ ](#a4c152bdc054a3e86a5baedcf4e8eed1d)carrier\_work

| struct [k\_work](structk__work.md) ethernet\_context::carrier\_work |
| --- |

Carrier ON/OFF handler worker.

This is used to create network interface UP/DOWN event when ethernet L2 driver notices carrier ON/OFF situation. We must not create another network management event from inside management handler thus we use worker thread to trigger the UP/DOWN event.

## [◆ ](#a81e35df9b1648c1e2dc6234bb2eb2d76)eth\_if\_type

| enum [ethernet\_if\_types](group__ethernet.md#ga139cc696837611a522b289f2ea7bf6fc) ethernet\_context::eth\_if\_type |
| --- |

Types of Ethernet network interfaces.

## [◆ ](#a49f0358828531ab6e3cc398ebaf6f6f9)ethernet\_l2\_flags

| enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) ethernet\_context::ethernet\_l2\_flags |
| --- |

This tells what L2 features does ethernet support.

## [◆ ](#a800f7b276341771addd3f1f1ffb5329b)flags

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) ethernet\_context::flags |
| --- |

Flags representing ethernet state, which are accessed from multiple threads.

## [◆ ](#a2358d48d02192220f2621dd96e353f37)iface

| struct [net\_if](structnet__if.md)\* ethernet\_context::iface |
| --- |

Network interface.

## [◆ ](#ab7ea3afc9bd0ac19893d4a7edf2be057)is\_init

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ethernet\_context::is\_init |
| --- |

Is this context already initialized.

## [◆ ](#a483abbb2e14fea59b01d6ee74466c702)is\_net\_carrier\_up

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ethernet\_context::is\_net\_carrier\_up |
| --- |

Is network carrier up.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ethernet.h](ethernet_8h_source.md)

- [ethernet\_context](structethernet__context.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
