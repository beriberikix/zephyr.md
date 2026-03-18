---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/fdtable_8h.html
original_path: doxygen/html/fdtable_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fdtable.h File Reference

`#include <stdarg.h>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/fs/fs.h](fs_8h_source.md)>`  
`#include <[zephyr/sys/mutex.h](mutex_8h_source.md)>`

[Go to the source code of this file.](fdtable_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [fd\_op\_vtable](structfd__op__vtable.md) |
|  | File descriptor virtual method table. [More...](structfd__op__vtable.md#details) |

| Enumerations | |
| --- | --- |
| enum | {     [ZFD\_IOCTL\_FSYNC](#aac8cb8bde69d227a7a8e9edf2980bd20a50a53736aa4724d43363b8b0b1986ca4) = 0x100 , [ZFD\_IOCTL\_LSEEK](#aac8cb8bde69d227a7a8e9edf2980bd20a5b7369d570c761ce85e6bd50a17eb072) , [ZFD\_IOCTL\_POLL\_PREPARE](#aac8cb8bde69d227a7a8e9edf2980bd20a41846852df9ee3d5dba7b0051e94945e) , [ZFD\_IOCTL\_POLL\_UPDATE](#aac8cb8bde69d227a7a8e9edf2980bd20a9e7250eac0c568051f35ab086b560eaa) ,     [ZFD\_IOCTL\_POLL\_OFFLOAD](#aac8cb8bde69d227a7a8e9edf2980bd20a901693ab4461b170c2da08c7518ddbbe) , [ZFD\_IOCTL\_SET\_LOCK](#aac8cb8bde69d227a7a8e9edf2980bd20a2920c62c09c574b21a58a6cf98017b62) , [ZFD\_IOCTL\_FIONREAD](#aac8cb8bde69d227a7a8e9edf2980bd20a34b26658321074989ee1db15aab5f683) = 0x541B , [ZFD\_IOCTL\_FIONBIO](#aac8cb8bde69d227a7a8e9edf2980bd20a7c70aef3ad6110cbdfa3bd4f843ec530) = 0x5421   } |
|  | Request codes for [fd\_op\_vtable.ioctl()](structfd__op__vtable.md#aff079f05422413a0df3394ddfecc0298). [More...](#aac8cb8bde69d227a7a8e9edf2980bd20) |

## Enumeration Type Documentation

## [◆ ](#aac8cb8bde69d227a7a8e9edf2980bd20)anonymous enum

| anonymous enum |
| --- |

Request codes for [fd\_op\_vtable.ioctl()](structfd__op__vtable.md#aff079f05422413a0df3394ddfecc0298).

Note that these codes are internal Zephyr numbers, for internal Zephyr operations (and subject to change without notice, not part of "stable ABI"). These are however expected to co-exist with "well-known" POSIX/Linux ioctl numbers, and not clash with them.

| Enumerator | |
| --- | --- |
| ZFD\_IOCTL\_FSYNC |  |
| ZFD\_IOCTL\_LSEEK |  |
| ZFD\_IOCTL\_POLL\_PREPARE |  |
| ZFD\_IOCTL\_POLL\_UPDATE |  |
| ZFD\_IOCTL\_POLL\_OFFLOAD |  |
| ZFD\_IOCTL\_SET\_LOCK |  |
| ZFD\_IOCTL\_FIONREAD |  |
| ZFD\_IOCTL\_FIONBIO |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [fdtable.h](fdtable_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
