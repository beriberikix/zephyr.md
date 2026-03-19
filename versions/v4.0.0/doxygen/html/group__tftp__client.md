---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__tftp__client.html
original_path: doxygen/html/group__tftp__client.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

TFTP Client library

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

| Data Structures | |
| --- | --- |
| struct | [tftp\_data\_param](structtftp__data__param.md) |
|  | Parameters for data event. [More...](structtftp__data__param.md#details) |
| struct | [tftp\_error\_param](structtftp__error__param.md) |
|  | Parameters for error event. [More...](structtftp__error__param.md#details) |
| union | [tftp\_evt\_param](uniontftp__evt__param.md) |
|  | Defines event parameters notified along with asynchronous events to the application. [More...](uniontftp__evt__param.md#details) |
| struct | [tftp\_evt](structtftp__evt.md) |
|  | Defines TFTP asynchronous event notified to the application. [More...](structtftp__evt.md#details) |
| struct | [tftpc](structtftpc.md) |
|  | TFTP client definition to maintain information relevant to the client. [More...](structtftpc.md#details) |

| Macros | |
| --- | --- |
| #define | [TFTP\_BLOCK\_SIZE](#ga762c61f0d58a300c91f7577f65574dd5)   512 |
|  | RFC1350: the file is sent in fixed length blocks of 512 bytes. |
| #define | [TFTP\_HEADER\_SIZE](#ga0dbc6adc4cb9be4ea86fce61846c2089)   4 |
|  | RFC1350: For non-request TFTP message, the header contains 2-byte operation code plus 2-byte block number or error code. |
| #define | [TFTPC\_MAX\_BUF\_SIZE](#ga4387f92c6327823d655d8aa4f1c65beb)   ([TFTP\_BLOCK\_SIZE](#ga762c61f0d58a300c91f7577f65574dd5) + [TFTP\_HEADER\_SIZE](#ga0dbc6adc4cb9be4ea86fce61846c2089)) |
|  | Maximum amount of data that can be sent or received. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [tftp\_callback\_t](#gafc2d0fd730046b0d3781362263e68ddc)) (const struct [tftp\_evt](structtftp__evt.md) \*evt) |
|  | TFTP event notification callback registered by the application. |

| Enumerations | |
| --- | --- |
| enum | [tftp\_evt\_type](#ga1ee3d814c6fbaf5570eb5fd9605af7ea) { [TFTP\_EVT\_DATA](#gga1ee3d814c6fbaf5570eb5fd9605af7eaa7bd0226d62c9b49a8381705bc1d5875d) , [TFTP\_EVT\_ERROR](#gga1ee3d814c6fbaf5570eb5fd9605af7eaa317d58f986f6f2f65b44fdaa5b655eb3) } |
|  | TFTP Asynchronous Events notified to the application from the module through the callback registered by the application. [More...](#ga1ee3d814c6fbaf5570eb5fd9605af7ea) |

| Functions | |
| --- | --- |
| int | [tftp\_get](#ga067de19b4089fbd2c2e49e925b73cfb0) (struct [tftpc](structtftpc.md) \*client, const char \*remote\_file, const char \*mode) |
|  | This function gets data from a "file" on the remote server. |
| int | [tftp\_put](#ga692f6a51f2ecd5c3d673ff64f59294b9) (struct [tftpc](structtftpc.md) \*client, const char \*remote\_file, const char \*mode, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*user\_buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) user\_buf\_size) |
|  | This function puts data to a "file" on the remote server. |

| TFTP client error codes. | |
| --- | --- |
| #define | [TFTPC\_SUCCESS](#ga40d1c46aafbf6ea66daa5937ceb1152f)   0 |
|  | Success. |
| #define | [TFTPC\_DUPLICATE\_DATA](#gac8b5e1f02de73c8cd42849ea0229eed2)   -1 |
|  | Duplicate data received. |
| #define | [TFTPC\_BUFFER\_OVERFLOW](#ga5ac8121d18b8eceffe281281aca1b700)   -2 |
|  | User buffer is too small. |
| #define | [TFTPC\_UNKNOWN\_FAILURE](#ga30ad373e8531ba675165bb61620c9a07)   -3 |
|  | Unknown failure. |
| #define | [TFTPC\_REMOTE\_ERROR](#ga75729dcb0b640a6fcb2079151cd74f51)   -4 |
|  | Remote server error. |
| #define | [TFTPC\_RETRIES\_EXHAUSTED](#ga514eaf5d77587b8719801157adf20566)   -5 |
|  | Retries exhausted. |

## Detailed Description

Since
:   2.3

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga762c61f0d58a300c91f7577f65574dd5)TFTP\_BLOCK\_SIZE

| #define TFTP\_BLOCK\_SIZE   512 |
| --- |

`#include <[tftp.h](tftp_8h.md)>`

RFC1350: the file is sent in fixed length blocks of 512 bytes.

Each data packet contains one block of data, and must be acknowledged by an acknowledgment packet before the next packet can be sent. A data packet of less than 512 bytes signals termination of a transfer.

## [◆ ](#ga0dbc6adc4cb9be4ea86fce61846c2089)TFTP\_HEADER\_SIZE

| #define TFTP\_HEADER\_SIZE   4 |
| --- |

`#include <[tftp.h](tftp_8h.md)>`

RFC1350: For non-request TFTP message, the header contains 2-byte operation code plus 2-byte block number or error code.

## [◆ ](#ga5ac8121d18b8eceffe281281aca1b700)TFTPC\_BUFFER\_OVERFLOW

| #define TFTPC\_BUFFER\_OVERFLOW   -2 |
| --- |

`#include <[tftp.h](tftp_8h.md)>`

User buffer is too small.

## [◆ ](#gac8b5e1f02de73c8cd42849ea0229eed2)TFTPC\_DUPLICATE\_DATA

| #define TFTPC\_DUPLICATE\_DATA   -1 |
| --- |

`#include <[tftp.h](tftp_8h.md)>`

Duplicate data received.

## [◆ ](#ga4387f92c6327823d655d8aa4f1c65beb)TFTPC\_MAX\_BUF\_SIZE

| #define TFTPC\_MAX\_BUF\_SIZE   ([TFTP\_BLOCK\_SIZE](#ga762c61f0d58a300c91f7577f65574dd5) + [TFTP\_HEADER\_SIZE](#ga0dbc6adc4cb9be4ea86fce61846c2089)) |
| --- |

`#include <[tftp.h](tftp_8h.md)>`

Maximum amount of data that can be sent or received.

## [◆ ](#ga75729dcb0b640a6fcb2079151cd74f51)TFTPC\_REMOTE\_ERROR

| #define TFTPC\_REMOTE\_ERROR   -4 |
| --- |

`#include <[tftp.h](tftp_8h.md)>`

Remote server error.

## [◆ ](#ga514eaf5d77587b8719801157adf20566)TFTPC\_RETRIES\_EXHAUSTED

| #define TFTPC\_RETRIES\_EXHAUSTED   -5 |
| --- |

`#include <[tftp.h](tftp_8h.md)>`

Retries exhausted.

## [◆ ](#ga40d1c46aafbf6ea66daa5937ceb1152f)TFTPC\_SUCCESS

| #define TFTPC\_SUCCESS   0 |
| --- |

`#include <[tftp.h](tftp_8h.md)>`

Success.

## [◆ ](#ga30ad373e8531ba675165bb61620c9a07)TFTPC\_UNKNOWN\_FAILURE

| #define TFTPC\_UNKNOWN\_FAILURE   -3 |
| --- |

`#include <[tftp.h](tftp_8h.md)>`

Unknown failure.

## Typedef Documentation

## [◆ ](#gafc2d0fd730046b0d3781362263e68ddc)tftp\_callback\_t

| typedef void(\* tftp\_callback\_t) (const struct [tftp\_evt](structtftp__evt.md) \*evt) |
| --- |

`#include <[tftp.h](tftp_8h.md)>`

TFTP event notification callback registered by the application.

Parameters
:   | [in] | evt | Event description along with result and associated parameters (if any). |
    | --- | --- | --- |

## Enumeration Type Documentation

## [◆ ](#ga1ee3d814c6fbaf5570eb5fd9605af7ea)tftp\_evt\_type

| enum [tftp\_evt\_type](#ga1ee3d814c6fbaf5570eb5fd9605af7ea) |
| --- |

`#include <[tftp.h](tftp_8h.md)>`

TFTP Asynchronous Events notified to the application from the module through the callback registered by the application.

| Enumerator | |
| --- | --- |
| TFTP\_EVT\_DATA | DATA event when data is received from remote server.  Note  DATA event structure contains payload data and size. |
| TFTP\_EVT\_ERROR | ERROR event when error is received from remote server.  Note  ERROR event structure contains error code and message. |

## Function Documentation

## [◆ ](#ga067de19b4089fbd2c2e49e925b73cfb0)tftp\_get()

| int tftp\_get | ( | struct [tftpc](structtftpc.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | const char \* | *remote\_file*, |
|  |  | const char \* | *mode* ) |

`#include <[tftp.h](tftp_8h.md)>`

This function gets data from a "file" on the remote server.

Parameters
:   | client | Client information of type [tftpc](structtftpc.md "tftpc"). |
    | --- | --- |
    | remote\_file | Name of the remote file to get. |
    | mode | TFTP Client "mode" setting. |

Return values
:   | The | size of data being received if the operation completed successfully. |
    | --- | --- |
    | [TFTPC\_BUFFER\_OVERFLOW](#ga5ac8121d18b8eceffe281281aca1b700) | if the file is larger than the user buffer. |
    | [TFTPC\_REMOTE\_ERROR](#ga75729dcb0b640a6fcb2079151cd74f51) | if the server failed to process our request. |
    | [TFTPC\_RETRIES\_EXHAUSTED](#ga514eaf5d77587b8719801157adf20566) | if the client timed out waiting for server. |
    | -EINVAL | if client is NULL. |

Note
:   This function blocks until the transfer is completed or network error happens. The integrity of the client structure must be ensured until the function returns.

## [◆ ](#ga692f6a51f2ecd5c3d673ff64f59294b9)tftp\_put()

| int tftp\_put | ( | struct [tftpc](structtftpc.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | const char \* | *remote\_file*, |
|  |  | const char \* | *mode*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *user\_buf*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *user\_buf\_size* ) |

`#include <[tftp.h](tftp_8h.md)>`

This function puts data to a "file" on the remote server.

Parameters
:   | client | Client information of type [tftpc](structtftpc.md "tftpc"). |
    | --- | --- |
    | remote\_file | Name of the remote file to put. |
    | mode | TFTP Client "mode" setting. |
    | user\_buf | Data buffer containing the data to put. |
    | user\_buf\_size | Length of the data to put. |

Return values
:   | The | size of data being sent if the operation completed successfully. |
    | --- | --- |
    | [TFTPC\_REMOTE\_ERROR](#ga75729dcb0b640a6fcb2079151cd74f51) | if the server failed to process our request. |
    | [TFTPC\_RETRIES\_EXHAUSTED](#ga514eaf5d77587b8719801157adf20566) | if the client timed out waiting for server. |
    | -EINVAL | if client or user\_buf is NULL or if user\_buf\_size is zero. |

Note
:   This function blocks until the transfer is completed or network error happens. The integrity of the client structure must be ensured until the function returns.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
