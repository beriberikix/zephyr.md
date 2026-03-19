---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/websocket_8h.html
original_path: doxygen/html/websocket_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

websocket.h File Reference

Websocket API.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/net/net_ip.h](net__ip_8h_source.md)>`  
`#include <[zephyr/net/http/parser.h](parser_8h_source.md)>`  
`#include <[zephyr/net/http/client.h](client_8h_source.md)>`

[Go to the source code of this file.](websocket_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [websocket\_request](structwebsocket__request.md) |
|  | Websocket client connection request. [More...](structwebsocket__request.md#details) |

| Macros | |
| --- | --- |
| #define | [WEBSOCKET\_FLAG\_FINAL](group__websocket.md#ga002ade0e3787b6d9da82ab84af1cd354)   0x00000001 |
|  | Message type values. |
| #define | [WEBSOCKET\_FLAG\_TEXT](group__websocket.md#ga9405e69474b48472dfe0b10017dfcd75)   0x00000002 |
|  | Textual data. |
| #define | [WEBSOCKET\_FLAG\_BINARY](group__websocket.md#ga8616f88cb194d82da9367f2f48832842)   0x00000004 |
|  | Binary data. |
| #define | [WEBSOCKET\_FLAG\_CLOSE](group__websocket.md#gaab5fa480351106751f6482f5056b4238)   0x00000008 |
|  | Closing connection. |
| #define | [WEBSOCKET\_FLAG\_PING](group__websocket.md#ga2f2ea01b18c13f38fe834f855ae0da93)   0x00000010 |
|  | Ping message. |
| #define | [WEBSOCKET\_FLAG\_PONG](group__websocket.md#ga68cdf577c5401440095dacf224541047)   0x00000020 |
|  | Pong message. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [websocket\_connect\_cb\_t](group__websocket.md#gaabfd7aa30ce659214b990eabb0b6d591)) (int ws\_sock, struct [http\_request](structhttp__request.md) \*req, void \*user\_data) |
|  | Callback called after Websocket connection is established. |

| Enumerations | |
| --- | --- |
| enum | [websocket\_opcode](group__websocket.md#ga207402575311103c75906143724e8c35) {     [WEBSOCKET\_OPCODE\_CONTINUE](group__websocket.md#gga207402575311103c75906143724e8c35a8912ad4ae9a3bbbe7ecb02cd2c1a8b35) = 0x00 , [WEBSOCKET\_OPCODE\_DATA\_TEXT](group__websocket.md#gga207402575311103c75906143724e8c35a2058fe14c900c3298affa6eed05d182c) = 0x01 , [WEBSOCKET\_OPCODE\_DATA\_BINARY](group__websocket.md#gga207402575311103c75906143724e8c35aa8d476ba0f4f3f892503d29fa76f1a69) = 0x02 , [WEBSOCKET\_OPCODE\_CLOSE](group__websocket.md#gga207402575311103c75906143724e8c35a291cb41ba1d8b535a1625d394c066191) = 0x08 ,     [WEBSOCKET\_OPCODE\_PING](group__websocket.md#gga207402575311103c75906143724e8c35af7a26bf82e06544e8393f17d6c074709) = 0x09 , [WEBSOCKET\_OPCODE\_PONG](group__websocket.md#gga207402575311103c75906143724e8c35a141c7a8d3c0864115c8bfe3248e59d90) = 0x0A   } |
|  | Websocket option codes. [More...](group__websocket.md#ga207402575311103c75906143724e8c35) |

| Functions | |
| --- | --- |
| int | [websocket\_connect](group__websocket.md#ga71a43ec629929d2eb1baba4e3f13a615) (int http\_sock, struct [websocket\_request](structwebsocket__request.md) \*req, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout, void \*user\_data) |
|  | Connect to a server that provides Websocket service. |
| int | [websocket\_send\_msg](group__websocket.md#gac23c351e5020d0fc9e936933d399b187) (int ws\_sock, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) payload\_len, enum [websocket\_opcode](group__websocket.md#ga207402575311103c75906143724e8c35) opcode, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mask, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) final, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Send websocket msg to peer. |
| int | [websocket\_recv\_msg](group__websocket.md#ga0fb118f84b7631d12c1b742b75593ba6) (int ws\_sock, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buf\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*message\_type, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*remaining, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Receive websocket msg from peer. |
| int | [websocket\_disconnect](group__websocket.md#gacc2f06e2c361317ff48f171abc3d1209) (int ws\_sock) |
|  | Close websocket. |
| int | [websocket\_register](group__websocket.md#gabc2556e62f001f8109bf6ae9f50f3952) (int http\_sock, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*recv\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) recv\_buf\_len) |
|  | Register a socket as websocket. |
| int | [websocket\_unregister](group__websocket.md#gaa3131d2599c8c69ab95c55c2e38e28e0) (int ws\_sock) |
|  | Unregister a websocket. |

## Detailed Description

Websocket API.

An API for applications to setup websocket connections

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [websocket.h](websocket_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
