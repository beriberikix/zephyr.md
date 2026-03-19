---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dom0_2domctl_8h.html
original_path: doxygen/html/dom0_2domctl_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

domctl.h File Reference

`#include <[zephyr/xen/generic.h](generic_8h_source.md)>`  
`#include <[zephyr/xen/public/domctl.h](public_2domctl_8h_source.md)>`  
`#include <[zephyr/xen/public/xen.h](xen_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](dom0_2domctl_8h_source.md)

| Functions | |
| --- | --- |
| int | [xen\_domctl\_scheduler\_op](#a7045c1f92142eceefe3e4c651708beae) (int domid, struct xen\_domctl\_scheduler\_op \*sched\_op) |
| int | [xen\_domctl\_pausedomain](#aff200f6bfe2a31b536337f5bf668fee7) (int domid) |
| int | [xen\_domctl\_unpausedomain](#a89be676e7f2ff66b4dc195e35e374083) (int domid) |
| int | [xen\_domctl\_resumedomain](#a50c40d73171240a047cf6e9b41898c99) (int domid) |
| int | [xen\_domctl\_getvcpucontext](#a9040a9ddca3406adc057960b0f423bcd) (int domid, int vcpu, vcpu\_guest\_context\_t \*ctxt) |
| int | [xen\_domctl\_setvcpucontext](#a66505a6d47e0c5ef3334043c668d6740) (int domid, int vcpu, vcpu\_guest\_context\_t \*ctxt) |
| int | [xen\_domctl\_getdomaininfo](#a4848541359c3e13358dc39b42b3c142f) (int domid, [xen\_domctl\_getdomaininfo\_t](public_2domctl_8h.md#a975bbf787336d78a2fe063f5f16766db) \*dom\_info) |
| int | [xen\_domctl\_set\_paging\_mempool\_size](#a7f7c3789fb44574317d9c69ca56f1e1d) (int domid, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) size\_mb) |
| int | [xen\_domctl\_max\_mem](#acbe8f22573487bcdb8612988da24b68e) (int domid, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) max\_memkb) |
| int | [xen\_domctl\_set\_address\_size](#a8dee93295a86c5d7b586676a831e1047) (int domid, int addr\_size) |
| int | [xen\_domctl\_iomem\_permission](#a2a34701f55250140576e8c71607801f8) (int domid, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) first\_mfn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) nr\_mfns, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) allow\_access) |
| int | [xen\_domctl\_memory\_mapping](#ac945f3330b3b03112f3fa6fb49f42e50) (int domid, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) first\_gfn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) first\_mfn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) nr\_mfns, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) add\_mapping) |
| int | [xen\_domctl\_assign\_dt\_device](#af7888bd31df37d449cde69bc693c244f) (int domid, char \*dtdev\_path) |
| int | [xen\_domctl\_bind\_pt\_irq](#ad5f80dd7c0a7981f8c5c757b06993dc5) (int domid, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) machine\_irq, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irq\_type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bus, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [device](structdevice.md), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) intx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) isa\_irq, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) spi) |
| int | [xen\_domctl\_max\_vcpus](#a8f954e5a7d1cd633c6d819780bb6372b) (int domid, int max\_vcpus) |
| int | [xen\_domctl\_createdomain](#a4514a348391808482a064b729bf1baeb) (int domid, struct xen\_domctl\_createdomain \*config) |
| int | [xen\_domctl\_cacheflush](#ad89ece398fc97a94c5c316066e2c29a5) (int domid, struct xen\_domctl\_cacheflush \*cacheflush) |
| int | [xen\_domctl\_destroydomain](#aba6a1f6e25ac6ee2a7b0d288ca4ab72d) (int domid) |

## Function Documentation

## [◆ ](#af7888bd31df37d449cde69bc693c244f)xen\_domctl\_assign\_dt\_device()

| int xen\_domctl\_assign\_dt\_device | ( | int | *domid*, |
| --- | --- | --- | --- |
|  |  | char \* | *dtdev\_path* ) |

## [◆ ](#ad5f80dd7c0a7981f8c5c757b06993dc5)xen\_domctl\_bind\_pt\_irq()

| int xen\_domctl\_bind\_pt\_irq | ( | int | *domid*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *machine\_irq*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *irq\_type*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *bus*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *device*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *intx*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *isa\_irq*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *spi* ) |

## [◆ ](#ad89ece398fc97a94c5c316066e2c29a5)xen\_domctl\_cacheflush()

| int xen\_domctl\_cacheflush | ( | int | *domid*, |
| --- | --- | --- | --- |
|  |  | struct xen\_domctl\_cacheflush \* | *cacheflush* ) |

## [◆ ](#a4514a348391808482a064b729bf1baeb)xen\_domctl\_createdomain()

| int xen\_domctl\_createdomain | ( | int | *domid*, |
| --- | --- | --- | --- |
|  |  | struct xen\_domctl\_createdomain \* | *config* ) |

## [◆ ](#aba6a1f6e25ac6ee2a7b0d288ca4ab72d)xen\_domctl\_destroydomain()

| int xen\_domctl\_destroydomain | ( | int | *domid* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a4848541359c3e13358dc39b42b3c142f)xen\_domctl\_getdomaininfo()

| int xen\_domctl\_getdomaininfo | ( | int | *domid*, |
| --- | --- | --- | --- |
|  |  | [xen\_domctl\_getdomaininfo\_t](public_2domctl_8h.md#a975bbf787336d78a2fe063f5f16766db) \* | *dom\_info* ) |

## [◆ ](#a9040a9ddca3406adc057960b0f423bcd)xen\_domctl\_getvcpucontext()

| int xen\_domctl\_getvcpucontext | ( | int | *domid*, |
| --- | --- | --- | --- |
|  |  | int | *vcpu*, |
|  |  | vcpu\_guest\_context\_t \* | *ctxt* ) |

## [◆ ](#a2a34701f55250140576e8c71607801f8)xen\_domctl\_iomem\_permission()

| int xen\_domctl\_iomem\_permission | ( | int | *domid*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *first\_mfn*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *nr\_mfns*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *allow\_access* ) |

## [◆ ](#acbe8f22573487bcdb8612988da24b68e)xen\_domctl\_max\_mem()

| int xen\_domctl\_max\_mem | ( | int | *domid*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *max\_memkb* ) |

## [◆ ](#a8f954e5a7d1cd633c6d819780bb6372b)xen\_domctl\_max\_vcpus()

| int xen\_domctl\_max\_vcpus | ( | int | *domid*, |
| --- | --- | --- | --- |
|  |  | int | *max\_vcpus* ) |

## [◆ ](#ac945f3330b3b03112f3fa6fb49f42e50)xen\_domctl\_memory\_mapping()

| int xen\_domctl\_memory\_mapping | ( | int | *domid*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *first\_gfn*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *first\_mfn*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *nr\_mfns*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *add\_mapping* ) |

## [◆ ](#aff200f6bfe2a31b536337f5bf668fee7)xen\_domctl\_pausedomain()

| int xen\_domctl\_pausedomain | ( | int | *domid* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a50c40d73171240a047cf6e9b41898c99)xen\_domctl\_resumedomain()

| int xen\_domctl\_resumedomain | ( | int | *domid* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a7045c1f92142eceefe3e4c651708beae)xen\_domctl\_scheduler\_op()

| int xen\_domctl\_scheduler\_op | ( | int | *domid*, |
| --- | --- | --- | --- |
|  |  | struct xen\_domctl\_scheduler\_op \* | *sched\_op* ) |

## [◆ ](#a8dee93295a86c5d7b586676a831e1047)xen\_domctl\_set\_address\_size()

| int xen\_domctl\_set\_address\_size | ( | int | *domid*, |
| --- | --- | --- | --- |
|  |  | int | *addr\_size* ) |

## [◆ ](#a7f7c3789fb44574317d9c69ca56f1e1d)xen\_domctl\_set\_paging\_mempool\_size()

| int xen\_domctl\_set\_paging\_mempool\_size | ( | int | *domid*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *size\_mb* ) |

## [◆ ](#a66505a6d47e0c5ef3334043c668d6740)xen\_domctl\_setvcpucontext()

| int xen\_domctl\_setvcpucontext | ( | int | *domid*, |
| --- | --- | --- | --- |
|  |  | int | *vcpu*, |
|  |  | vcpu\_guest\_context\_t \* | *ctxt* ) |

## [◆ ](#a89be676e7f2ff66b4dc195e35e374083)xen\_domctl\_unpausedomain()

| int xen\_domctl\_unpausedomain | ( | int | *domid* | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [dom0](dir_250ede4c158f258ed6e884af7ffad142.md)
- [domctl.h](dom0_2domctl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
