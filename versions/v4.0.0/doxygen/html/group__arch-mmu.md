---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__arch-mmu.html
original_path: doxygen/html/group__arch-mmu.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Architecture-specific memory-mapping APIs

[Internal and System API](group__internal__api.md) » [Architecture Interface](group__arch-interface.md)

| Enumerations | |
| --- | --- |
| enum | [arch\_page\_location](#ga65e10c80055d7e695add000f2ccfbb0b) { [ARCH\_PAGE\_LOCATION\_PAGED\_OUT](#gga65e10c80055d7e695add000f2ccfbb0bacf9e624eac380ea2bfa37632c4d17a3a) , [ARCH\_PAGE\_LOCATION\_PAGED\_IN](#gga65e10c80055d7e695add000f2ccfbb0bae378a008f497ae10ab50cab06f8c36db) , [ARCH\_PAGE\_LOCATION\_BAD](#gga65e10c80055d7e695add000f2ccfbb0ba7ff70acdf02345b5fa4c42ed2b2adde9) } |
|  | Status of a particular page location. [More...](#ga65e10c80055d7e695add000f2ccfbb0b) |

| Functions | |
| --- | --- |
| void | [arch\_mem\_map](#ga627bee468e54bb2d5ebe6ac53bb7fc94) (void \*virt, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Map physical memory into the virtual address space. |
| void | [arch\_mem\_unmap](#ga8783e1d292510477b3816b6686d7d8cd) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Remove mappings for a provided virtual address range. |
| int | [arch\_page\_phys\_get](#gaa31a233dab4ad575a9a969de10965200) (void \*virt, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*phys) |
|  | Get the mapped physical memory address from virtual address. |
| void | [arch\_reserved\_pages\_update](#ga229fa5699ad47951235af494f3d2a06a) (void) |
|  | Update page frame database with reserved pages. |
| void | [arch\_mem\_page\_out](#ga4c13ffab5b5a5f8c93971c4d3b51bd8f) (void \*addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) location) |
|  | Update all page tables for a paged-out data page. |
| void | [arch\_mem\_page\_in](#ga3c446aea862e37d479a809582322b3ae) (void \*addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys) |
|  | Update all page tables for a paged-in data page. |
| void | [arch\_mem\_scratch](#gae4e82c3100b08bdfdcd9361d316735a1) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys) |
|  | Update current page tables for a temporary mapping. |
| enum [arch\_page\_location](#ga65e10c80055d7e695add000f2ccfbb0b) | [arch\_page\_location\_get](#ga74b3ce1173b91a8f82c25ef89f9fbbc0) (void \*addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*location) |
|  | Fetch location information about a page at a particular address. |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_page\_info\_get](#gae4db701524d0614d0104706dc2a03a6c) (void \*addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*location, \_Bool clear\_accessed) |
|  | Retrieve page characteristics from the page table(s). |

## Detailed Description

## Enumeration Type Documentation

## [◆ ](#ga65e10c80055d7e695add000f2ccfbb0b)arch\_page\_location

| enum [arch\_page\_location](#ga65e10c80055d7e695add000f2ccfbb0b) |
| --- |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Status of a particular page location.

| Enumerator | |
| --- | --- |
| ARCH\_PAGE\_LOCATION\_PAGED\_OUT | The page has been evicted to the backing store. |
| ARCH\_PAGE\_LOCATION\_PAGED\_IN | The page is resident in memory. |
| ARCH\_PAGE\_LOCATION\_BAD | The page is not mapped. |

## Function Documentation

## [◆ ](#ga627bee468e54bb2d5ebe6ac53bb7fc94)arch\_mem\_map()

| void arch\_mem\_map | ( | void \* | *virt*, |
| --- | --- | --- | --- |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *phys*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Map physical memory into the virtual address space.

This is a low-level interface to mapping pages into the address space. Behavior when providing unaligned addresses/sizes is undefined, these are assumed to be aligned to CONFIG\_MMU\_PAGE\_SIZE.

The core kernel handles all management of the virtual address space; by the time we invoke this function, we know exactly where this mapping will be established. If the page tables already had mappings installed for the virtual memory region, these will be overwritten.

If the target architecture supports multiple page sizes, currently only the smallest page size will be used.

The memory range itself is never accessed by this operation.

This API must be safe to call in ISRs or exception handlers. Calls to this API are assumed to be serialized, and indeed all usage will originate from kernel/mm.c which handles virtual memory management.

Architectures are expected to pre-allocate page tables for the entire address space, as defined by CONFIG\_KERNEL\_VM\_BASE and CONFIG\_KERNEL\_VM\_SIZE. This operation should never require any kind of allocation for paging structures.

Validation of arguments should be done via assertions.

This API is part of infrastructure still under development and may change.

Parameters
:   | virt | Page-aligned Destination virtual address to map |
    | --- | --- |
    | phys | Page-aligned Source physical address to map |
    | size | Page-aligned size of the mapped memory region in bytes |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Caching, access and control flags, see K\_MAP\_\* macros |

## [◆ ](#ga3c446aea862e37d479a809582322b3ae)arch\_mem\_page\_in()

| void arch\_mem\_page\_in | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *phys* ) |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Update all page tables for a paged-in data page.

This function:

- Maps the specified virtual data page address to the provided physical page frame address, such that future memory accesses will function as expected. Access and caching attributes are undisturbed.
- Clears any accounting for "accessed" and "dirty" states.

If multiple page tables are in use, this must update all page tables. This function is called with interrupts locked.

Calling this function on data pages which are already paged in is undefined behavior.

This API is part of infrastructure still under development and may change.

## [◆ ](#ga4c13ffab5b5a5f8c93971c4d3b51bd8f)arch\_mem\_page\_out()

| void arch\_mem\_page\_out | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *location* ) |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Update all page tables for a paged-out data page.

This function:

- Sets the data page virtual address to trigger a fault if accessed that can be distinguished from access violations or un-mapped pages.
- Saves the provided location value so that it can retrieved for that data page in the page fault handler.
- The location value semantics are undefined here but the value will be always be page-aligned. It could be 0.

If multiple page tables are in use, this must update all page tables. This function is called with interrupts locked.

Calling this function on data pages which are already paged out is undefined behavior.

This API is part of infrastructure still under development and may change.

## [◆ ](#gae4e82c3100b08bdfdcd9361d316735a1)arch\_mem\_scratch()

| void arch\_mem\_scratch | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *phys* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Update current page tables for a temporary mapping.

Map a physical page frame address to a special virtual address K\_MEM\_SCRATCH\_PAGE, with read/write access to supervisor mode, such that when this function returns, the calling context can read/write the page frame's contents from the K\_MEM\_SCRATCH\_PAGE address.

This mapping only needs to be done on the current set of page tables, as it is only used for a short period of time exclusively by the caller. This function is called with interrupts locked.

This API is part of infrastructure still under development and may change.

## [◆ ](#ga8783e1d292510477b3816b6686d7d8cd)arch\_mem\_unmap()

| void arch\_mem\_unmap | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Remove mappings for a provided virtual address range.

This is a low-level interface for un-mapping pages from the address space. When this completes, the relevant page table entries will be updated as if no mapping was ever made for that memory range. No previous context needs to be preserved. This function must update mappings in all active page tables.

Behavior when providing unaligned addresses/sizes is undefined, these are assumed to be aligned to CONFIG\_MMU\_PAGE\_SIZE.

Behavior when providing an address range that is not already mapped is undefined.

This function should never require memory allocations for paging structures, and it is not necessary to free any paging structures. Empty page tables due to all contained entries being un-mapped may remain in place.

Implementations must invalidate TLBs as necessary.

This API is part of infrastructure still under development and may change.

Parameters
:   | addr | Page-aligned base virtual address to un-map |
    | --- | --- |
    | size | Page-aligned region size |

## [◆ ](#gae4db701524d0614d0104706dc2a03a6c)arch\_page\_info\_get()

| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arch\_page\_info\_get | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \* | *location*, |
|  |  | \_Bool | *clear\_accessed* ) |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Retrieve page characteristics from the page table(s).

The architecture is responsible for maintaining "accessed" and "dirty" states of data pages to support marking eviction algorithms. This can either be directly supported by hardware or emulated by modifying protection policy to generate faults on reads or writes. In all cases the architecture must maintain this information in some way.

For the provided virtual address, report the logical OR of the accessed and dirty states for the relevant entries in all active page tables in the system if the page is mapped and not paged out.

If clear\_accessed is true, the ARCH\_DATA\_PAGE\_ACCESSED flag will be reset. This function will report its prior state. If multiple page tables are in use, this function clears accessed state in all of them.

This function is called with interrupts locked, so that the reported information can't become stale while decisions are being made based on it.

The return value may have other bits set which the caller must ignore.

Clearing accessed state for data pages that are not ARCH\_DATA\_PAGE\_LOADED is undefined behavior.

ARCH\_DATA\_PAGE\_DIRTY and ARCH\_DATA\_PAGE\_ACCESSED bits in the return value are only significant if ARCH\_DATA\_PAGE\_LOADED is set, otherwise ignore them.

ARCH\_DATA\_PAGE\_NOT\_MAPPED bit in the return value is only significant if ARCH\_DATA\_PAGE\_LOADED is un-set, otherwise ignore it.

Unless otherwise specified, virtual data pages have the same mappings across all page tables. Calling this function on data pages that are exceptions to this rule (such as the scratch page) is undefined behavior.

This API is part of infrastructure still under development and may change.

Parameters
:   |  | addr | Virtual address to look up in page tables |
    | --- | --- | --- |
    | [out] | location | If non-NULL, updated with either physical page frame address or backing store location depending on ARCH\_DATA\_PAGE\_LOADED state. This is not touched if ARCH\_DATA\_PAGE\_NOT\_MAPPED. |
    |  | clear\_accessed | Whether to clear ARCH\_DATA\_PAGE\_ACCESSED state |

Return values
:   | Value | with ARCH\_DATA\_PAGE\_\* bits set reflecting the data page configuration |
    | --- | --- |

## [◆ ](#ga74b3ce1173b91a8f82c25ef89f9fbbc0)arch\_page\_location\_get()

| enum [arch\_page\_location](#ga65e10c80055d7e695add000f2ccfbb0b) arch\_page\_location\_get | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \* | *location* ) |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Fetch location information about a page at a particular address.

The function only needs to query the current set of page tables as the information it reports must be common to all of them if multiple page tables are in use. If multiple page tables are active it is unnecessary to iterate over all of them. This may allow certain types of optimizations (such as reverse page table mapping on x86).

This function is called with interrupts locked, so that the reported information can't become stale while decisions are being made based on it.

Unless otherwise specified, virtual data pages have the same mappings across all page tables. Calling this function on data pages that are exceptions to this rule (such as the scratch page) is undefined behavior. Just check the currently installed page tables and return the information in that.

Parameters
:   |  | addr | Virtual data page address that took the page fault |
    | --- | --- | --- |
    | [out] | location | In the case of ARCH\_PAGE\_LOCATION\_PAGED\_OUT, the backing store location value used to retrieve the data page. In the case of ARCH\_PAGE\_LOCATION\_PAGED\_IN, the physical address the page is mapped to. |

Return values
:   | [ARCH\_PAGE\_LOCATION\_PAGED\_OUT](#gga65e10c80055d7e695add000f2ccfbb0bacf9e624eac380ea2bfa37632c4d17a3a) | The page was evicted to the backing store. |
    | --- | --- |
    | [ARCH\_PAGE\_LOCATION\_PAGED\_IN](#gga65e10c80055d7e695add000f2ccfbb0bae378a008f497ae10ab50cab06f8c36db) | The data page is resident in memory. |
    | [ARCH\_PAGE\_LOCATION\_BAD](#gga65e10c80055d7e695add000f2ccfbb0ba7ff70acdf02345b5fa4c42ed2b2adde9) | The page is un-mapped or otherwise has had invalid access |

## [◆ ](#gaa31a233dab4ad575a9a969de10965200)arch\_page\_phys\_get()

| int arch\_page\_phys\_get | ( | void \* | *virt*, |
| --- | --- | --- | --- |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \* | *phys* ) |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Get the mapped physical memory address from virtual address.

The function only needs to query the current set of page tables as the information it reports must be common to all of them if multiple page tables are in use. If multiple page tables are active it is unnecessary to iterate over all of them.

Unless otherwise specified, virtual pages have the same mappings across all page tables. Calling this function on data pages that are exceptions to this rule (such as the scratch page) is undefined behavior. Just check the currently installed page tables and return the information in that.

Parameters
:   |  | virt | Page-aligned virtual address |
    | --- | --- | --- |
    | [out] | phys | Mapped physical address (can be NULL if only checking if virtual address is mapped) |

Return values
:   | 0 | if mapping is found and valid |
    | --- | --- |
    | -EFAULT | if virtual address is not mapped |

## [◆ ](#ga229fa5699ad47951235af494f3d2a06a)arch\_reserved\_pages\_update()

| void arch\_reserved\_pages\_update | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Update page frame database with reserved pages.

Some page frames within system RAM may not be available for use. A good example of this is reserved regions in the first megabyte on PC-like systems.

Implementations of this function should mark all relevant entries in k\_mem\_page\_frames with K\_PAGE\_FRAME\_RESERVED. This function is called at early system initialization with mm\_lock held.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
