---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/server_8h.html
original_path: doxygen/html/server_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
`#include <[zephyr/net/http/status.h](status_8h_source.md)>`  
`#include <[zephyr/net/socket.h](net_2socket_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](server_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [http\_resource\_detail](structhttp__resource__detail.md) |
|  | Representation of a server resource, common for all resource types. [More...](structhttp__resource__detail.md#details) |
| struct | [http\_resource\_detail\_static](structhttp__resource__detail__static.md) |
|  | Representation of a static server resource. [More...](structhttp__resource__detail__static.md#details) |
| struct | [http\_resource\_detail\_static\_fs](structhttp__resource__detail__static__fs.md) |
|  | Representation of a static filesystem server resource. [More...](structhttp__resource__detail__static__fs.md#details) |
| struct | [http\_content\_type](structhttp__content__type.md) |
| struct | [http\_header](structhttp__header.md) |
|  | HTTP header representation. [More...](structhttp__header.md#details) |
| struct | [http\_request\_ctx](structhttp__request__ctx.md) |
|  | HTTP request context. [More...](structhttp__request__ctx.md#details) |
| struct | [http\_response\_ctx](structhttp__response__ctx.md) |
|  | HTTP response context. [More...](structhttp__response__ctx.md#details) |
| struct | [http\_resource\_detail\_dynamic](structhttp__resource__detail__dynamic.md) |
|  | Representation of a dynamic server resource. [More...](structhttp__resource__detail__dynamic.md#details) |
| struct | [http\_resource\_detail\_websocket](structhttp__resource__detail__websocket.md) |
|  | Representation of a websocket server resource. [More...](structhttp__resource__detail__websocket.md#details) |
| struct | [http2\_stream\_ctx](structhttp2__stream__ctx.md) |
|  | HTTP/2 stream representation. [More...](structhttp2__stream__ctx.md#details) |
| struct | [http2\_frame](structhttp2__frame.md) |
|  | HTTP/2 frame representation. [More...](structhttp2__frame.md#details) |
| struct | [http\_header\_name](structhttp__header__name.md) |
|  | HTTP header name representation. [More...](structhttp__header__name.md#details) |
| struct | [http\_client\_ctx](structhttp__client__ctx.md) |
|  | Representation of an HTTP client connected to the server. [More...](structhttp__client__ctx.md#details) |

| Macros | |
| --- | --- |
| #define | [HTTP\_SERVER\_CONTENT\_TYPE](group__http__server.md#ga709ddfe3f5ae5605b3399687f8be8c47)(\_extension, \_content\_type) |
| #define | [HTTP\_SERVER\_CONTENT\_TYPE\_FOREACH](group__http__server.md#gad1ee2e803d6e38d54c344180a45a25c2)(\_it) |
| #define | [HTTP\_SERVER\_REGISTER\_HEADER\_CAPTURE](group__http__server.md#gae1710786f10729930cc6c220a19e2071)(\_id, \_header) |
|  | Register an HTTP request header to be captured by the server. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [http\_resource\_dynamic\_cb\_t](group__http__server.md#ga5b74095aacd9d8f6e203ff53d908a99f)) (struct [http\_client\_ctx](structhttp__client__ctx.md) \*client, enum [http\_data\_status](group__http__server.md#ga496accfe23add03417bdc98369d32ea8) status, const struct [http\_request\_ctx](structhttp__request__ctx.md) \*request\_ctx, struct [http\_response\_ctx](structhttp__response__ctx.md) \*response\_ctx, void \*user\_data) |
|  | Callback used when data is received. |
| typedef int(\* | [http\_resource\_websocket\_cb\_t](group__http__server.md#gaa51ec52c8960a37566d2ac77d624be93)) (int ws\_socket, struct [http\_request\_ctx](structhttp__request__ctx.md) \*request\_ctx, void \*user\_data) |
|  | Callback used when a Websocket connection is setup. |

| Enumerations | |
| --- | --- |
| enum | [http\_resource\_type](group__http__server.md#ga23d0077fb99827b25491111bd74d00af) { [HTTP\_RESOURCE\_TYPE\_STATIC](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa1170c8c886888c5c0c5dcdc6c593a248) , [HTTP\_RESOURCE\_TYPE\_STATIC\_FS](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa05a9e5c3c4c1cce4894e6250220fea6e) , [HTTP\_RESOURCE\_TYPE\_DYNAMIC](group__http__server.md#gga23d0077fb99827b25491111bd74d00afae9cdb0e1f8861de769a570399484587e) , [HTTP\_RESOURCE\_TYPE\_WEBSOCKET](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa6691e6fe43d8ffbd1ef1fd5c59661866) } |
|  | HTTP server resource type. [More...](group__http__server.md#ga23d0077fb99827b25491111bd74d00af) |
| enum | [http\_data\_status](group__http__server.md#ga496accfe23add03417bdc98369d32ea8) { [HTTP\_SERVER\_DATA\_ABORTED](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a85682febe2a08e3fe23eaa9b178db5dc) = -1 , [HTTP\_SERVER\_DATA\_MORE](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a3827f7f5876ef09332845b445cd65231) = 0 , [HTTP\_SERVER\_DATA\_FINAL](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a0f462355aede2440403f907d0c6af45a) = 1 } |
|  | Indicates the status of the currently processed piece of data. [More...](group__http__server.md#ga496accfe23add03417bdc98369d32ea8) |
| enum | [http\_header\_status](group__http__server.md#ga6c15e872ece1b9a740b6dca3974101b3) { [HTTP\_HEADER\_STATUS\_OK](group__http__server.md#gga6c15e872ece1b9a740b6dca3974101b3ad4ad497a135cc5855573cc0211e7b7ec) , [HTTP\_HEADER\_STATUS\_DROPPED](group__http__server.md#gga6c15e872ece1b9a740b6dca3974101b3a3f41dca87eecce1ac499389e72285621) , [HTTP\_HEADER\_STATUS\_NONE](group__http__server.md#gga6c15e872ece1b9a740b6dca3974101b3ac01b170099c3ea7fafa5d22f164930ed) } |
|  | Status of captured request headers. [More...](group__http__server.md#ga6c15e872ece1b9a740b6dca3974101b3) |

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
