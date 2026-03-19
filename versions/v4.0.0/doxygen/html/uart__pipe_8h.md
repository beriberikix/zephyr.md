---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/uart__pipe_8h.html
original_path: doxygen/html/uart__pipe_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_pipe.h File Reference

Pipe UART driver header file.
[More...](#details)

`#include <[stdlib.h](stdlib_8h_source.md)>`

[Go to the source code of this file.](uart__pipe_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*(\* | [uart\_pipe\_recv\_cb](#a8a840645edad0e2ac3da6cfd6f09557f)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*[off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)) |
|  | Received data callback. |

| Functions | |
| --- | --- |
| void | [uart\_pipe\_register](#a0ddac401c01681a22952ae792007b786) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [uart\_pipe\_recv\_cb](#a8a840645edad0e2ac3da6cfd6f09557f) cb) |
|  | Register UART application. |
| int | [uart\_pipe\_send](#a6136cfc4837939fd56243245f462cc0e) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, int len) |
|  | Send data over UART. |

## Detailed Description

Pipe UART driver header file.

A pipe UART driver that allows applications to handle all aspects of received protocol data.

## Typedef Documentation

## [◆ ](#a8a840645edad0e2ac3da6cfd6f09557f)uart\_pipe\_recv\_cb

| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*(\* uart\_pipe\_recv\_cb) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*[off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)) |
| --- |

Received data callback.

This function is called when new data is received on UART. The off parameter can be used to alter offset at which received data is stored. Typically, when the complete data is received and a new buffer is provided off should be set to 0.

Parameters
:   | buf | Buffer with received data. |
    | --- | --- |
    | [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) | Data offset on next received and accumulated data length. |

Returns
:   Buffer to be used on next receive.

## Function Documentation

## [◆ ](#a0ddac401c01681a22952ae792007b786)uart\_pipe\_register()

| void uart\_pipe\_register | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | [uart\_pipe\_recv\_cb](#a8a840645edad0e2ac3da6cfd6f09557f) | *cb* ) |

Register UART application.

This function is used to register new UART application.

Parameters
:   | buf | Initial buffer for received data. |
    | --- | --- |
    | len | Size of buffer. |
    | cb | Callback to be called on data reception. |

## [◆ ](#a6136cfc4837939fd56243245f462cc0e)uart\_pipe\_send()

| int uart\_pipe\_send | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
| --- | --- | --- | --- |
|  |  | int | *len* ) |

Send data over UART.

This function is used to send data over UART.

Parameters
:   | data | Buffer with data to be send. |
    | --- | --- |
    | len | Size of data. |

Returns
:   0 on success or negative error

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [uart\_pipe.h](uart__pipe_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
