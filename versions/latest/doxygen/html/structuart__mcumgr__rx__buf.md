---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structuart__mcumgr__rx__buf.html
original_path: doxygen/html/structuart__mcumgr__rx__buf.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_mcumgr\_rx\_buf Struct Reference

Contains an mcumgr fragment received over UART.
[More...](#details)

`#include <[uart_mcumgr.h](uart__mcumgr_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [fifo\_reserved](#a8484b842ce240d35dff22f704617d22d) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data](#a81696c833e2955e6888fcd439a59f786) [CONFIG\_UART\_MCUMGR\_RX\_BUF\_SIZE] |
| int | [length](#a6495e78b7f249c6b073c4b0e1c25160a) |

## Detailed Description

Contains an mcumgr fragment received over UART.

## Field Documentation

## [◆ ](#a81696c833e2955e6888fcd439a59f786)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uart\_mcumgr\_rx\_buf::data[CONFIG\_UART\_MCUMGR\_RX\_BUF\_SIZE] |
| --- |

## [◆ ](#a8484b842ce240d35dff22f704617d22d)fifo\_reserved

| void\* uart\_mcumgr\_rx\_buf::fifo\_reserved |
| --- |

## [◆ ](#a6495e78b7f249c6b073c4b0e1c25160a)length

| int uart\_mcumgr\_rx\_buf::length |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/console/[uart\_mcumgr.h](uart__mcumgr_8h_source.md)

- [uart\_mcumgr\_rx\_buf](structuart__mcumgr__rx__buf.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
