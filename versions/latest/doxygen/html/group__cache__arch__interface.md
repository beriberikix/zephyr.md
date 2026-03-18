---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__cache__arch__interface.html
original_path: doxygen/html/group__cache__arch__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Cache Controller Interface

[Device Driver APIs](group__io__interfaces.md)

Cache Controller Interface.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [cache\_data\_enable](#gaec0a2a0374c2c1fe0496f97a5e4a4456)   [arch\_dcache\_enable](#gaf616ce5134f8fd3a0fe0f690069915ce) |
| #define | [cache\_data\_disable](#gaf8e5056056c5609a8fd878f1b3aeaf5a)   [arch\_dcache\_disable](#ga01f917f9125a5fb38d9ec4b256630a80) |
| #define | [cache\_data\_flush\_all](#gae799dfd86b078f74bdeba952aa2eed92)   [arch\_dcache\_flush\_all](#ga9ec6cbe750133540d8f0460bfb8ca9d4) |
| #define | [cache\_data\_invd\_all](#gaade1db95fda43b875985d765f0aeee58)   [arch\_dcache\_invd\_all](#gacd9eed889dacd5dd42dab15b2dcc4097) |
| #define | [cache\_data\_flush\_and\_invd\_all](#gab48cc0cdaf4c6ec64748cb1d4ed51baa)   [arch\_dcache\_flush\_and\_invd\_all](#gac58493d5f3726d7e4131c48e9a6c75f9) |
| #define | [cache\_data\_flush\_range](#gab433cc69a23c0543376615336e80205b)(addr, size) |
| #define | [cache\_data\_invd\_range](#ga91e01cff6a459d21d97cd451ad63a29f)(addr, size) |
| #define | [cache\_data\_flush\_and\_invd\_range](#ga3d5443b3c6f83840c39bc177256ec24f)(addr, size) |
| #define | [cache\_data\_line\_size\_get](#gafdf1e8c95982a1fe5f39139d0fc6ab25)   [arch\_dcache\_line\_size\_get](#ga559156a12e712c641ca62dab7433e93e) |
| #define | [cache\_instr\_enable](#ga5f51912f5dba3e361e5849c4989d8260)   [arch\_icache\_enable](#gadb5dec5f9597565f597ba5592a330050) |
| #define | [cache\_instr\_disable](#ga287ead9fa07e9c13ba803a1fc3335479)   [arch\_icache\_disable](#ga03c14fd66267240460b0a37d72a3a971) |
| #define | [cache\_instr\_flush\_all](#ga3d02e8f383c9b15354c14274bf9daee8)   [arch\_icache\_flush\_all](#ga29fd1d9d9ba54306e00b6b3a393446a7) |
| #define | [cache\_instr\_invd\_all](#ga1f4241624e3879e8b43556d65867be22)   [arch\_icache\_invd\_all](#ga2bfbf102e413fc8af43f1fd15a79a093) |
| #define | [cache\_instr\_flush\_and\_invd\_all](#ga585fe4e3511d01af2585c439d722e828)   [arch\_icache\_flush\_and\_invd\_all](#ga29ae28d6e04ea0b136bcba5e461a7d6d) |
| #define | [cache\_instr\_flush\_range](#ga909eb6d67a146c97ffebd91a08419479)(addr, size) |
| #define | [cache\_instr\_invd\_range](#ga4f334ddb832d247041b95a177a426cb9)(addr, size) |
| #define | [cache\_instr\_flush\_and\_invd\_range](#ga96f1d12e5c52ed4063662cd8853f400c)(addr, size) |
| #define | [cache\_instr\_line\_size\_get](#gaf80d88e95d4eb6ab63301a5dee5a37fe)   [arch\_icache\_line\_size\_get](#ga717d37451103b7680bb54044d6ab1841) |
| #define | [cache\_is\_ptr\_cached](#gab3c3dd74ba3eb870fafe27a82ae6fa69)(ptr) |
| #define | [cache\_is\_ptr\_uncached](#ga3444529ef90c2a4de948967fe8cb48b7)(ptr) |
| #define | [cache\_cached\_ptr](#ga27e186c66d70ec25b665e0e88124a52a)(ptr) |
| #define | [cache\_uncached\_ptr](#ga11eb33eddf161352f5bbac9a4d6aed90)(ptr) |

| Functions | |
| --- | --- |
| void | [arch\_dcache\_enable](#gaf616ce5134f8fd3a0fe0f690069915ce) (void) |
|  | Enable the d-cache. |
| void | [arch\_dcache\_disable](#ga01f917f9125a5fb38d9ec4b256630a80) (void) |
|  | Disable the d-cache. |
| int | [arch\_dcache\_flush\_all](#ga9ec6cbe750133540d8f0460bfb8ca9d4) (void) |
|  | Flush the d-cache. |
| int | [arch\_dcache\_invd\_all](#gacd9eed889dacd5dd42dab15b2dcc4097) (void) |
|  | Invalidate the d-cache. |
| int | [arch\_dcache\_flush\_and\_invd\_all](#gac58493d5f3726d7e4131c48e9a6c75f9) (void) |
|  | Flush and Invalidate the d-cache. |
| int | [arch\_dcache\_flush\_range](#ga3a5b7426358790e7c54df7556bf2e6b8) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Flush an address range in the d-cache. |
| int | [arch\_dcache\_invd\_range](#ga1e12e643ba5855dd0cb67d2cc7fbb9ef) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Invalidate an address range in the d-cache. |
| int | [arch\_dcache\_flush\_and\_invd\_range](#gaf3afa0d36939f30a1995bf0755047122) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Flush and Invalidate an address range in the d-cache. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [arch\_dcache\_line\_size\_get](#ga559156a12e712c641ca62dab7433e93e) (void) |
|  | Get the d-cache line size. |
| void | [arch\_icache\_enable](#gadb5dec5f9597565f597ba5592a330050) (void) |
|  | Enable the i-cache. |
| void | [arch\_icache\_disable](#ga03c14fd66267240460b0a37d72a3a971) (void) |
|  | Disable the i-cache. |
| int | [arch\_icache\_flush\_all](#ga29fd1d9d9ba54306e00b6b3a393446a7) (void) |
|  | Flush the i-cache. |
| int | [arch\_icache\_invd\_all](#ga2bfbf102e413fc8af43f1fd15a79a093) (void) |
|  | Invalidate the i-cache. |
| int | [arch\_icache\_flush\_and\_invd\_all](#ga29ae28d6e04ea0b136bcba5e461a7d6d) (void) |
|  | Flush and Invalidate the i-cache. |
| int | [arch\_icache\_flush\_range](#ga7f6af61969ce97179f60ec483803500b) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Flush an address range in the i-cache. |
| int | [arch\_icache\_invd\_range](#ga84e877997349df3e53eed11be6fc3caa) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Invalidate an address range in the i-cache. |
| int | [arch\_icache\_flush\_and\_invd\_range](#gaa6caab419ca57523db54eb9125e7e1d0) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Flush and Invalidate an address range in the i-cache. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [arch\_icache\_line\_size\_get](#ga717d37451103b7680bb54044d6ab1841) (void) |
|  | Get the i-cache line size. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_cache\_is\_ptr\_cached](#ga9ed1c303508eb68db80f14fdb6eb7faa) (void \*ptr) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_cache\_is\_ptr\_uncached](#gab6bdf8089dce42e4463f761bae56e652) (void \*ptr) |
| void \* | [arch\_cache\_cached\_ptr\_get](#gabb31cd28a68b529ec0d7c389bb65bd9c) (void \*ptr) |
| void \* | [arch\_cache\_uncached\_ptr\_get](#ga1b507969ecccdaf7e47b16ba190bf816) (void \*ptr) |

## Detailed Description

Cache Controller Interface.

## Macro Definition Documentation

## [◆ ](#ga27e186c66d70ec25b665e0e88124a52a)cache\_cached\_ptr

| #define cache\_cached\_ptr | ( |  | *ptr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cache.h](arch_2cache_8h.md)>`

**Value:**

[arch\_cache\_cached\_ptr\_get](#gabb31cd28a68b529ec0d7c389bb65bd9c)(ptr)

[arch\_cache\_cached\_ptr\_get](#gabb31cd28a68b529ec0d7c389bb65bd9c)

void \* arch\_cache\_cached\_ptr\_get(void \*ptr)

## [◆ ](#gaf8e5056056c5609a8fd878f1b3aeaf5a)cache\_data\_disable

| #define cache\_data\_disable   [arch\_dcache\_disable](#ga01f917f9125a5fb38d9ec4b256630a80) |
| --- |

`#include <[cache.h](arch_2cache_8h.md)>`

## [◆ ](#gaec0a2a0374c2c1fe0496f97a5e4a4456)cache\_data\_enable

| #define cache\_data\_enable   [arch\_dcache\_enable](#gaf616ce5134f8fd3a0fe0f690069915ce) |
| --- |

`#include <[cache.h](arch_2cache_8h.md)>`

## [◆ ](#gae799dfd86b078f74bdeba952aa2eed92)cache\_data\_flush\_all

| #define cache\_data\_flush\_all   [arch\_dcache\_flush\_all](#ga9ec6cbe750133540d8f0460bfb8ca9d4) |
| --- |

`#include <[cache.h](arch_2cache_8h.md)>`

## [◆ ](#gab48cc0cdaf4c6ec64748cb1d4ed51baa)cache\_data\_flush\_and\_invd\_all

| #define cache\_data\_flush\_and\_invd\_all   [arch\_dcache\_flush\_and\_invd\_all](#gac58493d5f3726d7e4131c48e9a6c75f9) |
| --- |

`#include <[cache.h](arch_2cache_8h.md)>`

## [◆ ](#ga3d5443b3c6f83840c39bc177256ec24f)cache\_data\_flush\_and\_invd\_range

| #define cache\_data\_flush\_and\_invd\_range | ( |  | *addr*, |
| --- | --- | --- | --- |
|  |  |  | *size* ) |

`#include <[cache.h](arch_2cache_8h.md)>`

**Value:**

[arch\_dcache\_flush\_and\_invd\_range](#gaf3afa0d36939f30a1995bf0755047122)(addr, size)

[arch\_dcache\_flush\_and\_invd\_range](#gaf3afa0d36939f30a1995bf0755047122)

int arch\_dcache\_flush\_and\_invd\_range(void \*addr, size\_t size)

Flush and Invalidate an address range in the d-cache.

## [◆ ](#gab433cc69a23c0543376615336e80205b)cache\_data\_flush\_range

| #define cache\_data\_flush\_range | ( |  | *addr*, |
| --- | --- | --- | --- |
|  |  |  | *size* ) |

`#include <[cache.h](arch_2cache_8h.md)>`

**Value:**

[arch\_dcache\_flush\_range](#ga3a5b7426358790e7c54df7556bf2e6b8)(addr, size)

[arch\_dcache\_flush\_range](#ga3a5b7426358790e7c54df7556bf2e6b8)

int arch\_dcache\_flush\_range(void \*addr, size\_t size)

Flush an address range in the d-cache.

## [◆ ](#gaade1db95fda43b875985d765f0aeee58)cache\_data\_invd\_all

| #define cache\_data\_invd\_all   [arch\_dcache\_invd\_all](#gacd9eed889dacd5dd42dab15b2dcc4097) |
| --- |

`#include <[cache.h](arch_2cache_8h.md)>`

## [◆ ](#ga91e01cff6a459d21d97cd451ad63a29f)cache\_data\_invd\_range

| #define cache\_data\_invd\_range | ( |  | *addr*, |
| --- | --- | --- | --- |
|  |  |  | *size* ) |

`#include <[cache.h](arch_2cache_8h.md)>`

**Value:**

[arch\_dcache\_invd\_range](#ga1e12e643ba5855dd0cb67d2cc7fbb9ef)(addr, size)

[arch\_dcache\_invd\_range](#ga1e12e643ba5855dd0cb67d2cc7fbb9ef)

int arch\_dcache\_invd\_range(void \*addr, size\_t size)

Invalidate an address range in the d-cache.

## [◆ ](#gafdf1e8c95982a1fe5f39139d0fc6ab25)cache\_data\_line\_size\_get

| #define cache\_data\_line\_size\_get   [arch\_dcache\_line\_size\_get](#ga559156a12e712c641ca62dab7433e93e) |
| --- |

`#include <[cache.h](arch_2cache_8h.md)>`

## [◆ ](#ga287ead9fa07e9c13ba803a1fc3335479)cache\_instr\_disable

| #define cache\_instr\_disable   [arch\_icache\_disable](#ga03c14fd66267240460b0a37d72a3a971) |
| --- |

`#include <[cache.h](arch_2cache_8h.md)>`

## [◆ ](#ga5f51912f5dba3e361e5849c4989d8260)cache\_instr\_enable

| #define cache\_instr\_enable   [arch\_icache\_enable](#gadb5dec5f9597565f597ba5592a330050) |
| --- |

`#include <[cache.h](arch_2cache_8h.md)>`

## [◆ ](#ga3d02e8f383c9b15354c14274bf9daee8)cache\_instr\_flush\_all

| #define cache\_instr\_flush\_all   [arch\_icache\_flush\_all](#ga29fd1d9d9ba54306e00b6b3a393446a7) |
| --- |

`#include <[cache.h](arch_2cache_8h.md)>`

## [◆ ](#ga585fe4e3511d01af2585c439d722e828)cache\_instr\_flush\_and\_invd\_all

| #define cache\_instr\_flush\_and\_invd\_all   [arch\_icache\_flush\_and\_invd\_all](#ga29ae28d6e04ea0b136bcba5e461a7d6d) |
| --- |

`#include <[cache.h](arch_2cache_8h.md)>`

## [◆ ](#ga96f1d12e5c52ed4063662cd8853f400c)cache\_instr\_flush\_and\_invd\_range

| #define cache\_instr\_flush\_and\_invd\_range | ( |  | *addr*, |
| --- | --- | --- | --- |
|  |  |  | *size* ) |

`#include <[cache.h](arch_2cache_8h.md)>`

**Value:**

[arch\_icache\_flush\_and\_invd\_range](#gaa6caab419ca57523db54eb9125e7e1d0)(addr, size)

[arch\_icache\_flush\_and\_invd\_range](#gaa6caab419ca57523db54eb9125e7e1d0)

int arch\_icache\_flush\_and\_invd\_range(void \*addr, size\_t size)

Flush and Invalidate an address range in the i-cache.

## [◆ ](#ga909eb6d67a146c97ffebd91a08419479)cache\_instr\_flush\_range

| #define cache\_instr\_flush\_range | ( |  | *addr*, |
| --- | --- | --- | --- |
|  |  |  | *size* ) |

`#include <[cache.h](arch_2cache_8h.md)>`

**Value:**

[arch\_icache\_flush\_range](#ga7f6af61969ce97179f60ec483803500b)(addr, size)

[arch\_icache\_flush\_range](#ga7f6af61969ce97179f60ec483803500b)

int arch\_icache\_flush\_range(void \*addr, size\_t size)

Flush an address range in the i-cache.

## [◆ ](#ga1f4241624e3879e8b43556d65867be22)cache\_instr\_invd\_all

| #define cache\_instr\_invd\_all   [arch\_icache\_invd\_all](#ga2bfbf102e413fc8af43f1fd15a79a093) |
| --- |

`#include <[cache.h](arch_2cache_8h.md)>`

## [◆ ](#ga4f334ddb832d247041b95a177a426cb9)cache\_instr\_invd\_range

| #define cache\_instr\_invd\_range | ( |  | *addr*, |
| --- | --- | --- | --- |
|  |  |  | *size* ) |

`#include <[cache.h](arch_2cache_8h.md)>`

**Value:**

[arch\_icache\_invd\_range](#ga84e877997349df3e53eed11be6fc3caa)(addr, size)

[arch\_icache\_invd\_range](#ga84e877997349df3e53eed11be6fc3caa)

int arch\_icache\_invd\_range(void \*addr, size\_t size)

Invalidate an address range in the i-cache.

## [◆ ](#gaf80d88e95d4eb6ab63301a5dee5a37fe)cache\_instr\_line\_size\_get

| #define cache\_instr\_line\_size\_get   [arch\_icache\_line\_size\_get](#ga717d37451103b7680bb54044d6ab1841) |
| --- |

`#include <[cache.h](arch_2cache_8h.md)>`

## [◆ ](#gab3c3dd74ba3eb870fafe27a82ae6fa69)cache\_is\_ptr\_cached

| #define cache\_is\_ptr\_cached | ( |  | *ptr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cache.h](arch_2cache_8h.md)>`

**Value:**

[arch\_cache\_is\_ptr\_cached](#ga9ed1c303508eb68db80f14fdb6eb7faa)(ptr)

[arch\_cache\_is\_ptr\_cached](#ga9ed1c303508eb68db80f14fdb6eb7faa)

bool arch\_cache\_is\_ptr\_cached(void \*ptr)

## [◆ ](#ga3444529ef90c2a4de948967fe8cb48b7)cache\_is\_ptr\_uncached

| #define cache\_is\_ptr\_uncached | ( |  | *ptr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cache.h](arch_2cache_8h.md)>`

**Value:**

[arch\_cache\_is\_ptr\_uncached](#gab6bdf8089dce42e4463f761bae56e652)(ptr)

[arch\_cache\_is\_ptr\_uncached](#gab6bdf8089dce42e4463f761bae56e652)

bool arch\_cache\_is\_ptr\_uncached(void \*ptr)

## [◆ ](#ga11eb33eddf161352f5bbac9a4d6aed90)cache\_uncached\_ptr

| #define cache\_uncached\_ptr | ( |  | *ptr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cache.h](arch_2cache_8h.md)>`

**Value:**

[arch\_cache\_uncached\_ptr\_get](#ga1b507969ecccdaf7e47b16ba190bf816)(ptr)

[arch\_cache\_uncached\_ptr\_get](#ga1b507969ecccdaf7e47b16ba190bf816)

void \* arch\_cache\_uncached\_ptr\_get(void \*ptr)

## Function Documentation

## [◆ ](#gabb31cd28a68b529ec0d7c389bb65bd9c)arch\_cache\_cached\_ptr\_get()

| void \* arch\_cache\_cached\_ptr\_get | ( | void \* | *ptr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cache.h](arch_2cache_8h.md)>`

## [◆ ](#ga9ed1c303508eb68db80f14fdb6eb7faa)arch\_cache\_is\_ptr\_cached()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) arch\_cache\_is\_ptr\_cached | ( | void \* | *ptr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cache.h](arch_2cache_8h.md)>`

## [◆ ](#gab6bdf8089dce42e4463f761bae56e652)arch\_cache\_is\_ptr\_uncached()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) arch\_cache\_is\_ptr\_uncached | ( | void \* | *ptr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cache.h](arch_2cache_8h.md)>`

## [◆ ](#ga1b507969ecccdaf7e47b16ba190bf816)arch\_cache\_uncached\_ptr\_get()

| void \* arch\_cache\_uncached\_ptr\_get | ( | void \* | *ptr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cache.h](arch_2cache_8h.md)>`

## [◆ ](#ga01f917f9125a5fb38d9ec4b256630a80)arch\_dcache\_disable()

| void arch\_dcache\_disable | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cache.h](arch_2cache_8h.md)>`

Disable the d-cache.

Disable the data cache.

## [◆ ](#gaf616ce5134f8fd3a0fe0f690069915ce)arch\_dcache\_enable()

| void arch\_dcache\_enable | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cache.h](arch_2cache_8h.md)>`

Enable the d-cache.

Enable the data cache.

## [◆ ](#ga9ec6cbe750133540d8f0460bfb8ca9d4)arch\_dcache\_flush\_all()

| int arch\_dcache\_flush\_all | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cache.h](arch_2cache_8h.md)>`

Flush the d-cache.

Flush the whole data cache.

Return values
:   | 0 | If succeeded. |
    | --- | --- |
    | -ENOTSUP | If not supported. |
    | -errno | Negative errno for other failures. |

## [◆ ](#gac58493d5f3726d7e4131c48e9a6c75f9)arch\_dcache\_flush\_and\_invd\_all()

| int arch\_dcache\_flush\_and\_invd\_all | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cache.h](arch_2cache_8h.md)>`

Flush and Invalidate the d-cache.

Flush and Invalidate the whole data cache.

Return values
:   | 0 | If succeeded. |
    | --- | --- |
    | -ENOTSUP | If not supported. |
    | -errno | Negative errno for other failures. |

## [◆ ](#gaf3afa0d36939f30a1995bf0755047122)arch\_dcache\_flush\_and\_invd\_range()

| int arch\_dcache\_flush\_and\_invd\_range | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[cache.h](arch_2cache_8h.md)>`

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

## [◆ ](#ga3a5b7426358790e7c54df7556bf2e6b8)arch\_dcache\_flush\_range()

| int arch\_dcache\_flush\_range | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[cache.h](arch_2cache_8h.md)>`

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

## [◆ ](#gacd9eed889dacd5dd42dab15b2dcc4097)arch\_dcache\_invd\_all()

| int arch\_dcache\_invd\_all | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cache.h](arch_2cache_8h.md)>`

Invalidate the d-cache.

Invalidate the whole data cache.

Return values
:   | 0 | If succeeded. |
    | --- | --- |
    | -ENOTSUP | If not supported. |
    | -errno | Negative errno for other failures. |

## [◆ ](#ga1e12e643ba5855dd0cb67d2cc7fbb9ef)arch\_dcache\_invd\_range()

| int arch\_dcache\_invd\_range | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[cache.h](arch_2cache_8h.md)>`

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

## [◆ ](#ga559156a12e712c641ca62dab7433e93e)arch\_dcache\_line\_size\_get()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) arch\_dcache\_line\_size\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cache.h](arch_2cache_8h.md)>`

Get the d-cache line size.

The API is provided to dynamically detect the data cache line size at run time.

The function must be implemented only when CONFIG\_DCACHE\_LINE\_SIZE\_DETECT is defined.

Return values
:   | size | Size of the d-cache line. |
    | --- | --- |
    | 0 | If the d-cache is not enabled. |

## [◆ ](#ga03c14fd66267240460b0a37d72a3a971)arch\_icache\_disable()

| void arch\_icache\_disable | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cache.h](arch_2cache_8h.md)>`

Disable the i-cache.

Disable the instruction cache.

## [◆ ](#gadb5dec5f9597565f597ba5592a330050)arch\_icache\_enable()

| void arch\_icache\_enable | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cache.h](arch_2cache_8h.md)>`

Enable the i-cache.

Enable the instruction cache.

## [◆ ](#ga29fd1d9d9ba54306e00b6b3a393446a7)arch\_icache\_flush\_all()

| int arch\_icache\_flush\_all | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cache.h](arch_2cache_8h.md)>`

Flush the i-cache.

Flush the whole instruction cache.

Return values
:   | 0 | If succeeded. |
    | --- | --- |
    | -ENOTSUP | If not supported. |
    | -errno | Negative errno for other failures. |

## [◆ ](#ga29ae28d6e04ea0b136bcba5e461a7d6d)arch\_icache\_flush\_and\_invd\_all()

| int arch\_icache\_flush\_and\_invd\_all | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cache.h](arch_2cache_8h.md)>`

Flush and Invalidate the i-cache.

Flush and Invalidate the whole instruction cache.

Return values
:   | 0 | If succeeded. |
    | --- | --- |
    | -ENOTSUP | If not supported. |
    | -errno | Negative errno for other failures. |

## [◆ ](#gaa6caab419ca57523db54eb9125e7e1d0)arch\_icache\_flush\_and\_invd\_range()

| int arch\_icache\_flush\_and\_invd\_range | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[cache.h](arch_2cache_8h.md)>`

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

## [◆ ](#ga7f6af61969ce97179f60ec483803500b)arch\_icache\_flush\_range()

| int arch\_icache\_flush\_range | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[cache.h](arch_2cache_8h.md)>`

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

## [◆ ](#ga2bfbf102e413fc8af43f1fd15a79a093)arch\_icache\_invd\_all()

| int arch\_icache\_invd\_all | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cache.h](arch_2cache_8h.md)>`

Invalidate the i-cache.

Invalidate the whole instruction cache.

Return values
:   | 0 | If succeeded. |
    | --- | --- |
    | -ENOTSUP | If not supported. |
    | -errno | Negative errno for other failures. |

## [◆ ](#ga84e877997349df3e53eed11be6fc3caa)arch\_icache\_invd\_range()

| int arch\_icache\_invd\_range | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[cache.h](arch_2cache_8h.md)>`

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

## [◆ ](#ga717d37451103b7680bb54044d6ab1841)arch\_icache\_line\_size\_get()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) arch\_icache\_line\_size\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cache.h](arch_2cache_8h.md)>`

Get the i-cache line size.

The API is provided to dynamically detect the instruction cache line size at run time.

The function must be implemented only when CONFIG\_ICACHE\_LINE\_SIZE\_DETECT is defined.

Return values
:   | size | Size of the d-cache line. |
    | --- | --- |
    | 0 | If the d-cache is not enabled. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
