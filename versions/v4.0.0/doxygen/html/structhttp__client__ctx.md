---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structhttp__client__ctx.html
original_path: doxygen/html/structhttp__client__ctx.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

http\_client\_ctx Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [HTTP server API](group__http__server.md)

Representation of an HTTP client connected to the server.
[More...](#details)

`#include <[server.h](server_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int | [fd](#ab8d3ab7b98549e796e0ead8be60fedf5) |
|  | Socket descriptor associated with the server. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char | [buffer](#aca9893deabb995cb3b3099ba1711be63) [HTTP\_SERVER\_CLIENT\_BUFFER\_SIZE] |
|  | Client data buffer. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char \* | [cursor](#a27b7c773f250aaeff9cdcd5dab063376) |
|  | Cursor indicating currently processed byte. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [data\_len](#afe23c7fb1638a7822d6c2ff6b3c9d167) |
|  | Data left to process in the buffer. |
| int | [window\_size](#a35e9a23972eb02fabe6c62333bd11f0d) |
|  | Connection-level window size. |
| enum http\_server\_state | [server\_state](#a62c8f1d67b941a1e4cdc61b3a7aa9ffd) |
|  | Server state for the associated client. |
| struct [http2\_frame](structhttp2__frame.md) | [current\_frame](#acce3d5cefa58cbeed5b96c4f4a1a0406) |
|  | Currently processed HTTP/2 frame. |
| struct [http\_resource\_detail](structhttp__resource__detail.md) \* | [current\_detail](#a71ee18a5fa2250a01d9c732579a72314) |
|  | Currently processed resource detail. |
| struct [http2\_stream\_ctx](structhttp2__stream__ctx.md) \* | [current\_stream](#ad33d0a5a5b9176cf14b4115726e04448) |
|  | Currently processed stream. |
| struct [http\_hpack\_header\_buf](structhttp__hpack__header__buf.md) | [header\_field](#a6d8fb0fcde6d28b9f5dccd50f2b07b62) |
|  | HTTP/2 header parser context. |
| struct [http2\_stream\_ctx](structhttp2__stream__ctx.md) | [streams](#a0695be4e93cb09472692dfc2f2e9a138) [HTTP\_SERVER\_MAX\_STREAMS] |
|  | HTTP/2 streams context. |
| struct [http\_parser\_settings](structhttp__parser__settings.md) | [parser\_settings](#a1d18988c23f3207d8fcdc1f0fff8bc98) |
|  | HTTP/1 parser configuration. |
| struct [http\_parser](structhttp__parser.md) | [parser](#a4d91f65c886527e68c1251b7eb0f3847) |
|  | HTTP/1 parser context. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char | [url\_buffer](#a9aa78096102e35f58a14070eb9b35ac1) [HTTP\_SERVER\_MAX\_URL\_LENGTH] |
|  | Request URL. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char | [content\_type](#aa9d3f794bc8925d378dfc8cef74d6ae4) [HTTP\_SERVER\_MAX\_CONTENT\_TYPE\_LEN] |
|  | Request content type. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char | [header\_buffer](#a9fc3585221866815823264083b1ad2e5) [HTTP\_SERVER\_MAX\_HEADER\_LEN] |
|  | Temp buffer for currently processed header (HTTP/1 only). |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [content\_len](#aca2c3fae568ad984d90646e6b543b959) |
|  | Request content length. |
| enum [http\_method](group__http__methods.md#gaacd5f203e33ac338ca5cb8f02a3ff3b8) | [method](#ab0695811450793361bc88ca0bb582c15) |
|  | Request method. |
| enum http1\_parser\_state | [parser\_state](#a4486489bf6043c98aac83a2ff33d1bc0) |
|  | HTTP/1 parser state. |
| int | [http1\_frag\_data\_len](#a4fb9cbcf7c631ccf2625c8625a484b49) |
|  | Length of the payload length in the currently processed request fragment (HTTP/1 only). |
| struct [k\_work\_delayable](structk__work__delayable.md) | [inactivity\_timer](#a0c4c06035d6de735b15d8a3ce6694eac) |
|  | Client inactivity timer. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [preface\_sent](#aab71d232273c8bb6374b44d15614a7e1): 1 |
|  | Flag indicating that HTTP2 preface was sent. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [http1\_headers\_sent](#ac805cda657ee679d5ccbf80fcc6007b2): 1 |
|  | Flag indicating that HTTP1 headers were sent. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [has\_upgrade\_header](#ae8fe0bf1dd0e5015b077a01f01fa40e9): 1 |
|  | Flag indicating that upgrade header was present in the request. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [http2\_upgrade](#afcc28f111655bab47516d2e71468bc55): 1 |
|  | Flag indicating HTTP/2 upgrade takes place. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [websocket\_upgrade](#ae20c4d4038a643bef49dbb77b497e7b1): 1 |
|  | Flag indicating Websocket upgrade takes place. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [websocket\_sec\_key\_next](#a56f376d84aadb40a914b1f52e1216cc6): 1 |
|  | Flag indicating Websocket key is being processed. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [expect\_continuation](#a4ae7f83d0e28944a2bcc858d096cb620): 1 |
|  | The next frame on the stream is expectd to be a continuation frame. |

## Detailed Description

Representation of an HTTP client connected to the server.

## Field Documentation

## [◆ ](#aca9893deabb995cb3b3099ba1711be63)buffer

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char http\_client\_ctx::buffer[HTTP\_SERVER\_CLIENT\_BUFFER\_SIZE] |
| --- |

Client data buffer.

## [◆ ](#aca2c3fae568ad984d90646e6b543b959)content\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) http\_client\_ctx::content\_len |
| --- |

Request content length.

## [◆ ](#aa9d3f794bc8925d378dfc8cef74d6ae4)content\_type

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char http\_client\_ctx::content\_type[HTTP\_SERVER\_MAX\_CONTENT\_TYPE\_LEN] |
| --- |

Request content type.

## [◆ ](#a71ee18a5fa2250a01d9c732579a72314)current\_detail

| struct [http\_resource\_detail](structhttp__resource__detail.md)\* http\_client\_ctx::current\_detail |
| --- |

Currently processed resource detail.

## [◆ ](#acce3d5cefa58cbeed5b96c4f4a1a0406)current\_frame

| struct [http2\_frame](structhttp2__frame.md) http\_client\_ctx::current\_frame |
| --- |

Currently processed HTTP/2 frame.

## [◆ ](#ad33d0a5a5b9176cf14b4115726e04448)current\_stream

| struct [http2\_stream\_ctx](structhttp2__stream__ctx.md)\* http\_client\_ctx::current\_stream |
| --- |

Currently processed stream.

## [◆ ](#a27b7c773f250aaeff9cdcd5dab063376)cursor

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char\* http\_client\_ctx::cursor |
| --- |

Cursor indicating currently processed byte.

## [◆ ](#afe23c7fb1638a7822d6c2ff6b3c9d167)data\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) http\_client\_ctx::data\_len |
| --- |

Data left to process in the buffer.

## [◆ ](#a4ae7f83d0e28944a2bcc858d096cb620)expect\_continuation

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) http\_client\_ctx::expect\_continuation |
| --- |

The next frame on the stream is expectd to be a continuation frame.

## [◆ ](#ab8d3ab7b98549e796e0ead8be60fedf5)fd

| int http\_client\_ctx::fd |
| --- |

Socket descriptor associated with the server.

## [◆ ](#ae8fe0bf1dd0e5015b077a01f01fa40e9)has\_upgrade\_header

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) http\_client\_ctx::has\_upgrade\_header |
| --- |

Flag indicating that upgrade header was present in the request.

## [◆ ](#a9fc3585221866815823264083b1ad2e5)header\_buffer

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char http\_client\_ctx::header\_buffer[HTTP\_SERVER\_MAX\_HEADER\_LEN] |
| --- |

Temp buffer for currently processed header (HTTP/1 only).

## [◆ ](#a6d8fb0fcde6d28b9f5dccd50f2b07b62)header\_field

| struct [http\_hpack\_header\_buf](structhttp__hpack__header__buf.md) http\_client\_ctx::header\_field |
| --- |

HTTP/2 header parser context.

## [◆ ](#a4fb9cbcf7c631ccf2625c8625a484b49)http1\_frag\_data\_len

| int http\_client\_ctx::http1\_frag\_data\_len |
| --- |

Length of the payload length in the currently processed request fragment (HTTP/1 only).

## [◆ ](#ac805cda657ee679d5ccbf80fcc6007b2)http1\_headers\_sent

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) http\_client\_ctx::http1\_headers\_sent |
| --- |

Flag indicating that HTTP1 headers were sent.

## [◆ ](#afcc28f111655bab47516d2e71468bc55)http2\_upgrade

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) http\_client\_ctx::http2\_upgrade |
| --- |

Flag indicating HTTP/2 upgrade takes place.

## [◆ ](#a0c4c06035d6de735b15d8a3ce6694eac)inactivity\_timer

| struct [k\_work\_delayable](structk__work__delayable.md) http\_client\_ctx::inactivity\_timer |
| --- |

Client inactivity timer.

The client connection is closed by the server when it expires.

## [◆ ](#ab0695811450793361bc88ca0bb582c15)method

| enum [http\_method](group__http__methods.md#gaacd5f203e33ac338ca5cb8f02a3ff3b8) http\_client\_ctx::method |
| --- |

Request method.

## [◆ ](#a4d91f65c886527e68c1251b7eb0f3847)parser

| struct [http\_parser](structhttp__parser.md) http\_client\_ctx::parser |
| --- |

HTTP/1 parser context.

## [◆ ](#a1d18988c23f3207d8fcdc1f0fff8bc98)parser\_settings

| struct [http\_parser\_settings](structhttp__parser__settings.md) http\_client\_ctx::parser\_settings |
| --- |

HTTP/1 parser configuration.

## [◆ ](#a4486489bf6043c98aac83a2ff33d1bc0)parser\_state

| enum http1\_parser\_state http\_client\_ctx::parser\_state |
| --- |

HTTP/1 parser state.

## [◆ ](#aab71d232273c8bb6374b44d15614a7e1)preface\_sent

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) http\_client\_ctx::preface\_sent |
| --- |

Flag indicating that HTTP2 preface was sent.

## [◆ ](#a62c8f1d67b941a1e4cdc61b3a7aa9ffd)server\_state

| enum http\_server\_state http\_client\_ctx::server\_state |
| --- |

Server state for the associated client.

## [◆ ](#a0695be4e93cb09472692dfc2f2e9a138)streams

| struct [http2\_stream\_ctx](structhttp2__stream__ctx.md) http\_client\_ctx::streams[HTTP\_SERVER\_MAX\_STREAMS] |
| --- |

HTTP/2 streams context.

## [◆ ](#a9aa78096102e35f58a14070eb9b35ac1)url\_buffer

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char http\_client\_ctx::url\_buffer[HTTP\_SERVER\_MAX\_URL\_LENGTH] |
| --- |

Request URL.

## [◆ ](#a56f376d84aadb40a914b1f52e1216cc6)websocket\_sec\_key\_next

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) http\_client\_ctx::websocket\_sec\_key\_next |
| --- |

Flag indicating Websocket key is being processed.

## [◆ ](#ae20c4d4038a643bef49dbb77b497e7b1)websocket\_upgrade

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) http\_client\_ctx::websocket\_upgrade |
| --- |

Flag indicating Websocket upgrade takes place.

## [◆ ](#a35e9a23972eb02fabe6c62333bd11f0d)window\_size

| int http\_client\_ctx::window\_size |
| --- |

Connection-level window size.

---

The documentation for this struct was generated from the following file:

- zephyr/net/http/[server.h](server_8h_source.md)

- [http\_client\_ctx](structhttp__client__ctx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
