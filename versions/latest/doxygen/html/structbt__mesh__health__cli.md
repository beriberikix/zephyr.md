---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__mesh__health__cli.html
original_path: doxygen/html/structbt__mesh__health__cli.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_health\_cli Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Health Client Model](group__bt__mesh__health__cli.md)

Health Client Model Context.
[More...](#details)

`#include <[health_cli.h](health__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | [model](#ae472c161f7da7c1cb646102ca78f262b) |
|  | Composition data model entry pointer. |
| struct [bt\_mesh\_model\_pub](structbt__mesh__model__pub.md) | [pub](#ae33ffa14689438b39166f4d90386f329) |
|  | Publication structure instance. |
| struct [net\_buf\_simple](structnet__buf__simple.md) | [pub\_buf](#a9ae3415b328b25c6206dacdad874c2aa) |
|  | Publication buffer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pub\_data](#a103d110c6cccd69a9e48619668fc60bc) [[BT\_MESH\_MODEL\_BUF\_LEN](group__bt__mesh__msg.md#ga5352d6fa05808722eba8a76e2446eddb)([BT\_MESH\_MODEL\_OP\_2](group__bt__mesh__access.md#gaa52a40ef5972c4f34cf5ff5a10e21289)(0x80, 0x32), 3)] |
|  | Publication data. |
| void(\* | [period\_status](#a395f525d846ef029bf5ff9fdde6e7c61) )(struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) divisor) |
|  | Optional callback for Health Period Status messages. |
| void(\* | [attention\_status](#ae8d023ac56beb39c0d73a3b9e75f6c96) )(struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attention) |
|  | Optional callback for Health Attention Status messages. |
| void(\* | [fault\_status](#a4cbf24a2407df9bb80e19c1da1558294) )(struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) test\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*faults, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) fault\_count) |
|  | Optional callback for Health Fault Status messages. |
| void(\* | [current\_status](#a6246d36f8110f401f55003661ab15c86) )(struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) test\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*faults, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) fault\_count) |
|  | Optional callback for Health Current Status messages. |
| struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) | [ack\_ctx](#ac2ef6ae4fd8e14ad854a9f2c5c80fc43) |

## Detailed Description

Health Client Model Context.

## Field Documentation

## [◆ ](#ac2ef6ae4fd8e14ad854a9f2c5c80fc43)ack\_ctx

| struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) bt\_mesh\_health\_cli::ack\_ctx |
| --- |

## [◆ ](#ae8d023ac56beb39c0d73a3b9e75f6c96)attention\_status

| void(\* bt\_mesh\_health\_cli::attention\_status) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attention) |
| --- |

Optional callback for Health Attention Status messages.

Handles received Health Attention Status messages from a Health server. The `attention` param represents the current attention value.

Parameters
:   | cli | Health client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | attention | Current attention value. |

## [◆ ](#a6246d36f8110f401f55003661ab15c86)current\_status

| void(\* bt\_mesh\_health\_cli::current\_status) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) test\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*faults, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) fault\_count) |
| --- |

Optional callback for Health Current Status messages.

Handles received Health Current Status messages from a Health server. The `fault` array represents all faults that are currently present in the server's element.

See also
:   [Health faults](group__bt__mesh__health__faults.md "List of specification defined Health fault values.")

Parameters
:   | cli | Health client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | test\_id | Identifier of a most recently performed test. |
    | cid | Company Identifier of the node. |
    | faults | Array of faults. |
    | fault\_count | Number of faults in the fault array. |

## [◆ ](#a4cbf24a2407df9bb80e19c1da1558294)fault\_status

| void(\* bt\_mesh\_health\_cli::fault\_status) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) test\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*faults, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) fault\_count) |
| --- |

Optional callback for Health Fault Status messages.

Handles received Health Fault Status messages from a Health server. The `fault` array represents all faults that are currently present in the server's element.

See also
:   [Health faults](group__bt__mesh__health__faults.md "List of specification defined Health fault values.")

Parameters
:   | cli | Health client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | test\_id | Identifier of a most recently performed test. |
    | cid | Company Identifier of the node. |
    | faults | Array of faults. |
    | fault\_count | Number of faults in the fault array. |

## [◆ ](#ae472c161f7da7c1cb646102ca78f262b)model

| const struct [bt\_mesh\_model](structbt__mesh__model.md)\* bt\_mesh\_health\_cli::model |
| --- |

Composition data model entry pointer.

## [◆ ](#a395f525d846ef029bf5ff9fdde6e7c61)period\_status

| void(\* bt\_mesh\_health\_cli::period\_status) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) divisor) |
| --- |

Optional callback for Health Period Status messages.

Handles received Health Period Status messages from a Health server. The `divisor` param represents the period divisor value.

Parameters
:   | cli | Health client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | divisor | Health Period Divisor value. |

## [◆ ](#ae33ffa14689438b39166f4d90386f329)pub

| struct [bt\_mesh\_model\_pub](structbt__mesh__model__pub.md) bt\_mesh\_health\_cli::pub |
| --- |

Publication structure instance.

## [◆ ](#a9ae3415b328b25c6206dacdad874c2aa)pub\_buf

| struct [net\_buf\_simple](structnet__buf__simple.md) bt\_mesh\_health\_cli::pub\_buf |
| --- |

Publication buffer.

## [◆ ](#a103d110c6cccd69a9e48619668fc60bc)pub\_data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_health\_cli::pub\_data[[BT\_MESH\_MODEL\_BUF\_LEN](group__bt__mesh__msg.md#ga5352d6fa05808722eba8a76e2446eddb)([BT\_MESH\_MODEL\_OP\_2](group__bt__mesh__access.md#gaa52a40ef5972c4f34cf5ff5a10e21289)(0x80, 0x32), 3)] |
| --- |

Publication data.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[health\_cli.h](health__cli_8h_source.md)

- [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
