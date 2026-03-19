---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ioctl_8h.html
original_path: doxygen/html/ioctl_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ioctl.h File Reference

`#include <[zephyr/sys/fdtable.h](fdtable_8h_source.md)>`

[Go to the source code of this file.](ioctl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [FIONBIO](#af48a6e38eb0ae226621514b44b9844eb)   [ZFD\_IOCTL\_FIONBIO](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a7c70aef3ad6110cbdfa3bd4f843ec530) |
| #define | [FIONREAD](#ac68826c621a12d91544dab200c86c75a)   [ZFD\_IOCTL\_FIONREAD](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a34b26658321074989ee1db15aab5f683) |

| Functions | |
| --- | --- |
| int | [ioctl](#a1487536105f7a596481bf6bfa8de99f6) (int fd, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long request,...) |

## Macro Definition Documentation

## [◆ ](#af48a6e38eb0ae226621514b44b9844eb)FIONBIO

| #define FIONBIO   [ZFD\_IOCTL\_FIONBIO](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a7c70aef3ad6110cbdfa3bd4f843ec530) |
| --- |

## [◆ ](#ac68826c621a12d91544dab200c86c75a)FIONREAD

| #define FIONREAD   [ZFD\_IOCTL\_FIONREAD](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a34b26658321074989ee1db15aab5f683) |
| --- |

## Function Documentation

## [◆ ](#a1487536105f7a596481bf6bfa8de99f6)ioctl()

| int ioctl | ( | int | *fd*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *request*, |
|  |  |  | *...* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [ioctl.h](ioctl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
