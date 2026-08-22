---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structvirtq.html
original_path: doxygen/html/structvirtq.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

virtq Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Virtio Interface](group__virtio__interface.md) » [Virtqueue Interface](group__virtqueue__interface.md)

virtqueue
[More...](#details)

`#include <[zephyr/drivers/virtio/virtqueue.h](virtqueue_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [k\_spinlock](structk__spinlock.md) | [lock](#aa4a4101177743201210ec1267df31b57) |
|  | lock used to synchronize operations on virtqueue |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [num](#afeb3f726fe78a18574d7ddd77a1837f9) |
|  | size of virtqueue |
| struct [virtq\_desc](structvirtq__desc.md) \* | [desc](#aa299da6b7d7b4ede53423d17d3973a92) |
|  | array with descriptors |
| struct [virtq\_avail](structvirtq__avail.md) \* | [avail](#a872b79dd002eb3adf0f680c252323346) |
|  | available ring |
| struct [virtq\_used](structvirtq__used.md) \* | [used](#a7f12283618d0acc418d378a8d554215d) |
|  | used ring |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [last\_used\_idx](#a811241bbc1032b299f303c96e45e39c8) |
|  | last seen idx in used ring, used to determine first descriptor to process after receiving virtqueue interrupt |
| struct k\_stack | [free\_desc\_stack](#a441e32c89c78d6b432469957cb38db25) |
|  | Stack containing indexes of free descriptors. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [free\_desc\_n](#a540cc380e0e9ec5fc92cf1ea7f3252fe) |
|  | amount of free descriptors in the free\_desc\_stack |
| struct [virtq\_receive\_callback\_entry](structvirtq__receive__callback__entry.md) \* | [recv\_cbs](#a2cd048d18e1f8f30a197f33f24f53575) |
|  | array with callbacks invoked after receiving buffers back from the device |

## Detailed Description

virtqueue

contains structures required for virtqueue operation

## Field Documentation

## [◆ ](#a872b79dd002eb3adf0f680c252323346)avail

| struct [virtq\_avail](structvirtq__avail.md)\* virtq::avail |
| --- |

available ring

## [◆ ](#aa299da6b7d7b4ede53423d17d3973a92)desc

| struct [virtq\_desc](structvirtq__desc.md)\* virtq::desc |
| --- |

array with descriptors

## [◆ ](#a540cc380e0e9ec5fc92cf1ea7f3252fe)free\_desc\_n

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) virtq::free\_desc\_n |
| --- |

amount of free descriptors in the free\_desc\_stack

## [◆ ](#a441e32c89c78d6b432469957cb38db25)free\_desc\_stack

| struct k\_stack virtq::free\_desc\_stack |
| --- |

Stack containing indexes of free descriptors.

Because virtio devices are not required to use received descriptors in order (see 2.7.9) unless VIRTIO\_F\_IN\_ORDER was offered, we can't use array with descriptors as another ring buffer, always taking next descriptor. This is an auxilary structure to easily determine next free descriptor

## [◆ ](#a811241bbc1032b299f303c96e45e39c8)last\_used\_idx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) virtq::last\_used\_idx |
| --- |

last seen idx in used ring, used to determine first descriptor to process after receiving virtqueue interrupt

## [◆ ](#aa4a4101177743201210ec1267df31b57)lock

| struct [k\_spinlock](structk__spinlock.md) virtq::lock |
| --- |

lock used to synchronize operations on virtqueue

## [◆ ](#afeb3f726fe78a18574d7ddd77a1837f9)num

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) virtq::num |
| --- |

size of virtqueue

## [◆ ](#a2cd048d18e1f8f30a197f33f24f53575)recv\_cbs

| struct [virtq\_receive\_callback\_entry](structvirtq__receive__callback__entry.md)\* virtq::recv\_cbs |
| --- |

array with callbacks invoked after receiving buffers back from the device

## [◆ ](#a7f12283618d0acc418d378a8d554215d)used

| struct [virtq\_used](structvirtq__used.md)\* virtq::used |
| --- |

used ring

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/virtio/[virtqueue.h](virtqueue_8h_source.md)

- [virtq](structvirtq.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
