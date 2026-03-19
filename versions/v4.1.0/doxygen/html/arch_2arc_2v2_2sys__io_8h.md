---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arch_2arc_2v2_2sys__io_8h.html
original_path: doxygen/html/arch_2arc_2v2_2sys__io_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sys\_io.h File Reference

`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/sys/sys_io.h](sys_2sys__io_8h_source.md)>`  
`#include <[zephyr/arch/arc/v2/aux_regs.h](aux__regs_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <stddef.h>`

[Go to the source code of this file.](arch_2arc_2v2_2sys__io_8h_source.md)

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_out8](#a4eb1822b6af401aef41646d01f900733) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data, [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sys\_in8](#a38e2ce31ef09cb5d903da6f0fbd7b174) ([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_out16](#a8700f40b9c9951083b9a729b7e50f47d) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data, [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sys\_in16](#ab9823ccf71d78cbb0316e9c335081f6d) ([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_out32](#ae60822b265f38b57b70a2925996aaa88) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data, [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_in32](#af89948c04bd432f5fa14319f29d06968) ([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_io\_set\_bit](#ab74f07a31f01e5866d397e91b012abf7) ([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int bit) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_io\_clear\_bit](#a6a6ece8db6858d64378c6cce47a64238) ([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int bit) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_io\_test\_bit](#a1593f7afecfc05001fc47d1d75ee895d) ([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int bit) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_io\_test\_and\_set\_bit](#a070e38b330fc6402de5aae6192abd41b) ([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int bit) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_io\_test\_and\_clear\_bit](#a41953bee114b3317cd7bcdfbad4738b9) ([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int bit) |

## Function Documentation

## [◆ ](#ab9823ccf71d78cbb0316e9c335081f6d)sys\_in16()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sys\_in16 | ( | [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) | *port* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#af89948c04bd432f5fa14319f29d06968)sys\_in32()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_in32 | ( | [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) | *port* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a38e2ce31ef09cb5d903da6f0fbd7b174)sys\_in8()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sys\_in8 | ( | [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) | *port* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

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

## [◆ ](#a8700f40b9c9951083b9a729b7e50f47d)sys\_out16()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void sys\_out16 | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *data*, | | --- | --- | --- | --- | |  |  | [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) | *port* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ae60822b265f38b57b70a2925996aaa88)sys\_out32()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void sys\_out32 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *data*, | | --- | --- | --- | --- | |  |  | [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) | *port* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a4eb1822b6af401aef41646d01f900733)sys\_out8()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void sys\_out8 | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *data*, | | --- | --- | --- | --- | |  |  | [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) | *port* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [sys\_io.h](arch_2arc_2v2_2sys__io_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
