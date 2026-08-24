---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__virtqueue__interface.html
original_path: doxygen/html/group__virtqueue__interface.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Virtqueue Interface

[Device Driver APIs](group__io__interfaces.md) » [Virtio Interface](group__virtio__interface.md)

Virtqueue Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [virtq\_desc](structvirtq__desc.md) |
|  | virtqueue descriptor [More...](structvirtq__desc.md#details) |
| struct | [virtq\_avail](structvirtq__avail.md) |
|  | virtqueue available ring [More...](structvirtq__avail.md#details) |
| struct | [virtq\_used\_elem](structvirtq__used__elem.md) |
|  | used descriptor chain [More...](structvirtq__used__elem.md#details) |
| struct | [virtq\_used](structvirtq__used.md) |
|  | virtqueue used ring [More...](structvirtq__used.md#details) |
| struct | [virtq\_receive\_callback\_entry](structvirtq__receive__callback__entry.md) |
|  | callback descriptor [More...](structvirtq__receive__callback__entry.md#details) |
| struct | [virtq](structvirtq.md) |
|  | virtqueue [More...](structvirtq.md#details) |
| struct | [virtq\_buf](structvirtq__buf.md) |
|  | single buffer passed to virtq\_add\_buffer\_chain [More...](structvirtq__buf.md#details) |

| Macros | |
| --- | --- |
| #define | [VIRTQ\_DESC\_F\_NEXT](#ga20e010fee3553a39ff6af7a5cc2837c2)   1 |
|  | used in [virtq\_desc::flags](structvirtq__desc.md#a9731d25acdd201e07e4362f79fb5ba9e "buffer flags"), enables chaining descriptor via [virtq\_desc::next](structvirtq__desc.md#a2703fcd4eb5bf97530687444203e8ee6 "chaining next descriptor, valid if flags & VIRTQ_DESC_F_NEXT") |
| #define | [VIRTQ\_DESC\_F\_WRITE](#ga208ab0e95f24325454621095b80fcf27)   2 |
|  | used in [virtq\_desc::flags](structvirtq__desc.md#a9731d25acdd201e07e4362f79fb5ba9e "buffer flags"), makes descriptor device writeable |

| Typedefs | |
| --- | --- |
| typedef void(\* | [virtq\_receive\_callback](#ga311909fbebf3cb96ace6c751fabcf708)) (void \*opaque, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) used\_len) |
|  | receive callback function type |

| Functions | |
| --- | --- |
| int | [virtq\_create](#ga3dce3b5099fc117a94da63a24571b6c3) (struct [virtq](structvirtq.md) \*v, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | creates virtqueue |
| void | [virtq\_free](#ga9443eb15529fa16d1024a70075daca28) (struct [virtq](structvirtq.md) \*v) |
|  | frees virtqueue |
| int | [virtq\_add\_buffer\_chain](#ga5e01b141e28aec876c298047f8d623a6) (struct [virtq](structvirtq.md) \*v, struct [virtq\_buf](structvirtq__buf.md) \*bufs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bufs\_size, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) device\_readable\_count, [virtq\_receive\_callback](#ga311909fbebf3cb96ace6c751fabcf708) cb, void \*cb\_opaque, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | adds chain of buffers to the virtqueue |
| void | [virtq\_add\_free\_desc](#ga55abe7b8204cf0b57cd1c2380dcd66fb) (struct [virtq](structvirtq.md) \*v, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) desc\_idx) |
|  | adds free descriptor back |
| int | [virtq\_get\_free\_desc](#ga79b1b54f0ea6fe8b5110712488f663eb) (struct [virtq](structvirtq.md) \*v, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*desc\_idx, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | gets next free descriptor |

## Detailed Description

Virtqueue Interface.

## Macro Definition Documentation

## [◆ ](#ga20e010fee3553a39ff6af7a5cc2837c2)VIRTQ\_DESC\_F\_NEXT

| #define VIRTQ\_DESC\_F\_NEXT   1 |
| --- |

`#include <[zephyr/drivers/virtio/virtqueue.h](virtqueue_8h.md)>`

used in [virtq\_desc::flags](structvirtq__desc.md#a9731d25acdd201e07e4362f79fb5ba9e "buffer flags"), enables chaining descriptor via [virtq\_desc::next](structvirtq__desc.md#a2703fcd4eb5bf97530687444203e8ee6 "chaining next descriptor, valid if flags & VIRTQ_DESC_F_NEXT")

## [◆ ](#ga208ab0e95f24325454621095b80fcf27)VIRTQ\_DESC\_F\_WRITE

| #define VIRTQ\_DESC\_F\_WRITE   2 |
| --- |

`#include <[zephyr/drivers/virtio/virtqueue.h](virtqueue_8h.md)>`

used in [virtq\_desc::flags](structvirtq__desc.md#a9731d25acdd201e07e4362f79fb5ba9e "buffer flags"), makes descriptor device writeable

## Typedef Documentation

## [◆ ](#ga311909fbebf3cb96ace6c751fabcf708)virtq\_receive\_callback

| typedef void(\* virtq\_receive\_callback) (void \*opaque, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) used\_len) |
| --- |

`#include <[zephyr/drivers/virtio/virtqueue.h](virtqueue_8h.md)>`

receive callback function type

Parameters
:   | opaque | argument passed to the callback |
    | --- | --- |
    | used\_len | total amount of bytes written to the descriptor chain by the virtio device |

## Function Documentation

## [◆ ](#ga5e01b141e28aec876c298047f8d623a6)virtq\_add\_buffer\_chain()

| int virtq\_add\_buffer\_chain | ( | struct [virtq](structvirtq.md) \* | *v*, |
| --- | --- | --- | --- |
|  |  | struct [virtq\_buf](structvirtq__buf.md) \* | *bufs*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *bufs\_size*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *device\_readable\_count*, |
|  |  | [virtq\_receive\_callback](#ga311909fbebf3cb96ace6c751fabcf708) | *cb*, |
|  |  | void \* | *cb\_opaque*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[zephyr/drivers/virtio/virtqueue.h](virtqueue_8h.md)>`

adds chain of buffers to the virtqueue

Note that according to spec 2.7.13.3 the device may access the buffers as soon as the avail->idx is increased, which is done at the end of this function, so the device may access the buffers without notifying it with virtio\_notify\_virtqueue

Parameters
:   | v | virtqueue it operates on |
    | --- | --- |
    | bufs | array of buffers to be added to the virtqueue |
    | bufs\_size | amount of buffers |
    | device\_readable\_count | amount of bufferes readable by the device, the first device\_readable\_count buffers will be set as device readable |
    | cb | callback to be invoked after device returns the buffer chain, can be NULL |
    | cb\_opaque | opaque value that will be passed to the cb |
    | timeout | amount of time it will wait for free descriptors, with K\_NO\_WAIT it can be called from isr |

Returns
:   0 or error code on failure

## [◆ ](#ga55abe7b8204cf0b57cd1c2380dcd66fb)virtq\_add\_free\_desc()

| void virtq\_add\_free\_desc | ( | struct [virtq](structvirtq.md) \* | *v*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *desc\_idx* ) |

`#include <[zephyr/drivers/virtio/virtqueue.h](virtqueue_8h.md)>`

adds free descriptor back

Parameters
:   | v | virtqueue it operates on |
    | --- | --- |
    | desc\_idx | index of returned descriptor |

## [◆ ](#ga3dce3b5099fc117a94da63a24571b6c3)virtq\_create()

| int virtq\_create | ( | struct [virtq](structvirtq.md) \* | *v*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[zephyr/drivers/virtio/virtqueue.h](virtqueue_8h.md)>`

creates virtqueue

Parameters
:   | v | virtqueue to be created |
    | --- | --- |
    | size | size of the virtqueue |

Returns
:   0 or error code on failure

## [◆ ](#ga9443eb15529fa16d1024a70075daca28)virtq\_free()

| void virtq\_free | ( | struct [virtq](structvirtq.md) \* | *v* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/virtio/virtqueue.h](virtqueue_8h.md)>`

frees virtqueue

Parameters
:   | v | virtqueue to be freed |
    | --- | --- |

## [◆ ](#ga79b1b54f0ea6fe8b5110712488f663eb)virtq\_get\_free\_desc()

| int virtq\_get\_free\_desc | ( | struct [virtq](structvirtq.md) \* | *v*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *desc\_idx*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[zephyr/drivers/virtio/virtqueue.h](virtqueue_8h.md)>`

gets next free descriptor

Parameters
:   | v | virtqueue it operates on |
    | --- | --- |
    | desc\_idx | address where index of descriptor will be stored |
    | timeout | amount of time it will wait for free descriptor, with K\_NO\_WAIT it can be called from isr |

Returns
:   0 or error code on failure

- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
