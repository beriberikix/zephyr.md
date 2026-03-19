---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/armv8__timer_8h.html
original_path: doxygen/html/armv8__timer_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

armv8\_timer.h File Reference

`#include <[zephyr/drivers/timer/arm_arch_timer.h](arm__arch__timer_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](armv8__timer_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ARM\_ARCH\_TIMER\_IRQ](#a6740222458f89442f50b688bfa69797f)   [ARM\_TIMER\_VIRTUAL\_IRQ](arm__arch__timer_8h.md#a22468e93135e790458d9c2bfd493c070) |
| #define | [ARM\_ARCH\_TIMER\_PRIO](#a319716e35b4e65c8480c0b90624a7899)   [ARM\_TIMER\_VIRTUAL\_PRIO](arm__arch__timer_8h.md#acafac307be9d89ff4ebb72ab23c75ac6) |
| #define | [ARM\_ARCH\_TIMER\_FLAGS](#a2ab15e3403580f8986b7c7391f0fbbd2)   [ARM\_TIMER\_VIRTUAL\_FLAGS](arm__arch__timer_8h.md#a373af60653667562ca2ca950c45e4b20) |

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [arm\_arch\_timer\_init](#ada947e26d82e5ee70218ecde101eb85f) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [arm\_arch\_timer\_set\_compare](#ac2bf0a61b818c6d27eea31611471ed55) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [arm\_arch\_timer\_enable](#acbb90cd040cb2ada7562aa68c386861e) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char enable) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [arm\_arch\_timer\_set\_irq\_mask](#a5969eb25741240dd0030acb92018038c) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mask) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [arm\_arch\_timer\_count](#a27c012fc420c6dab58e101b565bc1ed1) (void) |

## Macro Definition Documentation

## [◆ ](#a2ab15e3403580f8986b7c7391f0fbbd2)ARM\_ARCH\_TIMER\_FLAGS

| #define ARM\_ARCH\_TIMER\_FLAGS   [ARM\_TIMER\_VIRTUAL\_FLAGS](arm__arch__timer_8h.md#a373af60653667562ca2ca950c45e4b20) |
| --- |

## [◆ ](#a6740222458f89442f50b688bfa69797f)ARM\_ARCH\_TIMER\_IRQ

| #define ARM\_ARCH\_TIMER\_IRQ   [ARM\_TIMER\_VIRTUAL\_IRQ](arm__arch__timer_8h.md#a22468e93135e790458d9c2bfd493c070) |
| --- |

## [◆ ](#a319716e35b4e65c8480c0b90624a7899)ARM\_ARCH\_TIMER\_PRIO

| #define ARM\_ARCH\_TIMER\_PRIO   [ARM\_TIMER\_VIRTUAL\_PRIO](arm__arch__timer_8h.md#acafac307be9d89ff4ebb72ab23c75ac6) |
| --- |

## Function Documentation

## [◆ ](#a27c012fc420c6dab58e101b565bc1ed1)arm\_arch\_timer\_count()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arm\_arch\_timer\_count | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#acbb90cd040cb2ada7562aa68c386861e)arm\_arch\_timer\_enable()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void arm\_arch\_timer\_enable | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char | *enable* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ada947e26d82e5ee70218ecde101eb85f)arm\_arch\_timer\_init()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void arm\_arch\_timer\_init | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ac2bf0a61b818c6d27eea31611471ed55)arm\_arch\_timer\_set\_compare()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void arm\_arch\_timer\_set\_compare | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a5969eb25741240dd0030acb92018038c)arm\_arch\_timer\_set\_irq\_mask()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void arm\_arch\_timer\_set\_irq\_mask | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *mask* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [cortex\_a\_r](dir_cde462911e3dbfe61dba09f2df37ee97.md)
- [armv8\_timer.h](armv8__timer_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
