---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__bt__mesh__health__cli.html
original_path: doxygen/html/group__bt__mesh__health__cli.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Health Client Model

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

Health Client Model.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) |
|  | Health Client Model Context. [More...](structbt__mesh__health__cli.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_HEALTH\_CLI](#ga0f869fc7d19f5e8be5953a8ece6e07f6)(cli\_data) |
|  | Generic Health Client model composition data entry. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_health\_cli\_fault\_get](#ga2951f45aaaee75f4c77c4381b1ddd617) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*test\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*faults, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*fault\_count) |
|  | Get the registered fault state for the given Company ID. |
| int | [bt\_mesh\_health\_cli\_fault\_clear](#ga77cc4e97193cca60d79a8076f3761ef5) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*test\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*faults, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*fault\_count) |
|  | Clear the registered faults for the given Company ID. |
| int | [bt\_mesh\_health\_cli\_fault\_clear\_unack](#gafb0a46136f82f1aff4273704f1c47ac4) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid) |
|  | Clear the registered faults for the given Company ID (unacked). |
| int | [bt\_mesh\_health\_cli\_fault\_test](#ga00cef275cdf90876f1381ffaff04b25c) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) test\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*faults, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*fault\_count) |
|  | Invoke a self-test procedure for the given Company ID. |
| int | [bt\_mesh\_health\_cli\_fault\_test\_unack](#ga8e58519ef78946e88258b335c350d754) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) test\_id) |
|  | Invoke a self-test procedure for the given Company ID (unacked). |
| int | [bt\_mesh\_health\_cli\_period\_get](#ga1e8e25681b9fcbc6584a29336924a78a) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*divisor) |
|  | Get the target node's Health fast period divisor. |
| int | [bt\_mesh\_health\_cli\_period\_set](#ga2ef46f0b5059a959d5b06d6e49c4f552) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) divisor, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*updated\_divisor) |
|  | Set the target node's Health fast period divisor. |
| int | [bt\_mesh\_health\_cli\_period\_set\_unack](#ga536c631d87daaca017af078d49094fc1) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) divisor) |
|  | Set the target node's Health fast period divisor (unacknowledged). |
| int | [bt\_mesh\_health\_cli\_attention\_get](#gad6f322f506b8577c56bb0613f7dcbd93) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*attention) |
|  | Get the current attention timer value. |
| int | [bt\_mesh\_health\_cli\_attention\_set](#ga1b910d0849ce4c33d6de4bf1ff47ece8) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attention, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*updated\_attention) |
|  | Set the attention timer. |
| int | [bt\_mesh\_health\_cli\_attention\_set\_unack](#ga3a528688e340edf49b4bd62317284834) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attention) |
|  | Set the attention timer (unacknowledged). |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [bt\_mesh\_health\_cli\_timeout\_get](#ga9abc0db22da327d02d23371bba59b46a) (void) |
|  | Get the current transmission timeout value. |
| void | [bt\_mesh\_health\_cli\_timeout\_set](#gaf3d54597a74a458df0053bd0599d39e9) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Set the transmission timeout value. |

## Detailed Description

Health Client Model.

## Macro Definition Documentation

## [◆ ](#ga0f869fc7d19f5e8be5953a8ece6e07f6)BT\_MESH\_MODEL\_HEALTH\_CLI

| #define BT\_MESH\_MODEL\_HEALTH\_CLI | ( |  | *cli\_data* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[health_cli.h](health__cli_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)([BT\_MESH\_MODEL\_ID\_HEALTH\_CLI](group__bt__mesh__access.md#gab58b85b7a77feeb579973177c12bb446), bt\_mesh\_health\_cli\_op, \

&(cli\_data)->pub, cli\_data, &bt\_mesh\_health\_cli\_cb)

[BT\_MESH\_MODEL\_ID\_HEALTH\_CLI](group__bt__mesh__access.md#gab58b85b7a77feeb579973177c12bb446)

#define BT\_MESH\_MODEL\_ID\_HEALTH\_CLI

Health Client.

**Definition** access.h:185

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)

#define BT\_MESH\_MODEL\_CB(\_id, \_op, \_pub, \_user\_data, \_cb)

Composition data SIG model entry with callback functions.

**Definition** access.h:491

Generic Health Client model composition data entry.

Parameters
:   | cli\_data | Pointer to a [Health Client Model](group__bt__mesh__health__cli.md "Health Client Model") instance. |
    | --- | --- |

## Function Documentation

## [◆ ](#gad6f322f506b8577c56bb0613f7dcbd93)bt\_mesh\_health\_cli\_attention\_get()

| int bt\_mesh\_health\_cli\_attention\_get | ( | struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \* | *ctx*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *attention* ) |

`#include <[health_cli.h](health__cli_8h.md)>`

Get the current attention timer value.

This method can be used asynchronously by setting `attention` as NULL. This way the method will not wait for response and will return immediately after sending the command.

To process the response arguments of an async method, register the `attention_status` callback in `[bt_mesh_health_cli](structbt__mesh__health__cli.md "Health Client Model Context.")` struct.

Parameters
:   | cli | Client model to send on. |
    | --- | --- |
    | ctx | Message context, or NULL to use the configured publish parameters. |
    | attention | Attention timer response buffer, measured in seconds. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga1b910d0849ce4c33d6de4bf1ff47ece8)bt\_mesh\_health\_cli\_attention\_set()

| int bt\_mesh\_health\_cli\_attention\_set | ( | struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \* | *ctx*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *attention*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *updated\_attention* ) |

`#include <[health_cli.h](health__cli_8h.md)>`

Set the attention timer.

This method can be used asynchronously by setting `updated_attention` as NULL. This way the method will not wait for response and will return immediately after sending the command.

To process the response arguments of an async method, register the `attention_status` callback in `[bt_mesh_health_cli](structbt__mesh__health__cli.md "Health Client Model Context.")` struct.

Parameters
:   | cli | Client model to send on. |
    | --- | --- |
    | ctx | Message context, or NULL to use the configured publish parameters. |
    | attention | New attention timer time, in seconds. |
    | updated\_attention | Attention timer response buffer, measured in seconds. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga3a528688e340edf49b4bd62317284834)bt\_mesh\_health\_cli\_attention\_set\_unack()

| int bt\_mesh\_health\_cli\_attention\_set\_unack | ( | struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \* | *ctx*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *attention* ) |

`#include <[health_cli.h](health__cli_8h.md)>`

Set the attention timer (unacknowledged).

Parameters
:   | cli | Client model to send on. |
    | --- | --- |
    | ctx | Message context, or NULL to use the configured publish parameters. |
    | attention | New attention timer time, in seconds. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga77cc4e97193cca60d79a8076f3761ef5)bt\_mesh\_health\_cli\_fault\_clear()

| int bt\_mesh\_health\_cli\_fault\_clear | ( | struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \* | *ctx*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *cid*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *test\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *faults*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *fault\_count* ) |

`#include <[health_cli.h](health__cli_8h.md)>`

Clear the registered faults for the given Company ID.

This method can be used asynchronously by setting `test_id` and ( `faults` or `fault_count` ) as NULL This way the method will not wait for response and will return immediately after sending the command.

To process the response arguments of an async method, register the `fault_status` callback in `[bt_mesh_health_cli](structbt__mesh__health__cli.md "Health Client Model Context.")` struct.

See also
:   [Health faults](group__bt__mesh__health__faults.md "List of specification defined Health fault values.")

Parameters
:   | cli | Client model to send on. |
    | --- | --- |
    | ctx | Message context, or NULL to use the configured publish parameters. |
    | cid | Company ID to clear the registered faults for. |
    | test\_id | Test ID response buffer. |
    | faults | Fault array response buffer. |
    | fault\_count | Fault count response buffer. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gafb0a46136f82f1aff4273704f1c47ac4)bt\_mesh\_health\_cli\_fault\_clear\_unack()

| int bt\_mesh\_health\_cli\_fault\_clear\_unack | ( | struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \* | *ctx*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *cid* ) |

`#include <[health_cli.h](health__cli_8h.md)>`

Clear the registered faults for the given Company ID (unacked).

See also
:   [Health faults](group__bt__mesh__health__faults.md "List of specification defined Health fault values.")

Parameters
:   | cli | Client model to send on. |
    | --- | --- |
    | ctx | Message context, or NULL to use the configured publish parameters. |
    | cid | Company ID to clear the registered faults for. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga2951f45aaaee75f4c77c4381b1ddd617)bt\_mesh\_health\_cli\_fault\_get()

| int bt\_mesh\_health\_cli\_fault\_get | ( | struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \* | *ctx*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *cid*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *test\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *faults*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *fault\_count* ) |

`#include <[health_cli.h](health__cli_8h.md)>`

Get the registered fault state for the given Company ID.

This method can be used asynchronously by setting `test_id` and ( `faults` or `fault_count` ) as NULL This way the method will not wait for response and will return immediately after sending the command.

To process the response arguments of an async method, register the `fault_status` callback in `[bt_mesh_health_cli](structbt__mesh__health__cli.md "Health Client Model Context.")` struct.

See also
:   [Health faults](group__bt__mesh__health__faults.md "List of specification defined Health fault values.")

Parameters
:   | cli | Client model to send on. |
    | --- | --- |
    | ctx | Message context, or NULL to use the configured publish parameters. |
    | cid | Company ID to get the registered faults of. |
    | test\_id | Test ID response buffer. |
    | faults | Fault array response buffer. |
    | fault\_count | Fault count response buffer. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga00cef275cdf90876f1381ffaff04b25c)bt\_mesh\_health\_cli\_fault\_test()

| int bt\_mesh\_health\_cli\_fault\_test | ( | struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \* | *ctx*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *cid*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *test\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *faults*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *fault\_count* ) |

`#include <[health_cli.h](health__cli_8h.md)>`

Invoke a self-test procedure for the given Company ID.

This method can be used asynchronously by setting `faults` or `fault_count` as NULL This way the method will not wait for response and will return immediately after sending the command.

To process the response arguments of an async method, register the `fault_status` callback in `[bt_mesh_health_cli](structbt__mesh__health__cli.md "Health Client Model Context.")` struct.

Parameters
:   | cli | Client model to send on. |
    | --- | --- |
    | ctx | Message context, or NULL to use the configured publish parameters. |
    | cid | Company ID to invoke the test for. |
    | test\_id | Test ID response buffer. |
    | faults | Fault array response buffer. |
    | fault\_count | Fault count response buffer. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga8e58519ef78946e88258b335c350d754)bt\_mesh\_health\_cli\_fault\_test\_unack()

| int bt\_mesh\_health\_cli\_fault\_test\_unack | ( | struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \* | *ctx*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *cid*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *test\_id* ) |

`#include <[health_cli.h](health__cli_8h.md)>`

Invoke a self-test procedure for the given Company ID (unacked).

Parameters
:   | cli | Client model to send on. |
    | --- | --- |
    | ctx | Message context, or NULL to use the configured publish parameters. |
    | cid | Company ID to invoke the test for. |
    | test\_id | Test ID response buffer. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga1e8e25681b9fcbc6584a29336924a78a)bt\_mesh\_health\_cli\_period\_get()

| int bt\_mesh\_health\_cli\_period\_get | ( | struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \* | *ctx*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *divisor* ) |

`#include <[health_cli.h](health__cli_8h.md)>`

Get the target node's Health fast period divisor.

The health period divisor is used to increase the publish rate when a fault is registered. Normally, the Health server will publish with the period in the configured publish parameters. When a fault is registered, the publish period is divided by (1 << divisor). For example, if the target node's Health server is configured to publish with a period of 16 seconds, and the Health fast period divisor is 5, the Health server will publish with an interval of 500 ms when a fault is registered.

This method can be used asynchronously by setting `divisor` as NULL. This way the method will not wait for response and will return immediately after sending the command.

To process the response arguments of an async method, register the `period_status` callback in `[bt_mesh_health_cli](structbt__mesh__health__cli.md "Health Client Model Context.")` struct.

Parameters
:   | cli | Client model to send on. |
    | --- | --- |
    | ctx | Message context, or NULL to use the configured publish parameters. |
    | divisor | Health period divisor response buffer. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga2ef46f0b5059a959d5b06d6e49c4f552)bt\_mesh\_health\_cli\_period\_set()

| int bt\_mesh\_health\_cli\_period\_set | ( | struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \* | *ctx*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *divisor*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *updated\_divisor* ) |

`#include <[health_cli.h](health__cli_8h.md)>`

Set the target node's Health fast period divisor.

The health period divisor is used to increase the publish rate when a fault is registered. Normally, the Health server will publish with the period in the configured publish parameters. When a fault is registered, the publish period is divided by (1 << divisor). For example, if the target node's Health server is configured to publish with a period of 16 seconds, and the Health fast period divisor is 5, the Health server will publish with an interval of 500 ms when a fault is registered.

This method can be used asynchronously by setting `updated_divisor` as NULL. This way the method will not wait for response and will return immediately after sending the command.

To process the response arguments of an async method, register the `period_status` callback in `[bt_mesh_health_cli](structbt__mesh__health__cli.md "Health Client Model Context.")` struct.

Parameters
:   | cli | Client model to send on. |
    | --- | --- |
    | ctx | Message context, or NULL to use the configured publish parameters. |
    | divisor | New Health period divisor. |
    | updated\_divisor | Health period divisor response buffer. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga536c631d87daaca017af078d49094fc1)bt\_mesh\_health\_cli\_period\_set\_unack()

| int bt\_mesh\_health\_cli\_period\_set\_unack | ( | struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \* | *ctx*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *divisor* ) |

`#include <[health_cli.h](health__cli_8h.md)>`

Set the target node's Health fast period divisor (unacknowledged).

This is an unacknowledged version of this API.

Parameters
:   | cli | Client model to send on. |
    | --- | --- |
    | ctx | Message context, or NULL to use the configured publish parameters. |
    | divisor | New Health period divisor. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga9abc0db22da327d02d23371bba59b46a)bt\_mesh\_health\_cli\_timeout\_get()

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) bt\_mesh\_health\_cli\_timeout\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[health_cli.h](health__cli_8h.md)>`

Get the current transmission timeout value.

Returns
:   The configured transmission timeout in milliseconds.

## [◆ ](#gaf3d54597a74a458df0053bd0599d39e9)bt\_mesh\_health\_cli\_timeout\_set()

| void bt\_mesh\_health\_cli\_timeout\_set | ( | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[health_cli.h](health__cli_8h.md)>`

Set the transmission timeout value.

Parameters
:   | timeout | The new transmission timeout. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
