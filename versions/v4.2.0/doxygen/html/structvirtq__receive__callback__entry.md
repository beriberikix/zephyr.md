---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structvirtq__receive__callback__entry.html
original_path: doxygen/html/structvirtq__receive__callback__entry.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

virtq\_receive\_callback\_entry Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Virtio Interface](group__virtio__interface.md) » [Virtqueue Interface](group__virtqueue__interface.md)

callback descriptor
[More...](#details)

`#include <[zephyr/drivers/virtio/virtqueue.h](virtqueue_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [virtq\_receive\_callback](group__virtqueue__interface.md#ga311909fbebf3cb96ace6c751fabcf708) | [cb](#ae892b29ffebb17cba4154e342278908d) |
|  | callback function pointer |
| void \* | [opaque](#adc164ebec52cd00cc15839b1cda4be56) |
|  | argument passed to the callback function |

## Detailed Description

callback descriptor

contains callback function ad its argument, invoked after virtio device return descriptor chain its associated with

## Field Documentation

## [◆ ](#ae892b29ffebb17cba4154e342278908d)cb

| [virtq\_receive\_callback](group__virtqueue__interface.md#ga311909fbebf3cb96ace6c751fabcf708) virtq\_receive\_callback\_entry::cb |
| --- |

callback function pointer

## [◆ ](#adc164ebec52cd00cc15839b1cda4be56)opaque

| void\* virtq\_receive\_callback\_entry::opaque |
| --- |

argument passed to the callback function

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/virtio/[virtqueue.h](virtqueue_8h_source.md)

- [virtq\_receive\_callback\_entry](structvirtq__receive__callback__entry.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
