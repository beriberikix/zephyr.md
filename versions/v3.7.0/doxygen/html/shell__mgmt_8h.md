---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/shell__mgmt_8h.html
original_path: doxygen/html/shell__mgmt_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_mgmt.h File Reference

[Go to the source code of this file.](shell__mgmt_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SHELL\_MGMT\_ID\_EXEC](#a5b360507490dd79996c59bb51b0bb791)   0 |
|  | Command IDs for shell management group. |

| Enumerations | |
| --- | --- |
| enum | [shell\_mgmt\_err\_code\_t](#ac37bf991450de1611ae54fd671b61581) { [SHELL\_MGMT\_ERR\_OK](#ac37bf991450de1611ae54fd671b61581a461f818c3dc3aee4423d6bb94108ed51) = 0 , [SHELL\_MGMT\_ERR\_UNKNOWN](#ac37bf991450de1611ae54fd671b61581a2e103a732de87c555b1e4ad5eccceb02) , [SHELL\_MGMT\_ERR\_COMMAND\_TOO\_LONG](#ac37bf991450de1611ae54fd671b61581a0086ab17e2685dc66e44704c6cd19205) , [SHELL\_MGMT\_ERR\_EMPTY\_COMMAND](#ac37bf991450de1611ae54fd671b61581a0ccd61db1c1f552a01d77128a4a75881) } |
|  | Command result codes for shell management group. [More...](#ac37bf991450de1611ae54fd671b61581) |

## Macro Definition Documentation

## [◆ ](#a5b360507490dd79996c59bb51b0bb791)SHELL\_MGMT\_ID\_EXEC

| #define SHELL\_MGMT\_ID\_EXEC   0 |
| --- |

Command IDs for shell management group.

## Enumeration Type Documentation

## [◆ ](#ac37bf991450de1611ae54fd671b61581)shell\_mgmt\_err\_code\_t

| enum [shell\_mgmt\_err\_code\_t](#ac37bf991450de1611ae54fd671b61581) |
| --- |

Command result codes for shell management group.

| Enumerator | |
| --- | --- |
| SHELL\_MGMT\_ERR\_OK | No error, this is implied if there is no ret value in the response. |
| SHELL\_MGMT\_ERR\_UNKNOWN | Unknown error occurred. |
| SHELL\_MGMT\_ERR\_COMMAND\_TOO\_LONG | The provided command to execute is too long. |
| SHELL\_MGMT\_ERR\_EMPTY\_COMMAND | No command to execute was provided. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [shell\_mgmt](dir_5e8382db16a4734888c451bd3831b770.md)
- [shell\_mgmt.h](shell__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
