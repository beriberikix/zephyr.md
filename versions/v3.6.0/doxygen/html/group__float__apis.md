---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__float__apis.html
original_path: doxygen/html/group__float__apis.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Floating Point APIs

[Kernel APIs](group__kernel__apis.md)

| Functions | |
| --- | --- |
| int | [k\_float\_disable](#ga2df4b2550ace30512cddebd36b6a54a1) (struct [k\_thread](structk__thread.md) \*thread) |
|  | Disable preservation of floating point context information. |
| int | [k\_float\_enable](#ga81fb955ddd41658a9aad5c083f173f77) (struct [k\_thread](structk__thread.md) \*thread, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int options) |
|  | Enable preservation of floating point context information. |

## Detailed Description

## Function Documentation

## [◆ ](#ga2df4b2550ace30512cddebd36b6a54a1)k\_float\_disable()

| int k\_float\_disable | ( | struct [k\_thread](structk__thread.md) \* | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Disable preservation of floating point context information.

This routine informs the kernel that the specified thread will no longer be using the floating point registers.

Warning
:   Some architectures apply restrictions on how the disabling of floating point preservation may be requested, see arch\_float\_disable.
:   This routine should only be used to disable floating point support for a thread that currently has such support enabled.

Parameters
:   | thread | ID of thread. |
    | --- | --- |

Return values
:   | 0 | On success. |
    | --- | --- |
    | -ENOTSUP | If the floating point disabling is not implemented. -EINVAL If the floating point disabling could not be performed. |

## [◆ ](#ga81fb955ddd41658a9aad5c083f173f77)k\_float\_enable()

| int k\_float\_enable | ( | struct [k\_thread](structk__thread.md) \* | *thread*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *options* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Enable preservation of floating point context information.

This routine informs the kernel that the specified thread will use the floating point registers.

Invoking this routine initializes the thread's floating point context info to that of an FPU that has been reset. The next time the thread is scheduled by z\_swap() it will either inherit an FPU that is guaranteed to be in a "sane" state (if the most recent user of the FPU was cooperatively swapped out) or the thread's own floating point context will be loaded (if the most recent user of the FPU was preempted, or if this thread is the first user of the FPU). Thereafter, the kernel will protect the thread's FP context so that it is not altered during a preemptive context switch.

The *options* parameter indicates which floating point register sets will be used by the specified thread.

For x86 options:

- K\_FP\_REGS indicates x87 FPU and MMX registers only
- K\_SSE\_REGS indicates SSE registers (and also x87 FPU and MMX registers)

Warning
:   Some architectures apply restrictions on how the enabling of floating point preservation may be requested, see arch\_float\_enable.
:   This routine should only be used to enable floating point support for a thread that currently has such support enabled.

Parameters
:   | thread | ID of thread. |
    | --- | --- |
    | options | architecture dependent options |

Return values
:   | 0 | On success. |
    | --- | --- |
    | -ENOTSUP | If the floating point enabling is not implemented. -EINVAL If the floating point enabling could not be performed. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
