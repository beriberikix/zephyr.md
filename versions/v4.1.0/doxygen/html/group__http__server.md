---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__http__server.html
original_path: doxygen/html/group__http__server.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| #define | [HTTP\_SERVER\_CONTENT\_TYPE](#ga709ddfe3f5ae5605b3399687f8be8c47)(\_extension, \_content\_type) |
| #define | [HTTP\_SERVER\_CONTENT\_TYPE\_FOREACH](#gad1ee2e803d6e38d54c344180a45a25c2)(\_it) |
| #define | [HTTP\_SERVER\_REGISTER\_HEADER\_CAPTURE](#gae1710786f10729930cc6c220a19e2071)(\_id, \_header) |
|  | Register an HTTP request header to be captured by the server. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [http\_resource\_dynamic\_cb\_t](#ga5b74095aacd9d8f6e203ff53d908a99f)) (struct [http\_client\_ctx](structhttp__client__ctx.md) \*client, enum [http\_data\_status](#ga496accfe23add03417bdc98369d32ea8) status, const struct [http\_request\_ctx](structhttp__request__ctx.md) \*request\_ctx, struct [http\_response\_ctx](structhttp__response__ctx.md) \*response\_ctx, void \*user\_data) |
|  | Callback used when data is received. |
| typedef int(\* | [http\_resource\_websocket\_cb\_t](#gaa51ec52c8960a37566d2ac77d624be93)) (int ws\_socket, struct [http\_request\_ctx](structhttp__request__ctx.md) \*request\_ctx, void \*user\_data) |
|  | Callback used when a Websocket connection is setup. |

| Enumerations | |
| --- | --- |
| enum | [http\_resource\_type](#ga23d0077fb99827b25491111bd74d00af) { [HTTP\_RESOURCE\_TYPE\_STATIC](#gga23d0077fb99827b25491111bd74d00afa1170c8c886888c5c0c5dcdc6c593a248) , [HTTP\_RESOURCE\_TYPE\_STATIC\_FS](#gga23d0077fb99827b25491111bd74d00afa05a9e5c3c4c1cce4894e6250220fea6e) , [HTTP\_RESOURCE\_TYPE\_DYNAMIC](#gga23d0077fb99827b25491111bd74d00afae9cdb0e1f8861de769a570399484587e) , [HTTP\_RESOURCE\_TYPE\_WEBSOCKET](#gga23d0077fb99827b25491111bd74d00afa6691e6fe43d8ffbd1ef1fd5c59661866) } |
|  | HTTP server resource type. [More...](#ga23d0077fb99827b25491111bd74d00af) |
| enum | [http\_data\_status](#ga496accfe23add03417bdc98369d32ea8) { [HTTP\_SERVER\_DATA\_ABORTED](#gga496accfe23add03417bdc98369d32ea8a85682febe2a08e3fe23eaa9b178db5dc) = -1 , [HTTP\_SERVER\_DATA\_MORE](#gga496accfe23add03417bdc98369d32ea8a3827f7f5876ef09332845b445cd65231) = 0 , [HTTP\_SERVER\_DATA\_FINAL](#gga496accfe23add03417bdc98369d32ea8a0f462355aede2440403f907d0c6af45a) = 1 } |
|  | Indicates the status of the currently processed piece of data. [More...](#ga496accfe23add03417bdc98369d32ea8) |
| enum | [http\_header\_status](#ga6c15e872ece1b9a740b6dca3974101b3) { [HTTP\_HEADER\_STATUS\_OK](#gga6c15e872ece1b9a740b6dca3974101b3ad4ad497a135cc5855573cc0211e7b7ec) , [HTTP\_HEADER\_STATUS\_DROPPED](#gga6c15e872ece1b9a740b6dca3974101b3a3f41dca87eecce1ac499389e72285621) , [HTTP\_HEADER\_STATUS\_NONE](#gga6c15e872ece1b9a740b6dca3974101b3ac01b170099c3ea7fafa5d22f164930ed) } |
|  | Status of captured request headers. [More...](#ga6c15e872ece1b9a740b6dca3974101b3) |

| Functions | |
| --- | --- |
| int | [http\_server\_start](#ga8125ef45732f81ec1c629a8f41e4c14d) (void) |
|  | Start the HTTP2 server. |
| int | [http\_server\_stop](#ga79f434b5bbc6d2a6ebc65a0c560730cf) (void) |
|  | Stop the HTTP2 server. |

## Detailed Description

Since
:   3.7

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga709ddfe3f5ae5605b3399687f8be8c47)HTTP\_SERVER\_CONTENT\_TYPE

| #define HTTP\_SERVER\_CONTENT\_TYPE | ( |  | *\_extension*, |
| --- | --- | --- | --- |
|  |  |  | *\_content\_type* ) |

`#include <[server.h](server_8h.md)>`

**Value:**

const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([http\_content\_type](structhttp__content__type.md), \_extension) = { \

.extension = [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(\_extension), \

.extension\_len = sizeof([STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(\_extension)) - 1, \

.content\_type = \_content\_type, \

};

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

[http\_content\_type](structhttp__content__type.md)

**Definition** server.h:146

## [◆ ](#gad1ee2e803d6e38d54c344180a45a25c2)HTTP\_SERVER\_CONTENT\_TYPE\_FOREACH

| #define HTTP\_SERVER\_CONTENT\_TYPE\_FOREACH | ( |  | *\_it* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[server.h](server_8h.md)>`

**Value:**

[STRUCT\_SECTION\_FOREACH](group__iterable__section__apis.md#gad723296f2650c25dd278e8586bfaf0ab)([http\_content\_type](structhttp__content__type.md), \_it)

[STRUCT\_SECTION\_FOREACH](group__iterable__section__apis.md#gad723296f2650c25dd278e8586bfaf0ab)

#define STRUCT\_SECTION\_FOREACH(struct\_type, iterator)

Iterate over a specified iterable section.

**Definition** iterable\_sections.h:270

## [◆ ](#gae1710786f10729930cc6c220a19e2071)HTTP\_SERVER\_REGISTER\_HEADER\_CAPTURE

| #define HTTP\_SERVER\_REGISTER\_HEADER\_CAPTURE | ( |  | *\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_header* ) |

`#include <[server.h](server_8h.md)>`

**Value:**

BUILD\_ASSERT(sizeof(\_header) <= CONFIG\_HTTP\_SERVER\_MAX\_HEADER\_LEN, \

"Header is too long to be captured, try increasing " \

"CONFIG\_HTTP\_SERVER\_MAX\_HEADER\_LEN"); \

static const char \*const \_id##\_str = \_header; \

static const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([http\_header\_name](structhttp__header__name.md), \_id) = { \

.name = \_id##\_str, \

}

[http\_header\_name](structhttp__header__name.md)

HTTP header name representation.

**Definition** server.h:392

Register an HTTP request header to be captured by the server.

Parameters
:   | \_id | variable name for the header capture instance |
    | --- | --- |
    | \_header | header to be captured, as literal string |

## Typedef Documentation

## [◆ ](#ga5b74095aacd9d8f6e203ff53d908a99f)http\_resource\_dynamic\_cb\_t

| typedef int(\* http\_resource\_dynamic\_cb\_t) (struct [http\_client\_ctx](structhttp__client__ctx.md) \*client, enum [http\_data\_status](#ga496accfe23add03417bdc98369d32ea8) status, const struct [http\_request\_ctx](structhttp__request__ctx.md) \*request\_ctx, struct [http\_response\_ctx](structhttp__response__ctx.md) \*response\_ctx, void \*user\_data) |
| --- |

`#include <[server.h](server_8h.md)>`

Callback used when data is received.

Data to be sent to client can be specified.

Parameters
:   | client | HTTP context information for this client connection. |
    | --- | --- |
    | status | HTTP data status, indicate whether more data is expected or not. |
    | request\_ctx | Request context structure containing HTTP request data that was received. |
    | response\_ctx | Response context structure for application to populate with response data. |
    | user\_data | User specified data. |

Returns
:   0 success, server can send any response data provided in the response\_ctx. <0 error, close the connection.

## [◆ ](#gaa51ec52c8960a37566d2ac77d624be93)http\_resource\_websocket\_cb\_t

| typedef int(\* http\_resource\_websocket\_cb\_t) (int ws\_socket, struct [http\_request\_ctx](structhttp__request__ctx.md) \*request\_ctx, void \*user\_data) |
| --- |

`#include <[server.h](server_8h.md)>`

Callback used when a Websocket connection is setup.

The application will need to handle all functionality related to the connection like reading and writing websocket data, and closing the connection.

Parameters
:   | ws\_socket | A socket for the Websocket data. |
    | --- | --- |
    | request\_ctx | Request context structure associated with HTTP upgrade request |
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

## [◆ ](#ga6c15e872ece1b9a740b6dca3974101b3)http\_header\_status

| enum [http\_header\_status](#ga6c15e872ece1b9a740b6dca3974101b3) |
| --- |

`#include <[server.h](server_8h.md)>`

Status of captured request headers.

| Enumerator | |
| --- | --- |
| HTTP\_HEADER\_STATUS\_OK | All available headers were successfully captured. |
| HTTP\_HEADER\_STATUS\_DROPPED | One or more headers were dropped due to lack of space. |
| HTTP\_HEADER\_STATUS\_NONE | No header status is available. |

## [◆ ](#ga23d0077fb99827b25491111bd74d00af)http\_resource\_type

| enum [http\_resource\_type](#ga23d0077fb99827b25491111bd74d00af) |
| --- |

`#include <[server.h](server_8h.md)>`

HTTP server resource type.

| Enumerator | |
| --- | --- |
| HTTP\_RESOURCE\_TYPE\_STATIC | Static resource, cannot be modified on runtime. |
| HTTP\_RESOURCE\_TYPE\_STATIC\_FS | serves static gzipped files from a filesystem |
| HTTP\_RESOURCE\_TYPE\_DYNAMIC | Dynamic resource, server interacts with the application via registered [http\_resource\_dynamic\_cb\_t](#ga5b74095aacd9d8f6e203ff53d908a99f). |
| HTTP\_RESOURCE\_TYPE\_WEBSOCKET | Websocket resource, application takes control over Websocket connection after and upgrade. |

## Function Documentation

## [◆ ](#ga8125ef45732f81ec1c629a8f41e4c14d)http\_server\_start()

| int http\_server\_start | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[server.h](server_8h.md)>`

Start the HTTP2 server.

The server runs in a background thread. Once started, the server will create a server socket for all HTTP services registered in the system and accept connections from clients (see [HTTP\_SERVICE\_DEFINE](group__http__service.md#ga1aa8efe3622b5c9421a6257140c5d2c5 "HTTP_SERVICE_DEFINE")).

## [◆ ](#ga79f434b5bbc6d2a6ebc65a0c560730cf)http\_server\_stop()

| int http\_server\_stop | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[server.h](server_8h.md)>`

Stop the HTTP2 server.

All server sockets are closed and the server thread is suspended.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
