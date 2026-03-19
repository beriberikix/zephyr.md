---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__mem-demand-paging-backing-store.html
original_path: doxygen/html/group__mem-demand-paging-backing-store.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Backing Store APIs

[Kernel APIs](group__kernel__apis.md) » [Kernel Memory Management](group__kernel__memory__management.md) » [Demand Paging](group__demand__paging.md)

Backing store APIs.
[More...](#details)

| Functions | |
| --- | --- |
| int | [k\_mem\_paging\_backing\_store\_location\_get](#ga1192487fdc8d63c025de42162fb204cd) (struct k\_mem\_page\_frame \*pf, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*location, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) page\_fault) |
|  | Reserve or fetch a storage location for a data page loaded into a page frame. |
| void | [k\_mem\_paging\_backing\_store\_location\_free](#ga6ad421ad5671d9df3d96e03361f672e8) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) location) |
|  | Free a backing store location. |
| int | [k\_mem\_paging\_backing\_store\_location\_query](#ga25debe925b369765ecd5bd7777ce32d0) (void \*addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*location) |
|  | Obtain persistent location token for on-demand content. |
| void | [k\_mem\_paging\_backing\_store\_page\_out](#ga51f663e0a8c31367082e78097359af6d) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) location) |
|  | Copy a data page from K\_MEM\_SCRATCH\_PAGE to the specified location. |
| void | [k\_mem\_paging\_backing\_store\_page\_in](#ga9becb4908cc7840ece93a2360692962d) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) location) |
|  | Copy a data page from the provided location to K\_MEM\_SCRATCH\_PAGE. |
| void | [k\_mem\_paging\_backing\_store\_page\_finalize](#ga8d4bd3ea311fd873413d0477e8deb464) (struct k\_mem\_page\_frame \*pf, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) location) |
|  | Update internal accounting after a page-in. |
| void | [k\_mem\_paging\_backing\_store\_init](#ga7ff441f23619b2678bfb72559d5bd592) (void) |
|  | Backing store initialization function. |

## Detailed Description

Backing store APIs.

## Function Documentation

## [◆ ](#ga7ff441f23619b2678bfb72559d5bd592)k\_mem\_paging\_backing\_store\_init()

| void k\_mem\_paging\_backing\_store\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[demand_paging.h](demand__paging_8h.md)>`

Backing store initialization function.

The implementation may expect to receive page in/out calls as soon as this returns, but not before that. Called at POST\_KERNEL.

This function is expected to do two things:

- Initialize any internal data structures and accounting for the backing store.
- If the backing store already contains all or some loaded kernel data pages at boot time, K\_MEM\_PAGE\_FRAME\_BACKED should be appropriately set for their associated page frames, and any internal accounting set up appropriately.

## [◆ ](#ga6ad421ad5671d9df3d96e03361f672e8)k\_mem\_paging\_backing\_store\_location\_free()

| void k\_mem\_paging\_backing\_store\_location\_free | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *location* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[demand_paging.h](demand__paging_8h.md)>`

Free a backing store location.

Any stored data may be discarded, and the location token associated with this address may be re-used for some other data page.

This function is invoked with interrupts locked.

Parameters
:   | location | Location token to free |
    | --- | --- |

## [◆ ](#ga1192487fdc8d63c025de42162fb204cd)k\_mem\_paging\_backing\_store\_location\_get()

| int k\_mem\_paging\_backing\_store\_location\_get | ( | struct k\_mem\_page\_frame \* | *pf*, |
| --- | --- | --- | --- |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \* | *location*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *page\_fault* ) |

`#include <[demand_paging.h](demand__paging_8h.md)>`

Reserve or fetch a storage location for a data page loaded into a page frame.

The returned location token must be unique to the mapped virtual address. This location will be used in the backing store to page out data page contents for later retrieval. The location value must be page-aligned.

This function may be called multiple times on the same data page. If its page frame has its K\_MEM\_PAGE\_FRAME\_BACKED bit set, it is expected to return the previous backing store location for the data page containing a cached clean copy. This clean copy may be updated on page-out, or used to discard clean pages without needing to write out their contents.

If the backing store is full, some other backing store location which caches a loaded data page may be selected, in which case its associated page frame will have the K\_MEM\_PAGE\_FRAME\_BACKED bit cleared (as it is no longer cached).

k\_mem\_page\_frame\_to\_virt(pf) will indicate the virtual address the page is currently mapped to. Large, sparse backing stores which can contain the entire address space may simply generate location tokens purely as a function of that virtual address with no other management necessary.

This function distinguishes whether it was called on behalf of a page fault. A free backing store location must always be reserved in order for page faults to succeed. If the page\_fault parameter is not set, this function should return -ENOMEM even if one location is available.

This function is invoked with interrupts locked.

Parameters
:   |  | pf | Virtual address to obtain a storage location |
    | --- | --- | --- |
    | [out] | location | storage location token |
    |  | page\_fault | Whether this request was for a page fault |

Returns
:   0 Success
:   -ENOMEM Backing store is full

## [◆ ](#ga25debe925b369765ecd5bd7777ce32d0)k\_mem\_paging\_backing\_store\_location\_query()

| int k\_mem\_paging\_backing\_store\_location\_query | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \* | *location* ) |

`#include <[demand_paging.h](demand__paging_8h.md)>`

Obtain persistent location token for on-demand content.

Unlike [k\_mem\_paging\_backing\_store\_location\_get()](#ga1192487fdc8d63c025de42162fb204cd) this does not allocate any backing store space. Instead, it returns a location token corresponding to some fixed storage content to be paged in on demand. This is expected to be used in conjonction with CONFIG\_LINKER\_USE\_ONDEMAND\_SECTION and the K\_MEM\_MAP\_UNPAGED flag to create demand mappings at boot time. This may also be used e.g. to implement file-based [mmap()](mman_8h.md#ac2e7d057b16f0c959ffb39d8719eb1ed).

Parameters
:   |  | addr | Virtual address to obtain a location token for |
    | --- | --- | --- |
    | [out] | location | storage location token |

Returns
:   0 for success or negative error code

## [◆ ](#ga8d4bd3ea311fd873413d0477e8deb464)k\_mem\_paging\_backing\_store\_page\_finalize()

| void k\_mem\_paging\_backing\_store\_page\_finalize | ( | struct k\_mem\_page\_frame \* | *pf*, |
| --- | --- | --- | --- |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *location* ) |

`#include <[demand_paging.h](demand__paging_8h.md)>`

Update internal accounting after a page-in.

This is invoked after [k\_mem\_paging\_backing\_store\_page\_in()](#ga9becb4908cc7840ece93a2360692962d) and interrupts have been\* re-locked, making it safe to access the k\_mem\_page\_frame data. The location value will be the same passed to [k\_mem\_paging\_backing\_store\_page\_in()](#ga9becb4908cc7840ece93a2360692962d).

The primary use-case for this is to update custom fields for the backing store in the page frame, to reflect where the data should be evicted to if it is paged out again. This may be a no-op in some implementations.

If the backing store caches paged-in data pages, this is the appropriate time to set the K\_MEM\_PAGE\_FRAME\_BACKED bit. The kernel only skips paging out clean data pages if they are noted as clean in the page tables and the K\_MEM\_PAGE\_FRAME\_BACKED bit is set in their associated page frame.

Parameters
:   | pf | Page frame that was loaded in |
    | --- | --- |
    | location | Location of where the loaded data page was retrieved |

## [◆ ](#ga9becb4908cc7840ece93a2360692962d)k\_mem\_paging\_backing\_store\_page\_in()

| void k\_mem\_paging\_backing\_store\_page\_in | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *location* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[demand_paging.h](demand__paging_8h.md)>`

Copy a data page from the provided location to K\_MEM\_SCRATCH\_PAGE.

Immediately before this is called, K\_MEM\_SCRATCH\_PAGE will be mapped read-write to the intended destination page frame for the calling context.

Calls to this and [k\_mem\_paging\_backing\_store\_page\_out()](#ga51f663e0a8c31367082e78097359af6d) will always be serialized, but interrupts may be enabled.

Parameters
:   | location | Location token for the data page |
    | --- | --- |

## [◆ ](#ga51f663e0a8c31367082e78097359af6d)k\_mem\_paging\_backing\_store\_page\_out()

| void k\_mem\_paging\_backing\_store\_page\_out | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *location* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[demand_paging.h](demand__paging_8h.md)>`

Copy a data page from K\_MEM\_SCRATCH\_PAGE to the specified location.

Immediately before this is called, K\_MEM\_SCRATCH\_PAGE will be mapped read-write to the intended source page frame for the calling context.

Calls to this and [k\_mem\_paging\_backing\_store\_page\_in()](#ga9becb4908cc7840ece93a2360692962d) will always be serialized, but interrupts may be enabled.

Parameters
:   | location | Location token for the data page, for later retrieval |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
