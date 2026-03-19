---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/linker-tool-gcc_8h.html
original_path: doxygen/html/linker-tool-gcc_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

linker-tool-gcc.h File Reference

GCC toolchain linker defs.
[More...](#details)

`#include <[zephyr/kernel/mm.h](kernel_2mm_8h_source.md)>`

[Go to the source code of this file.](linker-tool-gcc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [GROUP\_START](#a7461001a81999ec4da41a0f1027c4bbd)(where) |
| #define | [GROUP\_END](#ab29c47f59ee5a5456a5f81a9050b1a47)(where) |
| #define | [GROUP\_LINK\_IN](#a9250789b7dcbb7afd371010fb3a6031d)(where) |
|  | Route memory to a specified memory area. |
| #define | [GROUP\_ROM\_LINK\_IN](#a0cf8819559a7d33944b47130f478e116)(vregion, lregion) |
|  | Route memory for a read-only section. |
| #define | [GROUP\_DATA\_LINK\_IN](#a639d450cbafa51e8937d90df449b797f)(vregion, lregion) |
|  | Route memory for read-write sections that are loaded. |
| #define | [GROUP\_NOLOAD\_LINK\_IN](#a6784ceba92d50f9785cfd130b4341dae)(vregion, lregion) |
|  | Route memory for read-write sections that are NOT loaded; typically this is only used for 'BSS' and 'noinit'. |
| #define | [SECTION\_PROLOGUE](#a784c696b95848c5f070e257a50fbe23a)(name, options, align) |
|  | The [SECTION\_PROLOGUE()](#a784c696b95848c5f070e257a50fbe23a) macro is used to define the beginning of a section. |
| #define | [SECTION\_DATA\_PROLOGUE](#a0d8981d3817b2563846735c90d50240c)(name, options, align) |
|  | Same as for [SECTION\_PROLOGUE()](#a784c696b95848c5f070e257a50fbe23a), except that this one must be used for data sections which on XIP platforms will have differing virtual and load addresses (i.e. |
| #define | [COMMON\_SYMBOLS](#aa5f3d8dcfb378cdbf899467c01494a6f)   \*(COMMON) |

## Detailed Description

GCC toolchain linker defs.

This header file defines the necessary macros used by the linker script for use with the GCC linker.

## Macro Definition Documentation

## [◆ ](#aa5f3d8dcfb378cdbf899467c01494a6f)COMMON\_SYMBOLS

| #define COMMON\_SYMBOLS   \*(COMMON) |
| --- |

## [◆ ](#a639d450cbafa51e8937d90df449b797f)GROUP\_DATA\_LINK\_IN

| #define GROUP\_DATA\_LINK\_IN | ( |  | *vregion*, |
| --- | --- | --- | --- |
|  |  |  | *lregion* ) |

**Value:**

> vregion

Route memory for read-write sections that are loaded.

Used for initialized data sections that on XIP platforms must be copied at startup.

Parameters
:   | vregion | Output VMA |
    | --- | --- |
    | lregion | Output LMA (only used if CONFIG\_MMU if VMA != LMA, or CONFIG\_XIP) |

## [◆ ](#ab29c47f59ee5a5456a5f81a9050b1a47)GROUP\_END

| #define GROUP\_END | ( |  | *where* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a9250789b7dcbb7afd371010fb3a6031d)GROUP\_LINK\_IN

| #define GROUP\_LINK\_IN | ( |  | *where* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

> where

Route memory to a specified memory area.

The [GROUP\_LINK\_IN()](#a9250789b7dcbb7afd371010fb3a6031d) macro is located at the end of the section description and tells the linker that this section is located in the memory area specified by 'where' argument.

This macro is intentionally undefined for CONFIG\_MMU systems when CONFIG\_KERNEL\_VM\_BASE is not the same as CONFIG\_SRAM\_BASE\_ADDRESS, as both the LMA and VMA destinations must be known for all sections as this corresponds to physical vs. virtual location.

Parameters
:   | where | Destination memory area |
    | --- | --- |

## [◆ ](#a6784ceba92d50f9785cfd130b4341dae)GROUP\_NOLOAD\_LINK\_IN

| #define GROUP\_NOLOAD\_LINK\_IN | ( |  | *vregion*, |
| --- | --- | --- | --- |
|  |  |  | *lregion* ) |

**Value:**

> vregion

Route memory for read-write sections that are NOT loaded; typically this is only used for 'BSS' and 'noinit'.

Parameters
:   | vregion | Output VMA |
    | --- | --- |
    | lregion | Output LMA (only used if CONFIG\_MMU if VMA != LMA, corresponds to physical location) |

## [◆ ](#a0cf8819559a7d33944b47130f478e116)GROUP\_ROM\_LINK\_IN

| #define GROUP\_ROM\_LINK\_IN | ( |  | *vregion*, |
| --- | --- | --- | --- |
|  |  |  | *lregion* ) |

**Value:**

> lregion

Route memory for a read-only section.

The [GROUP\_ROM\_LINK\_IN()](#a0cf8819559a7d33944b47130f478e116) macro is located at the end of the section description and tells the linker that this a read-only section that is physically placed at the 'lregion` argument.

If CONFIG\_XIP is active, the 'lregion' area is flash memory.

If CONFIG\_MMU is active, the vregion argument will be used to determine where this is located in the virtual memory map, otherwise it is ignored.

Parameters
:   | vregion | Output VMA (only used if CONFIG\_MMU where LMA != VMA) |
    | --- | --- |
    | lregion | Output LMA \*/ |

#define [GROUP\_ROM\_LINK\_IN(vregion, lregion)](#a0cf8819559a7d33944b47130f478e116)

/\*\*

## [◆ ](#a7461001a81999ec4da41a0f1027c4bbd)GROUP\_START

| #define GROUP\_START | ( |  | *where* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a0d8981d3817b2563846735c90d50240c)SECTION\_DATA\_PROLOGUE

| #define SECTION\_DATA\_PROLOGUE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *options*, |
|  |  |  | *align* ) |

**Value:**

[SECTION\_PROLOGUE](#a784c696b95848c5f070e257a50fbe23a)(name, options, align)

[SECTION\_PROLOGUE](#a784c696b95848c5f070e257a50fbe23a)

#define SECTION\_PROLOGUE(name, options, align)

The SECTION\_PROLOGUE() macro is used to define the beginning of a section.

**Definition** linker-tool-gcc.h:180

Same as for [SECTION\_PROLOGUE()](#a784c696b95848c5f070e257a50fbe23a), except that this one must be used for data sections which on XIP platforms will have differing virtual and load addresses (i.e.

they'll be copied into RAM at program startup). Such a section must also use GROUP\_DATA\_LINK\_IN to specify the correct output load address.

This is equivalent to [SECTION\_PROLOGUE()](#a784c696b95848c5f070e257a50fbe23a) on non-XIP systems. On XIP systems there is an implicit ALIGN\_WITH\_INPUT specified.

Parameters
:   | name | Name of the output section |
    | --- | --- |
    | options | Section options, or left blank |
    | align | Alignment directives, such as [SUBALIGN()](linker-tool-mwdt_8h.md#aeec277ba79a2ce60397be71ac2efbe33). ALIGN() itself is not allowed. May be blank. |

## [◆ ](#a784c696b95848c5f070e257a50fbe23a)SECTION\_PROLOGUE

| #define SECTION\_PROLOGUE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *options*, |
|  |  |  | *align* ) |

**Value:**

name options : align

The [SECTION\_PROLOGUE()](#a784c696b95848c5f070e257a50fbe23a) macro is used to define the beginning of a section.

On MMU systems where VMA != LMA there is an implicit ALIGN\_WITH\_INPUT specified.

Parameters
:   | name | Name of the output section |
    | --- | --- |
    | options | Section options, such as (NOLOAD), or left blank |
    | align | Alignment directives, such as [SUBALIGN()](linker-tool-mwdt_8h.md#aeec277ba79a2ce60397be71ac2efbe33). ALIGN() itself is not allowed. May be blank. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [linker-tool-gcc.h](linker-tool-gcc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
