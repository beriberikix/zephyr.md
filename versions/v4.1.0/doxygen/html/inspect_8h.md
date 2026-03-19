---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/inspect_8h.html
original_path: doxygen/html/inspect_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

inspect.h File Reference

LLEXT ELF inspection routines.
[More...](#details)

`#include <stddef.h>`  
`#include <[zephyr/llext/llext.h](llext_8h_source.md)>`  
`#include <[zephyr/llext/loader.h](loader_8h_source.md)>`  
`#include <[zephyr/llext/llext_internal.h](llext__internal_8h_source.md)>`

[Go to the source code of this file.](inspect_8h_source.md)

| Functions | |
| --- | --- |
| static int | [llext\_get\_region\_info](group__llext__inspect__apis.md#gabef549f07291126f39b5065be3f73599) (const struct [llext\_loader](structllext__loader.md) \*ldr, const struct [llext](structllext.md) \*ext, enum [llext\_mem](group__llext__apis.md#ga9258a6fe4a45aa5dd48c80c7aa07b953) region, const [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) \*\*hdr, const void \*\*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size) |
|  | Get information about a memory region for the specified extension. |
| int | [llext\_section\_shndx](group__llext__inspect__apis.md#ga655023e915eb0ef60e76c0c1625c63c9) (const struct [llext\_loader](structllext__loader.md) \*ldr, const struct [llext](structllext.md) \*ext, const char \*section\_name) |
|  | Get the index of a section with the specified name. |
| static int | [llext\_get\_section\_info](group__llext__inspect__apis.md#ga23121962662f057da004ac1c527716e3) (const struct [llext\_loader](structllext__loader.md) \*ldr, const struct [llext](structllext.md) \*ext, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int shndx, const [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) \*\*hdr, enum [llext\_mem](group__llext__apis.md#ga9258a6fe4a45aa5dd48c80c7aa07b953) \*region, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*offset) |
|  | Get information about a section for the specified extension. |

## Detailed Description

LLEXT ELF inspection routines.

This file contains routines to inspect the contents of an ELF file. It is intended to be used by applications that need advanced access to the ELF file structures of a loaded extension.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [inspect.h](inspect_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
