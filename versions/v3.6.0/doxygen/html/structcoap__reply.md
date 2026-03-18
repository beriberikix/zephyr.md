---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structcoap__reply.html
original_path: doxygen/html/structcoap__reply.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coap\_reply Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [COAP Library](group__coap.md)

Represents the handler for the reply of a request, it is also used when observing resources.
[More...](#details)

`#include <[coap.h](coap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [coap\_reply\_t](group__coap.md#ga556deaf757f3047eefc2f032d0d7e0bc) | [reply](#a6a888bbb5652761002ce26aba09352cc) |
| void \* | [user\_data](#aa951d9ba4eb7f8041e8e82df9c1401dc) |
| int | [age](#aea6b98e109e270c08df1554c5eee65fe) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [id](#a94d17732056de3d8ecb3412c686091f8) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [token](#a18d40c327933c30681b924446c21ea9d) [8] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tkl](#a038ccb29c2abff6168db3247241a8cc3) |

## Detailed Description

Represents the handler for the reply of a request, it is also used when observing resources.

## Field Documentation

## [◆ ](#aea6b98e109e270c08df1554c5eee65fe)age

| int coap\_reply::age |
| --- |

## [◆ ](#a94d17732056de3d8ecb3412c686091f8)id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) coap\_reply::id |
| --- |

## [◆ ](#a6a888bbb5652761002ce26aba09352cc)reply

| [coap\_reply\_t](group__coap.md#ga556deaf757f3047eefc2f032d0d7e0bc) coap\_reply::reply |
| --- |

## [◆ ](#a038ccb29c2abff6168db3247241a8cc3)tkl

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) coap\_reply::tkl |
| --- |

## [◆ ](#a18d40c327933c30681b924446c21ea9d)token

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) coap\_reply::token[8] |
| --- |

## [◆ ](#aa951d9ba4eb7f8041e8e82df9c1401dc)user\_data

| void\* coap\_reply::user\_data |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[coap.h](coap_8h_source.md)

- [coap\_reply](structcoap__reply.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
