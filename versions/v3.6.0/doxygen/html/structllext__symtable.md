---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structllext__symtable.html
original_path: doxygen/html/structllext__symtable.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

llext\_symtable Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext.md) » [LLEXT symbols](group__llext__symbols.md)

A symbol table.
[More...](#details)

`#include <[symbol.h](symbol_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [sym\_cnt](#a1e65bbdadb52a27b60e835994357cca1) |
|  | Number of symbols in the table. |
| struct [llext\_symbol](structllext__symbol.md) \* | [syms](#ac03152f3cb9d1881feed1d840dd024d9) |
|  | Array of symbols. |

## Detailed Description

A symbol table.

An array of symbols

## Field Documentation

## [◆ ](#a1e65bbdadb52a27b60e835994357cca1)sym\_cnt

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) llext\_symtable::sym\_cnt |
| --- |

Number of symbols in the table.

## [◆ ](#ac03152f3cb9d1881feed1d840dd024d9)syms

| struct [llext\_symbol](structllext__symbol.md)\* llext\_symtable::syms |
| --- |

Array of symbols.

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[symbol.h](symbol_8h_source.md)

- [llext\_symtable](structllext__symtable.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
