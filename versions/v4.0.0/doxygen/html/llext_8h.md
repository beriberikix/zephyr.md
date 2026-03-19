---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/llext_8h.html
original_path: doxygen/html/llext_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

llext.h File Reference

Support for linkable loadable extensions.
[More...](#details)

`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/llext/elf.h](llext_2elf_8h_source.md)>`  
`#include <[zephyr/llext/symbol.h](symbol_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <zephyr/syscalls/llext.h>`

[Go to the source code of this file.](llext_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [llext](structllext.md) |
|  | Structure describing a linkable loadable extension. [More...](structllext.md#details) |
| struct | [llext\_load\_param](structllext__load__param.md) |
|  | Advanced llext\_load parameters. [More...](structllext__load__param.md#details) |

| Macros | |
| --- | --- |
| #define | [LLEXT\_MAX\_DEPENDENCIES](group__llext__apis.md#ga09b483779bce7612bfaba519e1ecb9e0)   8 |
| #define | [LLEXT\_LOAD\_PARAM\_DEFAULT](group__llext__apis.md#ga15f6bd18c1693009be46641ce1b008c6)   { .relocate\_local = [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7), } |
|  | Default initializer for [llext\_load\_param](structllext__load__param.md "llext_load_param"). |

| Typedefs | |
| --- | --- |
| typedef void(\* | [llext\_entry\_fn\_t](group__llext__apis.md#ga0c27a8648deab424948eeb776a3de5ea)) (void \*user\_data) |
|  | Entry point function signature for an extension. |

| Enumerations | |
| --- | --- |
| enum | [llext\_mem](group__llext__apis.md#ga9258a6fe4a45aa5dd48c80c7aa07b953) {     [LLEXT\_MEM\_TEXT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a4e7f671abb8e64ad6af7033a9439b7d0) , [LLEXT\_MEM\_DATA](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a5e8658f79b74a0916e5d0abe8f852854) , [LLEXT\_MEM\_RODATA](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a8ad55e9d9685edd3dfc4ede21854faeb) , [LLEXT\_MEM\_BSS](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a84ec2446a021fefa9e6786ad58d6986e) ,     [LLEXT\_MEM\_EXPORT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ae6ed486ed5719bf7058b2f95aa712028) , [LLEXT\_MEM\_SYMTAB](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a24549b7a2ee43076f5b8646e7fba5c81) , [LLEXT\_MEM\_STRTAB](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ae0ecbbcbe2d8143f5fac4783f7157c17) , [LLEXT\_MEM\_SHSTRTAB](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a325e4d3b4ecdbdb2fec8451fef5b582e) ,     [LLEXT\_MEM\_PREINIT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a812e884e2c4a3c6430d91998b75d7974) , [LLEXT\_MEM\_INIT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ab119ace11d5d6ca1dca32ef4ce4cef11) , [LLEXT\_MEM\_FINI](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953abfece5d78fbb60c5723eb39eb0df1c9d) , [LLEXT\_MEM\_COUNT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)   } |
|  | List of memory regions stored or referenced in the LLEXT subsystem. [More...](group__llext__apis.md#ga9258a6fe4a45aa5dd48c80c7aa07b953) |

| Functions | |
| --- | --- |
| struct [llext](structllext.md) \* | [llext\_by\_name](group__llext__apis.md#gaad89b0b44cf5c9528c3f8a0ce37a8fbe) (const char \*name) |
|  | Find an llext by name. |
| int | [llext\_iterate](group__llext__apis.md#ga0faf5a335199e63a424b122b03027c98) (int(\*fn)(struct [llext](structllext.md) \*ext, void \*arg), void \*arg) |
|  | Iterate over all loaded extensions. |
| int | [llext\_load](group__llext__apis.md#ga0a4c3db30bc3ec7aa8a9b0e076af7157) (struct [llext\_loader](structllext__loader.md) \*loader, const char \*name, struct [llext](structllext.md) \*\*ext, const struct [llext\_load\_param](structllext__load__param.md) \*ldr\_parm) |
|  | Load and link an extension. |
| int | [llext\_unload](group__llext__apis.md#gad3df7ed4d436846504c0047166eb929e) (struct [llext](structllext.md) \*\*ext) |
|  | Unload an extension. |
| int | [llext\_bringup](group__llext__apis.md#ga01c0c23dba5ff1aa9da42c7895cc7fab) (struct [llext](structllext.md) \*ext) |
|  | Calls bringup functions for an extension. |
| int | [llext\_teardown](group__llext__apis.md#gae061bb6100ad394fcaca7751ff3dadba) (struct [llext](structllext.md) \*ext) |
|  | Calls teardown functions for an extension. |
| void | [llext\_bootstrap](group__llext__apis.md#ga809f7a7976b4436dad31aa03d9ea3729) (struct [llext](structllext.md) \*ext, [llext\_entry\_fn\_t](group__llext__apis.md#ga0c27a8648deab424948eeb776a3de5ea) entry\_fn, void \*user\_data) |
|  | Bring up, execute, and teardown an extension. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [llext\_get\_fn\_table](group__llext__apis.md#ga201b2c853cb3ff35aaa7b891dad5464c) (struct [llext](structllext.md) \*ext, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_init, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Get pointers to setup or cleanup functions for an extension. |
| const void \* | [llext\_find\_sym](group__llext__apis.md#gac0982fad15a62723a5cad3f7edd6ba3e) (const struct [llext\_symtable](structllext__symtable.md) \*sym\_table, const char \*sym\_name) |
|  | Find the address for an arbitrary symbol. |
| int | [llext\_call\_fn](group__llext__apis.md#gad50ad281c70093da99851723fc6af470) (struct [llext](structllext.md) \*ext, const char \*sym\_name) |
|  | Call a function by name. |
| int | [llext\_add\_domain](group__llext__apis.md#ga64b13edf15b7c233b49c9c8edff884e6) (struct [llext](structllext.md) \*ext, struct [k\_mem\_domain](structk__mem__domain.md) \*domain) |
|  | Add an extension to a memory domain. |
| int | [arch\_elf\_relocate](group__llext__apis.md#ga1f1a02ac08db72db8cd8a01fa91c95cb) ([elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \*rel, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) loc, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) sym\_base\_addr, const char \*sym\_name, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) load\_bias) |
|  | Architecture specific opcode update function. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [llext\_find\_section](group__llext__apis.md#ga396bddb41c51415faf79e11fad44cb4e) (struct [llext\_loader](structllext__loader.md) \*loader, const char \*search\_name) |
|  | Locates an ELF section in the file. |
| void | [arch\_elf\_relocate\_local](group__llext__apis.md#ga3c36cb7b2337de143e9381b38e70285c) (struct [llext\_loader](structllext__loader.md) \*loader, struct [llext](structllext.md) \*ext, const [elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \*rel, const [elf\_sym\_t](group__llext__elf.md#ga144fdcc270b75a371880da097968555e) \*sym, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) got\_offset) |
|  | Architecture specific function for updating addresses via relocation table. |

## Detailed Description

Support for linkable loadable extensions.

This file describes the APIs for loading and interacting with Linkable Loadable Extensions (LLEXTs) in Zephyr.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [llext.h](llext_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
