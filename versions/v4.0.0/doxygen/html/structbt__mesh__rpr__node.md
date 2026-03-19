---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__rpr__node.html
original_path: doxygen/html/structbt__mesh__rpr__node.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_rpr\_node Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Remote Provisioning models](group__bt__mesh__rpr.md)

Remote provisioning actor, as seen across the mesh.
[More...](#details)

`#include <[rpr.h](rpr_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [addr](#a10ec7b9c480513e742566c6c3b9c4973) |
|  | Unicast address of the node. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_idx](#a2197a70aa97209a60136a09da1f513b2) |
|  | Network index used when communicating with the node. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ttl](#a4a73478764d4d15642475b8a822130af) |
|  | Time To Live value used when communicating with the node. |

## Detailed Description

Remote provisioning actor, as seen across the mesh.

## Field Documentation

## [◆ ](#a10ec7b9c480513e742566c6c3b9c4973)addr

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_rpr\_node::addr |
| --- |

Unicast address of the node.

## [◆ ](#a2197a70aa97209a60136a09da1f513b2)net\_idx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_rpr\_node::net\_idx |
| --- |

Network index used when communicating with the node.

## [◆ ](#a4a73478764d4d15642475b8a822130af)ttl

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_rpr\_node::ttl |
| --- |

Time To Live value used when communicating with the node.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[rpr.h](rpr_8h_source.md)

- [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
