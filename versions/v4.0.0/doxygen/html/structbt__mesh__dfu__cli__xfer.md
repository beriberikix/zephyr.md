---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__dfu__cli__xfer.html
original_path: doxygen/html/structbt__mesh__dfu__cli__xfer.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_dfu\_cli\_xfer Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh Device Firmware Update](group__bt__mesh__dfu.md) » [Firmware Uppdate Client model](group__bt__mesh__dfu__cli.md)

Firmware Update Client transfer parameters:
[More...](#details)

`#include <[dfu_cli.h](dfu__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [blob\_id](#adece8c0e0cec2262a7066b27636fc46e) |
|  | BLOB ID to use for this transfer, or 0 to set it randomly. |
| const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \* | [slot](#a3c25a54eb4e557d749a9fb1ba66aecb4) |
|  | DFU image slot to transfer. |
| enum [bt\_mesh\_blob\_xfer\_mode](group__bt__mesh__blob.md#gae0cb28c0e50d02f6e003062457053618) | [mode](#a6608f683fd94e12f7c3ef5f3de7ec248) |
|  | Transfer mode (Push (Push BLOB Transfer Mode) or Pull (Pull BLOB Transfer Mode)). |
| const struct [bt\_mesh\_dfu\_cli\_xfer\_blob\_params](structbt__mesh__dfu__cli__xfer__blob__params.md) \* | [blob\_params](#a2c4feacc090dace0986e533257f9b291) |
|  | BLOB parameters to be used for the transfer, or NULL to retrieve Target nodes' capabilities before sending a firmware. |

## Detailed Description

Firmware Update Client transfer parameters:

## Field Documentation

## [◆ ](#adece8c0e0cec2262a7066b27636fc46e)blob\_id

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) bt\_mesh\_dfu\_cli\_xfer::blob\_id |
| --- |

BLOB ID to use for this transfer, or 0 to set it randomly.

## [◆ ](#a2c4feacc090dace0986e533257f9b291)blob\_params

| const struct [bt\_mesh\_dfu\_cli\_xfer\_blob\_params](structbt__mesh__dfu__cli__xfer__blob__params.md)\* bt\_mesh\_dfu\_cli\_xfer::blob\_params |
| --- |

BLOB parameters to be used for the transfer, or NULL to retrieve Target nodes' capabilities before sending a firmware.

## [◆ ](#a6608f683fd94e12f7c3ef5f3de7ec248)mode

| enum [bt\_mesh\_blob\_xfer\_mode](group__bt__mesh__blob.md#gae0cb28c0e50d02f6e003062457053618) bt\_mesh\_dfu\_cli\_xfer::mode |
| --- |

Transfer mode (Push (Push BLOB Transfer Mode) or Pull (Pull BLOB Transfer Mode)).

## [◆ ](#a3c25a54eb4e557d749a9fb1ba66aecb4)slot

| const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md)\* bt\_mesh\_dfu\_cli\_xfer::slot |
| --- |

DFU image slot to transfer.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[dfu\_cli.h](dfu__cli_8h_source.md)

- [bt\_mesh\_dfu\_cli\_xfer](structbt__mesh__dfu__cli__xfer.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
