---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__sol__pdu__rpl__cli.html
original_path: doxygen/html/structbt__mesh__sol__pdu__rpl__cli.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_sol\_pdu\_rpl\_cli Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh Solicitation PDU RPL Client](group__bt__mesh__sol__pdu__rpl__cli.md)

Solicitation PDU RPL Client Model Context.
[More...](#details)

`#include <[sol_pdu_rpl_cli.h](sol__pdu__rpl__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | [model](#a272ff5ae0930f51c9175d99f5c9066e2) |
|  | Solicitation PDU RPL model entry pointer. |
| struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) | [ack\_ctx](#a291134f4b6acc60671307ef3b53c4ac8) |
| void(\* | [srpl\_status](#a6c734589ee3361bfc071da55521a6dee) )(struct [bt\_mesh\_sol\_pdu\_rpl\_cli](structbt__mesh__sol__pdu__rpl__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) range\_start, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) range\_length) |
|  | Optional callback for Solicitation PDU RPL Status messages. |

## Detailed Description

Solicitation PDU RPL Client Model Context.

## Field Documentation

## [◆ ](#a291134f4b6acc60671307ef3b53c4ac8)ack\_ctx

| struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) bt\_mesh\_sol\_pdu\_rpl\_cli::ack\_ctx |
| --- |

## [◆ ](#a272ff5ae0930f51c9175d99f5c9066e2)model

| const struct [bt\_mesh\_model](structbt__mesh__model.md)\* bt\_mesh\_sol\_pdu\_rpl\_cli::model |
| --- |

Solicitation PDU RPL model entry pointer.

## [◆ ](#a6c734589ee3361bfc071da55521a6dee)srpl\_status

| void(\* bt\_mesh\_sol\_pdu\_rpl\_cli::srpl\_status) (struct [bt\_mesh\_sol\_pdu\_rpl\_cli](structbt__mesh__sol__pdu__rpl__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) range\_start, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) range\_length) |
| --- |

Optional callback for Solicitation PDU RPL Status messages.

Handles received Solicitation PDU RPL Status messages from a Solicitation PDU RPL server.The `start` param represents the start of range that server has cleared. The `length` param represents length of range cleared by server.

Parameters
:   | cli | Solicitation PDU RPL client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | range\_start | Range start value. |
    | range\_length | Range length value. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[sol\_pdu\_rpl\_cli.h](sol__pdu__rpl__cli_8h_source.md)

- [bt\_mesh\_sol\_pdu\_rpl\_cli](structbt__mesh__sol__pdu__rpl__cli.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
