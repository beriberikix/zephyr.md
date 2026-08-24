---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/virtqueue_8h.html
original_path: doxygen/html/virtqueue_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

virtqueue.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](virtqueue_8h_source.md)

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
| #define | [VIRTQ\_DESC\_F\_NEXT](group__virtqueue__interface.md#ga20e010fee3553a39ff6af7a5cc2837c2)   1 |
|  | used in [virtq\_desc::flags](structvirtq__desc.md#a9731d25acdd201e07e4362f79fb5ba9e "buffer flags"), enables chaining descriptor via [virtq\_desc::next](structvirtq__desc.md#a2703fcd4eb5bf97530687444203e8ee6 "chaining next descriptor, valid if flags & VIRTQ_DESC_F_NEXT") |
| #define | [VIRTQ\_DESC\_F\_WRITE](group__virtqueue__interface.md#ga208ab0e95f24325454621095b80fcf27)   2 |
|  | used in [virtq\_desc::flags](structvirtq__desc.md#a9731d25acdd201e07e4362f79fb5ba9e "buffer flags"), makes descriptor device writeable |

| Typedefs | |
| --- | --- |
| typedef void(\* | [virtq\_receive\_callback](group__virtqueue__interface.md#ga311909fbebf3cb96ace6c751fabcf708)) (void \*opaque, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) used\_len) |
|  | receive callback function type |

| Functions | |
| --- | --- |
| int | [virtq\_create](group__virtqueue__interface.md#ga3dce3b5099fc117a94da63a24571b6c3) (struct [virtq](structvirtq.md) \*v, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | creates virtqueue |
| void | [virtq\_free](group__virtqueue__interface.md#ga9443eb15529fa16d1024a70075daca28) (struct [virtq](structvirtq.md) \*v) |
|  | frees virtqueue |
| int | [virtq\_add\_buffer\_chain](group__virtqueue__interface.md#ga5e01b141e28aec876c298047f8d623a6) (struct [virtq](structvirtq.md) \*v, struct [virtq\_buf](structvirtq__buf.md) \*bufs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bufs\_size, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) device\_readable\_count, [virtq\_receive\_callback](group__virtqueue__interface.md#ga311909fbebf3cb96ace6c751fabcf708) cb, void \*cb\_opaque, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | adds chain of buffers to the virtqueue |
| void | [virtq\_add\_free\_desc](group__virtqueue__interface.md#ga55abe7b8204cf0b57cd1c2380dcd66fb) (struct [virtq](structvirtq.md) \*v, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) desc\_idx) |
|  | adds free descriptor back |
| int | [virtq\_get\_free\_desc](group__virtqueue__interface.md#ga79b1b54f0ea6fe8b5110712488f663eb) (struct [virtq](structvirtq.md) \*v, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*desc\_idx, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | gets next free descriptor |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [virtio](dir_219496648d5efa24b2239bdfe387791d.md)
- [virtqueue.h](virtqueue_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
