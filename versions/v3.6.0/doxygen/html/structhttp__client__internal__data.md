---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structhttp__client__internal__data.html
original_path: doxygen/html/structhttp__client__internal__data.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

http\_client\_internal\_data Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [HTTP client API](group__http__client.md)

HTTP client internal data that the application should not touch.
[More...](#details)

`#include <[client.h](client_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [http\_parser](structhttp__parser.md) | [parser](#a1620ae6631414c3ba5e462d97deca157) |
|  | HTTP parser context. |
| struct [http\_parser\_settings](structhttp__parser__settings.md) | [parser\_settings](#a19876ea20cdca3a016d6e260e2795e83) |
|  | HTTP parser settings. |
| struct [http\_response](structhttp__response.md) | [response](#aa132cb0366969c04250f64075866227c) |
|  | HTTP response specific data (filled by [http\_client\_req()](group__http__client.md#gaa38b6efb03f88d6959273a41b6acac81 "Do a HTTP request.") when data is received). |
| void \* | [user\_data](#a330102d665b6601949eb7331ab45d517) |
|  | User data. |
| int | [sock](#a8486d8e8b64474e75cadeb9fb166a4a5) |
|  | HTTP socket. |

## Detailed Description

HTTP client internal data that the application should not touch.

## Field Documentation

## [◆ ](#a1620ae6631414c3ba5e462d97deca157)parser

| struct [http\_parser](structhttp__parser.md) http\_client\_internal\_data::parser |
| --- |

HTTP parser context.

## [◆ ](#a19876ea20cdca3a016d6e260e2795e83)parser\_settings

| struct [http\_parser\_settings](structhttp__parser__settings.md) http\_client\_internal\_data::parser\_settings |
| --- |

HTTP parser settings.

## [◆ ](#aa132cb0366969c04250f64075866227c)response

| struct [http\_response](structhttp__response.md) http\_client\_internal\_data::response |
| --- |

HTTP response specific data (filled by [http\_client\_req()](group__http__client.md#gaa38b6efb03f88d6959273a41b6acac81 "Do a HTTP request.") when data is received).

## [◆ ](#a8486d8e8b64474e75cadeb9fb166a4a5)sock

| int http\_client\_internal\_data::sock |
| --- |

HTTP socket.

## [◆ ](#a330102d665b6601949eb7331ab45d517)user\_data

| void\* http\_client\_internal\_data::user\_data |
| --- |

User data.

---

The documentation for this struct was generated from the following file:

- zephyr/net/http/[client.h](client_8h_source.md)

- [http\_client\_internal\_data](structhttp__client__internal__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
