---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/linker-defs_8h.html
original_path: doxygen/html/linker-defs_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

linker-defs.h File Reference

`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/toolchain/common.h](common_8h_source.md)>`  
`#include <[zephyr/linker/sections.h](sections_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <zephyr/offsets.h>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`

[Go to the source code of this file.](linker-defs_8h_source.md)

| Macros | |
| --- | --- |
| #define | [CREATE\_OBJ\_LEVEL](#a7401dc3cb7ae4d3bb3afcb99c79a50c2)(object, level) |

## Macro Definition Documentation

## [◆ ](#a7401dc3cb7ae4d3bb3afcb99c79a50c2)CREATE\_OBJ\_LEVEL

| #define CREATE\_OBJ\_LEVEL | ( |  | *object*, |
| --- | --- | --- | --- |
|  |  |  | *level* ) |

**Value:**

\_\_##object##\_##level##\_start = .; \

KEEP(\*(SORT(.z\_##object##\_##level?\_\*))); \

KEEP(\*(SORT(.z\_##object##\_##level??\_\*)));

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [linker-defs.h](linker-defs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
