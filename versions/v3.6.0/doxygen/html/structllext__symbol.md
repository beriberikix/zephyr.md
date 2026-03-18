---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structllext__symbol.html
original_path: doxygen/html/structllext__symbol.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

llext\_symbol Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext.md) » [LLEXT symbols](group__llext__symbols.md)

Symbols are named memory addresses.
[More...](#details)

`#include <[symbol.h](symbol_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [name](#ae827718e18c718002eeb0cc3a3ae0ab3) |
|  | Name of symbol. |
| void \* | [addr](#ae9d19614618dc3c000f3c4e71dbda5ac) |
|  | Address of symbol. |

## Detailed Description

Symbols are named memory addresses.

Symbols may be named function or global objects that have been exported for linking. These are mutable and should come from extensions where the location may need updating depending on where memory is placed.

## Field Documentation

## [◆ ](#ae9d19614618dc3c000f3c4e71dbda5ac)addr

| void\* llext\_symbol::addr |
| --- |

Address of symbol.

## [◆ ](#ae827718e18c718002eeb0cc3a3ae0ab3)name

| const char\* llext\_symbol::name |
| --- |

Name of symbol.

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[symbol.h](symbol_8h_source.md)

- [llext\_symbol](structllext__symbol.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
