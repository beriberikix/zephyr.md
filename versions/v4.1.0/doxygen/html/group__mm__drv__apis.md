---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__mm__drv__apis.html
original_path: doxygen/html/group__mm__drv__apis.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Memory Management Driver APIs

[Operating System Services](group__os__services.md) » [Memory Management](group__memory__management.md)

Memory Management Driver APIs.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [sys\_mm\_drv\_region](structsys__mm__drv__region.md) |
|  | Represents an available memory region. [More...](structsys__mm__drv__region.md#details) |

| Memory Mapping and Unmapping | |
| --- | --- |
| On mapping and unmapping of memory. | |
| int | [sys\_mm\_drv\_map\_page](#ga7097d4d8880cb0c3d5db7623ffc11b26) (void \*virt, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Map one physical page into the virtual address space. |
| int | [sys\_mm\_drv\_map\_region](#ga1186a31d55b24791d800e8f0aef311da) (void \*virt, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Map a region of physical memory into the virtual address space. |
| int | [sys\_mm\_drv\_map\_array](#gab36baa1ed134e5a69ea16451991b920e) (void \*virt, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*phys, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) cnt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Map an array of physical memory into the virtual address space. |
| int | [sys\_mm\_drv\_unmap\_page](#gab78668dd05ab1d4d17ca5bbe3182b0eb) (void \*virt) |
|  | Remove mapping for one page of the provided virtual address. |
| int | [sys\_mm\_drv\_unmap\_region](#gadc3ed78e29aef49b7578b9090dcaacbc) (void \*virt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Remove mappings for a provided virtual address range. |
| int | [sys\_mm\_drv\_remap\_region](#gae46a4189560e314e96f8bee80b55b40b) (void \*virt\_old, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, void \*virt\_new) |
|  | Remap virtual pages into new address. |

| Memory Moving | |
| --- | --- |
| On moving already mapped memory. | |
| int | [sys\_mm\_drv\_move\_region](#ga3b2e4b2b359d4fcba104e43866d30d14) (void \*virt\_old, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, void \*virt\_new, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys\_new) |
|  | Physically move memory, with copy. |
| int | [sys\_mm\_drv\_move\_array](#gab172793104608d2a5acae0eb40c50177) (void \*virt\_old, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, void \*virt\_new, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*phys\_new, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) phys\_cnt) |
|  | Physically move memory, with copy. |

| Memory Mapping Attributes | |
| --- | --- |
| On manipulating attributes of already mapped memory. | |
| int | [sys\_mm\_drv\_update\_page\_flags](#ga188aebe0dcb10e8a4d620cf0bf9a0444) (void \*virt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Update memory page flags. |
| int | [sys\_mm\_drv\_update\_region\_flags](#ga60a9aa179216ed7ac5179c3a7eeb97d3) (void \*virt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Update memory region flags. |

| Memory Mappings Query | |
| --- | --- |
| On querying information on memory mappings. | |
| int | [sys\_mm\_drv\_page\_phys\_get](#gaabbc2184a44f8c5c8cd98bf09a2cdc0f) (void \*virt, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*phys) |
|  | Get the mapped physical memory address from virtual address. |
| const struct [sys\_mm\_drv\_region](structsys__mm__drv__region.md) \* | [sys\_mm\_drv\_query\_memory\_regions](#gaf2c06488bd4ff3ecd1285ce7d70321c9) (void) |
|  | Query available memory regions. |
| void | [sys\_mm\_drv\_query\_memory\_regions\_free](#gab8d3585ffe98796a5c74d0bb9fc634d1) (const struct [sys\_mm\_drv\_region](structsys__mm__drv__region.md) \*regions) |
|  | Free the memory array returned by [sys\_mm\_drv\_query\_memory\_regions](#gaf2c06488bd4ff3ecd1285ce7d70321c9). |
| #define | [SYS\_MM\_DRV\_MEMORY\_REGION\_FOREACH](#gabd2c5de68d1976e4d0a8086523d66e7a)(regions, iter) |
|  | Iterates over an array of regions returned by [sys\_mm\_drv\_query\_memory\_regions](#gaf2c06488bd4ff3ecd1285ce7d70321c9). |

| Caching mode definitions. | |
| --- | --- |
| These are mutually exclusive. | |
| #define | [SYS\_MM\_MEM\_CACHE\_NONE](#gafe1b7f8b4075da1b461f2a74d3142e49)   2 |
|  | No caching. |
| #define | [SYS\_MM\_MEM\_CACHE\_WT](#gaed12cd6841eb0fd0af1cefe1d7a6b5aa)   1 |
|  | Write-through caching. |
| #define | [SYS\_MM\_MEM\_CACHE\_WB](#gad0859fb79c8da1d1af0f38ea63064b8c)   0 |
|  | Full write-back caching. |
| #define | [SYS\_MM\_MEM\_CACHE\_MASK](#ga43050af5740a0449da7998b48f540817)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) - 1) |
|  | Reserved bits for cache modes. |

| Region permission attributes. | |
| --- | --- |
| Default should be read-only, no user, no exec. | |
| #define | [SYS\_MM\_MEM\_PERM\_RW](#ga8547ea32c40b038daa34ee76cbaee275)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Region will have read/write access (and not read-only). |
| #define | [SYS\_MM\_MEM\_PERM\_EXEC](#gac564b8d2148bd7c0ac07313f0fa9861c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Region will be executable (normally forbidden). |
| #define | [SYS\_MM\_MEM\_PERM\_USER](#gad86f6d8cbb3102ad3e8375d10cb4551c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Region will be accessible to user mode (normally supervisor-only). |

## Detailed Description

Memory Management Driver APIs.

This contains APIs for a system-wide memory management driver. Only one instance is permitted on the system.

## Macro Definition Documentation

## [◆ ](#gabd2c5de68d1976e4d0a8086523d66e7a)SYS\_MM\_DRV\_MEMORY\_REGION\_FOREACH

| #define SYS\_MM\_DRV\_MEMORY\_REGION\_FOREACH | ( |  | *regions*, |
| --- | --- | --- | --- |
|  |  |  | *iter* ) |

`#include <[system_mm.h](system__mm_8h.md)>`

**Value:**

for (iter = regions; iter->size; iter++)

Iterates over an array of regions returned by [sys\_mm\_drv\_query\_memory\_regions](#gaf2c06488bd4ff3ecd1285ce7d70321c9).

Note that a sentinel item marking the end of the array is expected for this macro to work.

## [◆ ](#ga43050af5740a0449da7998b48f540817)SYS\_MM\_MEM\_CACHE\_MASK

| #define SYS\_MM\_MEM\_CACHE\_MASK   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) - 1) |
| --- |

`#include <[system_mm.h](system__mm_8h.md)>`

Reserved bits for cache modes.

## [◆ ](#gafe1b7f8b4075da1b461f2a74d3142e49)SYS\_MM\_MEM\_CACHE\_NONE

| #define SYS\_MM\_MEM\_CACHE\_NONE   2 |
| --- |

`#include <[system_mm.h](system__mm_8h.md)>`

No caching.

## [◆ ](#gad0859fb79c8da1d1af0f38ea63064b8c)SYS\_MM\_MEM\_CACHE\_WB

| #define SYS\_MM\_MEM\_CACHE\_WB   0 |
| --- |

`#include <[system_mm.h](system__mm_8h.md)>`

Full write-back caching.

## [◆ ](#gaed12cd6841eb0fd0af1cefe1d7a6b5aa)SYS\_MM\_MEM\_CACHE\_WT

| #define SYS\_MM\_MEM\_CACHE\_WT   1 |
| --- |

`#include <[system_mm.h](system__mm_8h.md)>`

Write-through caching.

## [◆ ](#gac564b8d2148bd7c0ac07313f0fa9861c)SYS\_MM\_MEM\_PERM\_EXEC

| #define SYS\_MM\_MEM\_PERM\_EXEC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[system_mm.h](system__mm_8h.md)>`

Region will be executable (normally forbidden).

## [◆ ](#ga8547ea32c40b038daa34ee76cbaee275)SYS\_MM\_MEM\_PERM\_RW

| #define SYS\_MM\_MEM\_PERM\_RW   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[system_mm.h](system__mm_8h.md)>`

Region will have read/write access (and not read-only).

## [◆ ](#gad86f6d8cbb3102ad3e8375d10cb4551c)SYS\_MM\_MEM\_PERM\_USER

| #define SYS\_MM\_MEM\_PERM\_USER   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[system_mm.h](system__mm_8h.md)>`

Region will be accessible to user mode (normally supervisor-only).

## Function Documentation

## [◆ ](#gab36baa1ed134e5a69ea16451991b920e)sys\_mm\_drv\_map\_array()

| int sys\_mm\_drv\_map\_array | ( | void \* | *virt*, |
| --- | --- | --- | --- |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \* | *phys*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *cnt*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) |

`#include <[system_mm.h](system__mm_8h.md)>`

Map an array of physical memory into the virtual address space.

This maps an array of physical pages into a continuous virtual address space. Behavior when providing unaligned addresses is undefined, these are assumed to be page aligned.

The physical memory pages are never accessed by this operation.

This API must be safe to call in ISRs or exception handlers. Calls to this API are assumed to be serialized.

Parameters
:   | virt | Page-aligned destination virtual address to map |
    | --- | --- |
    | phys | Array of pge-aligned source physical address to map |
    | cnt | Number of elements in the physical page array |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Caching, access and control flags, see SYS\_MM\_MEM\_\* macros |

Return values
:   | 0 | if successful |
    | --- | --- |
    | -EINVAL | if invalid arguments are provided |
    | -EFAULT | if any virtual addresses have already been mapped |

## [◆ ](#ga7097d4d8880cb0c3d5db7623ffc11b26)sys\_mm\_drv\_map\_page()

| int sys\_mm\_drv\_map\_page | ( | void \* | *virt*, |
| --- | --- | --- | --- |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *phys*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) |

`#include <[system_mm.h](system__mm_8h.md)>`

Map one physical page into the virtual address space.

This maps one physical page into the virtual address space. Behavior when providing unaligned address is undefined, this is assumed to be page aligned.

The memory range itself is never accessed by this operation.

This API must be safe to call in ISRs or exception handlers. Calls to this API are assumed to be serialized.

Parameters
:   | virt | Page-aligned destination virtual address to map |
    | --- | --- |
    | phys | Page-aligned source physical address to map |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Caching, access and control flags, see SYS\_MM\_MEM\_\* macros |

Return values
:   | 0 | if successful |
    | --- | --- |
    | -EINVAL | if invalid arguments are provided |
    | -EFAULT | if virtual address has already been mapped |

## [◆ ](#ga1186a31d55b24791d800e8f0aef311da)sys\_mm\_drv\_map\_region()

| int sys\_mm\_drv\_map\_region | ( | void \* | *virt*, |
| --- | --- | --- | --- |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *phys*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) |

`#include <[system_mm.h](system__mm_8h.md)>`

Map a region of physical memory into the virtual address space.

This maps a region of physical memory into the virtual address space. Behavior when providing unaligned addresses/sizes is undefined, these are assumed to be page aligned.

The memory range itself is never accessed by this operation.

This API must be safe to call in ISRs or exception handlers. Calls to this API are assumed to be serialized.

Parameters
:   | virt | Page-aligned destination virtual address to map |
    | --- | --- |
    | phys | Page-aligned source physical address to map |
    | size | Page-aligned size of the mapped memory region in bytes |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Caching, access and control flags, see SYS\_MM\_MEM\_\* macros |

Return values
:   | 0 | if successful |
    | --- | --- |
    | -EINVAL | if invalid arguments are provided |
    | -EFAULT | if any virtual addresses have already been mapped |

## [◆ ](#gab172793104608d2a5acae0eb40c50177)sys\_mm\_drv\_move\_array()

| int sys\_mm\_drv\_move\_array | ( | void \* | *virt\_old*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | void \* | *virt\_new*, |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \* | *phys\_new*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *phys\_cnt* ) |

`#include <[system_mm.h](system__mm_8h.md)>`

Physically move memory, with copy.

This maps a region of physical memory into the new virtual address space (`virt_new`), and copy region of size `size` from the old virtual address space (`virt_old`). The new virtual memory region is mapped from an array of physical pages.

Behavior when providing unaligned addresses/sizes is undefined, these are assumed to be page aligned.

Note that the virtual memory at both the old and new addresses must be unmapped in the memory domains of any runnable Zephyr thread as this does not deal with memory domains.

Note that overlapping of old and new virtual memory regions is usually not supported for simpler implementation. Refer to the actual driver to make sure if overlapping is allowed.

Parameters
:   | virt\_old | Page-aligned base virtual address of existing memory |
    | --- | --- |
    | size | Page-aligned size of the mapped memory region in bytes |
    | virt\_new | Page-aligned base virtual address to which to map new physical pages |
    | phys\_new | Array of page-aligned physical address to contain the moved memory |
    | phys\_cnt | Number of elements in the physical page array |

Return values
:   | 0 | if successful |
    | --- | --- |
    | -EINVAL | if invalid arguments are provided |
    | -EFAULT | if old virtual addresses are not all mapped or new virtual addresses are not all unmapped |

## [◆ ](#ga3b2e4b2b359d4fcba104e43866d30d14)sys\_mm\_drv\_move\_region()

| int sys\_mm\_drv\_move\_region | ( | void \* | *virt\_old*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | void \* | *virt\_new*, |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *phys\_new* ) |

`#include <[system_mm.h](system__mm_8h.md)>`

Physically move memory, with copy.

This maps a region of physical memory into the new virtual address space (`virt_new`), and copy region of size `size` from the old virtual address space (`virt_old`). The new virtual memory region is mapped from physical memory starting at `phys_new` of size `size`.

Behavior when providing unaligned addresses/sizes is undefined, these are assumed to be page aligned.

Note that the virtual memory at both the old and new addresses must be unmapped in the memory domains of any runnable Zephyr thread as this does not deal with memory domains.

Note that overlapping of old and new virtual memory regions is usually not supported for simpler implementation. Refer to the actual driver to make sure if overlapping is allowed.

Parameters
:   | virt\_old | Page-aligned base virtual address of existing memory |
    | --- | --- |
    | size | Page-aligned size of the mapped memory region in bytes |
    | virt\_new | Page-aligned base virtual address to which to map new physical pages |
    | phys\_new | Page-aligned base physical address to contain the moved memory |

Return values
:   | 0 | if successful |
    | --- | --- |
    | -EINVAL | if invalid arguments are provided |
    | -EFAULT | if old virtual addresses are not all mapped or new virtual addresses are not all unmapped |

## [◆ ](#gaabbc2184a44f8c5c8cd98bf09a2cdc0f)sys\_mm\_drv\_page\_phys\_get()

| int sys\_mm\_drv\_page\_phys\_get | ( | void \* | *virt*, |
| --- | --- | --- | --- |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \* | *phys* ) |

`#include <[system_mm.h](system__mm_8h.md)>`

Get the mapped physical memory address from virtual address.

The function queries the translation tables to find the physical memory address of a mapped virtual address.

Behavior when providing unaligned address is undefined, this is assumed to be page aligned.

Parameters
:   |  | virt | Page-aligned virtual address |
    | --- | --- | --- |
    | [out] | phys | Mapped physical address (can be NULL if only checking if virtual address is mapped) |

Return values
:   | 0 | if mapping is found and valid |
    | --- | --- |
    | -EINVAL | if invalid arguments are provided |
    | -EFAULT | if virtual address is not mapped |

## [◆ ](#gaf2c06488bd4ff3ecd1285ce7d70321c9)sys\_mm\_drv\_query\_memory\_regions()

| const struct [sys\_mm\_drv\_region](structsys__mm__drv__region.md) \* sys\_mm\_drv\_query\_memory\_regions | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[system_mm.h](system__mm_8h.md)>`

Query available memory regions.

Returns an array of available memory regions. One can iterate over the array using [SYS\_MM\_DRV\_MEMORY\_REGION\_FOREACH](#gabd2c5de68d1976e4d0a8086523d66e7a). Note that the last item of the array is a sentinel marking the end, and it's identified by it's size attribute, which is zero.

Return values
:   | regions | A possibly empty array - i.e. containing only the sentinel marking at the end - of memory regions. |
    | --- | --- |

## [◆ ](#gab8d3585ffe98796a5c74d0bb9fc634d1)sys\_mm\_drv\_query\_memory\_regions\_free()

| void sys\_mm\_drv\_query\_memory\_regions\_free | ( | const struct [sys\_mm\_drv\_region](structsys__mm__drv__region.md) \* | *regions* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[system_mm.h](system__mm_8h.md)>`

Free the memory array returned by [sys\_mm\_drv\_query\_memory\_regions](#gaf2c06488bd4ff3ecd1285ce7d70321c9).

The driver may have dynamically allocated the memory for the array of regions returned by [sys\_mm\_drv\_query\_memory\_regions](#gaf2c06488bd4ff3ecd1285ce7d70321c9). This method provides it the opportunity to free any related resources.

Parameters
:   | regions | Array of regions previously returned by [sys\_mm\_drv\_query\_memory\_regions](#gaf2c06488bd4ff3ecd1285ce7d70321c9) |
    | --- | --- |

## [◆ ](#gae46a4189560e314e96f8bee80b55b40b)sys\_mm\_drv\_remap\_region()

| int sys\_mm\_drv\_remap\_region | ( | void \* | *virt\_old*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | void \* | *virt\_new* ) |

`#include <[system_mm.h](system__mm_8h.md)>`

Remap virtual pages into new address.

This remaps a virtual memory region starting at `virt_old` of size `size` into a new virtual memory region starting at `virt_new`. In other words, physical memory at `virt_old` is remapped to appear at `virt_new`. Both addresses must be page aligned and valid.

Note that the virtual memory at both the old and new addresses must be unmapped in the memory domains of any runnable Zephyr thread as this does not deal with memory domains.

Note that overlapping of old and new virtual memory regions is usually not supported for simpler implementation. Refer to the actual driver to make sure if overlapping is allowed.

Parameters
:   | virt\_old | Page-aligned base virtual address of existing memory |
    | --- | --- |
    | size | Page-aligned size of the mapped memory region in bytes |
    | virt\_new | Page-aligned base virtual address to which to remap the memory |

Return values
:   | 0 | if successful |
    | --- | --- |
    | -EINVAL | if invalid arguments are provided |
    | -EFAULT | if old virtual addresses are not all mapped or new virtual addresses are not all unmapped |

## [◆ ](#gab78668dd05ab1d4d17ca5bbe3182b0eb)sys\_mm\_drv\_unmap\_page()

| int sys\_mm\_drv\_unmap\_page | ( | void \* | *virt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[system_mm.h](system__mm_8h.md)>`

Remove mapping for one page of the provided virtual address.

This unmaps one page from the virtual address space.

When this completes, the relevant translation table entries will be updated as if no mapping was ever made for that memory page. No previous context needs to be preserved. This function must update mapping in all active translation tables.

Behavior when providing unaligned address is undefined, this is assumed to be page aligned.

Implementations must invalidate translation caching as necessary.

Parameters
:   | virt | Page-aligned virtual address to un-map |
    | --- | --- |

Return values
:   | 0 | if successful |
    | --- | --- |
    | -EINVAL | if invalid arguments are provided |
    | -EFAULT | if virtual address is not mapped |

## [◆ ](#gadc3ed78e29aef49b7578b9090dcaacbc)sys\_mm\_drv\_unmap\_region()

| int sys\_mm\_drv\_unmap\_region | ( | void \* | *virt*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[system_mm.h](system__mm_8h.md)>`

Remove mappings for a provided virtual address range.

This unmaps pages in the provided virtual address range.

When this completes, the relevant translation table entries will be updated as if no mapping was ever made for that memory range. No previous context needs to be preserved. This function must update mappings in all active translation tables.

Behavior when providing unaligned address is undefined, this is assumed to be page aligned.

Implementations must invalidate translation caching as necessary.

Parameters
:   | virt | Page-aligned base virtual address to un-map |
    | --- | --- |
    | size | Page-aligned region size |

Return values
:   | 0 | if successful |
    | --- | --- |
    | -EINVAL | if invalid arguments are provided |
    | -EFAULT | if virtual address is not mapped |

## [◆ ](#ga188aebe0dcb10e8a4d620cf0bf9a0444)sys\_mm\_drv\_update\_page\_flags()

| int sys\_mm\_drv\_update\_page\_flags | ( | void \* | *virt*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) |

`#include <[system_mm.h](system__mm_8h.md)>`

Update memory page flags.

This changes the attributes of physical memory page which is already mapped to a virtual address. This is useful when use case of specific memory region changes. E.g. when the library/module code is copied to the memory then it needs to be read-write and after it has already been copied and library/module code is ready to be executed then attributes need to be changed to read-only/executable. Calling this API must not cause losing memory contents.

Parameters
:   | virt | Page-aligned virtual address to be updated |
    | --- | --- |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Caching, access and control flags, see SYS\_MM\_MEM\_\* macros |

Return values
:   | 0 | if successful |
    | --- | --- |
    | -EINVAL | if invalid arguments are provided |
    | -EFAULT | if virtual addresses is not mapped |

## [◆ ](#ga60a9aa179216ed7ac5179c3a7eeb97d3)sys\_mm\_drv\_update\_region\_flags()

| int sys\_mm\_drv\_update\_region\_flags | ( | void \* | *virt*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) |

`#include <[system_mm.h](system__mm_8h.md)>`

Update memory region flags.

This changes the attributes of physical memory which is already mapped to a virtual address. This is useful when use case of specific memory region changes. E.g. when the library/module code is copied to the memory then it needs to be read-write and after it has already been copied and library/module code is ready to be executed then attributes need to be changed to read-only/executable. Calling this API must not cause losing memory contents.

Parameters
:   | virt | Page-aligned virtual address to be updated |
    | --- | --- |
    | size | Page-aligned size of the mapped memory region in bytes |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Caching, access and control flags, see SYS\_MM\_MEM\_\* macros |

Return values
:   | 0 | if successful |
    | --- | --- |
    | -EINVAL | if invalid arguments are provided |
    | -EFAULT | if virtual addresses is not mapped |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
