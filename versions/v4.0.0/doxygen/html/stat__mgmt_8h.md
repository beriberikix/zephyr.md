---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stat__mgmt_8h.html
original_path: doxygen/html/stat__mgmt_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stat\_mgmt.h File Reference

[Go to the source code of this file.](stat__mgmt_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [stat\_mgmt\_entry](structstat__mgmt__entry.md) |
|  | Represents a single value in a statistics group. [More...](structstat__mgmt__entry.md#details) |

| Macros | |
| --- | --- |
| #define | [STAT\_MGMT\_ID\_SHOW](#a155235d2c21b5a698d833ca468d9473e)   0 |
|  | Command IDs for statistics management group. |
| #define | [STAT\_MGMT\_ID\_LIST](#aed49473584422e0270f2f06e0ee0c330)   1 |

| Enumerations | |
| --- | --- |
| enum | [stat\_mgmt\_err\_code\_t](#a9144a5e8c384093e47603a15b3d1ff69) {     [STAT\_MGMT\_ERR\_OK](#a9144a5e8c384093e47603a15b3d1ff69a8aa83ae8d80615f2789bc788dd260577) = 0 , [STAT\_MGMT\_ERR\_UNKNOWN](#a9144a5e8c384093e47603a15b3d1ff69aba909444504e8d93eafc8b29a171bc82) , [STAT\_MGMT\_ERR\_INVALID\_GROUP](#a9144a5e8c384093e47603a15b3d1ff69a1bff1f2f9b3f7d1a7ca09e80c4665710) , [STAT\_MGMT\_ERR\_INVALID\_STAT\_NAME](#a9144a5e8c384093e47603a15b3d1ff69a58b33ada336c88be45f3321dde52b52e) ,     [STAT\_MGMT\_ERR\_INVALID\_STAT\_SIZE](#a9144a5e8c384093e47603a15b3d1ff69ad6158abd9117931ece95a74473282b58) , [STAT\_MGMT\_ERR\_WALK\_ABORTED](#a9144a5e8c384093e47603a15b3d1ff69a7e1dc898fd0e6ace7dafd47ed766e833)   } |
|  | Command result codes for statistics management group. [More...](#a9144a5e8c384093e47603a15b3d1ff69) |

## Macro Definition Documentation

## [◆ ](#aed49473584422e0270f2f06e0ee0c330)STAT\_MGMT\_ID\_LIST

| #define STAT\_MGMT\_ID\_LIST   1 |
| --- |

## [◆ ](#a155235d2c21b5a698d833ca468d9473e)STAT\_MGMT\_ID\_SHOW

| #define STAT\_MGMT\_ID\_SHOW   0 |
| --- |

Command IDs for statistics management group.

## Enumeration Type Documentation

## [◆ ](#a9144a5e8c384093e47603a15b3d1ff69)stat\_mgmt\_err\_code\_t

| enum [stat\_mgmt\_err\_code\_t](#a9144a5e8c384093e47603a15b3d1ff69) |
| --- |

Command result codes for statistics management group.

| Enumerator | |
| --- | --- |
| STAT\_MGMT\_ERR\_OK | No error, this is implied if there is no ret value in the response. |
| STAT\_MGMT\_ERR\_UNKNOWN | Unknown error occurred. |
| STAT\_MGMT\_ERR\_INVALID\_GROUP | The provided statistic group name was not found. |
| STAT\_MGMT\_ERR\_INVALID\_STAT\_NAME | The provided statistic name was not found. |
| STAT\_MGMT\_ERR\_INVALID\_STAT\_SIZE | The size of the statistic cannot be handled. |
| STAT\_MGMT\_ERR\_WALK\_ABORTED | Walk through of statistics was aborted. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [stat\_mgmt](dir_02a570021bf1e49be869a1f46be4c519.md)
- [stat\_mgmt.h](stat__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
