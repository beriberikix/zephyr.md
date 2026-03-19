---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__mesh__dfu__metadata__status.html
original_path: doxygen/html/structbt__mesh__dfu__metadata__status.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_dfu\_metadata\_status Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh Device Firmware Update](group__bt__mesh__dfu.md) » [Firmware Uppdate Client model](group__bt__mesh__dfu__cli.md)

Metadata status response.
[More...](#details)

`#include <[dfu_cli.h](dfu__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [idx](#a1d41b76b66acadc20f7f9ec1f4bc8b9b) |
|  | Image index. |
| enum [bt\_mesh\_dfu\_status](group__bt__mesh__dfu.md#ga9e627a3c15de782faa11ef6c4ec5e05d) | [status](#ae7ad71649f295142e48863b6d884b966) |
|  | Status code. |
| enum [bt\_mesh\_dfu\_effect](group__bt__mesh__dfu.md#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8) | [effect](#a299723f7176938b2900cfdae4550965c) |
|  | Effect of transfer. |

## Detailed Description

Metadata status response.

## Field Documentation

## [◆ ](#a299723f7176938b2900cfdae4550965c)effect

| enum [bt\_mesh\_dfu\_effect](group__bt__mesh__dfu.md#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8) bt\_mesh\_dfu\_metadata\_status::effect |
| --- |

Effect of transfer.

## [◆ ](#a1d41b76b66acadc20f7f9ec1f4bc8b9b)idx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dfu\_metadata\_status::idx |
| --- |

Image index.

## [◆ ](#ae7ad71649f295142e48863b6d884b966)status

| enum [bt\_mesh\_dfu\_status](group__bt__mesh__dfu.md#ga9e627a3c15de782faa11ef6c4ec5e05d) bt\_mesh\_dfu\_metadata\_status::status |
| --- |

Status code.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[dfu\_cli.h](dfu__cli_8h_source.md)

- [bt\_mesh\_dfu\_metadata\_status](structbt__mesh__dfu__metadata__status.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
