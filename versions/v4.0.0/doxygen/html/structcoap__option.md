---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structcoap__option.html
original_path: doxygen/html/structcoap__option.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coap\_option Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [COAP Library](group__coap.md)

Representation of a CoAP option.
[More...](#details)

`#include <[coap.h](coap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [delta](#abca15b0a8f9bdcb3f493ab3801d4b58f) |
|  | Option delta. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [len](#a01c8abdf27c3f8c5a816af33c0c093d4) |
|  | Option length. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [value](#aff07b5d3673169b6316b91dc27780891) [12] |
|  | Option value. |

## Detailed Description

Representation of a CoAP option.

## Field Documentation

## [◆ ](#abca15b0a8f9bdcb3f493ab3801d4b58f)delta

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) coap\_option::delta |
| --- |

Option delta.

## [◆ ](#a01c8abdf27c3f8c5a816af33c0c093d4)len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) coap\_option::len |
| --- |

Option length.

## [◆ ](#aff07b5d3673169b6316b91dc27780891)value

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) coap\_option::value[12] |
| --- |

Option value.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[coap.h](coap_8h_source.md)

- [coap\_option](structcoap__option.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
