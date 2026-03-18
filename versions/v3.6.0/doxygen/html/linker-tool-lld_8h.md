---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/linker-tool-lld_8h.html
original_path: doxygen/html/linker-tool-lld_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

linker-tool-lld.h File Reference

LLVM LLD linker defs.
[More...](#details)

`#include <[zephyr/linker/linker-tool-gcc.h](linker-tool-gcc_8h_source.md)>`

[Go to the source code of this file.](linker-tool-lld_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SECTION\_PROLOGUE](#a784c696b95848c5f070e257a50fbe23a)(name, options, align) |
|  | The [SECTION\_PROLOGUE()](#a784c696b95848c5f070e257a50fbe23a) macro is used to define the beginning of a section. |
| #define | [SECTION\_DATA\_PROLOGUE](#a0d8981d3817b2563846735c90d50240c)(name, options, align) |
|  | Same as for [SECTION\_PROLOGUE()](#a784c696b95848c5f070e257a50fbe23a), except that this one must be used for data sections which on XIP platforms will have differing virtual and load addresses (i.e. |

## Detailed Description

LLVM LLD linker defs.

This header file defines the necessary macros used by the linker script for use with the LLD linker.

## Macro Definition Documentation

## [◆ ](#a0d8981d3817b2563846735c90d50240c)SECTION\_DATA\_PROLOGUE

| #define SECTION\_DATA\_PROLOGUE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *options*, |
|  |  |  | *align* ) |

**Value:**

[SECTION\_PROLOGUE](linker-tool-gcc_8h.md#a784c696b95848c5f070e257a50fbe23a)(name, options, align)

[SECTION\_PROLOGUE](linker-tool-gcc_8h.md#a784c696b95848c5f070e257a50fbe23a)

#define SECTION\_PROLOGUE(name, options, align)

The SECTION\_PROLOGUE() macro is used to define the beginning of a section.

**Definition** linker-tool-gcc.h:180

Same as for [SECTION\_PROLOGUE()](#a784c696b95848c5f070e257a50fbe23a), except that this one must be used for data sections which on XIP platforms will have differing virtual and load addresses (i.e.

they'll be copied into RAM at program startup). Such a section must also use GROUP\_DATA\_LINK\_IN to specify the correct output load address.

This is equivalent to [SECTION\_PROLOGUE()](#a784c696b95848c5f070e257a50fbe23a) when linking using LLD.

Parameters
:   | name | Name of the output section |
    | --- | --- |
    | options | Section options, or left blank |
    | align | Alignment directives, such as [SUBALIGN()](linker-tool-mwdt_8h.md#aeec277ba79a2ce60397be71ac2efbe33). May be blank. |

## [◆ ](#a784c696b95848c5f070e257a50fbe23a)SECTION\_PROLOGUE

| #define SECTION\_PROLOGUE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *options*, |
|  |  |  | *align* ) |

**Value:**

name options : align

The [SECTION\_PROLOGUE()](#a784c696b95848c5f070e257a50fbe23a) macro is used to define the beginning of a section.

When –omagic (-N) option is provided to LLD then only the first output section of given region has aligned LMA (by default, without –omagic, LLD aligns LMA and VMA of every section to the same value) and the difference between VMA addresses (0 is this is the first section) is added. The difference between LMA and VMA is constant for every section, so this emulates ALIGN\_WITH\_INPUT option present in GNU LD (required by XIP systems).

The –omagic flag is defined in cmake/linker/lld/target\_baremetal.cmake

Parameters
:   | name | Name of the output section |
    | --- | --- |
    | options | Section options, such as (NOLOAD), or left blank |
    | align | Alignment directives, such as [SUBALIGN()](linker-tool-mwdt_8h.md#aeec277ba79a2ce60397be71ac2efbe33). May be blank. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [linker-tool-lld.h](linker-tool-lld_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
