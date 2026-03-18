---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structuart__mux__driver__api.html
original_path: doxygen/html/structuart__mux__driver__api.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_mux\_driver\_api Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [UART Mux Interface](group__uart__mux__interface.md)

UART mux driver API structure.
[More...](#details)

`#include <[uart_mux.h](uart__mux_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct uart\_driver\_api | [uart\_api](#a600ea39ef3bcfcd8949ab3f38c8a454c) |
|  | The uart\_driver\_api must be placed in first position in this struct so that we are compatible with uart API. |
| int(\* | [attach](#a312a7c8724c885d9f8fdcd9434ce44c2) )(const struct [device](structdevice.md) \*mux, const struct [device](structdevice.md) \*uart, int dlci\_address, [uart\_mux\_attach\_cb\_t](group__uart__mux__interface.md#ga9796bc90e4feca3b7e775e1107b74cf3) cb, void \*user\_data) |
|  | Attach the mux to this UART. |

## Detailed Description

UART mux driver API structure.

## Field Documentation

## [◆ ](#a312a7c8724c885d9f8fdcd9434ce44c2)attach

| int(\* uart\_mux\_driver\_api::attach) (const struct [device](structdevice.md) \*mux, const struct [device](structdevice.md) \*uart, int dlci\_address, [uart\_mux\_attach\_cb\_t](group__uart__mux__interface.md#ga9796bc90e4feca3b7e775e1107b74cf3) cb, void \*user\_data) |
| --- |

Attach the mux to this UART.

The API will call the callback after the DLCI is created or not.

## [◆ ](#a600ea39ef3bcfcd8949ab3f38c8a454c)uart\_api

| struct uart\_driver\_api uart\_mux\_driver\_api::uart\_api |
| --- |

The uart\_driver\_api must be placed in first position in this struct so that we are compatible with uart API.

Note that currently not all of the UART API functions are implemented.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/console/[uart\_mux.h](uart__mux_8h_source.md)

- [uart\_mux\_driver\_api](structuart__mux__driver__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
