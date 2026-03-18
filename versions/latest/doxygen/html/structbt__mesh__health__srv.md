---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__mesh__health__srv.html
original_path: doxygen/html/structbt__mesh__health__srv.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_health\_srv Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Health Server Model](group__bt__mesh__health__srv.md)

Mesh Health Server Model Context.
[More...](#details)

`#include <[health_srv.h](health__srv_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | [model](#aff95fc381ea8048d4d76668b92126dc6) |
|  | Composition data model entry pointer. |
| const struct [bt\_mesh\_health\_srv\_cb](structbt__mesh__health__srv__cb.md) \* | [cb](#a4d316010b2737eca7bad3aef6774d52b) |
|  | Optional callback struct. |
| struct [k\_work\_delayable](structk__work__delayable.md) | [attn\_timer](#a8df7f6c7e434cb717b9b51a3167b5e86) |
|  | Attention Timer state. |

## Detailed Description

Mesh Health Server Model Context.

## Field Documentation

## [◆ ](#a8df7f6c7e434cb717b9b51a3167b5e86)attn\_timer

| struct [k\_work\_delayable](structk__work__delayable.md) bt\_mesh\_health\_srv::attn\_timer |
| --- |

Attention Timer state.

## [◆ ](#a4d316010b2737eca7bad3aef6774d52b)cb

| const struct [bt\_mesh\_health\_srv\_cb](structbt__mesh__health__srv__cb.md)\* bt\_mesh\_health\_srv::cb |
| --- |

Optional callback struct.

## [◆ ](#aff95fc381ea8048d4d76668b92126dc6)model

| const struct [bt\_mesh\_model](structbt__mesh__model.md)\* bt\_mesh\_health\_srv::model |
| --- |

Composition data model entry pointer.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[health\_srv.h](health__srv_8h_source.md)

- [bt\_mesh\_health\_srv](structbt__mesh__health__srv.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
