---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structcoap__client__request.html
original_path: doxygen/html/structcoap__client__request.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coap\_client\_request Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [CoAP client API](group__coap__client.md)

Representation of a CoAP client request.
[More...](#details)

`#include <[coap_client.h](coap__client_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [coap\_method](group__coap.md#ga6a6547e3c755cf7a5033302c8294e0b7) | [method](#a308709b298a7449d32492ee1170a6791) |
|  | Method of the request. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [confirmable](#a4db33f53cd9723d5c073d379578e5a18) |
|  | CoAP Confirmable/Non-confirmable message. |
| const char \* | [path](#a51dfca3516d01d3881e80615456e05bd) |
|  | Path of the requested resource. |
| enum [coap\_content\_format](group__coap.md#ga94a8f9956742d3928fc3c63b8d01ae73) | [fmt](#ae0a506b0baef3133f8665a5c8799e8d3) |
|  | Content format to be used. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [payload](#aeda75b6fe9e523f7f3847d4c469b0632) |
|  | User allocated buffer for send request. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [len](#a04e7fd6614e0a4b0a0e78f5420019582) |
|  | Length of the payload. |
| [coap\_client\_response\_cb\_t](group__coap__client.md#ga0a33095a309016ddb4ff00206cfd4bb0) | [cb](#aefc85ec14f031aabe5ed0830d819069a) |
|  | Callback when response received. |
| struct [coap\_client\_option](structcoap__client__option.md) \* | [options](#ab2f777b35287169c3510fdd5be19d072) |
|  | Extra options to be added to request. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_options](#a03f9aec935feab0352254f2d425c59be) |
|  | Number of extra options. |
| void \* | [user\_data](#ad725d95c1745d19e74d3ed39710b10b4) |
|  | User provided context. |

## Detailed Description

Representation of a CoAP client request.

## Field Documentation

## [◆ ](#aefc85ec14f031aabe5ed0830d819069a)cb

| [coap\_client\_response\_cb\_t](group__coap__client.md#ga0a33095a309016ddb4ff00206cfd4bb0) coap\_client\_request::cb |
| --- |

Callback when response received.

## [◆ ](#a4db33f53cd9723d5c073d379578e5a18)confirmable

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) coap\_client\_request::confirmable |
| --- |

CoAP Confirmable/Non-confirmable message.

## [◆ ](#ae0a506b0baef3133f8665a5c8799e8d3)fmt

| enum [coap\_content\_format](group__coap.md#ga94a8f9956742d3928fc3c63b8d01ae73) coap\_client\_request::fmt |
| --- |

Content format to be used.

## [◆ ](#a04e7fd6614e0a4b0a0e78f5420019582)len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) coap\_client\_request::len |
| --- |

Length of the payload.

## [◆ ](#a308709b298a7449d32492ee1170a6791)method

| enum [coap\_method](group__coap.md#ga6a6547e3c755cf7a5033302c8294e0b7) coap\_client\_request::method |
| --- |

Method of the request.

## [◆ ](#a03f9aec935feab0352254f2d425c59be)num\_options

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) coap\_client\_request::num\_options |
| --- |

Number of extra options.

## [◆ ](#ab2f777b35287169c3510fdd5be19d072)options

| struct [coap\_client\_option](structcoap__client__option.md)\* coap\_client\_request::options |
| --- |

Extra options to be added to request.

## [◆ ](#a51dfca3516d01d3881e80615456e05bd)path

| const char\* coap\_client\_request::path |
| --- |

Path of the requested resource.

## [◆ ](#aeda75b6fe9e523f7f3847d4c469b0632)payload

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* coap\_client\_request::payload |
| --- |

User allocated buffer for send request.

## [◆ ](#ad725d95c1745d19e74d3ed39710b10b4)user\_data

| void\* coap\_client\_request::user\_data |
| --- |

User provided context.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[coap\_client.h](coap__client_8h_source.md)

- [coap\_client\_request](structcoap__client__request.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
