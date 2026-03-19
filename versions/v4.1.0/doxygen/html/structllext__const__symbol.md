---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structllext__const__symbol.html
original_path: doxygen/html/structllext__const__symbol.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

llext\_const\_symbol Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext__apis.md) » [Exported symbol definitions](group__llext__symbols.md)

Constant symbols are unchangeable named memory addresses.
[More...](#details)

`#include <[symbol.h](symbol_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| const char \*const   [name](#a8e18aab091d8aa99b94eed2e215400f9) |  |
|  | Name of symbol. [More...](#a8e18aab091d8aa99b94eed2e215400f9) |
| const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)   [slid](#afe01c08dff4f9334a95a9be23aede72b) |  |
|  | Symbol Link Identifier. [More...](#afe01c08dff4f9334a95a9be23aede72b) |
| }; |  |
|  | At build time, we always write to 'name'. |
| const void \*const | [addr](#ac0bb3e3c67e91f790a1284f3ebc260b2) |
|  | Address of symbol. |

## Detailed Description

Constant symbols are unchangeable named memory addresses.

Symbols may be named function or global objects that have been exported for linking. These constant symbols are useful in the base image as they may be placed in ROM.

Note
:   When updating this structure, make sure to also update the 'scripts/build/llext\_prepare\_exptab.py' build script.

## Field Documentation

## [◆ ](#a1ffacf8c4906e0d64a0f292405e16a15)[union]

| union { ... } [llext\_const\_symbol](structllext__const__symbol.md) |
| --- |

At build time, we always write to 'name'.

At runtime, which field is used depends on CONFIG\_LLEXT\_EXPORT\_BUILTINS\_BY\_SLID.

## [◆ ](#ac0bb3e3c67e91f790a1284f3ebc260b2)addr

| const void\* const llext\_const\_symbol::addr |
| --- |

Address of symbol.

## [◆ ](#a8e18aab091d8aa99b94eed2e215400f9)name

| const char\* const llext\_const\_symbol::name |
| --- |

Name of symbol.

## [◆ ](#afe01c08dff4f9334a95a9be23aede72b)slid

| const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) llext\_const\_symbol::slid |
| --- |

Symbol Link Identifier.

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[symbol.h](symbol_8h_source.md)

- [llext\_const\_symbol](structllext__const__symbol.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
