---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structheap__listener.html
original_path: doxygen/html/structheap__listener.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

heap\_listener Struct Reference

[Operating System Services](group__os__services.md) » [Heap Management](group__heaps.md) » [Heap Listener APIs](group__heap__listener__apis.md)

`#include <[heap_listener.h](heap__listener_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#ab0f3071d7828856bcbee55ff9791a27c) |
|  | Singly linked list node. |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [heap\_id](#a9b13bffbb860ea78207b4ebe7c61b768) |
|  | Identifier of the heap whose events are listened. |
| enum [heap\_event\_types](group__heap__listener__apis.md#ga9679320e1c32dcbad726789946565510) | [event](#a1ef2db791f5422fa7e6bb17c2b6bf247) |
|  | The heap event to be notified. |
| union { |  |
| [heap\_listener\_alloc\_cb\_t](group__heap__listener__apis.md#ga325f3d6679f9bc6d6d1b2e98c8efd2f6)   [alloc\_cb](#a34a982da6ecc3564ef2194f045eea646) |  |
| [heap\_listener\_free\_cb\_t](group__heap__listener__apis.md#ga8a2e3c13b898647618ba93cd592e406f)   [free\_cb](#a46a7f4856397851c64ce07c95b1d9b19) |  |
| [heap\_listener\_resize\_cb\_t](group__heap__listener__apis.md#gad8addd23bfb3f303c10c13024a8c29ce)   [resize\_cb](#a0dcba80daeebe0be96d5e75051cbf287) |  |
| }; |  |

## Field Documentation

## [◆ ](#a2cd780402d745bdd2dfbaf632e2a6df6)[union]

| union { ... } [heap\_listener](structheap__listener.md) |
| --- |

## [◆ ](#a34a982da6ecc3564ef2194f045eea646)alloc\_cb

| [heap\_listener\_alloc\_cb\_t](group__heap__listener__apis.md#ga325f3d6679f9bc6d6d1b2e98c8efd2f6) heap\_listener::alloc\_cb |
| --- |

## [◆ ](#a1ef2db791f5422fa7e6bb17c2b6bf247)event

| enum [heap\_event\_types](group__heap__listener__apis.md#ga9679320e1c32dcbad726789946565510) heap\_listener::event |
| --- |

The heap event to be notified.

## [◆ ](#a46a7f4856397851c64ce07c95b1d9b19)free\_cb

| [heap\_listener\_free\_cb\_t](group__heap__listener__apis.md#ga8a2e3c13b898647618ba93cd592e406f) heap\_listener::free\_cb |
| --- |

## [◆ ](#a9b13bffbb860ea78207b4ebe7c61b768)heap\_id

| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_listener::heap\_id |
| --- |

Identifier of the heap whose events are listened.

It can be a heap pointer, if the heap is represented as an object, or 0 in the case of the global libc heap.

## [◆ ](#ab0f3071d7828856bcbee55ff9791a27c)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) heap\_listener::node |
| --- |

Singly linked list node.

## [◆ ](#a0dcba80daeebe0be96d5e75051cbf287)resize\_cb

| [heap\_listener\_resize\_cb\_t](group__heap__listener__apis.md#gad8addd23bfb3f303c10c13024a8c29ce) heap\_listener::resize\_cb |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[heap\_listener.h](heap__listener_8h_source.md)

- [heap\_listener](structheap__listener.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
