---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/linker-tool-mwdt_8h.html
original_path: doxygen/html/linker-tool-mwdt_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

linker-tool-mwdt.h File Reference

Metware toolchain linker defs.
[More...](#details)

[Go to the source code of this file.](linker-tool-mwdt_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ASSERT](#a0a3e46fec8345ab664843141b78b82a3)(x, y) |
| #define | [SUBALIGN](#aeec277ba79a2ce60397be71ac2efbe33)(x) |
| #define | [GROUP\_START](#a7461001a81999ec4da41a0f1027c4bbd)(where) |
| #define | [GROUP\_END](#ab29c47f59ee5a5456a5f81a9050b1a47)(where) |
| #define | [GROUP\_LINK\_IN](#a9250789b7dcbb7afd371010fb3a6031d)(where) |
| #define | [GROUP\_ROM\_LINK\_IN](#a0cf8819559a7d33944b47130f478e116)(vregion, lregion) |
| #define | [GROUP\_DATA\_LINK\_IN](#a639d450cbafa51e8937d90df449b797f)(vregion, lregion) |
|  | The [GROUP\_ROM\_LINK\_IN()](#a0cf8819559a7d33944b47130f478e116) macro is located at the end of the section description and tells the linker that this a read-only section that is physically placed at the 'lregion` argument. |
| #define | [GROUP\_NOLOAD\_LINK\_IN](#a6784ceba92d50f9785cfd130b4341dae)(vregion, lregion) |
|  | Route memory for read-write sections that are NOT loaded; typically this is only used for 'BSS' and 'noinit'. |
| #define | [SECTION\_PROLOGUE](#a784c696b95848c5f070e257a50fbe23a)(name, options, align) |
| #define | [SECTION\_DATA\_PROLOGUE](#a0d8981d3817b2563846735c90d50240c)(name, options, align) |
| #define | [SORT\_BY\_NAME](#afd4796dcd7496f1463f849165f7e2779)(x) |

## Detailed Description

Metware toolchain linker defs.

This header file defines the necessary macros used by the linker script for use with the metware linker.

## Macro Definition Documentation

## [◆ ](#a0a3e46fec8345ab664843141b78b82a3)ASSERT

| #define ASSERT | ( |  | *x*, |
| --- | --- | --- | --- |
|  |  |  | *y* ) |

## [◆ ](#a639d450cbafa51e8937d90df449b797f)GROUP\_DATA\_LINK\_IN

| #define GROUP\_DATA\_LINK\_IN | ( |  | *vregion*, |
| --- | --- | --- | --- |
|  |  |  | *lregion* ) |

**Value:**

> vregion

The [GROUP\_ROM\_LINK\_IN()](#a0cf8819559a7d33944b47130f478e116) macro is located at the end of the section description and tells the linker that this a read-only section that is physically placed at the 'lregion` argument.

\*/ #define [GROUP\_ROM\_LINK\_IN(vregion, lregion)](#a0cf8819559a7d33944b47130f478e116)

/\* As [GROUP\_LINK\_IN()](#a9250789b7dcbb7afd371010fb3a6031d), but takes a second argument indicating the memory region (e.g. "ROM") for the load address. Used for initialized data sections that on XIP platforms must be copied at startup.

And, because output directives in GNU ld are "sticky", this must also be used on the first section *after* such an initialized data section, specifying the same memory region (e.g. "RAM") for both vregion and lregion.

## [◆ ](#ab29c47f59ee5a5456a5f81a9050b1a47)GROUP\_END

| #define GROUP\_END | ( |  | *where* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a9250789b7dcbb7afd371010fb3a6031d)GROUP\_LINK\_IN

| #define GROUP\_LINK\_IN | ( |  | *where* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

> where

## [◆ ](#a6784ceba92d50f9785cfd130b4341dae)GROUP\_NOLOAD\_LINK\_IN

| #define GROUP\_NOLOAD\_LINK\_IN | ( |  | *vregion*, |
| --- | --- | --- | --- |
|  |  |  | *lregion* ) |

**Value:**

> vregion

Route memory for read-write sections that are NOT loaded; typically this is only used for 'BSS' and 'noinit'.

## [◆ ](#a0cf8819559a7d33944b47130f478e116)GROUP\_ROM\_LINK\_IN

| #define GROUP\_ROM\_LINK\_IN | ( |  | *vregion*, |
| --- | --- | --- | --- |
|  |  |  | *lregion* ) |

**Value:**

> lregion

## [◆ ](#a7461001a81999ec4da41a0f1027c4bbd)GROUP\_START

| #define GROUP\_START | ( |  | *where* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a0d8981d3817b2563846735c90d50240c)SECTION\_DATA\_PROLOGUE

| #define SECTION\_DATA\_PROLOGUE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *options*, |
|  |  |  | *align* ) |

**Value:**

name options : align

## [◆ ](#a784c696b95848c5f070e257a50fbe23a)SECTION\_PROLOGUE

| #define SECTION\_PROLOGUE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *options*, |
|  |  |  | *align* ) |

**Value:**

name options : align

## [◆ ](#afd4796dcd7496f1463f849165f7e2779)SORT\_BY\_NAME

| #define SORT\_BY\_NAME | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

SORT(x)

## [◆ ](#aeec277ba79a2ce60397be71ac2efbe33)SUBALIGN

| #define SUBALIGN | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

ALIGN(x)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [linker-tool-mwdt.h](linker-tool-mwdt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
