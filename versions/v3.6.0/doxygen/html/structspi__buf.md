---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structspi__buf.html
original_path: doxygen/html/structspi__buf.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spi\_buf Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [SPI Interface](group__spi__interface.md)

SPI buffer structure.
[More...](#details)

`#include <[spi.h](drivers_2spi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [buf](#aeaf52d3ff5af10545b2d6904ed452cba) |
|  | Valid pointer to a data buffer, or NULL otherwise. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [len](#a9755deadff0dd01a886f22e41099b8ba) |
|  | Length of the buffer *buf*. |

## Detailed Description

SPI buffer structure.

## Field Documentation

## [◆ ](#aeaf52d3ff5af10545b2d6904ed452cba)buf

| void\* spi\_buf::buf |
| --- |

Valid pointer to a data buffer, or NULL otherwise.

## [◆ ](#a9755deadff0dd01a886f22e41099b8ba)len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) spi\_buf::len |
| --- |

Length of the buffer *buf*.

If *buf* is NULL, length which as to be sent as dummy bytes (as TX buffer) or the length of bytes that should be skipped (as RX buffer).

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[spi.h](drivers_2spi_8h_source.md)

- [spi\_buf](structspi__buf.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
