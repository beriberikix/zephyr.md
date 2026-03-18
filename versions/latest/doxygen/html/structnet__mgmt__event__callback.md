---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnet__mgmt__event__callback.html
original_path: doxygen/html/structnet__mgmt__event__callback.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_mgmt\_event\_callback Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Management](group__net__mgmt.md)

Network Management event callback structure Used to register a callback into the network management event part, in order to let the owner of this struct to get network event notification based on given event mask.
[More...](#details)

`#include <[net_mgmt.h](net__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a05a4f445731f9f72209a652f2653e1ea) |
|  | Meant to be used internally, to insert the callback into a list. |
| union { |  |
| [net\_mgmt\_event\_handler\_t](group__net__mgmt.md#gadb876a681fe7f5fb6d2709015625a67f)   [handler](#ada57aabc8acc3e9be93fb2726321f1b2) |  |
|  | Actual callback function being used to notify the owner. [More...](#ada57aabc8acc3e9be93fb2726321f1b2) |
| struct k\_sem \*   [sync\_call](#a7403d98fe528c492a4b1b449b43c10d3) |  |
|  | Semaphore meant to be used internally for the synchronous [net\_mgmt\_event\_wait()](group__net__mgmt.md#gacbaa95c65717747d802dc80eb745aa17 "Used to wait synchronously on an event mask.") function. [More...](#a7403d98fe528c492a4b1b449b43c10d3) |
| }; |  |
| union { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [event\_mask](#acd2d06e59f71b30e6d9089c165c4a589) |  |
|  | A mask of network events on which the above handler should be called in case those events come. [More...](#acd2d06e59f71b30e6d9089c165c4a589) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [raised\_event](#a7c92da4524db9294d9a157606b85c497) |  |
|  | Internal place holder when a synchronous event wait is successfully unlocked on a event. [More...](#a7c92da4524db9294d9a157606b85c497) |
| }; |  |
|  | A mask of network events on which the above handler should be called in case those events come. |

## Detailed Description

Network Management event callback structure Used to register a callback into the network management event part, in order to let the owner of this struct to get network event notification based on given event mask.

## Field Documentation

## [◆ ](#a729c499ebef52b08828ab0cfe939135e)[union]

| union { ... } [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) |
| --- |

A mask of network events on which the above handler should be called in case those events come.

Such mask can be modified whenever necessary by the owner, and thus will affect the handler being called or not.

## [◆ ](#a0306812b62c4176ef0fafbc4f89d5f07)[union]

| union { ... } [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) |
| --- |

## [◆ ](#acd2d06e59f71b30e6d9089c165c4a589)event\_mask

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_mgmt\_event\_callback::event\_mask |
| --- |

A mask of network events on which the above handler should be called in case those events come.

Note that only the command part is treated as a mask, matching one to several commands. Layer and layer code will be made of an exact match. This means that in order to receive events from multiple layers, one must have multiple listeners registered, one for each layer being listened.

## [◆ ](#ada57aabc8acc3e9be93fb2726321f1b2)handler

| [net\_mgmt\_event\_handler\_t](group__net__mgmt.md#gadb876a681fe7f5fb6d2709015625a67f) net\_mgmt\_event\_callback::handler |
| --- |

Actual callback function being used to notify the owner.

## [◆ ](#a05a4f445731f9f72209a652f2653e1ea)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) net\_mgmt\_event\_callback::node |
| --- |

Meant to be used internally, to insert the callback into a list.

So nobody should mess with it.

## [◆ ](#a7c92da4524db9294d9a157606b85c497)raised\_event

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_mgmt\_event\_callback::raised\_event |
| --- |

Internal place holder when a synchronous event wait is successfully unlocked on a event.

## [◆ ](#a7403d98fe528c492a4b1b449b43c10d3)sync\_call

| struct k\_sem\* net\_mgmt\_event\_callback::sync\_call |
| --- |

Semaphore meant to be used internally for the synchronous [net\_mgmt\_event\_wait()](group__net__mgmt.md#gacbaa95c65717747d802dc80eb745aa17 "Used to wait synchronously on an event mask.") function.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_mgmt.h](net__mgmt_8h_source.md)

- [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
