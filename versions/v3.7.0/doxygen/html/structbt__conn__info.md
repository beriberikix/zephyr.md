---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__conn__info.html
original_path: doxygen/html/structbt__conn__info.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

Connection Info Structure.
[More...](#details)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [bt\_conn\_type](group__bt__conn.md#gab8dde20ae75b51f1e28dbeed06001f20) | [type](#a7995e1291be494b5bdf860eceea0cad1) |
|  | Connection Type. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [role](#a8237b8c1bb9a97a174d04cbe13dca7c7) |
|  | Connection Role. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [id](#a3a4e24519b5d3ba547423e53c4d92a5c) |
|  | Which local identity the connection was created with. |
| union { |  |
| struct [bt\_conn\_le\_info](structbt__conn__le__info.md)   [le](#a6b536e7732dcf7b77a7bc05116dca548) |  |
|  | LE Connection specific Info. [More...](#a6b536e7732dcf7b77a7bc05116dca548) |
| struct [bt\_conn\_br\_info](structbt__conn__br__info.md)   [br](#a799e59d3a85625799a32ac3f0b3d67d1) |  |
|  | BR/EDR Connection specific Info. [More...](#a799e59d3a85625799a32ac3f0b3d67d1) |
| }; |  |
|  | Connection Type specific Info. |
| enum [bt\_conn\_state](group__bt__conn.md#ga9442c1479db60e2db40a2ea6de565282) | [state](#ae566e2382b69ff27314dc1dd632dbdbc) |
|  | Connection state. |
| struct [bt\_security\_info](structbt__security__info.md) | [security](#ae4405f1b4f3fe2ff6253453964860931) |
|  | Security specific info. |

## Detailed Description

Connection Info Structure.

## Field Documentation

## [◆ ](#a2c398fd6e9ea2585a366c22f07f0ab7b)[union]

| union { ... } [bt\_conn\_info](structbt__conn__info.md) |
| --- |

Connection Type specific Info.

## [◆ ](#a799e59d3a85625799a32ac3f0b3d67d1)br

| struct [bt\_conn\_br\_info](structbt__conn__br__info.md) bt\_conn\_info::br |
| --- |

BR/EDR Connection specific Info.

## [◆ ](#a3a4e24519b5d3ba547423e53c4d92a5c)id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_info::id |
| --- |

Which local identity the connection was created with.

## [◆ ](#a6b536e7732dcf7b77a7bc05116dca548)le

| struct [bt\_conn\_le\_info](structbt__conn__le__info.md) bt\_conn\_info::le |
| --- |

LE Connection specific Info.

## [◆ ](#a8237b8c1bb9a97a174d04cbe13dca7c7)role

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_info::role |
| --- |

Connection Role.

## [◆ ](#ae4405f1b4f3fe2ff6253453964860931)security

| struct [bt\_security\_info](structbt__security__info.md) bt\_conn\_info::security |
| --- |

Security specific info.

## [◆ ](#ae566e2382b69ff27314dc1dd632dbdbc)state

| enum [bt\_conn\_state](group__bt__conn.md#ga9442c1479db60e2db40a2ea6de565282) bt\_conn\_info::state |
| --- |

Connection state.

## [◆ ](#a7995e1291be494b5bdf860eceea0cad1)type

| enum [bt\_conn\_type](group__bt__conn.md#gab8dde20ae75b51f1e28dbeed06001f20) bt\_conn\_info::type |
| --- |

Connection Type.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_info](structbt__conn__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
