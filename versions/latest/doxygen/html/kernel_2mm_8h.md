---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/kernel_2mm_8h.html
original_path: doxygen/html/kernel_2mm_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mm.h File Reference

`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/kernel/internal/mm.h](kernel_2internal_2mm_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[inttypes.h](inttypes_8h_source.md)>`

[Go to the source code of this file.](kernel_2mm_8h_source.md)

| Macros | |
| --- | --- |
| Caching mode definitions. | |
| These are mutually exclusive. | |
| #define | [K\_MEM\_CACHE\_NONE](group__kernel__memory__management.md#gaae7605452be94d1bd6e0364e9db113c6)   2 |
|  | No caching. |
| #define | [K\_MEM\_CACHE\_WT](group__kernel__memory__management.md#ga1c8d5fee98c68b08cc6acf781eb35320)   1 |
|  | Write-through caching. |
| #define | [K\_MEM\_CACHE\_WB](group__kernel__memory__management.md#ga802a69d7a53cafcf357861ab50258c99)   0 |
|  | Full write-back caching. |
| #define | [K\_MEM\_CACHE\_MASK](group__kernel__memory__management.md#gaae828c97c7bae5d235b863ff3b6b913e)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) - 1) |
|  | Reserved bits for cache modes in k\_map() flags argument. |
| Region permission attributes. | |
| Default is read-only, no user, no exec | |
| #define | [K\_MEM\_PERM\_RW](group__kernel__memory__management.md#gab9ea94b7155e276f0b653bc1a081866e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Region will have read/write access (and not read-only). |
| #define | [K\_MEM\_PERM\_EXEC](group__kernel__memory__management.md#gaf1b0db3c1c5b28b1810f39cdac03f9de)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Region will be executable (normally forbidden). |
| #define | [K\_MEM\_PERM\_USER](group__kernel__memory__management.md#gaa96222e46728d507ca229796a5724425)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Region will be accessible to user mode (normally supervisor-only). |
| Region mapping behaviour attributes | |
| #define | [K\_MEM\_DIRECT\_MAP](group__kernel__memory__management.md#ga36c4d2ede2f91490bc20ec399df663be)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Region will be mapped to 1:1 virtual and physical address. |
| k\_mem\_map() control flags | |
| #define | [K\_MEM\_MAP\_UNINIT](group__kernel__memory__management.md#ga0a3569731c9a9f8e94e913f840b4be61)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16) |
|  | The mapped region is not guaranteed to be zeroed. |
| #define | [K\_MEM\_MAP\_LOCK](group__kernel__memory__management.md#ga7bed120eac76f03a55b1ab8a1f61ce8b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17) |
|  | Region will be pinned in memory and never paged. |

| Functions | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [k\_mem\_free\_get](group__kernel__memory__management.md#gabb315b4994193147e9f51b0c3268bfcd) (void) |
|  | Return the amount of free memory available. |
| void \* | [k\_mem\_map](group__kernel__memory__management.md#gae9831427d79d64acfc9ad9c699d619d1) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Map anonymous memory into Zephyr's address space. |
| void | [k\_mem\_unmap](group__kernel__memory__management.md#gadc321dd750d9bdf36dec2f77d21a7207) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Un-map mapped memory. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [k\_mem\_region\_align](group__kernel__memory__management.md#gad9a0110394e8026e27deb15687321ee9) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*aligned\_addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*aligned\_size, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align) |
|  | Given an arbitrary region, provide a aligned region that covers it. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel](dir_87084789f4f879979d9b1b0acd11eedc.md)
- [mm.h](kernel_2mm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
