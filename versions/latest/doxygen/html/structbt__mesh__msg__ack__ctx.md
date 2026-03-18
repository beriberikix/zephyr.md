---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__mesh__msg__ack__ctx.html
original_path: doxygen/html/structbt__mesh__msg__ack__ctx.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_msg\_ack\_ctx Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Message](group__bt__mesh__msg.md)

Acknowledged message context for tracking the status of model messages pending a response.
[More...](#details)

`#include <[msg.h](msg_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct k\_sem | [sem](#a53ce3e10f27da773c227de6d6eaba5e3) |
|  | Sync semaphore. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [op](#a08f50fcae687026c45d891c9381bd9c2) |
|  | Opcode we're waiting for. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [dst](#ac83626299e197dbd0a9a36a6617c3b21) |
|  | Address of the node that should respond. |
| void \* | [user\_data](#a510baede03d53b2419ade8da6d02fa10) |
|  | User specific parameter. |

## Detailed Description

Acknowledged message context for tracking the status of model messages pending a response.

## Field Documentation

## [◆ ](#ac83626299e197dbd0a9a36a6617c3b21)dst

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_msg\_ack\_ctx::dst |
| --- |

Address of the node that should respond.

## [◆ ](#a08f50fcae687026c45d891c9381bd9c2)op

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_msg\_ack\_ctx::op |
| --- |

Opcode we're waiting for.

## [◆ ](#a53ce3e10f27da773c227de6d6eaba5e3)sem

| struct k\_sem bt\_mesh\_msg\_ack\_ctx::sem |
| --- |

Sync semaphore.

## [◆ ](#a510baede03d53b2419ade8da6d02fa10)user\_data

| void\* bt\_mesh\_msg\_ack\_ctx::user\_data |
| --- |

User specific parameter.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[msg.h](msg_8h_source.md)

- [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
