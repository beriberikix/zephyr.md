---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__llext__symbols.html
original_path: doxygen/html/group__llext__symbols.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

LLEXT symbols

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext.md)

Linkable loadable extension symbol.
[More...](#details)

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
|  | Export a constant symbol to a table of symbols. |
| #define | [LL\_EXTENSION\_SYMBOL](#ga2e05a6082a3ee50fbc74e14a48056626)(x) |
| #define | [EXPORT\_SYSCALL](#ga0cb660137c5768a1335f0970a5efb16b)(x) |
|  | Export a system call to a table of symbols. |

## Detailed Description

Linkable loadable extension symbol.

## Macro Definition Documentation

## [◆ ](#ga0188531646d69e784eccf85bd4fb34aa)EXPORT\_SYMBOL

| #define EXPORT\_SYMBOL | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[symbol.h](symbol_8h.md)>`

**Value:**

static const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([llext\_const\_symbol](structllext__const__symbol.md), x ## \_sym) = { \

.name = [STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(x), .addr = &x, \

}

[STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[llext\_const\_symbol](structllext__const__symbol.md)

Constant symbols are unchangeable named memory addresses.

**Definition** symbol.h:31

Export a constant symbol to a table of symbols.

Takes a symbol (function or object) by symbolic name and adds the name and address of the symbol to a table of symbols that may be used for linking.

Parameters
:   | x | Symbol to export |
    | --- | --- |

## [◆ ](#ga0cb660137c5768a1335f0970a5efb16b)EXPORT\_SYSCALL

| #define EXPORT\_SYSCALL | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[symbol.h](symbol_8h.md)>`

**Value:**

[EXPORT\_SYMBOL](#ga0188531646d69e784eccf85bd4fb34aa)(z\_impl\_ ## x)

[EXPORT\_SYMBOL](#ga0188531646d69e784eccf85bd4fb34aa)

#define EXPORT\_SYMBOL(x)

Export a constant symbol to a table of symbols.

**Definition** symbol.h:77

Export a system call to a table of symbols.

Takes a system call name and uses *[EXPORT\_SYMBOL()](#ga0188531646d69e784eccf85bd4fb34aa)* to export the respective function.

Parameters
:   | x | System call to export |
    | --- | --- |

## [◆ ](#ga2e05a6082a3ee50fbc74e14a48056626)LL\_EXTENSION\_SYMBOL

| #define LL\_EXTENSION\_SYMBOL | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[symbol.h](symbol_8h.md)>`

**Value:**

struct [llext\_symbol](structllext__symbol.md) Z\_GENERIC\_SECTION(".exported\_sym") \_\_used \

symbol\_##x = {[STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(x), &x}

[llext\_symbol](structllext__symbol.md)

Symbols are named memory addresses.

**Definition** symbol.h:46

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
