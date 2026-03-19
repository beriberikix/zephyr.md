---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__kernel__mm__internal__apis.html
original_path: doxygen/html/group__kernel__mm__internal__apis.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Kernel Memory Management Internal APIs

[Internal and System API](group__internal__api.md)

| Macros | |
| --- | --- |
| #define | [K\_MEM\_VIRT\_OFFSET](#gae9f618604758a034b52509c0377d1bdb) |
|  | Address offset of permanent virtual mapping from physical address. |
| #define | [K\_MEM\_PHYS\_ADDR](#ga49b13f5f43530952220fb223c3d56d3c)(virt) |
|  | Get physical address from virtual address. |
| #define | [K\_MEM\_VIRT\_ADDR](#ga850451db4842595d8d96e85a087e8964)(phys) |
|  | Get virtual address from physical address. |

| Functions | |
| --- | --- |
| static [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [k\_mem\_phys\_addr](#gadc2d4d6258059524eaba2ff139c2f9ff) (void \*virt) |
|  | Get physical address from virtual address. |
| static void \* | [k\_mem\_virt\_addr](#gaed8dccb2a3c15daff9d2e5b4d49f782a) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys) |
|  | Get virtual address from physical address. |
| void | [k\_mem\_map\_phys\_bare](#gaa2c52222198f4c7362c183e1397a4e5c) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*virt\_ptr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Map a physical memory region into the kernel's virtual address space. |
| void | [k\_mem\_unmap\_phys\_bare](#gae713c4eb253302d06f758f87503cf5dd) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*virt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Unmap a virtual memory region from kernel's virtual address space. |
| void \* | [k\_mem\_map\_phys\_guard](#ga2aeab99cba24ac3fd9479dbd421f6c5c) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_anon) |
|  | Map memory into virtual address space with guard pages. |
| void | [k\_mem\_unmap\_phys\_guard](#gaca476fbacb86815edd4898b13ecf5120) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_anon) |
|  | Un-map memory mapped via [k\_mem\_map\_phys\_guard()](#ga2aeab99cba24ac3fd9479dbd421f6c5c). |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga49b13f5f43530952220fb223c3d56d3c)K\_MEM\_PHYS\_ADDR

| #define K\_MEM\_PHYS\_ADDR | ( |  | *virt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mm.h](kernel_2internal_2mm_8h.md)>`

**Value:**

((virt) - [K\_MEM\_VIRT\_OFFSET](#gae9f618604758a034b52509c0377d1bdb))

[K\_MEM\_VIRT\_OFFSET](#gae9f618604758a034b52509c0377d1bdb)

#define K\_MEM\_VIRT\_OFFSET

Address offset of permanent virtual mapping from physical address.

**Definition** mm.h:41

Get physical address from virtual address.

This only works in the kernel's permanent mapping of RAM.

Parameters
:   | virt | Virtual address |
    | --- | --- |

Returns
:   Physical address.

## [◆ ](#ga850451db4842595d8d96e85a087e8964)K\_MEM\_VIRT\_ADDR

| #define K\_MEM\_VIRT\_ADDR | ( |  | *phys* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mm.h](kernel_2internal_2mm_8h.md)>`

**Value:**

((phys) + [K\_MEM\_VIRT\_OFFSET](#gae9f618604758a034b52509c0377d1bdb))

Get virtual address from physical address.

This only works in the kernel's permanent mapping of RAM.

Parameters
:   | phys | Physical address |
    | --- | --- |

Returns
:   Virtual address.

## [◆ ](#gae9f618604758a034b52509c0377d1bdb)K\_MEM\_VIRT\_OFFSET

| #define K\_MEM\_VIRT\_OFFSET |
| --- |

`#include <[mm.h](kernel_2internal_2mm_8h.md)>`

**Value:**

((CONFIG\_KERNEL\_VM\_BASE + CONFIG\_KERNEL\_VM\_OFFSET) - \

(CONFIG\_SRAM\_BASE\_ADDRESS + CONFIG\_SRAM\_OFFSET))

Address offset of permanent virtual mapping from physical address.

This is the offset to subtract from a virtual address mapped in the kernel's permanent mapping of RAM, to obtain its physical address.

```
virt_addr = phys_addr + K_MEM_VIRT_OFFSET
```

This only works for virtual addresses within the interval [CONFIG\_KERNEL\_VM\_BASE, CONFIG\_KERNEL\_VM\_BASE + (CONFIG\_SRAM\_SIZE \* 1024)).

These macros are intended for assembly, linker code, and static initializers. Use with care.

Note that when demand paging is active, these will only work with page frames that are pinned to their virtual mapping at boot.

TODO: This will likely need to move to an arch API or need additional constraints defined.

## Function Documentation

## [◆ ](#gaa2c52222198f4c7362c183e1397a4e5c)k\_mem\_map\_phys\_bare()

| void k\_mem\_map\_phys\_bare | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *virt\_ptr*, |
| --- | --- | --- | --- |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *phys*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) |

`#include <[mm.h](kernel_2internal_2mm_8h.md)>`

Map a physical memory region into the kernel's virtual address space.

This function is intended for mapping memory-mapped I/O regions into the virtual address space. Given a physical address and a size, return a linear address representing the base of where the physical region is mapped in the virtual address space for the Zephyr kernel.

The memory mapped via this function must be unmapped using [k\_mem\_unmap\_phys\_bare()](#gae713c4eb253302d06f758f87503cf5dd).

This function alters the active page tables in the area reserved for the kernel. This function will choose the virtual address and return it to the caller.

Portable code should never assume that phys\_addr and linear\_addr will be equal.

Caching and access properties are controlled by the 'flags' parameter. Unused bits in 'flags' are reserved for future expansion. A caching mode must be selected. By default, the region is read-only with user access and code execution forbidden. This policy is changed by passing K\_MEM\_CACHE\_\* and K\_MEM\_PERM\_\* macros into the 'flags' parameter.

If there is insufficient virtual address space for the mapping this will generate a kernel panic.

This API is only available if CONFIG\_MMU is enabled.

It is highly discouraged to use this function to map system RAM page frames. It may conflict with anonymous memory mappings and demand paging and produce undefined behavior. Do not use this for RAM unless you know exactly what you are doing. If you need a chunk of memory, use [k\_mem\_map()](group__kernel__memory__management.md#gacf5f9c43ac2c31c376fed4a19f607feb "Map anonymous memory into Zephyr's address space."). If you need a contiguous buffer of physical memory, statically declare it and pin it at build time, it will be mapped when the system boots.

This API is part of infrastructure still under development and may change.

Parameters
:   | [out] | virt\_ptr | Output virtual address storage location |
    | --- | --- | --- |
    | [in] | phys | Physical address base of the memory region |
    | [in] | size | Size of the memory region |
    | [in] | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Caching mode and access flags, see K\_MAP\_\* macros |

## [◆ ](#ga2aeab99cba24ac3fd9479dbd421f6c5c)k\_mem\_map\_phys\_guard()

| void \* k\_mem\_map\_phys\_guard | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *phys*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *is\_anon* ) |

`#include <[mm.h](kernel_2internal_2mm_8h.md)>`

Map memory into virtual address space with guard pages.

This maps memory into virtual address space with a preceding and a succeeding guard pages. The memory mapped via this function must be unmapped using [k\_mem\_unmap\_phys\_guard()](#gaca476fbacb86815edd4898b13ecf5120).

This function maps a contiguous physical memory region into kernel's virtual address space with a preceding and a succeeding guard pages. Given a physical address and a size, return a linear address representing the base of where the physical region is mapped in the virtual address space for the Zephyr kernel.

This function alters the active page tables in the area reserved for the kernel. This function will choose the virtual address and return it to the caller.

If user thread access control needs to be managed in any way, do not enable K\_MEM\_PERM\_USER flags here; instead manage the region's permissions with memory domain APIs after the mapping has been established. Setting K\_MEM\_PERM\_USER here will allow all user threads to access this memory which is usually undesirable.

Unless K\_MEM\_MAP\_UNINIT is used, the returned memory will be zeroed.

The returned virtual memory pointer will be page-aligned. The size parameter, and any base address for re-mapping purposes must be page- aligned.

Note that the allocation includes two guard pages immediately before and after the requested region. The total size of the allocation will be the requested size plus the size of these two guard pages.

Many K\_MEM\_MAP\_\* flags have been implemented to alter the behavior of this function, with details in the documentation for these flags.

See also
:   [k\_mem\_map()](group__kernel__memory__management.md#gacf5f9c43ac2c31c376fed4a19f607feb "Map anonymous memory into Zephyr's address space.") for additional information if called via that.

Parameters
:   | phys | Physical address base of the memory region if not requesting anonymous memory. Must be page-aligned. |
    | --- | --- |
    | size | Size of the memory mapping. This must be page-aligned. |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | K\_MEM\_PERM\_\*, K\_MEM\_MAP\_\* control flags. |
    | is\_anon | True is requesting mapping with anonymous memory. |

Returns
:   The mapped memory location, or NULL if insufficient virtual address space, insufficient physical memory to establish the mapping, or insufficient memory for paging structures.

## [◆ ](#gadc2d4d6258059524eaba2ff139c2f9ff)k\_mem\_phys\_addr()

| | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) k\_mem\_phys\_addr | ( | void \* | *virt* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mm.h](kernel_2internal_2mm_8h.md)>`

Get physical address from virtual address.

This only works in the kernel's permanent mapping of RAM.

Just like [K\_MEM\_PHYS\_ADDR()](#ga49b13f5f43530952220fb223c3d56d3c) but with type safety and assertions.

Parameters
:   | virt | Virtual address |
    | --- | --- |

Returns
:   Physical address.

## [◆ ](#gae713c4eb253302d06f758f87503cf5dd)k\_mem\_unmap\_phys\_bare()

| void k\_mem\_unmap\_phys\_bare | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *virt*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[mm.h](kernel_2internal_2mm_8h.md)>`

Unmap a virtual memory region from kernel's virtual address space.

This function is intended to be used by drivers and early boot routines where temporary memory mappings need to be made. This allows these memory mappings to be discarded once they are no longer needed.

This function alters the active page tables in the area reserved for the kernel.

This will align the input parameters to page boundaries so that this can be used with the virtual address as returned by [k\_mem\_map\_phys\_bare()](#gaa2c52222198f4c7362c183e1397a4e5c).

This API is only available if CONFIG\_MMU is enabled.

It is highly discouraged to use this function to unmap memory mappings. It may conflict with anonymous memory mappings and demand paging and produce undefined behavior. Do not use this unless you know exactly what you are doing.

This API is part of infrastructure still under development and may change.

Parameters
:   | virt | Starting address of the virtual address region to be unmapped. |
    | --- | --- |
    | size | Size of the virtual address region |

## [◆ ](#gaca476fbacb86815edd4898b13ecf5120)k\_mem\_unmap\_phys\_guard()

| void k\_mem\_unmap\_phys\_guard | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *is\_anon* ) |

`#include <[mm.h](kernel_2internal_2mm_8h.md)>`

Un-map memory mapped via [k\_mem\_map\_phys\_guard()](#ga2aeab99cba24ac3fd9479dbd421f6c5c).

This removes the memory mappings for the provided page-aligned region, and the two guard pages surrounding the region.

This function alters the active page tables in the area reserved for the kernel.

See also
:   [k\_mem\_unmap()](group__kernel__memory__management.md#ga1867ea13671daae6a5f38929ea9fd64a "Un-map mapped memory.") for additional information if called via that.

Note
:   Calling this function on a region which was not mapped via [k\_mem\_map\_phys\_guard()](#ga2aeab99cba24ac3fd9479dbd421f6c5c) to begin with is undefined behavior.

Parameters
:   | addr | Page-aligned memory region base virtual address |
    | --- | --- |
    | size | Page-aligned memory region size |
    | is\_anon | True if the mapped memory is from anonymous memory. |

## [◆ ](#gaed8dccb2a3c15daff9d2e5b4d49f782a)k\_mem\_virt\_addr()

| | void \* k\_mem\_virt\_addr | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *phys* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mm.h](kernel_2internal_2mm_8h.md)>`

Get virtual address from physical address.

This only works in the kernel's permanent mapping of RAM.

Just like [K\_MEM\_VIRT\_ADDR()](#ga850451db4842595d8d96e85a087e8964) but with type safety and assertions.

Parameters
:   | phys | Physical address |
    | --- | --- |

Returns
:   Virtual address.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
