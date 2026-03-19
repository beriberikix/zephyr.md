---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structhttp__request__ctx.html
original_path: doxygen/html/structhttp__request__ctx.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

http\_request\_ctx Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [HTTP server API](group__http__server.md)

HTTP request context.
[More...](#details)

`#include <[server.h](server_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [data](#aae773946b597bb7ca70d071daadf3c1d) |
|  | HTTP request data. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [data\_len](#a4de5c3114220bef60bcd587f4796603e) |
|  | Length of HTTP request data. |
| struct [http\_header](structhttp__header.md) \* | [headers](#a9500727563dd6f33663c0a26299a16a6) |
|  | Array of HTTP request headers. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [header\_count](#a404ff7f9946f162dc0ef6c0a872bf88b) |
|  | Array length of HTTP request headers. |
| enum [http\_header\_status](group__http__server.md#ga6c15e872ece1b9a740b6dca3974101b3) | [headers\_status](#a312cc4db494a0415a2c0342183b3a3c6) |
|  | Status of HTTP request headers. |

## Detailed Description

HTTP request context.

## Field Documentation

## [◆ ](#aae773946b597bb7ca70d071daadf3c1d)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* http\_request\_ctx::data |
| --- |

HTTP request data.

## [◆ ](#a4de5c3114220bef60bcd587f4796603e)data\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) http\_request\_ctx::data\_len |
| --- |

Length of HTTP request data.

## [◆ ](#a404ff7f9946f162dc0ef6c0a872bf88b)header\_count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) http\_request\_ctx::header\_count |
| --- |

Array length of HTTP request headers.

## [◆ ](#a9500727563dd6f33663c0a26299a16a6)headers

| struct [http\_header](structhttp__header.md)\* http\_request\_ctx::headers |
| --- |

Array of HTTP request headers.

## [◆ ](#a312cc4db494a0415a2c0342183b3a3c6)headers\_status

| enum [http\_header\_status](group__http__server.md#ga6c15e872ece1b9a740b6dca3974101b3) http\_request\_ctx::headers\_status |
| --- |

Status of HTTP request headers.

---

The documentation for this struct was generated from the following file:

- zephyr/net/http/[server.h](server_8h_source.md)

- [http\_request\_ctx](structhttp__request__ctx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
