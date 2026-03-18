---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__mesh__comp__p0.html
original_path: doxygen/html/structbt__mesh__comp__p0.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_comp\_p0 Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Configuration Client Model](group__bt__mesh__cfg__cli.md)

Parsed Composition data page 0 representation.
[More...](#details)

`#include <[cfg_cli.h](cfg__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [cid](#a3ed8f5ac643443bbcca308baff1c539c) |
|  | Company ID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [pid](#a009806e046583c99f56d271ecebbb8a3) |
|  | Product ID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [vid](#a27d910cdeb7b6b9d038898e3824dfb57) |
|  | Version ID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [crpl](#a32bfead26f338aba892a5459615a65a2) |
|  | Replay protection list size. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [feat](#a0a44e3778f9d134a5c056ca184c3b527) |
|  | Supported features, see [BT\_MESH\_FEAT\_SUPPORTED](group__bt__mesh.md#gac337fd8688d70e862974e010ad42a11b "BT_MESH_FEAT_SUPPORTED"). |

## Detailed Description

Parsed Composition data page 0 representation.

Should be pulled from the return buffer passed to [bt\_mesh\_cfg\_cli\_comp\_data\_get](group__bt__mesh__cfg__cli.md#ga36259e9c811a8f1a21d642739cf297df "bt_mesh_cfg_cli_comp_data_get") using [bt\_mesh\_comp\_p0\_get](group__bt__mesh__cfg__cli.md#ga1f79d98273a984f1c49b4d5dd5bf8d30 "bt_mesh_comp_p0_get").

## Field Documentation

## [◆ ](#a3ed8f5ac643443bbcca308baff1c539c)cid

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_comp\_p0::cid |
| --- |

Company ID.

## [◆ ](#a32bfead26f338aba892a5459615a65a2)crpl

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_comp\_p0::crpl |
| --- |

Replay protection list size.

## [◆ ](#a0a44e3778f9d134a5c056ca184c3b527)feat

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_comp\_p0::feat |
| --- |

Supported features, see [BT\_MESH\_FEAT\_SUPPORTED](group__bt__mesh.md#gac337fd8688d70e862974e010ad42a11b "BT_MESH_FEAT_SUPPORTED").

## [◆ ](#a009806e046583c99f56d271ecebbb8a3)pid

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_comp\_p0::pid |
| --- |

Product ID.

## [◆ ](#a27d910cdeb7b6b9d038898e3824dfb57)vid

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_comp\_p0::vid |
| --- |

Version ID.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[cfg\_cli.h](cfg__cli_8h_source.md)

- [bt\_mesh\_comp\_p0](structbt__mesh__comp__p0.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
