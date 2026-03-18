---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/common_8h.html
original_path: doxygen/html/common_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

common.h File Reference

Common toolchain abstraction.
[More...](#details)

[Go to the source code of this file.](common_8h_source.md)

| Macros | |
| --- | --- |
| #define | [EXTERN\_C](#abbaccfbed35b945162c27ef6d3748e77)   extern |
| #define | [ZRESTRICT](#a39314fd705c5a9ed45b671ca36f883fd)   restrict |
| #define | [REQUIRES](#ab9df20a7e00611b6bdfb246b35a761fc)(sym) |
| #define | [ALWAYS\_INLINE](#aa1dec568e79152c892dcf63f445cbd7a)   inline \_\_attribute\_\_((always\_inline)) |
| #define | [STRINGIFY](#a4689212d5a549893cabb9d7782eecfb6)([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
| #define | [IS\_PTR\_ALIGNED\_BYTES](#accd51a2e6e0aacde1d3c7ad7497e40ec)(ptr, bytes) |
| #define | [IS\_PTR\_ALIGNED](#ab13eb1fd10a663089d43679e8c172f71)(ptr, type) |
| #define | [LINKER\_KEEP](#ad9b02fb67670e2aed5766db629cd4bfa)(symbol) |
|  | Tag a symbol (e.g. |

## Detailed Description

Common toolchain abstraction.

Macros to abstract compiler capabilities (common to all toolchains).

## Macro Definition Documentation

## [◆ ](#aa1dec568e79152c892dcf63f445cbd7a)ALWAYS\_INLINE

| #define ALWAYS\_INLINE   inline \_\_attribute\_\_((always\_inline)) |
| --- |

## [◆ ](#abbaccfbed35b945162c27ef6d3748e77)EXTERN\_C

| #define EXTERN\_C   extern |
| --- |

## [◆ ](#ab13eb1fd10a663089d43679e8c172f71)IS\_PTR\_ALIGNED

| #define IS\_PTR\_ALIGNED | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | *type* ) |

**Value:**

[IS\_PTR\_ALIGNED\_BYTES](#accd51a2e6e0aacde1d3c7ad7497e40ec)(ptr, \_\_alignof(type))

[IS\_PTR\_ALIGNED\_BYTES](#accd51a2e6e0aacde1d3c7ad7497e40ec)

#define IS\_PTR\_ALIGNED\_BYTES(ptr, bytes)

**Definition** common.h:198

## [◆ ](#accd51a2e6e0aacde1d3c7ad7497e40ec)IS\_PTR\_ALIGNED\_BYTES

| #define IS\_PTR\_ALIGNED\_BYTES | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | *bytes* ) |

**Value:**

(((([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))ptr) % bytes) == 0)

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

## [◆ ](#ad9b02fb67670e2aed5766db629cd4bfa)LINKER\_KEEP

| #define LINKER\_KEEP | ( |  | *symbol* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static const void \* const symbol##\_ptr \_\_used \

\_\_attribute\_\_((\_\_section\_\_(".symbol\_to\_keep"))) = (void \*)&symbol

Tag a symbol (e.g.

function) to be kept in the binary even though it is not used.

It prevents symbol from being removed by the linker garbage collector. It is achieved by adding a pointer to that symbol to the kept memory section.

Parameters
:   | symbol | Symbol to keep. |
    | --- | --- |

## [◆ ](#ab9df20a7e00611b6bdfb246b35a761fc)REQUIRES

| #define REQUIRES | ( |  | *sym* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

\_\_asm\_\_ (".set " # sym "\_Requires, " # sym "\n\t");

## [◆ ](#a4689212d5a549893cabb9d7782eecfb6)STRINGIFY

| #define STRINGIFY | ( |  | *[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

Z\_STRINGIFY([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d))

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

## [◆ ](#a39314fd705c5a9ed45b671ca36f883fd)ZRESTRICT

| #define ZRESTRICT   restrict |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [common.h](common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
