---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bt__mesh__brg__cfg__srv.html
original_path: doxygen/html/group__bt__mesh__brg__cfg__srv.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bridge Configuration Server Model

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

API for the Bluetooth Mesh Bridge Configuration Server model.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_BRG\_CFG\_SRV](#ga54e0629a3ae842e7c57a69f2cdab98e3) |
|  | Bridge Configuration Server model Composition Data entry. |

## Detailed Description

API for the Bluetooth Mesh Bridge Configuration Server model.

## Macro Definition Documentation

## [◆ ](#ga54e0629a3ae842e7c57a69f2cdab98e3)BT\_MESH\_MODEL\_BRG\_CFG\_SRV

| #define BT\_MESH\_MODEL\_BRG\_CFG\_SRV |
| --- |

`#include <[brg_cfg_srv.h](brg__cfg__srv_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)([BT\_MESH\_MODEL\_ID\_BRG\_CFG\_SRV](group__bt__mesh__access.md#ga599d00e9d63ade6ed1a6803579c1e16e), \_bt\_mesh\_brg\_cfg\_srv\_op, NULL, NULL, \

&\_bt\_mesh\_brg\_cfg\_srv\_cb)

[BT\_MESH\_MODEL\_ID\_BRG\_CFG\_SRV](group__bt__mesh__access.md#ga599d00e9d63ade6ed1a6803579c1e16e)

#define BT\_MESH\_MODEL\_ID\_BRG\_CFG\_SRV

Bridge Configuration Sever.

**Definition** access.h:191

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)

#define BT\_MESH\_MODEL\_CB(\_id, \_op, \_pub, \_user\_data, \_cb)

Composition data SIG model entry with callback functions.

**Definition** access.h:495

Bridge Configuration Server model Composition Data entry.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
