---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__priv__node__id.html
original_path: doxygen/html/structbt__mesh__priv__node__id.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_priv\_node\_id Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh Private Beacon Client](group__bt__mesh__priv__beacon__cli.md)

Private Node Identity.
[More...](#details)

`#include <[priv_beacon_cli.h](priv__beacon__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_idx](#ab772f79daa361a9199f8445b7bda7e44) |
|  | Index of the NetKey. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [state](#a5bd318e61b974a94765e0d28db15994f) |
|  | Private Node Identity state. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [status](#a49c60fedb24de61a399f3da967f4ac7c) |
|  | Response status code. |

## Detailed Description

Private Node Identity.

## Field Documentation

## [◆ ](#ab772f79daa361a9199f8445b7bda7e44)net\_idx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_priv\_node\_id::net\_idx |
| --- |

Index of the NetKey.

## [◆ ](#a5bd318e61b974a94765e0d28db15994f)state

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_priv\_node\_id::state |
| --- |

Private Node Identity state.

## [◆ ](#a49c60fedb24de61a399f3da967f4ac7c)status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_priv\_node\_id::status |
| --- |

Response status code.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[priv\_beacon\_cli.h](priv__beacon__cli_8h_source.md)

- [bt\_mesh\_priv\_node\_id](structbt__mesh__priv__node__id.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
