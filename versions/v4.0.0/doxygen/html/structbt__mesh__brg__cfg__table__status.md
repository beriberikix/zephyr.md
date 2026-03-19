---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__brg__cfg__table__status.html
original_path: doxygen/html/structbt__mesh__brg__cfg__table__status.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_brg\_cfg\_table\_status Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bridge Configuration common header](group__bt__mesh__brg__cfg.md)

Bridging Table Status response.
[More...](#details)

`#include <[brg_cfg.h](brg__cfg_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [status](#a6f1ad52ec00ec819064edf503f74744a) |
|  | Status Code of the requesting message. |
| struct [bt\_mesh\_brg\_cfg\_table\_entry](structbt__mesh__brg__cfg__table__entry.md) | [entry](#ae469e4759604077773b45b8ee1f28c37) |
|  | Requested Bridging Table entry. |

## Detailed Description

Bridging Table Status response.

## Field Documentation

## [◆ ](#ae469e4759604077773b45b8ee1f28c37)entry

| struct [bt\_mesh\_brg\_cfg\_table\_entry](structbt__mesh__brg__cfg__table__entry.md) bt\_mesh\_brg\_cfg\_table\_status::entry |
| --- |

Requested Bridging Table entry.

## [◆ ](#a6f1ad52ec00ec819064edf503f74744a)status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_brg\_cfg\_table\_status::status |
| --- |

Status Code of the requesting message.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[brg\_cfg.h](brg__cfg_8h_source.md)

- [bt\_mesh\_brg\_cfg\_table\_status](structbt__mesh__brg__cfg__table__status.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
