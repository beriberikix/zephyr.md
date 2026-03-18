---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/utils_8h.html
original_path: doxygen/html/utils_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

utils.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`

[Go to the source code of this file.](utils_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RO\_START](#a5927556a88adec513a5d6265c5aa076b)   0 |
| #define | [RO\_END](#aac88e44c409fe39f224202ef757c7d25)   0 |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [linker\_is\_in\_rodata](#a6a48d32446fade9372ab88092d9b4861) (const void \*addr) |
|  | Check if address is in read only section. |

## Macro Definition Documentation

## [◆ ](#aac88e44c409fe39f224202ef757c7d25)RO\_END

| #define RO\_END   0 |
| --- |

## [◆ ](#a5927556a88adec513a5d6265c5aa076b)RO\_START

| #define RO\_START   0 |
| --- |

## Function Documentation

## [◆ ](#a6a48d32446fade9372ab88092d9b4861)linker\_is\_in\_rodata()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) linker\_is\_in\_rodata | ( | const void \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Check if address is in read only section.

Note that this may return false if the address lies outside the compiler's default read only sections (e.g. .rodata section), depending on the linker script used. This also applies to constants with explicit section attributes.

Parameters
:   | addr | Address. |
    | --- | --- |

Returns
:   True if address identified within read only section.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [utils.h](utils_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
