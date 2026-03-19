---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__mesh__op__agg__srv.html
original_path: doxygen/html/group__bt__mesh__op__agg__srv.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Opcodes Aggregator Server model

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_OP\_AGG\_SRV](#ga9729e918d83a5b86e2fb1d443d23558a) |
|  | Opcodes Aggretator Server model composition data entry. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga9729e918d83a5b86e2fb1d443d23558a)BT\_MESH\_MODEL\_OP\_AGG\_SRV

| #define BT\_MESH\_MODEL\_OP\_AGG\_SRV |
| --- |

`#include <[op_agg_srv.h](op__agg__srv_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)([BT\_MESH\_MODEL\_ID\_OP\_AGG\_SRV](group__bt__mesh__access.md#ga5cf2bb09e5eaa299cfc6b7fe4ed66e9a), \_bt\_mesh\_op\_agg\_srv\_op, \

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), &\_bt\_mesh\_op\_agg\_srv\_cb)

[BT\_MESH\_MODEL\_ID\_OP\_AGG\_SRV](group__bt__mesh__access.md#ga5cf2bb09e5eaa299cfc6b7fe4ed66e9a)

#define BT\_MESH\_MODEL\_ID\_OP\_AGG\_SRV

Opcodes Aggregator Server.

**Definition** access.h:203

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)

#define BT\_MESH\_MODEL\_CB(\_id, \_op, \_pub, \_user\_data, \_cb)

Composition data SIG model entry with callback functions.

**Definition** access.h:495

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

Opcodes Aggretator Server model composition data entry.

Note
:   The Opcodes Aggregator Server handles aggregated messages and dispatches them to the respective models and their message handlers. Current implementation assumes that responses are sent from the same execution context as the received message and doesn't allow to send a postponed response, e.g. from workqueue.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
