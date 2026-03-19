---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__mesh__large__comp__data__cli.html
original_path: doxygen/html/group__bt__mesh__large__comp__data__cli.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Large Composition Data Client model

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_large\_comp\_data\_rsp](structbt__mesh__large__comp__data__rsp.md) |
|  | Large Composition Data response. [More...](structbt__mesh__large__comp__data__rsp.md#details) |
| struct | [bt\_mesh\_large\_comp\_data\_cli\_cb](structbt__mesh__large__comp__data__cli__cb.md) |
|  | Large Composition Data Status messages callbacks. [More...](structbt__mesh__large__comp__data__cli__cb.md#details) |
| struct | [bt\_mesh\_large\_comp\_data\_cli](structbt__mesh__large__comp__data__cli.md) |
|  | Large Composition Data Client model context. [More...](structbt__mesh__large__comp__data__cli.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_LARGE\_COMP\_DATA\_CLI](#ga5860da397d1cd830e8010946c5b32f1e)(cli\_data) |
|  | Large Composition Data Client model Composition Data entry. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_large\_comp\_data\_get](#gaf505ee14246746fc245a34328443d1c6) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) page, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, struct [bt\_mesh\_large\_comp\_data\_rsp](structbt__mesh__large__comp__data__rsp.md) \*rsp) |
|  | Send Large Composition Data Get message. |
| int | [bt\_mesh\_models\_metadata\_get](#ga4073eb48c43460804705d80ac0919864) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) page, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, struct [bt\_mesh\_large\_comp\_data\_rsp](structbt__mesh__large__comp__data__rsp.md) \*rsp) |
|  | Send Models Metadata Get message. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga5860da397d1cd830e8010946c5b32f1e)BT\_MESH\_MODEL\_LARGE\_COMP\_DATA\_CLI

| #define BT\_MESH\_MODEL\_LARGE\_COMP\_DATA\_CLI | ( |  | *cli\_data* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[large_comp_data_cli.h](large__comp__data__cli_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)([BT\_MESH\_MODEL\_ID\_LARGE\_COMP\_DATA\_CLI](group__bt__mesh__access.md#ga729d67e4183457932e4c837d65abd842), \

\_bt\_mesh\_large\_comp\_data\_cli\_op, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), cli\_data, \

&\_bt\_mesh\_large\_comp\_data\_cli\_cb)

[BT\_MESH\_MODEL\_ID\_LARGE\_COMP\_DATA\_CLI](group__bt__mesh__access.md#ga729d67e4183457932e4c837d65abd842)

#define BT\_MESH\_MODEL\_ID\_LARGE\_COMP\_DATA\_CLI

Large Composition Data Client.

**Definition** access.h:209

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)

#define BT\_MESH\_MODEL\_CB(\_id, \_op, \_pub, \_user\_data, \_cb)

Composition data SIG model entry with callback functions.

**Definition** access.h:495

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

Large Composition Data Client model Composition Data entry.

Parameters
:   | cli\_data | Pointer to a [Large Composition Data Client model](group__bt__mesh__large__comp__data__cli.md "Large Composition Data Client model") instance. |
    | --- | --- |

## Function Documentation

## [◆ ](#gaf505ee14246746fc245a34328443d1c6)bt\_mesh\_large\_comp\_data\_get()

| int bt\_mesh\_large\_comp\_data\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *page*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *offset*, |
|  |  | struct [bt\_mesh\_large\_comp\_data\_rsp](structbt__mesh__large__comp__data__rsp.md) \* | *rsp* ) |

`#include <[large_comp_data_cli.h](large__comp__data__cli_8h.md)>`

Send Large Composition Data Get message.

This API is used to read a portion of a Composition Data Page.

This API can be used asynchronously by setting `rsp` as NULL. This way, the method will not wait for a response and will return immediately after sending the command.

When `rsp` is set, the user is responsible for providing a buffer for the Composition Data in [bt\_mesh\_large\_comp\_data\_rsp::data](structbt__mesh__large__comp__data__rsp.md#a02d92a210b5b7a26b1df4f5076ed99d8 "bt_mesh_large_comp_data_rsp::data"). If a buffer is not provided, the metadata won't be copied.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node element address. |
    | page | Composition Data Page to read. |
    | offset | Offset within the Composition Data Page. |
    | rsp | Pointer to a struct storing the received response from the server, or NULL to not wait for a response. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga4073eb48c43460804705d80ac0919864)bt\_mesh\_models\_metadata\_get()

| int bt\_mesh\_models\_metadata\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *page*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *offset*, |
|  |  | struct [bt\_mesh\_large\_comp\_data\_rsp](structbt__mesh__large__comp__data__rsp.md) \* | *rsp* ) |

`#include <[large_comp_data_cli.h](large__comp__data__cli_8h.md)>`

Send Models Metadata Get message.

This API is used to read a portion of a Models Metadata Page.

This API can be used asynchronously by setting `rsp` as NULL. This way, the method will not wait for a response and will return immediately after sending the command.

When `rsp` is set, a user is responsible for providing a buffer for metadata in [bt\_mesh\_large\_comp\_data\_rsp::data](structbt__mesh__large__comp__data__rsp.md#a02d92a210b5b7a26b1df4f5076ed99d8 "bt_mesh_large_comp_data_rsp::data"). If a buffer is not provided, the metadata won't be copied.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node element address. |
    | page | Models Metadata Page to read. |
    | offset | Offset within the Models Metadata Page. |
    | rsp | Pointer to a struct storing the received response from the server, or NULL to not wait for a response. |

Returns
:   0 on success, or (negative) error code on failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
