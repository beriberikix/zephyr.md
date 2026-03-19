---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/health__cli_8h.html
original_path: doxygen/html/health__cli_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

health\_cli.h File Reference

Health Client Model APIs.
[More...](#details)

`#include <[zephyr/bluetooth/mesh.h](mesh_8h_source.md)>`

[Go to the source code of this file.](health__cli_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) |
|  | Health Client Model Context. [More...](structbt__mesh__health__cli.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_HEALTH\_CLI](group__bt__mesh__health__cli.md#ga0f869fc7d19f5e8be5953a8ece6e07f6)(cli\_data) |
|  | Generic Health Client model composition data entry. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_health\_cli\_fault\_get](group__bt__mesh__health__cli.md#ga2951f45aaaee75f4c77c4381b1ddd617) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*test\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*faults, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*fault\_count) |
|  | Get the registered fault state for the given Company ID. |
| int | [bt\_mesh\_health\_cli\_fault\_clear](group__bt__mesh__health__cli.md#ga77cc4e97193cca60d79a8076f3761ef5) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*test\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*faults, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*fault\_count) |
|  | Clear the registered faults for the given Company ID. |
| int | [bt\_mesh\_health\_cli\_fault\_clear\_unack](group__bt__mesh__health__cli.md#gafb0a46136f82f1aff4273704f1c47ac4) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid) |
|  | Clear the registered faults for the given Company ID (unacked). |
| int | [bt\_mesh\_health\_cli\_fault\_test](group__bt__mesh__health__cli.md#ga00cef275cdf90876f1381ffaff04b25c) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) test\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*faults, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*fault\_count) |
|  | Invoke a self-test procedure for the given Company ID. |
| int | [bt\_mesh\_health\_cli\_fault\_test\_unack](group__bt__mesh__health__cli.md#ga8e58519ef78946e88258b335c350d754) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) test\_id) |
|  | Invoke a self-test procedure for the given Company ID (unacked). |
| int | [bt\_mesh\_health\_cli\_period\_get](group__bt__mesh__health__cli.md#ga1e8e25681b9fcbc6584a29336924a78a) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*divisor) |
|  | Get the target node's Health fast period divisor. |
| int | [bt\_mesh\_health\_cli\_period\_set](group__bt__mesh__health__cli.md#ga2ef46f0b5059a959d5b06d6e49c4f552) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) divisor, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*updated\_divisor) |
|  | Set the target node's Health fast period divisor. |
| int | [bt\_mesh\_health\_cli\_period\_set\_unack](group__bt__mesh__health__cli.md#ga536c631d87daaca017af078d49094fc1) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) divisor) |
|  | Set the target node's Health fast period divisor (unacknowledged). |
| int | [bt\_mesh\_health\_cli\_attention\_get](group__bt__mesh__health__cli.md#gad6f322f506b8577c56bb0613f7dcbd93) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*attention) |
|  | Get the current attention timer value. |
| int | [bt\_mesh\_health\_cli\_attention\_set](group__bt__mesh__health__cli.md#ga1b910d0849ce4c33d6de4bf1ff47ece8) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attention, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*updated\_attention) |
|  | Set the attention timer. |
| int | [bt\_mesh\_health\_cli\_attention\_set\_unack](group__bt__mesh__health__cli.md#ga3a528688e340edf49b4bd62317284834) (struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attention) |
|  | Set the attention timer (unacknowledged). |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [bt\_mesh\_health\_cli\_timeout\_get](group__bt__mesh__health__cli.md#ga9abc0db22da327d02d23371bba59b46a) (void) |
|  | Get the current transmission timeout value. |
| void | [bt\_mesh\_health\_cli\_timeout\_set](group__bt__mesh__health__cli.md#gaf3d54597a74a458df0053bd0599d39e9) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Set the transmission timeout value. |

## Detailed Description

Health Client Model APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [health\_cli.h](health__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
