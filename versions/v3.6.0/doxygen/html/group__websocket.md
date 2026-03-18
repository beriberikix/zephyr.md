---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__websocket.html
original_path: doxygen/html/group__websocket.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Websocket API

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Websocket API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [websocket\_request](structwebsocket__request.md) |
|  | Websocket client connection request. [More...](structwebsocket__request.md#details) |

| Macros | |
| --- | --- |
| #define | [WEBSOCKET\_FLAG\_FINAL](#ga002ade0e3787b6d9da82ab84af1cd354)   0x00000001 |
|  | Message type values. |
| #define | [WEBSOCKET\_FLAG\_TEXT](#ga9405e69474b48472dfe0b10017dfcd75)   0x00000002 |
|  | Textual data. |
| #define | [WEBSOCKET\_FLAG\_BINARY](#ga8616f88cb194d82da9367f2f48832842)   0x00000004 |
|  | Binary data. |
| #define | [WEBSOCKET\_FLAG\_CLOSE](#gaab5fa480351106751f6482f5056b4238)   0x00000008 |
|  | Closing connection. |
| #define | [WEBSOCKET\_FLAG\_PING](#ga2f2ea01b18c13f38fe834f855ae0da93)   0x00000010 |
|  | Ping message. |
| #define | [WEBSOCKET\_FLAG\_PONG](#ga68cdf577c5401440095dacf224541047)   0x00000020 |
|  | Pong message. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [websocket\_connect\_cb\_t](#gaabfd7aa30ce659214b990eabb0b6d591)) (int ws\_sock, struct [http\_request](structhttp__request.md) \*req, void \*user\_data) |
|  | Callback called after Websocket connection is established. |

| Enumerations | |
| --- | --- |
| enum | [websocket\_opcode](#ga207402575311103c75906143724e8c35) {     [WEBSOCKET\_OPCODE\_CONTINUE](#gga207402575311103c75906143724e8c35a8912ad4ae9a3bbbe7ecb02cd2c1a8b35) = 0x00 , [WEBSOCKET\_OPCODE\_DATA\_TEXT](#gga207402575311103c75906143724e8c35a2058fe14c900c3298affa6eed05d182c) = 0x01 , [WEBSOCKET\_OPCODE\_DATA\_BINARY](#gga207402575311103c75906143724e8c35aa8d476ba0f4f3f892503d29fa76f1a69) = 0x02 , [WEBSOCKET\_OPCODE\_CLOSE](#gga207402575311103c75906143724e8c35a291cb41ba1d8b535a1625d394c066191) = 0x08 ,     [WEBSOCKET\_OPCODE\_PING](#gga207402575311103c75906143724e8c35af7a26bf82e06544e8393f17d6c074709) = 0x09 , [WEBSOCKET\_OPCODE\_PONG](#gga207402575311103c75906143724e8c35a141c7a8d3c0864115c8bfe3248e59d90) = 0x0A   } |

| Functions | |
| --- | --- |
| int | [websocket\_connect](#ga71a43ec629929d2eb1baba4e3f13a615) (int http\_sock, struct [websocket\_request](structwebsocket__request.md) \*req, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout, void \*user\_data) |
|  | Connect to a server that provides Websocket service. |
| int | [websocket\_send\_msg](#gac23c351e5020d0fc9e936933d399b187) (int ws\_sock, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) payload\_len, enum [websocket\_opcode](#ga207402575311103c75906143724e8c35) opcode, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mask, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) final, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Send websocket msg to peer. |
| int | [websocket\_recv\_msg](#ga0fb118f84b7631d12c1b742b75593ba6) (int ws\_sock, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buf\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*message\_type, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*remaining, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Receive websocket msg from peer. |
| int | [websocket\_disconnect](#gacc2f06e2c361317ff48f171abc3d1209) (int ws\_sock) |
|  | Close websocket. |
| static void | [websocket\_init](#gab258dd52880c6cbbc7e2aceee329a4a3) (void) |

## Detailed Description

Websocket API.

## Macro Definition Documentation

## [◆ ](#ga8616f88cb194d82da9367f2f48832842)WEBSOCKET\_FLAG\_BINARY

| #define WEBSOCKET\_FLAG\_BINARY   0x00000004 |
| --- |

`#include <[websocket.h](websocket_8h.md)>`

Binary data.

## [◆ ](#gaab5fa480351106751f6482f5056b4238)WEBSOCKET\_FLAG\_CLOSE

| #define WEBSOCKET\_FLAG\_CLOSE   0x00000008 |
| --- |

`#include <[websocket.h](websocket_8h.md)>`

Closing connection.

## [◆ ](#ga002ade0e3787b6d9da82ab84af1cd354)WEBSOCKET\_FLAG\_FINAL

| #define WEBSOCKET\_FLAG\_FINAL   0x00000001 |
| --- |

`#include <[websocket.h](websocket_8h.md)>`

Message type values.

Returned in [websocket\_recv\_msg()](#ga0fb118f84b7631d12c1b742b75593ba6) Final frame

## [◆ ](#ga2f2ea01b18c13f38fe834f855ae0da93)WEBSOCKET\_FLAG\_PING

| #define WEBSOCKET\_FLAG\_PING   0x00000010 |
| --- |

`#include <[websocket.h](websocket_8h.md)>`

Ping message.

## [◆ ](#ga68cdf577c5401440095dacf224541047)WEBSOCKET\_FLAG\_PONG

| #define WEBSOCKET\_FLAG\_PONG   0x00000020 |
| --- |

`#include <[websocket.h](websocket_8h.md)>`

Pong message.

## [◆ ](#ga9405e69474b48472dfe0b10017dfcd75)WEBSOCKET\_FLAG\_TEXT

| #define WEBSOCKET\_FLAG\_TEXT   0x00000002 |
| --- |

`#include <[websocket.h](websocket_8h.md)>`

Textual data.

## Typedef Documentation

## [◆ ](#gaabfd7aa30ce659214b990eabb0b6d591)websocket\_connect\_cb\_t

| typedef int(\* websocket\_connect\_cb\_t) (int ws\_sock, struct [http\_request](structhttp__request.md) \*req, void \*user\_data) |
| --- |

`#include <[websocket.h](websocket_8h.md)>`

Callback called after Websocket connection is established.

Parameters
:   | ws\_sock | Websocket id |
    | --- | --- |
    | req | HTTP handshake request |
    | user\_data | A valid pointer on some user data or NULL |

Returns
:   0 if ok, <0 if there is an error and connection should be aborted

## Enumeration Type Documentation

## [◆ ](#ga207402575311103c75906143724e8c35)websocket\_opcode

| enum [websocket\_opcode](#ga207402575311103c75906143724e8c35) |
| --- |

`#include <[websocket.h](websocket_8h.md)>`

| Enumerator | |
| --- | --- |
| WEBSOCKET\_OPCODE\_CONTINUE |  |
| WEBSOCKET\_OPCODE\_DATA\_TEXT |  |
| WEBSOCKET\_OPCODE\_DATA\_BINARY |  |
| WEBSOCKET\_OPCODE\_CLOSE |  |
| WEBSOCKET\_OPCODE\_PING |  |
| WEBSOCKET\_OPCODE\_PONG |  |

## Function Documentation

## [◆ ](#ga71a43ec629929d2eb1baba4e3f13a615)websocket\_connect()

| int websocket\_connect | ( | int | *http\_sock*, |
| --- | --- | --- | --- |
|  |  | struct [websocket\_request](structwebsocket__request.md) \* | *req*, |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout*, |
|  |  | void \* | *user\_data* ) |

`#include <[websocket.h](websocket_8h.md)>`

Connect to a server that provides Websocket service.

The callback is called after connection is established. The returned value is a new socket descriptor that can be used to send / receive data using the BSD socket API.

Parameters
:   | http\_sock | Socket id to the server. Note that this socket is used to do HTTP handshakes etc. The actual Websocket connectivity is done via the returned websocket id. Note that the http\_sock must not be closed after this function returns as it is used to deliver the Websocket packets to the Websocket server. |
    | --- | --- |
    | req | Websocket request. User should allocate and fill the request data. |
    | timeout | Max timeout to wait for the connection. The timeout value is in milliseconds. Value SYS\_FOREVER\_MS means to wait forever. |
    | user\_data | User specified data that is passed to the callback. |

Returns
:   Websocket id to be used when sending/receiving Websocket data.

## [◆ ](#gacc2f06e2c361317ff48f171abc3d1209)websocket\_disconnect()

| int websocket\_disconnect | ( | int | *ws\_sock* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[websocket.h](websocket_8h.md)>`

Close websocket.

One must call [websocket\_connect()](#ga71a43ec629929d2eb1baba4e3f13a615) after this call to re-establish the connection.

Parameters
:   | ws\_sock | Websocket id returned by [websocket\_connect()](#ga71a43ec629929d2eb1baba4e3f13a615). |
    | --- | --- |

## [◆ ](#gab258dd52880c6cbbc7e2aceee329a4a3)websocket\_init()

| | void websocket\_init | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[websocket.h](websocket_8h.md)>`

## [◆ ](#ga0fb118f84b7631d12c1b742b75593ba6)websocket\_recv\_msg()

| int websocket\_recv\_msg | ( | int | *ws\_sock*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *buf\_len*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *message\_type*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *remaining*, |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* ) |

`#include <[websocket.h](websocket_8h.md)>`

Receive websocket msg from peer.

The function will automatically remove websocket header from the message.

Parameters
:   | ws\_sock | Websocket id returned by [websocket\_connect()](#ga71a43ec629929d2eb1baba4e3f13a615). |
    | --- | --- |
    | buf | Buffer where websocket data is read. |
    | buf\_len | Length of the data buffer. |
    | message\_type | Type of the message. |
    | remaining | How much there is data left in the message after this read. |
    | timeout | How long to try to receive the message. The value is in milliseconds. Value SYS\_FOREVER\_MS means to wait forever. |

Return values
:   | >=0 | amount of bytes received. |
    | --- | --- |
    | -EAGAIN | on timeout. |
    | -ENOTCONN | on socket close. |
    | -errno | other negative errno value in case of failure. |

## [◆ ](#gac23c351e5020d0fc9e936933d399b187)websocket\_send\_msg()

| int websocket\_send\_msg | ( | int | *ws\_sock*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *payload*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *payload\_len*, |
|  |  | enum [websocket\_opcode](#ga207402575311103c75906143724e8c35) | *opcode*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *mask*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *final*, |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* ) |

`#include <[websocket.h](websocket_8h.md)>`

Send websocket msg to peer.

The function will automatically add websocket header to the message.

Parameters
:   | ws\_sock | Websocket id returned by [websocket\_connect()](#ga71a43ec629929d2eb1baba4e3f13a615). |
    | --- | --- |
    | payload | Websocket data to send. |
    | payload\_len | Length of the data to be sent. |
    | opcode | Operation code (text, binary, ping, pong, close) |
    | mask | Mask the data, see RFC 6455 for details |
    | final | Is this final message for this message send. If final == false, then the first message must have valid opcode and subsequent messages must have opcode WEBSOCKET\_OPCODE\_CONTINUE. If final == true and this is the only message, then opcode should have proper opcode (text or binary) set. |
    | timeout | How long to try to send the message. The value is in milliseconds. Value SYS\_FOREVER\_MS means to wait forever. |

Returns
:   <0 if error, >=0 amount of bytes sent

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
