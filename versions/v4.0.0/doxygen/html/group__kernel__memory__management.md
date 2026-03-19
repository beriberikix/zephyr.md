---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__kernel__memory__management.html
original_path: doxygen/html/group__kernel__memory__management.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Kernel Memory Management

[Kernel APIs](group__kernel__apis.md)

Kernel Memory Management.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Demand Paging](group__demand__paging.md) |

| Functions | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [k\_mem\_free\_get](#gabb315b4994193147e9f51b0c3268bfcd) (void) |
|  | Return the amount of free memory available. |
| static void \* | [k\_mem\_map](#gacf5f9c43ac2c31c376fed4a19f607feb) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Map anonymous memory into Zephyr's address space. |
| static void | [k\_mem\_unmap](#ga1867ea13671daae6a5f38929ea9fd64a) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Un-map mapped memory. |
| int | [k\_mem\_update\_flags](#gaf4740377cd87525fc81fa2ddafef084d) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Modify memory mapping attribute flags. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [k\_mem\_region\_align](#gad9a0110394e8026e27deb15687321ee9) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*aligned\_addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*aligned\_size, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align) |
|  | Given an arbitrary region, provide a aligned region that covers it. |

| Caching mode definitions. | |
| --- | --- |
| These are mutually exclusive. | |
| #define | [K\_MEM\_CACHE\_NONE](#gaae7605452be94d1bd6e0364e9db113c6)   2 |
|  | No caching. |
| #define | [K\_MEM\_CACHE\_WT](#ga1c8d5fee98c68b08cc6acf781eb35320)   1 |
|  | Write-through caching. |
| #define | [K\_MEM\_CACHE\_WB](#ga802a69d7a53cafcf357861ab50258c99)   0 |
|  | Full write-back caching. |
| #define | [K\_MEM\_CACHE\_MASK](#gaae828c97c7bae5d235b863ff3b6b913e)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) - 1) |
|  | Reserved bits for cache modes in k\_map() flags argument. |

| Region permission attributes. | |
| --- | --- |
| Default is read-only, no user, no exec | |
| #define | [K\_MEM\_PERM\_RW](#gab9ea94b7155e276f0b653bc1a081866e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Region will have read/write access (and not read-only). |
| #define | [K\_MEM\_PERM\_EXEC](#gaf1b0db3c1c5b28b1810f39cdac03f9de)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Region will be executable (normally forbidden). |
| #define | [K\_MEM\_PERM\_USER](#gaa96222e46728d507ca229796a5724425)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Region will be accessible to user mode (normally supervisor-only). |

| Region mapping behaviour attributes | |
| --- | --- |
| #define | [K\_MEM\_DIRECT\_MAP](#ga36c4d2ede2f91490bc20ec399df663be)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Region will be mapped to 1:1 virtual and physical address. |

| k\_mem\_map() control flags | |
| --- | --- |
| #define | [K\_MEM\_MAP\_UNINIT](#ga0a3569731c9a9f8e94e913f840b4be61)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16) |
|  | The mapped region is not guaranteed to be zeroed. |
| #define | [K\_MEM\_MAP\_LOCK](#ga7bed120eac76f03a55b1ab8a1f61ce8b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17) |
|  | Region will be pinned in memory and never paged. |
| #define | [K\_MEM\_MAP\_UNPAGED](#ga1275f42967e72f16c58bc3351656bced)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18) |
|  | Region will be unpaged i.e. |

## Detailed Description

Kernel Memory Management.

## Macro Definition Documentation

## [◆ ](#gaae828c97c7bae5d235b863ff3b6b913e)K\_MEM\_CACHE\_MASK

| #define K\_MEM\_CACHE\_MASK   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) - 1) |
| --- |

`#include <[mm.h](kernel_2mm_8h.md)>`

Reserved bits for cache modes in k\_map() flags argument.

## [◆ ](#gaae7605452be94d1bd6e0364e9db113c6)K\_MEM\_CACHE\_NONE

| #define K\_MEM\_CACHE\_NONE   2 |
| --- |

`#include <[mm.h](kernel_2mm_8h.md)>`

No caching.

Most drivers want this.

## [◆ ](#ga802a69d7a53cafcf357861ab50258c99)K\_MEM\_CACHE\_WB

| #define K\_MEM\_CACHE\_WB   0 |
| --- |

`#include <[mm.h](kernel_2mm_8h.md)>`

Full write-back caching.

Any RAM mapped wants this.

## [◆ ](#ga1c8d5fee98c68b08cc6acf781eb35320)K\_MEM\_CACHE\_WT

| #define K\_MEM\_CACHE\_WT   1 |
| --- |

`#include <[mm.h](kernel_2mm_8h.md)>`

Write-through caching.

Used by certain drivers.

## [◆ ](#ga36c4d2ede2f91490bc20ec399df663be)K\_MEM\_DIRECT\_MAP

| #define K\_MEM\_DIRECT\_MAP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

`#include <[mm.h](kernel_2mm_8h.md)>`

Region will be mapped to 1:1 virtual and physical address.

## [◆ ](#ga7bed120eac76f03a55b1ab8a1f61ce8b)K\_MEM\_MAP\_LOCK

| #define K\_MEM\_MAP\_LOCK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17) |
| --- |

`#include <[mm.h](kernel_2mm_8h.md)>`

Region will be pinned in memory and never paged.

Such memory is guaranteed to never produce a page fault due to page-outs or copy-on-write once the mapping call has returned. Physical page frames will be pre-fetched as necessary and pinned.

## [◆ ](#ga0a3569731c9a9f8e94e913f840b4be61)K\_MEM\_MAP\_UNINIT

| #define K\_MEM\_MAP\_UNINIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16) |
| --- |

`#include <[mm.h](kernel_2mm_8h.md)>`

The mapped region is not guaranteed to be zeroed.

This may improve performance. The associated page frames may contain indeterminate data, zeroes, or even sensitive information.

This may not be used with K\_MEM\_PERM\_USER as there are no circumstances where this is safe.

## [◆ ](#ga1275f42967e72f16c58bc3351656bced)K\_MEM\_MAP\_UNPAGED

| #define K\_MEM\_MAP\_UNPAGED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18) |
| --- |

`#include <[mm.h](kernel_2mm_8h.md)>`

Region will be unpaged i.e.

not mapped into memory

This is meant to be used by kernel code and not by application code.

Corresponding memory address range will be set so no actual memory will be allocated initially. Allocation will happen through demand paging when addresses in that range are accessed. This is incompatible with K\_MEM\_MAP\_LOCK.

When this flag is specified, the phys argument to [arch\_mem\_map()](group__arch-mmu.md#ga627bee468e54bb2d5ebe6ac53bb7fc94 "Map physical memory into the virtual address space.") is interpreted as a backing store location value not a physical address. This is very similar to [arch\_mem\_page\_out()](group__arch-mmu.md#ga4c13ffab5b5a5f8c93971c4d3b51bd8f "Update all page tables for a paged-out data page.") in that regard. Two special location values are defined: ARCH\_UNPAGED\_ANON\_ZERO and ARCH\_UNPAGED\_ANON\_UNINIT. Those are to be used with anonymous memory mappings for zeroed and uninitialized pages respectively.

## [◆ ](#gaf1b0db3c1c5b28b1810f39cdac03f9de)K\_MEM\_PERM\_EXEC

| #define K\_MEM\_PERM\_EXEC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[mm.h](kernel_2mm_8h.md)>`

Region will be executable (normally forbidden).

## [◆ ](#gab9ea94b7155e276f0b653bc1a081866e)K\_MEM\_PERM\_RW

| #define K\_MEM\_PERM\_RW   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[mm.h](kernel_2mm_8h.md)>`

Region will have read/write access (and not read-only).

## [◆ ](#gaa96222e46728d507ca229796a5724425)K\_MEM\_PERM\_USER

| #define K\_MEM\_PERM\_USER   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[mm.h](kernel_2mm_8h.md)>`

Region will be accessible to user mode (normally supervisor-only).

## Function Documentation

## [◆ ](#gabb315b4994193147e9f51b0c3268bfcd)k\_mem\_free\_get()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) k\_mem\_free\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mm.h](kernel_2mm_8h.md)>`

Return the amount of free memory available.

The returned value will reflect how many free RAM page frames are available. If demand paging is enabled, it may still be possible to allocate more.

The information reported by this function may go stale immediately if concurrent memory mappings or page-ins take place.

Returns
:   Free physical RAM, in bytes

## [◆ ](#gacf5f9c43ac2c31c376fed4a19f607feb)k\_mem\_map()

| | void \* k\_mem\_map | ( | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mm.h](kernel_2mm_8h.md)>`

Map anonymous memory into Zephyr's address space.

This function effectively increases the data space available to Zephyr. The kernel will choose a base virtual address and return it to the caller. The memory will have access permissions for all contexts set per the provided flags argument.

If user thread access control needs to be managed in any way, do not enable K\_MEM\_PERM\_USER flags here; instead manage the region's permissions with memory domain APIs after the mapping has been established. Setting K\_MEM\_PERM\_USER here will allow all user threads to access this memory which is usually undesirable.

Unless K\_MEM\_MAP\_UNINIT is used, the returned memory will be zeroed.

The mapped region is not guaranteed to be physically contiguous in memory. Physically contiguous buffers should be allocated statically and pinned at build time.

Pages mapped in this way have write-back cache settings.

The returned virtual memory pointer will be page-aligned. The size parameter, and any base address for re-mapping purposes must be page- aligned.

Note that the allocation includes two guard pages immediately before and after the requested region. The total size of the allocation will be the requested size plus the size of these two guard pages.

Many K\_MEM\_MAP\_\* flags have been implemented to alter the behavior of this function, with details in the documentation for these flags.

Parameters
:   | size | Size of the memory mapping. This must be page-aligned. |
    | --- | --- |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | K\_MEM\_PERM\_\*, K\_MEM\_MAP\_\* control flags. |

Returns
:   The mapped memory location, or NULL if insufficient virtual address space, insufficient physical memory to establish the mapping, or insufficient memory for paging structures.

## [◆ ](#gad9a0110394e8026e27deb15687321ee9)k\_mem\_region\_align()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) k\_mem\_region\_align | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \* | *aligned\_addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *aligned\_size*, |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *addr*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *align* ) |

`#include <[mm.h](kernel_2mm_8h.md)>`

Given an arbitrary region, provide a aligned region that covers it.

The returned region will have both its base address and size aligned to the provided alignment value.

Parameters
:   | [out] | aligned\_addr | Aligned address |
    | --- | --- | --- |
    | [out] | aligned\_size | Aligned region size |
    | [in] | addr | Region base address |
    | [in] | size | Region size |
    | [in] | align | What to align the address and size to |

Return values
:   | offset | between aligned\_addr and addr |
    | --- | --- |

## [◆ ](#ga1867ea13671daae6a5f38929ea9fd64a)k\_mem\_unmap()

| | void k\_mem\_unmap | ( | void \* | *addr*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mm.h](kernel_2mm_8h.md)>`

Un-map mapped memory.

This removes a memory mapping for the provided page-aligned region. Associated page frames will be free and the kernel may re-use the associated virtual address region. Any paged out data pages may be discarded.

Calling this function on a region which was not mapped to begin with is undefined behavior.

Parameters
:   | addr | Page-aligned memory region base virtual address |
    | --- | --- |
    | size | Page-aligned memory region size |

## [◆ ](#gaf4740377cd87525fc81fa2ddafef084d)k\_mem\_update\_flags()

| int k\_mem\_update\_flags | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) |

`#include <[mm.h](kernel_2mm_8h.md)>`

Modify memory mapping attribute flags.

This updates caching, access and control flags for the provided page-aligned memory region.

Calling this function on a region which was not mapped to begin with is undefined behavior. However system memory implicitly mapped at boot time is supported.

Parameters
:   | addr | Page-aligned memory region base virtual address |
    | --- | --- |
    | size | Page-aligned memory region size |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | K\_MEM\_PERM\_\*, K\_MEM\_MAP\_\* control flags. |

Returns
:   0 for success, negative error code otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
