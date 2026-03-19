---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structhttp2__stream__ctx.html
original_path: doxygen/html/structhttp2__stream__ctx.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

http2\_stream\_ctx Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [HTTP server API](group__http__server.md)

HTTP/2 stream representation.
[More...](#details)

`#include <[server.h](server_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int | [stream\_id](#ad1b194318758f888b8218b0fd056dca7) |
|  | Stream identifier. |
| enum http2\_stream\_state | [stream\_state](#a61a05b72b578b1bae6806fc6ad125caa) |
|  | Stream state. |
| int | [window\_size](#a96a3a7ebdede35b4e925116c4d784279) |
|  | Stream-level window size. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [headers\_sent](#a4b8cc2fa54a3c8161a8085bf4ec8d70b): 1 |
|  | Flag indicating that headers were sent in the reply. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [end\_stream\_sent](#af94d72e8ed02699cefc08d92e58825b6): 1 |
|  | Flag indicating that END\_STREAM flag was sent. |

## Detailed Description

HTTP/2 stream representation.

## Field Documentation

## [◆ ](#af94d72e8ed02699cefc08d92e58825b6)end\_stream\_sent

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) http2\_stream\_ctx::end\_stream\_sent |
| --- |

Flag indicating that END\_STREAM flag was sent.

## [◆ ](#a4b8cc2fa54a3c8161a8085bf4ec8d70b)headers\_sent

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) http2\_stream\_ctx::headers\_sent |
| --- |

Flag indicating that headers were sent in the reply.

## [◆ ](#ad1b194318758f888b8218b0fd056dca7)stream\_id

| int http2\_stream\_ctx::stream\_id |
| --- |

Stream identifier.

## [◆ ](#a61a05b72b578b1bae6806fc6ad125caa)stream\_state

| enum http2\_stream\_state http2\_stream\_ctx::stream\_state |
| --- |

Stream state.

## [◆ ](#a96a3a7ebdede35b4e925116c4d784279)window\_size

| int http2\_stream\_ctx::window\_size |
| --- |

Stream-level window size.

---

The documentation for this struct was generated from the following file:

- zephyr/net/http/[server.h](server_8h_source.md)

- [http2\_stream\_ctx](structhttp2__stream__ctx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
