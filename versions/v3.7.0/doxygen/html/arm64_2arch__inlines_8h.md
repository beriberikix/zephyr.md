---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arm64_2arch__inlines_8h.html
original_path: doxygen/html/arm64_2arch__inlines_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch\_inlines.h File Reference

`#include <[zephyr/kernel_structs.h](kernel__structs_8h_source.md)>`  
`#include <[zephyr/arch/arm64/lib_helpers.h](4_2lib__helpers_8h_source.md)>`  
`#include <[zephyr/arch/arm64/tpidrro_el0.h](tpidrro__el0_8h_source.md)>`  
`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`

[Go to the source code of this file.](arm64_2arch__inlines_8h_source.md)

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) \_cpu\_t \* | [arch\_curr\_cpu](#a3e8a7515c0c3b8de5a037ce5997c73b0) (void) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [arch\_exception\_depth](#a39935d470a4190bae6e3063b4524e599) (void) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [arch\_proc\_id](#a4bf4475c062f66961e183d17fd4c22d3) (void) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arch\_num\_cpus](#a83c8ae933b0ec7d067569f17125c6a2c) (void) |

## Function Documentation

## [◆ ](#a3e8a7515c0c3b8de5a037ce5997c73b0)arch\_curr\_cpu()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) \_cpu\_t \* arch\_curr\_cpu | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a39935d470a4190bae6e3063b4524e599)arch\_exception\_depth()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int arch\_exception\_depth | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a83c8ae933b0ec7d067569f17125c6a2c)arch\_num\_cpus()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_num\_cpus | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a4bf4475c062f66961e183d17fd4c22d3)arch\_proc\_id()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_proc\_id | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [arch\_inlines.h](arm64_2arch__inlines_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
