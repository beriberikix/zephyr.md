---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__http__server.html
original_path: doxygen/html/group__http__server.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

HTTP server API

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

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
| typedef int(\* | [http\_resource\_dynamic\_cb\_t](#gace7ba97c942714d81f47c7ba860a0de2)) (struct [http\_client\_ctx](structhttp__client__ctx.md) \*client, enum [http\_data\_status](#ga496accfe23add03417bdc98369d32ea8) status, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_len, void \*user\_data) |
|  | Callback used when data is received. |
| typedef int(\* | [http\_resource\_websocket\_cb\_t](#ga5846da152b7734dedfe4b1c026349c2c)) (int ws\_socket, void \*user\_data) |
|  | Callback used when a Websocket connection is setup. |

| Enumerations | |
| --- | --- |
| enum | [http\_resource\_type](#ga23d0077fb99827b25491111bd74d00af) { [HTTP\_RESOURCE\_TYPE\_STATIC](#gga23d0077fb99827b25491111bd74d00afa1170c8c886888c5c0c5dcdc6c593a248) , [HTTP\_RESOURCE\_TYPE\_DYNAMIC](#gga23d0077fb99827b25491111bd74d00afae9cdb0e1f8861de769a570399484587e) , [HTTP\_RESOURCE\_TYPE\_WEBSOCKET](#gga23d0077fb99827b25491111bd74d00afa6691e6fe43d8ffbd1ef1fd5c59661866) } |
|  | HTTP server resource type. [More...](#ga23d0077fb99827b25491111bd74d00af) |
| enum | [http\_data\_status](#ga496accfe23add03417bdc98369d32ea8) { [HTTP\_SERVER\_DATA\_ABORTED](#gga496accfe23add03417bdc98369d32ea8a85682febe2a08e3fe23eaa9b178db5dc) = -1 , [HTTP\_SERVER\_DATA\_MORE](#gga496accfe23add03417bdc98369d32ea8a3827f7f5876ef09332845b445cd65231) = 0 , [HTTP\_SERVER\_DATA\_FINAL](#gga496accfe23add03417bdc98369d32ea8a0f462355aede2440403f907d0c6af45a) = 1 } |
|  | Indicates the status of the currently processed piece of data. [More...](#ga496accfe23add03417bdc98369d32ea8) |

| Functions | |
| --- | --- |
| int | [http\_server\_start](#ga8125ef45732f81ec1c629a8f41e4c14d) (void) |
|  | Start the HTTP2 server. |
| int | [http\_server\_stop](#ga79f434b5bbc6d2a6ebc65a0c560730cf) (void) |
|  | Stop the HTTP2 server. |

## Detailed Description

## Typedef Documentation

## [◆ ](#gace7ba97c942714d81f47c7ba860a0de2)http\_resource\_dynamic\_cb\_t

| typedef int(\* http\_resource\_dynamic\_cb\_t) (struct [http\_client\_ctx](structhttp__client__ctx.md) \*client, enum [http\_data\_status](#ga496accfe23add03417bdc98369d32ea8) status, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_len, void \*user\_data) |
| --- |

`#include <[server.h](server_8h.md)>`

Callback used when data is received.

Data to be sent to client can be specified.

Parameters
:   | client | HTTP context information for this client connection. |
    | --- | --- |
    | status | HTTP data status, indicate whether more data is expected or not. |
    | data\_buffer | Data received. |
    | data\_len | Amount of data received. |
    | user\_data | User specified data. |

Returns
:   >0 amount of data to be sent to client, let server to call this function again when new data is received. 0 nothing to sent to client, close the connection <0 error, close the connection.

## [◆ ](#ga5846da152b7734dedfe4b1c026349c2c)http\_resource\_websocket\_cb\_t

| typedef int(\* http\_resource\_websocket\_cb\_t) (int ws\_socket, void \*user\_data) |
| --- |

`#include <[server.h](server_8h.md)>`

Callback used when a Websocket connection is setup.

The application will need to handle all functionality related to the connection like reading and writing websocket data, and closing the connection.

Parameters
:   | ws\_socket | A socket for the Websocket data. |
    | --- | --- |
    | user\_data | User specified data. |

Returns
:   0 Accepting the connection, HTTP server library will no longer handle data to/from the socket and it is application responsibility to send and receive data to/from the supplied socket. <0 error, close the connection.

## Enumeration Type Documentation

## [◆ ](#ga496accfe23add03417bdc98369d32ea8)http\_data\_status

| enum [http\_data\_status](#ga496accfe23add03417bdc98369d32ea8) |
| --- |

`#include <[server.h](server_8h.md)>`

Indicates the status of the currently processed piece of data.

| Enumerator | |
| --- | --- |
| HTTP\_SERVER\_DATA\_ABORTED | Transaction aborted, data incomplete. |
| HTTP\_SERVER\_DATA\_MORE | Transaction incomplete, more data expected. |
| HTTP\_SERVER\_DATA\_FINAL | Final data fragment in current transaction. |

## [◆ ](#ga23d0077fb99827b25491111bd74d00af)http\_resource\_type

| enum [http\_resource\_type](#ga23d0077fb99827b25491111bd74d00af) |
| --- |

`#include <[server.h](server_8h.md)>`

HTTP server resource type.

| Enumerator | |
| --- | --- |
| HTTP\_RESOURCE\_TYPE\_STATIC | Static resource, cannot be modified on runtime. |
| HTTP\_RESOURCE\_TYPE\_DYNAMIC | Dynamic resource, server interacts with the application via registered [http\_resource\_dynamic\_cb\_t](#gace7ba97c942714d81f47c7ba860a0de2). |
| HTTP\_RESOURCE\_TYPE\_WEBSOCKET | Websocket resource, application takes control over Websocket connection after and upgrade. |

## Function Documentation

## [◆ ](#ga8125ef45732f81ec1c629a8f41e4c14d)http\_server\_start()

| int http\_server\_start | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[server.h](server_8h.md)>`

Start the HTTP2 server.

The server runs in a background thread. Once started, the server will create a server socket for all HTTP services registered in the system and accept connections from clients (see [HTTP\_SERVICE\_DEFINE](group__http__service.md#ga38d08c32ea0e082cb39ed2a8d1a3dcc3 "HTTP_SERVICE_DEFINE")).

## [◆ ](#ga79f434b5bbc6d2a6ebc65a0c560730cf)http\_server\_stop()

| int http\_server\_stop | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[server.h](server_8h.md)>`

Stop the HTTP2 server.

All server sockets are closed and the server thread is suspended.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
