---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__llext__symbols.html
original_path: doxygen/html/group__llext__symbols.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Exported symbol definitions

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext__apis.md)

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
| #define | [EXPORT\_SYMBOL](#ga0188531646d69e784eccf85bd4fb34aa)(x) |
|  | Export a constant symbol to extensions. |
| #define | [LL\_EXTENSION\_SYMBOL](#ga2e05a6082a3ee50fbc74e14a48056626)(x) |
|  | Exports a symbol from an extension to the base image. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga0188531646d69e784eccf85bd4fb34aa)EXPORT\_SYMBOL

| #define EXPORT\_SYMBOL | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[symbol.h](symbol_8h.md)>`

Export a constant symbol to extensions.

Takes a symbol (function or object) by symbolic name and adds the name and address of the symbol to a table of symbols that may be referenced by extensions.

Parameters
:   | x | Symbol to export to extensions |
    | --- | --- |

## [◆ ](#ga2e05a6082a3ee50fbc74e14a48056626)LL\_EXTENSION\_SYMBOL

| #define LL\_EXTENSION\_SYMBOL | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[symbol.h](symbol_8h.md)>`

Exports a symbol from an extension to the base image.

This macro can be used in extensions to add a symbol (function or object) to the extension's exported symbol table, so that it may be referenced by the base image.

Parameters
:   | x | Extension symbol to export to the base image |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
