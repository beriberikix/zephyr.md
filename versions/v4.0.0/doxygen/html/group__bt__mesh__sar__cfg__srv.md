---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bt__mesh__sar__cfg__srv.html
original_path: doxygen/html/group__bt__mesh__sar__cfg__srv.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bluetooth Mesh SAR Configuration Server Model

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

Bluetooth Mesh.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_SAR\_CFG\_SRV](#gaddb9214dd96ad476aac4f9a8947dfd45) |
|  | Transport SAR Configuration Server model composition data entry. |

## Detailed Description

Bluetooth Mesh.

## Macro Definition Documentation

## [◆ ](#gaddb9214dd96ad476aac4f9a8947dfd45)BT\_MESH\_MODEL\_SAR\_CFG\_SRV

| #define BT\_MESH\_MODEL\_SAR\_CFG\_SRV |
| --- |

`#include <[sar_cfg_srv.h](sar__cfg__srv_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)([BT\_MESH\_MODEL\_ID\_SAR\_CFG\_SRV](group__bt__mesh__access.md#ga1e9d8be1d2e65d2977aea0306b015258), bt\_mesh\_sar\_cfg\_srv\_op, \

NULL, NULL, &bt\_mesh\_sar\_cfg\_srv\_cb)

[BT\_MESH\_MODEL\_ID\_SAR\_CFG\_SRV](group__bt__mesh__access.md#ga1e9d8be1d2e65d2977aea0306b015258)

#define BT\_MESH\_MODEL\_ID\_SAR\_CFG\_SRV

SAR Configuration Server.

**Definition** access.h:199

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)

#define BT\_MESH\_MODEL\_CB(\_id, \_op, \_pub, \_user\_data, \_cb)

Composition data SIG model entry with callback functions.

**Definition** access.h:495

Transport SAR Configuration Server model composition data entry.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
