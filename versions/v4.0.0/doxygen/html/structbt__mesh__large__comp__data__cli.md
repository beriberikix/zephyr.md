---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__large__comp__data__cli.html
original_path: doxygen/html/structbt__mesh__large__comp__data__cli.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_large\_comp\_data\_cli Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Large Composition Data Client model](group__bt__mesh__large__comp__data__cli.md)

Large Composition Data Client model context.
[More...](#details)

`#include <[large_comp_data_cli.h](large__comp__data__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | [model](#a4401ff19edfe69c018dd0dbb6f81dc0d) |
|  | Model entry pointer. |
| struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) | [ack\_ctx](#afec070cb549d56b3900c4df1e14656ed) |
|  | Internal parameters for tracking message responses. |
| const struct [bt\_mesh\_large\_comp\_data\_cli\_cb](structbt__mesh__large__comp__data__cli__cb.md) \* | [cb](#a39d9086c8d9803f939c6103e613699b1) |
|  | Optional callback for Large Composition Data Status messages. |

## Detailed Description

Large Composition Data Client model context.

## Field Documentation

## [◆ ](#afec070cb549d56b3900c4df1e14656ed)ack\_ctx

| struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) bt\_mesh\_large\_comp\_data\_cli::ack\_ctx |
| --- |

Internal parameters for tracking message responses.

## [◆ ](#a39d9086c8d9803f939c6103e613699b1)cb

| const struct [bt\_mesh\_large\_comp\_data\_cli\_cb](structbt__mesh__large__comp__data__cli__cb.md)\* bt\_mesh\_large\_comp\_data\_cli::cb |
| --- |

Optional callback for Large Composition Data Status messages.

## [◆ ](#a4401ff19edfe69c018dd0dbb6f81dc0d)model

| const struct [bt\_mesh\_model](structbt__mesh__model.md)\* bt\_mesh\_large\_comp\_data\_cli::model |
| --- |

Model entry pointer.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[large\_comp\_data\_cli.h](large__comp__data__cli_8h_source.md)

- [bt\_mesh\_large\_comp\_data\_cli](structbt__mesh__large__comp__data__cli.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
