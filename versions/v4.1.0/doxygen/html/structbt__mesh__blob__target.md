---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__mesh__blob__target.html
original_path: doxygen/html/structbt__mesh__blob__target.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_blob\_target Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh BLOB Transfer Client model API](group__bt__mesh__blob__cli.md)

BLOB Transfer Client Target node.
[More...](#details)

`#include <[blob_cli.h](blob__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [n](#aca0f3cabb5c457cfb11a4bc71c3bea85) |
|  | Linked list node. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [addr](#ab4c032f92a4ec12e4bbd6fa84139c085) |
|  | Target node address. |
| struct [bt\_mesh\_blob\_target\_pull](structbt__mesh__blob__target__pull.md) \* | [pull](#a0498f23d640af4b006398d5482fbaa53) |
|  | Target node's Pull mode context. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [status](#a62b5a5be44d52ebf09421de57933459d) |
|  | BLOB transfer status, see [bt\_mesh\_blob\_status](group__bt__mesh__blob.md#ga7b5e2895a6577103a8a680a94ee7776d "bt_mesh_blob_status"). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [procedure\_complete](#a711a031e841bb54c4985d02a81c6846a):1 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [acked](#a4eef4809023e8d4a4ee8beece5e83160):1 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [timedout](#a3e14f4518ee054754dfa50d8070c1725):1 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [skip](#a7aa1066dbeee5ba4a5be5aa14d61d4d1):1 |

## Detailed Description

BLOB Transfer Client Target node.

## Field Documentation

## [◆ ](#a4eef4809023e8d4a4ee8beece5e83160)acked

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_blob\_target::acked |
| --- |

## [◆ ](#ab4c032f92a4ec12e4bbd6fa84139c085)addr

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_blob\_target::addr |
| --- |

Target node address.

## [◆ ](#aca0f3cabb5c457cfb11a4bc71c3bea85)n

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) bt\_mesh\_blob\_target::n |
| --- |

Linked list node.

## [◆ ](#a711a031e841bb54c4985d02a81c6846a)procedure\_complete

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_blob\_target::procedure\_complete |
| --- |

## [◆ ](#a0498f23d640af4b006398d5482fbaa53)pull

| struct [bt\_mesh\_blob\_target\_pull](structbt__mesh__blob__target__pull.md)\* bt\_mesh\_blob\_target::pull |
| --- |

Target node's Pull mode context.

Needs to be initialized when sending a BLOB in Pull mode.

## [◆ ](#a7aa1066dbeee5ba4a5be5aa14d61d4d1)skip

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_blob\_target::skip |
| --- |

## [◆ ](#a62b5a5be44d52ebf09421de57933459d)status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_blob\_target::status |
| --- |

BLOB transfer status, see [bt\_mesh\_blob\_status](group__bt__mesh__blob.md#ga7b5e2895a6577103a8a680a94ee7776d "bt_mesh_blob_status").

## [◆ ](#a3e14f4518ee054754dfa50d8070c1725)timedout

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_blob\_target::timedout |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[blob\_cli.h](blob__cli_8h_source.md)

- [bt\_mesh\_blob\_target](structbt__mesh__blob__target.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
