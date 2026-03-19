---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__llext__inspect__apis.html
original_path: doxygen/html/group__llext__inspect__apis.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ELF inspection APIs

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext__apis.md)

| Functions | |
| --- | --- |
| static int | [llext\_get\_region\_info](#gabef549f07291126f39b5065be3f73599) (const struct [llext\_loader](structllext__loader.md) \*ldr, const struct [llext](structllext.md) \*ext, enum [llext\_mem](group__llext__apis.md#ga9258a6fe4a45aa5dd48c80c7aa07b953) region, const [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) \*\*hdr, const void \*\*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size) |
|  | Get information about a memory region for the specified extension. |
| int | [llext\_section\_shndx](#ga655023e915eb0ef60e76c0c1625c63c9) (const struct [llext\_loader](structllext__loader.md) \*ldr, const struct [llext](structllext.md) \*ext, const char \*section\_name) |
|  | Get the index of a section with the specified name. |
| static int | [llext\_get\_section\_info](#ga23121962662f057da004ac1c527716e3) (const struct [llext\_loader](structllext__loader.md) \*ldr, const struct [llext](structllext.md) \*ext, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int shndx, const [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) \*\*hdr, enum [llext\_mem](group__llext__apis.md#ga9258a6fe4a45aa5dd48c80c7aa07b953) \*region, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*offset) |
|  | Get information about a section for the specified extension. |

## Detailed Description

## Function Documentation

## [◆ ](#gabef549f07291126f39b5065be3f73599)llext\_get\_region\_info()

| | int llext\_get\_region\_info | ( | const struct [llext\_loader](structllext__loader.md) \* | *ldr*, | | --- | --- | --- | --- | |  |  | const struct [llext](structllext.md) \* | *ext*, | |  |  | enum [llext\_mem](group__llext__apis.md#ga9258a6fe4a45aa5dd48c80c7aa07b953) | *region*, | |  |  | const [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) \*\* | *hdr*, | |  |  | const void \*\* | *addr*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *size* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[inspect.h](inspect_8h.md)>`

Get information about a memory region for the specified extension.

Retrieve information about a region (merged group of similar sections) in the extension. Any output parameter can be NULL if that information is not needed.

Parameters
:   | [in] | ldr | Loader |
    | --- | --- | --- |
    | [in] | ext | Extension |
    | [in] | region | Region to get information about |
    | [out] | hdr | Variable storing the pointer to the region header |
    | [out] | addr | Variable storing the region load address |
    | [out] | size | Variable storing the region size |

Returns
:   0 on success, -EINVAL if the region is invalid

## [◆ ](#ga23121962662f057da004ac1c527716e3)llext\_get\_section\_info()

| | int llext\_get\_section\_info | ( | const struct [llext\_loader](structllext__loader.md) \* | *ldr*, | | --- | --- | --- | --- | |  |  | const struct [llext](structllext.md) \* | *ext*, | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *shndx*, | |  |  | const [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) \*\* | *hdr*, | |  |  | enum [llext\_mem](group__llext__apis.md#ga9258a6fe4a45aa5dd48c80c7aa07b953) \* | *region*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *offset* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[inspect.h](inspect_8h.md)>`

Get information about a section for the specified extension.

Retrieve information about an ELF sections in the extension. Any output parameter can be `NULL` if that information is not needed.

Requires the [llext\_load\_param::keep\_section\_info](structllext__load__param.md#ae8e62920c8f47e7d2bcf7b7309058fb7 "llext_load_param::keep_section_info") flag to be set at extension load time.

Parameters
:   | [in] | ldr | Loader |
    | --- | --- | --- |
    | [in] | ext | Extension |
    | [in] | shndx | Section index |
    | [out] | hdr | Variable storing the pointer to the section header |
    | [out] | region | Variable storing the region the section belongs to |
    | [out] | offset | Variable storing the offset of the section in the region |

Returns
:   0 on success, -EINVAL if the section index is invalid, -ENOTSUP if section data is not available.

## [◆ ](#ga655023e915eb0ef60e76c0c1625c63c9)llext\_section\_shndx()

| int llext\_section\_shndx | ( | const struct [llext\_loader](structllext__loader.md) \* | *ldr*, |
| --- | --- | --- | --- |
|  |  | const struct [llext](structllext.md) \* | *ext*, |
|  |  | const char \* | *section\_name* ) |

`#include <[inspect.h](inspect_8h.md)>`

Get the index of a section with the specified name.

Requires the [llext\_load\_param::keep\_section\_info](structllext__load__param.md#ae8e62920c8f47e7d2bcf7b7309058fb7 "llext_load_param::keep_section_info") flag to be set at extension load time.

Parameters
:   | [in] | ldr | Loader |
    | --- | --- | --- |
    | [in] | ext | Extension |
    | [in] | section\_name | Name of the section to look for |

Returns
:   Section index on success, -ENOENT if the section was not found, -ENOTSUP if section data is not available.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
