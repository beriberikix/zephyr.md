---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arc__vpx_8h.html
original_path: doxygen/html/arc__vpx_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arc\_vpx.h File Reference

`#include <[zephyr/sys_clock.h](sys__clock_8h_source.md)>`

[Go to the source code of this file.](arc__vpx_8h_source.md)

| Functions | |
| --- | --- |
| int | [arc\_vpx\_lock](#a97f5476f56ce69acf4a0d169c6a78ba6) ([k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Obtain a cooperative lock on the VPX vector registers. |
| void | [arc\_vpx\_unlock](#a40a9dcc39bc184cb1a5aca5b8e7ad3ad) (void) |
|  | Release cooperative lock on the VPX vector registers. |
| void | [arc\_vpx\_unlock\_force](#aae826e8f1a2ce10b8183798633da8a20) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int cpu\_id) |
|  | Release cooperative lock on a CPU's VPX vector registers. |

## Function Documentation

## [◆ ](#a97f5476f56ce69acf4a0d169c6a78ba6)arc\_vpx\_lock()

| int arc\_vpx\_lock | ( | [k\_timeout\_t](structk__timeout__t.md) | *timeout* | ) |  |
| --- | --- | --- | --- | --- | --- |

Obtain a cooperative lock on the VPX vector registers.

This function is used to obtain a cooperative lock on the current CPU's VPX vector registers before the calling thread uses them. Callers attempting to obtain the cooperative lock must be already restricted to executing on a single CPU, and continue to execute on that same CPU while both waiting and holding the lock.

This routine is not callable from an ISR.

Parameters
:   | timeout | Waiting period to obtain the lock, or one of the special values K\_NO\_WAIT and K\_FOREVER. |
    | --- | --- |

Returns
:   Zero on success, otherwise error code

## [◆ ](#a40a9dcc39bc184cb1a5aca5b8e7ad3ad)arc\_vpx\_unlock()

| void arc\_vpx\_unlock | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Release cooperative lock on the VPX vector registers.

This function is used to release the cooperative lock on the current CPU's VPX vector registers. It is called after the current thread no longer needs to use the VPX vector registers, thereby allowing another thread to use them.

This routine is not callable from an ISR.

## [◆ ](#aae826e8f1a2ce10b8183798633da8a20)arc\_vpx\_unlock\_force()

| void arc\_vpx\_unlock\_force | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *cpu\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

Release cooperative lock on a CPU's VPX vector registers.

This function is used to release the cooperative lock on the specified CPU's VPX vector registers. This routine should not be used except by a system monitor to release the cooperative lock in case the locking thread where it is known that the locking thread is unable to release it (e.g. it was aborted while holding the lock).

Parameters
:   | cpu\_id | CPU ID of the VPX vector register set to be unlocked |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [vpx](dir_163ac165fb52f03f9d4ffcae544ed3b1.md)
- [arc\_vpx.h](arc__vpx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
