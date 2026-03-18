---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structllext.html
original_path: doxygen/html/structllext.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

llext Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext.md)

Linkable loadable extension.
[More...](#details)

`#include <[llext.h](llext_8h_source.md)>`

| Data Fields | |
| --- | --- |
| char | [name](#a505e052f55e25cf10ac0431defb774ea) [16] |
|  | Name of the llext. |
| void \* | [mem](#ae9d529433f30ed659758c9b29c9b96bd) [[LLEXT\_MEM\_COUNT](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)] |
|  | Lookup table of llext memory regions. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [mem\_on\_heap](#a7556c195516041439547d891897f4a44) [[LLEXT\_MEM\_COUNT](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)] |
|  | Is the memory for this section allocated on heap? |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [mem\_size](#a47cfcb60d773a6c16d2fda8cc5011a16) [[LLEXT\_MEM\_COUNT](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)] |
|  | Size of each stored section. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [alloc\_size](#a566e46e600e9b90f9d4b570ef007e6a6) |
|  | Total llext allocation size. |
| struct [llext\_symtable](structllext__symtable.md) | [sym\_tab](#a4f67c792a963ac124f32b2d7880f9cdf) |
| struct [llext\_symtable](structllext__symtable.md) | [exp\_tab](#a76cc3ef7989f2d4bfaeedadd05738de2) |
|  | Exported symbols from the llext, may be linked against by other llext. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [use\_count](#a61c5ca5c740f5bb14791f11354b68101) |
|  | Extension use counter, prevents unloading while in use. |

## Detailed Description

Linkable loadable extension.

## Field Documentation

## [◆ ](#a566e46e600e9b90f9d4b570ef007e6a6)alloc\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) llext::alloc\_size |
| --- |

Total llext allocation size.

## [◆ ](#a76cc3ef7989f2d4bfaeedadd05738de2)exp\_tab

| struct [llext\_symtable](structllext__symtable.md) llext::exp\_tab |
| --- |

Exported symbols from the llext, may be linked against by other llext.

## [◆ ](#ae9d529433f30ed659758c9b29c9b96bd)mem

| void\* llext::mem[[LLEXT\_MEM\_COUNT](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)] |
| --- |

Lookup table of llext memory regions.

## [◆ ](#a7556c195516041439547d891897f4a44)mem\_on\_heap

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) llext::mem\_on\_heap[[LLEXT\_MEM\_COUNT](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)] |
| --- |

Is the memory for this section allocated on heap?

## [◆ ](#a47cfcb60d773a6c16d2fda8cc5011a16)mem\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) llext::mem\_size[[LLEXT\_MEM\_COUNT](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)] |
| --- |

Size of each stored section.

## [◆ ](#a505e052f55e25cf10ac0431defb774ea)name

| char llext::name[16] |
| --- |

Name of the llext.

## [◆ ](#a4f67c792a963ac124f32b2d7880f9cdf)sym\_tab

| struct [llext\_symtable](structllext__symtable.md) llext::sym\_tab |
| --- |

## [◆ ](#a61c5ca5c740f5bb14791f11354b68101)use\_count

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int llext::use\_count |
| --- |

Extension use counter, prevents unloading while in use.

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[llext.h](llext_8h_source.md)

- [llext](structllext.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
