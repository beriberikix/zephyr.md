---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__cfg__cli.html
original_path: doxygen/html/structbt__mesh__cfg__cli.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_cfg\_cli Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Configuration Client Model](group__bt__mesh__cfg__cli.md)

Mesh Configuration Client Model Context.
[More...](#details)

`#include <[cfg_cli.h](cfg__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | [model](#a525dd5391c83c525c012940575245cea) |
|  | Composition data model entry pointer. |
| const struct [bt\_mesh\_cfg\_cli\_cb](structbt__mesh__cfg__cli__cb.md) \* | [cb](#a7160cf5d22fa0b909482bbc76f27b6bd) |
|  | Optional callback for Mesh Configuration Client Status messages. |
| struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) | [ack\_ctx](#a472bf5015857ab97e1a40ab6cfa70bb1) |

## Detailed Description

Mesh Configuration Client Model Context.

## Field Documentation

## [◆ ](#a472bf5015857ab97e1a40ab6cfa70bb1)ack\_ctx

| struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) bt\_mesh\_cfg\_cli::ack\_ctx |
| --- |

## [◆ ](#a7160cf5d22fa0b909482bbc76f27b6bd)cb

| const struct [bt\_mesh\_cfg\_cli\_cb](structbt__mesh__cfg__cli__cb.md)\* bt\_mesh\_cfg\_cli::cb |
| --- |

Optional callback for Mesh Configuration Client Status messages.

## [◆ ](#a525dd5391c83c525c012940575245cea)model

| const struct [bt\_mesh\_model](structbt__mesh__model.md)\* bt\_mesh\_cfg\_cli::model |
| --- |

Composition data model entry pointer.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[cfg\_cli.h](cfg__cli_8h_source.md)

- [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
