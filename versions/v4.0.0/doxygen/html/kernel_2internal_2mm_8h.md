---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/kernel_2internal_2mm_8h.html
original_path: doxygen/html/kernel_2internal_2mm_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mm.h File Reference

`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[inttypes.h](inttypes_8h_source.md)>`  
`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/sys/mem_manage.h](mem__manage_8h_source.md)>`

[Go to the source code of this file.](kernel_2internal_2mm_8h_source.md)

| Macros | |
| --- | --- |
| #define | [K\_MEM\_VIRT\_OFFSET](group__kernel__mm__internal__apis.md#gae9f618604758a034b52509c0377d1bdb) |
|  | Address offset of permanent virtual mapping from physical address. |
| #define | [K\_MEM\_PHYS\_ADDR](group__kernel__mm__internal__apis.md#ga49b13f5f43530952220fb223c3d56d3c)(virt) |
|  | Get physical address from virtual address. |
| #define | [K\_MEM\_VIRT\_ADDR](group__kernel__mm__internal__apis.md#ga850451db4842595d8d96e85a087e8964)(phys) |
|  | Get virtual address from physical address. |

| Functions | |
| --- | --- |
| static [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [k\_mem\_phys\_addr](group__kernel__mm__internal__apis.md#gadc2d4d6258059524eaba2ff139c2f9ff) (void \*virt) |
|  | Get physical address from virtual address. |
| static void \* | [k\_mem\_virt\_addr](group__kernel__mm__internal__apis.md#gaed8dccb2a3c15daff9d2e5b4d49f782a) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys) |
|  | Get virtual address from physical address. |
| void | [k\_mem\_map\_phys\_bare](group__kernel__mm__internal__apis.md#gaa2c52222198f4c7362c183e1397a4e5c) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*virt\_ptr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Map a physical memory region into the kernel's virtual address space. |
| void | [k\_mem\_unmap\_phys\_bare](group__kernel__mm__internal__apis.md#gae713c4eb253302d06f758f87503cf5dd) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*virt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Unmap a virtual memory region from kernel's virtual address space. |
| void \* | [k\_mem\_map\_phys\_guard](group__kernel__mm__internal__apis.md#ga2aeab99cba24ac3fd9479dbd421f6c5c) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_anon) |
|  | Map memory into virtual address space with guard pages. |
| void | [k\_mem\_unmap\_phys\_guard](group__kernel__mm__internal__apis.md#gaca476fbacb86815edd4898b13ecf5120) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_anon) |
|  | Un-map memory mapped via [k\_mem\_map\_phys\_guard()](group__kernel__mm__internal__apis.md#ga2aeab99cba24ac3fd9479dbd421f6c5c "Map memory into virtual address space with guard pages."). |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel](dir_87084789f4f879979d9b1b0acd11eedc.md)
- [internal](dir_5a28aaecc3642d39af859931377173ec.md)
- [mm.h](kernel_2internal_2mm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
