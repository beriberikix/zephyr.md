---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/memory_8h.html
original_path: doxygen/html/memory_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

memory.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/xen/public/memory.h](public_2memory_8h_source.md)>`  
`#include <[zephyr/xen/public/xen.h](xen_8h_source.md)>`

[Go to the source code of this file.](memory_8h_source.md)

| Functions | |
| --- | --- |
| int | [xendom\_add\_to\_physmap](#ab548b9bcc4479f33f3d8b8467dc6855f) (int domid, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long idx, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int space, [xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226) gpfn) |
|  | Add mapping for specified page frame in Xen domain physmap. |
| int | [xendom\_add\_to\_physmap\_batch](#ad3a6f591da88d9781fd08c197a7f933b) (int domid, int foreign\_domid, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int space, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int size, [xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc) \*idxs, [xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226) \*gpfns, int \*errs) |
|  | Add mapping for specified set of page frames to Xen domain physmap. |
| int | [xendom\_remove\_from\_physmap](#ae4c9930819726c7ce77725649c03dedf) (int domid, [xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226) gpfn) |
|  | Removes page frame from Xen domain physmap. |
| int | [xendom\_populate\_physmap](#a7fe2ce11ffa483afa33d95b7cf61520b) (int domid, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int extent\_order, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nr\_extents, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int mem\_flags, [xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226) \*extent\_start) |
|  | Populate specified Xen domain page frames with memory. |

## Function Documentation

## [◆ ](#ab548b9bcc4479f33f3d8b8467dc6855f)xendom\_add\_to\_physmap()

| int xendom\_add\_to\_physmap | ( | int | *domid*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *idx*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *space*, |
|  |  | [xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226) | *gpfn* ) |

Add mapping for specified page frame in Xen domain physmap.

Parameters
:   | domid | domain id, where mapping will be added. For unprivileged should be DOMID\_SELF. |
    | --- | --- |
    | idx | index into space being mapped. |
    | space | XENMAPSPACE\_\* mapping space identifier. |
    | gpfn | page frame where the source mapping page should appear. |

Returns
:   zero on success, negative errno on error.

## [◆ ](#ad3a6f591da88d9781fd08c197a7f933b)xendom\_add\_to\_physmap\_batch()

| int xendom\_add\_to\_physmap\_batch | ( | int | *domid*, |
| --- | --- | --- | --- |
|  |  | int | *foreign\_domid*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *space*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *size*, |
|  |  | [xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc) \* | *idxs*, |
|  |  | [xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226) \* | *gpfns*, |
|  |  | int \* | *errs* ) |

Add mapping for specified set of page frames to Xen domain physmap.

Parameters
:   | domid | domain id, where mapping will be added. For unprivileged should be DOMID\_SELF. |
    | --- | --- |
    | foreign\_domid | for gmfn\_foreign - domain id, whose pages being mapped, 0 for other. |
    | space | XENMAPSPACE\_\* mapping space identifier. |
    | size | number of page frames being mapped. |
    | idxs | array of indexes into space being mapped. |
    | gpfns | array of page frames where the mapping should appear. |
    | errs | array of per-index error codes. |

Returns
:   zero on success, negative errno on error.

## [◆ ](#a7fe2ce11ffa483afa33d95b7cf61520b)xendom\_populate\_physmap()

| int xendom\_populate\_physmap | ( | int | *domid*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *extent\_order*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *nr\_extents*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *mem\_flags*, |
|  |  | [xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226) \* | *extent\_start* ) |

Populate specified Xen domain page frames with memory.

Parameters
:   | domid | domain id, where mapping will be added. For unprivileged should be DOMID\_SELF. |
    | --- | --- |
    | extent\_order | size/alignment of each extent (size is 2^extent\_order), e.g. 0 for 4K extents, 9 for 2M etc. |
    | nr\_extents | number of page frames being populated. |
    | mem\_flags | N/A, should be 0 for Arm. |
    | extent\_start | page frame bases of extents to populate with memory. |

Returns
:   number of populated frames success, negative errno on error.

## [◆ ](#ae4c9930819726c7ce77725649c03dedf)xendom\_remove\_from\_physmap()

| int xendom\_remove\_from\_physmap | ( | int | *domid*, |
| --- | --- | --- | --- |
|  |  | [xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226) | *gpfn* ) |

Removes page frame from Xen domain physmap.

Parameters
:   | domid | domain id, whose page is going to be removed. For unprivileged should be DOMID\_SELF. |
    | --- | --- |
    | gpfn | page frame number, that needs to be removed |

Returns
:   zero on success, negative errno on error.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [memory.h](memory_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
