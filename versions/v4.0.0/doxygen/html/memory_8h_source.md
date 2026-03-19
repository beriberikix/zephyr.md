---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/memory_8h_source.html
original_path: doxygen/html/memory_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

memory.h

[Go to the documentation of this file.](memory_8h.md)

1/\* SPDX-License-Identifier: Apache-2.0 \*/

2/\*

3 \* Copyright (c) 2023 EPAM Systems

4 \*/

5

6#include <[zephyr/kernel.h](kernel_8h.md)>

7#include <[zephyr/xen/public/memory.h](public_2memory_8h.md)>

8#include <[zephyr/xen/public/xen.h](xen_8h.md)>

9

[ 20](memory_8h.md#ab548b9bcc4479f33f3d8b8467dc6855f)int [xendom\_add\_to\_physmap](memory_8h.md#ab548b9bcc4479f33f3d8b8467dc6855f)(int domid, unsigned long idx, unsigned int space,

21 [xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226) gpfn);

22

[ 37](memory_8h.md#ad3a6f591da88d9781fd08c197a7f933b)int [xendom\_add\_to\_physmap\_batch](memory_8h.md#ad3a6f591da88d9781fd08c197a7f933b)(int domid, int foreign\_domid,

38 unsigned int space, unsigned int size,

39 [xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc) \*idxs, [xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226) \*gpfns, int \*errs);

40

[ 49](memory_8h.md#ae4c9930819726c7ce77725649c03dedf)int [xendom\_remove\_from\_physmap](memory_8h.md#ae4c9930819726c7ce77725649c03dedf)(int domid, [xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226) gpfn);

50

[ 64](memory_8h.md#a7fe2ce11ffa483afa33d95b7cf61520b)int [xendom\_populate\_physmap](memory_8h.md#a7fe2ce11ffa483afa33d95b7cf61520b)(int domid, unsigned int extent\_order,

65 unsigned int nr\_extents, unsigned int mem\_flags,

66 [xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226) \*extent\_start);

[xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226)

uint64\_t xen\_pfn\_t

**Definition** arch-arm.h:204

[xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc)

uint64\_t xen\_ulong\_t

**Definition** arch-arm.h:214

[kernel.h](kernel_8h.md)

Public kernel APIs.

[xendom\_populate\_physmap](memory_8h.md#a7fe2ce11ffa483afa33d95b7cf61520b)

int xendom\_populate\_physmap(int domid, unsigned int extent\_order, unsigned int nr\_extents, unsigned int mem\_flags, xen\_pfn\_t \*extent\_start)

Populate specified Xen domain page frames with memory.

[xendom\_add\_to\_physmap](memory_8h.md#ab548b9bcc4479f33f3d8b8467dc6855f)

int xendom\_add\_to\_physmap(int domid, unsigned long idx, unsigned int space, xen\_pfn\_t gpfn)

Add mapping for specified page frame in Xen domain physmap.

[xendom\_add\_to\_physmap\_batch](memory_8h.md#ad3a6f591da88d9781fd08c197a7f933b)

int xendom\_add\_to\_physmap\_batch(int domid, int foreign\_domid, unsigned int space, unsigned int size, xen\_ulong\_t \*idxs, xen\_pfn\_t \*gpfns, int \*errs)

Add mapping for specified set of page frames to Xen domain physmap.

[xendom\_remove\_from\_physmap](memory_8h.md#ae4c9930819726c7ce77725649c03dedf)

int xendom\_remove\_from\_physmap(int domid, xen\_pfn\_t gpfn)

Removes page frame from Xen domain physmap.

[memory.h](public_2memory_8h.md)

[xen.h](xen_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [memory.h](memory_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
