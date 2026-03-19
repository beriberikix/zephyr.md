---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bt__mesh__brg__cfg.html
original_path: doxygen/html/group__bt__mesh__brg__cfg.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bridge Configuration common header

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_brg\_cfg\_table\_entry](structbt__mesh__brg__cfg__table__entry.md) |
|  | Bridging Table state entry corresponding to a entry in the Bridging Table. [More...](structbt__mesh__brg__cfg__table__entry.md#details) |
| struct | [bt\_mesh\_brg\_cfg\_table\_status](structbt__mesh__brg__cfg__table__status.md) |
|  | Bridging Table Status response. [More...](structbt__mesh__brg__cfg__table__status.md#details) |
| struct | [bt\_mesh\_brg\_cfg\_filter\_netkey](structbt__mesh__brg__cfg__filter__netkey.md) |
|  | Used to filter set of pairs of NetKey Indexes from the Bridging Table. [More...](structbt__mesh__brg__cfg__filter__netkey.md#details) |
| struct | [bt\_mesh\_brg\_cfg\_subnets\_list](structbt__mesh__brg__cfg__subnets__list.md) |
|  | Bridged Subnets List response. [More...](structbt__mesh__brg__cfg__subnets__list.md#details) |
| struct | [bt\_mesh\_brg\_cfg\_table\_list](structbt__mesh__brg__cfg__table__list.md) |
|  | Bridging Table List response. [More...](structbt__mesh__brg__cfg__table__list.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_BRG\_CFG\_DIR\_ONEWAY](#ga054c4efc3fbe9ee7f05020b8c93129ed)   1 |
| #define | [BT\_MESH\_BRG\_CFG\_DIR\_TWOWAY](#ga7787b27b46160aa0943c4c70a4b8ab4b)   2 |

| Enumerations | |
| --- | --- |
| enum | [bt\_mesh\_brg\_cfg\_state](#ga7bddcbe2b1196df6a1c80d8c213866f9) { [BT\_MESH\_BRG\_CFG\_DISABLED](#gga7bddcbe2b1196df6a1c80d8c213866f9a20b2a18d76793d0efabeb9e7e47a3dc4) , [BT\_MESH\_BRG\_CFG\_ENABLED](#gga7bddcbe2b1196df6a1c80d8c213866f9ab719036dc7e16001a14a5054331fa9b2) } |
|  | Subnet Bridge states. [More...](#ga7bddcbe2b1196df6a1c80d8c213866f9) |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga054c4efc3fbe9ee7f05020b8c93129ed)BT\_MESH\_BRG\_CFG\_DIR\_ONEWAY

| #define BT\_MESH\_BRG\_CFG\_DIR\_ONEWAY   1 |
| --- |

`#include <[brg_cfg.h](brg__cfg_8h.md)>`

## [◆ ](#ga7787b27b46160aa0943c4c70a4b8ab4b)BT\_MESH\_BRG\_CFG\_DIR\_TWOWAY

| #define BT\_MESH\_BRG\_CFG\_DIR\_TWOWAY   2 |
| --- |

`#include <[brg_cfg.h](brg__cfg_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#ga7bddcbe2b1196df6a1c80d8c213866f9)bt\_mesh\_brg\_cfg\_state

| enum [bt\_mesh\_brg\_cfg\_state](#ga7bddcbe2b1196df6a1c80d8c213866f9) |
| --- |

`#include <[brg_cfg.h](brg__cfg_8h.md)>`

Subnet Bridge states.

| Enumerator | |
| --- | --- |
| BT\_MESH\_BRG\_CFG\_DISABLED | Subnet bridge functionality is disabled. |
| BT\_MESH\_BRG\_CFG\_ENABLED | Subnet bridge state functionality is enabled. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
