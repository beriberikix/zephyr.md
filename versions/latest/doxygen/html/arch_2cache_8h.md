---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arch_2cache_8h.html
original_path: doxygen/html/arch_2cache_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cache.h File Reference

Public APIs for architectural cache controller drivers.
[More...](#details)

[Go to the source code of this file.](arch_2cache_8h_source.md)

| Macros | |
| --- | --- |
| #define | [cache\_data\_enable](group__cache__arch__interface.md#gaec0a2a0374c2c1fe0496f97a5e4a4456)   [arch\_dcache\_enable](group__cache__arch__interface.md#gaf616ce5134f8fd3a0fe0f690069915ce) |
| #define | [cache\_data\_disable](group__cache__arch__interface.md#gaf8e5056056c5609a8fd878f1b3aeaf5a)   [arch\_dcache\_disable](group__cache__arch__interface.md#ga01f917f9125a5fb38d9ec4b256630a80) |
| #define | [cache\_data\_flush\_all](group__cache__arch__interface.md#gae799dfd86b078f74bdeba952aa2eed92)   [arch\_dcache\_flush\_all](group__cache__arch__interface.md#ga9ec6cbe750133540d8f0460bfb8ca9d4) |
| #define | [cache\_data\_invd\_all](group__cache__arch__interface.md#gaade1db95fda43b875985d765f0aeee58)   [arch\_dcache\_invd\_all](group__cache__arch__interface.md#gacd9eed889dacd5dd42dab15b2dcc4097) |
| #define | [cache\_data\_flush\_and\_invd\_all](group__cache__arch__interface.md#gab48cc0cdaf4c6ec64748cb1d4ed51baa)   [arch\_dcache\_flush\_and\_invd\_all](group__cache__arch__interface.md#gac58493d5f3726d7e4131c48e9a6c75f9) |
| #define | [cache\_data\_flush\_range](group__cache__arch__interface.md#gab433cc69a23c0543376615336e80205b)(addr, size) |
| #define | [cache\_data\_invd\_range](group__cache__arch__interface.md#ga91e01cff6a459d21d97cd451ad63a29f)(addr, size) |
| #define | [cache\_data\_flush\_and\_invd\_range](group__cache__arch__interface.md#ga3d5443b3c6f83840c39bc177256ec24f)(addr, size) |
| #define | [cache\_data\_line\_size\_get](group__cache__arch__interface.md#gafdf1e8c95982a1fe5f39139d0fc6ab25)   [arch\_dcache\_line\_size\_get](group__cache__arch__interface.md#ga559156a12e712c641ca62dab7433e93e) |
| #define | [cache\_instr\_enable](group__cache__arch__interface.md#ga5f51912f5dba3e361e5849c4989d8260)   [arch\_icache\_enable](group__cache__arch__interface.md#gadb5dec5f9597565f597ba5592a330050) |
| #define | [cache\_instr\_disable](group__cache__arch__interface.md#ga287ead9fa07e9c13ba803a1fc3335479)   [arch\_icache\_disable](group__cache__arch__interface.md#ga03c14fd66267240460b0a37d72a3a971) |
| #define | [cache\_instr\_flush\_all](group__cache__arch__interface.md#ga3d02e8f383c9b15354c14274bf9daee8)   [arch\_icache\_flush\_all](group__cache__arch__interface.md#ga29fd1d9d9ba54306e00b6b3a393446a7) |
| #define | [cache\_instr\_invd\_all](group__cache__arch__interface.md#ga1f4241624e3879e8b43556d65867be22)   [arch\_icache\_invd\_all](group__cache__arch__interface.md#ga2bfbf102e413fc8af43f1fd15a79a093) |
| #define | [cache\_instr\_flush\_and\_invd\_all](group__cache__arch__interface.md#ga585fe4e3511d01af2585c439d722e828)   [arch\_icache\_flush\_and\_invd\_all](group__cache__arch__interface.md#ga29ae28d6e04ea0b136bcba5e461a7d6d) |
| #define | [cache\_instr\_flush\_range](group__cache__arch__interface.md#ga909eb6d67a146c97ffebd91a08419479)(addr, size) |
| #define | [cache\_instr\_invd\_range](group__cache__arch__interface.md#ga4f334ddb832d247041b95a177a426cb9)(addr, size) |
| #define | [cache\_instr\_flush\_and\_invd\_range](group__cache__arch__interface.md#ga96f1d12e5c52ed4063662cd8853f400c)(addr, size) |
| #define | [cache\_instr\_line\_size\_get](group__cache__arch__interface.md#gaf80d88e95d4eb6ab63301a5dee5a37fe)   [arch\_icache\_line\_size\_get](group__cache__arch__interface.md#ga717d37451103b7680bb54044d6ab1841) |
| #define | [cache\_is\_ptr\_cached](group__cache__arch__interface.md#gab3c3dd74ba3eb870fafe27a82ae6fa69)(ptr) |
| #define | [cache\_is\_ptr\_uncached](group__cache__arch__interface.md#ga3444529ef90c2a4de948967fe8cb48b7)(ptr) |
| #define | [cache\_cached\_ptr](group__cache__arch__interface.md#ga27e186c66d70ec25b665e0e88124a52a)(ptr) |
| #define | [cache\_uncached\_ptr](group__cache__arch__interface.md#ga11eb33eddf161352f5bbac9a4d6aed90)(ptr) |

| Functions | |
| --- | --- |
| void | [arch\_dcache\_enable](group__cache__arch__interface.md#gaf616ce5134f8fd3a0fe0f690069915ce) (void) |
|  | Enable the d-cache. |
| void | [arch\_dcache\_disable](group__cache__arch__interface.md#ga01f917f9125a5fb38d9ec4b256630a80) (void) |
|  | Disable the d-cache. |
| int | [arch\_dcache\_flush\_all](group__cache__arch__interface.md#ga9ec6cbe750133540d8f0460bfb8ca9d4) (void) |
|  | Flush the d-cache. |
| int | [arch\_dcache\_invd\_all](group__cache__arch__interface.md#gacd9eed889dacd5dd42dab15b2dcc4097) (void) |
|  | Invalidate the d-cache. |
| int | [arch\_dcache\_flush\_and\_invd\_all](group__cache__arch__interface.md#gac58493d5f3726d7e4131c48e9a6c75f9) (void) |
|  | Flush and Invalidate the d-cache. |
| int | [arch\_dcache\_flush\_range](group__cache__arch__interface.md#ga3a5b7426358790e7c54df7556bf2e6b8) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Flush an address range in the d-cache. |
| int | [arch\_dcache\_invd\_range](group__cache__arch__interface.md#ga1e12e643ba5855dd0cb67d2cc7fbb9ef) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Invalidate an address range in the d-cache. |
| int | [arch\_dcache\_flush\_and\_invd\_range](group__cache__arch__interface.md#gaf3afa0d36939f30a1995bf0755047122) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Flush and Invalidate an address range in the d-cache. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [arch\_dcache\_line\_size\_get](group__cache__arch__interface.md#ga559156a12e712c641ca62dab7433e93e) (void) |
|  | Get the d-cache line size. |
| void | [arch\_icache\_enable](group__cache__arch__interface.md#gadb5dec5f9597565f597ba5592a330050) (void) |
|  | Enable the i-cache. |
| void | [arch\_icache\_disable](group__cache__arch__interface.md#ga03c14fd66267240460b0a37d72a3a971) (void) |
|  | Disable the i-cache. |
| int | [arch\_icache\_flush\_all](group__cache__arch__interface.md#ga29fd1d9d9ba54306e00b6b3a393446a7) (void) |
|  | Flush the i-cache. |
| int | [arch\_icache\_invd\_all](group__cache__arch__interface.md#ga2bfbf102e413fc8af43f1fd15a79a093) (void) |
|  | Invalidate the i-cache. |
| int | [arch\_icache\_flush\_and\_invd\_all](group__cache__arch__interface.md#ga29ae28d6e04ea0b136bcba5e461a7d6d) (void) |
|  | Flush and Invalidate the i-cache. |
| int | [arch\_icache\_flush\_range](group__cache__arch__interface.md#ga7f6af61969ce97179f60ec483803500b) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Flush an address range in the i-cache. |
| int | [arch\_icache\_invd\_range](group__cache__arch__interface.md#ga84e877997349df3e53eed11be6fc3caa) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Invalidate an address range in the i-cache. |
| int | [arch\_icache\_flush\_and\_invd\_range](group__cache__arch__interface.md#gaa6caab419ca57523db54eb9125e7e1d0) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Flush and Invalidate an address range in the i-cache. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [arch\_icache\_line\_size\_get](group__cache__arch__interface.md#ga717d37451103b7680bb54044d6ab1841) (void) |
|  | Get the i-cache line size. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_cache\_is\_ptr\_cached](group__cache__arch__interface.md#ga9ed1c303508eb68db80f14fdb6eb7faa) (void \*ptr) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_cache\_is\_ptr\_uncached](group__cache__arch__interface.md#gab6bdf8089dce42e4463f761bae56e652) (void \*ptr) |
| void \* | [arch\_cache\_cached\_ptr\_get](group__cache__arch__interface.md#gabb31cd28a68b529ec0d7c389bb65bd9c) (void \*ptr) |
| void \* | [arch\_cache\_uncached\_ptr\_get](group__cache__arch__interface.md#ga1b507969ecccdaf7e47b16ba190bf816) (void \*ptr) |

## Detailed Description

Public APIs for architectural cache controller drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [cache.h](arch_2cache_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
