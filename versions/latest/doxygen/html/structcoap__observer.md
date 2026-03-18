---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structcoap__observer.html
original_path: doxygen/html/structcoap__observer.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coap\_observer Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [COAP Library](group__coap.md)

Represents a remote device that is observing a local resource.
[More...](#details)

`#include <[coap.h](coap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [list](#a24a9f853db17ff623f4c510fd0892eb5) |
| struct [sockaddr](structsockaddr.md) | [addr](#a9b6f807a0fc5d141e0ee3dd9596c3c82) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [token](#a6d7d792120b935bf61c739f95dd7361c) [8] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tkl](#a901f148d2eb697206fde732050c3d8b4) |

## Detailed Description

Represents a remote device that is observing a local resource.

## Field Documentation

## [◆ ](#a9b6f807a0fc5d141e0ee3dd9596c3c82)addr

| struct [sockaddr](structsockaddr.md) coap\_observer::addr |
| --- |

## [◆ ](#a24a9f853db17ff623f4c510fd0892eb5)list

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) coap\_observer::list |
| --- |

## [◆ ](#a901f148d2eb697206fde732050c3d8b4)tkl

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) coap\_observer::tkl |
| --- |

## [◆ ](#a6d7d792120b935bf61c739f95dd7361c)token

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) coap\_observer::token[8] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[coap.h](coap_8h_source.md)

- [coap\_observer](structcoap__observer.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
