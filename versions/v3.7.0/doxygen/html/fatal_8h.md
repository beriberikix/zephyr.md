---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/fatal_8h.html
original_path: doxygen/html/fatal_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fatal.h File Reference

Fatal error functions.
[More...](#details)

`#include <[zephyr/arch/cpu.h](cpu_8h_source.md)>`  
`#include <[zephyr/arch/exception.h](exception_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/fatal_types.h](fatal__types_8h_source.md)>`

[Go to the source code of this file.](fatal_8h_source.md)

| Functions | |
| --- | --- |
| FUNC\_NORETURN void | [k\_fatal\_halt](group__fatal__apis.md#gaa8c0b43a2360e5319d7910e8e0ceb951) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reason) |
|  | Halt the system on a fatal error. |
| void | [k\_sys\_fatal\_error\_handler](group__fatal__apis.md#ga255cc816d227f0a5c0e80e61bfba11fa) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reason, const struct [arch\_esf](structarch__esf.md) \*esf) |
|  | Fatal error policy handler. |

## Detailed Description

Fatal error functions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [fatal.h](fatal_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
