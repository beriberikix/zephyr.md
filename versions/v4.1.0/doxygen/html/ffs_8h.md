---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ffs_8h.html
original_path: doxygen/html/ffs_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ffs.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](ffs_8h_source.md)

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [find\_msb\_set](#a088db7d02e8f1fc559cbe1ec048494e8) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) op) |
|  | find most significant bit set in a 32-bit word |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [find\_lsb\_set](#a860b01217c1d5eb5f416272c3b719113) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) op) |
|  | find least significant bit set in a 32-bit word |

## Function Documentation

## [◆ ](#a860b01217c1d5eb5f416272c3b719113)find\_lsb\_set()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int find\_lsb\_set | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *op* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

find least significant bit set in a 32-bit word

This routine finds the first bit set starting from the least significant bit in the argument passed in and returns the index of that bit. Bits are numbered starting at 1 from the least significant bit. A return value of zero indicates that the value passed is zero.

Returns
:   least significant bit set, 0 if *op* is 0

## [◆ ](#a088db7d02e8f1fc559cbe1ec048494e8)find\_msb\_set()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int find\_msb\_set | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *op* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

find most significant bit set in a 32-bit word

This routine finds the first bit set starting from the most significant bit in the argument passed in and returns the index of that bit. Bits are numbered starting at 1 from the least significant bit. A return value of zero indicates that the value passed is zero.

Returns
:   most significant bit set, 0 if *op* is 0

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [common](dir_7cbd25c8850fe30be392200e83a608be.md)
- [ffs.h](ffs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
