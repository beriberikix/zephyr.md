---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dom0_2domctl_8h_source.html
original_path: doxygen/html/dom0_2domctl_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

domctl.h

[Go to the documentation of this file.](dom0_2domctl_8h.md)

1/\* SPDX-License-Identifier: Apache-2.0 \*/

2/\*

3 \* Copyright (c) 2023 EPAM Systems

4 \*

5 \*/

6#ifndef \_\_XEN\_DOM0\_DOMCTL\_H\_\_

7#define \_\_XEN\_DOM0\_DOMCTL\_H\_\_

8

9#include <[zephyr/xen/generic.h](generic_8h.md)>

10#include <[zephyr/xen/public/domctl.h](public_2domctl_8h.md)>

11#include <[zephyr/xen/public/xen.h](xen_8h.md)>

12

13#include <[zephyr/kernel.h](kernel_8h.md)>

14

[ 15](dom0_2domctl_8h.md#a7045c1f92142eceefe3e4c651708beae)int [xen\_domctl\_scheduler\_op](dom0_2domctl_8h.md#a7045c1f92142eceefe3e4c651708beae)(int domid, struct [xen\_domctl\_scheduler\_op](structxen__domctl__scheduler__op.md) \*sched\_op);

[ 16](dom0_2domctl_8h.md#aff200f6bfe2a31b536337f5bf668fee7)int [xen\_domctl\_pausedomain](dom0_2domctl_8h.md#aff200f6bfe2a31b536337f5bf668fee7)(int domid);

[ 17](dom0_2domctl_8h.md#a89be676e7f2ff66b4dc195e35e374083)int [xen\_domctl\_unpausedomain](dom0_2domctl_8h.md#a89be676e7f2ff66b4dc195e35e374083)(int domid);

[ 18](dom0_2domctl_8h.md#a50c40d73171240a047cf6e9b41898c99)int [xen\_domctl\_resumedomain](dom0_2domctl_8h.md#a50c40d73171240a047cf6e9b41898c99)(int domid);

[ 19](dom0_2domctl_8h.md#a9040a9ddca3406adc057960b0f423bcd)int [xen\_domctl\_getvcpucontext](dom0_2domctl_8h.md#a9040a9ddca3406adc057960b0f423bcd)(int domid, int vcpu, vcpu\_guest\_context\_t \*ctxt);

[ 20](dom0_2domctl_8h.md#a66505a6d47e0c5ef3334043c668d6740)int [xen\_domctl\_setvcpucontext](dom0_2domctl_8h.md#a66505a6d47e0c5ef3334043c668d6740)(int domid, int vcpu, vcpu\_guest\_context\_t \*ctxt);

[ 21](dom0_2domctl_8h.md#a4848541359c3e13358dc39b42b3c142f)int [xen\_domctl\_getdomaininfo](dom0_2domctl_8h.md#a4848541359c3e13358dc39b42b3c142f)(int domid, [xen\_domctl\_getdomaininfo\_t](public_2domctl_8h.md#a975bbf787336d78a2fe063f5f16766db) \*dom\_info);

[ 22](dom0_2domctl_8h.md#a7f7c3789fb44574317d9c69ca56f1e1d)int [xen\_domctl\_set\_paging\_mempool\_size](dom0_2domctl_8h.md#a7f7c3789fb44574317d9c69ca56f1e1d)(int domid, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) size\_mb);

[ 23](dom0_2domctl_8h.md#acbe8f22573487bcdb8612988da24b68e)int [xen\_domctl\_max\_mem](dom0_2domctl_8h.md#acbe8f22573487bcdb8612988da24b68e)(int domid, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) max\_memkb);

[ 24](dom0_2domctl_8h.md#a8dee93295a86c5d7b586676a831e1047)int [xen\_domctl\_set\_address\_size](dom0_2domctl_8h.md#a8dee93295a86c5d7b586676a831e1047)(int domid, int addr\_size);

[ 25](dom0_2domctl_8h.md#a2a34701f55250140576e8c71607801f8)int [xen\_domctl\_iomem\_permission](dom0_2domctl_8h.md#a2a34701f55250140576e8c71607801f8)(int domid, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) first\_mfn,

26 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) nr\_mfns, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) allow\_access);

[ 27](dom0_2domctl_8h.md#ac945f3330b3b03112f3fa6fb49f42e50)int [xen\_domctl\_memory\_mapping](dom0_2domctl_8h.md#ac945f3330b3b03112f3fa6fb49f42e50)(int domid, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) first\_gfn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) first\_mfn,

28 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) nr\_mfns, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) add\_mapping);

[ 29](dom0_2domctl_8h.md#af7888bd31df37d449cde69bc693c244f)int [xen\_domctl\_assign\_dt\_device](dom0_2domctl_8h.md#af7888bd31df37d449cde69bc693c244f)(int domid, char \*dtdev\_path);

[ 30](dom0_2domctl_8h.md#ad5f80dd7c0a7981f8c5c757b06993dc5)int [xen\_domctl\_bind\_pt\_irq](dom0_2domctl_8h.md#ad5f80dd7c0a7981f8c5c757b06993dc5)(int domid, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) machine\_irq, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irq\_type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bus,

31 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [device](structdevice.md), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) intx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) isa\_irq, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) spi);

[ 32](dom0_2domctl_8h.md#a8f954e5a7d1cd633c6d819780bb6372b)int [xen\_domctl\_max\_vcpus](dom0_2domctl_8h.md#a8f954e5a7d1cd633c6d819780bb6372b)(int domid, int max\_vcpus);

[ 33](dom0_2domctl_8h.md#a4514a348391808482a064b729bf1baeb)int [xen\_domctl\_createdomain](dom0_2domctl_8h.md#a4514a348391808482a064b729bf1baeb)(int domid, struct [xen\_domctl\_createdomain](structxen__domctl__createdomain.md) \*config);

[ 34](dom0_2domctl_8h.md#ad89ece398fc97a94c5c316066e2c29a5)int [xen\_domctl\_cacheflush](dom0_2domctl_8h.md#ad89ece398fc97a94c5c316066e2c29a5)(int domid, struct [xen\_domctl\_cacheflush](structxen__domctl__cacheflush.md) \*cacheflush);

[ 35](dom0_2domctl_8h.md#aba6a1f6e25ac6ee2a7b0d288ca4ab72d)int [xen\_domctl\_destroydomain](dom0_2domctl_8h.md#aba6a1f6e25ac6ee2a7b0d288ca4ab72d)(int domid);

36

37#endif /\* \_\_XEN\_DOM0\_DOMCTL\_H\_\_ \*/

[xen\_domctl\_iomem\_permission](dom0_2domctl_8h.md#a2a34701f55250140576e8c71607801f8)

int xen\_domctl\_iomem\_permission(int domid, uint64\_t first\_mfn, uint64\_t nr\_mfns, uint8\_t allow\_access)

[xen\_domctl\_createdomain](dom0_2domctl_8h.md#a4514a348391808482a064b729bf1baeb)

int xen\_domctl\_createdomain(int domid, struct xen\_domctl\_createdomain \*config)

[xen\_domctl\_getdomaininfo](dom0_2domctl_8h.md#a4848541359c3e13358dc39b42b3c142f)

int xen\_domctl\_getdomaininfo(int domid, xen\_domctl\_getdomaininfo\_t \*dom\_info)

[xen\_domctl\_resumedomain](dom0_2domctl_8h.md#a50c40d73171240a047cf6e9b41898c99)

int xen\_domctl\_resumedomain(int domid)

[xen\_domctl\_setvcpucontext](dom0_2domctl_8h.md#a66505a6d47e0c5ef3334043c668d6740)

int xen\_domctl\_setvcpucontext(int domid, int vcpu, vcpu\_guest\_context\_t \*ctxt)

[xen\_domctl\_scheduler\_op](dom0_2domctl_8h.md#a7045c1f92142eceefe3e4c651708beae)

int xen\_domctl\_scheduler\_op(int domid, struct xen\_domctl\_scheduler\_op \*sched\_op)

[xen\_domctl\_set\_paging\_mempool\_size](dom0_2domctl_8h.md#a7f7c3789fb44574317d9c69ca56f1e1d)

int xen\_domctl\_set\_paging\_mempool\_size(int domid, uint64\_t size\_mb)

[xen\_domctl\_unpausedomain](dom0_2domctl_8h.md#a89be676e7f2ff66b4dc195e35e374083)

int xen\_domctl\_unpausedomain(int domid)

[xen\_domctl\_set\_address\_size](dom0_2domctl_8h.md#a8dee93295a86c5d7b586676a831e1047)

int xen\_domctl\_set\_address\_size(int domid, int addr\_size)

[xen\_domctl\_max\_vcpus](dom0_2domctl_8h.md#a8f954e5a7d1cd633c6d819780bb6372b)

int xen\_domctl\_max\_vcpus(int domid, int max\_vcpus)

[xen\_domctl\_getvcpucontext](dom0_2domctl_8h.md#a9040a9ddca3406adc057960b0f423bcd)

int xen\_domctl\_getvcpucontext(int domid, int vcpu, vcpu\_guest\_context\_t \*ctxt)

[xen\_domctl\_destroydomain](dom0_2domctl_8h.md#aba6a1f6e25ac6ee2a7b0d288ca4ab72d)

int xen\_domctl\_destroydomain(int domid)

[xen\_domctl\_memory\_mapping](dom0_2domctl_8h.md#ac945f3330b3b03112f3fa6fb49f42e50)

int xen\_domctl\_memory\_mapping(int domid, uint64\_t first\_gfn, uint64\_t first\_mfn, uint64\_t nr\_mfns, uint32\_t add\_mapping)

[xen\_domctl\_max\_mem](dom0_2domctl_8h.md#acbe8f22573487bcdb8612988da24b68e)

int xen\_domctl\_max\_mem(int domid, uint64\_t max\_memkb)

[xen\_domctl\_bind\_pt\_irq](dom0_2domctl_8h.md#ad5f80dd7c0a7981f8c5c757b06993dc5)

int xen\_domctl\_bind\_pt\_irq(int domid, uint32\_t machine\_irq, uint8\_t irq\_type, uint8\_t bus, uint8\_t device, uint8\_t intx, uint8\_t isa\_irq, uint16\_t spi)

[xen\_domctl\_cacheflush](dom0_2domctl_8h.md#ad89ece398fc97a94c5c316066e2c29a5)

int xen\_domctl\_cacheflush(int domid, struct xen\_domctl\_cacheflush \*cacheflush)

[xen\_domctl\_assign\_dt\_device](dom0_2domctl_8h.md#af7888bd31df37d449cde69bc693c244f)

int xen\_domctl\_assign\_dt\_device(int domid, char \*dtdev\_path)

[xen\_domctl\_pausedomain](dom0_2domctl_8h.md#aff200f6bfe2a31b536337f5bf668fee7)

int xen\_domctl\_pausedomain(int domid)

[generic.h](generic_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[domctl.h](public_2domctl_8h.md)

[xen\_domctl\_getdomaininfo\_t](public_2domctl_8h.md#a975bbf787336d78a2fe063f5f16766db)

struct xen\_domctl\_getdomaininfo xen\_domctl\_getdomaininfo\_t

**Definition** domctl.h:150

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[xen\_domctl\_cacheflush](structxen__domctl__cacheflush.md)

**Definition** domctl.h:397

[xen\_domctl\_createdomain](structxen__domctl__createdomain.md)

**Definition** domctl.h:31

[xen\_domctl\_scheduler\_op](structxen__domctl__scheduler__op.md)

**Definition** domctl.h:264

[xen.h](xen_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [dom0](dir_250ede4c158f258ed6e884af7ffad142.md)
- [domctl.h](dom0_2domctl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
