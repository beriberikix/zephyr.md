---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/llext__internal_8h.html
original_path: doxygen/html/llext__internal_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

llext\_internal.h File Reference

Private header for linkable loadable extensions.
[More...](#details)

`#include <[zephyr/llext/llext.h](llext_8h_source.md)>`

[Go to the source code of this file.](llext__internal_8h_source.md)

| Functions | |
| --- | --- |
| int | [arch\_elf\_relocate\_local](#ace4d09c365b139a1def5af2f3372067a) (struct [llext\_loader](structllext__loader.md) \*loader, struct [llext](structllext.md) \*ext, const [elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \*rel, const [elf\_sym\_t](group__llext__elf.md#ga144fdcc270b75a371880da097968555e) \*sym, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rel\_addr, const struct [llext\_load\_param](structllext__load__param.md) \*ldr\_parm) |
|  | Architecture specific function for local binding relocations. |
| int | [arch\_elf\_relocate\_global](#acf5a8cd07260bd76f990530ad41453f0) (struct [llext\_loader](structllext__loader.md) \*loader, struct [llext](structllext.md) \*ext, const [elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \*rel, const [elf\_sym\_t](group__llext__elf.md#ga144fdcc270b75a371880da097968555e) \*sym, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rel\_addr, const void \*link\_addr) |
|  | Architecture specific function for global binding relocations. |

## Detailed Description

Private header for linkable loadable extensions.

## Function Documentation

## [◆ ](#acf5a8cd07260bd76f990530ad41453f0)arch\_elf\_relocate\_global()

| int arch\_elf\_relocate\_global | ( | struct [llext\_loader](structllext__loader.md) \* | *loader*, |
| --- | --- | --- | --- |
|  |  | struct [llext](structllext.md) \* | *ext*, |
|  |  | const [elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \* | *rel*, |
|  |  | const [elf\_sym\_t](group__llext__elf.md#ga144fdcc270b75a371880da097968555e) \* | *sym*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *rel\_addr*, |
|  |  | const void \* | *link\_addr* ) |

Architecture specific function for global binding relocations.

Parameters
:   | [in] | loader | Extension loader data and context |
    | --- | --- | --- |
    | [in] | ext | Extension to call function in |
    | [in] | rel | Relocation data provided by elf |
    | [in] | sym | Corresponding symbol table entry |
    | [in] | rel\_addr | Address where relocation should be performed |
    | [in] | link\_addr | target address for table-based relocations |

Returns
:   0 on success or a negative error code

## [◆ ](#ace4d09c365b139a1def5af2f3372067a)arch\_elf\_relocate\_local()

| int arch\_elf\_relocate\_local | ( | struct [llext\_loader](structllext__loader.md) \* | *loader*, |
| --- | --- | --- | --- |
|  |  | struct [llext](structllext.md) \* | *ext*, |
|  |  | const [elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \* | *rel*, |
|  |  | const [elf\_sym\_t](group__llext__elf.md#ga144fdcc270b75a371880da097968555e) \* | *sym*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *rel\_addr*, |
|  |  | const struct [llext\_load\_param](structllext__load__param.md) \* | *ldr\_parm* ) |

Architecture specific function for local binding relocations.

Parameters
:   | [in] | loader | Extension loader data and context |
    | --- | --- | --- |
    | [in] | ext | Extension to call function in |
    | [in] | rel | Relocation data provided by elf |
    | [in] | sym | Corresponding symbol table entry |
    | [in] | rel\_addr | Address where relocation should be performed |
    | [in] | ldr\_parm | Loader parameters |

Returns
:   0 on success or a negative error code

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [llext\_internal.h](llext__internal_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
