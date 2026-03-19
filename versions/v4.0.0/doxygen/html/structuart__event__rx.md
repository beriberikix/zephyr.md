---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structuart__event__rx.html
original_path: doxygen/html/structuart__event__rx.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_event\_rx Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [UART Interface](group__uart__interface.md) » [Async UART API](group__uart__async.md)

UART RX event data.
[More...](#details)

`#include <[uart.h](drivers_2uart_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [buf](#a2d9dfa9d9b25ff976cf2e937c72eb245) |
|  | Pointer to current buffer. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [offset](#aa483e719298c30b9f5e6c57d3d161281) |
|  | Currently received data offset in bytes. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [len](#a96414b96e63503336f8cf0d2249cd3bd) |
|  | Number of new bytes received. |

## Detailed Description

UART RX event data.

The data represented by the event is stored in rx.buf[rx.offset] to rx.buf[rx.offset+rx.len]. That is, the length is relative to the offset.

## Field Documentation

## [◆ ](#a2d9dfa9d9b25ff976cf2e937c72eb245)buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* uart\_event\_rx::buf |
| --- |

Pointer to current buffer.

## [◆ ](#a96414b96e63503336f8cf0d2249cd3bd)len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) uart\_event\_rx::len |
| --- |

Number of new bytes received.

## [◆ ](#aa483e719298c30b9f5e6c57d3d161281)offset

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) uart\_event\_rx::offset |
| --- |

Currently received data offset in bytes.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[uart.h](drivers_2uart_8h_source.md)

- [uart\_event\_rx](structuart__event__rx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
