---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/loader_8h.html
original_path: doxygen/html/loader_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

loader.h File Reference

LLEXT ELF loader context types.
[More...](#details)

`#include <[zephyr/llext/elf.h](llext_2elf_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/llext/llext.h](llext_8h_source.md)>`

[Go to the source code of this file.](loader_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [llext\_loader](structllext__loader.md) |
|  | Linkable loadable extension loader context. [More...](structllext__loader.md#details) |

| Enumerations | |
| --- | --- |
| enum | [llext\_storage\_type](group__llext__loader__apis.md#ga8e04f364aef19cf45843cc97cc702f24) { [LLEXT\_STORAGE\_TEMPORARY](group__llext__loader__apis.md#gga8e04f364aef19cf45843cc97cc702f24a256d7c93a7232505368ab49713d756e6) , [LLEXT\_STORAGE\_PERSISTENT](group__llext__loader__apis.md#gga8e04f364aef19cf45843cc97cc702f24ade339a696a5d3b0c1b3ff5ad0d73f8a0) , [LLEXT\_STORAGE\_WRITABLE](group__llext__loader__apis.md#gga8e04f364aef19cf45843cc97cc702f24ad588662b67dcd79213b43dc1ed78b52b) } |
|  | Storage type for the ELF data to be loaded. [More...](group__llext__loader__apis.md#ga8e04f364aef19cf45843cc97cc702f24) |

## Detailed Description

LLEXT ELF loader context types.

The following types are used to define the context of the ELF loader used by the [llext](structllext.md "llext") subsystem.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [loader.h](loader_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
