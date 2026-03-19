---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structcoap__client__option.html
original_path: doxygen/html/structcoap__client__option.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coap\_client\_option Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [CoAP client API](group__coap__client.md)

Representation of extra options for the CoAP client request.
[More...](#details)

`#include <[coap_client.h](coap__client_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [code](#a3b0c23802edd7cbb162bff6cfb745bfb) |
|  | Option code. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [len](#aebc27705f851af910757f0bb2a73bbe5) |
|  | Option len. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [value](#ac1f5a38dad7ea227e19a96a3799329c6) [12] |
|  | Buffer for the length. |

## Detailed Description

Representation of extra options for the CoAP client request.

## Field Documentation

## [◆ ](#a3b0c23802edd7cbb162bff6cfb745bfb)code

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) coap\_client\_option::code |
| --- |

Option code.

## [◆ ](#aebc27705f851af910757f0bb2a73bbe5)len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) coap\_client\_option::len |
| --- |

Option len.

## [◆ ](#ac1f5a38dad7ea227e19a96a3799329c6)value

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) coap\_client\_option::value[12] |
| --- |

Buffer for the length.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[coap\_client.h](coap__client_8h_source.md)

- [coap\_client\_option](structcoap__client__option.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
