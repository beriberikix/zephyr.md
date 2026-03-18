---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arc__dsp_8h.html
original_path: doxygen/html/arc__dsp_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arc\_dsp.h File Reference

[Go to the source code of this file.](arc__dsp_8h_source.md)

| Functions | |
| --- | --- |
| void | [arc\_dsp\_disable](#a119f6c3700a75e14f3d49f38725b93d7) (struct [k\_thread](structk__thread.md) \*thread, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int options) |
|  | Disable dsp context preservation. |
| void | [arc\_dsp\_enable](#a29fddbd6fdaad797481c6c4010e85046) (struct [k\_thread](structk__thread.md) \*thread, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int options) |
|  | Enable dsp context preservation. |

## Function Documentation

## [◆ ](#a119f6c3700a75e14f3d49f38725b93d7)arc\_dsp\_disable()

| void arc\_dsp\_disable | ( | struct [k\_thread](structk__thread.md) \* | *thread*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *options* ) |

Disable dsp context preservation.

The function is used to disable the preservation of dsp and agu context registers for a particular thread.

The *options* parameter indicates which register sets will not be used by the specified thread. It is used by ARC only.

Parameters
:   | thread | ID of thread. |
    | --- | --- |
    | options | register sets options |

## [◆ ](#a29fddbd6fdaad797481c6c4010e85046)arc\_dsp\_enable()

| void arc\_dsp\_enable | ( | struct [k\_thread](structk__thread.md) \* | *thread*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *options* ) |

Enable dsp context preservation.

The function is used to enable the preservation of dsp and agu context registers for a particular thread.

The *options* parameter indicates which register sets will be used by the specified thread. It is used by ARC only.

Parameters
:   | thread | ID of thread. |
    | --- | --- |
    | options | register sets options |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [dsp](dir_962e9c2a9ba605ed4f0852828f7b1083.md)
- [arc\_dsp.h](arc__dsp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
