---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__mesh__rpr__srv.html
original_path: doxygen/html/group__bt__mesh__rpr__srv.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Remote provisioning server

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_RPR\_SRV](#ga49c08c3e98b0c3863dd79b37aea25b34) |
|  | Remote Provisioning Server model composition data entry. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga49c08c3e98b0c3863dd79b37aea25b34)BT\_MESH\_MODEL\_RPR\_SRV

| #define BT\_MESH\_MODEL\_RPR\_SRV |
| --- |

`#include <[rpr_srv.h](rpr__srv_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)([BT\_MESH\_MODEL\_ID\_REMOTE\_PROV\_SRV](group__bt__mesh__access.md#ga9c7d1c5dfb87a5ce50c08747af47414f), \

\_bt\_mesh\_rpr\_srv\_op, NULL, NULL, \

&\_bt\_mesh\_rpr\_srv\_cb)

[BT\_MESH\_MODEL\_ID\_REMOTE\_PROV\_SRV](group__bt__mesh__access.md#ga9c7d1c5dfb87a5ce50c08747af47414f)

#define BT\_MESH\_MODEL\_ID\_REMOTE\_PROV\_SRV

Remote Provisioning Server.

**Definition** access.h:187

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)

#define BT\_MESH\_MODEL\_CB(\_id, \_op, \_pub, \_user\_data, \_cb)

Composition data SIG model entry with callback functions.

**Definition** access.h:491

Remote Provisioning Server model composition data entry.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
