---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arch_2riscv_2atomic_8h.html
original_path: doxygen/html/arch_2riscv_2atomic_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

atomic.h File Reference

[Go to the source code of this file.](arch_2riscv_2atomic_8h_source.md)

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_swap](#ad7b411811c56512edd93b23c5aa5a503) (const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) newval) |
|  | Copyright (c) 2024 NextSilicon SPDX-License-Identifier: Apache-2.0. |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_max](#aebee55ea9e302b35ddb4555c726c8482) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_min](#a9fdddd559afa2918ad69fafe91782df1) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [atomic\_maxu](#a51405da00fee2c1f894bab41e9c62386) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*target, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long value) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [atomic\_minu](#af165e862d4fd1219838fd209fab3ef7c) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*target, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long value) |

## Function Documentation

## [◆ ](#aebee55ea9e302b35ddb4555c726c8482)atomic\_max()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_max | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a51405da00fee2c1f894bab41e9c62386)atomic\_maxu()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long atomic\_maxu | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \* | *target*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *value* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a9fdddd559afa2918ad69fafe91782df1)atomic\_min()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_min | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#af165e862d4fd1219838fd209fab3ef7c)atomic\_minu()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long atomic\_minu | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \* | *target*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *value* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ad7b411811c56512edd93b23c5aa5a503)atomic\_swap()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_swap | ( | const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *newval* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Copyright (c) 2024 NextSilicon SPDX-License-Identifier: Apache-2.0.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [atomic.h](arch_2riscv_2atomic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
