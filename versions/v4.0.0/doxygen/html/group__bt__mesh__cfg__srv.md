---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bt__mesh__cfg__srv.html
original_path: doxygen/html/group__bt__mesh__cfg__srv.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Configuration Server Model

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

Configuration Server Model.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_CFG\_SRV](#gafc6b9dea9f72d5754c1a4b42bfafd656) |
|  | Generic Configuration Server model composition data entry. |

## Detailed Description

Configuration Server Model.

## Macro Definition Documentation

## [◆ ](#gafc6b9dea9f72d5754c1a4b42bfafd656)BT\_MESH\_MODEL\_CFG\_SRV

| #define BT\_MESH\_MODEL\_CFG\_SRV |
| --- |

`#include <[cfg_srv.h](cfg__srv_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_CNT\_CB](group__bt__mesh__access.md#ga925da443eb15a4c1980d48a69388dc2c)([BT\_MESH\_MODEL\_ID\_CFG\_SRV](group__bt__mesh__access.md#ga004d8d1be55b2aec56abbeeca1d118d8), \

bt\_mesh\_cfg\_srv\_op, NULL, \

NULL, 1, 0, &bt\_mesh\_cfg\_srv\_cb)

[BT\_MESH\_MODEL\_ID\_CFG\_SRV](group__bt__mesh__access.md#ga004d8d1be55b2aec56abbeeca1d118d8)

#define BT\_MESH\_MODEL\_ID\_CFG\_SRV

Configuration Server.

**Definition** access.h:179

[BT\_MESH\_MODEL\_CNT\_CB](group__bt__mesh__access.md#ga925da443eb15a4c1980d48a69388dc2c)

#define BT\_MESH\_MODEL\_CNT\_CB(\_id, \_op, \_pub, \_user\_data, \_keys, \_grps, \_cb)

Composition data SIG model entry with callback functions with specific number of keys & groups.

**Definition** access.h:436

Generic Configuration Server model composition data entry.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
