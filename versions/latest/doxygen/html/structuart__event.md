---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structuart__event.html
original_path: doxygen/html/structuart__event.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_event Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [UART Interface](group__uart__interface.md) » [Async UART API](group__uart__async.md)

Structure containing information about current event.
[More...](#details)

`#include <[uart.h](drivers_2uart_8h_source.md)>`

| Data Structures | |
| --- | --- |
| union | [uart\_event\_data](unionuart__event_1_1uart__event__data.md) |
|  | Event data. [More...](unionuart__event_1_1uart__event__data.md#details) |

| Data Fields | |
| --- | --- |
| enum [uart\_event\_type](group__uart__async.md#gaf0c9513cbafa36d86b4c83f2b6a03dcd) | [type](#a2fb82a30e414a74943067cd0784f4b44) |
|  | Type of event. |
| union [uart\_event::uart\_event\_data](unionuart__event_1_1uart__event__data.md) | [data](#a07e3eebb7642ab52c73baba514704c69) |

## Detailed Description

Structure containing information about current event.

## Field Documentation

## [◆ ](#a07e3eebb7642ab52c73baba514704c69)data

| union [uart\_event::uart\_event\_data](unionuart__event_1_1uart__event__data.md) uart\_event::data |
| --- |

## [◆ ](#a2fb82a30e414a74943067cd0784f4b44)type

| enum [uart\_event\_type](group__uart__async.md#gaf0c9513cbafa36d86b4c83f2b6a03dcd) uart\_event::type |
| --- |

Type of event.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[uart.h](drivers_2uart_8h_source.md)

- [uart\_event](structuart__event.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
