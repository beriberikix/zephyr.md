---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ext2_8h.html
original_path: doxygen/html/ext2_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ext2.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](ext2_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [ext2\_cfg](structext2__cfg.md) |
|  | Configuration used to format ext2 file system. [More...](structext2__cfg.md#details) |

| Macros | |
| --- | --- |
| #define | [FS\_EXT2\_DECLARE\_DEFAULT\_CONFIG](#a06e57a8a022d06a32a1bda2ae6747c54)(name) |

## Macro Definition Documentation

## [◆ ](#a06e57a8a022d06a32a1bda2ae6747c54)FS\_EXT2\_DECLARE\_DEFAULT\_CONFIG

| #define FS\_EXT2\_DECLARE\_DEFAULT\_CONFIG | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static struct [ext2\_cfg](structext2__cfg.md) name = { \

.block\_size = 1024, \

.fs\_size = 0x800000, \

.bytes\_per\_inode = 4096, \

.volume\_name = {'e', 'x', 't', '2', '\0'}, \

.set\_uuid = false, \

}

[ext2\_cfg](structext2__cfg.md)

Configuration used to format ext2 file system.

**Definition** ext2.h:26

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [fs](dir_b18564c48f4afd8a1a06d777dde5c6ec.md)
- [ext2.h](ext2_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
