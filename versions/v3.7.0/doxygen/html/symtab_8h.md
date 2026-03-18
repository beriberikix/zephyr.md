---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/symtab_8h.html
original_path: doxygen/html/symtab_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

symtab.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](symtab_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [symtab\_info](structsymtab__info.md) |

| Functions | |
| --- | --- |
| const struct [symtab\_info](structsymtab__info.md) \*const | [symtab\_get](group__symtab__apis.md#gaa6f7ff81f3553e05dd48fae20095e1e6) (void) |
|  | Get the pointer to the symbol table. |
| const char \*const | [symtab\_find\_symbol\_name](group__symtab__apis.md#ga483f5b70c9e28c50c3c29d7e5ad8ebb1) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*offset) |
|  | Find the symbol name with a binary search. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [debug](dir_44aa0acd5660d74ea205f18be43003ca.md)
- [symtab.h](symtab_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
