---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structhttp__response.html
original_path: doxygen/html/structhttp__response.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

http\_response Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [HTTP client API](group__http__client.md)

HTTP response from the server.
[More...](#details)

`#include <[client.h](client_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [http\_parser\_settings](structhttp__parser__settings.md) \* | [http\_cb](#af306ff4c8424b5abad76037abbfe2833) |
|  | HTTP parser settings for the application usage. |
| [http\_response\_cb\_t](group__http__client.md#ga9e079c737c325ee21a57e615b641f21a) | [cb](#a1936119331645bb421d4a5dc0d3fffb5) |
|  | User provided HTTP response callback which is called when a response is received to a sent HTTP request. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [body\_frag\_start](#a45c8596746f5a359a1e18c95838b59d9) |
|  | Start address of the body fragment contained in the recv\_buf. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [body\_frag\_len](#a58405582a11aa86892b80133f8b4fa43) |
|  | Length of the body fragment contained in the recv\_buf. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [recv\_buf](#aa16de8f3485062bf01b0536e64f58b46) |
|  | Where the response is stored, this is to be provided by the user. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [recv\_buf\_len](#a7454c5963b7bb1c5311f77971d0d1d2f) |
|  | Response buffer maximum length. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [data\_len](#a4208cf209674441a25231732aad91f89) |
|  | Length of the data in the result buf. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [content\_length](#aedcb476d4055a7ba04516cc7a8ef800f) |
|  | HTTP Content-Length field value. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [processed](#a0eb2181115c753a3e1676a18d9a3ed59) |
|  | Amount of data given to the response callback so far, including the current data given to the callback. |
| char | [http\_status](#ae8393f01865e57fcf8ac305990e8d925) [32] |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [http\_status\_code](#a94cd246204b04992712deefe51fc0c26) |
|  | Numeric HTTP status code which corresponds to the textual description. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cl\_present](#a0d28b200a74c150e98b5fc18c61638cc): 1 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [body\_found](#ac713af14995e36c1889291d12803ca18): 1 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [message\_complete](#a4f107746bfff244a841b950dd84b8162): 1 |

## Detailed Description

HTTP response from the server.

## Field Documentation

## [◆ ](#ac713af14995e36c1889291d12803ca18)body\_found

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) http\_response::body\_found |
| --- |

## [◆ ](#a58405582a11aa86892b80133f8b4fa43)body\_frag\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) http\_response::body\_frag\_len |
| --- |

Length of the body fragment contained in the recv\_buf.

## [◆ ](#a45c8596746f5a359a1e18c95838b59d9)body\_frag\_start

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* http\_response::body\_frag\_start |
| --- |

Start address of the body fragment contained in the recv\_buf.

```
                  recv_buffer that contains header + body
                  _______________________________________

                              |←-------- body_frag_len ---------→|
           |←--------------------- data len --------------------→|
       ---------------------------------------------------------------
 ..header  |      header      |               body               |  body..
       ---------------------------------------------------------------
           ↑                  ↑
        recv_buf          body_frag_start

                     recv_buffer that contains body only
                     ___________________________________

            |←------------------ body_frag_len ------------------→|
            |←--------------------- data len --------------------→|
       ---------------------------------------------------------------
```

## ..header/body | body | body..

↑ recv\_buf body\_frag\_start

body\_frag\_start >= recv\_buf body\_frag\_len = data\_len - (body\_frag\_start - recv\_buf)

## [◆ ](#a1936119331645bb421d4a5dc0d3fffb5)cb

| [http\_response\_cb\_t](group__http__client.md#ga9e079c737c325ee21a57e615b641f21a) http\_response::cb |
| --- |

User provided HTTP response callback which is called when a response is received to a sent HTTP request.

## [◆ ](#a0d28b200a74c150e98b5fc18c61638cc)cl\_present

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) http\_response::cl\_present |
| --- |

## [◆ ](#aedcb476d4055a7ba04516cc7a8ef800f)content\_length

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) http\_response::content\_length |
| --- |

HTTP Content-Length field value.

Will be set to zero in the event of a null response.

## [◆ ](#a4208cf209674441a25231732aad91f89)data\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) http\_response::data\_len |
| --- |

Length of the data in the result buf.

If the value is larger than recv\_buf\_len, then it means that the data is truncated and could not be fully copied into recv\_buf. This can only happen if the user did not set the response callback. If the callback is set, then the HTTP client API will call response callback many times so that all the data is delivered to the user. Will be zero in the event of a null response.

## [◆ ](#af306ff4c8424b5abad76037abbfe2833)http\_cb

| const struct [http\_parser\_settings](structhttp__parser__settings.md)\* http\_response::http\_cb |
| --- |

HTTP parser settings for the application usage.

## [◆ ](#ae8393f01865e57fcf8ac305990e8d925)http\_status

| char http\_response::http\_status[32] |
| --- |

## [◆ ](#a94cd246204b04992712deefe51fc0c26)http\_status\_code

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) http\_response::http\_status\_code |
| --- |

Numeric HTTP status code which corresponds to the textual description.

Set to zero if null response is given. Otherwise, will be a 3-digit integer code if valid HTTP response is given.

## [◆ ](#a4f107746bfff244a841b950dd84b8162)message\_complete

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) http\_response::message\_complete |
| --- |

## [◆ ](#a0eb2181115c753a3e1676a18d9a3ed59)processed

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) http\_response::processed |
| --- |

Amount of data given to the response callback so far, including the current data given to the callback.

This should be equal to the content\_length field once the entire body has been received. Will be zero if a null response is given.

## [◆ ](#aa16de8f3485062bf01b0536e64f58b46)recv\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* http\_response::recv\_buf |
| --- |

Where the response is stored, this is to be provided by the user.

## [◆ ](#a7454c5963b7bb1c5311f77971d0d1d2f)recv\_buf\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) http\_response::recv\_buf\_len |
| --- |

Response buffer maximum length.

---

The documentation for this struct was generated from the following file:

- zephyr/net/http/[client.h](client_8h_source.md)

- [http\_response](structhttp__response.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
