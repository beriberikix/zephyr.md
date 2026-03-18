---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/if_8h.html
original_path: doxygen/html/if_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

if.h File Reference

[Go to the source code of this file.](if_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [if\_nameindex](structif__nameindex.md) |

| Macros | |
| --- | --- |
| #define | [IF\_NAMESIZE](#aedb93bcce9682d7644080b859849f59d)   1 |

| Functions | |
| --- | --- |
| char \* | [if\_indextoname](#a4da7243450c66298378e0f2d6434b997) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int ifindex, char \*ifname) |
| void | [if\_freenameindex](#a4349b1231de2572765f6b3771e6023f1) (struct [if\_nameindex](structif__nameindex.md) \*ptr) |
| struct if\_nameindex \* | [if\_nameindex](#aadc0427486b1b97fa250760e8ccd4f7f) (void) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [if\_nametoindex](#aabacc3c49f072845092730128fbadd93) (const char \*ifname) |

## Macro Definition Documentation

## [◆ ](#aedb93bcce9682d7644080b859849f59d)IF\_NAMESIZE

| #define IF\_NAMESIZE   1 |
| --- |

## Function Documentation

## [◆ ](#a4349b1231de2572765f6b3771e6023f1)if\_freenameindex()

| void if\_freenameindex | ( | struct [if\_nameindex](structif__nameindex.md) \* | *ptr* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a4da7243450c66298378e0f2d6434b997)if\_indextoname()

| char \* if\_indextoname | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *ifindex*, |
| --- | --- | --- | --- |
|  |  | char \* | *ifname* ) |

## [◆ ](#aadc0427486b1b97fa250760e8ccd4f7f)if\_nameindex()

| struct if\_nameindex \* if\_nameindex | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#aabacc3c49f072845092730128fbadd93)if\_nametoindex()

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int if\_nametoindex | ( | const char \* | *ifname* | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [net](dir_2c168081a5287170970afe4d92a99d1b.md)
- [if.h](if_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
