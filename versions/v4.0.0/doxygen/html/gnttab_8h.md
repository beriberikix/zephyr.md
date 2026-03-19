---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/gnttab_8h.html
original_path: doxygen/html/gnttab_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gnttab.h File Reference

`#include <[zephyr/xen/public/grant_table.h](grant__table_8h_source.md)>`

[Go to the source code of this file.](gnttab_8h_source.md)

| Functions | |
| --- | --- |
| [grant\_ref\_t](grant__table_8h.md#aee25f6c8ecefd1d7c52e49e4886aca3e) | [gnttab\_grant\_access](#aa36d64f2cd70dedabc2c7a67ddb497a9) ([domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) domid, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long gfn, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) readonly) |
| int | [gnttab\_end\_access](#a16013267f3a28da2b672e9d8961b0d9d) ([grant\_ref\_t](grant__table_8h.md#aee25f6c8ecefd1d7c52e49e4886aca3e) gref) |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [gnttab\_alloc\_and\_grant](#afedf9bc092852f2fd9f7461b89482634) (void \*\*map, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) readonly) |
| void \* | [gnttab\_get\_page](#a920eb0f010b62517d0eabd46c0b6becc) (void) |
| void | [gnttab\_put\_page](#a3f354536f151d40ee0732b880f775bb5) (void \*page\_addr) |
| int | [gnttab\_map\_refs](#a64d478848b93048af3e7de5474cc3c0b) (struct [gnttab\_map\_grant\_ref](structgnttab__map__grant__ref.md) \*map\_ops, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int count) |
| int | [gnttab\_unmap\_refs](#a00a2b9fd5f480b3943d9c0ec164c7fed) (struct [gnttab\_map\_grant\_ref](structgnttab__map__grant__ref.md) \*unmap\_ops, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int count) |
| const char \* | [gnttabop\_error](#afe3ff541ac6015e39922f34940154724) ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) status) |

## Function Documentation

## [◆ ](#afedf9bc092852f2fd9f7461b89482634)gnttab\_alloc\_and\_grant()

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) gnttab\_alloc\_and\_grant | ( | void \*\* | *map*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *readonly* ) |

## [◆ ](#a16013267f3a28da2b672e9d8961b0d9d)gnttab\_end\_access()

| int gnttab\_end\_access | ( | [grant\_ref\_t](grant__table_8h.md#aee25f6c8ecefd1d7c52e49e4886aca3e) | *gref* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a920eb0f010b62517d0eabd46c0b6becc)gnttab\_get\_page()

| void \* gnttab\_get\_page | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#aa36d64f2cd70dedabc2c7a67ddb497a9)gnttab\_grant\_access()

| [grant\_ref\_t](grant__table_8h.md#aee25f6c8ecefd1d7c52e49e4886aca3e) gnttab\_grant\_access | ( | [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) | *domid*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *gfn*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *readonly* ) |

## [◆ ](#a64d478848b93048af3e7de5474cc3c0b)gnttab\_map\_refs()

| int gnttab\_map\_refs | ( | struct [gnttab\_map\_grant\_ref](structgnttab__map__grant__ref.md) \* | *map\_ops*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *count* ) |

## [◆ ](#a3f354536f151d40ee0732b880f775bb5)gnttab\_put\_page()

| void gnttab\_put\_page | ( | void \* | *page\_addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a00a2b9fd5f480b3943d9c0ec164c7fed)gnttab\_unmap\_refs()

| int gnttab\_unmap\_refs | ( | struct [gnttab\_map\_grant\_ref](structgnttab__map__grant__ref.md) \* | *unmap\_ops*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *count* ) |

## [◆ ](#afe3ff541ac6015e39922f34940154724)gnttabop\_error()

| const char \* gnttabop\_error | ( | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *status* | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [gnttab.h](gnttab_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
