---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/syscall_8h.html
original_path: doxygen/html/syscall_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

syscall.h File Reference

`#include <zephyr/syscall_list.h>`  
`#include <[zephyr/arch/syscall.h](arch_2syscall_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/linker/sections.h](sections_8h_source.md)>`

[Go to the source code of this file.](syscall_8h_source.md)

| Functions | |
| --- | --- |
| static \_\_pinned\_func [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_is\_user\_context](#acd625881dd1a23de2573fa86d870df20) (void) |
|  | Indicate whether the CPU is currently in user mode. |

## Function Documentation

## [◆ ](#acd625881dd1a23de2573fa86d870df20)k\_is\_user\_context()

| | \_\_pinned\_func [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) k\_is\_user\_context | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Indicate whether the CPU is currently in user mode.

Returns
:   true if the CPU is currently running with user permissions

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [syscall.h](syscall_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
