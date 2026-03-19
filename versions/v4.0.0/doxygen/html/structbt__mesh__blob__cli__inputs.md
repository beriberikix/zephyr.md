---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__blob__cli__inputs.html
original_path: doxygen/html/structbt__mesh__blob__cli__inputs.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_blob\_cli\_inputs Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh BLOB Transfer Client model API](group__bt__mesh__blob__cli.md)

BLOB Transfer Client transfer inputs.
[More...](#details)

`#include <[blob_cli.h](blob__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) | [targets](#a835a539b307c659f57da6c20e9223ed1) |
|  | Linked list of Target nodes. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [app\_idx](#a7fb308f895c57b66b50e1ab060228cb3) |
|  | AppKey index to send with. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [group](#ac204e179c2a6ea9cb672fc3c2f9ab017) |
|  | Group address destination for the BLOB transfer, or [BT\_MESH\_ADDR\_UNASSIGNED](group__bt__mesh__access.md#ga6d11790af686e6d48f08c6f1cd65317c "BT_MESH_ADDR_UNASSIGNED") to send every message to each Target node individually. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ttl](#adee5ecdba3adc4fe598483b1a160cafb) |
|  | Time to live value of BLOB transfer messages. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [timeout\_base](#a30fd3cd7a6df07f6aa90b85cdc6aea18) |
|  | Additional response time for the Target nodes, in 10-second increments. |

## Detailed Description

BLOB Transfer Client transfer inputs.

## Field Documentation

## [◆ ](#a7fb308f895c57b66b50e1ab060228cb3)app\_idx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_blob\_cli\_inputs::app\_idx |
| --- |

AppKey index to send with.

## [◆ ](#ac204e179c2a6ea9cb672fc3c2f9ab017)group

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_blob\_cli\_inputs::group |
| --- |

Group address destination for the BLOB transfer, or [BT\_MESH\_ADDR\_UNASSIGNED](group__bt__mesh__access.md#ga6d11790af686e6d48f08c6f1cd65317c "BT_MESH_ADDR_UNASSIGNED") to send every message to each Target node individually.

## [◆ ](#a835a539b307c659f57da6c20e9223ed1)targets

| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) bt\_mesh\_blob\_cli\_inputs::targets |
| --- |

Linked list of Target nodes.

Each node should point to [bt\_mesh\_blob\_target::n](structbt__mesh__blob__target.md#aca0f3cabb5c457cfb11a4bc71c3bea85 "bt_mesh_blob_target::n").

## [◆ ](#a30fd3cd7a6df07f6aa90b85cdc6aea18)timeout\_base

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_blob\_cli\_inputs::timeout\_base |
| --- |

Additional response time for the Target nodes, in 10-second increments.

The extra time can be used to give the Target nodes more time to respond to messages from the Client. The actual timeout will be calculated according to the following formula:

```
*  timeout = 20 seconds + (10 seconds * timeout_base) + (100 ms * TTL)
*
```

If a Target node fails to respond to a message from the Client within the configured transfer timeout, the Target node is dropped.

## [◆ ](#adee5ecdba3adc4fe598483b1a160cafb)ttl

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_blob\_cli\_inputs::ttl |
| --- |

Time to live value of BLOB transfer messages.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[blob\_cli.h](blob__cli_8h_source.md)

- [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
