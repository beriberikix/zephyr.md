---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structspi__buf.html
original_path: doxygen/html/structspi__buf.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spi\_buf Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [SPI Interface](group__spi__interface.md)

SPI buffer structure.
[More...](#details)

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [buf](#aeaf52d3ff5af10545b2d6904ed452cba) |
|  | Valid pointer to a data buffer, or NULL for NOP indication. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [len](#a9755deadff0dd01a886f22e41099b8ba) |
|  | Length of the buffer *buf* in bytes, or length of NOP. |

## Detailed Description

SPI buffer structure.

A SPI buffer describes either a real data buffer or an indication of NOP For a NOP indicator: If buffer is used for TX, only 0's will be sent for the length on the bus If buffer is used for RX, that length of data received by bus will be ignored/skipped

## Field Documentation

## [◆ ](#aeaf52d3ff5af10545b2d6904ed452cba)buf

| void\* spi\_buf::buf |
| --- |

Valid pointer to a data buffer, or NULL for NOP indication.

## [◆ ](#a9755deadff0dd01a886f22e41099b8ba)len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) spi\_buf::len |
| --- |

Length of the buffer *buf* in bytes, or length of NOP.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[spi.h](drivers_2spi_8h_source.md)

- [spi\_buf](structspi__buf.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
