---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structuart__event__rx__stop.html
original_path: doxygen/html/structuart__event__rx__stop.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_event\_rx\_stop Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [UART Interface](group__uart__interface.md) » [Async UART API](group__uart__async.md)

UART RX stopped data.
[More...](#details)

`#include <[uart.h](drivers_2uart_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [uart\_rx\_stop\_reason](group__uart__interface.md#gadeba6c5485e01dfc1c8a6e1c21668a88) | [reason](#a96fbae85208d9b3ea0382e7e236a932d) |
|  | Reason why receiving stopped. |
| struct [uart\_event\_rx](structuart__event__rx.md) | [data](#a1b361c8b7e17d1304a475235e734db48) |
|  | Last received data. |

## Detailed Description

UART RX stopped data.

## Field Documentation

## [◆ ](#a1b361c8b7e17d1304a475235e734db48)data

| struct [uart\_event\_rx](structuart__event__rx.md) uart\_event\_rx\_stop::data |
| --- |

Last received data.

## [◆ ](#a96fbae85208d9b3ea0382e7e236a932d)reason

| enum [uart\_rx\_stop\_reason](group__uart__interface.md#gadeba6c5485e01dfc1c8a6e1c21668a88) uart\_event\_rx\_stop::reason |
| --- |

Reason why receiving stopped.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[uart.h](drivers_2uart_8h_source.md)

- [uart\_event\_rx\_stop](structuart__event__rx__stop.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
