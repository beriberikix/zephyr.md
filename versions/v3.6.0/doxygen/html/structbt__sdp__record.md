---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__sdp__record.html
original_path: doxygen/html/structbt__sdp__record.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_sdp\_record Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Service Discovery Protocol (SDP)](group__bt__sdp.md)

SDP Service Record Value.
[More...](#details)

`#include <[sdp.h](sdp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [handle](#ae94becbbce55a43661ef0c563e314b6b) |
|  | Redundant, for quick ref. |
| struct [bt\_sdp\_attribute](structbt__sdp__attribute.md) \* | [attrs](#ad8ee5b17c45ca32696a492bc9c62d4fd) |
|  | Base addr of attr array. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [attr\_count](#a2bbcb54c385f88d512c1ccd4cf5e05ff) |
|  | Number of attributes. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [index](#ad54ca76a96964df3a6ac909eb54274df) |
|  | Index of the record in LL. |
| struct [bt\_sdp\_record](structbt__sdp__record.md) \* | [next](#ab1e1b5a630a62ca892b7ff0bb7a00eea) |
|  | Next service record. |

## Detailed Description

SDP Service Record Value.

## Field Documentation

## [◆ ](#a2bbcb54c385f88d512c1ccd4cf5e05ff)attr\_count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_sdp\_record::attr\_count |
| --- |

Number of attributes.

## [◆ ](#ad8ee5b17c45ca32696a492bc9c62d4fd)attrs

| struct [bt\_sdp\_attribute](structbt__sdp__attribute.md)\* bt\_sdp\_record::attrs |
| --- |

Base addr of attr array.

## [◆ ](#ae94becbbce55a43661ef0c563e314b6b)handle

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_sdp\_record::handle |
| --- |

Redundant, for quick ref.

## [◆ ](#ad54ca76a96964df3a6ac909eb54274df)index

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_sdp\_record::index |
| --- |

Index of the record in LL.

## [◆ ](#ab1e1b5a630a62ca892b7ff0bb7a00eea)next

| struct [bt\_sdp\_record](structbt__sdp__record.md)\* bt\_sdp\_record::next |
| --- |

Next service record.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[sdp.h](sdp_8h_source.md)

- [bt\_sdp\_record](structbt__sdp__record.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
