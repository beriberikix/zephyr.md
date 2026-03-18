---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structllext__const__symbol.html
original_path: doxygen/html/structllext__const__symbol.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

llext\_const\_symbol Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext.md) » [LLEXT symbols](group__llext__symbols.md)

Constant symbols are unchangeable named memory addresses.
[More...](#details)

`#include <[symbol.h](symbol_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \*const | [name](#a8e18aab091d8aa99b94eed2e215400f9) |
|  | Name of symbol. |
| const void \*const | [addr](#ac0bb3e3c67e91f790a1284f3ebc260b2) |
|  | Address of symbol. |

## Detailed Description

Constant symbols are unchangeable named memory addresses.

Symbols may be named function or global objects that have been exported for linking. These constant symbols are useful in the base image as they may be placed in ROM.

## Field Documentation

## [◆ ](#ac0bb3e3c67e91f790a1284f3ebc260b2)addr

| const void\* const llext\_const\_symbol::addr |
| --- |

Address of symbol.

## [◆ ](#a8e18aab091d8aa99b94eed2e215400f9)name

| const char\* const llext\_const\_symbol::name |
| --- |

Name of symbol.

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[symbol.h](symbol_8h_source.md)

- [llext\_const\_symbol](structllext__const__symbol.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
