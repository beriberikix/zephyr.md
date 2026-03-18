---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/coap__client_8h.html
original_path: doxygen/html/coap__client_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coap\_client.h File Reference

CoAP client API.
[More...](#details)

`#include <[zephyr/net/coap.h](coap_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](coap__client_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [coap\_client\_request](structcoap__client__request.md) |
|  | Representation of a CoAP client request. [More...](structcoap__client__request.md#details) |
| struct | [coap\_client\_option](structcoap__client__option.md) |
|  | Representation of extra options for the CoAP client request. [More...](structcoap__client__option.md#details) |

| Macros | |
| --- | --- |
| #define | [MAX\_COAP\_MSG\_LEN](group__coap__client.md#ga53c57dcb241786b6e0213a7198667bd0) |
|  | Maximum size of a CoAP message. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [coap\_client\_response\_cb\_t](group__coap__client.md#ga0a33095a309016ddb4ff00206cfd4bb0)) ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) result\_code, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) last\_block, void \*user\_data) |
|  | Callback for CoAP request. |

| Functions | |
| --- | --- |
| int | [coap\_client\_init](group__coap__client.md#gac85c4bcbc129b5d2be6a74f9024c84d9) (struct coap\_client \*client, const char \*info) |
|  | Initialize the CoAP client. |
| int | [coap\_client\_req](group__coap__client.md#ga028ebc6d75d98868599bca8b6ae56308) (struct coap\_client \*client, int sock, const struct [sockaddr](structsockaddr.md) \*addr, struct [coap\_client\_request](structcoap__client__request.md) \*req, struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \*params) |
|  | Send CoAP request. |
| void | [coap\_client\_cancel\_requests](group__coap__client.md#ga3f511d4df22bece05c1ac97ff4d09a80) (struct coap\_client \*client) |
|  | Cancel all current requests. |

## Detailed Description

CoAP client API.

An API for applications to do CoAP requests

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [coap\_client.h](coap__client_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
