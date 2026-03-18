---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__llext__apis.html
original_path: doxygen/html/group__llext__apis.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Linkable loadable extensions

[Operating System Services](group__os__services.md)

| Topics | |
| --- | --- |
|  | [ELF constants and data types](group__llext__elf.md) |
|  | [ELF loader context](group__llext__loader__apis.md) |
|  |  |
|  | [Exported symbol definitions](group__llext__symbols.md) |

| Data Structures | |
| --- | --- |
| struct | [llext](structllext.md) |
|  | Structure describing a linkable loadable extension. [More...](structllext.md#details) |
| struct | [llext\_load\_param](structllext__load__param.md) |
|  | Advanced llext\_load parameters. [More...](structllext__load__param.md#details) |

| Macros | |
| --- | --- |
| #define | [LLEXT\_LOAD\_PARAM\_DEFAULT](#ga15f6bd18c1693009be46641ce1b008c6)   { .relocate\_local = [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7), } |
|  | Default initializer for [llext\_load\_param](structllext__load__param.md "llext_load_param"). |

| Enumerations | |
| --- | --- |
| enum | [llext\_mem](#ga9258a6fe4a45aa5dd48c80c7aa07b953) {     [LLEXT\_MEM\_TEXT](#gga9258a6fe4a45aa5dd48c80c7aa07b953a4e7f671abb8e64ad6af7033a9439b7d0) , [LLEXT\_MEM\_DATA](#gga9258a6fe4a45aa5dd48c80c7aa07b953a5e8658f79b74a0916e5d0abe8f852854) , [LLEXT\_MEM\_RODATA](#gga9258a6fe4a45aa5dd48c80c7aa07b953a8ad55e9d9685edd3dfc4ede21854faeb) , [LLEXT\_MEM\_BSS](#gga9258a6fe4a45aa5dd48c80c7aa07b953a84ec2446a021fefa9e6786ad58d6986e) ,     [LLEXT\_MEM\_EXPORT](#gga9258a6fe4a45aa5dd48c80c7aa07b953ae6ed486ed5719bf7058b2f95aa712028) , [LLEXT\_MEM\_SYMTAB](#gga9258a6fe4a45aa5dd48c80c7aa07b953a24549b7a2ee43076f5b8646e7fba5c81) , [LLEXT\_MEM\_STRTAB](#gga9258a6fe4a45aa5dd48c80c7aa07b953ae0ecbbcbe2d8143f5fac4783f7157c17) , [LLEXT\_MEM\_SHSTRTAB](#gga9258a6fe4a45aa5dd48c80c7aa07b953a325e4d3b4ecdbdb2fec8451fef5b582e) ,     [LLEXT\_MEM\_COUNT](#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)   } |
|  | List of memory regions stored or referenced in the LLEXT subsystem. [More...](#ga9258a6fe4a45aa5dd48c80c7aa07b953) |

| Functions | |
| --- | --- |
| struct [llext](structllext.md) \* | [llext\_by\_name](#gaad89b0b44cf5c9528c3f8a0ce37a8fbe) (const char \*name) |
|  | Find an llext by name. |
| int | [llext\_iterate](#ga0faf5a335199e63a424b122b03027c98) (int(\*fn)(struct [llext](structllext.md) \*ext, void \*arg), void \*arg) |
|  | Iterate over all loaded extensions. |
| int | [llext\_load](#ga93c7d7f8987bd25e3dc486943785c8a1) (struct [llext\_loader](structllext__loader.md) \*loader, const char \*name, struct [llext](structllext.md) \*\*ext, struct [llext\_load\_param](structllext__load__param.md) \*ldr\_parm) |
|  | Load and link an extension. |
| int | [llext\_unload](#gad3df7ed4d436846504c0047166eb929e) (struct [llext](structllext.md) \*\*ext) |
|  | Unload an extension. |
| const void \* | [llext\_find\_sym](#gac0982fad15a62723a5cad3f7edd6ba3e) (const struct [llext\_symtable](structllext__symtable.md) \*sym\_table, const char \*sym\_name) |
|  | Find the address for an arbitrary symbol. |
| int | [llext\_call\_fn](#gad50ad281c70093da99851723fc6af470) (struct [llext](structllext.md) \*ext, const char \*sym\_name) |
|  | Call a function by name. |
| int | [llext\_add\_domain](#ga64b13edf15b7c233b49c9c8edff884e6) (struct [llext](structllext.md) \*ext, struct [k\_mem\_domain](structk__mem__domain.md) \*domain) |
|  | Add an extension to a memory domain. |
| int | [arch\_elf\_relocate](#ga1f1a02ac08db72db8cd8a01fa91c95cb) ([elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \*rel, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) loc, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) sym\_base\_addr, const char \*sym\_name, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) load\_bias) |
|  | Architecture specific opcode update function. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [llext\_find\_section](#ga396bddb41c51415faf79e11fad44cb4e) (struct [llext\_loader](structllext__loader.md) \*loader, const char \*search\_name) |
|  | Locates an ELF section in the file. |
| void | [arch\_elf\_relocate\_local](#ga3c36cb7b2337de143e9381b38e70285c) (struct [llext\_loader](structllext__loader.md) \*loader, struct [llext](structllext.md) \*ext, const [elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \*rel, const [elf\_sym\_t](group__llext__elf.md#ga144fdcc270b75a371880da097968555e) \*sym, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) got\_offset) |
|  | Architecture specific function for updating addresses via relocation table. |

## Detailed Description

Since
:   3.5

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga15f6bd18c1693009be46641ce1b008c6)LLEXT\_LOAD\_PARAM\_DEFAULT

| #define LLEXT\_LOAD\_PARAM\_DEFAULT   { .relocate\_local = [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7), } |
| --- |

`#include <[llext.h](llext_8h.md)>`

Default initializer for [llext\_load\_param](structllext__load__param.md "llext_load_param").

## Enumeration Type Documentation

## [◆ ](#ga9258a6fe4a45aa5dd48c80c7aa07b953)llext\_mem

| enum [llext\_mem](#ga9258a6fe4a45aa5dd48c80c7aa07b953) |
| --- |

`#include <[llext.h](llext_8h.md)>`

List of memory regions stored or referenced in the LLEXT subsystem.

This enum lists the different types of memory regions that are used by the LLEXT subsystem. The names match common ELF file section names; but note that at load time multiple ELF sections with similar flags may be merged together into a single memory region.

| Enumerator | |
| --- | --- |
| LLEXT\_MEM\_TEXT | Executable code. |
| LLEXT\_MEM\_DATA | Initialized data. |
| LLEXT\_MEM\_RODATA | Read-only data. |
| LLEXT\_MEM\_BSS | Uninitialized data. |
| LLEXT\_MEM\_EXPORT | Exported symbol table. |
| LLEXT\_MEM\_SYMTAB | Symbol table. |
| LLEXT\_MEM\_STRTAB | Symbol name strings. |
| LLEXT\_MEM\_SHSTRTAB | Section name strings. |
| LLEXT\_MEM\_COUNT | Number of regions managed by LLEXT. |

## Function Documentation

## [◆ ](#ga1f1a02ac08db72db8cd8a01fa91c95cb)arch\_elf\_relocate()

| int arch\_elf\_relocate | ( | [elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \* | *rel*, |
| --- | --- | --- | --- |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *loc*, |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *sym\_base\_addr*, |
|  |  | const char \* | *sym\_name*, |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *load\_bias* ) |

`#include <[llext.h](llext_8h.md)>`

Architecture specific opcode update function.

ELF files include sections describing a series of *relocations*, which are instructions on how to rewrite opcodes given the actual placement of some symbolic data such as a section, function, or object. These relocations are architecture specific and each architecture supporting LLEXT must implement this.

Parameters
:   | [in] | rel | Relocation data provided by ELF |
    | --- | --- | --- |
    | [in] | loc | Address of opcode to rewrite |
    | [in] | sym\_base\_addr | Address of symbol referenced by relocation |
    | [in] | sym\_name | Name of symbol referenced by relocation |
    | [in] | load\_bias | .text load address |

Return values
:   | 0 | Success |
    | --- | --- |
    | -ENOTSUP | Unsupported relocation |
    | -ENOEXEC | Invalid relocation |

## [◆ ](#ga3c36cb7b2337de143e9381b38e70285c)arch\_elf\_relocate\_local()

| void arch\_elf\_relocate\_local | ( | struct [llext\_loader](structllext__loader.md) \* | *loader*, |
| --- | --- | --- | --- |
|  |  | struct [llext](structllext.md) \* | *ext*, |
|  |  | const [elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \* | *rel*, |
|  |  | const [elf\_sym\_t](group__llext__elf.md#ga144fdcc270b75a371880da097968555e) \* | *sym*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *got\_offset* ) |

`#include <[llext.h](llext_8h.md)>`

Architecture specific function for updating addresses via relocation table.

Parameters
:   | [in] | loader | Extension loader data and context |
    | --- | --- | --- |
    | [in] | ext | Extension to call function in |
    | [in] | rel | Relocation data provided by elf |
    | [in] | sym | Corresponding symbol table entry |
    | [in] | got\_offset | Offset within a relocation table |

## [◆ ](#ga64b13edf15b7c233b49c9c8edff884e6)llext\_add\_domain()

| int llext\_add\_domain | ( | struct [llext](structllext.md) \* | *ext*, |
| --- | --- | --- | --- |
|  |  | struct [k\_mem\_domain](structk__mem__domain.md) \* | *domain* ) |

`#include <[llext.h](llext_8h.md)>`

Add an extension to a memory domain.

Allows an extension to be executed in user mode threads when memory protection hardware is enabled by adding memory partitions covering the extension's memory regions to a memory domain.

Parameters
:   | [in] | ext | Extension to add to a domain |
    | --- | --- | --- |
    | [in] | domain | Memory domain to add partitions to |

Returns
:   0 on success, or a negative error code.

Return values
:   | -ENOSYS | `CONFIG_USERSPACE` is not enabled or supported |
    | --- | --- |

## [◆ ](#gaad89b0b44cf5c9528c3f8a0ce37a8fbe)llext\_by\_name()

| struct [llext](structllext.md) \* llext\_by\_name | ( | const char \* | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[llext.h](llext_8h.md)>`

Find an llext by name.

Parameters
:   | [in] | name | String name of the llext |
    | --- | --- | --- |

Returns
:   a pointer to the [llext](structllext.md "llext"), or NULL if not found

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
:   | 0 | Success |
    | --- | --- |
    | -ENOENT | Symbol name not found |

## [◆ ](#ga396bddb41c51415faf79e11fad44cb4e)llext\_find\_section()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) llext\_find\_section | ( | struct [llext\_loader](structllext__loader.md) \* | *loader*, |
| --- | --- | --- | --- |
|  |  | const char \* | *search\_name* ) |

`#include <[llext.h](llext_8h.md)>`

Locates an ELF section in the file.

Searches for a section by name in the ELF file and returns its offset.

Parameters
:   | loader | Extension loader data and context |
    | --- | --- |
    | search\_name | Section name to search for |

Returns
:   the section offset or a negative error code

## [◆ ](#gac0982fad15a62723a5cad3f7edd6ba3e)llext\_find\_sym()

| const void \* llext\_find\_sym | ( | const struct [llext\_symtable](structllext__symtable.md) \* | *sym\_table*, |
| --- | --- | --- | --- |
|  |  | const char \* | *sym\_name* ) |

`#include <[llext.h](llext_8h.md)>`

Find the address for an arbitrary symbol.

Searches for a symbol address, either in the list of symbols exported by the main Zephyr binary or in an extension's symbol table.

Parameters
:   | [in] | sym\_table | Symbol table to lookup symbol in, or NULL to search in the main Zephyr symbol table |
    | --- | --- | --- |
    | [in] | sym\_name | Symbol name to find |

Returns
:   the address of symbol in memory, or NULL if not found

## [◆ ](#ga0faf5a335199e63a424b122b03027c98)llext\_iterate()

| int llext\_iterate | ( | int(\* | *fn*)(struct [llext](structllext.md) \*ext, void \*arg), |
| --- | --- | --- | --- |
|  |  | void \* | *arg* ) |

`#include <[llext.h](llext_8h.md)>`

Iterate over all loaded extensions.

Calls a provided callback function for each registered extension or until the callback function returns a non-0 value.

Parameters
:   | [in] | fn | callback function |
    | --- | --- | --- |
    | [in] | arg | a private argument to be provided to the callback function |

Returns
:   the value returned by the last callback invocation

Return values
:   | 0 | if no extensions are registered |
    | --- | --- |

## [◆ ](#ga93c7d7f8987bd25e3dc486943785c8a1)llext\_load()

| int llext\_load | ( | struct [llext\_loader](structllext__loader.md) \* | *loader*, |
| --- | --- | --- | --- |
|  |  | const char \* | *name*, |
|  |  | struct [llext](structllext.md) \*\* | *ext*, |
|  |  | struct [llext\_load\_param](structllext__load__param.md) \* | *ldr\_parm* ) |

`#include <[llext.h](llext_8h.md)>`

Load and link an extension.

Loads relevant ELF data into memory and provides a structure to work with it.

Parameters
:   | [in] | loader | An extension loader that provides input data and context |
    | --- | --- | --- |
    | [in] | name | A string identifier for the extension |
    | [out] | ext | Pointer to the newly allocated [llext](structllext.md "llext") structure |
    | [in] | ldr\_parm | Optional advanced load parameters (may be NULL) |

Returns
:   the previous extension use count on success, or a negative error code.

Return values
:   | -ENOMEM | Not enough memory |
    | --- | --- |
    | -ENOEXEC | Invalid ELF stream |
    | -ENOTSUP | Unsupported ELF features |

## [◆ ](#gad3df7ed4d436846504c0047166eb929e)llext\_unload()

| int llext\_unload | ( | struct [llext](structllext.md) \*\* | *ext* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[llext.h](llext_8h.md)>`

Unload an extension.

Parameters
:   | [in] | ext | Extension to unload |
    | --- | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
