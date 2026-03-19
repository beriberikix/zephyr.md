---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/uart__mcumgr_8h.html
original_path: doxygen/html/uart__mcumgr_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_mcumgr.h File Reference

A driver for sending and receiving mcumgr packets over UART.
[More...](#details)

`#include <[stdlib.h](stdlib_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](uart__mcumgr_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [uart\_mcumgr\_rx\_buf](structuart__mcumgr__rx__buf.md) |
|  | Contains an mcumgr fragment received over UART. [More...](structuart__mcumgr__rx__buf.md#details) |

| Typedefs | |
| --- | --- |
| typedef void | [uart\_mcumgr\_recv\_fn](#a0173a370be3e424b56cdfbb3d4174da1)(struct [uart\_mcumgr\_rx\_buf](structuart__mcumgr__rx__buf.md) \*rx\_buf) |
|  | Function that gets called when an mcumgr packet is received. |

| Functions | |
| --- | --- |
| int | [uart\_mcumgr\_send](#acf906a316bf77fc5cc8768130ce82e66) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, int len) |
|  | Sends an mcumgr packet over UART. |
| void | [uart\_mcumgr\_free\_rx\_buf](#ae173ad28a0301c8ddfdd9b8bc5583ba3) (struct [uart\_mcumgr\_rx\_buf](structuart__mcumgr__rx__buf.md) \*rx\_buf) |
|  | Frees the supplied receive buffer. |
| void | [uart\_mcumgr\_register](#a2b31278c4e600bcd10d1a069cc6f5655) ([uart\_mcumgr\_recv\_fn](#a0173a370be3e424b56cdfbb3d4174da1) \*cb) |
|  | Registers an mcumgr UART receive handler. |

## Detailed Description

A driver for sending and receiving mcumgr packets over UART.

See also
:   include/mgmt/serial.h

## Typedef Documentation

## [◆ ](#a0173a370be3e424b56cdfbb3d4174da1)uart\_mcumgr\_recv\_fn

| typedef void uart\_mcumgr\_recv\_fn(struct [uart\_mcumgr\_rx\_buf](structuart__mcumgr__rx__buf.md) \*rx\_buf) |
| --- |

Function that gets called when an mcumgr packet is received.

Function that gets called when an mcumgr packet is received. This function gets called in the interrupt context. Ownership of the specified buffer is transferred to the callback when this function gets called.

Parameters
:   | rx\_buf | A buffer containing the incoming mcumgr packet. |
    | --- | --- |

## Function Documentation

## [◆ ](#ae173ad28a0301c8ddfdd9b8bc5583ba3)uart\_mcumgr\_free\_rx\_buf()

| void uart\_mcumgr\_free\_rx\_buf | ( | struct [uart\_mcumgr\_rx\_buf](structuart__mcumgr__rx__buf.md) \* | *rx\_buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

Frees the supplied receive buffer.

Parameters
:   | rx\_buf | The buffer to free. |
    | --- | --- |

## [◆ ](#a2b31278c4e600bcd10d1a069cc6f5655)uart\_mcumgr\_register()

| void uart\_mcumgr\_register | ( | [uart\_mcumgr\_recv\_fn](#a0173a370be3e424b56cdfbb3d4174da1) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

Registers an mcumgr UART receive handler.

Configures the mcumgr UART driver to call the specified function when an mcumgr request packet is received.

Parameters
:   | cb | The callback to execute when an mcumgr request packet is received. |
    | --- | --- |

## [◆ ](#acf906a316bf77fc5cc8768130ce82e66)uart\_mcumgr\_send()

| int uart\_mcumgr\_send | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
| --- | --- | --- | --- |
|  |  | int | *len* ) |

Sends an mcumgr packet over UART.

Parameters
:   | data | Buffer containing the mcumgr packet to send. |
    | --- | --- |
    | len | The length of the buffer, in bytes. |

Returns
:   0 on success; negative error code on failure.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [console](dir_5678202c8994e72aafde82bf91697a82.md)
- [uart\_mcumgr.h](uart__mcumgr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
