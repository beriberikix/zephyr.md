---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/symbol_8h.html
original_path: doxygen/html/symbol_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

symbol.h File Reference

Linkable loadable extension symbol definitions.
[More...](#details)

`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](symbol_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [llext\_const\_symbol](structllext__const__symbol.md) |
|  | Constant symbols are unchangeable named memory addresses. [More...](structllext__const__symbol.md#details) |
| struct | [llext\_symbol](structllext__symbol.md) |
|  | Symbols are named memory addresses. [More...](structllext__symbol.md#details) |
| struct | [llext\_symtable](structllext__symtable.md) |
|  | A symbol table. [More...](structllext__symtable.md#details) |

| Macros | |
| --- | --- |
| #define | [LL\_EXTENSION\_SYMBOL](group__llext__symbols.md#ga2e05a6082a3ee50fbc74e14a48056626)(x) |
|  | Exports a symbol from an extension to the base image. |
| #define | [EXPORT\_SYMBOL](group__llext__symbols.md#ga0188531646d69e784eccf85bd4fb34aa)(x) |
|  | Export a constant symbol from the current build. |

## Detailed Description

Linkable loadable extension symbol definitions.

This file provides a set of macros and structures for defining and exporting symbols from the base image to extensions and vice versa, so that proper linking can be done between the two entities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [symbol.h](symbol_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
