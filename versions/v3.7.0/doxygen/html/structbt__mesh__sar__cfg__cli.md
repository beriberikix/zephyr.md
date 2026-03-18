---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__sar__cfg__cli.html
original_path: doxygen/html/structbt__mesh__sar__cfg__cli.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_sar\_cfg\_cli Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh SAR Configuration Client Model](group__bt__mesh__sar__cfg__cli.md)

Mesh SAR Configuration Client Model Context.
[More...](#details)

`#include <[sar_cfg_cli.h](sar__cfg__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | [model](#a94056c2b7bfc1b495b5bf7e6a5fe3066) |
|  | Access model pointer. |
| struct [bt\_mesh\_model\_pub](structbt__mesh__model__pub.md) | [pub](#a16a6f6c0b0ac8ae80abfb48a5f231418) |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [timeout](#a31fdb2608f2cf80ea17dd1f72e634769) |
| struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) | [ack\_ctx](#a30889368bd4e87efd39b6c456b3510d8) |

## Detailed Description

Mesh SAR Configuration Client Model Context.

## Field Documentation

## [◆ ](#a30889368bd4e87efd39b6c456b3510d8)ack\_ctx

| struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) bt\_mesh\_sar\_cfg\_cli::ack\_ctx |
| --- |

## [◆ ](#a94056c2b7bfc1b495b5bf7e6a5fe3066)model

| const struct [bt\_mesh\_model](structbt__mesh__model.md)\* bt\_mesh\_sar\_cfg\_cli::model |
| --- |

Access model pointer.

## [◆ ](#a16a6f6c0b0ac8ae80abfb48a5f231418)pub

| struct [bt\_mesh\_model\_pub](structbt__mesh__model__pub.md) bt\_mesh\_sar\_cfg\_cli::pub |
| --- |

## [◆ ](#a31fdb2608f2cf80ea17dd1f72e634769)timeout

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) bt\_mesh\_sar\_cfg\_cli::timeout |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[sar\_cfg\_cli.h](sar__cfg__cli_8h_source.md)

- [bt\_mesh\_sar\_cfg\_cli](structbt__mesh__sar__cfg__cli.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
