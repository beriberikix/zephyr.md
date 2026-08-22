---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structvirtq__desc.html
original_path: doxygen/html/structvirtq__desc.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

virtq\_desc Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Virtio Interface](group__virtio__interface.md) » [Virtqueue Interface](group__virtqueue__interface.md)

virtqueue descriptor
[More...](#details)

`#include <[zephyr/drivers/virtio/virtqueue.h](virtqueue_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [addr](#a1d5146808360ff5e359673c193fe4d53) |
|  | physical address of the buffer |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [len](#a1dcd1400d72aa7b628920258e226a7ce) |
|  | length of the buffer |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [flags](#a9731d25acdd201e07e4362f79fb5ba9e) |
|  | buffer flags |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [next](#a2703fcd4eb5bf97530687444203e8ee6) |
|  | chaining next descriptor, valid if flags & VIRTQ\_DESC\_F\_NEXT |

## Detailed Description

virtqueue descriptor

Describes a single buffer

## Field Documentation

## [◆ ](#a1d5146808360ff5e359673c193fe4d53)addr

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) virtq\_desc::addr |
| --- |

physical address of the buffer

## [◆ ](#a9731d25acdd201e07e4362f79fb5ba9e)flags

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) virtq\_desc::flags |
| --- |

buffer flags

## [◆ ](#a1dcd1400d72aa7b628920258e226a7ce)len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) virtq\_desc::len |
| --- |

length of the buffer

## [◆ ](#a2703fcd4eb5bf97530687444203e8ee6)next

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) virtq\_desc::next |
| --- |

chaining next descriptor, valid if flags & VIRTQ\_DESC\_F\_NEXT

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/virtio/[virtqueue.h](virtqueue_8h_source.md)

- [virtq\_desc](structvirtq__desc.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
