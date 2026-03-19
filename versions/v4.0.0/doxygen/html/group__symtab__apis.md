---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__symtab__apis.html
original_path: doxygen/html/group__symtab__apis.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Symbol Table API

[Operating System Services](group__os__services.md)

| Data Structures | |
| --- | --- |
| struct | [symtab\_info](structsymtab__info.md) |

| Functions | |
| --- | --- |
| const struct [symtab\_info](structsymtab__info.md) \* | [symtab\_get](#ga2f1c4fa3cc113c2e5f47c5bbcd337e32) (void) |
|  | Get the pointer to the symbol table. |
| const char \* | [symtab\_find\_symbol\_name](#gac5927cf3f4e0bf3e1b27b397290e44c5) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*offset) |
|  | Find the symbol name with a binary search. |

## Detailed Description

## Function Documentation

## [◆ ](#gac5927cf3f4e0bf3e1b27b397290e44c5)symtab\_find\_symbol\_name()

| const char \* symtab\_find\_symbol\_name | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *addr*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *offset* ) |

`#include <[symtab.h](symtab_8h.md)>`

Find the symbol name with a binary search.

Parameters
:   | [in] | addr | Address of the symbol to find |
    | --- | --- | --- |
    | [out] | offset | Offset of the symbol from the nearest symbol. If the symbol can't be found, this will be 0. |

Returns
:   Name of the nearest symbol if found, otherwise "?" is returned.

## [◆ ](#ga2f1c4fa3cc113c2e5f47c5bbcd337e32)symtab\_get()

| const struct [symtab\_info](structsymtab__info.md) \* symtab\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[symtab.h](symtab_8h.md)>`

Get the pointer to the symbol table.

Returns
:   Pointer to the symbol table.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
