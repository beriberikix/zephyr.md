---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arch_2arm64_2cache_8h.html
original_path: doxygen/html/arch_2arm64_2cache_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cache.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <[zephyr/sys/barrier.h](sys_2barrier_8h_source.md)>`  
`#include <zephyr/arch/cpu.h>`  
`#include <[errno.h](errno_8h_source.md)>`

[Go to the source code of this file.](arch_2arm64_2cache_8h_source.md)

| Macros | |
| --- | --- |
| #define | [K\_CACHE\_WB](#a67c04995b5bfa5270cc9aa15f927cdad)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [K\_CACHE\_INVD](#a58178f26d7c006f3219cb63d175c0480)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [K\_CACHE\_WB\_INVD](#ad6ef90303e280c90786c684c839ec1e7)   ([K\_CACHE\_WB](#a67c04995b5bfa5270cc9aa15f927cdad) | [K\_CACHE\_INVD](#a58178f26d7c006f3219cb63d175c0480)) |

## Macro Definition Documentation

## [◆ ](#a58178f26d7c006f3219cb63d175c0480)K\_CACHE\_INVD

| #define K\_CACHE\_INVD   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a67c04995b5bfa5270cc9aa15f927cdad)K\_CACHE\_WB

| #define K\_CACHE\_WB   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#ad6ef90303e280c90786c684c839ec1e7)K\_CACHE\_WB\_INVD

| #define K\_CACHE\_WB\_INVD   ([K\_CACHE\_WB](#a67c04995b5bfa5270cc9aa15f927cdad) | [K\_CACHE\_INVD](#a58178f26d7c006f3219cb63d175c0480)) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [cache.h](arch_2arm64_2cache_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
