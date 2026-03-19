---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__llext__symbols.html
original_path: doxygen/html/group__llext__symbols.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| #define | [LL\_EXTENSION\_SYMBOL\_NAMED](#ga7ee2d88028ae89dee9bf4bf83274807f)(sym\_ident, sym\_name) |
|  | Exports a symbol from an extension to the base image with a custom name. |
| #define | [LL\_EXTENSION\_SYMBOL](#ga2e05a6082a3ee50fbc74e14a48056626)(x) |
|  | Exports a symbol from an extension to the base image. |
| #define | [EXPORT\_SYMBOL\_NAMED](#ga9822b90952597e6acd993999a7228aa1)(sym\_ident, sym\_name) |
|  | Export a constant symbol from the current build with a custom name. |
| #define | [EXPORT\_SYMBOL](#ga0188531646d69e784eccf85bd4fb34aa)(x) |
|  | Export a constant symbol from the current build. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga0188531646d69e784eccf85bd4fb34aa)EXPORT\_SYMBOL

| #define EXPORT\_SYMBOL | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[symbol.h](symbol_8h.md)>`

**Value:**

[EXPORT\_SYMBOL\_NAMED](#ga9822b90952597e6acd993999a7228aa1)(x, x)

[EXPORT\_SYMBOL\_NAMED](#ga9822b90952597e6acd993999a7228aa1)

#define EXPORT\_SYMBOL\_NAMED(sym\_ident, sym\_name)

Export a constant symbol from the current build with a custom name.

**Definition** symbol.h:169

Export a constant symbol from the current build.

Takes a symbol (function or object) by symbolic name and adds the name and address of the symbol to a table of symbols that may be referenced by extensions or by the base image, depending on the current build type.

When `CONFIG_LLEXT` is not enabled, this macro is a no-op.

Parameters
:   | x | Symbol to export |
    | --- | --- |

## [◆ ](#ga9822b90952597e6acd993999a7228aa1)EXPORT\_SYMBOL\_NAMED

| #define EXPORT\_SYMBOL\_NAMED | ( |  | *sym\_ident*, |
| --- | --- | --- | --- |
|  |  |  | *sym\_name* ) |

`#include <[symbol.h](symbol_8h.md)>`

**Value:**

Z\_EXPORT\_SYMBOL\_NAMED(sym\_ident, sym\_name)

Export a constant symbol from the current build with a custom name.

Version of [EXPORT\_SYMBOL](#ga0188531646d69e784eccf85bd4fb34aa) that allows the user to specify a custom name for the exported symbol.

When `CONFIG_LLEXT` is not enabled, this macro is a no-op.

Parameters
:   | sym\_ident | Symbol to export |
    | --- | --- |
    | sym\_name | Name associated with the symbol |

## [◆ ](#ga2e05a6082a3ee50fbc74e14a48056626)LL\_EXTENSION\_SYMBOL

| #define LL\_EXTENSION\_SYMBOL | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[symbol.h](symbol_8h.md)>`

**Value:**

Z\_LL\_EXTENSION\_SYMBOL\_NAMED(x, x)

Exports a symbol from an extension to the base image.

This macro can be used in extensions to add a symbol (function or object) to the extension's exported symbol table, so that it may be referenced by the base image.

When not building an extension, this macro is a no-op.

Parameters
:   | x | Extension symbol to export to the base image |
    | --- | --- |

## [◆ ](#ga7ee2d88028ae89dee9bf4bf83274807f)LL\_EXTENSION\_SYMBOL\_NAMED

| #define LL\_EXTENSION\_SYMBOL\_NAMED | ( |  | *sym\_ident*, |
| --- | --- | --- | --- |
|  |  |  | *sym\_name* ) |

`#include <[symbol.h](symbol_8h.md)>`

**Value:**

Z\_LL\_EXTENSION\_SYMBOL\_NAMED(sym\_ident, sym\_name)

Exports a symbol from an extension to the base image with a custom name.

Version of [LL\_EXTENSION\_SYMBOL](#ga2e05a6082a3ee50fbc74e14a48056626) that allows the user to specify a custom name for the exported symbol.

Parameters
:   | sym\_ident | Extension symbol to export to the base image |
    | --- | --- |
    | sym\_name | Name associated with the symbol |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
