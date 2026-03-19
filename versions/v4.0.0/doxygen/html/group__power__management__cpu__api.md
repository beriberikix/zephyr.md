---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__power__management__cpu__api.html
original_path: doxygen/html/group__power__management__cpu__api.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

CPU Power Management

[Operating System Services](group__os__services.md) » [Power Management (PM)](group__subsys__pm.md)

| Functions | |
| --- | --- |
| int | [pm\_cpu\_off](#gaa6de91e837b262f432b4a80ef5e2b781) (void) |
|  | Power down the calling core. |
| int | [pm\_cpu\_on](#ga68c37acfc53eee990c34398ca0f1a3f5) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long cpuid, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) entry\_point) |
|  | Power up a core. |
| int | [pm\_system\_reset](#ga65dfe4b0c47af092c50c0022227ac8eb) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char reset) |
|  | System reset. |

## Detailed Description

## Function Documentation

## [◆ ](#gaa6de91e837b262f432b4a80ef5e2b781)pm\_cpu\_off()

| int pm\_cpu\_off | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pm_cpu_ops.h](pm__cpu__ops_8h.md)>`

Power down the calling core.

This call is intended for use in hotplug. A core that is powered down by cpu\_off can only be powered up again in response to a cpu\_on

Return values
:   | The | call does not return when successful |
    | --- | --- |
    | -ENOTSUP | If the operation is not supported |

## [◆ ](#ga68c37acfc53eee990c34398ca0f1a3f5)pm\_cpu\_on()

| int pm\_cpu\_on | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *cpuid*, |
| --- | --- | --- | --- |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *entry\_point* ) |

`#include <[pm_cpu_ops.h](pm__cpu__ops_8h.md)>`

Power up a core.

This call is used to power up cores that either have not yet been booted into the calling supervisory software or have been previously powered down with a cpu\_off call

Parameters
:   | cpuid | CPU id to power on |
    | --- | --- |
    | entry\_point | Address at which the core must commence execution |

Return values
:   | 0 | on success, a negative errno otherwise |
    | --- | --- |
    | -ENOTSUP | If the operation is not supported |

## [◆ ](#ga65dfe4b0c47af092c50c0022227ac8eb)pm\_system\_reset()

| int pm\_system\_reset | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char | *reset* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pm_cpu_ops.h](pm__cpu__ops_8h.md)>`

System reset.

This function provides a method for performing a system cold or warm reset.

Parameters
:   | reset | system reset type, cold or warm. |
    | --- | --- |

Return values
:   | 0 | on success, a negative errno otherwise |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
