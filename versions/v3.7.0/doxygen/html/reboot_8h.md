---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/reboot_8h.html
original_path: doxygen/html/reboot_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

reboot.h File Reference

Common target reboot functionality.
[More...](#details)

`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`

[Go to the source code of this file.](reboot_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SYS\_REBOOT\_WARM](#a956528997e1fa2cf52f3795b95dcc01b)   0 |
| #define | [SYS\_REBOOT\_COLD](#aa2589ee8e2e252dedeee80ec0f58ed15)   1 |

| Functions | |
| --- | --- |
| FUNC\_NORETURN void | [sys\_reboot](#a18abe5d5b8089e8429c25bafa5e76d3d) (int type) |
|  | Reboot the system. |

## Detailed Description

Common target reboot functionality.

See subsys/os/Kconfig and the reboot help for details.

## Macro Definition Documentation

## [◆ ](#aa2589ee8e2e252dedeee80ec0f58ed15)SYS\_REBOOT\_COLD

| #define SYS\_REBOOT\_COLD   1 |
| --- |

## [◆ ](#a956528997e1fa2cf52f3795b95dcc01b)SYS\_REBOOT\_WARM

| #define SYS\_REBOOT\_WARM   0 |
| --- |

## Function Documentation

## [◆ ](#a18abe5d5b8089e8429c25bafa5e76d3d)sys\_reboot()

| FUNC\_NORETURN void sys\_reboot | ( | int | *type* | ) |  |
| --- | --- | --- | --- | --- | --- |

Reboot the system.

Reboot the system in the manner specified by *type*. Not all architectures or platforms support the various reboot types (SYS\_REBOOT\_COLD, SYS\_REBOOT\_WARM).

When successful, this routine does not return.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [reboot.h](reboot_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
