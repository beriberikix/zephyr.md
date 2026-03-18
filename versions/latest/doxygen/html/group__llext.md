---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__llext.html
original_path: doxygen/html/group__llext.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Linkable loadable extensions

[Operating System Services](group__os__services.md)

Linkable loadable extensions.
[More...](#details)

| Topics | |
| --- | --- |
|  | [ELF data types and defines](group__elf.md) |
|  | ELF types and parsing. |
|  | [LLEXT symbols](group__llext__symbols.md) |
|  | Linkable loadable extension symbol. |
|  | [Linkable loadable extensions buffer loader](group__llext__buf__loader.md) |
|  | LLEXT buffer loader. |
|  | [Loader context for llext](group__llext__loader.md) |
|  | Loader context for llext. |

| Data Structures | |
| --- | --- |
| struct | [llext](structllext.md) |
|  | Linkable loadable extension. [More...](structllext.md#details) |
| struct | [llext\_load\_param](structllext__load__param.md) |
|  | llext loader parameters [More...](structllext__load__param.md#details) |

| Macros | |
| --- | --- |
| #define | [LLEXT\_MEM\_PARTITIONS](#ga8740e267a2d59772fde6cda3df1711f2)   ([LLEXT\_MEM\_BSS](#gga9258a6fe4a45aa5dd48c80c7aa07b953a84ec2446a021fefa9e6786ad58d6986e)+1) |
| #define | [LLEXT\_LOAD\_PARAM\_DEFAULT](#ga15f6bd18c1693009be46641ce1b008c6)   {.relocate\_local = [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7),} |

| Enumerations | |
| --- | --- |
| enum | [llext\_mem](#ga9258a6fe4a45aa5dd48c80c7aa07b953) {     [LLEXT\_MEM\_TEXT](#gga9258a6fe4a45aa5dd48c80c7aa07b953a4e7f671abb8e64ad6af7033a9439b7d0) , [LLEXT\_MEM\_DATA](#gga9258a6fe4a45aa5dd48c80c7aa07b953a5e8658f79b74a0916e5d0abe8f852854) , [LLEXT\_MEM\_RODATA](#gga9258a6fe4a45aa5dd48c80c7aa07b953a8ad55e9d9685edd3dfc4ede21854faeb) , [LLEXT\_MEM\_BSS](#gga9258a6fe4a45aa5dd48c80c7aa07b953a84ec2446a021fefa9e6786ad58d6986e) ,     [LLEXT\_MEM\_EXPORT](#gga9258a6fe4a45aa5dd48c80c7aa07b953ae6ed486ed5719bf7058b2f95aa712028) , [LLEXT\_MEM\_SYMTAB](#gga9258a6fe4a45aa5dd48c80c7aa07b953a24549b7a2ee43076f5b8646e7fba5c81) , [LLEXT\_MEM\_STRTAB](#gga9258a6fe4a45aa5dd48c80c7aa07b953ae0ecbbcbe2d8143f5fac4783f7157c17) , [LLEXT\_MEM\_SHSTRTAB](#gga9258a6fe4a45aa5dd48c80c7aa07b953a325e4d3b4ecdbdb2fec8451fef5b582e) ,     [LLEXT\_MEM\_COUNT](#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)   } |
|  | List of ELF regions that are stored or referenced in the llext. [More...](#ga9258a6fe4a45aa5dd48c80c7aa07b953) |

| Functions | |
| --- | --- |
| struct [llext](structllext.md) \* | [llext\_by\_name](#gaad89b0b44cf5c9528c3f8a0ce37a8fbe) (const char \*name) |
|  | Find an llext by name. |
| int | [llext\_iterate](#ga0faf5a335199e63a424b122b03027c98) (int(\*fn)(struct [llext](structllext.md) \*ext, void \*arg), void \*arg) |
|  | Iterate overall registered llext instances. |
| int | [llext\_load](#ga93c7d7f8987bd25e3dc486943785c8a1) (struct [llext\_loader](structllext__loader.md) \*loader, const char \*name, struct [llext](structllext.md) \*\*ext, struct [llext\_load\_param](structllext__load__param.md) \*ldr\_parm) |
|  | Load and link an extension. |
| int | [llext\_unload](#gad3df7ed4d436846504c0047166eb929e) (struct [llext](structllext.md) \*\*ext) |
|  | Unload an extension. |
| const void \*const | [llext\_find\_sym](#ga2554c14853cc809d63deb52096423838) (const struct [llext\_symtable](structllext__symtable.md) \*sym\_table, const char \*sym\_name) |
|  | Find the address for an arbitrary symbol name. |
| int | [llext\_call\_fn](#gad50ad281c70093da99851723fc6af470) (struct [llext](structllext.md) \*ext, const char \*sym\_name) |
|  | Call a function by name. |
| int | [llext\_add\_domain](#ga64b13edf15b7c233b49c9c8edff884e6) (struct [llext](structllext.md) \*ext, struct [k\_mem\_domain](structk__mem__domain.md) \*domain) |
|  | Add the known memory partitions of the extension to a memory domain. |
| void | [arch\_elf\_relocate](#gad3ced43229d6f68622d71e5bc7234ca2) ([elf\_rela\_t](group__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \*rel, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) opaddr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) opval) |
|  | Architecture specific function for updating op codes given a relocation. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [llext\_find\_section](#ga396bddb41c51415faf79e11fad44cb4e) (struct [llext\_loader](structllext__loader.md) \*loader, const char \*search\_name) |
|  | Find an ELF section. |
| void | [arch\_elf\_relocate\_local](#ga437e19a2132007a3f9636e349a233d36) (struct [llext\_loader](structllext__loader.md) \*loader, struct [llext](structllext.md) \*ext, [elf\_rela\_t](group__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \*rel, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) got\_offset) |
|  | Architecture specific function for updating addresses via relocation table. |

## Detailed Description

Linkable loadable extensions.

## Macro Definition Documentation

## [◆ ](#ga15f6bd18c1693009be46641ce1b008c6)LLEXT\_LOAD\_PARAM\_DEFAULT

| #define LLEXT\_LOAD\_PARAM\_DEFAULT   {.relocate\_local = [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7),} |
| --- |

`#include <[llext.h](llext_8h.md)>`

## [◆ ](#ga8740e267a2d59772fde6cda3df1711f2)LLEXT\_MEM\_PARTITIONS

| #define LLEXT\_MEM\_PARTITIONS   ([LLEXT\_MEM\_BSS](#gga9258a6fe4a45aa5dd48c80c7aa07b953a84ec2446a021fefa9e6786ad58d6986e)+1) |
| --- |

`#include <[llext.h](llext_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#ga9258a6fe4a45aa5dd48c80c7aa07b953)llext\_mem

| enum [llext\_mem](#ga9258a6fe4a45aa5dd48c80c7aa07b953) |
| --- |

`#include <[llext.h](llext_8h.md)>`

List of ELF regions that are stored or referenced in the llext.

| Enumerator | |
| --- | --- |
| LLEXT\_MEM\_TEXT |  |
| LLEXT\_MEM\_DATA |  |
| LLEXT\_MEM\_RODATA |  |
| LLEXT\_MEM\_BSS |  |
| LLEXT\_MEM\_EXPORT |  |
| LLEXT\_MEM\_SYMTAB |  |
| LLEXT\_MEM\_STRTAB |  |
| LLEXT\_MEM\_SHSTRTAB |  |
| LLEXT\_MEM\_COUNT |  |

## Function Documentation

## [◆ ](#gad3ced43229d6f68622d71e5bc7234ca2)arch\_elf\_relocate()

| void arch\_elf\_relocate | ( | [elf\_rela\_t](group__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \* | *rel*, |
| --- | --- | --- | --- |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *opaddr*, |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *opval* ) |

`#include <[llext.h](llext_8h.md)>`

Architecture specific function for updating op codes given a relocation.

Elf files contain a series of relocations described in a section. These relocation instructions are architecture specific and each architecture supporting extensions must implement this. They are instructions on how to rewrite opcodes given the actual placement of some symbolic data such as a section, function, or object.

Parameters
:   | [in] | rel | Relocation data provided by elf |
    | --- | --- | --- |
    | [in] | opaddr | Address of operation to rewrite with relocation |
    | [in] | opval | Value of looked up symbol to relocate |

## [◆ ](#ga437e19a2132007a3f9636e349a233d36)arch\_elf\_relocate\_local()

| void arch\_elf\_relocate\_local | ( | struct [llext\_loader](structllext__loader.md) \* | *loader*, |
| --- | --- | --- | --- |
|  |  | struct [llext](structllext.md) \* | *ext*, |
|  |  | [elf\_rela\_t](group__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \* | *rel*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *got\_offset* ) |

`#include <[llext.h](llext_8h.md)>`

Architecture specific function for updating addresses via relocation table.

Parameters
:   | [in] | loader | Extension loader data and context |
    | --- | --- | --- |
    | [in] | ext | Extension to call function in |
    | [in] | rel | Relocation data provided by elf |
    | [in] | got\_offset | Offset within a relocation table |

## [◆ ](#ga64b13edf15b7c233b49c9c8edff884e6)llext\_add\_domain()

| int llext\_add\_domain | ( | struct [llext](structllext.md) \* | *ext*, |
| --- | --- | --- | --- |
|  |  | struct [k\_mem\_domain](structk__mem__domain.md) \* | *domain* ) |

`#include <[llext.h](llext_8h.md)>`

Add the known memory partitions of the extension to a memory domain.

Allows an extension to be executed in supervisor or user mode threads when memory protection hardware is enabled.

Parameters
:   | [in] | ext | Extension to add to a domain |
    | --- | --- | --- |
    | [in] | domain | Memory domain to add partitions to |

Return values
:   | 0 | success |
    | --- | --- |
    | -errno | error |

## [◆ ](#gaad89b0b44cf5c9528c3f8a0ce37a8fbe)llext\_by\_name()

| struct [llext](structllext.md) \* llext\_by\_name | ( | const char \* | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[llext.h](llext_8h.md)>`

Find an llext by name.

Parameters
:   | [in] | name | String name of the llext |
    | --- | --- | --- |

Return values
:   | NULL | if no llext not found |
    | --- | --- |
    | [llext](structllext.md "Linkable loadable extension.") | if llext found |

## [◆ ](#gad50ad281c70093da99851723fc6af470)llext\_call\_fn()

| int llext\_call\_fn | ( | struct [llext](structllext.md) \* | *ext*, |
| --- | --- | --- | --- |
|  |  | const char \* | *sym\_name* ) |

`#include <[llext.h](llext_8h.md)>`

Call a function by name.

Expects a symbol representing a void fn(void) style function exists and may be called.

Parameters
:   | [in] | ext | Extension to call function in |
    | --- | --- | --- |
    | [in] | sym\_name | Function name (exported symbol) in the extension |

Return values
:   | 0 | success |
    | --- | --- |
    | -EINVAL | invalid symbol name |

## [◆ ](#ga396bddb41c51415faf79e11fad44cb4e)llext\_find\_section()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) llext\_find\_section | ( | struct [llext\_loader](structllext__loader.md) \* | *loader*, |
| --- | --- | --- | --- |
|  |  | const char \* | *search\_name* ) |

`#include <[llext.h](llext_8h.md)>`

Find an ELF section.

Parameters
:   | loader | Extension loader data and context |
    | --- | --- |
    | search\_name | Section name to search for |

Return values
:   | Section | offset or a negative error code |
    | --- | --- |

## [◆ ](#ga2554c14853cc809d63deb52096423838)llext\_find\_sym()

| const void \*const llext\_find\_sym | ( | const struct [llext\_symtable](structllext__symtable.md) \* | *sym\_table*, |
| --- | --- | --- | --- |
|  |  | const char \* | *sym\_name* ) |

`#include <[llext.h](llext_8h.md)>`

Find the address for an arbitrary symbol name.

Parameters
:   | [in] | sym\_table | Symbol table to lookup symbol in, if NULL uses base table |
    | --- | --- | --- |
    | [in] | sym\_name | Symbol name to find |

Return values
:   | NULL | if no symbol found |
    | --- | --- |
    | addr | Address of symbol in memory if found |

## [◆ ](#ga0faf5a335199e63a424b122b03027c98)llext\_iterate()

| int llext\_iterate | ( | int(\* | *fn*)(struct [llext](structllext.md) \*ext, void \*arg), |
| --- | --- | --- | --- |
|  |  | void \* | *arg* ) |

`#include <[llext.h](llext_8h.md)>`

Iterate overall registered llext instances.

Calls a provided callback function for each registered extension or until the callback function returns a non-0 value.

Parameters
:   | [in] | fn | callback function |
    | --- | --- | --- |
    | [in] | arg | a private argument to be provided to the callback function |

Return values
:   | 0 | if no extensions are registered |
    | --- | --- |
    | value | returned by the most recent callback invocation |

## [◆ ](#ga93c7d7f8987bd25e3dc486943785c8a1)llext\_load()

| int llext\_load | ( | struct [llext\_loader](structllext__loader.md) \* | *loader*, |
| --- | --- | --- | --- |
|  |  | const char \* | *name*, |
|  |  | struct [llext](structllext.md) \*\* | *ext*, |
|  |  | struct [llext\_load\_param](structllext__load__param.md) \* | *ldr\_parm* ) |

`#include <[llext.h](llext_8h.md)>`

Load and link an extension.

Loads relevant ELF data into memory and provides a structure to work with it.

Only relocatable ELF files are currently supported (partially linked).

Parameters
:   | [in] | loader | An extension loader that provides input data and context |
    | --- | --- | --- |
    | [in] | name | A string identifier for the extension |
    | [out] | ext | This will hold the pointer to the llext struct |
    | [in] | ldr\_parm | Loader parameters |

Return values
:   | 0 | Success |
    | --- | --- |
    | -ENOMEM | Not enough memory |
    | -EINVAL | Invalid ELF stream |

## [◆ ](#gad3df7ed4d436846504c0047166eb929e)llext\_unload()

| int llext\_unload | ( | struct [llext](structllext.md) \*\* | *ext* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[llext.h](llext_8h.md)>`

Unload an extension.

Parameters
:   | [in] | ext | Extension to unload |
    | --- | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
