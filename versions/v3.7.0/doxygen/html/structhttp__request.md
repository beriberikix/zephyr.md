---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structhttp__request.html
original_path: doxygen/html/structhttp__request.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

http\_request Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [HTTP client API](group__http__client.md)

HTTP client request.
[More...](#details)

`#include <[client.h](client_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [http\_client\_internal\_data](structhttp__client__internal__data.md) | [internal](#abb86ccd0e0801c278ef37a78a4b7a958) |
|  | HTTP client request internal data. |
| enum [http\_method](group__http__methods.md#gaacd5f203e33ac338ca5cb8f02a3ff3b8) | [method](#adbfcd3bcaf57205360bad957a13999e6) |
|  | The HTTP method: GET, HEAD, OPTIONS, POST, ... |
| [http\_response\_cb\_t](group__http__client.md#ga9e079c737c325ee21a57e615b641f21a) | [response](#aba8bf528f3e279d55662eedc9168d25c) |
|  | User supplied callback function to call when response is received. |
| const struct [http\_parser\_settings](structhttp__parser__settings.md) \* | [http\_cb](#afbe0c199a4a58029bf2d83a0b463639c) |
|  | User supplied list of HTTP callback functions if the calling application wants to know the parsing status or the HTTP fields. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [recv\_buf](#abaabd58d149720720ffd61025d58e4a9) |
|  | User supplied buffer where received data is stored. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [recv\_buf\_len](#a9da5216bbd27ad54fd11368897ed660f) |
|  | Length of the user supplied receive buffer. |
| const char \* | [url](#a6a7573252e31fddb5cad5a6764c486c1) |
|  | The URL for this request, for example: /index.html. |
| const char \* | [protocol](#a38cad3f92ed5b712f749851bbeed9a2f) |
|  | The HTTP protocol, for example "HTTP/1.1". |
| const char \*\* | [header\_fields](#a2d2f8be2634eb89d0b877b989307ac7b) |
|  | The HTTP header fields (application specific) The Content-Type may be specified here or in the next field. |
| const char \* | [content\_type\_value](#a1e610f06e9a8ec05cb0de382163a8c79) |
|  | The value of the Content-Type header field, may be NULL. |
| const char \* | [host](#a3ed1146d59f33e9042fae421619df27c) |
|  | Hostname to be used in the request. |
| const char \* | [port](#abe9fdaab40cac6afb16acc2560dfe7e7) |
|  | Port number to be used in the request. |
| [http\_payload\_cb\_t](group__http__client.md#gaf46ede77bdc83602c84b9342dd8d30ed) | [payload\_cb](#a15551f2e8c772479fb7acac20765fa12) |
|  | User supplied callback function to call when payload needs to be sent. |
| const char \* | [payload](#af201ae38024233307ed2c87684ea70d3) |
|  | Payload, may be NULL. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [payload\_len](#a589615592c6c14bdecc03553c395c12f) |
|  | Payload length is used to calculate Content-Length. |
| [http\_header\_cb\_t](group__http__client.md#ga34a431c54c52b86618ca0e27ce3862b4) | [optional\_headers\_cb](#ab6fe0ec09c24302279124043e82f17ff) |
|  | User supplied callback function to call when optional headers need to be sent. |
| const char \*\* | [optional\_headers](#aa29c2bcb70011c9776c959667e10bcf5) |
|  | A NULL terminated list of any optional headers that should be added to the HTTP request. |

## Detailed Description

HTTP client request.

This contains all the data that is needed when doing a HTTP request.

## Field Documentation

## [◆ ](#a1e610f06e9a8ec05cb0de382163a8c79)content\_type\_value

| const char\* http\_request::content\_type\_value |
| --- |

The value of the Content-Type header field, may be NULL.

## [◆ ](#a2d2f8be2634eb89d0b877b989307ac7b)header\_fields

| const char\*\* http\_request::header\_fields |
| --- |

The HTTP header fields (application specific) The Content-Type may be specified here or in the next field.

Depending on your application, the Content-Type may vary, however some header fields may remain constant through the application's life cycle. This is a NULL terminated list of header fields.

## [◆ ](#a3ed1146d59f33e9042fae421619df27c)host

| const char\* http\_request::host |
| --- |

Hostname to be used in the request.

## [◆ ](#afbe0c199a4a58029bf2d83a0b463639c)http\_cb

| const struct [http\_parser\_settings](structhttp__parser__settings.md)\* http\_request::http\_cb |
| --- |

User supplied list of HTTP callback functions if the calling application wants to know the parsing status or the HTTP fields.

This is optional and normally not needed.

## [◆ ](#abb86ccd0e0801c278ef37a78a4b7a958)internal

| struct [http\_client\_internal\_data](structhttp__client__internal__data.md) http\_request::internal |
| --- |

HTTP client request internal data.

## [◆ ](#adbfcd3bcaf57205360bad957a13999e6)method

| enum [http\_method](group__http__methods.md#gaacd5f203e33ac338ca5cb8f02a3ff3b8) http\_request::method |
| --- |

The HTTP method: GET, HEAD, OPTIONS, POST, ...

## [◆ ](#aa29c2bcb70011c9776c959667e10bcf5)optional\_headers

| const char\*\* http\_request::optional\_headers |
| --- |

A NULL terminated list of any optional headers that should be added to the HTTP request.

May be NULL. If the optional\_headers\_cb is specified, then this field is ignored. Note that there are two similar fields that contain headers, the header\_fields above and this optional\_headers. This is done like this to support Websocket use case where Websocket will use header\_fields variable and any optional application specific headers will be placed into this field.

## [◆ ](#ab6fe0ec09c24302279124043e82f17ff)optional\_headers\_cb

| [http\_header\_cb\_t](group__http__client.md#ga34a431c54c52b86618ca0e27ce3862b4) http\_request::optional\_headers\_cb |
| --- |

User supplied callback function to call when optional headers need to be sent.

This can be NULL, in which case the optional\_headers field in [http\_request](structhttp__request.md "HTTP client request.") is used. The idea of this optional\_headers callback is to allow user to send more HTTP header data that is practical to store in allocated memory.

## [◆ ](#af201ae38024233307ed2c87684ea70d3)payload

| const char\* http\_request::payload |
| --- |

Payload, may be NULL.

## [◆ ](#a15551f2e8c772479fb7acac20765fa12)payload\_cb

| [http\_payload\_cb\_t](group__http__client.md#gaf46ede77bdc83602c84b9342dd8d30ed) http\_request::payload\_cb |
| --- |

User supplied callback function to call when payload needs to be sent.

This can be NULL in which case the payload field in [http\_request](structhttp__request.md "HTTP client request.") is used. The idea of this payload callback is to allow user to send more data that is practical to store in allocated memory.

## [◆ ](#a589615592c6c14bdecc03553c395c12f)payload\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) http\_request::payload\_len |
| --- |

Payload length is used to calculate Content-Length.

Set to 0 for chunked transfers.

## [◆ ](#abe9fdaab40cac6afb16acc2560dfe7e7)port

| const char\* http\_request::port |
| --- |

Port number to be used in the request.

## [◆ ](#a38cad3f92ed5b712f749851bbeed9a2f)protocol

| const char\* http\_request::protocol |
| --- |

The HTTP protocol, for example "HTTP/1.1".

## [◆ ](#abaabd58d149720720ffd61025d58e4a9)recv\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* http\_request::recv\_buf |
| --- |

User supplied buffer where received data is stored.

## [◆ ](#a9da5216bbd27ad54fd11368897ed660f)recv\_buf\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) http\_request::recv\_buf\_len |
| --- |

Length of the user supplied receive buffer.

## [◆ ](#aba8bf528f3e279d55662eedc9168d25c)response

| [http\_response\_cb\_t](group__http__client.md#ga9e079c737c325ee21a57e615b641f21a) http\_request::response |
| --- |

User supplied callback function to call when response is received.

## [◆ ](#a6a7573252e31fddb5cad5a6764c486c1)url

| const char\* http\_request::url |
| --- |

The URL for this request, for example: /index.html.

---

The documentation for this struct was generated from the following file:

- zephyr/net/http/[client.h](client_8h_source.md)

- [http\_request](structhttp__request.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
