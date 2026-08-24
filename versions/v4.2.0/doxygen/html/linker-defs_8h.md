---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/linker-defs_8h.html
original_path: doxygen/html/linker-defs_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

linker-defs.h File Reference

`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/toolchain/common.h](include_2zephyr_2toolchain_2common_8h_source.md)>`  
`#include <[zephyr/linker/sections.h](sections_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <zephyr/offsets.h>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`

[Go to the source code of this file.](linker-defs_8h_source.md)

| Macros | |
| --- | --- |
| #define | [PLACE\_SYMBOL\_HERE](#a9a8b405bbdbdd1e16d7298b1b0b101fb)(symbol) |
| #define | [CREATE\_OBJ\_LEVEL](#a7401dc3cb7ae4d3bb3afcb99c79a50c2)(object, level) |

## Macro Definition Documentation

## [◆ ](#a7401dc3cb7ae4d3bb3afcb99c79a50c2)CREATE\_OBJ\_LEVEL

| #define CREATE\_OBJ\_LEVEL | ( |  | *object*, |
| --- | --- | --- | --- |
|  |  |  | *level* ) |

**Value:**

[PLACE\_SYMBOL\_HERE](#a9a8b405bbdbdd1e16d7298b1b0b101fb)(\_\_##object##\_##level##\_start);\

KEEP(\*(SORT(.z\_##object##\_##level##\_P\_?\_\*))); \

KEEP(\*(SORT(.z\_##object##\_##level##\_P\_??\_\*))); \

KEEP(\*(SORT(.z\_##object##\_##level##\_P\_???\_\*)));

[PLACE\_SYMBOL\_HERE](#a9a8b405bbdbdd1e16d7298b1b0b101fb)

#define PLACE\_SYMBOL\_HERE(symbol)

**Definition** linker-defs.h:49

## [◆ ](#a9a8b405bbdbdd1e16d7298b1b0b101fb)PLACE\_SYMBOL\_HERE

| #define PLACE\_SYMBOL\_HERE | ( |  | *symbol* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

symbol = .

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [linker-defs.h](linker-defs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
