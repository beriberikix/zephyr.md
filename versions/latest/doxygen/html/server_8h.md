---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/server_8h.html
original_path: doxygen/html/server_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

server.h File Reference

HTTP server API.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/net/http/parser.h](parser_8h_source.md)>`  
`#include <[zephyr/net/http/hpack.h](hpack_8h_source.md)>`  
`#include <[zephyr/net/socket.h](net_2socket_8h_source.md)>`

[Go to the source code of this file.](server_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [http\_resource\_detail](structhttp__resource__detail.md) |
|  | Representation of a server resource, common for all resource types. [More...](structhttp__resource__detail.md#details) |
| struct | [http\_resource\_detail\_static](structhttp__resource__detail__static.md) |
|  | Representation of a static server resource. [More...](structhttp__resource__detail__static.md#details) |
| struct | [http\_resource\_detail\_dynamic](structhttp__resource__detail__dynamic.md) |
|  | Representation of a dynamic server resource. [More...](structhttp__resource__detail__dynamic.md#details) |
| struct | [http\_resource\_detail\_websocket](structhttp__resource__detail__websocket.md) |
|  | Representation of a websocket server resource. [More...](structhttp__resource__detail__websocket.md#details) |
| struct | [http2\_stream\_ctx](structhttp2__stream__ctx.md) |
|  | HTTP/2 stream representation. [More...](structhttp2__stream__ctx.md#details) |
| struct | [http2\_frame](structhttp2__frame.md) |
|  | HTTP/2 frame representation. [More...](structhttp2__frame.md#details) |
| struct | [http\_client\_ctx](structhttp__client__ctx.md) |
|  | Representation of an HTTP client connected to the server. [More...](structhttp__client__ctx.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [http\_resource\_dynamic\_cb\_t](group__http__server.md#gace7ba97c942714d81f47c7ba860a0de2)) (struct [http\_client\_ctx](structhttp__client__ctx.md) \*client, enum [http\_data\_status](group__http__server.md#ga496accfe23add03417bdc98369d32ea8) status, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_len, void \*user\_data) |
|  | Callback used when data is received. |
| typedef int(\* | [http\_resource\_websocket\_cb\_t](group__http__server.md#ga5846da152b7734dedfe4b1c026349c2c)) (int ws\_socket, void \*user\_data) |
|  | Callback used when a Websocket connection is setup. |

| Enumerations | |
| --- | --- |
| enum | [http\_resource\_type](group__http__server.md#ga23d0077fb99827b25491111bd74d00af) { [HTTP\_RESOURCE\_TYPE\_STATIC](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa1170c8c886888c5c0c5dcdc6c593a248) , [HTTP\_RESOURCE\_TYPE\_DYNAMIC](group__http__server.md#gga23d0077fb99827b25491111bd74d00afae9cdb0e1f8861de769a570399484587e) , [HTTP\_RESOURCE\_TYPE\_WEBSOCKET](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa6691e6fe43d8ffbd1ef1fd5c59661866) } |
|  | HTTP server resource type. [More...](group__http__server.md#ga23d0077fb99827b25491111bd74d00af) |
| enum | [http\_data\_status](group__http__server.md#ga496accfe23add03417bdc98369d32ea8) { [HTTP\_SERVER\_DATA\_ABORTED](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a85682febe2a08e3fe23eaa9b178db5dc) = -1 , [HTTP\_SERVER\_DATA\_MORE](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a3827f7f5876ef09332845b445cd65231) = 0 , [HTTP\_SERVER\_DATA\_FINAL](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a0f462355aede2440403f907d0c6af45a) = 1 } |
|  | Indicates the status of the currently processed piece of data. [More...](group__http__server.md#ga496accfe23add03417bdc98369d32ea8) |

| Functions | |
| --- | --- |
| int | [http\_server\_start](group__http__server.md#ga8125ef45732f81ec1c629a8f41e4c14d) (void) |
|  | Start the HTTP2 server. |
| int | [http\_server\_stop](group__http__server.md#ga79f434b5bbc6d2a6ebc65a0c560730cf) (void) |
|  | Stop the HTTP2 server. |

## Detailed Description

HTTP server API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [http](dir_12a17b6e7ad2c8cb36f68b2ff871e607.md)
- [server.h](server_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
