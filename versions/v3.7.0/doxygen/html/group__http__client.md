---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__http__client.html
original_path: doxygen/html/group__http__client.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

HTTP client API

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

HTTP client API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [http\_response](structhttp__response.md) |
|  | HTTP response from the server. [More...](structhttp__response.md#details) |
| struct | [http\_client\_internal\_data](structhttp__client__internal__data.md) |
|  | HTTP client internal data that the application should not touch. [More...](structhttp__client__internal__data.md#details) |
| struct | [http\_request](structhttp__request.md) |
|  | HTTP client request. [More...](structhttp__request.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [http\_payload\_cb\_t](#gaf46ede77bdc83602c84b9342dd8d30ed)) (int sock, struct [http\_request](structhttp__request.md) \*req, void \*user\_data) |
|  | Callback used when data needs to be sent to the server. |
| typedef int(\* | [http\_header\_cb\_t](#ga34a431c54c52b86618ca0e27ce3862b4)) (int sock, struct [http\_request](structhttp__request.md) \*req, void \*user\_data) |
|  | Callback can be used if application wants to construct additional HTTP headers when the HTTP request is sent. |
| typedef void(\* | [http\_response\_cb\_t](#ga9e079c737c325ee21a57e615b641f21a)) (struct [http\_response](structhttp__response.md) \*rsp, enum [http\_final\_call](#ga04fc31de51404e35b3dfab6261bb8e6d) final\_data, void \*user\_data) |
|  | Callback used when data is received from the server. |

| Enumerations | |
| --- | --- |
| enum | [http\_final\_call](#ga04fc31de51404e35b3dfab6261bb8e6d) { [HTTP\_DATA\_MORE](#gga04fc31de51404e35b3dfab6261bb8e6da3f75fb095e40bfb4efd2c16059093359) = 0 , [HTTP\_DATA\_FINAL](#gga04fc31de51404e35b3dfab6261bb8e6da428633ff4a67c00c67fb5cbc23269d61) = 1 } |
|  | Is there more data to come. [More...](#ga04fc31de51404e35b3dfab6261bb8e6d) |

| Functions | |
| --- | --- |
| int | [http\_client\_req](#gaa38b6efb03f88d6959273a41b6acac81) (int sock, struct [http\_request](structhttp__request.md) \*req, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout, void \*user\_data) |
|  | Do a HTTP request. |

## Detailed Description

HTTP client API.

Since
:   2.1

Version
:   0.2.0

## Typedef Documentation

## [◆ ](#ga34a431c54c52b86618ca0e27ce3862b4)http\_header\_cb\_t

| typedef int(\* http\_header\_cb\_t) (int sock, struct [http\_request](structhttp__request.md) \*req, void \*user\_data) |
| --- |

`#include <[client.h](client_8h.md)>`

Callback can be used if application wants to construct additional HTTP headers when the HTTP request is sent.

Usage of this is optional.

Parameters
:   | sock | Socket id of the connection |
    | --- | --- |
    | req | HTTP request information |
    | user\_data | User specified data specified in [http\_client\_req()](#gaa38b6efb03f88d6959273a41b6acac81) |

Returns
:   >=0 amount of data sent, in this case [http\_client\_req()](#gaa38b6efb03f88d6959273a41b6acac81) should continue sending data, <0 if [http\_client\_req()](#gaa38b6efb03f88d6959273a41b6acac81) should return the error code to the caller.

## [◆ ](#gaf46ede77bdc83602c84b9342dd8d30ed)http\_payload\_cb\_t

| typedef int(\* http\_payload\_cb\_t) (int sock, struct [http\_request](structhttp__request.md) \*req, void \*user\_data) |
| --- |

`#include <[client.h](client_8h.md)>`

Callback used when data needs to be sent to the server.

Parameters
:   | sock | Socket id of the connection |
    | --- | --- |
    | req | HTTP request information |
    | user\_data | User specified data specified in [http\_client\_req()](#gaa38b6efb03f88d6959273a41b6acac81) |

Returns
:   >=0 amount of data sent, in this case [http\_client\_req()](#gaa38b6efb03f88d6959273a41b6acac81) should continue sending data, <0 if [http\_client\_req()](#gaa38b6efb03f88d6959273a41b6acac81) should return the error code to the caller.

## [◆ ](#ga9e079c737c325ee21a57e615b641f21a)http\_response\_cb\_t

| typedef void(\* http\_response\_cb\_t) (struct [http\_response](structhttp__response.md) \*rsp, enum [http\_final\_call](#ga04fc31de51404e35b3dfab6261bb8e6d) final\_data, void \*user\_data) |
| --- |

`#include <[client.h](client_8h.md)>`

Callback used when data is received from the server.

Parameters
:   | rsp | HTTP response information |
    | --- | --- |
    | final\_data | Does this data buffer contain all the data or is there still more data to come. |
    | user\_data | User specified data specified in [http\_client\_req()](#gaa38b6efb03f88d6959273a41b6acac81) |

## Enumeration Type Documentation

## [◆ ](#ga04fc31de51404e35b3dfab6261bb8e6d)http\_final\_call

| enum [http\_final\_call](#ga04fc31de51404e35b3dfab6261bb8e6d) |
| --- |

`#include <[client.h](client_8h.md)>`

Is there more data to come.

| Enumerator | |
| --- | --- |
| HTTP\_DATA\_MORE | More data will come. |
| HTTP\_DATA\_FINAL | End of data. |

## Function Documentation

## [◆ ](#gaa38b6efb03f88d6959273a41b6acac81)http\_client\_req()

| int http\_client\_req | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | struct [http\_request](structhttp__request.md) \* | *req*, |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout*, |
|  |  | void \* | *user\_data* ) |

`#include <[client.h](client_8h.md)>`

Do a HTTP request.

The callback is called when data is received from the HTTP server. The caller must have created a connection to the server before calling this function so [connect()](group__bsd__sockets.md#gadfa930dd3c38f6c287d64e1680dbf386 "POSIX wrapper for zsock_connect.") call must have be done successfully for the socket.

Parameters
:   | sock | Socket id of the connection. |
    | --- | --- |
    | req | HTTP request information |
    | timeout | Max timeout to wait for the data. The timeout value cannot be 0 as there would be no time to receive the data. The timeout value is in milliseconds. |
    | user\_data | User specified data that is passed to the callback. |

Returns
:   <0 if error, >=0 amount of data sent to the server

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
