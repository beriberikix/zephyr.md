---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__model__op.html
original_path: doxygen/html/structbt__mesh__model__op.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_model\_op Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Access layer](group__bt__mesh__access.md)

Model opcode handler.
[More...](#details)

`#include <[access.h](access_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [opcode](#a09c18a889e08bc708b9dc623f8177e39) |
|  | OpCode encoded using the BT\_MESH\_MODEL\_OP\_\* macros. |
| const [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [len](#a25445fe2e937a321942c312bd675e486) |
|  | Message length. |
| int(\*const | [func](#a4a5de7a12f2f8743048aafc81af0cece) )(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Handler function for this opcode. |

## Detailed Description

Model opcode handler.

## Field Documentation

## [◆ ](#a4a5de7a12f2f8743048aafc81af0cece)func

| int(\*const bt\_mesh\_model\_op::func) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
| --- |

Handler function for this opcode.

Parameters
:   | model | Model instance receiving the message. |
    | --- | --- |
    | ctx | Message context for the message. |
    | buf | Message buffer containing the message payload, not including the opcode. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#a25445fe2e937a321942c312bd675e486)len

| const [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) bt\_mesh\_model\_op::len |
| --- |

Message length.

If the message has variable length then this value indicates minimum message length and should be positive. Handler function should verify precise length based on the contents of the message. If the message has fixed length then this value should be negative. Use BT\_MESH\_LEN\_\* macros when defining this value.

## [◆ ](#a09c18a889e08bc708b9dc623f8177e39)opcode

| const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_model\_op::opcode |
| --- |

OpCode encoded using the BT\_MESH\_MODEL\_OP\_\* macros.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[access.h](access_8h_source.md)

- [bt\_mesh\_model\_op](structbt__mesh__model__op.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
