---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/littlefs_8h.html
original_path: doxygen/html/littlefs_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

littlefs.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/storage/flash_map.h](flash__map_8h_source.md)>`  
`#include <lfs.h>`

[Go to the source code of this file.](littlefs_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [fs\_littlefs](structfs__littlefs.md) |
|  | Filesystem info structure for LittleFS mount. [More...](structfs__littlefs.md#details) |

| Macros | |
| --- | --- |
| #define | [FS\_LITTLEFS\_DECLARE\_CUSTOM\_CONFIG](#a1560f156ad9d0f9aed149b1ed5cb537b)(name, alignment, read\_sz, prog\_sz, cache\_sz, lookahead\_sz) |
|  | Define a littlefs configuration with customized size characteristics. |
| #define | [FS\_LITTLEFS\_DECLARE\_DEFAULT\_CONFIG](#a9f584969a034fb4058c28fed33164d7a)(name) |
|  | Define a littlefs configuration with default characteristics. |

## Macro Definition Documentation

## [◆ ](#a1560f156ad9d0f9aed149b1ed5cb537b)FS\_LITTLEFS\_DECLARE\_CUSTOM\_CONFIG

| #define FS\_LITTLEFS\_DECLARE\_CUSTOM\_CONFIG | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *alignment*, |
|  |  |  | *read\_sz*, |
|  |  |  | *prog\_sz*, |
|  |  |  | *cache\_sz*, |
|  |  |  | *lookahead\_sz* ) |

**Value:**

static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_\_aligned(alignment) name ## \_read\_buffer[cache\_sz]; \

static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_\_aligned(alignment) name ## \_prog\_buffer[cache\_sz]; \

static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) name ## \_lookahead\_buffer[(lookahead\_sz) / sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))]; \

static struct [fs\_littlefs](structfs__littlefs.md) name = { \

.cfg = { \

.read\_size = (read\_sz), \

.prog\_size = (prog\_sz), \

.cache\_size = (cache\_sz), \

.lookahead\_size = (lookahead\_sz), \

.read\_buffer = name ## \_read\_buffer, \

.[prog\_buffer](structfs__littlefs.md#a239d1ac90cc0de3a9cca766d41180def) = name ## \_prog\_buffer, \

.[lookahead\_buffer](structfs__littlefs.md#a7cd0dcd14e83138ba2ed698f55377e49) = name ## \_lookahead\_buffer, \

}, \

}

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[fs\_littlefs](structfs__littlefs.md)

Filesystem info structure for LittleFS mount.

**Definition** littlefs.h:21

[fs\_littlefs::prog\_buffer](structfs__littlefs.md#a239d1ac90cc0de3a9cca766d41180def)

uint8\_t \* prog\_buffer

**Definition** littlefs.h:29

[fs\_littlefs::lookahead\_buffer](structfs__littlefs.md#a7cd0dcd14e83138ba2ed698f55377e49)

uint32\_t \* lookahead\_buffer[CONFIG\_FS\_LITTLEFS\_LOOKAHEAD\_SIZE/sizeof(uint32\_t)]

**Definition** littlefs.h:34

Define a littlefs configuration with customized size characteristics.

This defines static arrays required for caches, and initializes the littlefs configuration structure to use the provided values instead of the global Kconfig defaults. A pointer to the named object must be stored in the [fs\_mount\_t::fs\_data](structfs__mount__t.md#a5c2e3e4fa34e5396b6e37fa0b09d5554 "fs_mount_t::fs_data") field of a [fs\_mount\_t](structfs__mount__t.md "fs_mount_t") object.

To define an instance for the Kconfig defaults, use [FS\_LITTLEFS\_DECLARE\_DEFAULT\_CONFIG](#a9f584969a034fb4058c28fed33164d7a).

To completely control file system configuration the application can directly define and initialize a [fs\_littlefs](structfs__littlefs.md "fs_littlefs") object. The application is responsible for ensuring the configured values are consistent with littlefs requirements.

Note
:   If you use a non-default configuration for cache size, you must also select `CONFIG_FS_LITTLEFS_FC_HEAP_SIZE` to relax the size constraints on per-file cache allocations.

Parameters
:   | name | the name for the structure. The defined object has file scope. |
    | --- | --- |
    | alignment | needed alignment for read/prog buffer for specific device |
    | read\_sz | see `CONFIG_FS_LITTLEFS_READ_SIZE` |
    | prog\_sz | see `CONFIG_FS_LITTLEFS_PROG_SIZE` |
    | cache\_sz | see `CONFIG_FS_LITTLEFS_CACHE_SIZE` |
    | lookahead\_sz | see `CONFIG_FS_LITTLEFS_LOOKAHEAD_SIZE` |

## [◆ ](#a9f584969a034fb4058c28fed33164d7a)FS\_LITTLEFS\_DECLARE\_DEFAULT\_CONFIG

| #define FS\_LITTLEFS\_DECLARE\_DEFAULT\_CONFIG | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[FS\_LITTLEFS\_DECLARE\_CUSTOM\_CONFIG](#a1560f156ad9d0f9aed149b1ed5cb537b)(name, \

4, \

CONFIG\_FS\_LITTLEFS\_READ\_SIZE, \

CONFIG\_FS\_LITTLEFS\_PROG\_SIZE, \

CONFIG\_FS\_LITTLEFS\_CACHE\_SIZE, \

CONFIG\_FS\_LITTLEFS\_LOOKAHEAD\_SIZE)

[FS\_LITTLEFS\_DECLARE\_CUSTOM\_CONFIG](#a1560f156ad9d0f9aed149b1ed5cb537b)

#define FS\_LITTLEFS\_DECLARE\_CUSTOM\_CONFIG(name, alignment, read\_sz, prog\_sz, cache\_sz, lookahead\_sz)

Define a littlefs configuration with customized size characteristics.

**Definition** littlefs.h:70

Define a littlefs configuration with default characteristics.

This defines static arrays and initializes the littlefs configuration structure to use the default size configuration provided by Kconfig.

Parameters
:   | name | the name for the structure. The defined object has file scope. |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [fs](dir_b18564c48f4afd8a1a06d777dde5c6ec.md)
- [littlefs.h](littlefs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
