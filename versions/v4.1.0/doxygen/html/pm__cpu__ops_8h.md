---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/pm__cpu__ops_8h.html
original_path: doxygen/html/pm__cpu__ops_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pm\_cpu\_ops.h File Reference

Public API for CPU Power Management.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](pm__cpu__ops_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SYS\_WARM\_RESET](#a98f079e56ab5b320bb52e1ebaa873d9b)   0 |
| #define | [SYS\_COLD\_RESET](#a92747266cafef3783fcfb550e08ce132)   1 |

| Functions | |
| --- | --- |
| int | [pm\_cpu\_off](group__power__management__cpu__api.md#gaa6de91e837b262f432b4a80ef5e2b781) (void) |
|  | Power down the calling core. |
| int | [pm\_cpu\_on](group__power__management__cpu__api.md#ga68c37acfc53eee990c34398ca0f1a3f5) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long cpuid, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) entry\_point) |
|  | Power up a core. |
| int | [pm\_system\_reset](group__power__management__cpu__api.md#ga65dfe4b0c47af092c50c0022227ac8eb) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char reset) |
|  | System reset. |

## Detailed Description

Public API for CPU Power Management.

## Macro Definition Documentation

## [◆ ](#a92747266cafef3783fcfb550e08ce132)SYS\_COLD\_RESET

| #define SYS\_COLD\_RESET   1 |
| --- |

## [◆ ](#a98f079e56ab5b320bb52e1ebaa873d9b)SYS\_WARM\_RESET

| #define SYS\_WARM\_RESET   0 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pm\_cpu\_ops.h](pm__cpu__ops_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
