---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structvirtq__buf.html
original_path: doxygen/html/structvirtq__buf.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

virtq\_buf Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Virtio Interface](group__virtio__interface.md) » [Virtqueue Interface](group__virtqueue__interface.md)

single buffer passed to virtq\_add\_buffer\_chain
[More...](#details)

`#include <[zephyr/drivers/virtio/virtqueue.h](virtqueue_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [addr](#ad05060db8d467017fca4af593bab9417) |
|  | virtual address of the buffer |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [len](#aaa047b4296f5c104d5a8f5eaf48aaaac) |
|  | length of the buffer |

## Detailed Description

single buffer passed to virtq\_add\_buffer\_chain

## Field Documentation

## [◆ ](#ad05060db8d467017fca4af593bab9417)addr

| void\* virtq\_buf::addr |
| --- |

virtual address of the buffer

## [◆ ](#aaa047b4296f5c104d5a8f5eaf48aaaac)len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) virtq\_buf::len |
| --- |

length of the buffer

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/virtio/[virtqueue.h](virtqueue_8h_source.md)

- [virtq\_buf](structvirtq__buf.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
