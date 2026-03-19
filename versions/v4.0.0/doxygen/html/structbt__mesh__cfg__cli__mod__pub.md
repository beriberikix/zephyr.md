---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__cfg__cli__mod__pub.html
original_path: doxygen/html/structbt__mesh__cfg__cli__mod__pub.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_cfg\_cli\_mod\_pub Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Configuration Client Model](group__bt__mesh__cfg__cli.md)

Model publication configuration parameters.
[More...](#details)

`#include <[cfg_cli.h](cfg__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [addr](#ab52dd35df271ae5bd70a4640e6f3bea8) |
|  | Publication destination address. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [uuid](#a29cbd50ad33f25ad3b98b4ec7ac56a6c) |
|  | Virtual address UUID, or NULL if this is not a virtual address. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [app\_idx](#aefbe5449a10379b064dea054300cb9a0) |
|  | Application index to publish with. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [cred\_flag](#aa7452f697410fdf8a63808bcb29c53ee) |
|  | Friendship credential flag. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ttl](#a9513db038ec4f51734892bd1ce7d08f3) |
|  | Time To Live to publish with. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [period](#a104afe2b8d9766e037293b09c0c1b91c) |
|  | Encoded publish period. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [transmit](#a2a5a0ead8155bf971c84f73dfa4ec282) |
|  | Encoded transmit parameters. |

## Detailed Description

Model publication configuration parameters.

## Field Documentation

## [◆ ](#ab52dd35df271ae5bd70a4640e6f3bea8)addr

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_cfg\_cli\_mod\_pub::addr |
| --- |

Publication destination address.

## [◆ ](#aefbe5449a10379b064dea054300cb9a0)app\_idx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_cfg\_cli\_mod\_pub::app\_idx |
| --- |

Application index to publish with.

## [◆ ](#aa7452f697410fdf8a63808bcb29c53ee)cred\_flag

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_mesh\_cfg\_cli\_mod\_pub::cred\_flag |
| --- |

Friendship credential flag.

## [◆ ](#a104afe2b8d9766e037293b09c0c1b91c)period

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_cfg\_cli\_mod\_pub::period |
| --- |

Encoded publish period.

See also
:   [BT\_MESH\_PUB\_PERIOD\_100MS](group__bt__mesh__cfg__cli.md#gab542c707fb5bad0a15088fefda775a42 "Helper macro to encode model publication period in units of 100ms."), [BT\_MESH\_PUB\_PERIOD\_SEC](group__bt__mesh__cfg__cli.md#ga29435e527a73ff6e19339b773c8eb79e "Helper macro to encode model publication period in units of 1 second."), [BT\_MESH\_PUB\_PERIOD\_10SEC](group__bt__mesh__cfg__cli.md#ga654204077adaa08259d1afbfe92e070e "Helper macro to encode model publication period in units of 10 seconds."), [BT\_MESH\_PUB\_PERIOD\_10MIN](group__bt__mesh__cfg__cli.md#ga36c37f644ee39ad91b6167f68c806b7e "Helper macro to encode model publication period in units of 10 minutes.")

## [◆ ](#a2a5a0ead8155bf971c84f73dfa4ec282)transmit

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_cfg\_cli\_mod\_pub::transmit |
| --- |

Encoded transmit parameters.

See also
:   [BT\_MESH\_TRANSMIT](group__bt__mesh__access.md#gaff82bf652232fbce71c31f38a10577a9 "Encode transmission count & interval steps.")

## [◆ ](#a9513db038ec4f51734892bd1ce7d08f3)ttl

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_cfg\_cli\_mod\_pub::ttl |
| --- |

Time To Live to publish with.

## [◆ ](#a29cbd50ad33f25ad3b98b4ec7ac56a6c)uuid

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_mesh\_cfg\_cli\_mod\_pub::uuid |
| --- |

Virtual address UUID, or NULL if this is not a virtual address.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[cfg\_cli.h](cfg__cli_8h_source.md)

- [bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
