---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/client_8h.html
original_path: doxygen/html/client_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

client.h File Reference

HTTP client API.
[More...](#details)

`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/net/net_ip.h](net__ip_8h_source.md)>`  
`#include <[zephyr/net/http/parser.h](parser_8h_source.md)>`

[Go to the source code of this file.](client_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [http\_response](structhttp__response.md) |
|  | HTTP response from the server. [More...](structhttp__response.md#details) |
| struct | [http\_client\_internal\_data](structhttp__client__internal__data.md) |
|  | HTTP client internal data that the application should not touch. [More...](structhttp__client__internal__data.md#details) |
| struct | [http\_request](structhttp__request.md) |
|  | HTTP client request. [More...](structhttp__request.md#details) |

| Macros | |
| --- | --- |
| #define | [HTTP\_CRLF](group__http__client.md#gaca074be7a96314dfc8fd39e49b563977)   "\r\n" |
| #define | [HTTP\_STATUS\_STR\_SIZE](group__http__client.md#ga0a5dd25385eb7e6e76c39acc9331a388)   32 |

| Typedefs | |
| --- | --- |
| typedef int(\* | [http\_payload\_cb\_t](group__http__client.md#gaf46ede77bdc83602c84b9342dd8d30ed)) (int sock, struct [http\_request](structhttp__request.md) \*req, void \*user\_data) |
|  | Callback used when data needs to be sent to the server. |
| typedef int(\* | [http\_header\_cb\_t](group__http__client.md#ga34a431c54c52b86618ca0e27ce3862b4)) (int sock, struct [http\_request](structhttp__request.md) \*req, void \*user\_data) |
|  | Callback can be used if application wants to construct additional HTTP headers when the HTTP request is sent. |
| typedef void(\* | [http\_response\_cb\_t](group__http__client.md#ga9e079c737c325ee21a57e615b641f21a)) (struct [http\_response](structhttp__response.md) \*rsp, enum [http\_final\_call](group__http__client.md#ga04fc31de51404e35b3dfab6261bb8e6d) final\_data, void \*user\_data) |
|  | Callback used when data is received from the server. |

| Enumerations | |
| --- | --- |
| enum | [http\_final\_call](group__http__client.md#ga04fc31de51404e35b3dfab6261bb8e6d) { [HTTP\_DATA\_MORE](group__http__client.md#gga04fc31de51404e35b3dfab6261bb8e6da3f75fb095e40bfb4efd2c16059093359) = 0 , [HTTP\_DATA\_FINAL](group__http__client.md#gga04fc31de51404e35b3dfab6261bb8e6da428633ff4a67c00c67fb5cbc23269d61) = 1 } |

| Functions | |
| --- | --- |
| int | [http\_client\_req](group__http__client.md#gaa38b6efb03f88d6959273a41b6acac81) (int sock, struct [http\_request](structhttp__request.md) \*req, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout, void \*user\_data) |
|  | Do a HTTP request. |

## Detailed Description

HTTP client API.

An API for applications do HTTP requests

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [http](dir_12a17b6e7ad2c8cb36f68b2ff871e607.md)
- [client.h](client_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
