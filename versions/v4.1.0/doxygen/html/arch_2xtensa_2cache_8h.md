---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arch_2xtensa_2cache_8h.html
original_path: doxygen/html/arch_2xtensa_2cache_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cache.h File Reference

`#include <xtensa/config/core-isa.h>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/debug/sparse.h](sparse_8h_source.md)>`  
`#include <xtensa/hal.h>`

[Go to the source code of this file.](arch_2xtensa_2cache_8h_source.md)

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [arch\_dcache\_flush\_range](#a67b31dd2c4be8f94d95a7eb9d5f9b3c9) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Implementation of [arch\_dcache\_flush\_range](group__cache__arch__interface.md#ga3a5b7426358790e7c54df7556bf2e6b8 "arch_dcache_flush_range"). |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [arch\_dcache\_flush\_and\_invd\_range](#a83106c2dd8004a0d308f26265f20a2c3) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Implementation of [arch\_dcache\_flush\_and\_invd\_range](group__cache__arch__interface.md#gaf3afa0d36939f30a1995bf0755047122 "arch_dcache_flush_and_invd_range"). |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [arch\_dcache\_invd\_range](#a92b35e4648bac37f0ca709054320c125) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Implementation of [arch\_dcache\_invd\_range](group__cache__arch__interface.md#ga1e12e643ba5855dd0cb67d2cc7fbb9ef "arch_dcache_invd_range"). |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [arch\_dcache\_invd\_all](#a8a5666d8ab2fd898413d1b836c69adc3) (void) |
|  | Implementation of [arch\_dcache\_invd\_all](group__cache__arch__interface.md#gacd9eed889dacd5dd42dab15b2dcc4097 "arch_dcache_invd_all"). |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [arch\_dcache\_flush\_all](#a3386effa850b7b46773a7ca082d2f695) (void) |
|  | Implementation of [arch\_dcache\_flush\_all](group__cache__arch__interface.md#ga9ec6cbe750133540d8f0460bfb8ca9d4 "arch_dcache_flush_all"). |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [arch\_dcache\_flush\_and\_invd\_all](#a61de91dc463ddc8f53855bbb68776752) (void) |
|  | Implementation of [arch\_dcache\_flush\_and\_invd\_all](group__cache__arch__interface.md#gac58493d5f3726d7e4131c48e9a6c75f9 "arch_dcache_flush_and_invd_all"). |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [arch\_dcache\_enable](#a2d311a83cbd78a7d959cc0216d42701b) (void) |
|  | Implementation of [arch\_dcache\_enable](group__cache__arch__interface.md#gaf616ce5134f8fd3a0fe0f690069915ce "arch_dcache_enable"). |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [arch\_dcache\_disable](#af789498070dadadafd15af00900fae8b) (void) |
|  | Implementation of [arch\_dcache\_disable](group__cache__arch__interface.md#ga01f917f9125a5fb38d9ec4b256630a80 "arch_dcache_disable"). |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [arch\_icache\_line\_size\_get](#aafeb5923d0e811759cee20e5f7dcb40a) (void) |
|  | Implementation of [arch\_icache\_line\_size\_get](group__cache__arch__interface.md#ga717d37451103b7680bb54044d6ab1841 "arch_icache_line_size_get"). |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [arch\_icache\_flush\_all](#ae6cb0ef4fbcbffc551daf428bffbb54b) (void) |
|  | Implementation of [arch\_icache\_flush\_all](group__cache__arch__interface.md#ga29fd1d9d9ba54306e00b6b3a393446a7 "arch_icache_flush_all"). |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [arch\_icache\_invd\_all](#afbd63018906d9d721eb752340bc111d9) (void) |
|  | Implementation of [arch\_icache\_invd\_all](group__cache__arch__interface.md#ga2bfbf102e413fc8af43f1fd15a79a093 "arch_icache_invd_all"). |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [arch\_icache\_flush\_and\_invd\_all](#a51cab7fde80d6c07621ac721f73d8e1c) (void) |
|  | Implementation of [arch\_icache\_flush\_and\_invd\_all](group__cache__arch__interface.md#ga29ae28d6e04ea0b136bcba5e461a7d6d "arch_icache_flush_and_invd_all"). |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [arch\_icache\_flush\_range](#aa676959f8b53e0860be8a92b2ae0e56f) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Implementation of [arch\_icache\_flush\_range](group__cache__arch__interface.md#ga7f6af61969ce97179f60ec483803500b "arch_icache_flush_range"). |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [arch\_icache\_invd\_range](#ad1fcc25b06988a18ae2d3ba28d26faea) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Implementation of [arch\_icache\_invd\_range](group__cache__arch__interface.md#ga84e877997349df3e53eed11be6fc3caa "arch_icache_invd_range"). |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [arch\_icache\_flush\_and\_invd\_range](#a731ad4f69a6d52df276d09a662ea5f0a) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Implementation of [arch\_icache\_flush\_and\_invd\_range](group__cache__arch__interface.md#gaa6caab419ca57523db54eb9125e7e1d0 "arch_icache_flush_and_invd_range"). |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [arch\_icache\_enable](#a4420e7af2ca86b8da4b3d720d61cbf3b) (void) |
|  | Implementation of [arch\_icache\_enable](group__cache__arch__interface.md#gadb5dec5f9597565f597ba5592a330050 "arch_icache_enable"). |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [arch\_icache\_disable](#a3529c39dad808265db75036938ea8a61) (void) |
|  | Implementation of [arch\_icache\_disable](group__cache__arch__interface.md#ga03c14fd66267240460b0a37d72a3a971 "arch_icache_disable"). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_cache\_is\_ptr\_cached](#a7e8218e05aa541964a0387bbe28a40e5) (void \*ptr) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_cache\_is\_ptr\_uncached](#a8098fec4edbd77142b9f94f04bc61e4e) (void \*ptr) |
| static void \* | [arch\_cache\_cached\_ptr\_get](#afa8a52786bd86cb3305b9a4d37c5f27c) (void \*ptr) |
| static void \* | [arch\_cache\_uncached\_ptr\_get](#adf2d51455bdd6ff36609c6c68fe0fdc7) (void \*ptr) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [arch\_cache\_init](#a183fd26e5a8a478562d39c6fbe6a85bc) (void) |

## Function Documentation

## [◆ ](#afa8a52786bd86cb3305b9a4d37c5f27c)arch\_cache\_cached\_ptr\_get()

| | void \* arch\_cache\_cached\_ptr\_get | ( | void \* | *ptr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a183fd26e5a8a478562d39c6fbe6a85bc)arch\_cache\_init()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void arch\_cache\_init | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a7e8218e05aa541964a0387bbe28a40e5)arch\_cache\_is\_ptr\_cached()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) arch\_cache\_is\_ptr\_cached | ( | void \* | *ptr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a8098fec4edbd77142b9f94f04bc61e4e)arch\_cache\_is\_ptr\_uncached()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) arch\_cache\_is\_ptr\_uncached | ( | void \* | *ptr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#adf2d51455bdd6ff36609c6c68fe0fdc7)arch\_cache\_uncached\_ptr\_get()

| | void \* arch\_cache\_uncached\_ptr\_get | ( | void \* | *ptr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#af789498070dadadafd15af00900fae8b)arch\_dcache\_disable()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void arch\_dcache\_disable | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_dcache\_disable](group__cache__arch__interface.md#ga01f917f9125a5fb38d9ec4b256630a80 "arch_dcache_disable").

## [◆ ](#a2d311a83cbd78a7d959cc0216d42701b)arch\_dcache\_enable()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void arch\_dcache\_enable | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_dcache\_enable](group__cache__arch__interface.md#gaf616ce5134f8fd3a0fe0f690069915ce "arch_dcache_enable").

## [◆ ](#a3386effa850b7b46773a7ca082d2f695)arch\_dcache\_flush\_all()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int arch\_dcache\_flush\_all | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_dcache\_flush\_all](group__cache__arch__interface.md#ga9ec6cbe750133540d8f0460bfb8ca9d4 "arch_dcache_flush_all").

## [◆ ](#a61de91dc463ddc8f53855bbb68776752)arch\_dcache\_flush\_and\_invd\_all()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int arch\_dcache\_flush\_and\_invd\_all | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_dcache\_flush\_and\_invd\_all](group__cache__arch__interface.md#gac58493d5f3726d7e4131c48e9a6c75f9 "arch_dcache_flush_and_invd_all").

## [◆ ](#a83106c2dd8004a0d308f26265f20a2c3)arch\_dcache\_flush\_and\_invd\_range()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int arch\_dcache\_flush\_and\_invd\_range | ( | void \* | *addr*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bytes* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_dcache\_flush\_and\_invd\_range](group__cache__arch__interface.md#gaf3afa0d36939f30a1995bf0755047122 "arch_dcache_flush_and_invd_range").

## [◆ ](#a67b31dd2c4be8f94d95a7eb9d5f9b3c9)arch\_dcache\_flush\_range()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int arch\_dcache\_flush\_range | ( | void \* | *addr*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bytes* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_dcache\_flush\_range](group__cache__arch__interface.md#ga3a5b7426358790e7c54df7556bf2e6b8 "arch_dcache_flush_range").

## [◆ ](#a8a5666d8ab2fd898413d1b836c69adc3)arch\_dcache\_invd\_all()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int arch\_dcache\_invd\_all | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_dcache\_invd\_all](group__cache__arch__interface.md#gacd9eed889dacd5dd42dab15b2dcc4097 "arch_dcache_invd_all").

## [◆ ](#a92b35e4648bac37f0ca709054320c125)arch\_dcache\_invd\_range()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int arch\_dcache\_invd\_range | ( | void \* | *addr*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bytes* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_dcache\_invd\_range](group__cache__arch__interface.md#ga1e12e643ba5855dd0cb67d2cc7fbb9ef "arch_dcache_invd_range").

## [◆ ](#a3529c39dad808265db75036938ea8a61)arch\_icache\_disable()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void arch\_icache\_disable | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_icache\_disable](group__cache__arch__interface.md#ga03c14fd66267240460b0a37d72a3a971 "arch_icache_disable").

## [◆ ](#a4420e7af2ca86b8da4b3d720d61cbf3b)arch\_icache\_enable()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void arch\_icache\_enable | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_icache\_enable](group__cache__arch__interface.md#gadb5dec5f9597565f597ba5592a330050 "arch_icache_enable").

## [◆ ](#ae6cb0ef4fbcbffc551daf428bffbb54b)arch\_icache\_flush\_all()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int arch\_icache\_flush\_all | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_icache\_flush\_all](group__cache__arch__interface.md#ga29fd1d9d9ba54306e00b6b3a393446a7 "arch_icache_flush_all").

## [◆ ](#a51cab7fde80d6c07621ac721f73d8e1c)arch\_icache\_flush\_and\_invd\_all()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int arch\_icache\_flush\_and\_invd\_all | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_icache\_flush\_and\_invd\_all](group__cache__arch__interface.md#ga29ae28d6e04ea0b136bcba5e461a7d6d "arch_icache_flush_and_invd_all").

## [◆ ](#a731ad4f69a6d52df276d09a662ea5f0a)arch\_icache\_flush\_and\_invd\_range()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int arch\_icache\_flush\_and\_invd\_range | ( | void \* | *addr*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_icache\_flush\_and\_invd\_range](group__cache__arch__interface.md#gaa6caab419ca57523db54eb9125e7e1d0 "arch_icache_flush_and_invd_range").

## [◆ ](#aa676959f8b53e0860be8a92b2ae0e56f)arch\_icache\_flush\_range()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int arch\_icache\_flush\_range | ( | void \* | *addr*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_icache\_flush\_range](group__cache__arch__interface.md#ga7f6af61969ce97179f60ec483803500b "arch_icache_flush_range").

## [◆ ](#afbd63018906d9d721eb752340bc111d9)arch\_icache\_invd\_all()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int arch\_icache\_invd\_all | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_icache\_invd\_all](group__cache__arch__interface.md#ga2bfbf102e413fc8af43f1fd15a79a093 "arch_icache_invd_all").

## [◆ ](#ad1fcc25b06988a18ae2d3ba28d26faea)arch\_icache\_invd\_range()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int arch\_icache\_invd\_range | ( | void \* | *addr*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_icache\_invd\_range](group__cache__arch__interface.md#ga84e877997349df3e53eed11be6fc3caa "arch_icache_invd_range").

## [◆ ](#aafeb5923d0e811759cee20e5f7dcb40a)arch\_icache\_line\_size\_get()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) arch\_icache\_line\_size\_get | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_icache\_line\_size\_get](group__cache__arch__interface.md#ga717d37451103b7680bb54044d6ab1841 "arch_icache_line_size_get").

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [cache.h](arch_2xtensa_2cache_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
