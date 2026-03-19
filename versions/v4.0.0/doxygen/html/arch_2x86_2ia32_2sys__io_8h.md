---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2x86_2ia32_2sys__io_8h.html
original_path: doxygen/html/arch_2x86_2ia32_2sys__io_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sys\_io.h File Reference

`#include <[zephyr/sys/sys_io.h](sys_2sys__io_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <stddef.h>`

[Go to the source code of this file.](arch_2x86_2ia32_2sys__io_8h_source.md)

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_io\_set\_bit](#ab74f07a31f01e5866d397e91b012abf7) ([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int bit) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_io\_clear\_bit](#a6a6ece8db6858d64378c6cce47a64238) ([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int bit) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_io\_test\_bit](#a1593f7afecfc05001fc47d1d75ee895d) ([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int bit) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_io\_test\_and\_set\_bit](#a070e38b330fc6402de5aae6192abd41b) ([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int bit) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_io\_test\_and\_clear\_bit](#a41953bee114b3317cd7bcdfbad4738b9) ([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int bit) |

## Function Documentation

## [◆ ](#a6a6ece8db6858d64378c6cce47a64238)sys\_io\_clear\_bit()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void sys\_io\_clear\_bit | ( | [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) | *port*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *bit* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ab74f07a31f01e5866d397e91b012abf7)sys\_io\_set\_bit()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void sys\_io\_set\_bit | ( | [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) | *port*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *bit* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a41953bee114b3317cd7bcdfbad4738b9)sys\_io\_test\_and\_clear\_bit()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int sys\_io\_test\_and\_clear\_bit | ( | [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) | *port*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *bit* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a070e38b330fc6402de5aae6192abd41b)sys\_io\_test\_and\_set\_bit()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int sys\_io\_test\_and\_set\_bit | ( | [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) | *port*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *bit* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a1593f7afecfc05001fc47d1d75ee895d)sys\_io\_test\_bit()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int sys\_io\_test\_bit | ( | [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) | *port*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *bit* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [ia32](dir_b429dacf948f53b894465a48d17dcb95.md)
- [sys\_io.h](arch_2x86_2ia32_2sys__io_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
