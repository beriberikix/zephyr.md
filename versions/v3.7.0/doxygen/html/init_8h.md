---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/init_8h.html
original_path: doxygen/html/init_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

init.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`

[Go to the source code of this file.](init_8h_source.md)

| Data Structures | |
| --- | --- |
| union | [init\_function](unioninit__function.md) |
|  | Initialization function for init entries. [More...](unioninit__function.md#details) |
| struct | [init\_entry](structinit__entry.md) |
|  | Structure to store initialization entry information. [More...](structinit__entry.md#details) |

| Macros | |
| --- | --- |
| #define | [INIT\_LEVEL\_ORD](group__sys__init.md#ga3025b426a99f8351d4b483205f437e48)(level) |
|  | Obtain the ordinal for an init level. |
| #define | [SYS\_INIT](group__sys__init.md#gaf507cc0613add8113c41896bd631254f)(init\_fn, level, prio) |
|  | Register an initialization function. |
| #define | [SYS\_INIT\_NAMED](group__sys__init.md#gae862feb31eb4628b8ec95b471e5d4c54)(name, init\_fn\_, level, prio) |
|  | Register an initialization function (named). |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [init.h](init_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
