---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structwebsocket__request.html
original_path: doxygen/html/structwebsocket__request.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

websocket\_request Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Websocket API](group__websocket.md)

Websocket client connection request.
[More...](#details)

`#include <[websocket.h](websocket_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [host](#a8769d50f1a6168dc6518f2dd0c74b62a) |
|  | Host of the Websocket server when doing HTTP handshakes. |
| const char \* | [url](#a49ef6c2f4201beeb3af8992ded2bd4a3) |
|  | URL of the Websocket. |
| [http\_header\_cb\_t](group__http__client.md#ga34a431c54c52b86618ca0e27ce3862b4) | [optional\_headers\_cb](#ab7a281fff2a27a52f7ec346643f55b71) |
|  | User supplied callback function to call when optional headers need to be sent. |
| const char \*\* | [optional\_headers](#a4cea74d6094325b218b6bbed4005b912) |
|  | A NULL terminated list of any optional headers that should be added to the HTTP request. |
| [websocket\_connect\_cb\_t](group__websocket.md#gaabfd7aa30ce659214b990eabb0b6d591) | [cb](#a96936b68fec07f077d9e9569ef1411d1) |
|  | User supplied callback function to call when a connection is established. |
| const struct [http\_parser\_settings](structhttp__parser__settings.md) \* | [http\_cb](#a38315d0c37bdc8cfe22cdbc6d2c8af4a) |
|  | User supplied list of callback functions if the calling application wants to know the parsing status or the HTTP fields during the handshake. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [tmp\_buf](#a939ed8e980af4bc98f30d1bad835a2d2) |
|  | User supplied buffer where HTTP connection data is stored. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [tmp\_buf\_len](#a09bb3c708b51d8f86de244b3fc4a9f57) |
|  | Length of the user supplied temp buffer. |

## Detailed Description

Websocket client connection request.

This contains all the data that is needed when doing a Websocket connection request.

## Field Documentation

## [◆ ](#a96936b68fec07f077d9e9569ef1411d1)cb

| [websocket\_connect\_cb\_t](group__websocket.md#gaabfd7aa30ce659214b990eabb0b6d591) websocket\_request::cb |
| --- |

User supplied callback function to call when a connection is established.

## [◆ ](#a8769d50f1a6168dc6518f2dd0c74b62a)host

| const char\* websocket\_request::host |
| --- |

Host of the Websocket server when doing HTTP handshakes.

## [◆ ](#a38315d0c37bdc8cfe22cdbc6d2c8af4a)http\_cb

| const struct [http\_parser\_settings](structhttp__parser__settings.md)\* websocket\_request::http\_cb |
| --- |

User supplied list of callback functions if the calling application wants to know the parsing status or the HTTP fields during the handshake.

This is optional parameter and normally not needed but is useful if the caller wants to know something about the fields that the server is sending.

## [◆ ](#a4cea74d6094325b218b6bbed4005b912)optional\_headers

| const char\*\* websocket\_request::optional\_headers |
| --- |

A NULL terminated list of any optional headers that should be added to the HTTP request.

May be NULL. If the optional\_headers\_cb is specified, then this field is ignored.

## [◆ ](#ab7a281fff2a27a52f7ec346643f55b71)optional\_headers\_cb

| [http\_header\_cb\_t](group__http__client.md#ga34a431c54c52b86618ca0e27ce3862b4) websocket\_request::optional\_headers\_cb |
| --- |

User supplied callback function to call when optional headers need to be sent.

This can be NULL, in which case the optional\_headers field in [http\_request](structhttp__request.md "HTTP client request.") is used. The idea of this optional\_headers callback is to allow user to send more HTTP header data that is practical to store in allocated memory.

## [◆ ](#a939ed8e980af4bc98f30d1bad835a2d2)tmp\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* websocket\_request::tmp\_buf |
| --- |

User supplied buffer where HTTP connection data is stored.

## [◆ ](#a09bb3c708b51d8f86de244b3fc4a9f57)tmp\_buf\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) websocket\_request::tmp\_buf\_len |
| --- |

Length of the user supplied temp buffer.

## [◆ ](#a49ef6c2f4201beeb3af8992ded2bd4a3)url

| const char\* websocket\_request::url |
| --- |

URL of the Websocket.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[websocket.h](websocket_8h_source.md)

- [websocket\_request](structwebsocket__request.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
