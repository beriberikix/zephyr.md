---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structuart__event__tx.html
original_path: doxygen/html/structuart__event__tx.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_event\_tx Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [UART Interface](group__uart__interface.md) » [Async UART API](group__uart__async.md)

UART TX event data.
[More...](#details)

`#include <[uart.h](drivers_2uart_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [buf](#a314a676a4050b2438b6f41485656bdbd) |
|  | Pointer to current buffer. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [len](#a7d844b2c0833d24accf82d58ee3408ff) |
|  | Number of bytes sent. |

## Detailed Description

UART TX event data.

## Field Documentation

## [◆ ](#a314a676a4050b2438b6f41485656bdbd)buf

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* uart\_event\_tx::buf |
| --- |

Pointer to current buffer.

## [◆ ](#a7d844b2c0833d24accf82d58ee3408ff)len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) uart\_event\_tx::len |
| --- |

Number of bytes sent.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[uart.h](drivers_2uart_8h_source.md)

- [uart\_event\_tx](structuart__event__tx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
