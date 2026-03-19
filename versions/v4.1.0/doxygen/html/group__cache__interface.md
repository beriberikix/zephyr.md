---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__cache__interface.html
original_path: doxygen/html/group__cache__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Cache Interface

[Operating System Services](group__os__services.md)

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_cache\_data\_enable](#ga8e065404f0d13a33f7b04096165b8776) (void) |
|  | Enable the d-cache. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_cache\_data\_disable](#ga7952019e9231e250a37a3226908102ee) (void) |
|  | Disable the d-cache. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_cache\_instr\_enable](#ga98bd00d87195cbf5f99cea4b68765a7f) (void) |
|  | Enable the i-cache. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_cache\_instr\_disable](#ga502377e711c5399926992e530456af60) (void) |
|  | Disable the i-cache. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_cache\_data\_flush\_all](#ga3992ceae117dbd8bd11a5392e8ab2aa3) (void) |
|  | Flush the d-cache. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_cache\_instr\_flush\_all](#ga6846744d9cdfe5d164679f12abe31e48) (void) |
|  | Flush the i-cache. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_cache\_data\_invd\_all](#ga9c7f8f6783196fc226e58d2da1b7781d) (void) |
|  | Invalidate the d-cache. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_cache\_instr\_invd\_all](#gadc460f782f2642203e1bd4797dd46308) (void) |
|  | Invalidate the i-cache. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_cache\_data\_flush\_and\_invd\_all](#gaa38ce02275c001f4c542c6d967be25ac) (void) |
|  | Flush and Invalidate the d-cache. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_cache\_instr\_flush\_and\_invd\_all](#ga3ac77afb61ae32cc0af7bd61e07cf765) (void) |
|  | Flush and Invalidate the i-cache. |
| int | [sys\_cache\_data\_flush\_range](#ga6b61424f0aa81e2893c915b096de0cdb) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Flush an address range in the d-cache. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_cache\_instr\_flush\_range](#ga628ee038060351a9958067dfc2e3192c) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Flush an address range in the i-cache. |
| int | [sys\_cache\_data\_invd\_range](#ga578f2f926cbf5ad196765881c8c1265e) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Invalidate an address range in the d-cache. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_cache\_instr\_invd\_range](#ga7cc3e53a18492b871b69af8b2d1d0db9) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Invalidate an address range in the i-cache. |
| int | [sys\_cache\_data\_flush\_and\_invd\_range](#ga51d2bfa0ed0d139d1d299d14e8269eac) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Flush and Invalidate an address range in the d-cache. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_cache\_instr\_flush\_and\_invd\_range](#ga768ada6618e2b9ddc5ba3bb54ba48773) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Flush and Invalidate an address range in the i-cache. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [sys\_cache\_data\_line\_size\_get](#ga6b25a6076791c4a559aa20633b49b07e) (void) |
|  | Get the d-cache line size. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [sys\_cache\_instr\_line\_size\_get](#ga4d130b1ef9a3ecfcd08c0eb2f474e5f1) (void) |
|  | Get the i-cache line size. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_cache\_is\_ptr\_cached](#ga0d21da511beb423a64d9bb23e6b5dacf) (void \*ptr) |
|  | Test if a pointer is in cached region. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_cache\_is\_ptr\_uncached](#gaa02f0bac4addff95dda539dca2b1d4d1) (void \*ptr) |
|  | Test if a pointer is in un-cached region. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void \* | [sys\_cache\_cached\_ptr\_get](#ga773d9fef6f1a2d76927957e73e245ef5) (void \*ptr) |
|  | Return cached pointer to a RAM address. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void \* | [sys\_cache\_uncached\_ptr\_get](#ga1410d43a8c6d16e1b54a32868eaecfe3) (void \*ptr) |
|  | Return uncached pointer to a RAM address. |

## Detailed Description

## Function Documentation

## [◆ ](#ga773d9fef6f1a2d76927957e73e245ef5)sys\_cache\_cached\_ptr\_get()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void \* sys\_cache\_cached\_ptr\_get | ( | void \* | *ptr* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cache.h](cache_8h.md)>`

Return cached pointer to a RAM address.

This function takes a pointer to any addressable object (either in cacheable memory or not) and returns a pointer that can be used to refer to the same memory through the L1 data cache. Data read through the resulting pointer will reflect locally cached values on the current CPU if they exist, and writes will go first into the cache and be written back later.

Note
:   This API returns the same pointer if CONFIG\_CACHE\_DOUBLEMAP is not enabled.

See also
:   arch\_uncached\_ptr()

Parameters
:   | ptr | A pointer to a valid C object |
    | --- | --- |

Returns
:   A pointer to the same object via the L1 dcache

## [◆ ](#ga7952019e9231e250a37a3226908102ee)sys\_cache\_data\_disable()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void sys\_cache\_data\_disable | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cache.h](cache_8h.md)>`

Disable the d-cache.

Disable the data cache

## [◆ ](#ga8e065404f0d13a33f7b04096165b8776)sys\_cache\_data\_enable()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void sys\_cache\_data\_enable | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cache.h](cache_8h.md)>`

Enable the d-cache.

Enable the data cache

## [◆ ](#ga3992ceae117dbd8bd11a5392e8ab2aa3)sys\_cache\_data\_flush\_all()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int sys\_cache\_data\_flush\_all | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cache.h](cache_8h.md)>`

Flush the d-cache.

Flush the whole data cache.

Return values
:   | 0 | If succeeded. |
    | --- | --- |
    | -ENOTSUP | If not supported. |
    | -errno | Negative errno for other failures. |

## [◆ ](#gaa38ce02275c001f4c542c6d967be25ac)sys\_cache\_data\_flush\_and\_invd\_all()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int sys\_cache\_data\_flush\_and\_invd\_all | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cache.h](cache_8h.md)>`

Flush and Invalidate the d-cache.

Flush and Invalidate the whole data cache.

Return values
:   | 0 | If succeeded. |
    | --- | --- |
    | -ENOTSUP | If not supported. |
    | -errno | Negative errno for other failures. |

## [◆ ](#ga51d2bfa0ed0d139d1d299d14e8269eac)sys\_cache\_data\_flush\_and\_invd\_range()

| int sys\_cache\_data\_flush\_and\_invd\_range | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[cache.h](cache_8h.md)>`

Flush and Invalidate an address range in the d-cache.

Flush and Invalidate the specified address range of the data cache.

Note
:   the cache operations act on cache line. When multiple data structures share the same cache line being flushed, all the portions of the data structures sharing the same line will be flushed before being invalidated. This is usually not a problem because writing back is a non-destructive process that could be triggered by hardware at any time, so having an aligned `addr` or a padded `size` is not strictly necessary.

Parameters
:   | addr | Starting address to flush and invalidate. |
    | --- | --- |
    | size | Range size. |

Return values
:   | 0 | If succeeded. |
    | --- | --- |
    | -ENOTSUP | If not supported. |
    | -errno | Negative errno for other failures. |

## [◆ ](#ga6b61424f0aa81e2893c915b096de0cdb)sys\_cache\_data\_flush\_range()

| int sys\_cache\_data\_flush\_range | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[cache.h](cache_8h.md)>`

Flush an address range in the d-cache.

Flush the specified address range of the data cache.

Note
:   the cache operations act on cache line. When multiple data structures share the same cache line being flushed, all the portions of the data structures sharing the same line will be flushed. This is usually not a problem because writing back is a non-destructive process that could be triggered by hardware at any time, so having an aligned `addr` or a padded `size` is not strictly necessary.

Parameters
:   | addr | Starting address to flush. |
    | --- | --- |
    | size | Range size. |

Return values
:   | 0 | If succeeded. |
    | --- | --- |
    | -ENOTSUP | If not supported. |
    | -errno | Negative errno for other failures. |

## [◆ ](#ga9c7f8f6783196fc226e58d2da1b7781d)sys\_cache\_data\_invd\_all()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int sys\_cache\_data\_invd\_all | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cache.h](cache_8h.md)>`

Invalidate the d-cache.

Invalidate the whole data cache.

Return values
:   | 0 | If succeeded. |
    | --- | --- |
    | -ENOTSUP | If not supported. |
    | -errno | Negative errno for other failures. |

## [◆ ](#ga578f2f926cbf5ad196765881c8c1265e)sys\_cache\_data\_invd\_range()

| int sys\_cache\_data\_invd\_range | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[cache.h](cache_8h.md)>`

Invalidate an address range in the d-cache.

Invalidate the specified address range of the data cache.

Note
:   the cache operations act on cache line. When multiple data structures share the same cache line being invalidated, all the portions of the non-read-only data structures sharing the same line will be invalidated as well. This is a destructive process that could lead to data loss and/or corruption. When `addr` is not aligned to the cache line and/or `size` is not a multiple of the cache line size the behaviour is undefined.

Parameters
:   | addr | Starting address to invalidate. |
    | --- | --- |
    | size | Range size. |

Return values
:   | 0 | If succeeded. |
    | --- | --- |
    | -ENOTSUP | If not supported. |
    | -errno | Negative errno for other failures. |

## [◆ ](#ga6b25a6076791c4a559aa20633b49b07e)sys\_cache\_data\_line\_size\_get()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sys\_cache\_data\_line\_size\_get | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cache.h](cache_8h.md)>`

Get the d-cache line size.

The API is provided to get the data cache line.

The cache line size is calculated (in order of priority):

- At run-time when `CONFIG_DCACHE_LINE_SIZE_DETECT` is set.
- At compile time using the value set in `CONFIG_DCACHE_LINE_SIZE`.
- At compile time using the d-cache-line-size CPU0 property of the DT.
- 0 otherwise

Return values
:   | size | Size of the d-cache line. |
    | --- | --- |
    | 0 | If the d-cache is not enabled. |

## [◆ ](#ga502377e711c5399926992e530456af60)sys\_cache\_instr\_disable()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void sys\_cache\_instr\_disable | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cache.h](cache_8h.md)>`

Disable the i-cache.

Disable the instruction cache

## [◆ ](#ga98bd00d87195cbf5f99cea4b68765a7f)sys\_cache\_instr\_enable()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void sys\_cache\_instr\_enable | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cache.h](cache_8h.md)>`

Enable the i-cache.

Enable the instruction cache

## [◆ ](#ga6846744d9cdfe5d164679f12abe31e48)sys\_cache\_instr\_flush\_all()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int sys\_cache\_instr\_flush\_all | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cache.h](cache_8h.md)>`

Flush the i-cache.

Flush the whole instruction cache.

Return values
:   | 0 | If succeeded. |
    | --- | --- |
    | -ENOTSUP | If not supported. |
    | -errno | Negative errno for other failures. |

## [◆ ](#ga3ac77afb61ae32cc0af7bd61e07cf765)sys\_cache\_instr\_flush\_and\_invd\_all()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int sys\_cache\_instr\_flush\_and\_invd\_all | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cache.h](cache_8h.md)>`

Flush and Invalidate the i-cache.

Flush and Invalidate the whole instruction cache.

Return values
:   | 0 | If succeeded. |
    | --- | --- |
    | -ENOTSUP | If not supported. |
    | -errno | Negative errno for other failures. |

## [◆ ](#ga768ada6618e2b9ddc5ba3bb54ba48773)sys\_cache\_instr\_flush\_and\_invd\_range()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int sys\_cache\_instr\_flush\_and\_invd\_range | ( | void \* | *addr*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cache.h](cache_8h.md)>`

Flush and Invalidate an address range in the i-cache.

Flush and Invalidate the specified address range of the instruction cache.

Note
:   the cache operations act on cache line. When multiple data structures share the same cache line being flushed, all the portions of the data structures sharing the same line will be flushed before being invalidated. This is usually not a problem because writing back is a non-destructive process that could be triggered by hardware at any time, so having an aligned `addr` or a padded `size` is not strictly necessary.

Parameters
:   | addr | Starting address to flush and invalidate. |
    | --- | --- |
    | size | Range size. |

Return values
:   | 0 | If succeeded. |
    | --- | --- |
    | -ENOTSUP | If not supported. |
    | -errno | Negative errno for other failures. |

## [◆ ](#ga628ee038060351a9958067dfc2e3192c)sys\_cache\_instr\_flush\_range()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int sys\_cache\_instr\_flush\_range | ( | void \* | *addr*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cache.h](cache_8h.md)>`

Flush an address range in the i-cache.

Flush the specified address range of the instruction cache.

Note
:   the cache operations act on cache line. When multiple data structures share the same cache line being flushed, all the portions of the data structures sharing the same line will be flushed. This is usually not a problem because writing back is a non-destructive process that could be triggered by hardware at any time, so having an aligned `addr` or a padded `size` is not strictly necessary.

Parameters
:   | addr | Starting address to flush. |
    | --- | --- |
    | size | Range size. |

Return values
:   | 0 | If succeeded. |
    | --- | --- |
    | -ENOTSUP | If not supported. |
    | -errno | Negative errno for other failures. |

## [◆ ](#gadc460f782f2642203e1bd4797dd46308)sys\_cache\_instr\_invd\_all()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int sys\_cache\_instr\_invd\_all | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cache.h](cache_8h.md)>`

Invalidate the i-cache.

Invalidate the whole instruction cache.

Return values
:   | 0 | If succeeded. |
    | --- | --- |
    | -ENOTSUP | If not supported. |
    | -errno | Negative errno for other failures. |

## [◆ ](#ga7cc3e53a18492b871b69af8b2d1d0db9)sys\_cache\_instr\_invd\_range()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int sys\_cache\_instr\_invd\_range | ( | void \* | *addr*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cache.h](cache_8h.md)>`

Invalidate an address range in the i-cache.

Invalidate the specified address range of the instruction cache.

Note
:   the cache operations act on cache line. When multiple data structures share the same cache line being invalidated, all the portions of the non-read-only data structures sharing the same line will be invalidated as well. This is a destructive process that could lead to data loss and/or corruption. When `addr` is not aligned to the cache line and/or `size` is not a multiple of the cache line size the behaviour is undefined.

Parameters
:   | addr | Starting address to invalidate. |
    | --- | --- |
    | size | Range size. |

Return values
:   | 0 | If succeeded. |
    | --- | --- |
    | -ENOTSUP | If not supported. |
    | -errno | Negative errno for other failures. |

## [◆ ](#ga4d130b1ef9a3ecfcd08c0eb2f474e5f1)sys\_cache\_instr\_line\_size\_get()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sys\_cache\_instr\_line\_size\_get | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cache.h](cache_8h.md)>`

Get the i-cache line size.

The API is provided to get the instruction cache line.

The cache line size is calculated (in order of priority):

- At run-time when `CONFIG_ICACHE_LINE_SIZE_DETECT` is set.
- At compile time using the value set in `CONFIG_ICACHE_LINE_SIZE`.
- At compile time using the i-cache-line-size CPU0 property of the DT.
- 0 otherwise

Return values
:   | size | Size of the d-cache line. |
    | --- | --- |
    | 0 | If the d-cache is not enabled. |

## [◆ ](#ga0d21da511beb423a64d9bb23e6b5dacf)sys\_cache\_is\_ptr\_cached()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_cache\_is\_ptr\_cached | ( | void \* | *ptr* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cache.h](cache_8h.md)>`

Test if a pointer is in cached region.

Some hardware may map the same physical memory twice so that it can be seen in both (incoherent) cached mappings and a coherent "shared" area. This tests if a particular pointer is within the cached, coherent area.

Parameters
:   | ptr | Pointer |
    | --- | --- |

Return values
:   | True | if pointer is in cached region. |
    | --- | --- |
    | False | if pointer is not in cached region. |

## [◆ ](#gaa02f0bac4addff95dda539dca2b1d4d1)sys\_cache\_is\_ptr\_uncached()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_cache\_is\_ptr\_uncached | ( | void \* | *ptr* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cache.h](cache_8h.md)>`

Test if a pointer is in un-cached region.

Some hardware may map the same physical memory twice so that it can be seen in both (incoherent) cached mappings and a coherent "shared" area. This tests if a particular pointer is within the un-cached, incoherent area.

Parameters
:   | ptr | Pointer |
    | --- | --- |

Return values
:   | True | if pointer is not in cached region. |
    | --- | --- |
    | False | if pointer is in cached region. |

## [◆ ](#ga1410d43a8c6d16e1b54a32868eaecfe3)sys\_cache\_uncached\_ptr\_get()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void \* sys\_cache\_uncached\_ptr\_get | ( | void \* | *ptr* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cache.h](cache_8h.md)>`

Return uncached pointer to a RAM address.

This function takes a pointer to any addressable object (either in cacheable memory or not) and returns a pointer that can be used to refer to the same memory while bypassing the L1 data cache. Data in the L1 cache will not be inspected nor modified by the access.

Note
:   This API returns the same pointer if CONFIG\_CACHE\_DOUBLEMAP is not enabled.

See also
:   arch\_cached\_ptr()

Parameters
:   | ptr | A pointer to a valid C object |
    | --- | --- |

Returns
:   A pointer to the same object bypassing the L1 dcache

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
