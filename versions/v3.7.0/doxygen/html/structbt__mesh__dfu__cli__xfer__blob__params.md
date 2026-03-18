---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__dfu__cli__xfer__blob__params.html
original_path: doxygen/html/structbt__mesh__dfu__cli__xfer__blob__params.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_dfu\_cli\_xfer\_blob\_params Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh Device Firmware Update](group__bt__mesh__dfu.md) » [Firmware Uppdate Client model](group__bt__mesh__dfu__cli.md)

BLOB parameters for Firmware Update Client transfer:
[More...](#details)

`#include <[dfu_cli.h](dfu__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [block\_size\_log](#a45452ae73f585ffba5c76291d41dd1ed) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [chunk\_size](#a1015b239306bd5eb1c9648b5c1d59481) |
|  | Base chunk size. |

## Detailed Description

BLOB parameters for Firmware Update Client transfer:

## Field Documentation

## [◆ ](#a45452ae73f585ffba5c76291d41dd1ed)block\_size\_log

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dfu\_cli\_xfer\_blob\_params::block\_size\_log |
| --- |

## [◆ ](#a1015b239306bd5eb1c9648b5c1d59481)chunk\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_dfu\_cli\_xfer\_blob\_params::chunk\_size |
| --- |

Base chunk size.

May be smaller for the last chunk.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[dfu\_cli.h](dfu__cli_8h_source.md)

- [bt\_mesh\_dfu\_cli\_xfer\_blob\_params](structbt__mesh__dfu__cli__xfer__blob__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
