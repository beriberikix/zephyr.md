---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmgmt__group.html
original_path: doxygen/html/structmgmt__group.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mgmt\_group Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr mgmt API](group__mcumgr__mgmt__api.md)

A collection of handlers for an entire command group.
[More...](#details)

`#include <[mgmt.h](mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#ac150809b03f73c4c2f94742504af772c) |
|  | Entry list node. |
| const struct [mgmt\_handler](structmgmt__handler.md) \* | [mg\_handlers](#a7a6e90e500716095b9a22e3f56edac03) |
|  | Array of handlers; one entry per command ID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [mg\_handlers\_count](#a8b2de48e97c0de4c902d72aba4e920b4) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [mg\_group\_id](#a9d55dbf947096eed7cacfb9087d304d4) |
|  | The numeric ID of this group. |

## Detailed Description

A collection of handlers for an entire command group.

## Field Documentation

## [◆ ](#a9d55dbf947096eed7cacfb9087d304d4)mg\_group\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mgmt\_group::mg\_group\_id |
| --- |

The numeric ID of this group.

## [◆ ](#a7a6e90e500716095b9a22e3f56edac03)mg\_handlers

| const struct [mgmt\_handler](structmgmt__handler.md)\* mgmt\_group::mg\_handlers |
| --- |

Array of handlers; one entry per command ID.

## [◆ ](#a8b2de48e97c0de4c902d72aba4e920b4)mg\_handlers\_count

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mgmt\_group::mg\_handlers\_count |
| --- |

## [◆ ](#ac150809b03f73c4c2f94742504af772c)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) mgmt\_group::node |
| --- |

Entry list node.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/mgmt/[mgmt.h](mgmt_8h_source.md)

- [mgmt\_group](structmgmt__group.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
