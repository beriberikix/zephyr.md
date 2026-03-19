---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__brg__cfg__cli.html
original_path: doxygen/html/structbt__mesh__brg__cfg__cli.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_brg\_cfg\_cli Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bridge Configuration Client Model](group__bt__mesh__brg__cfg__cli.md)

Bridge Configuration Client Model Context.
[More...](#details)

`#include <[brg_cfg_cli.h](brg__cfg__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | [model](#a6cbc5bb1a79c9951b4cd2f16e06d1beb) |
|  | Bridge Configuration model entry pointer. |
| const struct [bt\_mesh\_brg\_cfg\_cli\_cb](structbt__mesh__brg__cfg__cli__cb.md) \* | [cb](#a5a7b181b3d026de617085efc0c671474) |
|  | Event handler callbacks. |
| struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) | [ack\_ctx](#ac0f982fa211bb6660a3159f7e796abb7) |

## Detailed Description

Bridge Configuration Client Model Context.

## Field Documentation

## [◆ ](#ac0f982fa211bb6660a3159f7e796abb7)ack\_ctx

| struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) bt\_mesh\_brg\_cfg\_cli::ack\_ctx |
| --- |

## [◆ ](#a5a7b181b3d026de617085efc0c671474)cb

| const struct [bt\_mesh\_brg\_cfg\_cli\_cb](structbt__mesh__brg__cfg__cli__cb.md)\* bt\_mesh\_brg\_cfg\_cli::cb |
| --- |

Event handler callbacks.

## [◆ ](#a6cbc5bb1a79c9951b4cd2f16e06d1beb)model

| const struct [bt\_mesh\_model](structbt__mesh__model.md)\* bt\_mesh\_brg\_cfg\_cli::model |
| --- |

Bridge Configuration model entry pointer.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[brg\_cfg\_cli.h](brg__cfg__cli_8h_source.md)

- [bt\_mesh\_brg\_cfg\_cli](structbt__mesh__brg__cfg__cli.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
