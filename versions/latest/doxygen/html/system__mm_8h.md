---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/system__mm_8h.html
original_path: doxygen/html/system__mm_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

system\_mm.h File Reference

Memory Management Driver APIs.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](system__mm_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sys\_mm\_drv\_region](structsys__mm__drv__region.md) |
|  | Represents an available memory region. [More...](structsys__mm__drv__region.md#details) |

| Macros | |
| --- | --- |
| Caching mode definitions. | |
| These are mutually exclusive. | |
| #define | [SYS\_MM\_MEM\_CACHE\_NONE](group__mm__drv__apis.md#gafe1b7f8b4075da1b461f2a74d3142e49)   2 |
|  | No caching. |
| #define | [SYS\_MM\_MEM\_CACHE\_WT](group__mm__drv__apis.md#gaed12cd6841eb0fd0af1cefe1d7a6b5aa)   1 |
|  | Write-through caching. |
| #define | [SYS\_MM\_MEM\_CACHE\_WB](group__mm__drv__apis.md#gad0859fb79c8da1d1af0f38ea63064b8c)   0 |
|  | Full write-back caching. |
| #define | [SYS\_MM\_MEM\_CACHE\_MASK](group__mm__drv__apis.md#ga43050af5740a0449da7998b48f540817)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) - 1) |
|  | Reserved bits for cache modes. |
| Region permission attributes. | |
| Default should be read-only, no user, no exec. | |
| #define | [SYS\_MM\_MEM\_PERM\_RW](group__mm__drv__apis.md#ga8547ea32c40b038daa34ee76cbaee275)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Region will have read/write access (and not read-only). |
| #define | [SYS\_MM\_MEM\_PERM\_EXEC](group__mm__drv__apis.md#gac564b8d2148bd7c0ac07313f0fa9861c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Region will be executable (normally forbidden). |
| #define | [SYS\_MM\_MEM\_PERM\_USER](group__mm__drv__apis.md#gad86f6d8cbb3102ad3e8375d10cb4551c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Region will be accessible to user mode (normally supervisor-only). |

| Functions | |
| --- | --- |
| Memory Mapping and Unmapping | |
| On mapping and unmapping of memory. | |
| int | [sys\_mm\_drv\_map\_page](group__mm__drv__apis.md#ga7097d4d8880cb0c3d5db7623ffc11b26) (void \*virt, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Map one physical page into the virtual address space. |
| int | [sys\_mm\_drv\_map\_region](group__mm__drv__apis.md#ga1186a31d55b24791d800e8f0aef311da) (void \*virt, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Map a region of physical memory into the virtual address space. |
| int | [sys\_mm\_drv\_map\_array](group__mm__drv__apis.md#gab36baa1ed134e5a69ea16451991b920e) (void \*virt, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*phys, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) cnt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Map an array of physical memory into the virtual address space. |
| int | [sys\_mm\_drv\_unmap\_page](group__mm__drv__apis.md#gab78668dd05ab1d4d17ca5bbe3182b0eb) (void \*virt) |
|  | Remove mapping for one page of the provided virtual address. |
| int | [sys\_mm\_drv\_unmap\_region](group__mm__drv__apis.md#gadc3ed78e29aef49b7578b9090dcaacbc) (void \*virt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Remove mappings for a provided virtual address range. |
| int | [sys\_mm\_drv\_remap\_region](group__mm__drv__apis.md#gae46a4189560e314e96f8bee80b55b40b) (void \*virt\_old, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, void \*virt\_new) |
|  | Remap virtual pages into new address. |
| Memory Moving | |
| On moving already mapped memory. | |
| int | [sys\_mm\_drv\_move\_region](group__mm__drv__apis.md#ga3b2e4b2b359d4fcba104e43866d30d14) (void \*virt\_old, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, void \*virt\_new, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys\_new) |
|  | Physically move memory, with copy. |
| int | [sys\_mm\_drv\_move\_array](group__mm__drv__apis.md#gab172793104608d2a5acae0eb40c50177) (void \*virt\_old, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, void \*virt\_new, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*phys\_new, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) phys\_cnt) |
|  | Physically move memory, with copy. |
| Memory Mapping Attributes | |
| On manipulating attributes of already mapped memory. | |
| int | [sys\_mm\_drv\_update\_page\_flags](group__mm__drv__apis.md#ga188aebe0dcb10e8a4d620cf0bf9a0444) (void \*virt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Update memory page flags. |
| int | [sys\_mm\_drv\_update\_region\_flags](group__mm__drv__apis.md#ga60a9aa179216ed7ac5179c3a7eeb97d3) (void \*virt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Update memory region flags. |

| Memory Mappings Query | |
| --- | --- |
| On querying information on memory mappings. | |
| #define | [SYS\_MM\_DRV\_MEMORY\_REGION\_FOREACH](group__mm__drv__apis.md#gabd2c5de68d1976e4d0a8086523d66e7a)(regions, iter) |
|  | Iterates over an array of regions returned by [sys\_mm\_drv\_query\_memory\_regions](group__mm__drv__apis.md#gaf2c06488bd4ff3ecd1285ce7d70321c9 "Query available memory regions."). |
| int | [sys\_mm\_drv\_page\_phys\_get](group__mm__drv__apis.md#gaabbc2184a44f8c5c8cd98bf09a2cdc0f) (void \*virt, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*phys) |
|  | Get the mapped physical memory address from virtual address. |
| const struct [sys\_mm\_drv\_region](structsys__mm__drv__region.md) \* | [sys\_mm\_drv\_query\_memory\_regions](group__mm__drv__apis.md#gaf2c06488bd4ff3ecd1285ce7d70321c9) (void) |
|  | Query available memory regions. |
| void | [sys\_mm\_drv\_query\_memory\_regions\_free](group__mm__drv__apis.md#gab8d3585ffe98796a5c74d0bb9fc634d1) (const struct [sys\_mm\_drv\_region](structsys__mm__drv__region.md) \*regions) |
|  | Free the memory array returned by [sys\_mm\_drv\_query\_memory\_regions](group__mm__drv__apis.md#gaf2c06488bd4ff3ecd1285ce7d70321c9 "Query available memory regions."). |

## Detailed Description

Memory Management Driver APIs.

This contains APIs for a system-wide memory management driver. Only one instance is permitted on the system.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mm](dir_464cfbc388e9245b11da9b89dd2be842.md)
- [system\_mm.h](system__mm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
