---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structmgmt__callback.html
original_path: doxygen/html/structmgmt__callback.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mgmt\_callback Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr callback API](group__mcumgr__callback__api.md)

MGMT callback struct.
[More...](#details)

`#include <[callbacks.h](callbacks_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a4595cb6a72ebf8b9396e63a8f31c497f) |
|  | Entry list node. |
| [mgmt\_cb](group__mcumgr__callback__api.md#gae61f705224a859776ee5161dfda5ed7d) | [callback](#acd79e73a2a3d44697bbda2b401d1e7df) |
|  | Callback that will be called. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [event\_id](#a3dc18e5f7e3e00c1c05cc104bb1f3ab1) |
|  | MGMT\_EVT\_[...] Event ID for handler to be called on. |

## Detailed Description

MGMT callback struct.

## Field Documentation

## [◆ ](#acd79e73a2a3d44697bbda2b401d1e7df)callback

| [mgmt\_cb](group__mcumgr__callback__api.md#gae61f705224a859776ee5161dfda5ed7d) mgmt\_callback::callback |
| --- |

Callback that will be called.

## [◆ ](#a3dc18e5f7e3e00c1c05cc104bb1f3ab1)event\_id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_callback::event\_id |
| --- |

MGMT\_EVT\_[...] Event ID for handler to be called on.

This has special meaning if [MGMT\_EVT\_OP\_ALL](group__mcumgr__callback__api.md#ggaab6470007be89e5aab88838456f9561aaf9e289ad5f7e0fd8bec581f67951813a "Used to enable all events.") is used (which will cover all events for all groups), or MGMT\_EVT\_OP\_\*\_MGMT\_ALL (which will cover all events for a single group). For events that are part of a single group, they can be or'd together for this to have one registration trigger on multiple events, please note that this will only work for a single group, to register for events in different groups, they must be registered separately.

## [◆ ](#a4595cb6a72ebf8b9396e63a8f31c497f)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) mgmt\_callback::node |
| --- |

Entry list node.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/mgmt/[callbacks.h](callbacks_8h_source.md)

- [mgmt\_callback](structmgmt__callback.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
