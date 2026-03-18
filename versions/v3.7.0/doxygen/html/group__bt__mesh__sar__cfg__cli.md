---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__mesh__sar__cfg__cli.html
original_path: doxygen/html/group__bt__mesh__sar__cfg__cli.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bluetooth Mesh SAR Configuration Client Model

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

Bluetooth Mesh.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_sar\_cfg\_cli](structbt__mesh__sar__cfg__cli.md) |
|  | Mesh SAR Configuration Client Model Context. [More...](structbt__mesh__sar__cfg__cli.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_SAR\_CFG\_CLI](#ga742d31e7175e472f1a096ffa6a5acdc5)(\_cli) |
|  | SAR Configuration Client model composition data entry. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_sar\_cfg\_cli\_transmitter\_get](#ga893ef5861708bec12f87b9f9cc64b9fc) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_sar\_tx](structbt__mesh__sar__tx.md) \*rsp) |
|  | Get the SAR Transmitter state of the target node. |
| int | [bt\_mesh\_sar\_cfg\_cli\_transmitter\_set](#ga32e2a580b24a41761911e88413e9664e) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, const struct [bt\_mesh\_sar\_tx](structbt__mesh__sar__tx.md) \*set, struct [bt\_mesh\_sar\_tx](structbt__mesh__sar__tx.md) \*rsp) |
|  | Set the SAR Transmitter state of the target node. |
| int | [bt\_mesh\_sar\_cfg\_cli\_receiver\_get](#ga444c99254ef2ccdd10dac08a94219d79) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_sar\_rx](structbt__mesh__sar__rx.md) \*rsp) |
|  | Get the SAR Receiver state of the target node. |
| int | [bt\_mesh\_sar\_cfg\_cli\_receiver\_set](#ga884025b2baf8559950ba6dc83e9ef486) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, const struct [bt\_mesh\_sar\_rx](structbt__mesh__sar__rx.md) \*set, struct [bt\_mesh\_sar\_rx](structbt__mesh__sar__rx.md) \*rsp) |
|  | Set the SAR Receiver state of the target node. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [bt\_mesh\_sar\_cfg\_cli\_timeout\_get](#ga998846e5735676dc5f79b387d02630d4) (void) |
|  | Get the current transmission timeout value. |
| void | [bt\_mesh\_sar\_cfg\_cli\_timeout\_set](#ga57d7c6a973b35f53689cbf8a065a538f) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Set the transmission timeout value. |

## Detailed Description

Bluetooth Mesh.

## Macro Definition Documentation

## [◆ ](#ga742d31e7175e472f1a096ffa6a5acdc5)BT\_MESH\_MODEL\_SAR\_CFG\_CLI

| #define BT\_MESH\_MODEL\_SAR\_CFG\_CLI | ( |  | *\_cli* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sar_cfg_cli.h](sar__cfg__cli_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)([BT\_MESH\_MODEL\_ID\_SAR\_CFG\_CLI](group__bt__mesh__access.md#gaf214eb7eef3530919432b62ff9b353c3), \

\_bt\_mesh\_sar\_cfg\_cli\_op, \_cli.pub, \_cli, \

&\_bt\_mesh\_sar\_cfg\_cli\_cb)

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)

#define BT\_MESH\_MODEL\_CB(\_id, \_op, \_pub, \_user\_data, \_cb)

Composition data SIG model entry with callback functions.

**Definition** access.h:491

[BT\_MESH\_MODEL\_ID\_SAR\_CFG\_CLI](group__bt__mesh__access.md#gaf214eb7eef3530919432b62ff9b353c3)

#define BT\_MESH\_MODEL\_ID\_SAR\_CFG\_CLI

SAR Configuration Client.

**Definition** access.h:197

SAR Configuration Client model composition data entry.

Parameters
:   | [in] | \_cli | Pointer to a [Bluetooth Mesh SAR Configuration Client Model](group__bt__mesh__sar__cfg__cli.md "Bluetooth Mesh SAR Configuration Client Model") instance. |
    | --- | --- | --- |

## Function Documentation

## [◆ ](#ga444c99254ef2ccdd10dac08a94219d79)bt\_mesh\_sar\_cfg\_cli\_receiver\_get()

| int bt\_mesh\_sar\_cfg\_cli\_receiver\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | struct [bt\_mesh\_sar\_rx](structbt__mesh__sar__rx.md) \* | *rsp* ) |

`#include <[sar_cfg_cli.h](sar__cfg__cli_8h.md)>`

Get the SAR Receiver state of the target node.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | rsp | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga884025b2baf8559950ba6dc83e9ef486)bt\_mesh\_sar\_cfg\_cli\_receiver\_set()

| int bt\_mesh\_sar\_cfg\_cli\_receiver\_set | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | const struct [bt\_mesh\_sar\_rx](structbt__mesh__sar__rx.md) \* | *set*, |
|  |  | struct [bt\_mesh\_sar\_rx](structbt__mesh__sar__rx.md) \* | *rsp* ) |

`#include <[sar_cfg_cli.h](sar__cfg__cli_8h.md)>`

Set the SAR Receiver state of the target node.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | set | New SAR Receiver state to set on the target node. |
    | rsp | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga998846e5735676dc5f79b387d02630d4)bt\_mesh\_sar\_cfg\_cli\_timeout\_get()

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) bt\_mesh\_sar\_cfg\_cli\_timeout\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sar_cfg_cli.h](sar__cfg__cli_8h.md)>`

Get the current transmission timeout value.

Returns
:   The configured transmission timeout in milliseconds.

## [◆ ](#ga57d7c6a973b35f53689cbf8a065a538f)bt\_mesh\_sar\_cfg\_cli\_timeout\_set()

| void bt\_mesh\_sar\_cfg\_cli\_timeout\_set | ( | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sar_cfg_cli.h](sar__cfg__cli_8h.md)>`

Set the transmission timeout value.

Parameters
:   | timeout | The new transmission timeout. |
    | --- | --- |

## [◆ ](#ga893ef5861708bec12f87b9f9cc64b9fc)bt\_mesh\_sar\_cfg\_cli\_transmitter\_get()

| int bt\_mesh\_sar\_cfg\_cli\_transmitter\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | struct [bt\_mesh\_sar\_tx](structbt__mesh__sar__tx.md) \* | *rsp* ) |

`#include <[sar_cfg_cli.h](sar__cfg__cli_8h.md)>`

Get the SAR Transmitter state of the target node.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | rsp | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga32e2a580b24a41761911e88413e9664e)bt\_mesh\_sar\_cfg\_cli\_transmitter\_set()

| int bt\_mesh\_sar\_cfg\_cli\_transmitter\_set | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | const struct [bt\_mesh\_sar\_tx](structbt__mesh__sar__tx.md) \* | *set*, |
|  |  | struct [bt\_mesh\_sar\_tx](structbt__mesh__sar__tx.md) \* | *rsp* ) |

`#include <[sar_cfg_cli.h](sar__cfg__cli_8h.md)>`

Set the SAR Transmitter state of the target node.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | set | New SAR Transmitter state to set on the target node. |
    | rsp | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
