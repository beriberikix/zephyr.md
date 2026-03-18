---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/symbol_8h.html
original_path: doxygen/html/symbol_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

symbol.h File Reference

`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <stddef.h>`

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
| #define | [EXPORT\_SYMBOL](group__llext__symbols.md#ga0188531646d69e784eccf85bd4fb34aa)(x) |
|  | Export a constant symbol to a table of symbols. |
| #define | [LL\_EXTENSION\_SYMBOL](group__llext__symbols.md#ga2e05a6082a3ee50fbc74e14a48056626)(x) |
| #define | [EXPORT\_SYSCALL](group__llext__symbols.md#ga0cb660137c5768a1335f0970a5efb16b)(x) |
|  | Export a system call to a table of symbols. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [symbol.h](symbol_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
