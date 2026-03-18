---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structwifi__mode__info.html
original_path: doxygen/html/structwifi__mode__info.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_mode\_info Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

Wi-Fi mode setup.
[More...](#details)

`#include <[wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mode](#aa29d3b88fc718aa3ac05daf38974707d) |
|  | Mode setting for a specific mode of operation. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [if\_index](#add58dd3b45fd2ddaf684d1b0de81bef9) |
|  | Interface index. |
| enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) | [oper](#a57c101db8b81ab0ac5dd0a158057a64a) |
|  | Get or set operation. |

## Detailed Description

Wi-Fi mode setup.

## Field Documentation

## [◆ ](#add58dd3b45fd2ddaf684d1b0de81bef9)if\_index

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_mode\_info::if\_index |
| --- |

Interface index.

## [◆ ](#aa29d3b88fc718aa3ac05daf38974707d)mode

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_mode\_info::mode |
| --- |

Mode setting for a specific mode of operation.

## [◆ ](#a57c101db8b81ab0ac5dd0a158057a64a)oper

| enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) wifi\_mode\_info::oper |
| --- |

Get or set operation.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [wifi\_mode\_info](structwifi__mode__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
