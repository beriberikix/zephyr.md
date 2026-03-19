---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/unistd_8h.html
original_path: doxygen/html/unistd_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

unistd.h File Reference

`#include <[zephyr/posix/posix_types.h](posix__types_8h_source.md)>`  
`#include <[zephyr/posix/sys/confstr.h](confstr_8h_source.md)>`  
`#include <[zephyr/posix/sys/stat.h](stat_8h_source.md)>`  
`#include <[zephyr/posix/sys/sysconf.h](sysconf_8h_source.md)>`  
`#include "[posix_features.h](posix__features_8h_source.md)"`

[Go to the source code of this file.](unistd_8h_source.md)

| Functions | |
| --- | --- |
| int | [getentropy](#a5d88641f86c8a447fefd1e531758a3c0) (void \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
| [pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) | [getpid](#ac61b207337ca21b3b309593fd1a0cb82) (void) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) | [sleep](#aaa1de6debea33c41fbfaa909e813c2f4) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int seconds) |
| int | [usleep](#a59715f1a0a2ee4dc75e8343aca15c1dd) ([useconds\_t](posix__types_8h.md#a1cf3c794977f92f3ccf2e041a68f3342) useconds) |
| long | [sysconf](#a599f55d9eaa01b6921367233437b9b13) (int opt) |

## Function Documentation

## [◆ ](#a5d88641f86c8a447fefd1e531758a3c0)getentropy()

| int getentropy | ( | void \* | *buffer*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *length* ) |

## [◆ ](#ac61b207337ca21b3b309593fd1a0cb82)getpid()

| [pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) getpid | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#aaa1de6debea33c41fbfaa909e813c2f4)sleep()

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) sleep | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *seconds* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a599f55d9eaa01b6921367233437b9b13)sysconf()

| long sysconf | ( | int | *opt* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a59715f1a0a2ee4dc75e8343aca15c1dd)usleep()

| int usleep | ( | [useconds\_t](posix__types_8h.md#a1cf3c794977f92f3ccf2e041a68f3342) | *useconds* | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [unistd.h](unistd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
