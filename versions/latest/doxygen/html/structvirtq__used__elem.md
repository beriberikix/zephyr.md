---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structvirtq__used__elem.html
original_path: doxygen/html/structvirtq__used__elem.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

virtq\_used\_elem Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Virtio Interface](group__virtio__interface.md) » [Virtqueue Interface](group__virtqueue__interface.md)

used descriptor chain
[More...](#details)

`#include <[zephyr/drivers/virtio/virtqueue.h](virtqueue_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [id](#a7f1f8b4bc3590a00e85bed3657a9fbdc) |
|  | index of the head of descriptor chain |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [len](#ad61ce7642ec40dba74c2f8ffd28ba8ed) |
|  | total amount of bytes written to descriptor chain by the virtio device |

## Detailed Description

used descriptor chain

Describes a single descriptor chain returned by the virtio device

## Field Documentation

## [◆ ](#a7f1f8b4bc3590a00e85bed3657a9fbdc)id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) virtq\_used\_elem::id |
| --- |

index of the head of descriptor chain

## [◆ ](#ad61ce7642ec40dba74c2f8ffd28ba8ed)len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) virtq\_used\_elem::len |
| --- |

total amount of bytes written to descriptor chain by the virtio device

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/virtio/[virtqueue.h](virtqueue_8h_source.md)

- [virtq\_used\_elem](structvirtq__used__elem.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
