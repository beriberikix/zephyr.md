---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__mesh__priv__beacon__srv.html
original_path: doxygen/html/group__bt__mesh__priv__beacon__srv.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bluetooth Mesh Private Beacon Server

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_PRIV\_BEACON\_SRV](#gac2e5a8847c2abf94feddfc78d0589dc2) |
|  | Private Beacon Server model composition data entry. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gac2e5a8847c2abf94feddfc78d0589dc2)BT\_MESH\_MODEL\_PRIV\_BEACON\_SRV

| #define BT\_MESH\_MODEL\_PRIV\_BEACON\_SRV |
| --- |

`#include <[priv_beacon_srv.h](priv__beacon__srv_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)([BT\_MESH\_MODEL\_ID\_PRIV\_BEACON\_SRV](group__bt__mesh__access.md#gacca0e355982935cfbde46a06b09a7bec), \

bt\_mesh\_priv\_beacon\_srv\_op, NULL, NULL, \

&bt\_mesh\_priv\_beacon\_srv\_cb)

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)

#define BT\_MESH\_MODEL\_CB(\_id, \_op, \_pub, \_user\_data, \_cb)

Composition data SIG model entry with callback functions.

**Definition** access.h:491

[BT\_MESH\_MODEL\_ID\_PRIV\_BEACON\_SRV](group__bt__mesh__access.md#gacca0e355982935cfbde46a06b09a7bec)

#define BT\_MESH\_MODEL\_ID\_PRIV\_BEACON\_SRV

Private Beacon Server.

**Definition** access.h:191

Private Beacon Server model composition data entry.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
