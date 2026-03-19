---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structhttp__response__ctx.html
original_path: doxygen/html/structhttp__response__ctx.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

http\_response\_ctx Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [HTTP server API](group__http__server.md)

HTTP response context.
[More...](#details)

`#include <[server.h](server_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [http\_status](group__http__status__codes.md#gabc3b93f68c8bdd857ad32913628dfa8d) | [status](#ada151e7a981885622a79a5ae1f12b2e9) |
| const struct [http\_header](structhttp__header.md) \* | [headers](#a63acf00d5ff891ab51107458c545399d) |
|  | HTTP status code to include in response. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [header\_count](#a7a7b446baf1a1ab343437ee527ddde95) |
|  | Array of HTTP headers. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [body](#aa027d1577dd19db43a17cdd0959b8e39) |
|  | Length of headers array. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [body\_len](#a88b128e354c85f574409abd55633d2e2) |
|  | Pointer to body data. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [final\_chunk](#a53162ff65b66567b31ec323558bc1fe2) |
|  | Length of body data. |

## Detailed Description

HTTP response context.

## Field Documentation

## [◆ ](#aa027d1577dd19db43a17cdd0959b8e39)body

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* http\_response\_ctx::body |
| --- |

Length of headers array.

## [◆ ](#a88b128e354c85f574409abd55633d2e2)body\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) http\_response\_ctx::body\_len |
| --- |

Pointer to body data.

## [◆ ](#a53162ff65b66567b31ec323558bc1fe2)final\_chunk

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) http\_response\_ctx::final\_chunk |
| --- |

Length of body data.

## [◆ ](#a7a7b446baf1a1ab343437ee527ddde95)header\_count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) http\_response\_ctx::header\_count |
| --- |

Array of HTTP headers.

## [◆ ](#a63acf00d5ff891ab51107458c545399d)headers

| const struct [http\_header](structhttp__header.md)\* http\_response\_ctx::headers |
| --- |

HTTP status code to include in response.

## [◆ ](#ada151e7a981885622a79a5ae1f12b2e9)status

| enum [http\_status](group__http__status__codes.md#gabc3b93f68c8bdd857ad32913628dfa8d) http\_response\_ctx::status |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/http/[server.h](server_8h_source.md)

- [http\_response\_ctx](structhttp__response__ctx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
