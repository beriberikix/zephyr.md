---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/tftp_8h.html
original_path: doxygen/html/tftp_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tftp.h File Reference

`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/net/socket.h](net_2socket_8h_source.md)>`

[Go to the source code of this file.](tftp_8h_source.md)

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
| #define | [TFTP\_BLOCK\_SIZE](group__tftp__client.md#ga762c61f0d58a300c91f7577f65574dd5)   512 |
|  | RFC1350: the file is sent in fixed length blocks of 512 bytes. |
| #define | [TFTP\_HEADER\_SIZE](group__tftp__client.md#ga0dbc6adc4cb9be4ea86fce61846c2089)   4 |
|  | RFC1350: For non-request TFTP message, the header contains 2-byte operation code plus 2-byte block number or error code. |
| #define | [TFTPC\_MAX\_BUF\_SIZE](group__tftp__client.md#ga4387f92c6327823d655d8aa4f1c65beb)   ([TFTP\_BLOCK\_SIZE](group__tftp__client.md#ga762c61f0d58a300c91f7577f65574dd5) + [TFTP\_HEADER\_SIZE](group__tftp__client.md#ga0dbc6adc4cb9be4ea86fce61846c2089)) |
|  | Maximum amount of data that can be sent or received. |
| TFTP client error codes. | |
| #define | [TFTPC\_SUCCESS](group__tftp__client.md#ga40d1c46aafbf6ea66daa5937ceb1152f)   0 |
|  | Success. |
| #define | [TFTPC\_DUPLICATE\_DATA](group__tftp__client.md#gac8b5e1f02de73c8cd42849ea0229eed2)   -1 |
|  | Duplicate data received. |
| #define | [TFTPC\_BUFFER\_OVERFLOW](group__tftp__client.md#ga5ac8121d18b8eceffe281281aca1b700)   -2 |
|  | User buffer is too small. |
| #define | [TFTPC\_UNKNOWN\_FAILURE](group__tftp__client.md#ga30ad373e8531ba675165bb61620c9a07)   -3 |
|  | Unknown failure. |
| #define | [TFTPC\_REMOTE\_ERROR](group__tftp__client.md#ga75729dcb0b640a6fcb2079151cd74f51)   -4 |
|  | Remote server error. |
| #define | [TFTPC\_RETRIES\_EXHAUSTED](group__tftp__client.md#ga514eaf5d77587b8719801157adf20566)   -5 |
|  | Retries exhausted. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [tftp\_callback\_t](group__tftp__client.md#gafc2d0fd730046b0d3781362263e68ddc)) (const struct [tftp\_evt](structtftp__evt.md) \*evt) |
|  | TFTP event notification callback registered by the application. |

| Enumerations | |
| --- | --- |
| enum | [tftp\_evt\_type](group__tftp__client.md#ga1ee3d814c6fbaf5570eb5fd9605af7ea) { [TFTP\_EVT\_DATA](group__tftp__client.md#gga1ee3d814c6fbaf5570eb5fd9605af7eaa7bd0226d62c9b49a8381705bc1d5875d) , [TFTP\_EVT\_ERROR](group__tftp__client.md#gga1ee3d814c6fbaf5570eb5fd9605af7eaa317d58f986f6f2f65b44fdaa5b655eb3) } |
|  | TFTP Asynchronous Events notified to the application from the module through the callback registered by the application. [More...](group__tftp__client.md#ga1ee3d814c6fbaf5570eb5fd9605af7ea) |

| Functions | |
| --- | --- |
| int | [tftp\_get](group__tftp__client.md#ga067de19b4089fbd2c2e49e925b73cfb0) (struct [tftpc](structtftpc.md) \*client, const char \*remote\_file, const char \*mode) |
|  | This function gets data from a "file" on the remote server. |
| int | [tftp\_put](group__tftp__client.md#ga692f6a51f2ecd5c3d673ff64f59294b9) (struct [tftpc](structtftpc.md) \*client, const char \*remote\_file, const char \*mode, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*user\_buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) user\_buf\_size) |
|  | This function puts data to a "file" on the remote server. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [tftp.h](tftp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
