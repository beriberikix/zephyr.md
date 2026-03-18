---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structuart__event__rx__buf.html
original_path: doxygen/html/structuart__event__rx__buf.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_event\_rx\_buf Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [UART Interface](group__uart__interface.md) » [Async UART API](group__uart__async.md)

UART RX buffer released event data.
[More...](#details)

`#include <[uart.h](drivers_2uart_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [buf](#a2547c84b742f454cfedf1de6d433297b) |
|  | Pointer to buffer that is no longer in use. |

## Detailed Description

UART RX buffer released event data.

## Field Documentation

## [◆ ](#a2547c84b742f454cfedf1de6d433297b)buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* uart\_event\_rx\_buf::buf |
| --- |

Pointer to buffer that is no longer in use.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[uart.h](drivers_2uart_8h_source.md)

- [uart\_event\_rx\_buf](structuart__event__rx__buf.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
