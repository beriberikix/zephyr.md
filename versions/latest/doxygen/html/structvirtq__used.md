---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structvirtq__used.html
original_path: doxygen/html/structvirtq__used.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

virtq\_used Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Virtio Interface](group__virtio__interface.md) » [Virtqueue Interface](group__virtqueue__interface.md)

virtqueue used ring
[More...](#details)

`#include <[zephyr/drivers/virtio/virtqueue.h](virtqueue_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [flags](#a77e64d4bc15ae058515aa96987794f90) |
|  | ring flags, e.g. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [idx](#ad3e466c8aee5efcfef250e907717e656) |
|  | head of the ring |
| struct [virtq\_used\_elem](structvirtq__used__elem.md) | [ring](#a36575313c28554dda228a32ed58156e8) [] |
|  | ring of struct [virtq\_used\_elem](structvirtq__used__elem.md "used descriptor chain") |

## Detailed Description

virtqueue used ring

Used to receive descriptors from the virtio device. Driver readable, device writeable

## Field Documentation

## [◆ ](#a77e64d4bc15ae058515aa96987794f90)flags

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) virtq\_used::flags |
| --- |

ring flags, e.g.

VIRTQ\_USED\_F\_NO\_NOTIFY, currently unused

## [◆ ](#ad3e466c8aee5efcfef250e907717e656)idx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) virtq\_used::idx |
| --- |

head of the ring

## [◆ ](#a36575313c28554dda228a32ed58156e8)ring

| struct [virtq\_used\_elem](structvirtq__used__elem.md) virtq\_used::ring[] |
| --- |

ring of struct [virtq\_used\_elem](structvirtq__used__elem.md "used descriptor chain")

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/virtio/[virtqueue.h](virtqueue_8h_source.md)

- [virtq\_used](structvirtq__used.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
