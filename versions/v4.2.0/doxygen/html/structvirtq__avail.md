---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structvirtq__avail.html
original_path: doxygen/html/structvirtq__avail.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

virtq\_avail Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Virtio Interface](group__virtio__interface.md) » [Virtqueue Interface](group__virtqueue__interface.md)

virtqueue available ring
[More...](#details)

`#include <[zephyr/drivers/virtio/virtqueue.h](virtqueue_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [flags](#ab013600ebaa7a4c855112599755ce607) |
|  | ring flags, e.g. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [idx](#a70caebae8d3a86d05cb718c5e0a9f88d) |
|  | head of the ring, by increasing it newly added descriptors are committed |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [ring](#a03f0bc25a3459316bd166f3cbf9a66c3) [] |
|  | ring with indexes of descriptors |

## Detailed Description

virtqueue available ring

Used to pass descriptors to the virtio device. Driver writeable, device readable

## Field Documentation

## [◆ ](#ab013600ebaa7a4c855112599755ce607)flags

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) virtq\_avail::flags |
| --- |

ring flags, e.g.

VIRTQ\_AVAIL\_F\_NO\_INTERRUPT, currently unused

## [◆ ](#a70caebae8d3a86d05cb718c5e0a9f88d)idx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) virtq\_avail::idx |
| --- |

head of the ring, by increasing it newly added descriptors are committed

## [◆ ](#a03f0bc25a3459316bd166f3cbf9a66c3)ring

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) virtq\_avail::ring[] |
| --- |

ring with indexes of descriptors

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/virtio/[virtqueue.h](virtqueue_8h_source.md)

- [virtq\_avail](structvirtq__avail.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
