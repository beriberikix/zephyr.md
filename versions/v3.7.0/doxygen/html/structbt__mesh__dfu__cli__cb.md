---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__dfu__cli__cb.html
original_path: doxygen/html/structbt__mesh__dfu__cli__cb.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_dfu\_cli\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh Device Firmware Update](group__bt__mesh__dfu.md) » [Firmware Uppdate Client model](group__bt__mesh__dfu__cli.md)

Firmware Update Client event callbacks.
[More...](#details)

`#include <[dfu_cli.h](dfu__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [suspended](#ad2abfdf93f23cecd30e12241bb064a7f) )(struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli) |
|  | BLOB transfer is suspended. |
| void(\* | [ended](#aa3c8985490a6b2bd6fcd81dff0132060) )(struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli, enum [bt\_mesh\_dfu\_status](group__bt__mesh__dfu.md#ga9e627a3c15de782faa11ef6c4ec5e05d) reason) |
|  | DFU ended. |
| void(\* | [applied](#a6f580db9629d81f72c79d00a5aea2de4) )(struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli) |
|  | DFU transfer applied on all active Target nodes. |
| void(\* | [confirmed](#a32b20280b2196437bad6d85edc017c63) )(struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli) |
|  | DFU transfer confirmed on all active Target nodes. |
| void(\* | [lost\_target](#ab4d00147b1e525f392d09d5545de2465) )(struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli, struct [bt\_mesh\_dfu\_target](structbt__mesh__dfu__target.md) \*target) |
|  | DFU Target node was lost. |

## Detailed Description

Firmware Update Client event callbacks.

## Field Documentation

## [◆ ](#a6f580db9629d81f72c79d00a5aea2de4)applied

| void(\* bt\_mesh\_dfu\_cli\_cb::applied) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli) |
| --- |

DFU transfer applied on all active Target nodes.

Called at the end of the apply procedure started by [bt\_mesh\_dfu\_cli\_apply](group__bt__mesh__dfu__cli.md#ga2904ba992a00ee9fba6704c1efc8f074 "bt_mesh_dfu_cli_apply").

Parameters
:   | cli | Firmware Update Client model instance. |
    | --- | --- |

## [◆ ](#a32b20280b2196437bad6d85edc017c63)confirmed

| void(\* bt\_mesh\_dfu\_cli\_cb::confirmed) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli) |
| --- |

DFU transfer confirmed on all active Target nodes.

Called at the end of the apply procedure started by [bt\_mesh\_dfu\_cli\_confirm](group__bt__mesh__dfu__cli.md#gaf76f0cdb5c6b0df12ddb495c718c3c93 "bt_mesh_dfu_cli_confirm").

Parameters
:   | cli | Firmware Update Client model instance. |
    | --- | --- |

## [◆ ](#aa3c8985490a6b2bd6fcd81dff0132060)ended

| void(\* bt\_mesh\_dfu\_cli\_cb::ended) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli, enum [bt\_mesh\_dfu\_status](group__bt__mesh__dfu.md#ga9e627a3c15de782faa11ef6c4ec5e05d) reason) |
| --- |

DFU ended.

Called when the DFU transfer ends, either because all Target nodes were lost or because the transfer was completed successfully.

Parameters
:   | cli | Firmware Update Client model instance. |
    | --- | --- |
    | reason | Reason for ending. |

## [◆ ](#ab4d00147b1e525f392d09d5545de2465)lost\_target

| void(\* bt\_mesh\_dfu\_cli\_cb::lost\_target) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli, struct [bt\_mesh\_dfu\_target](structbt__mesh__dfu__target.md) \*target) |
| --- |

DFU Target node was lost.

A DFU Target node was dropped from the receivers list. The Target node's `status` is set to reflect the reason for the failure.

Parameters
:   | cli | Firmware Update Client model instance. |
    | --- | --- |
    | target | DFU Target node that was lost. |

## [◆ ](#ad2abfdf93f23cecd30e12241bb064a7f)suspended

| void(\* bt\_mesh\_dfu\_cli\_cb::suspended) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli) |
| --- |

BLOB transfer is suspended.

Called when the BLOB transfer is suspended due to response timeout from all Target nodes.

Parameters
:   | cli | Firmware Update Client model instance. |
    | --- | --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[dfu\_cli.h](dfu__cli_8h_source.md)

- [bt\_mesh\_dfu\_cli\_cb](structbt__mesh__dfu__cli__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
