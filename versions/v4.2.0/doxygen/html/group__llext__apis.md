---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__llext__apis.html
original_path: doxygen/html/group__llext__apis.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Linkable loadable extensions

[Operating System Services](group__os__services.md)

| Topics | |
| --- | --- |
|  | [ELF constants and data types](group__llext__elf.md) |
|  | [ELF inspection APIs](group__llext__inspect__apis.md) |
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
| #define | [LLEXT\_MAX\_NAME\_LEN](#ga9b01694abfb050daa3f99e197fecc1a3)   15 |
|  | Maximum length of an extension name. |
| #define | [LLEXT\_MAX\_DEPENDENCIES](#ga09b483779bce7612bfaba519e1ecb9e0)   8 |
|  | Maximum number of dependency LLEXTs. |
| #define | [LLEXT\_LOAD\_PARAM\_DEFAULT](#ga15f6bd18c1693009be46641ce1b008c6)   { .relocate\_local = [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7), } |
|  | Default initializer for [llext\_load\_param](structllext__load__param.md "llext_load_param"). |

| Typedefs | |
| --- | --- |
| typedef void(\* | [llext\_entry\_fn\_t](#ga0c27a8648deab424948eeb776a3de5ea)) (void \*user\_data) |
|  | Entry point function signature for an extension. |

| Enumerations | |
| --- | --- |
| enum | [llext\_mem](#ga9258a6fe4a45aa5dd48c80c7aa07b953) {     [LLEXT\_MEM\_TEXT](#gga9258a6fe4a45aa5dd48c80c7aa07b953a4e7f671abb8e64ad6af7033a9439b7d0) , [LLEXT\_MEM\_DATA](#gga9258a6fe4a45aa5dd48c80c7aa07b953a5e8658f79b74a0916e5d0abe8f852854) , [LLEXT\_MEM\_RODATA](#gga9258a6fe4a45aa5dd48c80c7aa07b953a8ad55e9d9685edd3dfc4ede21854faeb) , [LLEXT\_MEM\_BSS](#gga9258a6fe4a45aa5dd48c80c7aa07b953a84ec2446a021fefa9e6786ad58d6986e) ,     [LLEXT\_MEM\_EXPORT](#gga9258a6fe4a45aa5dd48c80c7aa07b953ae6ed486ed5719bf7058b2f95aa712028) , [LLEXT\_MEM\_SYMTAB](#gga9258a6fe4a45aa5dd48c80c7aa07b953a24549b7a2ee43076f5b8646e7fba5c81) , [LLEXT\_MEM\_STRTAB](#gga9258a6fe4a45aa5dd48c80c7aa07b953ae0ecbbcbe2d8143f5fac4783f7157c17) , [LLEXT\_MEM\_SHSTRTAB](#gga9258a6fe4a45aa5dd48c80c7aa07b953a325e4d3b4ecdbdb2fec8451fef5b582e) ,     [LLEXT\_MEM\_PREINIT](#gga9258a6fe4a45aa5dd48c80c7aa07b953a812e884e2c4a3c6430d91998b75d7974) , [LLEXT\_MEM\_INIT](#gga9258a6fe4a45aa5dd48c80c7aa07b953ab119ace11d5d6ca1dca32ef4ce4cef11) , [LLEXT\_MEM\_FINI](#gga9258a6fe4a45aa5dd48c80c7aa07b953abfece5d78fbb60c5723eb39eb0df1c9d) , [LLEXT\_MEM\_COUNT](#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)   } |
|  | List of memory regions stored or referenced in the LLEXT subsystem. [More...](#ga9258a6fe4a45aa5dd48c80c7aa07b953) |

| Functions | |
| --- | --- |
| static const [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) \* | [llext\_section\_headers](#ga2432e14161e327d2b1adb5bde5ce6a86) (const struct [llext](structllext.md) \*ext) |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [llext\_section\_count](#ga0b4a3969f1322bf77aaaa614be789bd9) (const struct [llext](structllext.md) \*ext) |
| struct [llext](structllext.md) \* | [llext\_by\_name](#gaad89b0b44cf5c9528c3f8a0ce37a8fbe) (const char \*name) |
|  | Find an llext by name. |
| int | [llext\_iterate](#ga0faf5a335199e63a424b122b03027c98) (int(\*fn)(struct [llext](structllext.md) \*ext, void \*arg), void \*arg) |
|  | Iterate over all loaded extensions. |
| int | [llext\_load](#ga0a4c3db30bc3ec7aa8a9b0e076af7157) (struct [llext\_loader](structllext__loader.md) \*loader, const char \*name, struct [llext](structllext.md) \*\*ext, const struct [llext\_load\_param](structllext__load__param.md) \*ldr\_parm) |
|  | Load and link an extension. |
| int | [llext\_unload](#gad3df7ed4d436846504c0047166eb929e) (struct [llext](structllext.md) \*\*ext) |
|  | Unload an extension. |
| int | [llext\_free\_inspection\_data](#ga54f3aaed749e8c6bad6fbecb1622ab06) (struct [llext\_loader](structllext__loader.md) \*ldr, struct [llext](structllext.md) \*ext) |
|  | Free any inspection-related memory for the specified loader and extension. |
| int | [llext\_bringup](#ga01c0c23dba5ff1aa9da42c7895cc7fab) (struct [llext](structllext.md) \*ext) |
|  | Calls bringup functions for an extension. |
| int | [llext\_teardown](#gae061bb6100ad394fcaca7751ff3dadba) (struct [llext](structllext.md) \*ext) |
|  | Calls teardown functions for an extension. |
| void | [llext\_bootstrap](#ga809f7a7976b4436dad31aa03d9ea3729) (struct [llext](structllext.md) \*ext, [llext\_entry\_fn\_t](#ga0c27a8648deab424948eeb776a3de5ea) entry\_fn, void \*user\_data) |
|  | Bring up, execute, and teardown an extension. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [llext\_get\_fn\_table](#ga201b2c853cb3ff35aaa7b891dad5464c) (struct [llext](structllext.md) \*ext, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_init, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Get pointers to setup or cleanup functions for an extension. |
| const void \* | [llext\_find\_sym](#gac0982fad15a62723a5cad3f7edd6ba3e) (const struct [llext\_symtable](structllext__symtable.md) \*sym\_table, const char \*sym\_name) |
|  | Find the address for an arbitrary symbol. |
| int | [llext\_call\_fn](#gad50ad281c70093da99851723fc6af470) (struct [llext](structllext.md) \*ext, const char \*sym\_name) |
|  | Call a function by name. |
| int | [llext\_add\_domain](#ga64b13edf15b7c233b49c9c8edff884e6) (struct [llext](structllext.md) \*ext, struct [k\_mem\_domain](structk__mem__domain.md) \*domain) |
|  | Add an extension to a memory domain. |
| int | [arch\_elf\_relocate](#gaeaf6817a9f9c7ae66000cc960e8edf31) (struct [llext\_loader](structllext__loader.md) \*ldr, struct [llext](structllext.md) \*ext, [elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \*rel, const [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) \*shdr) |
|  | Architecture specific opcode update function. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [llext\_find\_section](#ga396bddb41c51415faf79e11fad44cb4e) (struct [llext\_loader](structllext__loader.md) \*loader, const char \*search\_name) |
|  | Locates an ELF section in the file. |
| int | [llext\_get\_section\_header](#ga308d3c0b60358dcfbd8d7481fa68ff90) (struct [llext\_loader](structllext__loader.md) \*loader, struct [llext](structllext.md) \*ext, const char \*search\_name, [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) \*shdr) |
|  | Extract ELF section header by name. |
| int | [llext\_heap\_init](#ga1fa344ade4911a259e7b8ded51241d13) (void \*mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Initialize LLEXT heap dynamically. |
| int | [llext\_heap\_uninit](#gab20e01c13bdb344978a0fb9b5bd8531d) (void) |
|  | Mark LLEXT heap as uninitialized. |
| int | [llext\_relink\_dependency](#gab7c9e78852207c064b52b19bb924ccda) (struct [llext](structllext.md) \*ext, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int n\_ext) |
|  | Relink dependencies to prepare for suspend. |
| int | [llext\_restore](#gad3c4daf1bf7f7e9f04451bcafc94173d) (struct [llext](structllext.md) \*\*ext, struct [llext\_loader](structllext__loader.md) \*\*ldr, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int n\_ext) |
|  | Restore LLEXT context from saved data. |

## Detailed Description

Since
:   3.5

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga15f6bd18c1693009be46641ce1b008c6)LLEXT\_LOAD\_PARAM\_DEFAULT

| #define LLEXT\_LOAD\_PARAM\_DEFAULT   { .relocate\_local = [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7), } |
| --- |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

Default initializer for [llext\_load\_param](structllext__load__param.md "llext_load_param").

## [◆ ](#ga09b483779bce7612bfaba519e1ecb9e0)LLEXT\_MAX\_DEPENDENCIES

| #define LLEXT\_MAX\_DEPENDENCIES   8 |
| --- |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

Maximum number of dependency LLEXTs.

## [◆ ](#ga9b01694abfb050daa3f99e197fecc1a3)LLEXT\_MAX\_NAME\_LEN

| #define LLEXT\_MAX\_NAME\_LEN   15 |
| --- |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

Maximum length of an extension name.

## Typedef Documentation

## [◆ ](#ga0c27a8648deab424948eeb776a3de5ea)llext\_entry\_fn\_t

| typedef void(\* llext\_entry\_fn\_t) (void \*user\_data) |
| --- |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

Entry point function signature for an extension.

## Enumeration Type Documentation

## [◆ ](#ga9258a6fe4a45aa5dd48c80c7aa07b953)llext\_mem

| enum [llext\_mem](#ga9258a6fe4a45aa5dd48c80c7aa07b953) |
| --- |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

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
| LLEXT\_MEM\_PREINIT | Array of early setup functions. |
| LLEXT\_MEM\_INIT | Array of setup functions. |
| LLEXT\_MEM\_FINI | Array of cleanup functions. |
| LLEXT\_MEM\_COUNT | Number of regions managed by LLEXT. |

## Function Documentation

## [◆ ](#gaeaf6817a9f9c7ae66000cc960e8edf31)arch\_elf\_relocate()

| int arch\_elf\_relocate | ( | struct [llext\_loader](structllext__loader.md) \* | *ldr*, |
| --- | --- | --- | --- |
|  |  | struct [llext](structllext.md) \* | *ext*, |
|  |  | [elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \* | *rel*, |
|  |  | const [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) \* | *shdr* ) |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

Architecture specific opcode update function.

ELF files include sections describing a series of *relocations*, which are instructions on how to rewrite opcodes given the actual placement of some symbolic data such as a section, function, or object. These relocations are architecture specific and each architecture supporting LLEXT must implement this. Arguments sym\_base\_addr, sym\_name can be computed from the sym parameter, but these parameters are provided redundantly to increase efficiency.

Parameters
:   | [in] | ldr | Extension loader |
    | --- | --- | --- |
    | [in] | ext | Extension being relocated refers to |
    | [in] | rel | Relocation data provided by ELF |
    | [in] | shdr | Header of the ELF section currently being located |

Return values
:   | 0 | Success |
    | --- | --- |
    | -ENOTSUP | Unsupported relocation |
    | -ENOEXEC | Invalid relocation |

## [◆ ](#ga64b13edf15b7c233b49c9c8edff884e6)llext\_add\_domain()

| int llext\_add\_domain | ( | struct [llext](structllext.md) \* | *ext*, |
| --- | --- | --- | --- |
|  |  | struct [k\_mem\_domain](structk__mem__domain.md) \* | *domain* ) |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

Add an extension to a memory domain.

Allows an extension to be executed in user mode threads when memory protection hardware is enabled by adding memory partitions covering the extension's memory regions to a memory domain.

Parameters
:   | [in] | ext | Extension to add to a domain |
    | --- | --- | --- |
    | [in] | domain | Memory domain to add partitions to |

Returns
:   0 on success, or a negative error code.

Return values
:   | -ENOSYS | Option `CONFIG_USERSPACE` is not enabled or supported |
    | --- | --- |

## [◆ ](#ga809f7a7976b4436dad31aa03d9ea3729)llext\_bootstrap()

| void llext\_bootstrap | ( | struct [llext](structllext.md) \* | *ext*, |
| --- | --- | --- | --- |
|  |  | [llext\_entry\_fn\_t](#ga0c27a8648deab424948eeb776a3de5ea) | *entry\_fn*, |
|  |  | void \* | *user\_data* ) |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

Bring up, execute, and teardown an extension.

Calls the extension's own setup functions, an additional entry point and the extension's cleanup functions in the current thread context.

This is a convenient wrapper around [llext\_bringup](#ga01c0c23dba5ff1aa9da42c7895cc7fab) and [llext\_teardown](#gae061bb6100ad394fcaca7751ff3dadba) that matches the [k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717 "k_thread_entry_t") signature, so it can be directly started as a new user or kernel thread via [k\_thread\_create](group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367 "k_thread_create").

Parameters
:   | [in] | ext | Extension to execute. Passed as p1 in [k\_thread\_create](group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367 "k_thread_create"). |
    | --- | --- | --- |
    | [in] | entry\_fn | Main entry point of the thread after performing extension setup. Passed as p2 in [k\_thread\_create](group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367 "k_thread_create"). |
    | [in] | user\_data | Argument passed to *entry\_fn*. Passed as p3 in [k\_thread\_create](group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367 "k_thread_create"). |

## [◆ ](#ga01c0c23dba5ff1aa9da42c7895cc7fab)llext\_bringup()

| int llext\_bringup | ( | struct [llext](structllext.md) \* | *ext* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

Calls bringup functions for an extension.

Must be called before accessing any symbol in the extension. Will execute the extension's own setup functions in the caller context.

See also
:   [llext\_bootstrap](#ga809f7a7976b4436dad31aa03d9ea3729)

Parameters
:   | [in] | ext | Extension to initialize. |
    | --- | --- | --- |

Returns
:   0 on success, or a negative error code.

Return values
:   | -EFAULT | A relocation issue was detected |
    | --- | --- |

## [◆ ](#gaad89b0b44cf5c9528c3f8a0ce37a8fbe)llext\_by\_name()

| struct [llext](structllext.md) \* llext\_by\_name | ( | const char \* | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

Find an llext by name.

Parameters
:   | [in] | name | String name of the llext |
    | --- | --- | --- |

Returns
:   a pointer to the [llext](structllext.md "llext"), or [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) if not found

## [◆ ](#gad50ad281c70093da99851723fc6af470)llext\_call\_fn()

| int llext\_call\_fn | ( | struct [llext](structllext.md) \* | *ext*, |
| --- | --- | --- | --- |
|  |  | const char \* | *sym\_name* ) |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

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

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

Locates an ELF section in the file.

Searches for a section by name in the ELF file and returns its offset.

Parameters
:   | [in] | loader | Extension loader data and context |
    | --- | --- | --- |
    | [in] | search\_name | Section name to search for |

Returns
:   the section offset or a negative error code

## [◆ ](#gac0982fad15a62723a5cad3f7edd6ba3e)llext\_find\_sym()

| const void \* llext\_find\_sym | ( | const struct [llext\_symtable](structllext__symtable.md) \* | *sym\_table*, |
| --- | --- | --- | --- |
|  |  | const char \* | *sym\_name* ) |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

Find the address for an arbitrary symbol.

Searches for a symbol address, either in the list of symbols exported by the main Zephyr binary or in an extension's symbol table.

Parameters
:   | [in] | sym\_table | Symbol table to lookup symbol in, or [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) to search in the main Zephyr symbol table |
    | --- | --- | --- |
    | [in] | sym\_name | Symbol name to find |

Returns
:   the address of symbol in memory, or [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) if not found

## [◆ ](#ga54f3aaed749e8c6bad6fbecb1622ab06)llext\_free\_inspection\_data()

| int llext\_free\_inspection\_data | ( | struct [llext\_loader](structllext__loader.md) \* | *ldr*, |
| --- | --- | --- | --- |
|  |  | struct [llext](structllext.md) \* | *ext* ) |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

Free any inspection-related memory for the specified loader and extension.

This is only required if inspection data was requested at load time by setting [llext\_load\_param::keep\_section\_info](structllext__load__param.md#ae8e62920c8f47e7d2bcf7b7309058fb7 "llext_load_param::keep_section_info"); otherwise, this call will be a no-op.

Parameters
:   | [in] | ldr | Extension loader |
    | --- | --- | --- |
    | [in] | ext | Extension |

Returns
:   0 on success, or a negative error code.

## [◆ ](#ga201b2c853cb3ff35aaa7b891dad5464c)llext\_get\_fn\_table()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) llext\_get\_fn\_table | ( | struct [llext](structllext.md) \* | *ext*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *is\_init*, |
|  |  | void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

Get pointers to setup or cleanup functions for an extension.

This syscall can be used to get the addresses of all the functions that have to be called for full extension setup or cleanup.

See also
:   [llext\_bootstrap](#ga809f7a7976b4436dad31aa03d9ea3729)

Parameters
:   | [in] | ext | Extension to initialize. |
    | --- | --- | --- |
    | [in] | is\_init | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) to get functions to be called at setup time, [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) to get the cleanup ones. |
    | [in,out] | buf | Buffer to store the function pointers in. Can be [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) to only get the minimum required size. |
    | [in] | size | Allocated size of the buffer in bytes. |

Returns
:   the size used by the array in bytes, or a negative error code.

Return values
:   | -EFAULT | A relocation issue was detected |
    | --- | --- |
    | -ENOMEM | Array does not fit in the allocated buffer |

## [◆ ](#ga308d3c0b60358dcfbd8d7481fa68ff90)llext\_get\_section\_header()

| int llext\_get\_section\_header | ( | struct [llext\_loader](structllext__loader.md) \* | *loader*, |
| --- | --- | --- | --- |
|  |  | struct [llext](structllext.md) \* | *ext*, |
|  |  | const char \* | *search\_name*, |
|  |  | [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) \* | *shdr* ) |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

Extract ELF section header by name.

Searches for a section by name in the ELF file and retrieves its full header.

Parameters
:   | [in] | loader | Extension loader data and context |
    | --- | --- | --- |
    | [in] | ext | Extension to be searched |
    | [in] | search\_name | Section name to search for |
    | [out] | shdr | Buffer for the section header |

Return values
:   | 0 | Success |
    | --- | --- |
    | -ENOTSUP | "peek" method not supported |
    | -ENOENT | section not found |

## [◆ ](#ga1fa344ade4911a259e7b8ded51241d13)llext\_heap\_init()

| int llext\_heap\_init | ( | void \* | *mem*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bytes* ) |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

Initialize LLEXT heap dynamically.

Use the provided memory block as the LLEXT heap at runtime.

Parameters
:   | mem | Pointer to memory. |
    | --- | --- |
    | bytes | Size of memory region, in bytes |

Returns
:   0 on success, or a negative error code.

Return values
:   | -ENOSYS | Option `CONFIG_LLEXT_HEAP_DYNAMIC` is not enabled or supported |
    | --- | --- |

## [◆ ](#gab20e01c13bdb344978a0fb9b5bd8531d)llext\_heap\_uninit()

| int llext\_heap\_uninit | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

Mark LLEXT heap as uninitialized.

Returns
:   0 on success, or a negative error code.

Return values
:   | -ENOSYS | Option `CONFIG_LLEXT_HEAP_DYNAMIC` is not enabled or supported |
    | --- | --- |
    | -EBUSY | On heap not empty |

## [◆ ](#ga0faf5a335199e63a424b122b03027c98)llext\_iterate()

| int llext\_iterate | ( | int(\* | *fn*)(struct [llext](structllext.md) \*ext, void \*arg), |
| --- | --- | --- | --- |
|  |  | void \* | *arg* ) |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

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

## [◆ ](#ga0a4c3db30bc3ec7aa8a9b0e076af7157)llext\_load()

| int llext\_load | ( | struct [llext\_loader](structllext__loader.md) \* | *loader*, |
| --- | --- | --- | --- |
|  |  | const char \* | *name*, |
|  |  | struct [llext](structllext.md) \*\* | *ext*, |
|  |  | const struct [llext\_load\_param](structllext__load__param.md) \* | *ldr\_parm* ) |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

Load and link an extension.

Loads relevant ELF data into memory and provides a structure to work with it.

Parameters
:   | [in] | loader | An extension loader that provides input data and context |
    | --- | --- | --- |
    | [in] | name | A string identifier for the extension |
    | [out] | ext | Pointer to the newly allocated [llext](structllext.md "llext") structure |
    | [in] | ldr\_parm | Optional advanced load parameters (may be [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) |

Returns
:   the previous extension use count on success, or a negative error code.

Return values
:   | -ENOMEM | Not enough memory |
    | --- | --- |
    | -ENOEXEC | Invalid ELF stream |
    | -ENOTSUP | Unsupported ELF features |

## [◆ ](#gab7c9e78852207c064b52b19bb924ccda)llext\_relink\_dependency()

| int llext\_relink\_dependency | ( | struct [llext](structllext.md) \* | *ext*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *n\_ext* ) |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

Relink dependencies to prepare for suspend.

For suspend-resume use-cases, when LLEXT context should be saved in a non-volatile buffer, the user can save most LLEXT support data, but they have to use [llext\_restore()](#gad3c4daf1bf7f7e9f04451bcafc94173d) to re-allocate objects, which will also have to restore dependency pointers. To make sure dependency saving and restoring is done consistently, we provide a helper function for the former too.

Warning
:   this is a part of an experimental API, it WILL change in the future! Its availability depends on CONFIG\_LLEXT\_EXPERIMENTAL, which is disabled by default.

Parameters
:   | [in] | ext | Extension array |
    | --- | --- | --- |
    | [in] | n\_ext | Number of extensions |

Return values
:   | 0 | Success |
    | --- | --- |
    | -ENOENT | Some dependencies not found |

## [◆ ](#gad3c4daf1bf7f7e9f04451bcafc94173d)llext\_restore()

| int llext\_restore | ( | struct [llext](structllext.md) \*\* | *ext*, |
| --- | --- | --- | --- |
|  |  | struct [llext\_loader](structllext__loader.md) \*\* | *ldr*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *n\_ext* ) |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

Restore LLEXT context from saved data.

During suspend the user has saved all the extension and loader descriptors and related objects and called [llext\_relink\_dependency()](#gab7c9e78852207c064b52b19bb924ccda) to prepare dependency pointers. When resuming llext\_alloc() has to be used to re-allocate all the objects, therefore the user needs support from LLEXT core to accomplish that. This function takes arrays of pointers to saved copies of extensions and loaders as arguments and re-allocates all the objects, while also adding them to the global extension list. At the same time it relinks dependency pointers to newly allocated extensions.

Warning
:   this is a part of an experimental API, it WILL change in the future! Its availability depends on CONFIG\_LLEXT\_EXPERIMENTAL, which is disabled by default.

Parameters
:   | [in,out] | ext | Extension pointer array - replaced with re-allocated copies |
    | --- | --- | --- |
    | [in,out] | ldr | Array of loader pointers to restore section maps |
    | [in] | n\_ext | Number of extensions |

Return values
:   | 0 | Success |
    | --- | --- |
    | -ENOMEM | No memory |
    | -EINVAL | Stored dependency out of range |
    | -EFAULT | Internal algorithmic error |

## [◆ ](#ga0b4a3969f1322bf77aaaa614be789bd9)llext\_section\_count()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int llext\_section\_count | ( | const struct [llext](structllext.md) \* | *ext* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

## [◆ ](#ga2432e14161e327d2b1adb5bde5ce6a86)llext\_section\_headers()

| | const [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) \* llext\_section\_headers | ( | const struct [llext](structllext.md) \* | *ext* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

## [◆ ](#gae061bb6100ad394fcaca7751ff3dadba)llext\_teardown()

| int llext\_teardown | ( | struct [llext](structllext.md) \* | *ext* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

Calls teardown functions for an extension.

Will execute the extension's own cleanup functions in the caller context. After this function completes, the extension is no longer usable and must be fully unloaded with [llext\_unload](#gad3df7ed4d436846504c0047166eb929e).

See also
:   [llext\_bootstrap](#ga809f7a7976b4436dad31aa03d9ea3729)

Parameters
:   | [in] | ext | Extension to de-initialize. |
    | --- | --- | --- |

Returns
:   0 on success, or a negative error code.

Return values
:   | -EFAULT | A relocation issue was detected |
    | --- | --- |

## [◆ ](#gad3df7ed4d436846504c0047166eb929e)llext\_unload()

| int llext\_unload | ( | struct [llext](structllext.md) \*\* | *ext* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/llext/llext.h](llext_8h.md)>`

Unload an extension.

Parameters
:   | [in] | ext | Extension to unload |
    | --- | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
