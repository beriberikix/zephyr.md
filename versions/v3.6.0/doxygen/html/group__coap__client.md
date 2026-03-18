---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__coap__client.html
original_path: doxygen/html/group__coap__client.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

CoAP client API

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

CoAP client API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [coap\_client\_request](structcoap__client__request.md) |
|  | Representation of a CoAP client request. [More...](structcoap__client__request.md#details) |
| struct | [coap\_client\_option](structcoap__client__option.md) |
|  | Representation of extra options for the CoAP client request. [More...](structcoap__client__option.md#details) |

| Macros | |
| --- | --- |
| #define | [MAX\_COAP\_MSG\_LEN](#ga53c57dcb241786b6e0213a7198667bd0) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [coap\_client\_response\_cb\_t](#ga0a33095a309016ddb4ff00206cfd4bb0)) ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) result\_code, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) last\_block, void \*user\_data) |
|  | Callback for CoAP request. |

| Functions | |
| --- | --- |
| int | [coap\_client\_init](#gac85c4bcbc129b5d2be6a74f9024c84d9) (struct coap\_client \*client, const char \*info) |
|  | Initialize the CoAP client. |
| int | [coap\_client\_req](#ga028ebc6d75d98868599bca8b6ae56308) (struct coap\_client \*client, int sock, const struct [sockaddr](structsockaddr.md) \*addr, struct [coap\_client\_request](structcoap__client__request.md) \*req, struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \*params) |
|  | Send CoAP request. |

## Detailed Description

CoAP client API.

## Macro Definition Documentation

## [◆ ](#ga53c57dcb241786b6e0213a7198667bd0)MAX\_COAP\_MSG\_LEN

| #define MAX\_COAP\_MSG\_LEN |
| --- |

`#include <[coap_client.h](coap__client_8h.md)>`

**Value:**

(CONFIG\_COAP\_CLIENT\_MESSAGE\_HEADER\_SIZE + \

CONFIG\_COAP\_CLIENT\_MESSAGE\_SIZE)

## Typedef Documentation

## [◆ ](#ga0a33095a309016ddb4ff00206cfd4bb0)coap\_client\_response\_cb\_t

| typedef void(\* coap\_client\_response\_cb\_t) ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) result\_code, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) last\_block, void \*user\_data) |
| --- |

`#include <[coap_client.h](coap__client_8h.md)>`

Callback for CoAP request.

This callback is called for responses to CoAP client requests. It is used to indicate errors, response codes from server or to deliver payload. Blockwise transfers cause this callback to be called sequentially with increasing payload offset and only partial content in buffer pointed by payload parameter.

Parameters
:   | result\_code | Result code of the response. Negative if there was a failure in send. [coap\_response\_code](group__coap.md#ga1ea81a365834e96f43ab7be573069d26 "coap_response_code") for positive. |
    | --- | --- |
    | offset | Payload offset from the beginning of a blockwise transfer. |
    | payload | Buffer containing the payload from the response. NULL for empty payload. |
    | len | Size of the payload. |
    | last\_block | Indicates the last block of the response. |
    | user\_data | User provided context. |

## Function Documentation

## [◆ ](#gac85c4bcbc129b5d2be6a74f9024c84d9)coap\_client\_init()

| int coap\_client\_init | ( | struct coap\_client \* | *client*, |
| --- | --- | --- | --- |
|  |  | const char \* | *info* ) |

`#include <[coap_client.h](coap__client_8h.md)>`

Initialize the CoAP client.

Parameters
:   | [in] | client | Client instance. |
    | --- | --- | --- |
    | [in] | info | Name for the receiving thread of the client. Setting this NULL will result as default name of "coap\_client". |

Returns
:   int Zero on success, otherwise a negative error code.

## [◆ ](#ga028ebc6d75d98868599bca8b6ae56308)coap\_client\_req()

| int coap\_client\_req | ( | struct coap\_client \* | *client*, |
| --- | --- | --- | --- |
|  |  | int | *sock*, |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | struct [coap\_client\_request](structcoap__client__request.md) \* | *req*, |
|  |  | struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \* | *params* ) |

`#include <[coap_client.h](coap__client_8h.md)>`

Send CoAP request.

Operation is handled asynchronously using a background thread. If the socket isn't connected to a destination address, user must provide a destination address, otherwise the address should be set as NULL. Once the callback is called with last block set as true, socket can be closed or used for another query.

Parameters
:   | client | Client instance. |
    | --- | --- |
    | sock | Open socket file descriptor. |
    | addr | the destination address of the request, NULL if socket is already connected. |
    | req | CoAP request structure |
    | params | Pointer to transmission parameters structure or NULL to use default values. |

Returns
:   zero when operation started successfully or negative error code otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
