---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__mesh__sol__pdu__rpl__cli.html
original_path: doxygen/html/group__bt__mesh__sol__pdu__rpl__cli.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bluetooth Mesh Solicitation PDU RPL Client

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_sol\_pdu\_rpl\_cli](structbt__mesh__sol__pdu__rpl__cli.md) |
|  | Solicitation PDU RPL Client Model Context. [More...](structbt__mesh__sol__pdu__rpl__cli.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_SOL\_PDU\_RPL\_CLI](#gac5969e20994b07977484391ac2d7bacb)(cli\_data) |
|  | Solicitation PDU RPL Client model composition data entry. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_sol\_pdu\_rpl\_clear](#gae7e8a0e364c6695a467a64cd89627d81) (struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) range\_start, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) range\_len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*start\_rsp, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*len\_rsp) |
|  | Remove entries from Solicitation PDU RPL of addresses in given range. |
| int | [bt\_mesh\_sol\_pdu\_rpl\_clear\_unack](#ga68fb70fbfb87e76ef6fdb5ac8a1a9506) (struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) range\_start, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) range\_len) |
|  | Remove entries from Solicitation PDU RPL of addresses in given range (unacked). |
| void | [bt\_mesh\_sol\_pdu\_rpl\_cli\_timeout\_set](#gadabdbd95f39a498307e3ca9e50acfeb9) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Set the transmission timeout value. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gac5969e20994b07977484391ac2d7bacb)BT\_MESH\_MODEL\_SOL\_PDU\_RPL\_CLI

| #define BT\_MESH\_MODEL\_SOL\_PDU\_RPL\_CLI | ( |  | *cli\_data* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sol_pdu_rpl_cli.h](sol__pdu__rpl__cli_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)([BT\_MESH\_MODEL\_ID\_SOL\_PDU\_RPL\_CLI](group__bt__mesh__access.md#ga6e747dd364bcfaa368e37c5f01afd530), \

\_bt\_mesh\_sol\_pdu\_rpl\_cli\_op, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), cli\_data, \

&\_bt\_mesh\_sol\_pdu\_rpl\_cli\_cb)

[BT\_MESH\_MODEL\_ID\_SOL\_PDU\_RPL\_CLI](group__bt__mesh__access.md#ga6e747dd364bcfaa368e37c5f01afd530)

#define BT\_MESH\_MODEL\_ID\_SOL\_PDU\_RPL\_CLI

Solicitation PDU RPL Configuration Server.

**Definition** access.h:213

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)

#define BT\_MESH\_MODEL\_CB(\_id, \_op, \_pub, \_user\_data, \_cb)

Composition data SIG model entry with callback functions.

**Definition** access.h:495

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

Solicitation PDU RPL Client model composition data entry.

## Function Documentation

## [◆ ](#gae7e8a0e364c6695a467a64cd89627d81)bt\_mesh\_sol\_pdu\_rpl\_clear()

| int bt\_mesh\_sol\_pdu\_rpl\_clear | ( | struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *range\_start*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *range\_len*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *start\_rsp*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *len\_rsp* ) |

`#include <[sol_pdu_rpl_cli.h](sol__pdu__rpl__cli_8h.md)>`

Remove entries from Solicitation PDU RPL of addresses in given range.

This method can be used asynchronously by setting `start_rsp` or `len_rsp` as NULL. This way the method will not wait for response and will return immediately after sending the command.

To process the response arguments of an async method, register the `srpl_status` callback in `[bt_mesh_sol_pdu_rpl_cli](structbt__mesh__sol__pdu__rpl__cli.md "Solicitation PDU RPL Client Model Context.")` struct.

Parameters
:   | ctx | Message context for the message. |
    | --- | --- |
    | range\_start | Start of Unicast address range. |
    | range\_len | Length of Unicast address range. Valid values are 0x00 and 0x02 to 0xff. |
    | start\_rsp | Range start response buffer. |
    | len\_rsp | Range length response buffer. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ga68fb70fbfb87e76ef6fdb5ac8a1a9506)bt\_mesh\_sol\_pdu\_rpl\_clear\_unack()

| int bt\_mesh\_sol\_pdu\_rpl\_clear\_unack | ( | struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *range\_start*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *range\_len* ) |

`#include <[sol_pdu_rpl_cli.h](sol__pdu__rpl__cli_8h.md)>`

Remove entries from Solicitation PDU RPL of addresses in given range (unacked).

Parameters
:   | ctx | Message context for the message. |
    | --- | --- |
    | range\_start | Start of Unicast address range. |
    | range\_len | Length of Unicast address range. Valid values are 0x00 and 0x02 to 0xff. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#gadabdbd95f39a498307e3ca9e50acfeb9)bt\_mesh\_sol\_pdu\_rpl\_cli\_timeout\_set()

| void bt\_mesh\_sol\_pdu\_rpl\_cli\_timeout\_set | ( | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sol_pdu_rpl_cli.h](sol__pdu__rpl__cli_8h.md)>`

Set the transmission timeout value.

Parameters
:   | timeout | The new transmission timeout in milliseconds. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
