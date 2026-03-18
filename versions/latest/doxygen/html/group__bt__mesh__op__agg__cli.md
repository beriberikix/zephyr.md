---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__bt__mesh__op__agg__cli.html
original_path: doxygen/html/group__bt__mesh__op__agg__cli.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Opcodes Aggregator Client model

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_OP\_AGG\_CLI](#ga0a8dec4b4f53d1ec95db1efc4ab22f69) |
|  | Opcodes Aggregator Client model composition data entry. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_op\_agg\_cli\_seq\_start](#gac1905d778362faf442a9538adca34a8c) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) app\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dst, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr) |
|  | Configure Opcodes Aggregator context. |
| int | [bt\_mesh\_op\_agg\_cli\_seq\_send](#gab151f44fcb5d3f3f0f1dafaf90f05c18) (void) |
|  | Opcodes Aggregator message send. |
| void | [bt\_mesh\_op\_agg\_cli\_seq\_abort](#ga00b5e695503ba169a1b5ec626413b322) (void) |
|  | Abort Opcodes Aggregator context. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_op\_agg\_cli\_seq\_is\_started](#gadbc347b2dc3d78a4ac71d424f0623b6f) (void) |
|  | Check if Opcodes Aggregator Sequence context is started. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [bt\_mesh\_op\_agg\_cli\_seq\_tailroom](#ga4269bc6118371e2af0967841b18a02dd) (void) |
|  | Get Opcodes Aggregator context tailroom. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [bt\_mesh\_op\_agg\_cli\_timeout\_get](#ga83e44b062babcf0bdb343455e3eddf5f) (void) |
|  | Get the current transmission timeout value. |
| void | [bt\_mesh\_op\_agg\_cli\_timeout\_set](#gaf70cebae8dbd6eb4ef6402585a90e0d5) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Set the transmission timeout value. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga0a8dec4b4f53d1ec95db1efc4ab22f69)BT\_MESH\_MODEL\_OP\_AGG\_CLI

| #define BT\_MESH\_MODEL\_OP\_AGG\_CLI |
| --- |

`#include <[op_agg_cli.h](op__agg__cli_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)([BT\_MESH\_MODEL\_ID\_OP\_AGG\_CLI](group__bt__mesh__access.md#gabac62a77e7d2d7677af21c33c8629187), \_bt\_mesh\_op\_agg\_cli\_op, \

NULL, NULL, &\_bt\_mesh\_op\_agg\_cli\_cb)

[BT\_MESH\_MODEL\_ID\_OP\_AGG\_CLI](group__bt__mesh__access.md#gabac62a77e7d2d7677af21c33c8629187)

#define BT\_MESH\_MODEL\_ID\_OP\_AGG\_CLI

Opcodes Aggregator Client.

**Definition** access.h:201

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)

#define BT\_MESH\_MODEL\_CB(\_id, \_op, \_pub, \_user\_data, \_cb)

Composition data SIG model entry with callback functions.

**Definition** access.h:491

Opcodes Aggregator Client model composition data entry.

## Function Documentation

## [◆ ](#ga00b5e695503ba169a1b5ec626413b322)bt\_mesh\_op\_agg\_cli\_seq\_abort()

| void bt\_mesh\_op\_agg\_cli\_seq\_abort | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[op_agg_cli.h](op__agg__cli_8h.md)>`

Abort Opcodes Aggregator context.

## [◆ ](#gadbc347b2dc3d78a4ac71d424f0623b6f)bt\_mesh\_op\_agg\_cli\_seq\_is\_started()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_mesh\_op\_agg\_cli\_seq\_is\_started | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[op_agg_cli.h](op__agg__cli_8h.md)>`

Check if Opcodes Aggregator Sequence context is started.

Returns
:   true if it is started, otherwise false.

## [◆ ](#gab151f44fcb5d3f3f0f1dafaf90f05c18)bt\_mesh\_op\_agg\_cli\_seq\_send()

| int bt\_mesh\_op\_agg\_cli\_seq\_send | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[op_agg_cli.h](op__agg__cli_8h.md)>`

Opcodes Aggregator message send.

Uses previously configured context and sends aggregated message to target node.

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gac1905d778362faf442a9538adca34a8c)bt\_mesh\_op\_agg\_cli\_seq\_start()

| int bt\_mesh\_op\_agg\_cli\_seq\_start | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *app\_idx*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *dst*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr* ) |

`#include <[op_agg_cli.h](op__agg__cli_8h.md)>`

Configure Opcodes Aggregator context.

Parameters
:   | net\_idx | NetKey index to encrypt with. |
    | --- | --- |
    | app\_idx | AppKey index to encrypt with. |
    | dst | Target Opcodes Aggregator Server address. |
    | elem\_addr | Target node element address for the sequence message. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga4269bc6118371e2af0967841b18a02dd)bt\_mesh\_op\_agg\_cli\_seq\_tailroom()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_mesh\_op\_agg\_cli\_seq\_tailroom | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[op_agg_cli.h](op__agg__cli_8h.md)>`

Get Opcodes Aggregator context tailroom.

Returns
:   Remaning tailroom of Opcodes Aggregator SDU.

## [◆ ](#ga83e44b062babcf0bdb343455e3eddf5f)bt\_mesh\_op\_agg\_cli\_timeout\_get()

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) bt\_mesh\_op\_agg\_cli\_timeout\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[op_agg_cli.h](op__agg__cli_8h.md)>`

Get the current transmission timeout value.

Returns
:   The configured transmission timeout in milliseconds.

## [◆ ](#gaf70cebae8dbd6eb4ef6402585a90e0d5)bt\_mesh\_op\_agg\_cli\_timeout\_set()

| void bt\_mesh\_op\_agg\_cli\_timeout\_set | ( | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[op_agg_cli.h](op__agg__cli_8h.md)>`

Set the transmission timeout value.

Parameters
:   | timeout | The new transmission timeout. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
