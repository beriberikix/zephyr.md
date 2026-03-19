---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structwifi__channel__info.html
original_path: doxygen/html/structwifi__channel__info.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_channel\_info Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

Wi-Fi channel setting for monitor and TX-injection modes.
[More...](#details)

`#include <[wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [channel](#a799cbc0a67764f6680322ba0f2ad3300) |
|  | Channel value to set. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [if\_index](#a43a7dd8c19d0c6540e3cc0b5d1d6165d) |
|  | Interface index. |
| enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) | [oper](#aa8ef8a71b49ead3664fff9a4d61b1ce8) |
|  | Get or set operation. |

## Detailed Description

Wi-Fi channel setting for monitor and TX-injection modes.

## Field Documentation

## [◆ ](#a799cbc0a67764f6680322ba0f2ad3300)channel

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) wifi\_channel\_info::channel |
| --- |

Channel value to set.

## [◆ ](#a43a7dd8c19d0c6540e3cc0b5d1d6165d)if\_index

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_channel\_info::if\_index |
| --- |

Interface index.

## [◆ ](#aa8ef8a71b49ead3664fff9a4d61b1ce8)oper

| enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) wifi\_channel\_info::oper |
| --- |

Get or set operation.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [wifi\_channel\_info](structwifi__channel__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
